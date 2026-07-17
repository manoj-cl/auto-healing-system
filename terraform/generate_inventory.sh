#!/bin/bash

SSH_KEY="$HOME/.ssh/id_ed25519"
IP=$(terraform output -raw instance_public_ip)

cat > ../ansible/inventory <<EOF
[auto_healer]
$IP ansible_user=ubuntu ansible_ssh_private_key_file=/Users/manojrrao/.ssh/id_ed25519
EOF

echo "Inventory generated successfully"
