# Project-3 AIOps Lite HERO - README

This project contains a small FastAPI RAG app that uses ChromaDB for retrieval and a private Ollama LLM for generation. It also includes a simple self-healing script (healer.py) which queries logs and asks Ollama for a kubectl fix command.

Prerequisites
- Ollama service accessible at http://ollama:11434 (or adjust the URL in app.py/healer.py)
- ChromaDB Python client installed and running
- Kubernetes cluster if you intend to use healer.py (the healer runs kubectl commands returned by the model)

How to run (local)
1. Create a Python virtualenv and install requirements (not included): chromadb, fastapi, uvicorn, requests
2. Start the FastAPI app:
   uvicorn app:app --host 0.0.0.0 --port 8000

Healer script (warning)
- healer.py will execute kubectl commands returned by an LLM. This is potentially dangerous. Review returned commands and test in a safe environment.

CronJob
- cronjob-cost-saver.yaml is included and scales the aiops-bot deployment to 0 replicas nightly as a cost-saving measure.

Loom video
- I cannot create the Loom recording. To produce the recruiter-ready video, record a 2-minute Loom that demonstrates:
  - Running `mvn clean package` in Project-1
  - Showing Terraform init/apply and terraform destroy output in Project-2 (or the terraform-destroy-output.txt)
  - Starting the FastAPI app and a quick `curl` to /ask to show a response.
- Upload the Loom video and paste the URL into this repo's README or a file: Project-3-AIOps-Lite-HERO/LOOM_URL.txt
