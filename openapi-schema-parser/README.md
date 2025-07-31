# Asciidoctor OpenAPI Macro

This is a custom Asciidoctor extension that lets you embed **OpenAPI (Swagger) endpoint documentation** directly in your AsciiDoc files using a simple macro syntax.

## ✨ What It Does

With this extension, you can extract and display structured documentation for specific API endpoints from an OpenAPI YAML file:

```adoc
openapi::[path=/users, method=GET, spec=openapi.yaml]
````

This renders a formatted summary of the endpoint, including:

* Summary and description
* Parameters (query/path/header/body)
* Response codes and descriptions

The content is parsed from your OpenAPI spec and injected as part of your AsciiDoc-to-HTML or PDF output.

---

## 🧠 Why Use It?

Writing and maintaining API docs manually is tedious and error-prone. This extension allows you to:

* **Document APIs once** in your OpenAPI file and reuse the source of truth
* **Embed only what’s needed** — great for guides, SDK docs, or tutorials
* **Avoid duplication** across AsciiDoc and OpenAPI specs
* **Generate static docs** that stay in sync with your spec

---

## 📦 Installation

Clone this repo and use it with the Asciidoctor CLI:

```bash
git clone https://github.com/your-org/asciidoctor-openapi
cd asciidoctor-openapi
bundle install  # optional if using Bundler
```

Then render your AsciiDoc like this:

```bash
asciidoctor -r ./lib/asciidoctor-openapi.rb your-doc.adoc
```

---

## 📄 Usage

### AsciiDoc Syntax

```adoc
openapi::[path=/your-endpoint, method=GET, spec=path/to/openapi.yaml]
```

### Attributes

| Attribute | Required | Description                                              |
| --------- | -------- | -------------------------------------------------------- |
| `path`    | ✅        | The OpenAPI path to look up (e.g. `/users`)              |
| `method`  | ✅        | The HTTP method (GET, POST, etc.)                        |
| `spec`    | ❌        | Path to your OpenAPI YAML file (default: `openapi.yaml`) |

---

## 🧪 Example

Given this OpenAPI spec:

```yaml
paths:
  /users:
    get:
      summary: List users
      description: Returns all users.
      parameters:
        - name: limit
          in: query
          description: Max number of users to return
      responses:
        "200":
          description: A list of users
```

The following macro:

```adoc
openapi::[path=/users, method=GET]
```

Will render:

```
*Summary:* List users
*Description:* Returns all users.

*Parameters:*
- `limit` (query): Max number of users to return

*Responses:*
- `200`: A list of users
```

---

## 🛠️ Roadmap Ideas

* Support for JSON specs
* Render HTML tables instead of plain lists
* Link `$ref` schemas to components
* Add filtering for specific response codes or tags

---

## 🧑‍💻 Who Should Use This?

This tool is perfect for:

* API publishers writing dev guides in AsciiDoc
* DevRel teams maintaining tutorials
* Product teams generating human-readable docs from OpenAPI

---

## 📜 License

MIT — do what you want, just don’t blame us if you use it wrong 😄

---

## 💬 Questions?

Feel free to open an issue or PR!



