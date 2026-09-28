#!/usr/bin/env ruby
# Validate this catalog against vendor/okf/SPEC.md (OKF 0.2) and its domain conventions.
# Link integrity, index coverage, and domain fields are repository checks, not OKF
# conformance requirements. This is not a general-purpose OKF validator.
require 'yaml'
require 'pathname'
require 'date'

root = Pathname.new(ARGV.fetch(0, File.expand_path('../catalog', __dir__))).expand_path
errors = []
documents = {}
metadata = {}
fail_check = ->(path, message) { errors << "#{path.relative_path_from(root)}: #{message}" }

root.glob('**/*.md').sort.each do |path|
  text = path.read(encoding: 'UTF-8')
  unless text.valid_encoding?
    fail_check.call(path, 'invalid UTF-8')
    next
  end
  frontmatter = text.match(/\A---\r?\n(.*?)\r?\n---(?:\r?\n|\z)/m)
  data = {}
  if frontmatter
    begin
      data = YAML.safe_load(frontmatter[1], permitted_classes: [Date, Time])
      raise 'frontmatter must be a mapping' unless data.is_a?(Hash)
    rescue StandardError => e
      fail_check.call(path, "invalid YAML: #{e.message}")
      next
    end
  end
  body = frontmatter ? text[frontmatter.end(0)..-1] : text
  documents[path] = body
  metadata[path] = data
  case path.basename.to_s
  when 'index.md'
    if path == root.join('index.md')
      fail_check.call(path, 'root index must declare only okf_version: "0.2"') unless data == { 'okf_version' => '0.2' }
    elsif frontmatter
      fail_check.call(path, 'nested index cannot contain frontmatter')
    end
  when 'log.md'
    fail_check.call(path, 'log cannot contain frontmatter') if frontmatter
    body.scan(/^## (.+)$/).flatten.each do |heading|
      begin
        raise 'invalid date' unless heading.match?(/\A\d{4}-\d{2}-\d{2}\z/)
        Date.iso8601(heading)
      rescue ArgumentError, RuntimeError
        fail_check.call(path, "invalid log date #{heading}")
      end
    end
  else
    %w[type title description].each do |key|
      fail_check.call(path, "missing non-empty #{key}") unless data[key].is_a?(String) && !data[key].strip.empty?
    end
    fail_check.call(path, 'catalog_version must be v0.1.0 during baseline hold') unless data['catalog_version'] == 'v0.1.0'
    if data.key?('status') && !%w[draft stable deprecated].include?(data['status'])
      fail_check.call(path, 'invalid OKF lifecycle status')
    end
  end
end

errors << 'index.md: missing bundle entry point' unless documents.key?(root.join('index.md'))

resolve = lambda do |path, target|
  local = target.start_with?('/') ? root.join(target.delete_prefix('/')) : path.dirname.join(target)
  local.cleanpath
end
links = {}
documents.each do |path, body|
  # Fenced examples contain literal sample references, not navigation links.
  prose = body.gsub(/^```.*?^```[^\n]*$/m, '')
  links[path] = prose.scan(/\[[^\]]*\]\(([^)\s]+)\)/).flatten
  links[path].each do |target|
    next if target.match?(/\A[a-z][a-z0-9+.-]*:/i)
    file, anchor = target.split('#', 2)
    dest = file.empty? ? path : resolve.call(path, file)
    unless dest.to_s.start_with?(root.to_s + '/') && dest.exist?
      fail_check.call(path, "missing or out-of-bundle link #{target}")
      next
    end
    next unless anchor
    headings = documents.fetch(dest, '').scan(/^\#{1,6}\s+(.+)$/).flatten.map do |heading|
      heading.downcase.gsub(/[^\p{L}\p{N}_\- ]/, '').tr(' ', '-')
    end
    fail_check.call(path, "missing heading #{target}") unless headings.include?(anchor)
  end
end

documents.keys.map(&:dirname).uniq.each do |directory|
  index = directory.join('index.md')
  unless documents.key?(index)
    fail_check.call(index, 'missing directory index')
    next
  end
  targets = links.fetch(index, []).map { |link| resolve.call(index, link.split('#').first) }
  directory.children.each do |child|
    next if child.basename.to_s == 'index.md'
    expected = child.directory? ? child.join('index.md') : child
    next unless expected.extname == '.md'
    unless targets.include?(expected) || (child.directory? && targets.include?(child))
      fail_check.call(index, "unlisted entry #{child.basename}")
    end
  end
end

vocabulary = lambda do |filename|
  documents.fetch(root.join(filename), '').scan(/^\|[^|]+\| `([^`]+)` \|/).flatten
end
families = vocabulary.call('control-families.md')
work_types = vocabulary.call('work-types.md')
metadata.each do |path, data|
  case data['type']
  when 'Control'
    fail_check.call(path, 'unknown family') unless families.include?(data['family'])
    ['Purpose and applicability', 'Requirement', 'Implementation', 'Expected outcome and assessment', 'Dependencies and limitations'].each do |heading|
      fail_check.call(path, "missing section #{heading}") unless documents[path].include?("## #{heading}\n")
    end
  when 'Factory Example'
    fail_check.call(path, 'example must be true') unless data['example'] == true
    fail_check.call(path, 'missing domain') unless data['domain'].is_a?(String) && !data['domain'].strip.empty?
    types = data['work_types']
    unless types.is_a?(Array) && !types.empty? && (types - work_types).empty?
      fail_check.call(path, 'missing or unknown work types')
    end
    selections = data['control_selections']
    unless selections.is_a?(Array) && !selections.empty?
      fail_check.call(path, 'missing control selections')
      next
    end
    selections.each do |selection|
      unless selection.is_a?(Hash) && selection['control'].is_a?(String)
        fail_check.call(path, 'invalid control selection')
        next
      end
      dest = resolve.call(path, selection['control'])
      fail_check.call(path, "selection does not reference a Control: #{selection['control']}") unless metadata.fetch(dest, {})['type'] == 'Control'
      { 'applicability' => %w[applicable not-applicable undetermined],
        'implementation_state' => %w[not-planned proposed implemented retired],
        'assessment_result' => %w[not-assessed pass fail inconclusive] }.each do |key, values|
        fail_check.call(path, "invalid #{key}") unless values.include?(selection[key])
      end
    end
  end
end

if errors.empty?
  puts "PASS: #{documents.length} Markdown files; OKF structure, catalog metadata, local links, and index coverage."
else
  warn errors.join("\n")
  exit 1
end
