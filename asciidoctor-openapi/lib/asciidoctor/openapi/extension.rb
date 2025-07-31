require 'asciidoctor'
require 'asciidoctor/extensions'
require 'yaml'
require 'json'

module OpenAPI
  class Macro < Asciidoctor::Extensions::BlockMacroProcessor
    use_dsl
    named :openapi

    def process(parent, target, attrs)
      spec_path = attrs['spec'] || 'openapi.yaml'
      path = attrs['path']
      method = attrs['method']&.downcase

      return create_block(parent, :paragraph, ["⚠️ Missing path or method"]) unless path && method
      return create_block(parent, :paragraph, ["⚠️ Spec not found: #{spec_path}"]) unless File.exist?(spec_path)

      spec = YAML.load_file(spec_path)
      operation = spec.dig('paths', path, method)

      return create_block(parent, :paragraph, ["⚠️ Operation not found for #{method.upcase} #{path}"]) unless operation

      lines = []
      lines << "*Summary:* #{operation['summary']}" if operation['summary']
      lines << "*Description:* #{operation['description']}" if operation['description']
      lines << ""
      lines << "*Parameters:*"
      (operation['parameters'] || []).each do |param|
        lines << "- `#{param['name']}` (#{param['in']}): #{param['description']}"
      end
      lines << ""
      lines << "*Responses:*"
      (operation['responses'] || {}).each do |code, resp|
        lines << "- `#{code}`: #{resp['description']}"
      end

      create_block(parent, :listing, lines.join("
"), { language: 'markdown' })
    end
  end

  module Extension
    def self.register(registry)
      registry.block_macro Macro
    end
  end
end