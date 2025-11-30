import tkinter as tk
from tkinter import ttk, messagebox, filedialog, simpledialog
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from datetime import datetime
import os
import csv

from Classes_and_Definitions import Repair, Employee, Event, Company, VisitorLog

# Color scheme
COLORS = {
    'primary': '#2C3E50',
    'secondary': '#3498DB',
    'accent': '#E74C3C',
    'success': '#27AE60',
    'warning': '#F39C12',
    'light': '#ECF0F1',
    'dark': '#34495E',
    'white': '#FFFFFF',
    'hover': '#5DADE2',
    'purple': '#9B59B6',
    'teal': '#1ABC9C'
}

# Global variable for current user
current_user = None
current_user_role = None

def load_users():
    """Load users from CSV file"""
    try:
        df = pd.read_csv("Datasets/users.csv")
        return df
    except:
        # Create default users if file doesn't exist
        default_users = pd.DataFrame({
            'Username': ['Jelena', 'Nandhana', 'admin'],
            'Password': ['1234', '5678', 'admin123'],
            'Email': ['jelena@techpark.com', 'nandhana@techpark.com', 'admin@techpark.com'],
            'SecurityQuestion': ['What is your favorite color?', 'What is your pet name?', 'What city were you born in?'],
            'SecurityAnswer': ['Blue', 'Max', 'Seattle'],
            'Role': ['Admin', 'Admin', 'Admin']
        })
        default_users.to_csv("Datasets/users.csv", index=False)
        return default_users

def save_users(df):
    """Save users to CSV file"""
    df.to_csv("Datasets/users.csv", index=False)

