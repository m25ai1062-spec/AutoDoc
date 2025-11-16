# AutoDoc – Intelligent API Documentation and Testing Assistant

Author: Vivek Pankantavita  
Institute: IITJ  
Course: SDE  

## Overview
AutoDoc automatically extracts FastAPI routes and generates:

- API_DOCUMENTATION.md  
- openapi.json  
- test_cases.json  

A fully offline pseudo-AI summarizer is used to generate human-readable endpoint summaries.

## Installation
python -m venv venv
source venv/bin/activate
pip install fastapi uvicorn pydantic

## Usage
python run_autodoc.py

## Optional: Run API
uvicorn sample_api:app --reload

## No external LLMs used
The project is fully offline and safe for academic submission.



```bash
pip install fastapi uvicorn
python run_autodoc.py
