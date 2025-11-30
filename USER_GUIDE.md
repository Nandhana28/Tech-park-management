# Tech Park Manager - User Guide

## Building Overview Features

### 3D Building Visualization

The 3D view includes interactive controls:

#### Controls
- Zoom Slider (0.5x - 2.0x): Zoom in/out to see building details
- Elevation Slider (0 - 90 degrees): Change vertical viewing angle
- Rotation Slider (0 - 360 degrees): Rotate building horizontally

#### Visual Information
- Color-Coded Floors:
  - Red: High occupancy (>80%)
  - Orange: Medium occupancy (50-80%)
  - Green: Low occupancy (<50%)
- Floor Labels: Shows floor number and occupancy (e.g., "5O/2V" = 5 Occupied, 2 Vacant)
- Building Name: Displayed at the top

#### Tips
1. Start with default view (Zoom: 1.0, Elevation: 20, Rotation: 45)
2. Use Zoom: 1.5-2.0 to see floor details clearly
3. Try Elevation: 45 for best overview
4. Rotation: 0 for front view, 90 for side view

---

## Floor Plans

### Detailed Room Visualization

Each room card shows:
- Room Number: Large, bold identifier
- Occupant/Usage: Company name or room type
- Dimensions: Room size in sq ft
- Capacity: For offices - number of PCs and tables
- Status Color:
  - Red: Occupied
  - Green: Vacant
  - Yellow: Meeting/Shared spaces

### Features
- Shadow Effects: 3D-like appearance
- Icon Integration: Visual indicators for capacity
- 4-Column Layout: More rooms visible at once
- Interactive Selection: Choose any floor from dropdown

---

## Lift Status Monitor

### Enhanced Display

Each lift shows:
- Lift ID: Clear identification
- Location: North/South Wing
- Capacity: 
  - Maximum people
  - Weight capacity
  - Maximum floors
- Status: Operational/Under Maintenance
- Personnel:
  - Employee in charge
  - Supplier/Manufacturer

### Status Colors
- Green: Operational
- Yellow: Under Maintenance
- Red: Out of Service

---

## Room Allocation

### Action Buttons

Every room card has prominent buttons:

#### For Vacant Rooms:
- Edit: Modify room details
- Allocate: Assign to a company

#### For Occupied Rooms:
- Edit: Modify room details
- Release: Free up the room

### Allocation Process
1. Click Allocate on vacant room
2. Select company from dropdown
3. Click Allocate Room
4. Room status updates immediately

### Release Process
1. Click Release on occupied room
2. Confirm the action
3. Room becomes vacant

---

## Revenue Analysis

### Detailed Breakdown

The revenue section includes:

#### Summary Cards
- Total Revenue
- Average Monthly Revenue
- Top Performing Product
- Highest Revenue Value

#### Proof Table
Shows for each product:
- Total Revenue: Sum of all months
- Average Monthly: Mean revenue
- Best Month: Peak performance month
- Growth %: Year-over-year growth

#### Key Insights
- Total products tracked
- Best performing product
- Products needing attention
- Average per product
- Report timestamp

### Why This Matters
- Transparency: See exact calculations
- Accountability: Proof of numbers
- Decision Making: Identify trends
- Reporting: Export for presentations

---

## Visual Improvements

### Better Fit
- All plots sized to fit screen
- No overflow or cut-off content
- Proper spacing and margins
- Responsive to window size

### Scrolling
- Vertical Scroll: Mouse wheel or trackpad
- Horizontal Scroll: Shift + Mouse wheel
- Smooth Navigation: Swipe in any direction

### Action Buttons
- Larger Size: Easy to click
- High Contrast: Clearly visible
- Color Coded: 
  - Yellow = Edit
  - Red = Delete
  - Green = Allocate/Add
- Always Visible: No hover required

---

## Date Management

### Current Date Integration
- All timestamps use system date
- Reports show generation time
- Future-proof for any date
- Consistent formatting throughout

### Where Dates Appear
- Status bar (live clock)
- Quick insights panel
- Revenue reports
- Maintenance schedules
- Event calendars

---

## Troubleshooting

### If 3D View Doesn't Load
1. Check if matplotlib is installed
2. Try adjusting zoom to 1.0
3. Reset elevation to 20 and rotation to 45

### If Statistics Show Zero
- Data files are loading individually
- Zero means no records, not an error
- Add data via "Add New" buttons

### If Buttons Not Visible
- Scroll down on the card
- Check if you're logged in as Admin/Manager
- Regular users have view-only access

---

## Best Practices

### For Managers
1. Daily: Check building overview for occupancy
2. Weekly: Review room allocations
3. Monthly: Analyze revenue reports
4. As Needed: Schedule maintenance

### For Admins
1. Keep employee records updated
2. Monitor lift status regularly
3. Track visitor logs
4. Maintain company directory

### For All Users
1. Use search to find records quickly
2. Export data for offline analysis
3. Check insights panel for quick stats
4. Report issues via proper channels

---

## Quick Reference

### Keyboard Shortcuts
- Enter: Submit login
- Mouse Wheel: Scroll vertically
- Shift + Wheel: Scroll horizontally
- Drag: Rotate 3D view (if enabled)

### Common Tasks
- Add Record: Click "Add New" button
- Edit Record: Click "Edit" on card
- Delete Record: Click "Delete" on card
- Allocate Room: Click "Allocate" on vacant room
- Export Data: Click "Export to CSV"

### Navigation
- Dashboard: Main statistics and insights
- Building Overview: 3D view and floor plans
- Room Allocation: Manage room assignments
- Analytics: Detailed charts and graphs
- Revenue: Financial analysis with proof

---

## Support

For additional help:
1. Check README.md for feature list
2. Review this guide for detailed instructions
3. Contact system administrator
4. Report bugs to development team

---

Last Updated: 2024
Version: 2.0.0
Status: Production Ready
