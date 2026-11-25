
# CloudOps AI Copilot

An AI-powered cloud incident analysis platform.

## Project Objectives

Develop an enterprise-style platform to analyse
cloud incidents using Python, LLMs, RAG and AWS.

## Current Features

- FastAPI REST application
- Health check endpoint
- Incident analysis endpoint
- Request validation with Pydantic
- Automated testing with pytest

## Planned Features

- LLM-powered incident analysis
- Retrieval-Augmented Generation (RAG)
- AWS CloudWatch integration
- AWS Bedrock model integration
- Containerisation with Docker
- Terraform-based cloud deployment
- CI/CD automation
- Monitoring and LLMOps

## Local Development

Create and activate a Python environment:

    python3 -m venv .venv
    source .venv/bin/activate

Install dependencies:

    python -m pip install -r requirements.txt

Start the application:

    fastapi dev main.py

API documentation:

    http://localhost:8000/docs

Run tests:

    python -m pytest -v