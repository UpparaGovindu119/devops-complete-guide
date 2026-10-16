# PR Title
Add runnable project scaffolding and recruiter checklist

# PR Body
This PR adds runnable project scaffolding for three projects and supporting documentation so the repository is recruiter-ready.

What this PR includes
- Project-1-Enterprise-CICD: Jenkinsfile, Dockerfile, pom.xml, sample Java app (src/...), .dockerignore
- Project-2-AWS-Terraform-CostAware: main.tf, backend.tf (S3 backend placeholder), README-Terraform.md
- Project-3-AIOps-Lite-HERO: app.py, hardened healer.py (dry-run/auto-approve), k8s manifests, cronjob, README, LOOM instructions, recruiter checklist

Recruiter checklist (to attach to PR):
- mvn clean package output and resulting JAR
- docker build commands and image
- terraform init/apply and terraform destroy output (or terraform-destroy-output.txt)
- Project-3 running: curl / and sample /ask response

Notes
- Replace placeholders in backend.tf (<BUCKET_NAME>, <DYNAMODB_TABLE>) before running terraform.
- healer.py defaults to DRY_RUN to avoid executing LLM commands. Use HEALER_DRY_RUN=true for safe testing.

Please review and merge when satisfied.
