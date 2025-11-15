
# AutoDoc — Project Report

## Abstract
AutoDoc is an Intelligent API Documentation and Testing Assistant which parses FastAPI code, generates structured OpenAPI + Markdown documentation, and synthesizes test cases using an LLM. The scaffold includes a deterministic LLM stub so the pipeline can run offline for demo and evaluation.

## Architecture
(Describe components: Parser, Generator, LLM, Test Runner, Reporter)

## Implementation
- Parser: AST-based parser located at src/parser/parser.py.
- Generator: src/generator/generator.py builds a minimal OpenAPI JSON and endpoint Markdown files.
- LLM: src/llm/llm_stub.py provides reproducible summaries and test-case templates.
- Postman: src/generator/postman_gen.py creates a Postman collection from LLM output.

## Evaluation & Evidence
- Unit tests: pytest shows parser correctness.
- Newman HTML report: evidence/newman-report.html (generated in CI or locally).
- Security scans and additional evidence can be added to evidence/.

## Quality Attributes
1. Testability — evidenced by runnable Postman collections and Newman reports.
2. Correctness — parser unit tests and integration checks.
3. Maintainability — modular code with clear separation of concerns.

## Conclusion
This scaffold is suitable to demonstrate the full AutoDoc pipeline; replace the LLM stub with a real LLM adapter and add more parsers to support complex schemas for the final project.
