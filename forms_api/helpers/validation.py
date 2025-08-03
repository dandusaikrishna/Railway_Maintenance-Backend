"""
Validation helper functions for KPA Forms API
"""
from datetime import datetime
import re

def validate_date(date_string):
    """Validate date string format (YYYY-MM-DD)"""
    if not date_string:
        return False, "Date is required"
    
    try:
        datetime.strptime(date_string, '%Y-%m-%d')
        return True, None
    except ValueError:
        return False, "Invalid date format. Expected YYYY-MM-DD"

def validate_required_fields(data, required_fields):
    """Validate that all required fields are present"""
    missing_fields = []
    for field in required_fields:
        if field not in data or data[field] is None or data[field] == "":
            missing_fields.append(field)
    
    if missing_fields:
        return False, f"Missing required fields: {', '.join(missing_fields)}"
    
    return True, None

def validate_form_number(form_number):
    """Validate form number format"""
    if not form_number:
        return False, "Form number is required"
    
    # Basic validation - can be enhanced based on specific requirements
    if len(form_number) < 3:
        return False, "Form number is too short"
    
    return True, None

def validate_non_empty_string(value, field_name):
    """Validate that a string field is not empty"""
    if not value or not value.strip():
        return False, f"{field_name} cannot be empty"
    
    return True, None

def validate_fields_presence(data, required_fields, section_name):
    """Validate that all required fields in a section are present"""
    missing_fields = []
    for field in required_fields:
        if field not in data or data[field] is None or data[field] == "":
            missing_fields.append(field)
    
    if missing_fields:
        return False, f"Missing required {section_name} fields: {', '.join(missing_fields)}"
    
    return True, None

def validate_wheel_specification_fields(fields):
    """Validate wheel specification fields"""
    if not fields:
        return False, "Fields object is required"
    
    required_wheel_fields = [
        'axleBoxHousingBoreDia', 'bearingSeatDiameter', 'condemningDia',
        'intermediateWWP', 'lastShopIssueSize', 'rollerBearingBoreDia',
        'rollerBearingOuterDia', 'rollerBearingWidth', 'treadDiameterNew',
        'variationSameAxle', 'variationSameBogie', 'variationSameCoach',
        'wheelDiscWidth', 'wheelGauge', 'wheelProfile'
    ]
    
    return validate_fields_presence(fields, required_wheel_fields, "wheel specification")

def validate_bogie_checksheet_fields(bogie_details, bogie_checksheet, bmbc_checksheet):
    """Validate bogie checksheet fields"""
    if not bogie_details:
        return False, "Bogie details are required"
    
    if not bogie_checksheet:
        return False, "Bogie checksheet fields are required"
    
    if not bmbc_checksheet:
        return False, "BMB checksheet fields are required"
    
    # Validate bogie details
    bogie_details_required = ['bogieNo', 'dateOfIOH', 'incomingDivAndDate', 'makerYearBuilt']
    is_valid, error_message = validate_fields_presence(bogie_details, bogie_details_required, "bogie details")
    if not is_valid:
        return False, error_message
    
    # Validate bogie checksheet fields
    bogie_checksheet_required = ['axleGuide', 'bogieFrameCondition', 'bolster', 'bolsterSuspensionBracket', 'lowerSpringSeat']
    is_valid, error_message = validate_fields_presence(bogie_checksheet, bogie_checksheet_required, "bogie checksheet")
    if not is_valid:
        return False, error_message
    
    # Validate BMB checksheet fields
    bmbc_checksheet_required = ['adjustingTube', 'cylinderBody', 'pistonTrunnion', 'plungerSpring']
    is_valid, error_message = validate_fields_presence(bmbc_checksheet, bmbc_checksheet_required, "BMB checksheet")
    if not is_valid:
        return False, error_message
    
    return True, None
