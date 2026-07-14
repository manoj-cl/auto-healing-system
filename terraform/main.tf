# ------------------- SECURITY GROUP -------------------

resource "aws_security_group" "auto_healer_sg" {
  name        = "auto-healer-sg"
  description = "Security group for Auto-Healing System"

  ingress {
    description = "SSH"
    from_port = 22
    to_port   = 22
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port = 0
    to_port   = 0
    protocol = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "auto-healer-sg"
  }
}

# ------------------- KEY PAIR -------------------

resource "aws_key_pair" "auto_healer_key" {
    key_name   = var.key_name
    public_key = file(var.public_key_path)  # It does not upload the file itself—only the public key content.
    tags = {
        Name = "auto-healer-key"
    }
}

