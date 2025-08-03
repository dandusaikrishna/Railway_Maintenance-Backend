"""
Response formatter helper for KPA Forms API
"""
from datetime import datetime

def format_bogie_checksheet_response(bogie_checksheet):
    """Format the response for a bogie checksheet"""
    return {
        'data': {
            'formNumber': bogie_checksheet.form_number,
            'inspectionBy': bogie_checksheet.inspection_by,
            'inspectionDate': bogie_checksheet.inspection_date,
            'status': 'Saved'
        },
        'message': 'Bogie checksheet submitted successfully.',
        'success': True
    }

def format_wheel_specification_post_response(wheel_spec):
    """Format the response for a wheel specification post"""
    return {
        'data': {
            'formNumber': wheel_spec.form_number,
            'status': 'Saved',
            'submittedBy': wheel_spec.submitted_by,
            'submittedDate': wheel_spec.submitted_date
        },
        'message': 'Wheel specification submitted successfully.',
        'success': True
    }

def format_wheel_specification_get_response(wheel_specs):
    """Format the response for getting wheel specifications"""
    formatted_specs = []
    for spec in wheel_specs:
        formatted_spec = {
            'fields': {
                'axleBoxHousingBoreDia': spec.axle_box_housing_bore_dia,
                'bearingSeatDiameter': spec.bearing_seat_diameter,
                'condemningDia': spec.condemning_dia,
                'intermediateWWP': spec.intermediate_wwp,
                'lastShopIssueSize': spec.last_shop_issue_size,
                'rollerBearingBoreDia': spec.roller_bearing_bore_dia,
                'rollerBearingOuterDia': spec.roller_bearing_outer_dia,
                'rollerBearingWidth': spec.roller_bearing_width,
                'treadDiameterNew': spec.tread_diameter_new,
                'variationSameAxle': spec.variation_same_axle,
                'variationSameBogie': spec.variation_same_bogie,
                'variationSameCoach': spec.variation_same_coach,
                'wheelDiscWidth': spec.wheel_disc_width,
                'wheelGauge': spec.wheel_gauge,
                'wheelProfile': spec.wheel_profile
            },
            'formNumber': spec.form_number,
            'submittedBy': spec.submitted_by,
            'submittedDate': spec.submitted_date
        }
        formatted_specs.append(formatted_spec)
    
    return {
        'data': formatted_specs,
        'message': 'Filtered wheel specification forms fetched successfully.',
        'success': True
    }
