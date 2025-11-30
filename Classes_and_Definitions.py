class Building:
    def __init__(self, name=None, address=None, no_of_floors=None, parking_space=None, no_of_lifts=None, company_occupancy=None, no_of_companies=None, no_of_cctv=None, security=None):
        self.Name = name
        self.Address = address
        self.NoOfFloors = no_of_floors
        self.ParkingSpace = parking_space
        self.NoOfLifts = no_of_lifts
        self.CompanyOccupancy = company_occupancy
        self.NoOfCompanies = no_of_companies
        self.NoOfCCTV = no_of_cctv
        self.Security = security

    def get_name(self):
        return self.Name

    def get_address(self):
        return self.Address

    def get_no_of_floors(self):
        return self.NoOfFloors

    def get_parking_space(self):
        return self.ParkingSpace

    def get_no_of_lifts(self):
        return self.NoOfLifts

    def get_company_occupancy(self):
        return self.CompanyOccupancy

    def get_no_of_companies(self):
        return self.NoOfCompanies

    def get_no_of_cctv(self):
        return self.NoOfCCTV

    def get_security(self):
        return self.Security

    def set_name(self, name):
        self.Name = name

    def set_address(self, address):
        self.Address = address

    def set_no_of_floors(self, no_of_floors):
        self.NoOfFloors = no_of_floors

    def set_parking_space(self, parking_space):
        self.ParkingSpace = parking_space

    def set_no_of_lifts(self, no_of_lifts):
        self.NoOfLifts = no_of_lifts

    def set_company_occupancy(self, company_occupancy):
        self.CompanyOccupancy = company_occupancy

    def set_no_of_companies(self, no_of_companies):
        self.NoOfCompanies = no_of_companies

    def set_no_of_cctv(self, no_of_cctv):
        self.NoOfCCTV = no_of_cctv

    def set_security(self, security):
        self.Security = security

        
class Lift:
    def __init__(self, lift_id=None, location=None, weight_capacity=None, maximum_people_carried=None, emergency_caller=None, fan_working_condition=None, light_working_condition=None, maximum_floors_taken=None, employee_incharge=None, supplier=None):
        self.LiftID = lift_id
        self.Location = location
        self.WeightCapacity = weight_capacity
        self.MaximumPeopleCarried = maximum_people_carried
        self.EmergencyCaller = emergency_caller
        self.FanWorkingCondition = fan_working_condition
        self.LightWorkingCondition = light_working_condition
        self.MaximumFloorsTaken = maximum_floors_taken
        self.EmployeeIncharge = employee_incharge
        self.Supplier = supplier

    def get_lift_id(self):
        return self.LiftID

    def get_location(self):
        return self.Location

    def get_weight_capacity(self):
        return self.WeightCapacity

    def get_maximum_people_carried(self):
        return self.MaximumPeopleCarried

    def get_emergency_caller(self):
        return self.EmergencyCaller

    def get_fan_working_condition(self):
        return self.FanWorkingCondition

    def get_light_working_condition(self):
        return self.LightWorkingCondition

    def get_maximum_floors_taken(self):
        return self.MaximumFloorsTaken

    def get_employee_incharge(self):
        return self.EmployeeIncharge

    def get_supplier(self):
        return self.Supplier

    def set_lift_id(self, lift_id):
        self.LiftID = lift_id

    def set_location(self, location):
        self.Location = location

    def set_weight_capacity(self, weight_capacity):
        self.WeightCapacity = weight_capacity

    def set_maximum_people_carried(self, maximum_people_carried):
        self.MaximumPeopleCarried = maximum_people_carried

    def set_emergency_caller(self, emergency_caller):
        self.EmergencyCaller = emergency_caller

    def set_fan_working_condition(self, fan_working_condition):
        self.FanWorkingCondition = fan_working_condition

    def set_light_working_condition(self, light_working_condition):
        self.LightWorkingCondition = light_working_condition

    def set_maximum_floors_taken(self, maximum_floors_taken):
        self.MaximumFloorsTaken = maximum_floors_taken

    def set_employee_incharge(self, employee_incharge):
        self.EmployeeIncharge = employee_incharge

    def set_supplier(self, supplier):
        self.Supplier = supplier

        
