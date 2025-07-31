import os

project_name = "asciidoctor-openapi"

files = {
    "Gemfile": """source 'https://rubygems.org'

gem 'asciidoctor'
gem 'asciidoctor-extensions'
gem 'yaml'
gem 'json'""",

    "README.md": """# Asciidoctor OpenAPI Macro

This Asciidoctor extension allows you to embed OpenAPI endpoint documentation directly into your AsciiDoc documents.

## Usage

```adoc
openapi::[path=/users, method=GET, spec=openapi.yaml]
```

## Features
- Extracts endpoint descriptions, parameters, and responses from an OpenAPI YAML file
- Keeps documentation DRY by pulling from your spec

## Run It

```bash
asciidoctor -r ./lib/asciidoctor-openapi.rb openapi-test.adoc
```

## License
MIT
""",

    "openapi-test.adoc": """= OpenAPI Test

openapi::[path=/users, method=GET, spec=openapi.yaml]""",

    "openapi.yaml": """openapi: 3.0.0
info:
  title: Sample API
  version: 1.0.0
paths:
  /users:
    get:
      summary: Get users
      description: Retrieve a list of users.
      parameters:
        - name: limit
          in: query
          description: Max number of users
          required: false
          schema:
            type: integer
      responses:
        "200":
          description: A list of users
""",

    "lib/asciidoctor-openapi.rb": """require_relative 'asciidoctor/openapi/extension'

Asciidoctor::Extensions.register do
  OpenAPI::Extension.register(self)
end""",

    "lib/asciidoctor/openapi/extension.rb": """require 'asciidoctor'
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

      create_block(parent, :listing, lines.join("\n"), { language: 'markdown' })
    end
  end

  module Extension
    def self.register(registry)
      registry.block_macro Macro
    end
  end
end"""
}

def scaffold():
    print(f"\nScaffolding project: {project_name}\n")
    for path, content in files.items():
        full_path = os.path.join(project_name, path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w") as f:
            f.write(content)
            print(f"[+] Created {full_path}")

    print("\n✅ All files created successfully.")

if __name__ == "__main__":
    scaffold()


