#!/bin/bash

set -e  # Exit immediately if any command exits with a non-zero status (stops script on errors)

echo "========================================"
echo "Provisioning infrastructure with Terraform..."
echo "========================================"

cd terraform
terraform apply -auto-approve

cd ../scripts
echo ""
echo "Generating Ansible inventory..."
./generate_inventory.sh

# IP=$(terraform output -raw instance_public_ip)

# echo ""
# echo "Waiting for SSH..."

# until ssh -o StrictHostKeyChecking=no \
#           -o ConnectTimeout=5 \
#           -i ~/.ssh/id_ed25519 \
#           ubuntu@$IP "echo 'SSH Ready.'" >/dev/null 2>&1

# do 
#     echo "EC2 not ready yet..."
#     sleep 10
# done

# echo "SSH is ready. (From the local)"

cd ../ansible

echo ""
echo "Deploying application using Ansible..."
ansible-playbook playbook.yml

echo ""
echo "========================================"
echo "Deployment completed successfully!"
echo "========================================"