def sign_up():
    """Sign up new user"""
    signup_window = tk.Toplevel(window)
    signup_window.title(' Sign Up')
    signup_window.geometry('500x600')
    signup_window.configure(bg=COLORS['light'])
    signup_window.transient(window)
    signup_window.grab_set()
    
    # Center the window
    signup_window.update_idletasks()
    x = (signup_window.winfo_screenwidth() // 2) - (500 // 2)
    y = (signup_window.winfo_screenheight() // 2) - (600 // 2)
    signup_window.geometry(f'500x600+{x}+{y}')
    
    # Header
    header = tk.Frame(signup_window, bg=COLORS['secondary'], height=80)
    header.pack(fill=tk.X)
    header.pack_propagate(False)
    tk.Label(header, text=' Create New Account', font=('Arial', 20, 'bold'),
            bg=COLORS['secondary'], fg=COLORS['white']).pack(pady=25)
    
    # Form
    form = tk.Frame(signup_window, bg=COLORS['white'])
    form.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
    
    fields = {}
    field_configs = [
        ('Username', 'text'),
        ('Password', 'password'),
        ('Confirm Password', 'password'),
        ('Email', 'text'),
        ('Security Question', 'text'),
        ('Security Answer', 'text')
    ]
    
    for label_text, field_type in field_configs:
        tk.Label(form, text=label_text, font=('Arial', 11, 'bold'),
                bg=COLORS['white'], fg=COLORS['dark']).pack(anchor='w', pady=(10, 2))
        
        entry = tk.Entry(form, font=('Arial', 12), width=40)
        if field_type == 'password':
            entry.config(show='●')
        entry.pack(pady=(0, 5))
        fields[label_text] = entry
    
    def submit_signup():
        username = fields['Username'].get().strip()
        password = fields['Password'].get().strip()
        confirm_pass = fields['Confirm Password'].get().strip()
        email = fields['Email'].get().strip()
        security_q = fields['Security Question'].get().strip()
        security_a = fields['Security Answer'].get().strip()
        
        if not all([username, password, email, security_q, security_a]):
            messagebox.showerror('Error', 'All fields are required!')
            return
        
        if password != confirm_pass:
            messagebox.showerror('Error', 'Passwords do not match!')
            return
        
        users_df = load_users()
        if username in users_df['Username'].values:
            messagebox.showerror('Error', 'Username already exists!')
            return
        
        # Add new user
        new_user = pd.DataFrame({
            'Username': [username],
            'Password': [password],
            'Email': [email],
            'SecurityQuestion': [security_q],
            'SecurityAnswer': [security_a],
            'Role': ['User']
        })
        users_df = pd.concat([users_df, new_user], ignore_index=True)
        save_users(users_df)
        
        messagebox.showinfo('Success', f'Account created successfully!\nWelcome, {username}!')
        signup_window.destroy()
    
    tk.Button(form, text='Create Account', command=submit_signup,
             font=('Arial', 12, 'bold'), bg=COLORS['success'], fg=COLORS['white'],
             width=20, height=2, cursor='hand2').pack(pady=20)

def forgot_password():
    """Forgot password recovery"""
    forgot_window = tk.Toplevel(window)
    forgot_window.title(' Forgot Password')
    forgot_window.geometry('500x500')
    forgot_window.configure(bg=COLORS['light'])
    forgot_window.transient(window)
    forgot_window.grab_set()
    
    # Center the window
    forgot_window.update_idletasks()
    x = (forgot_window.winfo_screenwidth() // 2) - (500 // 2)
    y = (forgot_window.winfo_screenheight() // 2) - (500 // 2)
    forgot_window.geometry(f'500x500+{x}+{y}')
    
    # Header
    header = tk.Frame(forgot_window, bg=COLORS['warning'], height=80)
    header.pack(fill=tk.X)
    header.pack_propagate(False)
    tk.Label(header, text=' Password Recovery', font=('Arial', 20, 'bold'),
            bg=COLORS['warning'], fg=COLORS['white']).pack(pady=25)
    
    # Form
    form = tk.Frame(forgot_window, bg=COLORS['white'])
    form.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
    
    tk.Label(form, text='Enter your username:', font=('Arial', 11, 'bold'),
            bg=COLORS['white'], fg=COLORS['dark']).pack(anchor='w', pady=(20, 5))
    username_entry = tk.Entry(form, font=('Arial', 12), width=40)
    username_entry.pack(pady=(0, 20))
    
    question_label = tk.Label(form, text='', font=('Arial', 11),
                             bg=COLORS['white'], fg=COLORS['dark'], wraplength=400)
    question_label.pack(anchor='w', pady=(10, 5))
    
    answer_entry = tk.Entry(form, font=('Arial', 12), width=40)
    
    new_password_label = tk.Label(form, text='New Password:', font=('Arial', 11, 'bold'),
                                  bg=COLORS['white'], fg=COLORS['dark'])
    new_password_entry = tk.Entry(form, font=('Arial', 12), width=40, show='●')
    
    def verify_user():
        username = username_entry.get().strip()
        if not username:
            messagebox.showerror('Error', 'Please enter username!')
            return
        
        users_df = load_users()
        user_data = users_df[users_df['Username'] == username]
        
        if user_data.empty:
            messagebox.showerror('Error', 'Username not found!')
            return
        
        question = user_data.iloc[0]['SecurityQuestion']
        question_label.config(text=f'Security Question: {question}')
        answer_entry.pack(pady=(0, 20))
        
        new_password_label.pack(anchor='w', pady=(10, 5))
        new_password_entry.pack(pady=(0, 20))
        
        verify_btn.config(state='disabled')
        reset_btn.pack(pady=10)
    
    def reset_password():
        username = username_entry.get().strip()
        answer = answer_entry.get().strip()
        new_password = new_password_entry.get().strip()
        
        if not all([answer, new_password]):
            messagebox.showerror('Error', 'All fields are required!')
            return
        
        users_df = load_users()
        user_data = users_df[users_df['Username'] == username]
        
        if user_data.iloc[0]['SecurityAnswer'].lower() != answer.lower():
            messagebox.showerror('Error', 'Incorrect security answer!')
            return
        
        # Update password
        users_df.loc[users_df['Username'] == username, 'Password'] = new_password
        save_users(users_df)
        
        messagebox.showinfo('Success', 'Password reset successfully!')
        forgot_window.destroy()
    
    verify_btn = tk.Button(form, text='Verify', command=verify_user,
                          font=('Arial', 12, 'bold'), bg=COLORS['secondary'],
                          fg=COLORS['white'], width=20, height=2, cursor='hand2')
    verify_btn.pack(pady=10)
    
    reset_btn = tk.Button(form, text='Reset Password', command=reset_password,
                          font=('Arial', 12, 'bold'), bg=COLORS['success'],
                          fg=COLORS['white'], width=20, height=2, cursor='hand2')

def login():
    """Login user"""
    global current_user, current_user_role
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if username == '' or password == '':
        messagebox.showerror('❌ Error', 'Please enter both username and password.')
        return
    
    users_df = load_users()
    user_data = users_df[(users_df['Username'] == username) & (users_df['Password'] == password)]
    
    if user_data.empty:
        messagebox.showerror('❌ Error', 'Invalid username or password.')
        return
    
    current_user = username
    current_user_role = user_data.iloc[0]['Role']
    messagebox.showinfo('✅ Success', f'Welcome back, {username}!')
    window.withdraw()
    open_main_window(username, current_user_role)

def bind_mousewheel(canvas, horizontal_canvas=None):
    """Enable mouse wheel scrolling for canvas (vertical and horizontal)"""
    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    def _on_shift_mousewheel(event):
        if horizontal_canvas:
            horizontal_canvas.xview_scroll(int(-1*(event.delta/120)), "units")
    
    def _bind_to_mousewheel(event):
        canvas.bind_all("<MouseWheel>", _on_mousewheel)
        if horizontal_canvas:
            canvas.bind_all("<Shift-MouseWheel>", _on_shift_mousewheel)
    
    def _unbind_from_mousewheel(event):
        canvas.unbind_all("<MouseWheel>")
        if horizontal_canvas:
            canvas.unbind_all("<Shift-MouseWheel>")
    
    canvas.bind('<Enter>', _bind_to_mousewheel)
    canvas.bind('<Leave>', _unbind_from_mousewheel)


class MyApp:
    def __init__(self, root, username="User", role="User"):
        self.root = root
        self.username = username
        self.role = role
        self.root.title(" Tech Park Manager - Dashboard")
        self.root.configure(bg=COLORS['light'])
        
        # Header Frame
        header_frame = tk.Frame(root, bg=COLORS['primary'], height=80)
        header_frame.pack(side=tk.TOP, fill=tk.X)
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(header_frame, text=' TECH PARK MANAGER', 
                              font=('Arial', 28, 'bold'), 
                              bg=COLORS['primary'], fg=COLORS['white'])
        title_label.pack(side=tk.LEFT, padx=30, pady=20)
        
        user_info = tk.Label(header_frame, text=f' {username} ({role})', 
                            font=('Arial', 14), 
                            bg=COLORS['primary'], fg=COLORS['light'])
        user_info.pack(side=tk.RIGHT, padx=30)
        
        # Main container
        main_container = tk.Frame(root, bg=COLORS['light'])
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Left panel - Buttons (2 columns)
        left_panel = tk.Frame(main_container, bg=COLORS['light'])
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        features_label = tk.Label(left_panel, text=' FEATURES', 
                                 font=('Arial', 20, 'bold'), 
                                 bg=COLORS['light'], fg=COLORS['primary'])
        features_label.pack(pady=(0, 20))
        
        # Button configurations with icons - 2 columns
        buttons_config = [
            ("️ Building Overview", self.open_building_overview, COLORS['primary']),
            ("️ Floor Plans", self.open_floor_plans, COLORS['teal']),
            (" Room Allocation", self.open_room_allocation, COLORS['secondary']),
            (" Lift Management", self.open_lift_management, COLORS['warning']),
            (" Facility Maintenance", self.open_facility_maintenance, COLORS['accent']),
            (" Employee Management", self.open_employee_details, COLORS['success']),
            (" Event History", self.open_event_window, COLORS['purple']),
            (" Upcoming Events", self.open_upcoming_events, COLORS['warning']),
            (" Visitor Log", self.open_visitor_log_history, COLORS['dark']),
            (" Revenue Analysis", self.open_monthly_revenue, COLORS['teal'])
        ]
        
        # Create buttons in 2-column grid
        for i in range(0, len(buttons_config), 2):
            row_frame = tk.Frame(left_panel, bg=COLORS['light'])
            row_frame.pack(fill=tk.X, pady=8)
            
            # First button in row
            text1, command1, color1 = buttons_config[i]
            btn1 = tk.Button(row_frame, text=text1, 
                           font=('Arial', 13, 'bold'),
                           width=22, height=2,
                           bg=color1, fg=COLORS['white'],
                           activebackground=COLORS['hover'],
                           activeforeground=COLORS['white'],
                           relief=tk.RAISED,
                           bd=3,
                           cursor='hand2',
                           command=command1)
            btn1.pack(side=tk.LEFT, padx=(0, 8), expand=True, fill=tk.BOTH)
            self.add_hover_effect(btn1, color1)
            
            # Second button in row (if exists)
            if i + 1 < len(buttons_config):
                text2, command2, color2 = buttons_config[i + 1]
                btn2 = tk.Button(row_frame, text=text2, 
                               font=('Arial', 13, 'bold'),
                               width=22, height=2,
                               bg=color2, fg=COLORS['white'],
                               activebackground=COLORS['hover'],
                               activeforeground=COLORS['white'],
                               relief=tk.RAISED,
                               bd=3,
                               cursor='hand2',
                               command=command2)
                btn2.pack(side=tk.LEFT, padx=(8, 0), expand=True, fill=tk.BOTH)
                self.add_hover_effect(btn2, color2)
        
        # Right panel - Statistics Dashboard
        right_panel = tk.Frame(main_container, bg=COLORS['light'], width=450)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, padx=(10, 0))
        right_panel.pack_propagate(False)
        
        stats_label = tk.Label(right_panel, text=' STATISTICS', 
                              font=('Arial', 18, 'bold'), 
                              bg=COLORS['light'], fg=COLORS['primary'])
        stats_label.pack(pady=(0, 10))
        
        # Load statistics with individual error handling
        stats_data = []
        
        # Try to load each dataset individually
        try:
            emp_df = pd.read_csv("Datasets/Employee.csv")
            stats_data.append((" Total Employees", len(emp_df), COLORS['success']))
        except:
            stats_data.append((" Total Employees", 0, COLORS['success']))
        
        try:
            repair_df = pd.read_csv("Datasets/repair.csv")
            stats_data.append((" Total Repairs", len(repair_df), COLORS['accent']))
        except:
            stats_data.append((" Total Repairs", 0, COLORS['accent']))
        
        try:
            visitor_df = pd.read_csv("Datasets/VisiterLog.csv")
            stats_data.append((" Total Visitors", len(visitor_df), COLORS['warning']))
        except:
            stats_data.append((" Total Visitors", 0, COLORS['warning']))
        
        try:
            event_df = pd.read_csv("Datasets/event_history.csv")
            stats_data.append((" Past Events", len(event_df), COLORS['purple']))
        except:
            stats_data.append((" Past Events", 0, COLORS['purple']))
        
        try:
            upcoming_df = pd.read_csv("Datasets/upcoming_events.csv")
            stats_data.append((" Upcoming Events", len(upcoming_df), COLORS['teal']))
        except:
            stats_data.append((" Upcoming Events", 0, COLORS['teal']))
        
        try:
            rooms_df = pd.read_csv("Datasets/rooms.csv")
            stats_data.append((" Total Rooms", len(rooms_df), COLORS['secondary']))
        except:
            stats_data.append((" Total Rooms", 0, COLORS['secondary']))
        
        # Display statistics cards
        for title, value, color in stats_data:
            stat_card = tk.Frame(right_panel, bg=COLORS['white'], relief=tk.RAISED, bd=2)
            stat_card.pack(fill=tk.X, pady=4)
            
            card_header = tk.Frame(stat_card, bg=color, height=28)
            card_header.pack(fill=tk.X)
            card_header.pack_propagate(False)
            
            tk.Label(card_header, text=title, font=('Arial', 10, 'bold'),
                    bg=color, fg=COLORS['white']).pack(pady=4)
            
            tk.Label(stat_card, text=str(value), font=('Arial', 28, 'bold'),
                    bg=COLORS['white'], fg=color).pack(pady=8)
        
        # Quick insights
        insights_card = tk.Frame(right_panel, bg=COLORS['white'], relief=tk.RAISED, bd=2)
        insights_card.pack(fill=tk.BOTH, expand=True, pady=(10, 0))
        
        tk.Label(insights_card, text=" Quick Insights", font=('Arial', 12, 'bold'),
                bg=COLORS['white'], fg=COLORS['primary']).pack(pady=8)
        
        insights_text = tk.Text(insights_card, height=7, font=('Arial', 9),
                               bg=COLORS['white'], fg=COLORS['dark'],
                               relief=tk.FLAT, padx=12, pady=5, wrap=tk.WORD)
        insights_text.pack(fill=tk.BOTH, expand=True, padx=8, pady=(0, 8))
        
        # Calculate insights safely
        try:
            emp_df = pd.read_csv("Datasets/Employee.csv")
            repair_df = pd.read_csv("Datasets/repair.csv")
            rooms_df = pd.read_csv("Datasets/rooms.csv")
            
            avg_salary = emp_df['Salary'].mean()
            top_dept = emp_df['Department'].value_counts().idxmax()
            dept_count = emp_df['Department'].value_counts().max()
            occupied_rooms = len(rooms_df[rooms_df['Status'] == 'Occupied'])
            
            insights_text.insert(tk.END, f" Avg Salary: ${avg_salary:,.0f}\n\n")
            insights_text.insert(tk.END, f" Top Dept: {top_dept}\n   ({dept_count} employees)\n\n")
            insights_text.insert(tk.END, f" Occupied Rooms: {occupied_rooms}/{len(rooms_df)}\n\n")
        except:
            insights_text.insert(tk.END, " Loading insights...\n\n")
        
        insights_text.insert(tk.END, f"✅ Status: Active\n")
        insights_text.insert(tk.END, f" User: {username}\n")
        insights_text.insert(tk.END, f" Date: {datetime.now().strftime('%Y-%m-%d')}")
        
        insights_text.config(state=tk.DISABLED)
        
        # Status bar
        status_bar = tk.Label(root, text=f" {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | Status: Active", 
                            font=('Arial', 10), 
                            bg=COLORS['dark'], fg=COLORS['white'],
                            anchor=tk.W, padx=10)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        self.update_status_bar(status_bar)
    
    def add_hover_effect(self, button, original_color):
        def on_enter(e):
            button['bg'] = COLORS['hover']
        
        def on_leave(e):
            button['bg'] = original_color
        
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
    
    def update_status_bar(self, status_bar):
        status_bar.config(text=f" {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | Status: Active | User: {self.username} ({self.role})")
        self.root.after(1000, lambda: self.update_status_bar(status_bar))

    
    def open_building_overview(self):
        """Open 3D building overview with all visualizations"""
        from building_visualization import create_3d_building_view, create_occupancy_heatmap, create_lift_status_display
        
        building_window = tk.Toplevel(self.root)
        building_window.title("️ Building Overview")
        building_window.state('zoomed')
        building_window.configure(bg=COLORS['light'])
        
        # Header
        header = tk.Frame(building_window, bg=COLORS['primary'], height=70)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        
        tk.Label(header, text='️ TECH PARK TOWER - BUILDING OVERVIEW', 
                font=('Arial', 24, 'bold'), 
                bg=COLORS['primary'], fg=COLORS['white']).pack(pady=15)
        
        # Create scrollable canvas
        canvas = tk.Canvas(building_window, bg=COLORS['light'])
        scrollbar = ttk.Scrollbar(building_window, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=COLORS['light'])
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        bind_mousewheel(canvas)
        
        try:
            # Load building data
            building_df = pd.read_csv("Datasets/building.csv")
            building = building_df.iloc[0]
            
            # Building Info Card
            info_frame = tk.Frame(scrollable_frame, bg=COLORS['white'], relief=tk.RAISED, bd=2)
            info_frame.pack(fill=tk.X, padx=20, pady=20)
            
            tk.Label(info_frame, text=" Building Information", 
                    font=('Arial', 18, 'bold'), bg=COLORS['white'], 
                    fg=COLORS['primary']).pack(pady=15)
            
            info_grid = tk.Frame(info_frame, bg=COLORS['white'])
            info_grid.pack(fill=tk.X, padx=30, pady=(0, 20))
            
            info_data = [
                (" Name", building['Name']),
                (" Address", building['Address']),
                ("️ Floors", building['NoOfFloors']),
                ("🅿️ Parking Spaces", building['ParkingSpace']),
                (" Lifts", building['NoOfLifts']),
                (" Occupancy", building['CompanyOccupancy']),
                (" Companies", building['NoOfCompanies']),
                (" CCTV Cameras", building['NoOfCCTV']),
                (" Security", building['Security'])
            ]
            
            for i, (label, value) in enumerate(info_data):
                row = i // 3
                col = i % 3
                
                card = tk.Frame(info_grid, bg=COLORS['light'], relief=tk.RAISED, bd=1)
                card.grid(row=row, column=col, padx=10, pady=10, sticky='ew')
                
                tk.Label(card, text=label, font=('Arial', 10, 'bold'),
                        bg=COLORS['light'], fg=COLORS['dark']).pack(pady=(10, 2))
                tk.Label(card, text=str(value), font=('Arial', 14, 'bold'),
                        bg=COLORS['light'], fg=COLORS['secondary']).pack(pady=(2, 10))
            
            for i in range(3):
                info_grid.columnconfigure(i, weight=1)
            
            # 3D Building View - Full Width Row with Controls
            view_3d_frame = tk.Frame(scrollable_frame, bg=COLORS['white'], relief=tk.RAISED, bd=2)
            view_3d_frame.pack(fill=tk.X, padx=20, pady=(0, 20))
            
            # Header with controls
            header_3d = tk.Frame(view_3d_frame, bg=COLORS['white'])
            header_3d.pack(fill=tk.X, padx=15, pady=15)
            
            tk.Label(header_3d, text="️ 3D Building Visualization", 
                    font=('Arial', 16, 'bold'), bg=COLORS['white'], 
                    fg=COLORS['primary']).pack(side=tk.LEFT)
            
            # Zoom controls
            control_frame = tk.Frame(header_3d, bg=COLORS['white'])
            control_frame.pack(side=tk.RIGHT)
            
            zoom_var = tk.DoubleVar(value=1.0)
            elev_var = tk.IntVar(value=20)
            azim_var = tk.IntVar(value=45)
            
            tk.Label(control_frame, text="Zoom:", font=('Arial', 10, 'bold'),
                    bg=COLORS['white']).pack(side=tk.LEFT, padx=5)
            
            zoom_scale = tk.Scale(control_frame, from_=0.5, to=2.0, resolution=0.1,
                                 orient=tk.HORIZONTAL, variable=zoom_var,
                                 bg=COLORS['white'], length=100)
            zoom_scale.pack(side=tk.LEFT, padx=5)
            
            tk.Label(control_frame, text="Elevation:", font=('Arial', 10, 'bold'),
                    bg=COLORS['white']).pack(side=tk.LEFT, padx=5)
            
            elev_scale = tk.Scale(control_frame, from_=0, to=90, resolution=5,
                                 orient=tk.HORIZONTAL, variable=elev_var,
                                 bg=COLORS['white'], length=100)
            elev_scale.pack(side=tk.LEFT, padx=5)
            
            tk.Label(control_frame, text="Rotation:", font=('Arial', 10, 'bold'),
                    bg=COLORS['white']).pack(side=tk.LEFT, padx=5)
            
            azim_scale = tk.Scale(control_frame, from_=0, to=360, resolution=15,
                                 orient=tk.HORIZONTAL, variable=azim_var,
                                 bg=COLORS['white'], length=100)
            azim_scale.pack(side=tk.LEFT, padx=5)
            
            # Canvas for 3D view
            canvas_3d_container = tk.Frame(view_3d_frame, bg=COLORS['white'])
            canvas_3d_container.pack(fill=tk.BOTH, expand=True, padx=15, pady=(0, 15))
            
            def update_3d_view(*args):
                for widget in canvas_3d_container.winfo_children():
                    widget.destroy()
                
                fig_3d = create_3d_building_view(building_window, 
                                                 elev=elev_var.get(), 
                                                 azim=azim_var.get(),
                                                 zoom=zoom_var.get())
                if fig_3d:
                    canvas_3d = FigureCanvasTkAgg(fig_3d, master=canvas_3d_container)
                    canvas_3d.draw()
                    canvas_3d.get_tk_widget().pack(fill=tk.BOTH, expand=True)
            
            # Bind updates
            zoom_var.trace('w', update_3d_view)
            elev_var.trace('w', update_3d_view)
            azim_var.trace('w', update_3d_view)
            
            # Initial draw
            update_3d_view()
            
            # Occupancy Heatmap - Full Width Row
            occupancy_frame = tk.Frame(scrollable_frame, bg=COLORS['white'], relief=tk.RAISED, bd=2)
            occupancy_frame.pack(fill=tk.X, padx=20, pady=(0, 20))
            
            tk.Label(occupancy_frame, text=" Occupancy Overview", 
                    font=('Arial', 16, 'bold'), bg=COLORS['white'], 
                    fg=COLORS['primary']).pack(pady=15)
            
            fig_occ = create_occupancy_heatmap()
            if fig_occ:
                canvas_occ = FigureCanvasTkAgg(fig_occ, master=occupancy_frame)
                canvas_occ.draw()
                canvas_occ.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
            
            # Lift Status - Full Width Row
            lift_frame = tk.Frame(scrollable_frame, bg=COLORS['white'], relief=tk.RAISED, bd=2)
            lift_frame.pack(fill=tk.X, padx=20, pady=(0, 20))
            
            tk.Label(lift_frame, text=" Lift Status Monitor", 
                    font=('Arial', 16, 'bold'), bg=COLORS['white'], 
                    fg=COLORS['primary']).pack(pady=15)
            
            fig_lift = create_lift_status_display()
            if fig_lift:
                canvas_lift = FigureCanvasTkAgg(fig_lift, master=lift_frame)
                canvas_lift.draw()
                canvas_lift.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
            
        except Exception as e:
            tk.Label(scrollable_frame, text=f"⚠️ Error loading building data: {str(e)}", 
                    font=('Arial', 14), bg=COLORS['light'], 
                    fg=COLORS['accent']).pack(pady=50)
        
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(20, 0), pady=(0, 20))
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, pady=(0, 20), padx=(0, 20))
    
    def open_floor_plans(self):
        """Open interactive floor plans"""
        from building_visualization import create_floor_plan
        
        floor_window = tk.Toplevel(self.root)
        floor_window.title("️ Floor Plans")
        floor_window.state('zoomed')
        floor_window.configure(bg=COLORS['light'])
        
        # Header
        header = tk.Frame(floor_window, bg=COLORS['teal'], height=70)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        
        tk.Label(header, text='️ INTERACTIVE FLOOR PLANS', 
                font=('Arial', 24, 'bold'), 
                bg=COLORS['teal'], fg=COLORS['white']).pack(side=tk.LEFT, padx=30, pady=15)
        
        # Floor selector
        floors_df = pd.read_csv("Datasets/floors.csv")
        floor_numbers = floors_df['FloorNumber'].tolist()
        
        selected_floor = tk.StringVar(value=floor_numbers[0])
        
        tk.Label(header, text="Select Floor:", font=('Arial', 12, 'bold'),
                bg=COLORS['teal'], fg=COLORS['white']).pack(side=tk.RIGHT, padx=(0, 10))
        
        floor_combo = ttk.Combobox(header, textvariable=selected_floor, 
                                   values=floor_numbers, state='readonly',
                                   font=('Arial', 12), width=15)
        floor_combo.pack(side=tk.RIGHT, padx=(0, 30))
        
        # Canvas for floor plan
        plan_frame = tk.Frame(floor_window, bg=COLORS['white'], relief=tk.RAISED, bd=2)
        plan_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        def update_floor_plan(*args):
            for widget in plan_frame.winfo_children():
                widget.destroy()
            
            floor = selected_floor.get()
            
            tk.Label(plan_frame, text=f"Floor {floor} Layout", 
                    font=('Arial', 16, 'bold'), bg=COLORS['white'], 
                    fg=COLORS['primary']).pack(pady=15)
            
            fig = create_floor_plan(floor)
            if fig:
                canvas_plan = FigureCanvasTkAgg(fig, master=plan_frame)
                canvas_plan.draw()
                canvas_plan.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        selected_floor.trace('w', update_floor_plan)
        update_floor_plan()
    
    def open_room_allocation(self):
        """Open room allocation management"""
        from crud_operations import create_record_dialog, edit_record_dialog, delete_record
        
        room_window = tk.Toplevel(self.root)
        room_window.title(" Room Allocation")
        room_window.state('zoomed')
        room_window.configure(bg=COLORS['light'])
        
        # Header
        header = tk.Frame(room_window, bg=COLORS['secondary'], height=70)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        
        tk.Label(header, text=' ROOM ALLOCATION MANAGEMENT', 
                font=('Arial', 24, 'bold'), 
                bg=COLORS['secondary'], fg=COLORS['white']).pack(side=tk.LEFT, padx=30, pady=15)
        
        # Control Frame
        control_frame = tk.Frame(room_window, bg=COLORS['light'])
        control_frame.pack(fill=tk.X, padx=20, pady=10)
        
        tk.Label(control_frame, text=" Search:", 
                font=('Arial', 12), bg=COLORS['light']).pack(side=tk.LEFT, padx=5)
        
        search_var = tk.StringVar()
        search_entry = tk.Entry(control_frame, textvariable=search_var, 
                               font=('Arial', 12), width=30)
        search_entry.pack(side=tk.LEFT, padx=5)
        
        # Filter by status
        tk.Label(control_frame, text="Status:", 
                font=('Arial', 12), bg=COLORS['light']).pack(side=tk.LEFT, padx=(20, 5))
        
        status_var = tk.StringVar(value="All")
        status_combo = ttk.Combobox(control_frame, textvariable=status_var, 
                                    values=["All", "Occupied", "Vacant", "Available"],
                                    state='readonly', font=('Arial', 11), width=12)
        status_combo.pack(side=tk.LEFT, padx=5)
        
        # Scrollable Frame
        canvas = tk.Canvas(room_window, bg=COLORS['light'])
        scrollbar = ttk.Scrollbar(room_window, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=COLORS['light'])
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        bind_mousewheel(canvas)
        
        def update_display():
            try:
                rooms_df = pd.read_csv("Datasets/rooms.csv")
                
                for widget in scrollable_frame.winfo_children():
                    widget.destroy()
                
                search_term = search_var.get().lower()
                status_filter = status_var.get()
                
                filtered_df = rooms_df[rooms_df.apply(lambda row: search_term in str(row).lower(), axis=1)]
                
                if status_filter != "All":
                    filtered_df = filtered_df[filtered_df['Status'] == status_filter]
                
                # Create room cards in 3-column layout
                current_row = None
                for index, (idx, room) in enumerate(filtered_df.iterrows()):
                    if index % 3 == 0:
                        current_row = tk.Frame(scrollable_frame, bg=COLORS['light'])
                        current_row.pack(fill=tk.X, padx=20, pady=8)
                    
                    # Determine card color
                    if room['Status'] == 'Occupied':
                        card_color = COLORS['accent']
                    elif room['Status'] == 'Vacant':
                        card_color = COLORS['success']
                    else:
                        card_color = COLORS['warning']
                    
                    card = tk.Frame(current_row, bg=COLORS['white'], 
                                   relief=tk.RAISED, bd=2, width=380, height=280)
                    card.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
                    card.pack_propagate(False)
                    
                    # Header
                    header_card = tk.Frame(card, bg=card_color, height=30)
                    header_card.pack(fill=tk.X)
                    header_card.pack_propagate(False)
                    tk.Label(header_card, text=f"🚪 Room {room['RoomNumber']}", 
                            font=('Arial', 10, 'bold'), 
                            bg=card_color, fg=COLORS['white']).pack(pady=5)
                    
                    # Content
                    content = tk.Frame(card, bg=COLORS['white'])
                    content.pack(fill=tk.BOTH, expand=True, padx=10, pady=8)
                    
                    info = [
                        ("📏", "Size", room['Dimension']),
                        ("🏢", "Floor", f"Floor {room['FloorNumber']}"),
                        ("💼", "Usage", room['Usage']),
                        ("👤", "Occupied", room['OccupiedBy'][:20]),
                        ("✅", "Status", room['Status'])
                    ]
                    
                    for icon, label, value in info:
                        row_frame = tk.Frame(content, bg=COLORS['white'])
                        row_frame.pack(fill=tk.X, pady=1)
                        tk.Label(row_frame, text=icon, font=('Arial', 9),
                                bg=COLORS['white']).pack(side=tk.LEFT)
                        tk.Label(row_frame, text=f"{label}:", font=('Arial', 8, 'bold'),
                                bg=COLORS['white'], fg=COLORS['dark'], width=9, anchor='w').pack(side=tk.LEFT)
                        tk.Label(row_frame, text=str(value), font=('Arial', 8),
                                bg=COLORS['white'], fg=COLORS['dark'], anchor='w').pack(side=tk.LEFT)
                    
                    # Action buttons - Always visible and prominent
                    if self.role in ['Admin', 'Manager']:
                        action_frame = tk.Frame(card, bg=COLORS['light'])
                        action_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=5, pady=5)
                        
                        fields = ['RoomNumber', 'FloorNumber', 'Dimension', 'Usage', 'NoOfPC', 
                                 'NoOfWindows', 'NoOfTables', 'NoOfFans', 'NoOfLights', 
                                 'OccupiedBy', 'Status']
                        
                        tk.Button(action_frame, text="✏️", 
                                font=('Arial', 9, 'bold'),
                                bg=COLORS['warning'], fg=COLORS['white'],
                                cursor='hand2', relief=tk.RAISED, bd=2,
                                width=4, height=1,
                                command=lambda i=idx: [edit_record_dialog(room_window, "Room", fields, 
                                                                          "Datasets/rooms.csv", i, update_display)]).pack(side=tk.LEFT, padx=2, expand=True, fill=tk.X)
                        
                        if room['Status'] == 'Vacant':
                            tk.Button(action_frame, text="✅ Allocate", 
                                    font=('Arial', 8, 'bold'),
                                    bg=COLORS['success'], fg=COLORS['white'],
                                    cursor='hand2', relief=tk.RAISED, bd=2,
                                    width=8, height=1,
                                    command=lambda i=idx: self.allocate_room(i, update_display)).pack(side=tk.LEFT, padx=2, expand=True, fill=tk.X)
                        else:
                            tk.Button(action_frame, text="🔓 Release", 
                                    font=('Arial', 8, 'bold'),
                                    bg=COLORS['accent'], fg=COLORS['white'],
                                    cursor='hand2', relief=tk.RAISED, bd=2,
                                    width=8, height=1,
                                    command=lambda i=idx: self.release_room(i, update_display)).pack(side=tk.LEFT, padx=2, expand=True, fill=tk.X)
            
            except Exception as e:
                tk.Label(scrollable_frame, text=f"⚠️ Error loading rooms: {str(e)}", 
                        font=('Arial', 14), bg=COLORS['light'], 
                        fg=COLORS['accent']).pack(pady=50)
        
        search_var.trace('w', lambda *args: update_display())
        status_var.trace('w', lambda *args: update_display())
        update_display()
        
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(20, 0), pady=(0, 20))
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, pady=(0, 20), padx=(0, 20))
    
    def release_room(self, room_index, callback):
        """Release a room from current occupant"""
        if not messagebox.askyesno('Confirm Release', 
                                   'Are you sure you want to release this room?\nIt will become vacant.'):
            return
        
        try:
            rooms_df = pd.read_csv("Datasets/rooms.csv")
            rooms_df.at[room_index, 'OccupiedBy'] = 'Vacant'
            rooms_df.at[room_index, 'Status'] = 'Vacant'
            rooms_df.to_csv("Datasets/rooms.csv", index=False)
            
            messagebox.showinfo('Success', 'Room released successfully!')
            if callback:
                callback()
        except Exception as e:
            messagebox.showerror('Error', f'Failed to release room:\n{str(e)}')
    
    def allocate_room(self, room_index, callback):
        """Allocate a room to a company"""
        dialog = tk.Toplevel(self.root)
        dialog.title(" Allocate Room")
        dialog.geometry('500x400')
        dialog.configure(bg=COLORS['light'])
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Center dialog
        dialog.update_idletasks()
        x = (dialog.winfo_screenwidth() // 2) - (500 // 2)
        y = (dialog.winfo_screenheight() // 2) - (400 // 2)
        dialog.geometry(f'500x400+{x}+{y}')
        
        # Header
        header = tk.Frame(dialog, bg=COLORS['success'], height=70)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        tk.Label(header, text=' Allocate Room to Company', font=('Arial', 16, 'bold'),
                bg=COLORS['success'], fg=COLORS['white']).pack(pady=20)
        
        # Form
        form = tk.Frame(dialog, bg=COLORS['white'])
        form.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
        
        # Load companies
        companies_df = pd.read_csv("Datasets/company_details.csv")
        company_names = companies_df['Name'].tolist()
        
        tk.Label(form, text='Select Company:', font=('Arial', 12, 'bold'),
                bg=COLORS['white'], fg=COLORS['dark']).pack(anchor='w', pady=(20, 5))
        
        company_var = tk.StringVar()
        company_combo = ttk.Combobox(form, textvariable=company_var, 
                                     values=company_names, state='readonly',
                                     font=('Arial', 12), width=40)
        company_combo.pack(pady=(0, 20))
        
        def submit():
            company = company_var.get()
            if not company:
                messagebox.showerror('Error', 'Please select a company!')
                return
            
            try:
                rooms_df = pd.read_csv("Datasets/rooms.csv")
                rooms_df.at[room_index, 'OccupiedBy'] = company
                rooms_df.at[room_index, 'Status'] = 'Occupied'
                rooms_df.to_csv("Datasets/rooms.csv", index=False)
                
                messagebox.showinfo('Success', f'Room allocated to {company} successfully!')
                dialog.destroy()
                if callback:
                    callback()
            except Exception as e:
                messagebox.showerror('Error', f'Failed to allocate room:\n{str(e)}')
        
        tk.Button(form, text='✅ Allocate Room', command=submit,
                 font=('Arial', 12, 'bold'), bg=COLORS['success'], fg=COLORS['white'],
                 width=20, height=2, cursor='hand2').pack(pady=20)
        
        tk.Button(form, text='❌ Cancel', command=dialog.destroy,
                 font=('Arial', 12, 'bold'), bg=COLORS['accent'], fg=COLORS['white'],
                 width=20, height=2, cursor='hand2').pack()
    
    def open_lift_management(self):
        """Open lift management system"""
        from crud_operations import create_record_dialog, edit_record_dialog, delete_record
        
        fields = ['LiftID', 'Location', 'WeightCapacity', 'MaximumPeopleCarried', 
                 'EmergencyCaller', 'FanWorkingCondition', 'LightWorkingCondition', 
                 'MaximumFloorsTaken', 'EmployeeIncharge', 'Supplier', 'Status']
        
        def build_lift_card(card, row, index):
            # Header
            status_color = COLORS['success'] if row['Status'] == 'Operational' else COLORS['warning']
            header = tk.Frame(card, bg=status_color, height=30)
            header.pack(fill=tk.X)
            header.pack_propagate(False)
            tk.Label(header, text=f"🛗 {row['LiftID']}", 
                    font=('Arial', 10, 'bold'), 
                    bg=status_color, fg=COLORS['white']).pack(pady=5)
            
            # Content
            content = tk.Frame(card, bg=COLORS['white'])
            content.pack(fill=tk.BOTH, expand=True, padx=10, pady=8)
            
            info = [
                ("📍", row['Location'][:20]),
                ("⚖️", f"{row['WeightCapacity']}"),
                ("👥", f"{row['MaximumPeopleCarried']} people"),
                ("🏢", f"{row['MaximumFloorsTaken']} floors"),
                ("👤", row['EmployeeIncharge'][:18]),
                ("✅", row['Status'])
            ]
            
            for icon, value in info:
                row_frame = tk.Frame(content, bg=COLORS['white'])
                row_frame.pack(fill=tk.X, pady=1)
                tk.Label(row_frame, text=icon, font=('Arial', 9),
                        bg=COLORS['white']).pack(side=tk.LEFT, padx=2)
                tk.Label(row_frame, text=str(value), font=('Arial', 8),
                        bg=COLORS['white'], fg=COLORS['dark'], anchor='w').pack(side=tk.LEFT)
        
        self.create_2column_crud_window("Lift Management", "🛗", COLORS['warning'], 
                                       "Datasets/lifts.csv", fields, build_lift_card, 240)
    
    def open_facility_maintenance(self):
        """Open facility maintenance tracking"""
        from crud_operations import create_record_dialog, edit_record_dialog, delete_record
        
        fields = ['MaintenanceID', 'FacilityType', 'Description', 'ScheduledDate', 
                 'CompletionStatus', 'AssignedStaff']
        
        def build_maintenance_card(card, row, index):
            # Header
            if row['CompletionStatus'] == 'Completed':
                status_color = COLORS['success']
            elif row['CompletionStatus'] == 'In Progress':
                status_color = COLORS['warning']
            else:
                status_color = COLORS['secondary']
            
            header = tk.Frame(card, bg=status_color, height=30)
            header.pack(fill=tk.X)
            header.pack_propagate(False)
            tk.Label(header, text=f"🔧 {row['MaintenanceID']}", 
                    font=('Arial', 10, 'bold'), 
                    bg=status_color, fg=COLORS['white']).pack(pady=5)
            
            # Content
            content = tk.Frame(card, bg=COLORS['white'])
            content.pack(fill=tk.BOTH, expand=True, padx=10, pady=8)
            
            info = [
                ("🏢", row['FacilityType'][:18]),
                ("📝", row['Description'][:25]),
                ("📅", row['ScheduledDate']),
                ("✅", row['CompletionStatus']),
                ("👤", row['AssignedStaff'][:18])
            ]
            
            for icon, value in info:
                row_frame = tk.Frame(content, bg=COLORS['white'])
                row_frame.pack(fill=tk.X, pady=1)
                tk.Label(row_frame, text=icon, font=('Arial', 9),
                        bg=COLORS['white']).pack(side=tk.LEFT, padx=2)
                tk.Label(row_frame, text=str(value), font=('Arial', 8),
                        bg=COLORS['white'], fg=COLORS['dark'], anchor='w').pack(side=tk.LEFT)
        
        self.create_2column_crud_window("Facility Maintenance", "🔧", COLORS['accent'], 
                                       "Datasets/facility_maintenance.csv", fields, build_maintenance_card, 230)
    


    
    def create_2column_crud_window(self, title, icon, color, csv_file, fields, card_builder, card_height=250):
        """Generic function to create 3-column card layout windows with CRUD operations"""
        from crud_operations import create_record_dialog, edit_record_dialog, delete_record
        
        window = tk.Toplevel(self.root)
        window.title(f"{icon} {title}")
        window.state('zoomed')
        window.configure(bg=COLORS['light'])
        
        # Header
        header = tk.Frame(window, bg=color, height=70)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        
        tk.Label(header, text=f'{icon} {title.upper()}', 
                font=('Arial', 22, 'bold'), 
                bg=color, fg=COLORS['white']).pack(side=tk.LEFT, padx=30, pady=15)
        
        # Add button in header
        if self.role in ['Admin', 'Manager']:
            add_btn = tk.Button(header, text="➕ Add New", 
                              font=('Arial', 12, 'bold'),
                              bg=COLORS['success'], fg=COLORS['white'],
                              cursor='hand2', relief=tk.RAISED, bd=3,
                              width=12, height=1,
                              command=lambda: create_record_dialog(window, title, fields, csv_file, update_display))
            add_btn.pack(side=tk.RIGHT, padx=30, pady=15)
        
        # Search and Export Frame
        control_frame = tk.Frame(window, bg=COLORS['light'])
        control_frame.pack(fill=tk.X, padx=20, pady=10)
        
        tk.Label(control_frame, text="🔍 Search:", 
                font=('Arial', 11, 'bold'), bg=COLORS['light']).pack(side=tk.LEFT, padx=5)
        
        search_var = tk.StringVar()
        search_entry = tk.Entry(control_frame, textvariable=search_var, 
                               font=('Arial', 11), width=30)
        search_entry.pack(side=tk.LEFT, padx=5)
        
        export_btn = tk.Button(control_frame, text="📥 Export to CSV", 
                              font=('Arial', 10, 'bold'),
                              bg=COLORS['success'], fg=COLORS['white'],
                              cursor='hand2', relief=tk.RAISED, bd=2,
                              width=15, height=1,
                              command=lambda: self.export_data(csv_file))
        export_btn.pack(side=tk.RIGHT, padx=5)
        
        # Scrollable Frame
        canvas = tk.Canvas(window, bg=COLORS['light'])
        scrollbar = ttk.Scrollbar(window, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=COLORS['light'])
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        bind_mousewheel(canvas)
        
        def update_display():
            try:
                df = pd.read_csv(csv_file)
                
                for widget in scrollable_frame.winfo_children():
                    widget.destroy()
                
                search_term = search_var.get().lower()
                filtered_df = df[df.apply(lambda row: search_term in str(row).lower(), axis=1)]
                
                if len(filtered_df) == 0:
                    tk.Label(scrollable_frame, text="No records found", 
                            font=('Arial', 14), bg=COLORS['light'], 
                            fg=COLORS['dark']).pack(pady=50)
                    return
                
                # Create rows for 3-column layout
                current_row = None
                for idx, (index, row) in enumerate(filtered_df.iterrows()):
                    if idx % 3 == 0:
                        current_row = tk.Frame(scrollable_frame, bg=COLORS['light'])
                        current_row.pack(fill=tk.X, padx=20, pady=8)
                    
                    # Create card
                    card = tk.Frame(current_row, bg=COLORS['white'], 
                                   relief=tk.RAISED, bd=2, width=400, height=card_height)
                    card.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
                    card.pack_propagate(False)
                    
                    # Build card content
                    card_builder(card, row, index)
                    
                    # Add action buttons if admin/manager
                    if self.role in ['Admin', 'Manager']:
                        action_frame = tk.Frame(card, bg=COLORS['light'])
                        action_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=5, pady=5)
                        
                        tk.Button(action_frame, text="✏️ Edit", 
                                font=('Arial', 9, 'bold'),
                                bg=COLORS['warning'], fg=COLORS['white'],
                                cursor='hand2', relief=tk.RAISED, bd=2,
                                width=8, height=1,
                                command=lambda idx=index: [edit_record_dialog(window, title, fields, csv_file, idx, update_display)]).pack(side=tk.LEFT, padx=2, expand=True, fill=tk.X)
                        
                        tk.Button(action_frame, text="🗑️ Delete", 
                                font=('Arial', 9, 'bold'),
                                bg=COLORS['accent'], fg=COLORS['white'],
                                cursor='hand2', relief=tk.RAISED, bd=2,
                                width=8, height=1,
                                command=lambda idx=index: delete_record(window, title, csv_file, idx, update_display)).pack(side=tk.LEFT, padx=2, expand=True, fill=tk.X)
            
            except Exception as e:
                tk.Label(scrollable_frame, text=f"⚠️ Error loading data: {str(e)}", 
                        font=('Arial', 14), bg=COLORS['light'], 
                        fg=COLORS['accent']).pack(pady=50)
        
        search_var.trace('w', lambda *args: update_display())
        update_display()
        
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(20, 0), pady=(0, 20))
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, pady=(0, 20), padx=(0, 20))
    
    def open_repair_window(self):
        fields = ['Object Repaired', 'Repair Charge', 'Object Brand', 'Company Repaired', 
                 'Date', 'Number of components', 'Person Name']
        
        def build_repair_card(card, row, index):
            # Header with object name
            header = tk.Frame(card, bg=COLORS['secondary'], height=30)
            header.pack(fill=tk.X)
            header.pack_propagate(False)
            tk.Label(header, text=f"🔧 {row['Object Repaired'][:20]}", 
                    font=('Arial', 10, 'bold'), 
                    bg=COLORS['secondary'], fg=COLORS['white']).pack(pady=5)
            
            # Content
            content = tk.Frame(card, bg=COLORS['white'])
            content.pack(fill=tk.BOTH, expand=True, padx=10, pady=8)
            
            info = [
                ("💰", row['Repair Charge']),
                ("🏷️", row['Object Brand'][:18]),
                ("🏢", row['Company Repaired'][:18]),
                ("📅", row['Date']),
                ("🔩", f"{row['Number of components']} parts"),
                ("👤", row['Person Name'][:18])
            ]
            
            for icon, value in info:
                row_frame = tk.Frame(content, bg=COLORS['white'])
                row_frame.pack(fill=tk.X, pady=1)
                tk.Label(row_frame, text=icon, font=('Arial', 9),
                        bg=COLORS['white']).pack(side=tk.LEFT, padx=2)
                tk.Label(row_frame, text=str(value), font=('Arial', 8),
                        bg=COLORS['white'], fg=COLORS['dark'], anchor='w').pack(side=tk.LEFT)
        
        self.create_2column_crud_window("Repair Management", "🔧", COLORS['secondary'], 
                                       "Datasets/repair.csv", fields, build_repair_card, 250)
    
    def open_employee_details(self):
        fields = ['Name', 'EmployeeID', 'YearsOfExperience', 'DateOfJoin', 'Department', 
                 'Designation', 'Availability', 'TeamName', 'WorkAssigned', 'Salary', 
                 'WorkHours', 'Qualification']
        
        def build_employee_card(card, row, index):
            # Header
            header = tk.Frame(card, bg=COLORS['success'], height=30)
            header.pack(fill=tk.X)
            header.pack_propagate(False)
            tk.Label(header, text=f"👤 {row['Name'][:20]}", 
                    font=('Arial', 10, 'bold'), 
                    bg=COLORS['success'], fg=COLORS['white']).pack(pady=5)
            
            # Content
            content = tk.Frame(card, bg=COLORS['white'])
            content.pack(fill=tk.BOTH, expand=True, padx=10, pady=8)
            
            info = [
                ("🆔", row['EmployeeID']),
                ("🏢", row['Department'][:18]),
                ("💼", row['Designation'][:18]),
                ("📅", f"{row['YearsOfExperience']} yrs exp"),
                ("👥", row['TeamName'][:18]),
                ("💰", f"${row['Salary']}"),
                ("⏰", f"{row['WorkHours']} hrs")
            ]
            
            for icon, value in info:
                row_frame = tk.Frame(content, bg=COLORS['white'])
                row_frame.pack(fill=tk.X, pady=1)
                tk.Label(row_frame, text=icon, font=('Arial', 9),
                        bg=COLORS['white']).pack(side=tk.LEFT, padx=2)
                tk.Label(row_frame, text=str(value), font=('Arial', 8),
                        bg=COLORS['white'], fg=COLORS['dark'], anchor='w').pack(side=tk.LEFT)
        
        self.create_2column_crud_window("Employee Management", "👥", COLORS['success'], 
                                       "Datasets/Employee.csv", fields, build_employee_card, 260)
    


    
    def open_event_window(self):
        fields = ['Event Name', 'Date', 'Time', 'Location', 'Attendees Limit', 'Organizer',
                 'Description', 'Theme', 'Registration required', 'Registration link']
        
        def build_event_card(card, row, index):
            # Header
            header = tk.Frame(card, bg=COLORS['purple'], height=30)
            header.pack(fill=tk.X)
            header.pack_propagate(False)
            tk.Label(header, text=f"🎉 {row['Event Name'][:22]}", 
                    font=('Arial', 10, 'bold'), 
                    bg=COLORS['purple'], fg=COLORS['white']).pack(pady=5)
            
            # Content
            content = tk.Frame(card, bg=COLORS['white'])
            content.pack(fill=tk.BOTH, expand=True, padx=10, pady=8)
            
            info = [
                ("📅", row['Date']),
                ("⏰", row['Time']),
                ("📍", row['Location'][:18]),
                ("👥", f"{row['Attendees Limit']} people"),
                ("👤", row['Organizer'][:18]),
                ("🎨", row['Theme'][:18])
            ]
            
            for icon, value in info:
                row_frame = tk.Frame(content, bg=COLORS['white'])
                row_frame.pack(fill=tk.X, pady=1)
                tk.Label(row_frame, text=icon, font=('Arial', 9),
                        bg=COLORS['white']).pack(side=tk.LEFT, padx=2)
                tk.Label(row_frame, text=str(value), font=('Arial', 8),
                        bg=COLORS['white'], fg=COLORS['dark'], anchor='w').pack(side=tk.LEFT)
        
        self.create_2column_crud_window("Event History", "🎉", COLORS['purple'], 
                                       "Datasets/event_history.csv", fields, build_event_card, 250)
    
    def open_upcoming_events(self):
        fields = ['Event Name', 'Date', 'Time', 'Location', 'Attendees Limit', 'Organizer',
                 'Description', 'Theme', 'Registration Required', 'Registration Link']
        
        def build_event_card(card, row, index):
            # Header
            header = tk.Frame(card, bg=COLORS['warning'], height=30)
            header.pack(fill=tk.X)
            header.pack_propagate(False)
            tk.Label(header, text=f"📅 {row['Event Name'][:22]}", 
                    font=('Arial', 10, 'bold'), 
                    bg=COLORS['warning'], fg=COLORS['white']).pack(pady=5)
            
            # Content
            content = tk.Frame(card, bg=COLORS['white'])
            content.pack(fill=tk.BOTH, expand=True, padx=10, pady=8)
            
            info = [
                ("📅", row['Date']),
                ("⏰", row['Time']),
                ("📍", row['Location'][:18]),
                ("👥", f"{row['Attendees Limit']} people"),
                ("👤", row['Organizer'][:18]),
                ("🎨", row['Theme'][:18])
            ]
            
            for icon, value in info:
                row_frame = tk.Frame(content, bg=COLORS['white'])
                row_frame.pack(fill=tk.X, pady=1)
                tk.Label(row_frame, text=icon, font=('Arial', 9),
                        bg=COLORS['white']).pack(side=tk.LEFT, padx=2)
                tk.Label(row_frame, text=str(value), font=('Arial', 8),
                        bg=COLORS['white'], fg=COLORS['dark'], anchor='w').pack(side=tk.LEFT)
        
        self.create_2column_crud_window("Upcoming Events", "📅", COLORS['warning'], 
                                       "Datasets/upcoming_events.csv", fields, build_event_card, 250)
    
    def open_visitor_log_history(self):
        fields = ['VisitorName', 'ContactDetails', 'PurposeOfVisit', 'CheckInTime', 
                 'CheckOutTime', 'HostEmployee']
        
        def build_visitor_card(card, row, index):
            # Header
            header = tk.Frame(card, bg=COLORS['dark'], height=30)
            header.pack(fill=tk.X)
            header.pack_propagate(False)
            tk.Label(header, text=f"👤 {row['VisitorName'][:20]}", 
                    font=('Arial', 10, 'bold'), 
                    bg=COLORS['dark'], fg=COLORS['white']).pack(pady=5)
            
            # Content
            content = tk.Frame(card, bg=COLORS['white'])
            content.pack(fill=tk.BOTH, expand=True, padx=10, pady=8)
            
            info = [
                ("📞", row['ContactDetails'][:20]),
                ("💼", row['PurposeOfVisit'][:20]),
                ("🕐", row['CheckInTime']),
                ("🕑", row['CheckOutTime']),
                ("👥", row['HostEmployee'][:18])
            ]
            
            for icon, value in info:
                row_frame = tk.Frame(content, bg=COLORS['white'])
                row_frame.pack(fill=tk.X, pady=1)
                tk.Label(row_frame, text=icon, font=('Arial', 9),
                        bg=COLORS['white']).pack(side=tk.LEFT, padx=2)
                tk.Label(row_frame, text=str(value), font=('Arial', 8),
                        bg=COLORS['white'], fg=COLORS['dark'], anchor='w').pack(side=tk.LEFT)
        
        self.create_2column_crud_window("Visitor Log History", "👥", COLORS['dark'], 
                                       "Datasets/VisiterLog.csv", fields, build_visitor_card, 230)

    
    def open_monthly_revenue(self):
        """Open enhanced revenue analysis window"""
        revenue_window = tk.Toplevel(self.root)
        revenue_window.title(" Revenue Analysis")
        revenue_window.state('zoomed')
        revenue_window.configure(bg=COLORS['light'])
        
        # Header
        header = tk.Frame(revenue_window, bg=COLORS['teal'], height=70)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        
        tk.Label(header, text=' REVENUE ANALYSIS', 
                font=('Arial', 26, 'bold'), 
                bg=COLORS['teal'], fg=COLORS['white']).pack(pady=15)
        
        # Create scrollable canvas
        canvas = tk.Canvas(revenue_window, bg=COLORS['light'])
        scrollbar = ttk.Scrollbar(revenue_window, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=COLORS['light'])
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        bind_mousewheel(canvas)
        
        try:
            df = pd.read_csv("Datasets/Product_Revenue.csv")
            
            # Container for charts
            charts_container = tk.Frame(scrollable_frame, bg=COLORS['light'])
            charts_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
            
            # Chart 1: Line Chart - Revenue Trends
            chart1_frame = tk.Frame(charts_container, bg=COLORS['white'], relief=tk.RAISED, bd=2)
            chart1_frame.pack(fill=tk.BOTH, pady=(0, 20))
            
            tk.Label(chart1_frame, text=" Monthly Revenue Trends", 
                    font=('Arial', 14, 'bold'), bg=COLORS['white'], 
                    fg=COLORS['primary']).pack(pady=10)
            
            fig1 = Figure(figsize=(11, 4), dpi=80)
            ax1 = fig1.add_subplot(111)
            fig1.patch.set_facecolor(COLORS['white'])
            ax1.set_facecolor('#F8F9FA')
            
            colors_line = ['#3498DB', '#E74C3C', '#27AE60', '#F39C12', '#9B59B6', '#1ABC9C']
            
            for idx, column in enumerate(df.columns[1:7]):  # First 6 products
                ax1.plot(df['Month'], df[column], 
                       marker='o', linewidth=2.5, 
                       markersize=8, label=column,
                       color=colors_line[idx % len(colors_line)])
            
            ax1.set_xlabel('Month', fontsize=12, fontweight='bold')
            ax1.set_ylabel('Revenue ($)', fontsize=12, fontweight='bold')
            ax1.set_title('Product Revenue Over Time', fontsize=14, fontweight='bold', pad=15)
            ax1.legend(fontsize=10, loc='best', framealpha=0.9)
            ax1.grid(True, alpha=0.3, linestyle='--')
            plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45, ha='right')
            fig1.tight_layout()
            
            canvas1 = FigureCanvasTkAgg(fig1, master=chart1_frame)
            canvas1.draw()
            canvas1.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
            
            # Row with 2 charts
            row2 = tk.Frame(charts_container, bg=COLORS['light'])
            row2.pack(fill=tk.X, pady=(0, 20))
            
            # Chart 2: Bar Chart - Total Revenue by Product
            chart2_frame = tk.Frame(row2, bg=COLORS['white'], relief=tk.RAISED, bd=2)
            chart2_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
            
            tk.Label(chart2_frame, text=" Total Revenue by Product", 
                    font=('Arial', 12, 'bold'), bg=COLORS['white'], 
                    fg=COLORS['primary']).pack(pady=8)
            
            fig2 = Figure(figsize=(5, 4), dpi=80)
            ax2 = fig2.add_subplot(111)
            
            total_revenue = df[df.columns[1:]].sum().sort_values(ascending=False).head(8)
            bars = ax2.bar(total_revenue.index, total_revenue.values, 
                          color=[colors_line[i % len(colors_line)] for i in range(len(total_revenue))])
            ax2.set_ylabel('Total Revenue ($)', fontweight='bold')
            ax2.set_title('Top 8 Products', fontweight='bold')
            ax2.grid(axis='y', alpha=0.3)
            plt.setp(ax2.xaxis.get_majorticklabels(), rotation=45, ha='right')
            
            # Add value labels on bars
            for bar in bars:
                height = bar.get_height()
                ax2.text(bar.get_x() + bar.get_width()/2., height,
                        f'${int(height)}', ha='center', va='bottom', fontweight='bold', fontsize=8)
            
            fig2.tight_layout()
            
            canvas2 = FigureCanvasTkAgg(fig2, master=chart2_frame)
            canvas2.draw()
            canvas2.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
            
            # Chart 3: Pie Chart - Revenue Distribution
            chart3_frame = tk.Frame(row2, bg=COLORS['white'], relief=tk.RAISED, bd=2)
            chart3_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 0))
            
            tk.Label(chart3_frame, text=" Revenue Distribution", 
                    font=('Arial', 12, 'bold'), bg=COLORS['white'], 
                    fg=COLORS['primary']).pack(pady=8)
            
            fig3 = Figure(figsize=(5, 4), dpi=80)
            ax3 = fig3.add_subplot(111)
            
            top_products = total_revenue.head(6)
            ax3.pie(top_products.values, labels=top_products.index, autopct='%1.1f%%',
                   colors=colors_line, startangle=90, textprops={'fontweight': 'bold', 'fontsize': 9})
            ax3.set_title('Market Share (Top 6)', fontweight='bold', pad=15)
            
            canvas3 = FigureCanvasTkAgg(fig3, master=chart3_frame)
            canvas3.draw()
            canvas3.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
            
            # Summary Statistics
            stats_frame = tk.Frame(charts_container, bg=COLORS['white'], relief=tk.RAISED, bd=2)
            stats_frame.pack(fill=tk.X, pady=(0, 20))
            
            tk.Label(stats_frame, text=" Revenue Summary & Analysis", 
                    font=('Arial', 16, 'bold'), bg=COLORS['white'], 
                    fg=COLORS['primary']).pack(pady=15)
            
            stats_container = tk.Frame(stats_frame, bg=COLORS['white'])
            stats_container.pack(fill=tk.X, padx=20, pady=(0, 10))
            
            # Calculate statistics
            total_all = df[df.columns[1:]].sum().sum()
            avg_monthly = df[df.columns[1:]].mean().mean()
            max_product = total_revenue.idxmax()
            max_value = total_revenue.max()
            min_product = total_revenue.idxmin()
            min_value = total_revenue.min()
            
            stats = [
                (" Total Revenue", f"${int(total_all):,}", COLORS['success']),
                (" Avg Monthly", f"${int(avg_monthly):,}", COLORS['secondary']),
                (" Top Product", f"{max_product}", COLORS['warning']),
                (" Top Revenue", f"${int(max_value):,}", COLORS['accent'])
            ]
            
            for title, value, color in stats:
                stat_card = tk.Frame(stats_container, bg=COLORS['light'], relief=tk.RAISED, bd=1)
                stat_card.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
                
                tk.Label(stat_card, text=title, font=('Arial', 11, 'bold'),
                        bg=COLORS['light'], fg=COLORS['dark']).pack(pady=(10, 5))
                tk.Label(stat_card, text=value, font=('Arial', 20, 'bold'),
                        bg=COLORS['light'], fg=color).pack(pady=(5, 10))
            
            # Detailed Breakdown Table
            breakdown_frame = tk.Frame(stats_frame, bg=COLORS['white'])
            breakdown_frame.pack(fill=tk.X, padx=20, pady=(10, 20))
            
            tk.Label(breakdown_frame, text=" Detailed Revenue Breakdown (Proof)", 
                    font=('Arial', 14, 'bold'), bg=COLORS['white'], 
                    fg=COLORS['primary']).pack(pady=10)
            
            # Create table
            table_frame = tk.Frame(breakdown_frame, bg=COLORS['white'])
            table_frame.pack(fill=tk.X, padx=10, pady=10)
            
            # Headers
            headers = ["Product", "Total Revenue", "Avg Monthly", "Best Month", "Growth %"]
            for col, header in enumerate(headers):
                tk.Label(table_frame, text=header, font=('Arial', 10, 'bold'),
                        bg=COLORS['secondary'], fg=COLORS['white'],
                        relief=tk.RAISED, bd=1, width=15).grid(row=0, column=col, sticky='ew', padx=1, pady=1)
            
            # Data rows
            for idx, product in enumerate(total_revenue.head(8).index, 1):
                product_data = df[product]
                total = product_data.sum()
                avg = product_data.mean()
                best_month = df.loc[product_data.idxmax(), 'Month']
                growth = ((product_data.iloc[-1] - product_data.iloc[0]) / product_data.iloc[0] * 100)
                
                row_data = [
                    product[:12],
                    f"${int(total):,}",
                    f"${int(avg):,}",
                    best_month,
                    f"{growth:.1f}%"
                ]
                
                for col, value in enumerate(row_data):
                    bg_color = COLORS['light'] if idx % 2 == 0 else COLORS['white']
                    tk.Label(table_frame, text=value, font=('Arial', 9),
                            bg=bg_color, fg=COLORS['dark'],
                            relief=tk.SOLID, bd=1, width=15).grid(row=idx, column=col, sticky='ew', padx=1, pady=1)
            
            # Key Insights
            insights_frame = tk.Frame(stats_frame, bg=COLORS['light'], relief=tk.RAISED, bd=2)
            insights_frame.pack(fill=tk.X, padx=20, pady=(0, 20))
            
            tk.Label(insights_frame, text=" Key Insights", 
                    font=('Arial', 12, 'bold'), bg=COLORS['light'], 
                    fg=COLORS['primary']).pack(pady=10)
            
            insights_text = tk.Text(insights_frame, height=6, font=('Arial', 10),
                                   bg=COLORS['light'], fg=COLORS['dark'],
                                   relief=tk.FLAT, padx=15, pady=5, wrap=tk.WORD)
            insights_text.pack(fill=tk.X, padx=10, pady=(0, 10))
            
            insights_text.insert(tk.END, f"✅ Total products tracked: {len(df.columns)-1}\n")
            insights_text.insert(tk.END, f"✅ Best performing: {max_product} (${int(max_value):,})\n")
            insights_text.insert(tk.END, f"✅ Needs attention: {min_product} (${int(min_value):,})\n")
            insights_text.insert(tk.END, f"✅ Average revenue per product: ${int(total_all/len(df.columns)-1):,}\n")
            insights_text.insert(tk.END, f"✅ Report generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            insights_text.config(state=tk.DISABLED)
            
        except Exception as e:
            tk.Label(scrollable_frame, text=f"⚠️ Error loading revenue data: {str(e)}", 
                    font=('Arial', 14), bg=COLORS['light'], 
                    fg=COLORS['accent']).pack(pady=50)
        
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(20, 0), pady=(0, 20))
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, pady=(0, 20), padx=(0, 20))
    
    def export_data(self, filepath):
        """Export data to a user-selected location"""
        try:
            save_path = filedialog.asksaveasfilename(
                defaultextension=".csv",
                filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
                initialfile=os.path.basename(filepath)
            )
            if save_path:
                df = pd.read_csv(filepath)
                df.to_csv(save_path, index=False)
                messagebox.showinfo("✅ Success", f"Data exported successfully to:\n{save_path}")
        except Exception as e:
            messagebox.showerror("❌ Error", f"Failed to export data:\n{str(e)}")
    
    def export_chart(self, fig):
        """Export chart to image file"""
        try:
            save_path = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[("PNG files", "*.png"), ("PDF files", "*.pdf"), ("All files", "*.*")],
                initialfile="chart.png"
            )
            if save_path:
                fig.savefig(save_path, dpi=300, bbox_inches='tight')
                messagebox.showinfo("✅ Success", f"Chart exported successfully to:\n{save_path}")
        except Exception as e:
            messagebox.showerror("❌ Error", f"Failed to export chart:\n{str(e)}")


