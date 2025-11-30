# Tech Park Management System

A comprehensive, professional-grade Tech Park Management System with 3D visualization, room allocation, and complete facility management.

## Features

### Authentication System
- Login/Sign Up - Secure user authentication
- Forgot Password - Security question-based password recovery
- Role-Based Access - Admin, Manager, and User roles with different permissions

### Building Management
- 3D Building Visualization - Interactive 3D view of the entire building
- Floor Plans - Detailed 2D floor layouts with room status
- Occupancy Heatmap - Visual representation of building occupancy
- Lift Status Monitor - Real-time lift operational status

### Room Allocation System
- Room Management - View all rooms with status (Occupied/Vacant/Available)
- Allocate Rooms - Assign vacant rooms to companies
- Release Rooms - Free up occupied rooms
- Search & Filter - Find rooms by status, floor, or occupant
- Full CRUD Operations - Create, Read, Update, Delete room records

### Lift Management
- Lift Monitoring - Track all lifts in the building
- Maintenance Status - View operational and maintenance status
- Capacity Information - Weight and people capacity details
- Employee Assignment - Track responsible personnel

### Facility Maintenance
- Maintenance Tracking - Schedule and track all maintenance activities
- Status Management - Completed, In Progress, Scheduled
- Staff Assignment - Assign maintenance to specific staff members
- Facility Types - HVAC, Elevator, Fire Safety, Plumbing, Electrical, CCTV, etc.

### Employee Management
- Employee Database - Complete employee information
- Department Tracking - Organize by departments and teams
- Salary Management - Track compensation and work hours
- Search & Filter - Find employees quickly
- Full CRUD Operations - Add, edit, delete employee records

### Company Management
- Company Directory - All companies in the tech park
- Industry Classification - Track company industries
- Revenue Tracking - Monitor company revenues
- Employee Count - Track company sizes
- Full CRUD Operations - Manage company records

### Event Management
- Event History - Past events with full details
- Upcoming Events - Future events calendar
- Event Details - Location, attendees, organizer, theme
- Registration Tracking - Track registration requirements and links

### Visitor Log
- Visitor Tracking - Log all visitors
- Check-in/Check-out - Time tracking
- Host Assignment - Link visitors to host employees
- Purpose Tracking - Record visit purposes

### Revenue Analysis
- Monthly Trends - Line charts showing revenue over time
- Product Comparison - Bar charts comparing products
- Market Share - Pie charts showing distribution
- Detailed Breakdown - Table with proof of calculations
- Key Insights - Automated analysis and recommendations
- Growth Metrics - Calculate growth percentages

### Analytics Dashboard
- Department Distribution - Pie chart of employees by department
- Salary Analysis - Average salary by department
- Revenue Trends - Monthly revenue visualization
- Repair Costs - Analysis of maintenance expenses
- Key Metrics - Total employees, companies, repairs, visitors

### Repair Management
- Repair History - Track all repairs
- Cost Tracking - Monitor repair expenses
- Component Details - Number of components replaced
- Vendor Information - Track repair companies

## User Interface Features

### Modern Design
- Professional Color Scheme - Consistent, eye-pleasing colors
- Card-Based Layout - Clean, organized information display
- Responsive Design - Adapts to screen size
- Icon Integration - Visual clarity

### Navigation
- 2-Column Button Layout - Easy access to all features
- Smooth Scrolling - Mouse wheel and trackpad support
- Vertical & Horizontal Scroll - Navigate in any direction
- Search Functionality - Quick filtering on all pages

### Interaction
- Hover Effects - Visual feedback on buttons
- Prominent Action Buttons - Large, visible Edit/Delete/Allocate buttons
- Real-time Updates - Instant refresh after changes
- Status Bar - Live time and user information

## Data Management

### CSV-Based Storage
All data stored in organized CSV files:
- building.csv - Building information
- floors.csv - Floor details
- rooms.csv - Room allocation data
- lifts.csv - Lift information
- facility_maintenance.csv - Maintenance records
- Employee.csv - Employee data
- company_details.csv - Company information
- event_history.csv - Past events
- upcoming_events.csv - Future events
- VisiterLog.csv - Visitor records
- repair.csv - Repair history
- Product_Revenue.csv - Revenue data
- users.csv - User authentication

### Export Functionality
- Export any dataset to CSV
- Export charts to PNG/PDF
- Preserve data for reporting

## Security Features

- Password Protection - Secure login system
- Role-Based Access Control - Different permissions for Admin/Manager/User
- Security Questions - Password recovery mechanism
- Session Management - Proper login/logout handling

## Date Management

- Current Date Integration - All features use current system date
- Future-Proof - Works for any future date
- Timestamp Tracking - Records creation and modification times
- Date Formatting - Consistent date display throughout

## Technical Stack

- Python 3.x - Core programming language
- Tkinter - GUI framework
- Pandas - Data manipulation
- Matplotlib - Data visualization
- NumPy - Numerical operations

## Installation

1. Install required packages:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python main.py
```

## Default Users

- Username: Jelena | Password: 1234 | Role: Admin
- Username: Nandhana | Password: 5678 | Role: Admin
- Username: admin | Password: admin123 | Role: Admin

## Usage Tips

1. Login - Use default credentials or create new account
2. Explore Dashboard - View statistics and quick insights
3. Building Overview - See 3D visualization and occupancy
4. Manage Rooms - Allocate/release rooms to companies
5. Track Maintenance - Schedule and monitor facility maintenance
6. Analyze Revenue - View detailed revenue breakdowns with proof
7. Manage Data - Use Edit/Delete buttons on any record
8. Export Reports - Export data and charts for presentations

## CRUD Operations

All major features support full CRUD operations:
- Create - Add new records via "Add New" button
- Read - View all records with search/filter
- Update - Edit records via "Edit" button
- Delete - Remove records via "Delete" button

## Visualization Features

- 3D Building View - Isometric building visualization
- Floor Plans - Color-coded room layouts
- Occupancy Heatmap - Stacked bar charts
- Lift Status - Visual lift monitoring
- Revenue Charts - Line, bar, and pie charts
- Analytics Graphs - Department and salary analysis

## Color Coding

- Green - Vacant/Available/Operational
- Red - Occupied/Critical
- Yellow - Meeting Rooms/Warnings
- Blue - Information/Secondary
- Purple - Analytics/Special

## Notes

- All data is stored locally in CSV files
- Changes are saved immediately
- Statistics update in real-time
- Scroll with mouse wheel or trackpad
- Use Shift+Scroll for horizontal scrolling

## Future Enhancements

- Database integration (MySQL/PostgreSQL)
- Email notifications
- Mobile app version
- Advanced reporting
- Automated backups
- Multi-language support

## License

Copyright 2024 Tech Park Manager | All Rights Reserved

## Support

For issues or questions, please refer to the documentation or contact the development team.

---

Version: 2.0.0
Last Updated: 2024
Status: Production Ready
