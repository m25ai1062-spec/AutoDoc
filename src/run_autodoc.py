import json
from autodoc_core import (
extract_routes,
generate_markdown,
generate_openapi,
generate_testcases,
)
from sample_api import app




def run():
    routes = extract_routes(app)

    # Write documentation
    with open("../API_DOCUMENTATION.md", "w", encoding="utf-8") as f:
        f.write(generate_markdown(routes))

    # Write OpenAPI JSON
    with open("openapi.json", "w", encoding="utf-8") as f:
        json.dump(generate_openapi(routes), f, indent=2)

    # Write AI-generated test cases
    with open("test_cases.json", "w", encoding="utf-8") as f:
        json.dump(generate_testcases(routes), f, indent=2)

    print("Documentation + OpenAPI + Test cases generated successfully.")


if __name__ == "__main__":
    run()