def open_main_window(username, role):
    main_window = tk.Toplevel()
    main_window.title(' Tech Park Manager')
    main_window.state('zoomed')
    main_window.configure(bg=COLORS['light'])
    
    # Handle window close
    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            main_window.destroy()
            window.deiconify()
    
    main_window.protocol("WM_DELETE_WINDOW", on_closing)
    my_app = MyApp(main_window, username, role)

# Main Login Window
window = tk.Tk()
window.title(' Tech Park Manager - Login')
window.state('zoomed')
window.configure(bg=COLORS['light'])

# Create main container
main_frame = tk.Frame(window, bg=COLORS['light'])
main_frame.place(relx=0.5, rely=0.5, anchor='center')

# Header
header_frame = tk.Frame(main_frame, bg=COLORS['primary'], width=500, height=120)
header_frame.pack(fill=tk.X)
header_frame.pack_propagate(False)

tk.Label(header_frame, text="", font=('Arial', 40), 
        bg=COLORS['primary'], fg=COLORS['white']).pack(pady=(10, 0))
tk.Label(header_frame, text="TECH PARK MANAGER", 
        font=('Arial', 24, 'bold'), 
        bg=COLORS['primary'], fg=COLORS['white']).pack()

# Login Form
form_frame = tk.Frame(main_frame, bg=COLORS['white'], width=500)
form_frame.pack(fill=tk.BOTH, expand=True, padx=0, pady=0)

