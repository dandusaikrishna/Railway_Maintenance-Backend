# KPA Forms API – Django Backend for Railway Maintenance Forms
This backend project implements APIs using Django REST Framework to handle and validate railway maintenance forms, including bogie checksheets and wheel specifications, with structured data storage in PostgreSQL.

## 🛠️ Technologies Used
- **Backend**: Python Django, Django REST Framework
- **Database**: PostgreSQL
- **Deployment**: Gunicorn, Docker & Docker Compose

## 📋 Setup Instructions

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

## 📁 Project Structure
```
.
├── forms_api/               # Main Django app for forms processing
│   ├── helpers/             # Validation and response formatting helpers
│   ├── migrations/          # Database migration files
│   ├── models.py            # Django models for form data
│   ├── serializers.py       # Serializers for API responses
│   ├── urls.py              # URL routing for forms API
│   ├── views.py             # View classes for handling API requests
│   └── tests.py             # Unit tests for forms API
├── kpa_project/             # Django project settings
├── Dockerfile               # Docker configuration
├── docker-compose.yml       # Docker Compose configuration
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

## 🚀 Django-Powered Architecture
**Framework**: Django with Django REST Framework

## 📄 API Endpoints

| Endpoint                                 | Method | Description                                              |
|------------------------------------------|--------|----------------------------------------------------------|
| `/api/forms/bogie-checksheet`            | POST   | Submit bogie checksheet data with validation            |
| `/api/forms/wheel-specifications`        | POST   | Submit wheel specification data with validation          |
| `/api/forms/wheel-specifications/list`   | GET    | Retrieve wheel specifications with optional query parameter filters     |

**Schema Models**: Uses Django models for data validation and storage

## ⚙️ Processing Pipeline
### Form Validation
Ensures all required fields are present and properly formatted
Validates dates, form numbers, and specific field values

### Data Storage
Stores validated form data in PostgreSQL database
Maintains metadata like form numbers, submission dates, and user IDs

### Response Formatting
Formats responses consistently with success status and messages
Provides structured data in responses for client-side processing

## 📦 Modular Design
Each processing step is encapsulated in modular components:

**Validation Helpers**
- `forms_api/helpers/validation.py` – Contains validation functions for all form fields

**Response Formatters**
- `forms_api/helpers/response_formatter.py` – Contains functions to format API responses consistently

**Models**
- `forms_api/models.py` – Django models for BogieChecksheet and WheelSpecification

**Views**
- `forms_api/views.py` – APIView classes for handling each endpoint

**URLs**
- `forms_api/urls.py` – URL routing for the forms API endpoints

This design ensures the system is:
- Scalable (easy to add new form types)
- Testable (each component can be unit tested independently)
- Maintainable (separation of concerns)

## 🧠 Example Validation Logic
These are the validation rules implemented in the system:

### Bogie Checksheet Validation
``` Validate bogie details: bogieNo, dateOfIOH, incomingDivAndDate, makerYearBuilt Validate bogie checksheet fields: axleGuide, bogieFrameCondition, bolster, bolsterSuspensionBracket, lowerSpringSeat Validate BMB checksheet fields: adjustingTube, cylinderBody, pistonTrunnion, plungerSpring ```

### Wheel Specification Validation
``` Validate all wheel specification fields: axleBoxHousingBoreDia, bearingSeatDiameter, condemningDia, intermediateWWP, lastShopIssueSize, rollerBearingBoreDia, rollerBearingOuterDia, rollerBearingWidth, treadDiameterNew, variationSameAxle, variationSameBogie, variationSameCoach, wheelDiscWidth, wheelGauge, wheelProfile ```

### Date Validation
``` Validate date string format (YYYY-MM-DD) ```

### Form Number Validation
``` Validate form number is present and not too short ```


## 🧪 Running Tests
```bash
python manage.py test
```

## 📬 Example API Usage

### 1. Submit Wheel Specification (POST)
**URL:** `/api/forms/wheel-specifications`  
**Method:** POST  
**Request Body:**
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
  "data": {
    "formNumber": "WHEEL-2025-001",
    "status": "Saved",
    "submittedBy": "user_id_123",
    "submittedDate": "2025-07-03"
  },
  "message": "Wheel specification submitted successfully.",
  "success": true
}
```

### 2. Submit Bogie Checksheet (POST)
**URL:** `/api/forms/bogie-checksheet`  
**Method:** POST  
**Request Body:**
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

**Response:**
```json
{
  "data": {
    "formNumber": "BOGIE-2025-001",
    "inspectionBy": "user_id_456",
    "inspectionDate": "2025-07-03",
    "status": "Saved"
  },
  "message": "Bogie checksheet submitted successfully.",
  "success": true
}
```

### 3. Get Wheel Specifications (GET)
**URL:** `/api/forms/wheel-specifications/list`  
**Method:** GET  
**Query Parameters:**
- `formNumber` (optional): Filter by form number
- `submittedBy` (optional): Filter by submitter
- `submittedDate` (optional): Filter by submission date

**Response:**
```json
{
  "data": [
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
  ],
  "message": "Filtered wheel specification forms fetched successfully.",
  "success": true
}
```

## 📎 Resources

- [Postman Collection](KPA_form_data.postman_collection.json)

## ⚠️ Assumptions and Limitations
1. PostgreSQL database is required and must be configured
2. API responses follow the specified structure
3. Basic input validation is implemented
4. Environment variables are used for configuration management
5. The project assumes proper database connectivity and permissions
