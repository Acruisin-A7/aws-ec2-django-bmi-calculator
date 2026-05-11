# AWS EC2 Django BMI Calculator

A Django-based BMI Calculator deployed on AWS using traditional 
EC2 infrastructure — demonstrating VPC networking, Linux server 
configuration, and a production-grade Nginx + Gunicorn stack.

## AWS Infrastructure

- **VPC** — Custom VPC with CIDR 10.0.0.0/16
- **Subnet** — Public subnet 10.0.1.0/24 with auto-assign public IP
- **Internet Gateway** — Attached with 0.0.0.0/0 route
- **Security Group** — HTTP (80) open, SSH (22) restricted to admin IP
- **EC2** — t2.micro, Ubuntu 22.04 LTS (Free Tier)

## Tech Stack

- **Python / Django** — Server-rendered web application
- **Gunicorn** — Production WSGI server (3 workers, Unix socket)
- **Nginx** — Reverse proxy and static file serving
- **Systemd** — Process management and auto-restart
- **SQLite** — Local database (no RDS — intentionally kept simple)

## Local Setup

```bash
git clone https://github.com/YOUR_USERNAME/aws-ec2-django-bmi-calculator
cd aws-ec2-django-bmi-calculator
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Key Learning Outcomes

- VPC networking: subnets, route tables, internet gateways
- EC2 provisioning and Linux server configuration
- Nginx as a reverse proxy forwarding to Gunicorn via Unix socket
- Systemd service management for production process persistence
- Django production settings (ALLOWED_HOSTS, STATIC_ROOT, collectstatic)