tk.Label(form_frame, text="Welcome Back!", 
        font=('Arial', 20, 'bold'), 
        bg=COLORS['white'], fg=COLORS['primary']).pack(pady=(30, 10))

tk.Label(form_frame, text="Please login to continue", 
        font=('Arial', 12), 
        bg=COLORS['white'], fg=COLORS['dark']).pack(pady=(0, 30))

# Username
username_frame = tk.Frame(form_frame, bg=COLORS['white'])
username_frame.pack(pady=10)

tk.Label(username_frame, text=' Username', 
        font=('Arial', 12, 'bold'), 
        bg=COLORS['white'], fg=COLORS['dark']).pack(anchor='w', padx=50)

username_entry = tk.Entry(username_frame, font=('Arial', 14), 
                         width=30, relief=tk.SOLID, bd=1)
username_entry.pack(padx=50, pady=5)

# Password
password_frame = tk.Frame(form_frame, bg=COLORS['white'])
password_frame.pack(pady=10)

tk.Label(password_frame, text=' Password', 
        font=('Arial', 12, 'bold'), 
        bg=COLORS['white'], fg=COLORS['dark']).pack(anchor='w', padx=50)

password_entry = tk.Entry(password_frame, show='●', font=('Arial', 14), 
                         width=30, relief=tk.SOLID, bd=1)
