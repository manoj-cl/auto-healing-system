variable "aws_region" {
    description = "The AWS region to deploy resources in"
    type        = string
}

variable "instance_type" {
    description = "The EC2 instance type to use for the auto-healing system"
    type        = string
}

variable "key_name" {
    description = "The name of the SSH key pair to use for EC2 instances"
    type        = string
}

variable "public_key_path" {
    description = "The path to the public key file for the SSH key pair"
    type        = string
}