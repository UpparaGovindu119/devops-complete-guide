# Terraform S3 backend configuration (placeholder)
# Replace <BUCKET_NAME>, <DYNAMODB_TABLE>, and region with your values.
terraform {
  backend "s3" {
    bucket = "<BUCKET_NAME>"
    key    = "devops-complete-guide/terraform.tfstate"
    region = "ap-south-1"
    dynamodb_table = "<DYNAMODB_TABLE>" # optional for state locking
    encrypt = true
  }
}