class Employee:
    def __init__(self, name=None, employee_id=None, years_of_experience=None, date_of_join=None, department=None, designation=None, availability=None, team_name=None, work_assigned=None, salary=None, work_hours=None, qualification=None):
        self.Name = name
        self.EmployeeID = employee_id
        self.YearsOfExperience = years_of_experience
        self.DateOfJoin = date_of_join
        self.Department = department
        self.Designation = designation
        self.Availability = availability
        self.TeamName = team_name
        self.WorkAssigned = work_assigned
        self.Salary = salary
        self.WorkHours = work_hours
        self.Qualification = qualification

    def get_name(self):
        return self.Name

    def get_employee_id(self):
        return self.EmployeeID

    def get_years_of_experience(self):
        return self.YearsOfExperience

    def get_date_of_join(self):
        return self.DateOfJoin

    def get_department(self):
        return self.Department

    def get_designation(self):
        return self.Designation

    def get_availability(self):
        return self.Availability

    def get_team_name(self):
        return self.TeamName

    def get_work_assigned(self):
        return self.WorkAssigned

    def get_salary(self):
        return self.Salary

    def get_work_hours(self):
        return self.WorkHours

    def get_qualification(self):
        return self.Qualification

    def set_name(self, name):
        self.Name = name

    def set_employee_id(self, employee_id):
        self.EmployeeID = employee_id

    def set_years_of_experience(self, years_of_experience):
        self.YearsOfExperience = years_of_experience

    def set_date_of_join(self, date_of_join):
        self.DateOfJoin = date_of_join

    def set_department(self, department):
        self.Department = department

    def set_designation(self, designation):
        self.Designation = designation

    def set_availability(self, availability):
        self.Availability = availability

    def set_team_name(self, team_name):
        self.TeamName = team_name

    def set_work_assigned(self, work_assigned):
        self.WorkAssigned = work_assigned

    def set_salary(self, salary):
        self.Salary = salary

    def set_work_hours(self, work_hours):
        self.WorkHours = work_hours

    def set_qualification(self, qualification):
        self.Qualification = qualification


class Employee_Personal:
    def __init__(self, name=None, age=None, gender=None, father_name=None, date_of_birth=None, residential_address=None, blood_group=None, phone_number=None, emergency_contact=None, email_id=None):
        self.Name = name
        self.Age = age
        self.Gender = gender
        self.FatherName = father_name
        self.DateOfBirth = date_of_birth
        self.ResidentialAddress = residential_address
        self.BloodGroup = blood_group
        self.PhoneNumber = phone_number
        self.EmergencyContact = emergency_contact
        self.EmailID = email_id

    def get_name(self):
        return self.Name

    def get_age(self):
        return self.Age

    def get_gender(self):
        return self.Gender

    def get_father_name(self):
        return self.FatherName

    def get_date_of_birth(self):
        return self.DateOfBirth

    def get_residential_address(self):
        return self.ResidentialAddress

    def get_blood_group(self):
        return self.BloodGroup

    def get_phone_number(self):
        return self.PhoneNumber

    def get_emergency_contact(self):
        return self.EmergencyContact

    def get_email_id(self):
        return self.EmailID

    def set_name(self, name):
        self.Name = name

    def set_age(self, age):
        self.Age = age

    def set_gender(self, gender):
        self.Gender = gender

    def set_father_name(self, father_name):
        self.FatherName = father_name

    def set_date_of_birth(self, date_of_birth):
        self.DateOfBirth = date_of_birth

    def set_residential_address(self, residential_address):
        self.ResidentialAddress = residential_address

    def set_blood_group(self, blood_group):
        self.BloodGroup = blood_group

    def set_phone_number(self, phone_number):
        self.PhoneNumber = phone_number

    def set_emergency_contact(self, emergency_contact):
        self.EmergencyContact = emergency_contact

    def set_email_id(self, email_id):
        self.EmailID = email_id


class Room:
    def __init__(self, room_number=None, dimension=None, usage=None, no_of_pc=None, no_of_windows=None, no_of_tables=None, no_of_fans=None, no_of_lights=None, floor_number=None):
        self.RoomNumber = room_number
        self.Dimension = dimension
        self.Usage = usage
        self.NoOfPC = no_of_pc
        self.NoOfWindows = no_of_windows
        self.NoOfTables = no_of_tables
        self.NoOfFans = no_of_fans
        self.NoOfLights = no_of_lights
        self.FloorNumber = floor_number

    def get_room_number(self):
        return self.RoomNumber

    def get_dimension(self):
        return self.Dimension

    def get_usage(self):
        return self.Usage

    def get_no_of_pc(self):
        return self.NoOfPC

    def get_no_of_windows(self):
        return self.NoOfWindows

    def get_no_of_tables(self):
        return self.NoOfTables

    def get_no_of_fans(self):
        return self.NoOfFans

    def get_no_of_lights(self):
        return self.NoOfLights

    def get_floor_number(self):
        return self.FloorNumber

    def set_room_number(self, room_number):
        self.RoomNumber = room_number

    def set_dimension(self, dimension):
        self.Dimension = dimension

    def set_usage(self, usage):
        self.Usage = usage

    def set_no_of_pc(self, no_of_pc):
        self.NoOfPC = no_of_pc

    def set_no_of_windows(self, no_of_windows):
        self.NoOfWindows = no_of_windows

    def set_no_of_tables(self, no_of_tables):
        self.NoOfTables = no_of_tables

    def set_no_of_fans(self, no_of_fans):
        self.NoOfFans = no_of_fans

    def set_no_of_lights(self, no_of_lights):
        self.NoOfLights = no_of_lights

    def set_floor_number(self, floor_number):
        self.FloorNumber = floor_number

        
