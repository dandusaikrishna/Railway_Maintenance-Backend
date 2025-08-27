# Datadog Logging Integration TODO - AWS EC2 Deployment

## Steps to Complete:

1. [x] Update requirements.txt - Add datadog library
2. [x] Create Datadog configuration in logging_config.py
3. [x] Update middleware to use Datadog logging
4. [ ] Install Datadog Agent on AWS EC2
5. [ ] Configure Datadog Agent for log collection
6. [ ] Test the integration

## Files to Modify:
- requirements.txt ✓
- kpa_project/logging_config.py ✓
- kpa_project/middleware.py ✓
- .env.example ✓

## AWS EC2 Setup Required:
- Install Datadog Agent on EC2 instance
- Configure agent to collect Django application logs
- Set up environment variables on EC2

## Environment Variables Needed:
- DATADOG_API_KEY
- DATADOG_APP_KEY
- DD_SITE (optional, defaults to datadoghq.com)
- DD_ENV (optional, environment name)
- DD_SERVICE (optional, service name)
- DD_VERSION (optional, service version)
