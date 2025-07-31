require_relative 'asciidoctor/openapi/extension'

Asciidoctor::Extensions.register do
  OpenAPI::Extension.register(self)
end