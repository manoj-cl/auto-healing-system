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