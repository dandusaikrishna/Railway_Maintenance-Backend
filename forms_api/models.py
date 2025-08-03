from django.db import models

class BogieChecksheet(models.Model):
    # Bogie Details 
    bogie_no = models.CharField("Bogie No.", max_length=50)
    date_of_ioh = models.DateField("Date of IOH", null=True, blank=True)
    incoming_div_and_date = models.CharField("Incoming Div. & Date", max_length=100)
    maker_year_built = models.CharField("Maker & Year Built", max_length=100)
    deficit_components = models.TextField("Deficit of component (if any)", blank=True, null=True)
    
    # Bogie Checksheet fields 
    bogie_frame_condition = models.CharField("Bogie Frame Condition", max_length=50, blank=True, null=True)
    bolster = models.CharField("Bolster", max_length=50, blank=True, null=True)
    bolster_suspension_bracket = models.CharField("Bolster Suspension Bracket", max_length=50, blank=True, null=True)
    lower_spring_seat = models.CharField("Lower Spring Seat", max_length=50, blank=True, null=True)
    axle_guide = models.CharField("Axle Guide", max_length=50, blank=True, null=True)
    axle_guide_assembly = models.CharField("Axle Guide Assembly", max_length=50, blank=True, null=True)
    protective_tubes = models.CharField("Protective Tubes", max_length=50, blank=True, null=True)
    anchor_links = models.CharField("Anchor Links", max_length=50, blank=True, null=True)
    side_bearer = models.CharField("Side Bearer", max_length=50, blank=True, null=True)
    
    # BMBC Checksheet fields
    cylinder_body = models.CharField("Cylinder Body & Dome Cover", max_length=50, blank=True, null=True)
    piston_trunnion = models.CharField("Piston & Trunnion Body", max_length=50, blank=True, null=True)
    adjusting_tube = models.CharField("Adjusting Tube and Screw", max_length=50, blank=True, null=True)
    plunger_spring = models.CharField("Plunger Spring", max_length=50, blank=True, null=True)
    tee_bolt_hex_nut = models.CharField("Tee Bolt, Hex Nut", max_length=50, blank=True, null=True)
    pawl_and_pawl_spring = models.CharField("Pawl and Pawl Spring", max_length=50, blank=True, null=True)
    dust_excluder = models.CharField("Dust Excluder", max_length=50, blank=True, null=True)
    
    # Metadata
    form_number = models.CharField(max_length=50)
    inspection_by = models.CharField(max_length=50, blank=True, null=True)
    inspection_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.form_number} - {self.bogie_no}"

class WheelSpecification(models.Model):
    # Wheel specification fields 
    tread_diameter_new = models.CharField("Tread Diameter (New)", max_length=100, blank=True, null=True)
    last_shop_issue_size = models.CharField("Last Shop Issue Size (Dia.)", max_length=100, blank=True, null=True)
    condemning_dia = models.CharField("Condemning Dia.", max_length=100, blank=True, null=True)
    wheel_gauge = models.CharField("Wheel Gauge (IFD)", max_length=100, blank=True, null=True)
    variation_same_axle = models.CharField("Variation Same Axle", max_length=50, blank=True, null=True)
    variation_same_bogie = models.CharField("Variation Same Bogie", max_length=50, blank=True, null=True)
    variation_same_coach = models.CharField("Variation Same Coach", max_length=50, blank=True, null=True)
    wheel_profile = models.CharField("Wheel Profile", max_length=100, blank=True, null=True)
    intermediate_wwp = models.CharField("Intermediate WWP", max_length=100, blank=True, null=True)
    bearing_seat_diameter = models.CharField("Bearing Seat Diameter", max_length=100, blank=True, null=True)
    roller_bearing_outer_dia = models.CharField("Roller Bearing Outer Dia.", max_length=100, blank=True, null=True)
    roller_bearing_bore_dia = models.CharField("Roller Bearing Bore Dia.", max_length=100, blank=True, null=True)
    roller_bearing_width = models.CharField("Roller Bearing Width", max_length=100, blank=True, null=True)
    axle_box_housing_bore_dia = models.CharField("Axle Box Housing Bore Dia.", max_length=100, blank=True, null=True)
    wheel_disc_width = models.CharField("Wheel Disc Width", max_length=100, blank=True, null=True)
    
    # Metadata
    form_number = models.CharField(max_length=50)
    submitted_by = models.CharField(max_length=50, blank=True, null=True)
    submitted_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.form_number} - Wheel Spec"