class Repair:
    def __init__(self, object_repaired=None, repair_charge=None, object_brand=None, company_repaired=None, date=None, number_of_components=None, person_name=None):
        self.ObjectRepaired = object_repaired
        self.RepairCharge = repair_charge
        self.ObjectBrand = object_brand
        self.CompanyRepaired = company_repaired
        self.Date = date
        self.NumberOfComponents = number_of_components
        self.PersonName = person_name

    def get_object_repaired(self):
        return self.ObjectRepaired

    def get_repair_charge(self):
        return self.RepairCharge

    def get_object_brand(self):
        return self.ObjectBrand

    def get_company_repaired(self):
        return self.CompanyRepaired

    def get_date(self):
        return self.Date

    def get_number_of_components(self):
        return self.NumberOfComponents

    def get_person_name(self):
        return self.PersonName

    def set_object_repaired(self, object_repaired):
        self.ObjectRepaired = object_repaired

    def set_repair_charge(self, repair_charge):
        self.RepairCharge = repair_charge

    def set_object_brand(self, object_brand):
        self.ObjectBrand = object_brand

    def set_company_repaired(self, company_repaired):
        self.CompanyRepaired = company_repaired

    def set_date(self, date):
        self.Date = date

    def set_number_of_components(self, number_of_components):
        self.NumberOfComponents = number_of_components

    def set_person_name(self, person_name):
        self.PersonName = person_name

        
class Floor:
    def __init__(self, no_of_rooms=None, no_of_washrooms=None, no_of_vending_machines=None, no_of_water_dispenser=None, floor_area=None, floor_number=None, no_of_meeting_rooms=None):
        self.NoOfRooms = no_of_rooms
        self.NoOfWashrooms = no_of_washrooms
        self.NoOfVendingMachines = no_of_vending_machines
        self.NoOfWaterDispenser = no_of_water_dispenser
        self.FloorArea = floor_area
        self.FloorNumber = floor_number
        self.NoOfMeetingRooms = no_of_meeting_rooms

    def get_no_of_rooms(self):
        return self.NoOfRooms

    def get_no_of_washrooms(self):
        return self.NoOfWashrooms

    def get_no_of_vending_machines(self):
        return self.NoOfVendingMachines

    def get_no_of_water_dispenser(self):
        return self.NoOfWaterDispenser

    def get_floor_area(self):
        return self.FloorArea

    def get_floor_number(self):
        return self.FloorNumber

    def get_no_of_meeting_rooms(self):
        return self.NoOfMeetingRooms

    def set_no_of_rooms(self, no_of_rooms):
        self.NoOfRooms = no_of_rooms

    def set_no_of_washrooms(self, no_of_washrooms):
        self.NoOfWashrooms = no_of_washrooms

    def set_no_of_vending_machines(self, no_of_vending_machines):
        self.NoOfVendingMachines = no_of_vending_machines

    def set_no_of_water_dispenser(self, no_of_water_dispenser):
        self.NoOfWaterDispenser = no_of_water_dispenser

    def set_floor_area(self, floor_area):
        self.FloorArea = floor_area

    def set_floor_number(self, floor_number):
        self.FloorNumber = floor_number

    def set_no_of_meeting_rooms(self, no_of_meeting_rooms):
        self.NoOfMeetingRooms = no_of_meeting_rooms

 

class VisitorLog:
    def __init__(self, visitor_name=None, contact_details=None, purpose_of_visit=None, check_in_time=None, check_out_time=None, host_employee=None):
        self.VisitorName = visitor_name
        self.ContactDetails = contact_details
        self.PurposeOfVisit = purpose_of_visit
        self.CheckInTime = check_in_time
        self.CheckOutTime = check_out_time
        self.HostEmployee = host_employee

    def get_visitor_name(self):
        return self.VisitorName

    def get_contact_details(self):
        return self.ContactDetails

    def get_purpose_of_visit(self):
        return self.PurposeOfVisit

    def get_check_in_time(self):
        return self.CheckInTime

    def get_check_out_time(self):
        return self.CheckOutTime

    def get_host_employee(self):
        return self.HostEmployee

    def set_visitor_name(self, visitor_name):
        self.VisitorName = visitor_name

    def set_contact_details(self, contact_details):
        self.ContactDetails = contact_details

    def set_purpose_of_visit(self, purpose_of_visit):
        self.PurposeOfVisit = purpose_of_visit

    def set_check_in_time(self, check_in_time):
        self.CheckInTime = check_in_time

    def set_check_out_time(self, check_out_time):
        self.CheckOutTime = check_out_time

    def set_host_employee(self, host_employee):
        self.HostEmployee = host_employee

        