password_entry.pack(padx=50, pady=5)

# Forgot password link
forgot_link = tk.Label(form_frame, text='Forgot Password?', 
                      font=('Arial', 10, 'underline'), 
                      bg=COLORS['white'], fg=COLORS['secondary'],
                      cursor='hand2')
forgot_link.pack(pady=(5, 0))
forgot_link.bind('<Button-1>', lambda e: forgot_password())

# Buttons
button_frame = tk.Frame(form_frame, bg=COLORS['white'])
button_frame.pack(pady=30)

login_button = tk.Button(button_frame, text=' Login', command=login,
                        font=('Arial', 14, 'bold'), width=12, height=2,
                        bg=COLORS['success'], fg=COLORS['white'],
                        relief=tk.FLAT, cursor='hand2')
login_button.pack(side=tk.LEFT, padx=10)

sign_up_button = tk.Button(button_frame, text=' Sign Up', command=sign_up,
                          font=('Arial', 14, 'bold'), width=12, height=2,
                          bg=COLORS['secondary'], fg=COLORS['white'],
                          relief=tk.FLAT, cursor='hand2')
sign_up_button.pack(side=tk.LEFT, padx=10)

# Add hover effects
def add_button_hover(btn, original_color):
    def on_enter(e):
        btn['bg'] = COLORS['hover']
    def on_leave(e):
        btn['bg'] = original_color
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

add_button_hover(login_button, COLORS['success'])
add_button_hover(sign_up_button, COLORS['secondary'])

# Footer
tk.Label(form_frame, text="© 2024 Tech Park Manager | All Rights Reserved", 
        font=('Arial', 9), 
        bg=COLORS['white'], fg=COLORS['dark']).pack(side=tk.BOTTOM, pady=20)

# Bind Enter key to login
window.bind('<Return>', lambda e: login())

window.mainloop()
