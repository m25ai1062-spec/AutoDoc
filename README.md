# AutoDoc – Intelligent API Documentation and Testing Assistant

Author: Vivek Pankantavita  
Institute: IITJ  
Course: SDE  

## Overview
AutoDoc automates REST API documentation and test-case generation for FastAPI projects.  
It includes a fully offline AI-like summarizer requiring no API keys.

## Features
- Extracts FastAPI routes
- Generates Markdown documentation
- Creates OpenAPI JSON spec
- Suggests test cases
- 100% offline pseudo-AI summarizer

## How to Run
pip install fastapi uvicorn  
python run_autodoc.py

## Generated Files
- API_DOCUMENTATION.md  
- openapi.json  
- test_cases.json  

## Project Structure
ai_engine.py  
autodoc_core.py  
sample_api.py  
run_autodoc.py  

## Licence
For academic use only


```bash
pip install fastapi uvicorn
python run_autodoc.py
