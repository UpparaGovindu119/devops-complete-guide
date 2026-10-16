# Project-2: AWS Terraform CostAware
# Hyderabad (ap-south-1) region and simple cost-saver instance with schedule tag
provider "aws" { region = "ap-south-1" } # Hyderabad region

resource "aws_vpc" "main" { cidr_block = "10.0.0.0/16" tags = {Name="finops-vpc"} }
resource "aws_subnet" "public" { vpc_id=aws_vpc.main.id cidr_block="10.0.1.0/24" map_public_ip_on_launch=true }
resource "aws_instance" "app" {
  ami="ami-0f5ee92e2d63afc18" instance_type="t2.micro"
  subnet_id=aws_subnet.public.id tags={Name="cost-saver", Schedule="stop-at-night"}
}
