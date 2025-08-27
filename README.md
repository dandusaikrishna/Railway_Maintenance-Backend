# KPA Forms API – Django Backend for Railway Maintenance Forms

> A Django-powered REST API backend for managing railway maintenance forms with comprehensive validation, PostgreSQL integration, and Datadog monitoring.

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org)
[![Django](https://img.shields.io/badge/Django-5.2.4-green.svg)](https://djangorestframework.org)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue.svg)](https://postgresql.org)
[![Docker](https://img.shields.io/badge/Docker-Containerized-blue.svg)](https://docker.com)
[![Datadog](https://img.shields.io/badge/Datadog-Monitoring-purple.svg)](https://datadoghq.com)
[![AWS](https://img.shields.io/badge/AWS-EC2%20%7C%20RDS-orange.svg)](https://aws.amazon.com)

---
## 🎥 Video Tutorials

| Tutorial | Link | Description |
|----------|------|-------------|
| 🚀 **Setup & Development** | [Watch Now](https://drive.google.com/file/d/17QCv4pfbuGwF-YY-i1CHJYKyUKcSJ8ya/view?usp=sharing) | Initial setup, configuration & API testing |
| 🐳 **Docker & AWS Deployment** | [Watch Now](https://drive.google.com/file/d/1pbGgeTAep39GuDYdNK1tmojN1PWTQ1Fv/view?usp=drive_link) | Containerization, AWS deployment & logging |
| 📊 **Datadog Integration** | [Watch Now](https://drive.google.com/file/d/1pbGgeTAep39GuDYdNK1tmojN1PWTQ1Fv/view?usp=sharing) | Real-time monitoring & log analytics setup |
---

## Overview

The **KPA Forms API** is a robust Django REST Framework backend designed specifically for railway maintenance operations. It provides structured APIs to handle and validate critical maintenance forms including bogie checksheets and wheel specifications, ensuring data integrity and compliance with railway standards.

## Key Differentiators

### Beyond Basic CRUD
- **Railway Domain Expertise**: Understanding of engineering tolerances and maintenance workflows
- **Production-Ready Architecture**: Full monitoring, logging, and deployment pipeline
- **Comprehensive Testing**: API testing suite with edge cases
- **Documentation Quality**: Clear setup instructions and video walkthroughs

### Technical Depth
- **Custom Middleware**: Request/response logging and timing
- **Advanced Querying**: Optimized database queries with proper indexing
- **Error Recovery**: Graceful handling of database connection issues
- **Monitoring Integration**: Real-time application health tracking

### Key Highlights

- **Comprehensive Validation** - Custom validation logic for all railway-specific form fields
- **Modular Architecture** - Clean separation of concerns with Django apps
- **PostgreSQL Integration** - Reliable data storage with advanced querying capabilities  
- **Containerized Deployment** - Docker-ready with production configurations
- **Advanced Monitoring** - Integrated Datadog APM and logging for production insights
- **Cloud-Native** - Optimized for AWS EC2 and RDS deployment
- **API Documentation** - Complete Postman collection with examples


---

## 🚀 Quick Start

### Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.9+**
- **PostgreSQL 12+**
- **Docker & Docker Compose** (for containerized setup)
- **pip** (Python package manager)

### 🛠️ Local Development Setup

#### Option 1: Traditional Setup

```bash
# 1. Clone and navigate to the project
git clone <repository-url>
cd kpa-forms-api

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment variables
cp .env.example .env
# Edit .env with your database credentials

# 5. Run database migrations
python manage.py migrate

# 6. Start the development server
python manage.py runserver
```

#### Option 2: Docker Setup with Monitoring (Recommended)

```bash
# 1. Clone the repository
git clone <repository-url>
cd kpa-forms-api

# 2. Configure environment variables
cp .env.example .env
# Add your Datadog API key and other configurations

# 3. Build and start containers with monitoring
docker-compose up --build

# 4. Access the API
# http://localhost:8000
```

---

## 📊 Technology Stack

<table>
<tr>
<td>

**Backend Framework**
- Django 5.2.4
- Django REST Framework
- Python 3.9+

</td>
<td>

**Database**
- PostgreSQL 12+
- Django ORM
- Custom migrations

</td>
</tr>
<tr>
<td>

**Monitoring & Logging**
- Datadog APM
- Structured JSON logging
- Request/Response middleware
- Error tracking & alerts

</td>
<td>

**Infrastructure**
- Docker & Docker Compose
- Gunicorn WSGI server
- Environment-based config

</td>
</tr>
<tr>
<td colspan="2">

**Deployment**
- AWS EC2 instances
- AWS RDS PostgreSQL
- Production-ready monitoring
- Automated log aggregation

</td>
</tr>
</table>

---

## 🏗️ Project Architecture


```
kpa-forms-api/
├── forms_api/                       # Core Django app
│   ├──  helpers/                    # Utility functions
│   │   ├── validation.py            # Form validation logic
│   │   └── response_formatter.py    # API response formatting
│   ├──  migrations/                 # Database schema changes
│   ├──  models.py                   # Data models
│   ├──  serializers.py              # API serializers
│   ├──  urls.py                     # URL routing
│   ├──  views.py                    # API view classes
│   └──  tests.py                    # Unit tests
├── kpa_project/                     # Django project settings
│   ├── logging_config.py            # Comprehensive logging setup
│   ├── middleware.py                # Request/Response logging
│   └── settings.py                  # Django configuration
├── logs/                            # Application logs
│   ├── django.log                   # General Django logs
│   ├── requests.log                 # HTTP request logs
│   ├── forms_api.log               # API-specific logs
│   ├── database.log                # Database query logs
│   └── errors.log                  # Error logs
├── Dockerfile                       # Container configuration
├── docker-compose.yml               # Multi-container setup with Datadog
├── requirements.txt                 # Python dependencies
└── README.md                        # Project documentation
```


---

## 🔌 API Endpoints

| Endpoint | Method | Description | Status |
|----------|--------|-------------|--------|
| `/api/forms/bogie-checksheet` | `POST` | Submit bogie checksheet with validation | ✅ Active |
| `/api/forms/wheel-specifications` | `POST` | Submit wheel specification data | ✅ Active |
| `/api/forms/wheel-specifications/list` | `GET` | Retrieve wheel specifications with filters | ✅ Active |

## 📘 API Usage Examples

### 1️⃣ Submit Wheel Specification

**Endpoint:** `POST /api/forms/wheel-specifications`

```json
{
  "fields": {
    "axleBoxHousingBoreDia": "280 (+0.030/+0.052)",
    "bearingSeatDiameter": "130.043 TO 130.068",
    "condemningDia": "825 (800-900)",
    "intermediateWWP": "20 TO 28",
    "lastShopIssueSize": "837 (800-900)",
    "rollerBearingBoreDia": "130 (+0.0/-0.025)",
    "rollerBearingOuterDia": "280 (+0.0/-0.035)",
    "rollerBearingWidth": "93 (+0/-0.250)",
    "treadDiameterNew": "915 (900-1000)",
    "variationSameAxle": "0.5",
    "variationSameBogie": "5",
    "variationSameCoach": "13",
    "wheelDiscWidth": "127 (+4/-0)",
    "wheelGauge": "1600 (+2,-1)",
    "wheelProfile": "29.4 Flange Thickness"
  },
  "formNumber": "WHEEL-2025-001",
  "submittedBy": "user_id_123",
  "submittedDate": "2025-07-03"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Wheel specification submitted successfully.",
  "data": {
    "formNumber": "WHEEL-2025-001",
    "status": "Saved",
    "submittedBy": "user_id_123",
    "submittedDate": "2025-07-03"
  }
}
```

### 2️⃣ Submit Bogie Checksheet

**Endpoint:** `POST /api/forms/bogie-checksheet`

```json
{
  "bogieDetails": {
    "bogieNo": "BG1234",
    "dateOfIOH": "2025-07-01",
    "deficitComponents": "None",
    "incomingDivAndDate": "NR / 2025-06-25",
    "makerYearBuilt": "RDSO/2018"
  },
  "bogieChecksheet": {
    "axleGuide": "Worn",
    "bogieFrameCondition": "Good",
    "bolster": "Good",
    "bolsterSuspensionBracket": "Cracked",
    "lowerSpringSeat": "Good"
  },
  "bmbcChecksheet": {
    "adjustingTube": "DAMAGED",
    "cylinderBody": "WORN OUT",
    "pistonTrunnion": "GOOD",
    "plungerSpring": "GOOD"
  },
  "formNumber": "BOGIE-2025-001",
  "inspectionBy": "user_id_456",
  "inspectionDate": "2025-07-03"
}
```

### 3️⃣ Retrieve Wheel Specifications

**Endpoint:** `GET /api/forms/wheel-specifications/list?formNumber=WHEEL-2025-001`

```json
{
  "success": true,
  "message": "Filtered wheel specification forms fetched successfully.",
  "data": [
    {
      "formNumber": "WHEEL-2025-001",
      "submittedBy": "user_id_123",
      "submittedDate": "2025-07-03",
      "fields": {
        "axleBoxHousingBoreDia": "280 (+0.030/+0.052)",
        "bearingSeatDiameter": "130.043 TO 130.068"
        // ... additional fields
      }
    }
  ]
}
```


---
## 📊 Monitoring & Logging

### Datadog Integration

The application includes comprehensive monitoring and logging through Datadog:

- **APM (Application Performance Monitoring)** - Track request performance and database queries
- **Log Management** - Centralized logging with structured JSON format
- **Error Tracking** - Automatic error detection and alerting
- **Custom Metrics** - Business-specific metrics and dashboards

### Live Monitoring Screenshots

> **Real Production Environment**: These screenshots demonstrate the live Datadog monitoring setup running on AWS EC2, showing actual application metrics, traces, and log streams in real-time.


| Monitoring View | Screenshot | Description |
|----------------|------------|-------------|
| 📊 **Datadog Dashboard** | <img width="600" alt="Datadog Dashboard" src="https://github.com/user-attachments/assets/321b0eb6-3f32-43e6-9e64-e4918b7cea68" /> | Real-time application metrics and performance |
| 🔍 **APM Traces** | <img width="600" alt="APM Traces" src="https://github.com/user-attachments/assets/e5c0c96b-9a1e-443b-afe5-41301d10b785" /> | Request tracing and performance analysis |
| ⚠️ **Error Tracking** | <img width="600" alt="Error Alerts" src="https://github.com/user-attachments/assets/e012ced0-21b9-42fc-bbce-2653a79f9453" /> | Automated error detection and alerting |
| ⚠️ **Warning Logs** | <img width="600" alt="Warning Logs" src="https://github.com/user-attachments/assets/56768d53-c63d-44ac-83ac-c784f1699d4e" /> | Real-time warning and info log monitoring |

### Log Categories

| Log Type | File | Description |
|----------|------|-------------|
| **General** | `django.log` | Django framework logs |
| **Requests** | `requests.log` | HTTP request/response logs |
| **API** | `forms_api.log` | Application-specific logs |
| **Database** | `database.log` | Database query logs |
| **Errors** | `errors.log` | Error and exception logs |

### Environment Configuration

```bash
# Datadog Configuration
DD_API_KEY=your-datadog-api-key
DD_ENV=development
DD_SERVICE=kpa-django-app
DD_VERSION=1.0.0
DD_AGENT_HOST=datadog-agent
DD_AGENT_PORT=8126
DD_SITE=datadoghq.com
```

---


## 🌩️ AWS Deployment

### Infrastructure Setup

```bash
# 1. Launch EC2 instance
aws ec2 run-instances \
  --image-id ami-0abcdef1234567890 \
  --count 1 \
  --instance-type t3.medium \
  --key-name your-key-pair \
  --security-groups web-server-sg

# 2. Create RDS PostgreSQL instance
aws rds create-db-instance \
  --db-instance-identifier kpa-forms-db \
  --db-instance-class db.t3.micro \
  --engine postgres \
  --master-username admin \
  --master-user-password your-secure-password \
  --allocated-storage 20
```

### Deployment Steps

1. **Configure Security Groups**
   - Allow HTTP/HTTPS traffic (ports 80, 443)
   - Allow SSH access (port 22)
   - Configure RDS security group for PostgreSQL (port 5432)
   - Allow Datadog agent communication (ports 8125, 8126)

2. **Environment Setup**
   ```bash
   # SSH into EC2 instance
   ssh -i your-key.pem ec2-user@your-ec2-ip
   
   # Install Docker
   sudo yum update -y
   sudo yum install -y docker
   sudo systemctl start docker
   
   # Deploy application with monitoring
   git clone <your-repo>
   cd kpa-forms-api
   docker-compose up -d
   ```

3. **Production Environment Variables**
   ```bash
   # .env configuration for production
   DEBUG=False
   SECRET_KEY=your-production-secret-key
   ALLOWED_HOSTS=your-domain.com,your-ec2-ip
   
   # Database Configuration
   DB_HOST=your-rds-endpoint.amazonaws.com
   DB_NAME=kpa_forms_db
   DB_USER=admin
   DB_PASSWORD=your-secure-password
   DB_PORT=5432
   
   # Datadog Configuration
   DD_API_KEY=your-datadog-api-key
   DD_ENV=production
   DD_SERVICE=kpa-django-app
   DD_VERSION=1.0.0
   DD_SITE=datadoghq.com
   ```

---

## 🧪 Testing

### Run Test Suite

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test forms_api

# Run with coverage
pip install coverage
coverage run --source='.' manage.py test
coverage report
```

### Test Categories

- **✅ Unit Tests** - Individual function validation
- **🔗 Integration Tests** - API endpoint testing  
- **📊 Data Validation Tests** - Form field validation
- **🔒 Authentication Tests** - Security validation
- **🖥️ Monitoring Tests** - Logging and metrics validation

---

## 📚 Resources & Documentation

| Resource | Link | Description |
|----------|------|-------------|
| 📮 **Postman Collection** | [Download](https://drive.google.com/file/d/1-A6R_Paf6DYv2s4L8zza_fCkPygGduqf/view) | Complete API testing collection |
| 📊 **Datadog Dashboard** | [View Dashboard](https://app.datadoghq.com) | Production monitoring dashboard |

---

## ⚠️ Important Notes

### System Requirements
- ✅ PostgreSQL database is required and must be properly configured
- ✅ Environment variables must be set for database connectivity and monitoring
- ✅ Docker containers require sufficient system resources
- ✅ AWS deployment requires proper IAM permissions
- ✅ Datadog account required for monitoring features

### Data Validation
- ✅ All form fields undergo comprehensive validation
- ✅ Date formats must follow ISO 8601 standard (YYYY-MM-DD)
- ✅ Form numbers must be unique and follow specified patterns
- ✅ Railway-specific measurements must include proper units and tolerances

### API Response Format
All API responses follow this consistent structure:
```json
{
  "success": boolean,
  "message": "string",
  "data": object | array
}
```

### Monitoring & Alerts
- ✅ All API requests are automatically logged and monitored
- ✅ Database query performance is tracked
- ✅ Error rates and response times are monitored
- ✅ Custom business metrics are available in Datadog dashboards

---

## 📦 Dependencies

### Core Dependencies
```txt
Django==5.2.4
djangorestframework
django-cors-headers
python-decouple
psycopg2-binary
gunicorn
python-json-logger
ddtrace  # Datadog APM
```

### Development Dependencies
```txt
pytest
pytest-django
coverage
black  # Code formatting
flake8  # Code linting
```

---

## 📞 Support & Contributing

### Getting Help
- 📧 **Email**: saikrishnadandu9@gmail.com
- 📊 **Monitoring**: Check Datadog dashboard for system health

### Code Style
- Follow PEP 8 guidelines
- Use meaningful variable names
- Add docstrings to functions
- Include logging for important operations
- Write tests for new features

---


## 🚀 Roadmap

### Current Sprint
- ✅ Basic form submission APIs
- ✅ PostgreSQL integration
- ✅ Docker containerization
- ✅ Datadog monitoring integration
- ✅ AWS deployment guide


