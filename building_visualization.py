import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.patches import Rectangle, FancyBboxPatch
import matplotlib.patches as mpatches
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

COLORS = {
    'primary': '#2C3E50',
    'secondary': '#3498DB',
    'accent': '#E74C3C',
    'success': '#27AE60',
    'warning': '#F39C12',
    'light': '#ECF0F1',
    'dark': '#34495E',
    'white': '#FFFFFF',
    'occupied': '#E74C3C',
    'vacant': '#27AE60',
    'meeting': '#F39C12',
    'common': '#95A5A6'
}

def create_3d_building_view(parent, elev=20, azim=45, zoom=1.0):
    try:
        floors_df = pd.read_csv("Datasets/floors.csv")
        rooms_df = pd.read_csv("Datasets/rooms.csv")
        
        fig = plt.figure(figsize=(12, 8), dpi=90)
        ax = fig.add_subplot(111, projection='3d')
        
        building_width = 10
        building_depth = 8
        floor_height = 1
        
        for idx, floor in floors_df.iterrows():
            floor_num = floor['FloorNumber']
            if floor_num == 'Ground':
                z = 0
            else:
                z = int(floor_num) * floor_height
            
            floor_rooms = rooms_df[rooms_df['FloorNumber'] == floor_num]
            occupied_count = len(floor_rooms[floor_rooms['Status'] == 'Occupied'])
            vacant_count = len(floor_rooms[floor_rooms['Status'] == 'Vacant'])
            
            occupancy_rate = occupied_count / len(floor_rooms) if len(floor_rooms) > 0 else 0
            if occupancy_rate > 0.8:
                floor_color = '#E74C3C'
            elif occupancy_rate > 0.5:
                floor_color = '#F39C12'
            else:
                floor_color = '#27AE60'
            
            vertices = [
                [0, 0, z],
                [building_width, 0, z],
                [building_width, building_depth, z],
                [0, building_depth, z]
            ]
            
            floor_face = Poly3DCollection([vertices], alpha=0.6, facecolor=floor_color, edgecolor='black', linewidth=2)
            ax.add_collection3d(floor_face)
            
            wall_vertices = [
                [[0, 0, z], [building_width, 0, z], [building_width, 0, z+floor_height], [0, 0, z+floor_height]],
                [[building_width, 0, z], [building_width, building_depth, z], [building_width, building_depth, z+floor_height], [building_width, 0, z+floor_height]],
                [[building_width, building_depth, z], [0, building_depth, z], [0, building_depth, z+floor_height], [building_width, building_depth, z+floor_height]],
                [[0, building_depth, z], [0, 0, z], [0, 0, z+floor_height], [0, building_depth, z+floor_height]]
            ]
            
            for wall in wall_vertices:
                wall_face = Poly3DCollection([wall], alpha=0.15, facecolor='lightgray', edgecolor='black', linewidth=1)
                ax.add_collection3d(wall_face)
            
            label_text = f'Floor {floor_num}\n{occupied_count}O/{vacant_count}V'
            ax.text(building_width/2, building_depth/2, z+floor_height/2, 
                   label_text, fontsize=9, ha='center', fontweight='bold',
                   bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))
        
        ax.text(building_width/2, building_depth/2, 10.5, 
               'TECH PARK\nTOWER', fontsize=14, ha='center', fontweight='bold',
               bbox=dict(boxstyle='round,pad=0.5', facecolor='lightblue', alpha=0.9))
        
        ax.set_xlabel('Width (m)', fontsize=11, fontweight='bold')
        ax.set_ylabel('Depth (m)', fontsize=11, fontweight='bold')
        ax.set_zlabel('Height (Floors)', fontsize=11, fontweight='bold')
        ax.set_title('Tech Park Tower - 3D Interactive View\n(Drag to rotate, scroll to zoom)', 
                    fontsize=14, fontweight='bold', pad=20)
        
        ax.view_init(elev=elev, azim=azim)
        
        margin = 2 / zoom
        ax.set_xlim(-margin, building_width + margin)
        ax.set_ylim(-margin, building_depth + margin)
        ax.set_zlim(-margin, 11 + margin)
        
        ax.grid(True, alpha=0.3)
        
        from matplotlib.patches import Patch
        legend_elements = [
            Patch(facecolor='#E74C3C', label='High Occupancy (>80%)'),
            Patch(facecolor='#F39C12', label='Medium Occupancy (50-80%)'),
            Patch(facecolor='#27AE60', label='Low Occupancy (<50%)')
        ]
        ax.legend(handles=legend_elements, loc='upper left', fontsize=9)
        
        plt.tight_layout()
        return fig
        
    except Exception as e:
        print(f"Error creating 3D view: {e}")
        return None

