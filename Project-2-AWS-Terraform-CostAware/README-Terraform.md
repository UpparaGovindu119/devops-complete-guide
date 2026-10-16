# Terraform README - S3 backend & destroy proof

This folder contains a minimal Terraform configuration for a VPC, subnet, and an EC2 instance. To make the backend durable and shared, configure an S3 backend and (optionally) a DynamoDB table for locking.

Steps to prepare S3 backend (example):
1. Create an S3 bucket for state:
   aws s3api create-bucket --bucket my-terraform-state-bucket --region ap-south-1 --create-bucket-configuration LocationConstraint=ap-south-1
2. Create a DynamoDB table for locking (optional but recommended):
   aws dynamodb create-table --table-name terraform-locks --attribute-definitions AttributeName=LockID,AttributeType=S --key-schema AttributeName=LockID,KeyType=HASH --billing-mode PAY_PER_REQUEST --region ap-south-1
3. Update backend.tf with your bucket and table names, then run:
   terraform init
   terraform apply -auto-approve

To demonstrate destroy proof (what recruiters expect):
- Run:
  terraform destroy -auto-approve
- Capture the terminal output and save to terraform-destroy-output.txt, or record a 1-2 minute Loom video showing apply -> destroy.

Note: Do not store AWS credentials in the repo. Use environment variables or an AWS profile.
