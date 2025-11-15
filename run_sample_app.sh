#!/bin/bash
uvicorn examples.sample_fastapi_app.main:app --reload --port 8000
