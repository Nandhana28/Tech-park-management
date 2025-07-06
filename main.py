import tkinter as tk

from Classes_and_Definitions import Repair
from Classes_and_Definitions import Employee
from Classes_and_Definitions import Event
from Classes_and_Definitions import Company
from Classes_and_Definitions import VisitorLog

from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox

users = {'Jelena': '1234', 'Nandhana': '5678'}

def sign_up():
    username = username_entry.get()
    password = password_entry.get()

    if username == '' or password == '':
        messagebox.showerror('Error', 'Please enter both username and password.')
    elif username in users:
        messagebox.showerror('Error', 'Username already exists. Please choose a different one.')
    else:
        users[username] = password
        messagebox.showinfo('Success', 'Sign up successful!')

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == '' or password == '':
        messagebox.showerror('Error', 'Please enter both username and password.')
    elif username not in users or users[username] != password:
        messagebox.showerror('Error', 'Invalid username or password.')
    else:
        messagebox.showinfo('Success', 'Login successful!')
        open_main_window()

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tech Park Manager")
        #heading
        top_label = tk.Label(root, text='FEATURES', font=('Helvetica', 30, 'bold'))
        top_label.pack(side=tk.TOP, pady=10)
        #creates a left frame for buttons
        buttons_frame = tk.Frame(root)
        buttons_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5)

        repair_button = tk.Button(buttons_frame, text="Repair History", font=('Helvetica', 15, 'bold'),width=40, height=2, command=self.open_repair_window)
        repair_button.pack(pady=15, padx=200, anchor='center')

        event_button = tk.Button(buttons_frame, text="Event History", font=('Helvetica', 15, 'bold'),width=40, height=2,command=self.open_event_window)
        event_button.pack(pady=15, padx=200, anchor='center')

        upcoming_events_button = tk.Button(buttons_frame, text="Upcoming Events", font=('Helvetica', 15, 'bold'),width=40, height=2, command=self.open_upcoming_events)
        upcoming_events_button.pack(pady=15, padx=200, anchor='center')

        employee_button = tk.Button(buttons_frame, text="Employee Details",font=('Helvetica', 15, 'bold'),width=40, height=2, command=self.open_employee_details)
        employee_button.pack(pady=15, padx=200, anchor='center')

        visitor_log_button = tk.Button(buttons_frame, text="Visitor Log History", font=('Helvetica', 15, 'bold'),width=40, height=2, command=self.open_visitor_log_history)
        visitor_log_button.pack(pady=15, padx=200, anchor='center')

        revenue_button = tk.Button(buttons_frame, text="Monthly Revenue", font=('Helvetica', 15, 'bold'),width=40, height=2, command=self.open_monthly_revenue)
        revenue_button.pack(pady=15, padx=200, anchor='center')

        company_button = tk.Button(buttons_frame, text="Company Details", font=('Helvetica', 15, 'bold'),width=40, height=2, command=self.open_company_details)
        company_button.pack(pady=15, padx=200, anchor='center')
        #creates a right frame for text boxes
        right_frame = tk.Frame(root)
        right_frame.pack(fill=tk.BOTH, side=tk.LEFT, padx=5)
        
        reminder_label = tk.Label(right_frame, text="Remainder:", font=('Times New Roman', 20, 'bold'))
        reminder_label.grid(row=0, column=0, sticky="w", pady=(20, 5)) 
        
        reminder_text = tk.Text(right_frame, height=20, width=50)
        reminder_text.grid(row=1, column=0, sticky="w",pady=(0, 10)) 
        #insert data into remainder box
        file = open("upcoming_events.csv", "r")
        data = file.readlines()
        record = data[1].split(',')
        reminder_text.insert(tk.END, f"Event Name            : {record[0]}")
        reminder_text.insert(tk.END, f"\nDate                  : {record[1]}")
        reminder_text.insert(tk.END, f"\nTime                  : {record[2]}")
        reminder_text.insert(tk.END, f"\nLocation              : {record[3]}")
        reminder_text.insert(tk.END, f"\nAttendees limit       : {record[4]}")
        reminder_text.insert(tk.END, f"\nOrganizer             : {record[5]}")
        reminder_text.insert(tk.END, f"\nDescription           : {record[6]}")
        reminder_text.insert(tk.END, f"\nTheme                 : {record[7]}")
        reminder_text.insert(tk.END, f"\nRegistration required : {record[8]}")
        reminder_text.insert(tk.END, f"\nRegistration link     : {record[9]}")
        
        file.close()

        employee_count_label = tk.Label(right_frame, text="Employee Count:", font=('Times New Roman', 20, 'bold'))
        employee_count_label.grid(row=2, column=0, sticky="w", pady=10)
        
        employee_count_text = tk.Text(right_frame, height=5, width=50)
        employee_count_text.grid(row=3, column=0, pady=(0, 20))  
        #insert number of employees in this box
        file = open("Employee.csv", "r")
        data = file.readlines()[1:]
        EmployeeCount = len(data)
        employee_count_text.insert(tk.END, EmployeeCount)
        file.close()
        
        
    def open_repair_window(self):
        repair_window = tk.Toplevel(self.root)
        repair_window.title("Repair History")
        screen_width = repair_window.winfo_screenwidth()
        screen_height = repair_window.winfo_screenheight()
        repair_window.geometry(f'{screen_width}x{screen_height}')
        
        top_label = tk.Label(repair_window, text='REPAIR  HISTORY', font=('Helvetica', 30, 'bold'))
        top_label.pack(side=tk.TOP, pady=10)
        
        df = pd.read_csv("repair.csv")
        frame = tk.Frame(repair_window)
        frame.pack(fill=tk.BOTH, pady=5)
        
        for index, row in df.iterrows():
            repair_text = tk.Text(frame, height=8, width=80)
            repair_text.pack(pady=(0, 20), anchor='center')
            
            repair = Repair(row['Object Repaired'], row['Repair Charge'], row['Object Brand'], row['Company Repaired'], row['Date'], row['Number of components'], row['Person Name'])
            repair_text.insert(tk.END, f"Object Repaired      : {repair.ObjectRepaired}\n")
            repair_text.insert(tk.END, f"Repair Charge        : {repair.RepairCharge}\n")
            repair_text.insert(tk.END, f"Object Brand         : {repair.ObjectBrand}\n")
            repair_text.insert(tk.END, f"Company Repaired     : {repair.CompanyRepaired}\n")
            repair_text.insert(tk.END, f"Date                 : {repair.Date}\n")
            repair_text.insert(tk.END, f"Number of components : {repair.NumberOfComponents}\n")
            repair_text.insert(tk.END, f"Person Name          : {repair.PersonName}\n")


            

    def open_event_window(self):
        event_window = tk.Toplevel(self.root)
        event_window.title("Event History")
        screen_width = event_window.winfo_screenwidth()
        screen_height = event_window.winfo_screenheight()
        event_window.geometry(f'{screen_width}x{screen_height}')
        
        top_label = tk.Label(event_window, text='EVENT  HISTORY', font=('Helvetica', 30, 'bold'))
        top_label.pack(side=tk.TOP, pady=10)
        
        df=pd.read_csv("event_history.csv")
        frame = tk.Frame(event_window)
        frame.pack(fill=tk.BOTH, pady=5)
        
        for index,row in df.iterrows():
            event_text = tk.Text(frame, height=15, width=80)
            event_text.pack(pady=(0, 20), anchor='center')
            
            event = Event(row['Event Name'], row['Date'], row['Time'], row['Location'], row['Attendees Limit'],row['Organizer'],row['Description'],row['Theme'],row['Registration required'],row['Registration link'])
            event_text.insert(tk.END, f"Event Name            : {event.EventName}")
            event_text.insert(tk.END, f"\nDate                  : {event.Date}")
            event_text.insert(tk.END, f"\nTime                  : {event.Time}")
            event_text.insert(tk.END, f"\nLocation              : {event.Location}")
            event_text.insert(tk.END, f"\nAttendees Limit       : {event.AttendeesLimit}")
            event_text.insert(tk.END, f"\nOrganizer             : {event.Organizer}")
            event_text.insert(tk.END, f"\nDescription           : {event.Description}")
            event_text.insert(tk.END, f"\nTheme                 : {event.Theme}")
            event_text.insert(tk.END, f"\nRegistration Required : {event.RegistrationRequired}")
            event_text.insert(tk.END, f"\nRegistration Link     : {event.RegistrationLink}\n")

        
    def open_upcoming_events(self):
        upcoming_events=tk.Toplevel(self.root)
        upcoming_events.title("Upcoming Events")
        screen_width = upcoming_events.winfo_screenwidth()
        screen_height =upcoming_events.winfo_screenheight()
        upcoming_events.geometry(f'{screen_width}x{screen_height}')
        
        top_label = tk.Label(upcoming_events, text='UPCOMING  EVENTS', font=('Helvetica', 30, 'bold'))
        top_label.pack(side=tk.TOP, pady=10)
        
        df=pd.read_csv("upcoming_events.csv")
        frame = tk.Frame(upcoming_events)
        frame.pack(fill=tk.BOTH, pady=5)
        
        for index,row in df.iterrows():
            upcoming_events_text = tk.Text(frame, height=15, width=80)
            upcoming_events_text.pack(pady=(0, 20), anchor='center')
            
            event = Event(row['Event Name'], row['Date'], row['Time'], row['Location'], row['Attendees Limit'],row['Organizer'],row['Description'],row['Theme'],row['Registration Required'],row['Registration Link'])
            upcoming_events_text.insert(tk.END, f"Event Name            : {event.EventName}")
            upcoming_events_text.insert(tk.END, f"\nDate                  : {event.Date}")
            upcoming_events_text.insert(tk.END, f"\nTime                  : {event.Time}")
            upcoming_events_text.insert(tk.END, f"\nLocation              : {event.Location}")
            upcoming_events_text.insert(tk.END, f"\nAttendees Limit       : {event.AttendeesLimit}")
            upcoming_events_text.insert(tk.END, f"\nOrganizer             : {event.Organizer}")
            upcoming_events_text.insert(tk.END, f"\nDescription           : {event.Description}")
            upcoming_events_text.insert(tk.END, f"\nTheme                 : {event.Theme}")
            upcoming_events_text.insert(tk.END, f"\nRegistration Required : {event.RegistrationRequired}")
            upcoming_events_text.insert(tk.END, f"\nRegistration Link     : {event.RegistrationLink}\n")

        
    def open_employee_details(self):
        employee_details=tk.Toplevel(self.root)
        employee_details.title("Employee Details")
        screen_width = employee_details.winfo_screenwidth()
        screen_height = employee_details.winfo_screenheight()
        employee_details.geometry(f'{screen_width}x{screen_height}')
        
        top_label = tk.Label(employee_details, text='EMPLOYEE  DETAILS', font=('Helvetica', 30, 'bold'))
        top_label.pack(side=tk.TOP, pady=10)
        
        df=pd.read_csv("Employee.csv")
        frame = tk.Frame(employee_details)
        frame.pack(fill=tk.BOTH, pady=5)
        
        for index,row in df.iterrows():
            employee_details_text = tk.Text(frame, height=14, width=80)
            employee_details_text.pack(pady=(0, 20), anchor='center')
            
            employee = Employee(row['Name'], row['EmployeeID'], row['YearsOfExperience'], row['DateOfJoin'], row['Department'], row['Designation'], row['Availability'], row['TeamName'], row['WorkAssigned'], row['Salary'], row['WorkHours'], row['Qualification'])
            employee_details_text.insert(tk.END, f"Name                : {employee.Name}")
            employee_details_text.insert(tk.END, f"\nEmployeeID          : {employee.EmployeeID}")
            employee_details_text.insert(tk.END, f"\nYears of Experience : {employee.YearsOfExperience}")
            employee_details_text.insert(tk.END, f"\nDate of Join        : {employee.DateOfJoin}")
            employee_details_text.insert(tk.END, f"\nDepartment          : {employee.Department}")
            employee_details_text.insert(tk.END, f"\nDesignation         : {employee.Designation}")
            employee_details_text.insert(tk.END, f"\nAvailability        : {employee.Availability}")
            employee_details_text.insert(tk.END, f"\nTeam name           : {employee.TeamName}")
            employee_details_text.insert(tk.END, f"\nWork assigned       : {employee.WorkAssigned}")
            employee_details_text.insert(tk.END, f"\nSalary              : {employee.Salary}")
            employee_details_text.insert(tk.END, f"\nWork hours          : {employee.WorkHours}")
            employee_details_text.insert(tk.END, f"\nQualification       : {employee.Qualification}\n")

        
    def open_visitor_log_history(self):
        visitor_log_history=tk.Toplevel(self.root)
        visitor_log_history.title("Visitor Log History")
        screen_width = visitor_log_history.winfo_screenwidth()
        screen_height = visitor_log_history.winfo_screenheight()
        visitor_log_history.geometry(f'{screen_width}x{screen_height}')
        
        top_label = tk.Label(visitor_log_history, text='VISITER  LOG  HISTORY', font=('Helvetica', 30, 'bold'))
        top_label.pack(side=tk.TOP, pady=10)
        
        df=pd.read_csv("VisiterLog.csv")
        frame = tk.Frame(visitor_log_history)
        frame.pack(fill=tk.BOTH, pady=5)
        
        for index,row in df.iterrows():
            visitor_log_text = tk.Text(frame, height=9, width=80)
            visitor_log_text.pack(pady=(0, 20), anchor='center')
            
            log = VisitorLog(row['VisitorName'], row['ContactDetails'], row['PurposeOfVisit'], row['CheckInTime'], row['CheckOutTime'],row['HostEmployee'])
            visitor_log_text.insert(tk.END, f"Visitor Name     : {log.VisitorName}")
            visitor_log_text.insert(tk.END, f"\nContact Details  : {log.ContactDetails}")
            visitor_log_text.insert(tk.END, f"\nPurpose Of Visit : {log.PurposeOfVisit}")
            visitor_log_text.insert(tk.END, f"\nCheck In Time    : {log.CheckInTime}")
            visitor_log_text.insert(tk.END, f"\nCheck Out Time   : {log.CheckOutTime}")
            visitor_log_text.insert(tk.END, f"\nHost Employee    : {log.HostEmployee}\n")
        
    def open_monthly_revenue(self):
        monthly_revenue = tk.Toplevel(self.root)
        monthly_revenue.title("Monthly revenue")
        screen_width = monthly_revenue.winfo_screenwidth()
        screen_height = monthly_revenue.winfo_screenheight()
        monthly_revenue.geometry(f'{screen_width}x{screen_height}')
        
        top_label = tk.Label(monthly_revenue, text='MONTHLY  REVENUE', font=('Helvetica', 30, 'bold'))
        top_label.pack(side=tk.TOP, pady=10)
       
        plot_frame = ttk.Frame(monthly_revenue)  
        plot_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        df = pd.read_csv("Product_Revenue.csv")
        
        fig, ax = plt.subplots(figsize=(10, 6))  
        for column in df.columns[1:]: 
            ax.plot(df['Month'], df[column], marker='o', label=column)  
        
        ax.set_xlabel('Product')
        ax.set_ylabel('Revenue')
        ax.set_title('Monthly Revenue by Product')
        ax.legend()  
        
        canvas = FigureCanvasTkAgg(fig, master=plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    
    def open_company_details(self):
        company_details=tk.Toplevel(self.root)
        company_details.title("Company Details")
        screen_width = company_details.winfo_screenwidth()
        screen_height = company_details.winfo_screenheight()
        company_details.geometry(f'{screen_width}x{screen_height}')
        
        top_label = tk.Label(company_details, text='COMPANY  DETAILS', font=('Helvetica', 30, 'bold'))
        top_label.pack(side=tk.TOP, pady=10)
       
        df=pd.read_csv("company_details.csv")
        frame = tk.Frame(company_details)
        frame.pack(fill=tk.BOTH, pady=5)
        
        for index,row in df.iterrows():
            company_details_text = tk.Text(frame, height=9, width=80)
            company_details_text.pack(pady=(0, 20), anchor='center')
            
            company = Company(row['Name'], row['Address'], row['Industry'], row['Employee Count'], row['Revenue'])
            company_details_text.insert(tk.END, f"Name           : {company.Name}")
            company_details_text.insert(tk.END, f"\nAddress        : {company.Address}")
            company_details_text.insert(tk.END, f"\nIndustry       : {company.Industry}")
            company_details_text.insert(tk.END, f"\nEmployee Count : {company.EmployeeCount}")
            company_details_text.insert(tk.END, f"\nRevenue        : {company.Revenue}\n")

        

def open_main_window():
    main_window = tk.Toplevel()
    main_window.title('Main Window')
    screen_width = main_window.winfo_screenwidth()
    screen_height = main_window.winfo_screenheight()
    main_window.geometry(f'{screen_width}x{screen_height}')
    my_app = MyApp(main_window)

window = tk.Tk()
window.title('Sign Up & Login')

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(f'{screen_width}x{screen_height}')

label = tk.Label(window, text="WELCOME TO TECH PARK MANAGER", font=('Helvetica', 30, 'bold'))
label.place(relx=0.5, rely=0.2, anchor='center')

top_label = tk.Label(window, text='Welcome to Sign Up & Login', font=('Helvetica', 25, 'bold'))
top_label.place(relx=0.5, rely=0.3, anchor='center')

username_label = tk.Label(window, text='Username :', font=('Times New Roman', 18, 'bold'))
username_label.place(x=(screen_width - username_label.winfo_reqwidth()) / 2.1 - 120,
                      y=(screen_height - username_label.winfo_reqheight()) / 2 - 60)

username_entry = tk.Entry(window, font=('Times New Roman', 15))
username_entry.place(x=(screen_width - username_entry.winfo_reqwidth()) / 2 + 30,
                      y=(screen_height - username_entry.winfo_reqheight()) / 2 - 60, width=200)

password_label = tk.Label(window, text='Password :', font=('Times New Roman', 18, 'bold'))
password_label.place(x=(screen_width - password_label.winfo_reqwidth()) / 2.1 - 120,
                      y=(screen_height - password_label.winfo_reqheight()) / 2)

password_entry = tk.Entry(window, show='*', font=('Times New Roman', 15))
password_entry.place(x=(screen_width - password_entry.winfo_reqwidth()) / 2 + 30,
                      y=(screen_height - password_entry.winfo_reqheight()) / 2, width=200)

sign_up_button = tk.Button(window, text='Sign Up', command=sign_up, font=('Times New Roman', 15, 'bold'),width=15, height=2)
sign_up_button.place(x=(screen_width - sign_up_button.winfo_reqwidth()) / 2.4 - 40,
                      y=(screen_height - sign_up_button.winfo_reqheight()) / 2 + 70)

login_button = tk.Button(window, text='Login', command=login,font=('Times New Roman', 15, 'bold'),width=15, height=2, )
login_button.place(x=(screen_width - login_button.winfo_reqwidth()) / 1.73 - 40,
                    y=(screen_height - login_button.winfo_reqheight()) / 2 + 70)

window.mainloop()
