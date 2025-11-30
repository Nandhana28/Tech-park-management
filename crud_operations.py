import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
from datetime import datetime

COLORS = {
    'primary': '#2C3E50',
    'secondary': '#3498DB',
    'accent': '#E74C3C',
    'success': '#27AE60',
    'warning': '#F39C12',
    'light': '#ECF0F1',
    'dark': '#34495E',
    'white': '#FFFFFF',
    'hover': '#5DADE2'
}

def create_record_dialog(parent, title, fields, csv_file, callback=None):
    dialog = tk.Toplevel(parent)
    dialog.title(f"Add New {title}")
    dialog.geometry('600x700')
    dialog.configure(bg=COLORS['light'])
    dialog.transient(parent)
    dialog.grab_set()
    
    dialog.update_idletasks()
    x = (dialog.winfo_screenwidth() // 2) - (600 // 2)
    y = (dialog.winfo_screenheight() // 2) - (700 // 2)
    dialog.geometry(f'600x700+{x}+{y}')
    
    header = tk.Frame(dialog, bg=COLORS['success'], height=70)
    header.pack(fill=tk.X)
    header.pack_propagate(False)
    tk.Label(header, text=f'Add New {title}', font=('Arial', 18, 'bold'),
            bg=COLORS['success'], fg=COLORS['white']).pack(pady=20)
    
    canvas = tk.Canvas(dialog, bg=COLORS['white'])
    scrollbar = ttk.Scrollbar(dialog, orient="vertical", command=canvas.yview)
    form_frame = tk.Frame(canvas, bg=COLORS['white'])
    
    form_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=form_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    entries = {}
    for field_name in fields:
        tk.Label(form_frame, text=field_name, font=('Arial', 11, 'bold'),
                bg=COLORS['white'], fg=COLORS['dark']).pack(anchor='w', padx=30, pady=(15, 2))
        
        entry = tk.Entry(form_frame, font=('Arial', 11), width=50)
        entry.pack(padx=30, pady=(0, 5))
        entries[field_name] = entry
    
    def submit():
        values = {}
        for field_name, entry in entries.items():
            value = entry.get().strip()
            if not value:
                messagebox.showerror('Error', f'{field_name} is required!')
                return
            values[field_name] = value
        
        try:
            df = pd.read_csv(csv_file)
            new_record = pd.DataFrame([values])
            df = pd.concat([df, new_record], ignore_index=True)
            df.to_csv(csv_file, index=False)
            
            messagebox.showinfo('Success', f'{title} added successfully!')
            dialog.destroy()
            if callback:
                callback()
        except Exception as e:
            messagebox.showerror('Error', f'Failed to add record:\n{str(e)}')
    
    btn_frame = tk.Frame(form_frame, bg=COLORS['white'])
    btn_frame.pack(pady=30)
    
    tk.Button(btn_frame, text='Add Record', command=submit,
             font=('Arial', 12, 'bold'), bg=COLORS['success'], fg=COLORS['white'],
             width=15, height=2, cursor='hand2').pack(side=tk.LEFT, padx=5)
    
    tk.Button(btn_frame, text='Cancel', command=dialog.destroy,
             font=('Arial', 12, 'bold'), bg=COLORS['accent'], fg=COLORS['white'],
             width=15, height=2, cursor='hand2').pack(side=tk.LEFT, padx=5)
    
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(20, 0), pady=20)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y, pady=20, padx=(0, 20))

def edit_record_dialog(parent, title, fields, csv_file, record_index, callback=None):
    dialog = tk.Toplevel(parent)
    dialog.title(f"Edit {title}")
    dialog.geometry('600x700')
    dialog.configure(bg=COLORS['light'])
    dialog.transient(parent)
    dialog.grab_set()
    
    dialog.update_idletasks()
    x = (dialog.winfo_screenwidth() // 2) - (600 // 2)
    y = (dialog.winfo_screenheight() // 2) - (700 // 2)
    dialog.geometry(f'600x700+{x}+{y}')
    
    header = tk.Frame(dialog, bg=COLORS['warning'], height=70)
    header.pack(fill=tk.X)
    header.pack_propagate(False)
    tk.Label(header, text=f'Edit {title}', font=('Arial', 18, 'bold'),
            bg=COLORS['warning'], fg=COLORS['white']).pack(pady=20)
    
    canvas = tk.Canvas(dialog, bg=COLORS['white'])
    scrollbar = ttk.Scrollbar(dialog, orient="vertical", command=canvas.yview)
    form_frame = tk.Frame(canvas, bg=COLORS['white'])
    
    form_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=form_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    try:
        df = pd.read_csv(csv_file)
        record = df.iloc[record_index]
    except Exception as e:
        messagebox.showerror('Error', f'Failed to load record:\n{str(e)}')
        dialog.destroy()
        return
    
    entries = {}
    for field_name in fields:
        tk.Label(form_frame, text=field_name, font=('Arial', 11, 'bold'),
                bg=COLORS['white'], fg=COLORS['dark']).pack(anchor='w', padx=30, pady=(15, 2))
        
        entry = tk.Entry(form_frame, font=('Arial', 11), width=50)
        entry.insert(0, str(record[field_name]))
        entry.pack(padx=30, pady=(0, 5))
        entries[field_name] = entry
    
    def submit():
        values = {}
        for field_name, entry in entries.items():
            value = entry.get().strip()
            if not value:
                messagebox.showerror('Error', f'{field_name} is required!')
                return
            values[field_name] = value
        
        try:
            df = pd.read_csv(csv_file)
            for field_name, value in values.items():
                df.at[record_index, field_name] = value
            
            df.to_csv(csv_file, index=False)
            
            messagebox.showinfo('Success', f'{title} updated successfully!')
            dialog.destroy()
            if callback:
                callback()
        except Exception as e:
            messagebox.showerror('Error', f'Failed to update record:\n{str(e)}')
    
    btn_frame = tk.Frame(form_frame, bg=COLORS['white'])
    btn_frame.pack(pady=30)
    
    tk.Button(btn_frame, text='Save Changes', command=submit,
             font=('Arial', 12, 'bold'), bg=COLORS['warning'], fg=COLORS['white'],
             width=15, height=2, cursor='hand2').pack(side=tk.LEFT, padx=5)
    
    tk.Button(btn_frame, text='Cancel', command=dialog.destroy,
             font=('Arial', 12, 'bold'), bg=COLORS['accent'], fg=COLORS['white'],
             width=15, height=2, cursor='hand2').pack(side=tk.LEFT, padx=5)
    
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(20, 0), pady=20)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y, pady=20, padx=(0, 20))

def delete_record(parent, title, csv_file, record_index, callback=None):
    if not messagebox.askyesno('Confirm Delete', 
                               f'Are you sure you want to delete this {title}?\nThis action cannot be undone!'):
        return
    
    try:
        df = pd.read_csv(csv_file)
        df = df.drop(record_index)
        df.to_csv(csv_file, index=False)
        
        messagebox.showinfo('Success', f'{title} deleted successfully!')
        if callback:
            callback()
    except Exception as e:
        messagebox.showerror('Error', f'Failed to delete record:\n{str(e)}')
