
# AutoDoc — Intelligent API Documentation & Testing Assistant (Scaffold)

This repository contains a working scaffold for the AutoDoc project used in the SDE Major Project.

## What this scaffold provides
- A minimal FastAPI sample app (examples/sample_fastapi_app/main.py).
- An AST-based parser that extracts endpoint metadata (src/parser/parser.py).
- A generator to build a minimal OpenAPI spec and endpoint Markdown docs (src/generator/generator.py).
- An LLM stub that deterministically generates readable summaries and simple test cases (src/llm/llm_stub.py).
- A Postman collection generator (src/generator/postman_gen.py).
- A CLI to run the pipeline and produce artifacts in docs/ (src/cli.py).
- Unit test for the parser (src/tests/test_parser.py).
- Example Postman collection and CI workflow.

## Quickstart (local)
1. Create venv and install dependencies (FastAPI required to run example app):

```bash
python -m venv .venv
source .venv/bin/activate
pip install fastapi uvicorn pytest
```

2. Run the sample app:

```bash
uvicorn examples.sample_fastapi_app.main:app --reload --port 8000
```

3. Run the pipeline to generate docs & postman collection:

```bash
python -m src.cli examples/sample_fastapi_app/main.py --out docs
```

4. Run tests:

```bash
pytest -q
```

5. Run Newman (requires node + newman):

```bash
# install newman globally
npm install -g newman
newman run examples/sample_collection.postman_collection.json -r html --reporter-html-export evidence/newman-report.html
```

## CI (GitHub Actions)
See .github/workflows/ci.yml — it runs tests and a Newman run and uploads evidence/ as an artifact.

## How to extend
- Replace src/llm/llm_stub.py with a real LLM adapter (OpenAI or local Llama) and store prompts in evidence/prompts/.
- Improve parser to inspect Pydantic models and extract request/response schemas.
- Add schema validation and post-processing to avoid hallucinations from the LLM.

## License
MIT
