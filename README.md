# fastapi-karate-testing

Demo project: FastAPI backend + Karate DSL tests + CI/CD + JMeter

## Overview
Build a small API with FastAPI and test it using Karate DSL. Automate tests with GitHub Actions (or Jenkins) and run performance tests with JMeter.

## Quickstart (Day 1)
1. Create virtualenv: `python3 -m venv .venv`
2. Activate and install: `pip install -r requirements.txt`
3. Run server: `uvicorn app.main:app --reload`
4. Open Swagger: http://127.0.0.1:8000/docs