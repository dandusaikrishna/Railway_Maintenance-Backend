# KPA Forms API

A Django REST Framework application implementing APIs for KPA forms system.

## Technologies Used

- **Backend**: Python Django, Django REST Framework
- **Database**: PostgreSQL
- **Deployment**: Gunicorn, Docker & Docker Compose
- **Configuration**: python-decouple for environment management

## Setup Instructions

### Prerequisites

- Python 3.8+
- PostgreSQL database
- pip (Python package installer)
- Docker & Docker Compose (optional)

### Installation

1. Clone the repository and navigate to the project directory:
   ```bash
   git clone <repository-url>
   cd kpa-forms-api
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up PostgreSQL database:
   - Create a database named `kpa_forms_db`
   - Create a user with appropriate permissions
   - Configure `.env` file with your database credentials

5. Run database migrations:
   ```bash
   python manage.py migrate
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

### Docker Setup (Alternative)

1. Ensure Docker and Docker Compose are installed
2. Run the application:
   ```bash
   docker-compose up --build
   ```
3. Access at `http://localhost:8000`

## API Endpoints

### 1. POST /api/forms/bogie-checksheet

Submit bogie checksheet data with validation.

**Example Request:**
```json
{
  "bogieDetails": {
    "bogieNo": "BG1234",
    "dateOfIOH": "2025-07-01",
    "incomingDivAndDate": "NR / 2025-06-25",
    "makerYearBuilt": "RDSO/2018"
  },
  "bogieChecksheet": {
    "axleGuide": "Worn",
    "bogieFrameCondition": "Good"
  },
  "bmbcChecksheet": {
    "adjustingTube": "DAMAGED",
    "cylinderBody": "WORN OUT"
  },
  "formNumber": "BOGIE-2025-001",
  "inspectionBy": "user_id_456",
  "inspectionDate": "2025-07-03"
}
```

### 2. POST /api/forms/wheel-specifications

Submit wheel specification data with validation.

**Example Request:**
```json
{
  "fields": {
    "axleBoxHousingBoreDia": "280 (+0.030/+0.052)",
    "bearingSeatDiameter": "130.043 TO 130.068",
    "condemningDia": "825 (800-900)"
  },
  "formNumber": "WHEEL-2025-001",
  "submittedBy": "user_id_123",
  "submittedDate": "2025-07-03"
}
```

### 3. GET /api/forms/wheel-specifications/list

Retrieve wheel specifications with optional filters.

**Query Parameters:**
- `formNumber` (optional)
- `submittedBy` (optional)
- `submittedDate` (optional)

## Improvements Made

1. Enhanced security with non-root user in Docker
2. Added health checks to docker-compose.yml
3. Refactored validation code to reduce duplication
4. Improved error handling with specific exception types
5. Enhanced response formatting to include all fields
6. Better input validation and error messages

## Assumptions and Limitations

1. PostgreSQL database is required and must be configured
2. API responses follow the specified Swagger structure
3. Basic input validation is implemented
4. Environment variables are used for configuration management
5. The project assumes proper database connectivity and permissions
