from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from .models import BogieChecksheet, WheelSpecification
from .serializers import BogieChecksheetSerializer, WheelSpecificationSerializer, WheelSpecificationGetSerializer
from .helpers.validation import validate_bogie_checksheet_fields, validate_wheel_specification_fields, validate_form_number, validate_date
from .helpers.response_formatter import format_bogie_checksheet_response, format_wheel_specification_post_response, format_wheel_specification_get_response

from .serializers import LoginRequestSerializer

class LoginView(APIView):
    def post(self, request):
        serializer = LoginRequestSerializer(data=request.data)
        if serializer.is_valid():
            phone = serializer.validated_data['phone']
            password = serializer.validated_data['password']
            
            if phone == "7760873976" and password == "to_share@123":
                return Response({
                    "success": True,
                    "message": "Login successful.",
                    "data": {
                        "user_id": "user_id_123",
                        "name": "Test User",
                        "token": "fake-jwt-token"
                    }
                }, status=status.HTTP_200_OK)

            return Response(
                {"detail": "Invalid credentials"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BogieChecksheetView(APIView):
    """
    POST /api/forms/bogie-checksheet
    """
    def post(self, request):
        try:
            # Extract data from request
            data = request.data
            
            # Helper function to handle date fields
            def get_date_value(value):
                if not value or value == '':
                    return None
                return value
            
            # BogieChecksheet instance 
            bogie_checksheet_obj = BogieChecksheet.objects.create(

                bogie_no=data.get('Bogie No.', '') or data.get('bogie_no', ''),
                date_of_ioh=get_date_value(data.get('Date of IOH', '') or data.get('date_of_ioh', '')),
                incoming_div_and_date=data.get('Incoming Div. & Date', '') or data.get('incoming_div_date', ''),
                maker_year_built=data.get('Maker & Year Built', '') or data.get('maker_year_built', ''),
                deficit_components=data.get('Deficit of component (if any)', '') or data.get('deficit_components', ''),

                bogie_frame_condition=data.get('Bogie Frame Condition', '') or data.get('bogie_frame_condition', ''),
                bolster=data.get('Bolster', '') or data.get('bolster', ''),
                bolster_suspension_bracket=data.get('Bolster Suspension Bracket', '') or data.get('bolster_suspension_bracket', ''),
                lower_spring_seat=data.get('Lower Spring Seat', '') or data.get('lower_spring_seat', ''),
                axle_guide=data.get('Axle Guide', '') or data.get('axle_guide', ''),
                

                axle_guide_assembly=data.get('Axle Guide Assembly', ''),
                protective_tubes=data.get('Protective Tubes', ''),
                anchor_links=data.get('Anchor Links', ''),
                side_bearer=data.get('Side Bearer', ''),
                
                # BMBC Checksheet
                cylinder_body=data.get('Cylinder Body & Dome Cover', '') or data.get('cylinder_body', ''),
                piston_trunnion=data.get('Piston & Trunnion Body', '') or data.get('piston_trunnion', ''),
                adjusting_tube=data.get('Adjusting Tube and Screw', '') or data.get('adjusting_tube', ''),
                plunger_spring=data.get('Plunger Spring', '') or data.get('plunger_spring', ''),
            
                tee_bolt_hex_nut=data.get('Tee Bolt, Hex Nut', ''),
                pawl_and_pawl_spring=data.get('Pawl and Pawl Spring', ''),
                dust_excluder=data.get('Dust Excluder', ''),
                
                # Metadata
                form_number=data.get('form_number', ''),
                inspection_by=data.get('inspection_by', ''),
                inspection_date=get_date_value(data.get('inspection_date', ''))
            )
            
            # Format and return response
            response_data = format_bogie_checksheet_response(bogie_checksheet_obj)
            return Response(response_data, status=status.HTTP_201_CREATED)
            
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
            
            # Helper function to handle date fields
            def get_date_value(value):
                if not value or value == '':
                    return None
                return value
            
            #  WheelSpecification instance 
            wheel_spec = WheelSpecification.objects.create(
                tread_diameter_new=data.get('Tread Diameter (New)', '') or data.get('tread_diameter', ''),
                last_shop_issue_size=data.get('Last Shop Issue Size (Dia.)', '') or data.get('last_shop_issue', ''),
                condemning_dia=data.get('Condemning Dia.', '') or data.get('condemning_dia', ''),
                wheel_gauge=data.get('Wheel Gauge (IFD)', '') or data.get('wheel_gauge', ''),
                variation_same_axle=data.get('Variation Same Axle', '') or data.get('variation_same_axle', ''),
                variation_same_bogie=data.get('Variation Same Bogie', '') or data.get('variation_same_bogie', ''),
                variation_same_coach=data.get('Variation Same Coach', '') or data.get('variation_same_coach', ''),
                wheel_profile=data.get('Wheel Profile', '') or data.get('wheel_profile', ''),
                intermediate_wwp=data.get('Intermediate WWP', '') or data.get('intermediate_wwp', ''),
                bearing_seat_diameter=data.get('Bearing Seat Diameter', '') or data.get('bearing_seat_diameter', ''),
                roller_bearing_outer_dia=data.get('Roller Bearing Outer Dia.', '') or data.get('roller_bearing_outer_dia', ''),
                roller_bearing_bore_dia=data.get('Roller Bearing Bore Dia.', '') or data.get('roller_bearing_bore_dia', ''),
                roller_bearing_width=data.get('Roller Bearing Width', '') or data.get('roller_bearing_width', ''),
                axle_box_housing_bore_dia=data.get('Axle Box Housing Bore Dia.', '') or data.get('axle_box_housing_bore_dia', ''),
                wheel_disc_width=data.get('Wheel Disc Width', '') or data.get('wheel_disc_width', ''),
                
                # Metadata
                form_number=data.get('form_number', ''),
                submitted_by=data.get('submitted_by', ''),
                submitted_date=get_date_value(data.get('submitted_date', ''))
            )
            
            # Format and return response
            response_data = format_wheel_specification_post_response(wheel_spec)
            return Response(response_data, status=status.HTTP_201_CREATED)
            
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