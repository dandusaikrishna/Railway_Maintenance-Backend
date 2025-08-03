from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from .models import BogieChecksheet, WheelSpecification
from .serializers import BogieChecksheetSerializer, WheelSpecificationSerializer, WheelSpecificationGetSerializer
from .helpers.validation import validate_bogie_checksheet_fields, validate_wheel_specification_fields, validate_form_number, validate_date
from .helpers.response_formatter import format_bogie_checksheet_response, format_wheel_specification_post_response, format_wheel_specification_get_response

class BogieChecksheetView(APIView):
    """
    POST /api/forms/bogie-checksheet
    """
    def post(self, request):
        try:
            # Extract data from request
            data = request.data
            
            # Validate required fields
            bogie_details = data.get('bogieDetails', {})
            bogie_checksheet = data.get('bogieChecksheet', {})
            bmbc_checksheet = data.get('bmbcChecksheet', {})
            
            is_valid, error_message = validate_bogie_checksheet_fields(bogie_details, bogie_checksheet, bmbc_checksheet)
            if not is_valid:
                return Response({
                    'message': error_message,
                    'success': False
                }, status=status.HTTP_400_BAD_REQUEST)
            
            # Validate form number
            is_valid, error_message = validate_form_number(data.get('formNumber', ''))
            if not is_valid:
                return Response({
                    'message': error_message,
                    'success': False
                }, status=status.HTTP_400_BAD_REQUEST)
            
            # Validate inspection date
            is_valid, error_message = validate_date(data.get('inspectionDate', ''))
            if not is_valid:
                return Response({
                    'message': error_message,
                    'success': False
                }, status=status.HTTP_400_BAD_REQUEST)
            
            # Create BogieChecksheet instance
            bogie_checksheet_obj = BogieChecksheet.objects.create(
                # Bogie Details
                bogie_no=bogie_details.get('bogieNo', ''),
                date_of_ioh=bogie_details.get('dateOfIOH', ''),
                incoming_div_and_date=bogie_details.get('incomingDivAndDate', ''),
                maker_year_built=bogie_details.get('makerYearBuilt', ''),
                deficit_components=bogie_details.get('deficitComponents', ''),
                
                # Bogie Checksheet fields
                axle_guide=bogie_checksheet.get('axleGuide', ''),
                bogie_frame_condition=bogie_checksheet.get('bogieFrameCondition', ''),
                bolster=bogie_checksheet.get('bolster', ''),
                bolster_suspension_bracket=bogie_checksheet.get('bolsterSuspensionBracket', ''),
                lower_spring_seat=bogie_checksheet.get('lowerSpringSeat', ''),
                
                # BMB Checksheet fields
                adjusting_tube=bmbc_checksheet.get('adjustingTube', ''),
                cylinder_body=bmbc_checksheet.get('cylinderBody', ''),
                piston_trunnion=bmbc_checksheet.get('pistonTrunnion', ''),
                plunger_spring=bmbc_checksheet.get('plungerSpring', ''),
                
                # Metadata
                form_number=data.get('formNumber', ''),
                inspection_by=data.get('inspectionBy', ''),
                inspection_date=data.get('inspectionDate', '')
            )
            
            # Format and return response
            response_data = format_bogie_checksheet_response(bogie_checksheet_obj)
            return Response(response_data, status=status.HTTP_201_CREATED)
            
        except ValueError as e:
            return Response({
                'message': f'Invalid data format: {str(e)}',
                'success': False
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                'message': f'Error submitting bogie checksheet: {str(e)}',
                'success': False
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class WheelSpecificationPostView(APIView):
    """
    POST /api/forms/wheel-specifications
    """
    def post(self, request):
        try:
            # Extract data from request
            data = request.data
            
            # Validate required fields
            fields = data.get('fields', {})
            
            is_valid, error_message = validate_wheel_specification_fields(fields)
            if not is_valid:
                return Response({
                    'message': error_message,
                    'success': False
                }, status=status.HTTP_400_BAD_REQUEST)
            
            # Validate form number
            is_valid, error_message = validate_form_number(data.get('formNumber', ''))
            if not is_valid:
                return Response({
                    'message': error_message,
                    'success': False
                }, status=status.HTTP_400_BAD_REQUEST)
            
            # Validate submitted date
            is_valid, error_message = validate_date(data.get('submittedDate', ''))
            if not is_valid:
                return Response({
                    'message': error_message,
                    'success': False
                }, status=status.HTTP_400_BAD_REQUEST)
            
            # Create WheelSpecification instance
            wheel_spec = WheelSpecification.objects.create(
                # Wheel specification fields
                axle_box_housing_bore_dia=fields.get('axleBoxHousingBoreDia', ''),
                bearing_seat_diameter=fields.get('bearingSeatDiameter', ''),
                condemning_dia=fields.get('condemningDia', ''),
                intermediate_wwp=fields.get('intermediateWWP', ''),
                last_shop_issue_size=fields.get('lastShopIssueSize', ''),
                roller_bearing_bore_dia=fields.get('rollerBearingBoreDia', ''),
                roller_bearing_outer_dia=fields.get('rollerBearingOuterDia', ''),
                roller_bearing_width=fields.get('rollerBearingWidth', ''),
                tread_diameter_new=fields.get('treadDiameterNew', ''),
                variation_same_axle=fields.get('variationSameAxle', ''),
                variation_same_bogie=fields.get('variationSameBogie', ''),
                variation_same_coach=fields.get('variationSameCoach', ''),
                wheel_disc_width=fields.get('wheelDiscWidth', ''),
                wheel_gauge=fields.get('wheelGauge', ''),
                wheel_profile=fields.get('wheelProfile', ''),
                
                # Metadata
                form_number=data.get('formNumber', ''),
                submitted_by=data.get('submittedBy', ''),
                submitted_date=data.get('submittedDate', '')
            )
            
            # Format and return response
            response_data = format_wheel_specification_post_response(wheel_spec)
            return Response(response_data, status=status.HTTP_201_CREATED)
            
        except ValueError as e:
            return Response({
                'message': f'Invalid data format: {str(e)}',
                'success': False
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                'message': f'Error submitting wheel specification: {str(e)}',
                'success': False
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class WheelSpecificationGetView(APIView):
    """
    GET /api/forms/wheel-specifications (with filters)
    """
    def get(self, request):
        try:
            # Get query parameters for filtering
            form_number = request.query_params.get('formNumber', None)
            submitted_by = request.query_params.get('submittedBy', None)
            submitted_date = request.query_params.get('submittedDate', None)
            
            # Start with all records
            queryset = WheelSpecification.objects.all()
            
            # Apply filters if provided
            if form_number:
                queryset = queryset.filter(form_number__icontains=form_number)
            if submitted_by:
                queryset = queryset.filter(submitted_by__icontains=submitted_by)
            if submitted_date:
                queryset = queryset.filter(submitted_date=submitted_date)
            
            # Format the response
            response_data = format_wheel_specification_get_response(queryset)
            return Response(response_data, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({
                'message': f'Error fetching wheel specifications: {str(e)}',
                'success': False
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
