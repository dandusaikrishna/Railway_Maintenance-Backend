from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import BogieChecksheet, WheelSpecification

class FormsAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        
        # Create a sample BogieChecksheet instance
        self.bogie_checksheet_data = {
            "bmbcChecksheet": {
                "adjustingTube": "DAMAGED",
                "cylinderBody": "WORN OUT",
                "pistonTrunnion": "GOOD",
                "plungerSpring": "GOOD"
            },
            "bogieChecksheet": {
                "axleGuide": "Worn",
                "bogieFrameCondition": "Good",
                "bolster": "Good",
                "bolsterSuspensionBracket": "Cracked",
                "lowerSpringSeat": "Good"
            },
            "bogieDetails": {
                "bogieNo": "BG1234",
                "dateOfIOH": "2025-07-01",
                "deficitComponents": "None",
                "incomingDivAndDate": "NR / 2025-06-25",
                "makerYearBuilt": "RDSO/2018"
            },
            "formNumber": "BOGIE-2025-001",
            "inspectionBy": "user_id_456",
            "inspectionDate": "2025-07-03"
        }
        
        # Create a sample WheelSpecification instance
        self.wheel_specification_post_data = {
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
        
        # Create a sample WheelSpecification instance for GET requests
        self.wheel_specification = WheelSpecification.objects.create(
            axle_box_housing_bore_dia="280 (+0.030/+0.052)",
            bearing_seat_diameter="130.043 TO 130.068",
            condemning_dia="825 (800-900)",
            intermediate_wwp="20 TO 28",
            last_shop_issue_size="837 (800-900)",
            roller_bearing_bore_dia="130 (+0.0/-0.025)",
            roller_bearing_outer_dia="280 (+0.0/-0.035)",
            roller_bearing_width="93 (+0/-0.250)",
            tread_diameter_new="915 (900-1000)",
            variation_same_axle="0.5",
            variation_same_bogie="5",
            variation_same_coach="13",
            wheel_disc_width="127 (+4/-0)",
            wheel_gauge="1600 (+2,-1)",
            wheel_profile="29.4 Flange Thickness",
            form_number="WHEEL-2025-001",
            submitted_by="user_id_123",
            submitted_date="2025-07-03"
        )

    def test_bogie_checksheet_post(self):
        """Test POST /api/forms/bogie-checksheet"""
        url = reverse('bogie-checksheet')
        response = self.client.post(url, self.bogie_checksheet_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data['success'])
        self.assertEqual(response.data['message'], 'Bogie checksheet submitted successfully.')
        
        # Check if the data was saved in the database
        self.assertEqual(BogieChecksheet.objects.count(), 1)
        bogie_checksheet = BogieChecksheet.objects.first()
        self.assertEqual(bogie_checksheet.form_number, "BOGIE-2025-001")

    def test_wheel_specification_post(self):
        """Test POST /api/forms/wheel-specifications"""
        url = reverse('wheel-specifications')
        response = self.client.post(url, self.wheel_specification_post_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data['success'])
        self.assertEqual(response.data['message'], 'Wheel specification submitted successfully.')
        
        # Check if the data was saved in the database
        self.assertEqual(WheelSpecification.objects.count(), 2)  # 1 from setUp + 1 from this test
        wheel_spec = WheelSpecification.objects.last()
        self.assertEqual(wheel_spec.form_number, "WHEEL-2025-001")

    def test_wheel_specification_get(self):
        """Test GET /api/forms/wheel-specifications"""
        url = reverse('wheel-specifications')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['success'])
        self.assertEqual(response.data['message'], 'Filtered wheel specification forms fetched successfully.')
        self.assertEqual(len(response.data['data']), 1)
        
        # Check the structure of the response
        wheel_spec_data = response.data['data'][0]
        self.assertIn('fields', wheel_spec_data)
        self.assertIn('formNumber', wheel_spec_data)
        self.assertIn('submittedBy', wheel_spec_data)
        self.assertIn('submittedDate', wheel_spec_data)
        
        # Check specific field values
        self.assertEqual(wheel_spec_data['formNumber'], "WHEEL-2025-001")
        self.assertEqual(wheel_spec_data['submittedBy'], "user_id_123")
        self.assertEqual(wheel_spec_data['submittedDate'], "2025-07-03")
        
        # Check fields structure
        fields = wheel_spec_data['fields']
        self.assertEqual(fields['condemningDia'], "825 (800-900)")
        self.assertEqual(fields['lastShopIssueSize'], "837 (800-900)")
        self.assertEqual(fields['treadDiameterNew'], "915 (900-1000)")
        self.assertEqual(fields['wheelGauge'], "1600 (+2,-1)")
