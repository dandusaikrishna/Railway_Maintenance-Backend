# KPA Forms API – Django Backend for Railway Maintenance Forms

> A Django-powered REST API backend for managing railway maintenance forms with comprehensive validation and PostgreSQL integration.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Django](https://img.shields.io/badge/Django-REST-green.svg)](https://djangorestframework.org)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue.svg)](https://postgresql.org)
[![Docker](https://img.shields.io/badge/Docker-Containerized-blue.svg)](https://docker.com)
[![AWS](https://img.shields.io/badge/AWS-EC2%20%7C%20RDS-orange.svg)](https://aws.amazon.com)

---

## 🎯 Overview

The **KPA Forms API** is a robust Django REST Framework backend designed specifically for railway maintenance operations. It provides structured APIs to handle and validate critical maintenance forms including bogie checksheets and wheel specifications, ensuring data integrity and compliance with railway standards.

### ✨ Key Highlights

- **🔒 Comprehensive Validation** - Custom validation logic for all railway-specific form fields
- **🏗️ Modular Architecture** - Clean separation of concerns with Django apps
- **🐘 PostgreSQL Integration** - Reliable data storage with advanced querying capabilities  
- **🐳 Containerized Deployment** - Docker-ready with production configurations
- **☁️ Cloud-Native** - Optimized for AWS EC2 and RDS deployment
- **📋 API Documentation** - Complete Postman collection with examples

---

## 🚀 Quick Start

### Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8+**
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

#### Option 2: Docker Setup (Recommended)

```bash
# 1. Clone the repository
git clone <repository-url>
cd kpa-form-api-development

# 2. Build and start containers
docker-compose up --build

# 3. Access the API
# http://localhost:8000
```

---

## 📊 Technology Stack

<table>
<tr>
<td>

**Backend Framework**
- Django 4.2+
- Django REST Framework
- Python 3.8+

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

**Infrastructure**
- Docker & Docker Compose
- Gunicorn WSGI server
- Environment-based config

</td>
<td>

**Deployment**
- AWS EC2 instances
- AWS RDS PostgreSQL
- Production-ready setup

</td>
</tr>
</table>

---

## 🏗️ Project Architecture

```
kpa-forms-api/
├── 📁 forms_api/                    # Core Django app
│   ├──  helpers/                    # Utility functions
│   │   ├── validation.py            # Form validation logic
│   │   └── response_formatter.py    # API response formatting
│   ├──  migrations/                 # Database schema changes
│   ├──  models.py                   # Data models
│   ├──  serializers.py              # API serializers
│   ├──  urls.py                     # URL routing
│   ├──  views.py                    # API view classes
│   └── 🧪 tests.py                  # Unit tests
├── ⚙️ kpa_project/                  # Django project settings
├── 🐳 Dockerfile                    # Container configuration
├── 🔧 docker-compose.yml            # Multi-container setup
├── 📋 requirements.txt              # Python dependencies
└── 📖 README.md                     # Project documentation
```

---

## 🔌 API Endpoints

| Endpoint | Method | Description | Status |
|----------|--------|-------------|--------|
| `/api/forms/bogie-checksheet` | `POST` | Submit bogie checksheet with validation | ✅ Active |
| `/api/forms/wheel-specifications` | `POST` | Submit wheel specification data | ✅ Active |
| `/api/forms/wheel-specifications/list` | `GET` | Retrieve wheel specifications with filters | ✅ Active |

### 🔍 Query Parameters

**For `/wheel-specifications/list`:**
- `formNumber` - Filter by specific form number
- `submittedBy` - Filter by user ID
- `submittedDate` - Filter by submission date (YYYY-MM-DD)

---

## 🛡️ Validation Framework

### 📋 Bogie Checksheet Validation

```python
# Bogie Details
✓ bogieNo              # Required, alphanumeric
✓ dateOfIOH            # Date format (YYYY-MM-DD)
✓ incomingDivAndDate   # Division and date format
✓ makerYearBuilt       # Manufacturer and year

# Checksheet Fields
✓ axleGuide            # Condition assessment
✓ bogieFrameCondition  # Frame status
✓ bolster              # Bolster condition
✓ bolsterSuspensionBracket  # Bracket status
✓ lowerSpringSeat      # Spring seat condition
```

### 🎯 Wheel Specification Validation

```python
# Critical Measurements
✓ axleBoxHousingBoreDia    # Housing diameter specs
✓ bearingSeatDiameter      # Bearing seat measurements
✓ condemningDia            # Condemning diameter limits
✓ treadDiameterNew         # New tread diameter
✓ wheelGauge               # Gauge specifications

# Tolerance Validations
✓ variationSameAxle        # Same axle variation limits
✓ variationSameBogie       # Same bogie variation limits
✓ variationSameCoach       # Same coach variation limits
```

---

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
        "bearingSeatDiameter": "130.043 TO 130.068",
        // ... additional fields
      }
    }
  ]
}
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

2. **Environment Setup**
   ```bash
   # SSH into EC2 instance
   ssh -i your-key.pem ec2-user@your-ec2-ip
   
   # Install Docker
   sudo yum update -y
   sudo yum install -y docker
   sudo systemctl start docker
   
   # Deploy application
   git clone <your-repo>
   cd kpa-forms-api
   docker-compose up -d
   ```

3. **Environment Variables**
   ```bash
   # .env configuration for production
   DB_HOST=your-rds-endpoint.amazonaws.com
   DB_NAME=kpa_forms_db
   DB_USER=admin
   DB_PASSWORD=your-secure-password
   DEBUG=False
   ALLOWED_HOSTS=your-domain.com,your-ec2-ip
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

---

## 📚 Resources & Documentation

| Resource | Link | Description |
|----------|------|-------------|
| 📮 **Postman Collection** | [Download](https://drive.google.com/file/d/1-A6R_Paf6DYv2s4L8zza_fCkPygGduqf/view) | Complete API testing collection |
| 📖 **Django Docs** | [djangoproject.com](https://djangoproject.com) | Framework documentation |
| 🐘 **PostgreSQL Guide** | [postgresql.org](https://postgresql.org) | Database documentation |
| ☁️ **AWS Documentation** | [aws.amazon.com](https://aws.amazon.com) | Cloud deployment guides |

---

## ⚠️ Important Notes

### System Requirements
- ✅ PostgreSQL database is required and must be properly configured
- ✅ Environment variables must be set for database connectivity
- ✅ Docker containers require sufficient system resources
- ✅ AWS deployment requires proper IAM permissions

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

---


## 📞 Support

For support and questions:

- 📧 **Email**: saikrishnadandu9@gmai.com