class FacilityMaintenance:
    def __init__(self, maintenance_id=None, facility_type=None, description=None, scheduled_date=None, completion_status=None, assigned_staff=None):
        self.maintenanceID = maintenance_id
        self.facilityType = facility_type
        self.Description = description
        self.ScheduledData = scheduled_date
        self.CompletionStatus = completion_status
        self.AssignedStaff = assigned_staff

    def get_maintenance_id(self):
        return self.maintenanceID

    def get_facility_type(self):
        return self.facilityType

    def get_description(self):
        return self.Description

    def get_scheduled_data(self):
        return self.ScheduledData

    def get_completion_status(self):
        return self.CompletionStatus

    def get_assigned_staff(self):
        return self.AssignedStaff

    def set_maintenance_id(self, maintenance_id):
        self.maintenanceID = maintenance_id

    def set_facility_type(self, facility_type):
        self.facilityType = facility_type

    def set_description(self, description):
        self.Description = description

    def set_scheduled_data(self, scheduled_data):
        self.ScheduledData = scheduled_data

    def set_completion_status(self, completion_status):
        self.CompletionStatus = completion_status

    def set_assigned_staff(self, assigned_staff):
        self.AssignedStaff = assigned_staff

        
class Event:
    def __init__(self, event_name=None, date=None, time=None, location=None, attendees_limit=None, organizer=None, description=None, theme=None, registration_required=None, registration_link=None):
        self.EventName = event_name
        self.Date = date
        self.Time = time
        self.Location = location
        self.AttendeesLimit = attendees_limit
        self.Organizer = organizer
        self.Description = description
        self.Theme = theme
        self.RegistrationRequired = registration_required
        self.RegistrationLink = registration_link

    def get_event_name(self):
        return self.EventName

    def get_date(self):
        return self.Date

    def get_time(self):
        return self.Time

    def get_location(self):
        return self.Location

    def get_attendees_limit(self):
        return self.AttendeesLimit

    def get_organizer(self):
        return self.Organizer

    def get_description(self):
        return self.Description

    def get_theme(self):
        return self.Theme

    def is_registration_required(self):
        return self.RegistrationRequired

    def get_registration_link(self):
        return self.RegistrationLink

    def set_event_name(self, event_name):
        self.EventName = event_name

    def set_date(self, date):
        self.Date = date

    def set_time(self, time):
        self.Time = time

    def set_location(self, location):
        self.Location = location

    def set_attendees_limit(self, attendees_limit):
        self.AttendeesLimit = attendees_limit

    def set_organizer(self, organizer):
        self.Organizer = organizer

    def set_description(self, description):
        self.Description = description

    def set_theme(self, theme):
        self.Theme = theme

    def set_registration_required(self, registration_required):
        self.RegistrationRequired = registration_required

    def set_registration_link(self, registration_link):
        self.RegistrationLink = registration_link


class TechEvent(Event):
    def __init__(self, techFocus=None):
        super().__init__()
        self.TechnologyFocus = techFocus
        
    def get_topic(self):
        return self.TechnologyFocus
    
    def set_topic(self, techFocus):
        self.TechnologyFocus = techFocus
    

class CommunityEvent(Event):
    def __init__(self, topic=None, Community=None):
        super().__init__()
        self.Topic = topic
        self.CommunityType = Community
    
    def get_topic(self):
        return self.Topic

    def get_community_type(self):
        return self.CommunityType

    def set_topic(self, topic):
        self.Topic = topic

    def set_community_type(self, community_type):
        self.CommunityType = community_type
        

class Company:
    def __init__(self, name=None, address=None, industry=None, employee_count=None, revenue=None):
        self.Name = name
        self.Address = address
        self.Industry = industry
        self.EmployeeCount = employee_count
        self.Revenue = revenue

    def get_name(self):
        return self.Name

    def get_address(self):
        return self.Address

    def get_industry(self):
        return self.Industry

    def get_employee_count(self):
        return self.EmployeeCount

    def get_revenue(self):
        return self.Revenue

    def set_name(self, name):
        self.Name = name

    def set_address(self, address):
        self.Address = address

    def set_industry(self, industry):
        self.Industry = industry

    def set_employee_count(self, employee_count):
        self.EmployeeCount = employee_count

    def set_revenue(self, revenue):
        self.Revenue = revenue