def create_floor_plan(floor_number):
    try:
        rooms_df = pd.read_csv("Datasets/rooms.csv")
        floor_rooms = rooms_df[rooms_df['FloorNumber'] == floor_number]
        
        fig, ax = plt.subplots(figsize=(14, 9), dpi=90)
        fig.patch.set_facecolor('white')
        ax.set_facecolor('#E8E8E8')
        
        room_positions = {}
        rooms_per_row = 4
        room_width = 2.2
        room_height = 1.8
        spacing = 0.4
        
        for idx, (_, room) in enumerate(floor_rooms.iterrows()):
            row = idx // rooms_per_row
            col = idx % rooms_per_row
            
            x = col * (room_width + spacing) + 0.5
            y = row * (room_height + spacing) + 0.5
            
            if room['Status'] == 'Occupied':
                color = COLORS['occupied']
                alpha = 0.7
            elif room['Status'] == 'Vacant':
                color = COLORS['vacant']
                alpha = 0.7
            elif room['Status'] == 'Available':
                color = COLORS['meeting']
                alpha = 0.7
            else:
                color = COLORS['common']
                alpha = 0.5
            
            shadow_box = FancyBboxPatch((x+0.05, y-0.05), room_width, room_height,
                                       boxstyle="round,pad=0.1",
                                       facecolor='gray', edgecolor='none',
                                       alpha=0.3, linewidth=0)
            ax.add_patch(shadow_box)
            
            fancy_box = FancyBboxPatch((x, y), room_width, room_height,
                                      boxstyle="round,pad=0.1",
                                      facecolor=color, edgecolor='black',
                                      alpha=alpha, linewidth=2.5)
            ax.add_patch(fancy_box)
            
            ax.text(x + room_width/2, y + room_height - 0.25,
                   room['RoomNumber'],
                   ha='center', va='center',
                   fontsize=13, fontweight='bold', color='white',
                   bbox=dict(boxstyle='round,pad=0.3', facecolor='black', alpha=0.5))
            
            occupant = room['OccupiedBy'] if room['Status'] == 'Occupied' else room['Usage']
            ax.text(x + room_width/2, y + room_height/2,
                   occupant[:25],
                   ha='center', va='center',
                   fontsize=9, color='white', fontweight='bold', wrap=True)
            
            ax.text(x + room_width/2, y + 0.25,
                   room['Dimension'],
                   ha='center', va='center',
                   fontsize=8, color='white', style='italic',
                   bbox=dict(boxstyle='round,pad=0.2', facecolor='black', alpha=0.3))
            
            if room['Usage'] == 'Office':
                capacity_text = f"{room['NoOfPC']} PCs | {room['NoOfTables']} Tables"
                ax.text(x + room_width/2, y + 0.6,
                       capacity_text,
                       ha='center', va='center',
                       fontsize=7, color='white')
        
        legend_elements = [
            mpatches.Patch(facecolor=COLORS['occupied'], label='Occupied', alpha=0.7),
            mpatches.Patch(facecolor=COLORS['vacant'], label='Vacant', alpha=0.7),
            mpatches.Patch(facecolor=COLORS['meeting'], label='Meeting/Shared', alpha=0.7),
            mpatches.Patch(facecolor=COLORS['common'], label='Common Area', alpha=0.5)
        ]
        ax.legend(handles=legend_elements, loc='upper right', fontsize=10)
        
        ax.set_title(f'Floor {floor_number} - Room Layout', fontsize=16, fontweight='bold', pad=20)
        ax.set_xlabel('Building Width', fontsize=12)
        ax.set_ylabel('Building Depth', fontsize=12)
        
        ax.set_xticks([])
        ax.set_yticks([])
        
        max_x = ((len(floor_rooms) - 1) % rooms_per_row + 1) * (room_width + spacing) + 1
        max_y = ((len(floor_rooms) - 1) // rooms_per_row + 1) * (room_height + spacing) + 1
        ax.set_xlim(0, max(max_x, 10))
        ax.set_ylim(0, max(max_y, 6))
        
        ax.grid(True, alpha=0.2, linestyle='--')
        plt.tight_layout()
        
        return fig
        
    except Exception as e:
        print(f"Error creating floor plan: {e}")
        return None

def create_occupancy_heatmap():
    try:
        rooms_df = pd.read_csv("Datasets/rooms.csv")
        floors_df = pd.read_csv("Datasets/floors.csv")
        
        fig, ax = plt.subplots(figsize=(12, 7), dpi=90)
        
        floor_data = []
        floor_labels = []
        
        for _, floor in floors_df.iterrows():
            floor_num = floor['FloorNumber']
            floor_rooms = rooms_df[rooms_df['FloorNumber'] == floor_num]
            
            total_rooms = len(floor_rooms[floor_rooms['Usage'] == 'Office'])
            occupied_rooms = len(floor_rooms[(floor_rooms['Usage'] == 'Office') & (floor_rooms['Status'] == 'Occupied')])
            vacant_rooms = len(floor_rooms[(floor_rooms['Usage'] == 'Office') & (floor_rooms['Status'] == 'Vacant')])
            
            floor_data.append([occupied_rooms, vacant_rooms])
            floor_labels.append(f'Floor {floor_num}')
        
        floor_data = np.array(floor_data)
        
        x = np.arange(len(floor_labels))
        width = 0.6
        
        p1 = ax.barh(x, floor_data[:, 0], width, label='Occupied', color=COLORS['occupied'])
        p2 = ax.barh(x, floor_data[:, 1], width, left=floor_data[:, 0], label='Vacant', color=COLORS['vacant'])
        
        ax.set_ylabel('Floors', fontsize=12, fontweight='bold')
        ax.set_xlabel('Number of Rooms', fontsize=12, fontweight='bold')
        ax.set_title('Building Occupancy Overview', fontsize=16, fontweight='bold', pad=20)
        ax.set_yticks(x)
        ax.set_yticklabels(floor_labels)
        ax.legend(loc='upper right', fontsize=11)
        ax.grid(axis='x', alpha=0.3)
        
        for i, (occ, vac) in enumerate(floor_data):
            if occ > 0:
                ax.text(occ/2, i, str(int(occ)), ha='center', va='center', 
                       fontweight='bold', color='white', fontsize=10)
            if vac > 0:
                ax.text(occ + vac/2, i, str(int(vac)), ha='center', va='center',
                       fontweight='bold', color='white', fontsize=10)
        
        plt.tight_layout()
        return fig
        
    except Exception as e:
        print(f"Error creating heatmap: {e}")
        return None

def create_lift_status_display():
    try:
        lifts_df = pd.read_csv("Datasets/lifts.csv")
        
        fig, ax = plt.subplots(figsize=(12, 6), dpi=90)
        fig.patch.set_facecolor('white')
        
        lift_width = 2.5
        lift_height = 10
        spacing = 1.0
        
        for idx, (_, lift) in enumerate(lifts_df.iterrows()):
            x = idx * (lift_width + spacing) + 2
            
            if lift['Status'] == 'Operational':
                color = COLORS['success']
            elif lift['Status'] == 'Under Maintenance':
                color = COLORS['warning']
            else:
                color = COLORS['accent']
            
            shadow = Rectangle((x+0.1, -0.1), lift_width, lift_height,
                              facecolor='gray', edgecolor='none',
                              alpha=0.3, linewidth=0)
            ax.add_patch(shadow)
            
            rect = Rectangle((x, 0), lift_width, lift_height,
                           facecolor=color, edgecolor='black',
                           alpha=0.8, linewidth=3)
            ax.add_patch(rect)
            
            ax.text(x + lift_width/2, lift_height + 0.7,
                   lift['LiftID'],
                   ha='center', va='bottom',
                   fontsize=16, fontweight='bold',
                   bbox=dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.9))
            
            ax.text(x + lift_width/2, lift_height - 1,
                   lift['Location'],
                   ha='center', va='center',
                   fontsize=11, color='white', fontweight='bold',
                   bbox=dict(boxstyle='round,pad=0.3', facecolor='black', alpha=0.5))
            
            ax.text(x + lift_width/2, lift_height/2 + 1,
                   f"{lift['MaximumPeopleCarried']} persons",
                   ha='center', va='center',
                   fontsize=10, color='white', fontweight='bold')
            
            ax.text(x + lift_width/2, lift_height/2,
                   f"{lift['WeightCapacity']}",
                   ha='center', va='center',
                   fontsize=10, color='white', fontweight='bold')
            
            ax.text(x + lift_width/2, lift_height/2 - 1,
                   f"{lift['MaximumFloorsTaken']} floors",
                   ha='center', va='center',
                   fontsize=9, color='white')
            
            ax.text(x + lift_width/2, 1,
                   lift['Status'],
                   ha='center', va='center',
                   fontsize=10, color='white', fontweight='bold',
                   bbox=dict(boxstyle='round,pad=0.3', facecolor='black', alpha=0.6))
            
            ax.text(x + lift_width/2, -0.8,
                   f"{lift['EmployeeIncharge']}",
                   ha='center', va='top',
                   fontsize=8, style='italic')
            
            ax.text(x + lift_width/2, -1.3,
                   f"{lift['Supplier']}",
                   ha='center', va='top',
                   fontsize=8, style='italic')
        
        ax.set_xlim(0, len(lifts_df) * (lift_width + spacing) + 3)
        ax.set_ylim(-2, lift_height + 2)
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_title('Lift Status Monitor - Real-time Overview', fontsize=16, fontweight='bold', pad=20)
        
        legend_elements = [
            mpatches.Patch(facecolor=COLORS['success'], label='Operational', alpha=0.7),
            mpatches.Patch(facecolor=COLORS['warning'], label='Under Maintenance', alpha=0.7),
            mpatches.Patch(facecolor=COLORS['accent'], label='Out of Service', alpha=0.7)
        ]
        ax.legend(handles=legend_elements, loc='upper right', fontsize=10)
        
        plt.tight_layout()
        return fig
        
    except Exception as e:
        print(f"Error creating lift display: {e}")
        return None
