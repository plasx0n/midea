# Midea PortaSplit Stock Monitor (EU)

Monitors European retailers every 15 minutes and emails you when Midea PortaSplit (8000 / 12000 BTU) comes back in stock.

## Features
- 20+ EU retailers
- Email alerts
- GitHub Actions (free)
- Duplicate alert protection

## Setup

### Install
pip install -r requirements.txt

### Configure
Copy .env.example → .env

Fill:
EMAIL_FROM
EMAIL_PASSWORD
EMAIL_TO

### GitHub Actions
Add same values as Secrets:
- EMAIL_FROM
- EMAIL_PASSWORD
- EMAIL_TO

Then push repo → runs automatically every 15 min.
