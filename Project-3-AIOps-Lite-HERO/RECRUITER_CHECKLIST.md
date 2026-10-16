# Recruiter Checklist - DevOps Complete Guide

Use this checklist when recording your 2-minute Loom or preparing evidence for recruiters.

Project-1 (Enterprise CI/CD)
- Build locally: `mvn clean package` -> show target/devops-app-*.jar
- Docker build: `docker build -t devops-app:local .` and `docker run -p 8080:8080 ...`

Project-2 (Terraform FinOps)
- Configure backend.tf with your S3 bucket. Run:
  - `terraform init`
  - `terraform apply -auto-approve`
  - `terraform destroy -auto-approve` -> capture output in terraform-destroy-output.txt

Project-3 (AIOps RAG)
- Start: `uvicorn app:app --host 0.0.0.0 --port 8000`
- Test: `curl http://localhost:8000/` and `curl -X POST "http://localhost:8000/ask" -d "q=help"`
- Healer: run with `HEALER_DRY_RUN=true python healer.py` to show suggestions without executing commands

LOOM
- Record a 2-minute Loom showing: build -> terraform apply/destroy -> run app and one /ask call.
- Paste the Loom share URL in Project-3-AIOps-Lite-HERO/LOOM_URL.txt
