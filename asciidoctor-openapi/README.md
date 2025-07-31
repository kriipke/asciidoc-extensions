# Asciidoctor OpenAPI Macro

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
