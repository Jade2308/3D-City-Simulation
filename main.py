"""
3D City Simulation - Main Application
A simple 3D city simulator with buildings, roads, trees, and animated cars
"""
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import tkinter as tk
from tkinter import ttk, messagebox
import threading
import sys

# Import engine components
from engine.renderer import Renderer
from engine.camera import Camera
from engine.lighting import Lighting

# Import objects
from objects.building import Building
from objects.road import Road
from objects.tree import Tree
from objects.car import Car

# Import utilities
from utils.helpers import generate_random_city, create_cars


class CitySimulation:
    def __init__(self):
        """Initialize the 3D city simulation"""
        # Renderer setup
        self.renderer = Renderer(800, 600)
        self.renderer.init_pygame()
        
        # Camera setup
        self.camera = Camera()
        
        # Lighting setup
        self.lighting = Lighting()
        self.lighting.setup()
        
        # Scene objects
        self.road = Road()
        self.buildings = []
        self.trees = []
        self.cars = []
        
        # Generate initial city
        self.generate_city()
        
        # Animation state
        self.animation_running = True
        self.car_speed = 1.0
        
        # Mouse control state
        self.mouse_down = False
        self.last_mouse_x = 0
        self.last_mouse_y = 0
        
        # FPS control
        self.clock = pygame.time.Clock()
        self.fps = 60
        
    def generate_city(self):
        """Generate or regenerate city layout"""
        self.buildings, self.trees = generate_random_city(num_buildings=15, num_trees=10)
        self.cars = create_cars(num_cars=4)
    
    def screen_to_world(self, mouse_x, mouse_y):
        """
        Convert screen coordinates to world coordinates on the ground plane (y=0)
        Args:
            mouse_x: Mouse X coordinate in screen space
            mouse_y: Mouse Y coordinate in screen space
        Returns:
            tuple: (x, z) world coordinates or None if no intersection
        """
        # Get viewport, modelview, and projection matrices
        viewport = glGetIntegerv(GL_VIEWPORT)
        modelview = glGetDoublev(GL_MODELVIEW_MATRIX)
        projection = glGetDoublev(GL_PROJECTION_MATRIX)
        
        # Convert mouse coordinates to OpenGL coordinates (flip Y)
        win_x = float(mouse_x)
        win_y = float(viewport[3] - mouse_y)
        
        # Unproject at near and far planes
        try:
            # Near plane
            near_point = gluUnProject(win_x, win_y, 0.0, modelview, projection, viewport)
            # Far plane
            far_point = gluUnProject(win_x, win_y, 1.0, modelview, projection, viewport)
            
            # Calculate intersection with ground plane (y = 0)
            # Ray equation: P = near_point + t * (far_point - near_point)
            # For ground plane: y = 0
            # near_point[1] + t * (far_point[1] - near_point[1]) = 0
            
            if abs(far_point[1] - near_point[1]) < 0.0001:
                return None  # Ray is parallel to ground
            
            t = -near_point[1] / (far_point[1] - near_point[1])
            
            if t < 0 or t > 1:
                return None  # Intersection is outside the ray segment
            
            # Calculate world coordinates
            world_x = near_point[0] + t * (far_point[0] - near_point[0])
            world_z = near_point[2] + t * (far_point[2] - near_point[2])
            
            return (world_x, world_z)
        except:
            return None
    
    def show_building_dialog(self, x, z):
        """
        Show a dialog to input building parameters and create building at position
        Args:
            x: X coordinate in world space
            z: Z coordinate in world space
        """
        # Create a simple dialog window
        dialog = tk.Toplevel()
        dialog.title("Add Building")
        dialog.geometry("300x220")
        dialog.resizable(False, False)
        dialog.transient()  # Keep on top
        dialog.grab_set()  # Modal dialog
        
        # Position label
        tk.Label(dialog, text=f"Position: X={x:.1f}, Z={z:.1f}", 
                font=("Arial", 10, "bold")).pack(pady=10)
        
        # Width input
        width_frame = tk.Frame(dialog)
        width_frame.pack(pady=5)
        tk.Label(width_frame, text="Width:", width=10, anchor='w').pack(side=tk.LEFT)
        width_entry = tk.Entry(width_frame, width=10)
        width_entry.insert(0, "3")
        width_entry.pack(side=tk.LEFT)
        
        # Depth input
        depth_frame = tk.Frame(dialog)
        depth_frame.pack(pady=5)
        tk.Label(depth_frame, text="Depth:", width=10, anchor='w').pack(side=tk.LEFT)
        depth_entry = tk.Entry(depth_frame, width=10)
        depth_entry.insert(0, "3")
        depth_entry.pack(side=tk.LEFT)
        
        # Height input
        height_frame = tk.Frame(dialog)
        height_frame.pack(pady=5)
        tk.Label(height_frame, text="Height:", width=10, anchor='w').pack(side=tk.LEFT)
        height_entry = tk.Entry(height_frame, width=10)
        height_entry.insert(0, "10")
        height_entry.pack(side=tk.LEFT)
        
        # Buttons
        button_frame = tk.Frame(dialog)
        button_frame.pack(pady=15)
        
        def create_building():
            try:
                width = float(width_entry.get())
                depth = float(depth_entry.get())
                height = float(height_entry.get())
                
                # Validate
                if width <= 0 or width > 10:
                    messagebox.showwarning("Invalid Input", "Width must be between 0 and 10")
                    return
                if depth <= 0 or depth > 10:
                    messagebox.showwarning("Invalid Input", "Depth must be between 0 and 10")
                    return
                if height <= 0 or height > 30:
                    messagebox.showwarning("Invalid Input", "Height must be between 0 and 30")
                    return
                
                # Create building
                building = Building(x, z, width=width, height=height, depth=depth)
                self.buildings.append(building)
                dialog.destroy()
                
            except ValueError:
                messagebox.showerror("Error", "Please enter valid numbers")
        
        tk.Button(button_frame, text="Create", command=create_building, 
                 width=10, bg="#51cf66", fg="white").pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Cancel", command=dialog.destroy, 
                 width=10).pack(side=tk.LEFT, padx=5)
        
    def handle_events(self):
        """Handle pygame events (keyboard, mouse)"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
                
            # Mouse button events
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    self.mouse_down = True
                    self.last_mouse_x, self.last_mouse_y = event.pos
                elif event.button == 3:  # Right mouse button
                    # Get world coordinates from mouse position
                    world_pos = self.screen_to_world(event.pos[0], event.pos[1])
                    if world_pos:
                        # Show dialog to add building at this position
                        self.show_building_dialog(world_pos[0], world_pos[1])
                elif event.button == 4:  # Mouse wheel up (zoom in)
                    self.camera.zoom_camera(-2.0)
                elif event.button == 5:  # Mouse wheel down (zoom out)
                    self.camera.zoom_camera(2.0)
                    
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.mouse_down = False
                    
            # Mouse motion for camera rotation
            elif event.type == pygame.MOUSEMOTION:
                if self.mouse_down:
                    x, y = event.pos
                    dx = x - self.last_mouse_x
                    dy = y - self.last_mouse_y
                    
                    # Rotate camera
                    self.camera.rotate(dx * 0.5, -dy * 0.5)
                    
                    self.last_mouse_x = x
                    self.last_mouse_y = y
            
            # Keyboard events
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                elif event.key == pygame.K_SPACE:
                    self.animation_running = not self.animation_running
                elif event.key == pygame.K_r:
                    self.generate_city()
                # Camera zoom with +/-
                elif event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                    self.camera.zoom_camera(-2.0)
                elif event.key == pygame.K_MINUS:
                    self.camera.zoom_camera(2.0)
                # View presets
                elif event.key == pygame.K_1:
                    self.camera.set_preset_view('top')
                elif event.key == pygame.K_2:
                    self.camera.set_preset_view('street')
                elif event.key == pygame.K_3:
                    self.camera.set_preset_view('45')
                # Arrow keys for camera rotation
                elif event.key == pygame.K_LEFT:
                    self.camera.rotate(-5.0, 0.0)
                elif event.key == pygame.K_RIGHT:
                    self.camera.rotate(5.0, 0.0)
                elif event.key == pygame.K_UP:
                    self.camera.rotate(0.0, 5.0)
                elif event.key == pygame.K_DOWN:
                    self.camera.rotate(0.0, -5.0)
                # WASD keys for camera panning (moving target)
                elif event.key == pygame.K_w:
                    self.camera.move_target(0.0, -2.0)
                elif event.key == pygame.K_s:
                    self.camera.move_target(0.0, 2.0)
                elif event.key == pygame.K_a:
                    self.camera.move_target(-2.0, 0.0)
                elif event.key == pygame.K_d:
                    self.camera.move_target(2.0, 0.0)
        
        return True
    
    def update(self):
        """Update animation state"""
        if self.animation_running:
            for car in self.cars:
                car.update(self.car_speed)
    
    def render(self):
        """Render the 3D scene"""
        # Clear screen
        self.renderer.clear_screen()
        
        # Apply camera transformations
        self.camera.apply_view()
        
        # Update lighting
        self.lighting.update_position()
        
        # Draw ground plane
        self.draw_ground()
        
        # Draw road network
        self.road.draw()
        
        # Draw buildings
        for building in self.buildings:
            building.draw()
        
        # Draw trees
        for tree in self.trees:
            tree.draw()
        
        # Draw cars
        for car in self.cars:
            car.draw()
        
        # Swap buffers
        self.renderer.swap_buffers()
    
    def draw_ground(self):
        """Draw simple ground plane"""
        glPushMatrix()
        glColor3f(0.2, 0.5, 0.2)  # Green grass
        
        glBegin(GL_QUADS)
        glNormal3f(0, 1, 0)
        size = 100
        glVertex3f(-size, 0, -size)
        glVertex3f(size, 0, -size)
        glVertex3f(size, 0, size)
        glVertex3f(-size, 0, size)
        glEnd()
        
        glPopMatrix()
    
    def run(self):
        """Main application loop"""
        running = True
        
        while running:
            # Handle events
            running = self.handle_events()
            
            # Update simulation
            self.update()
            
            # Render scene
            self.render()
            
            # Control frame rate
            self.clock.tick(self.fps)
        
        # Cleanup
        pygame.quit()


class ControlGUI:
    """Tkinter GUI for controlling the simulation"""
    
    def __init__(self, simulation):
        """
        Initialize control GUI
        Args:
            simulation: CitySimulation instance to control
        """
        self.simulation = simulation
        
        # Create Tkinter window
        self.root = tk.Tk()
        self.root.title("3D City Simulation Controls")
        self.root.geometry("300x550")
        self.root.resizable(False, False)
        
        # Create GUI elements
        self.create_widgets()
        
    def create_widgets(self):
        """Create GUI control widgets"""
        # Title
        title = tk.Label(self.root, text="3D City Simulation", font=("Arial", 16, "bold"))
        title.pack(pady=10)
        
        # Instructions
        instructions = tk.Label(
            self.root, 
            text="Mouse: Drag to rotate\nWheel: Zoom\nSpace: Pause/Resume\nR: Regenerate city",
            justify=tk.LEFT,
            font=("Arial", 9)
        )
        instructions.pack(pady=5)
        
        # Separator
        ttk.Separator(self.root, orient='horizontal').pack(fill='x', pady=10)
        
        # Animation control
        anim_frame = tk.LabelFrame(self.root, text="Animation Control", padx=10, pady=10)
        anim_frame.pack(padx=10, pady=5, fill='x')
        
        # Start/Stop button
        self.anim_button = tk.Button(
            anim_frame,
            text="Stop Animation",
            command=self.toggle_animation,
            width=20,
            bg="#ff6b6b",
            fg="white",
            font=("Arial", 10, "bold")
        )
        self.anim_button.pack(pady=5)
        
        # Speed control
        speed_label = tk.Label(anim_frame, text="Car Speed:")
        speed_label.pack()
        
        self.speed_slider = tk.Scale(
            anim_frame,
            from_=0.0,
            to=3.0,
            resolution=0.1,
            orient=tk.HORIZONTAL,
            command=self.update_speed,
            length=200
        )
        self.speed_slider.set(1.0)
        self.speed_slider.pack(pady=5)
        
        # View presets
        view_frame = tk.LabelFrame(self.root, text="Camera Views", padx=10, pady=10)
        view_frame.pack(padx=10, pady=5, fill='x')
        
        tk.Button(
            view_frame,
            text="Top View",
            command=lambda: self.set_view('top'),
            width=20
        ).pack(pady=2)
        
        tk.Button(
            view_frame,
            text="Street View",
            command=lambda: self.set_view('street'),
            width=20
        ).pack(pady=2)
        
        tk.Button(
            view_frame,
            text="45° View",
            command=lambda: self.set_view('45'),
            width=20
        ).pack(pady=2)
        
        # Add Building section
        building_frame = tk.LabelFrame(self.root, text="Add Custom Building", padx=10, pady=10)
        building_frame.pack(padx=10, pady=5, fill='x')
        
        # Position controls
        pos_frame = tk.Frame(building_frame)
        pos_frame.pack(fill='x', pady=2)
        tk.Label(pos_frame, text="Position X:", width=10, anchor='w').pack(side=tk.LEFT)
        self.pos_x = tk.Entry(pos_frame, width=8)
        self.pos_x.insert(0, "0")
        self.pos_x.pack(side=tk.LEFT, padx=2)
        tk.Label(pos_frame, text="Z:", width=3).pack(side=tk.LEFT)
        self.pos_z = tk.Entry(pos_frame, width=8)
        self.pos_z.insert(0, "0")
        self.pos_z.pack(side=tk.LEFT, padx=2)
        
        # Size controls
        size_frame = tk.Frame(building_frame)
        size_frame.pack(fill='x', pady=2)
        tk.Label(size_frame, text="Width:", width=10, anchor='w').pack(side=tk.LEFT)
        self.building_width = tk.Entry(size_frame, width=8)
        self.building_width.insert(0, "3")
        self.building_width.pack(side=tk.LEFT, padx=2)
        tk.Label(size_frame, text="Depth:", width=3).pack(side=tk.LEFT)
        self.building_depth = tk.Entry(size_frame, width=8)
        self.building_depth.insert(0, "3")
        self.building_depth.pack(side=tk.LEFT, padx=2)
        
        # Height control
        height_frame = tk.Frame(building_frame)
        height_frame.pack(fill='x', pady=2)
        tk.Label(height_frame, text="Height:", width=10, anchor='w').pack(side=tk.LEFT)
        self.building_height = tk.Entry(height_frame, width=8)
        self.building_height.insert(0, "10")
        self.building_height.pack(side=tk.LEFT, padx=2)
        
        # Add Building button
        tk.Button(
            building_frame,
            text="➕ Add Building",
            command=self.add_building,
            width=20,
            bg="#95e1d3",
            font=("Arial", 9, "bold")
        ).pack(pady=5)
        
        # Random city button
        random_frame = tk.Frame(self.root, padx=10, pady=10)
        random_frame.pack(padx=10, pady=5, fill='x')
        
        tk.Button(
            random_frame,
            text="🔄 Generate Random City",
            command=self.regenerate_city,
            width=25,
            bg="#4ecdc4",
            fg="white",
            font=("Arial", 10, "bold")
        ).pack()
        
    def toggle_animation(self):
        """Toggle animation on/off"""
        self.simulation.animation_running = not self.simulation.animation_running
        
        if self.simulation.animation_running:
            self.anim_button.config(text="Stop Animation", bg="#ff6b6b")
        else:
            self.anim_button.config(text="Start Animation", bg="#51cf66")
    
    def update_speed(self, value):
        """Update car speed from slider"""
        self.simulation.car_speed = float(value)
    
    def set_view(self, view_type):
        """Set camera to preset view"""
        self.simulation.camera.set_preset_view(view_type)
    
    def regenerate_city(self):
        """Regenerate random city layout"""
        self.simulation.generate_city()
    
    def add_building(self):
        """Add a custom building with user-specified parameters"""
        try:
            # Get values from input fields
            x = float(self.pos_x.get())
            z = float(self.pos_z.get())
            width = float(self.building_width.get())
            height = float(self.building_height.get())
            depth = float(self.building_depth.get())
            
            # Validate ranges
            if width <= 0 or width > 10:
                tk.messagebox.showwarning("Invalid Input", "Width must be between 0 and 10")
                return
            if height <= 0 or height > 30:
                tk.messagebox.showwarning("Invalid Input", "Height must be between 0 and 30")
                return
            if depth <= 0 or depth > 10:
                tk.messagebox.showwarning("Invalid Input", "Depth must be between 0 and 10")
                return
            if abs(x) > 30 or abs(z) > 30:
                tk.messagebox.showwarning("Invalid Input", "Position must be within ±30 from center")
                return
            
            # Create and add building
            building = Building(x, z, width=width, height=height, depth=depth)
            self.simulation.buildings.append(building)
            
            # Show success message
            tk.messagebox.showinfo("Success", f"Building added at ({x}, {z})")
            
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter valid numbers for all fields")
    
    def run(self):
        """Run the GUI main loop"""
        self.root.mainloop()


def main():
    """Main entry point"""
    print("=" * 50)
    print("3D City Simulation")
    print("=" * 50)
    print("\nControls:")
    print("  Mouse Drag: Rotate camera")
    print("  Mouse Wheel: Zoom in/out")
    print("  Arrow Keys: Rotate camera (↑↓←→)")
    print("  WASD: Move view position")
    print("  Space: Pause/Resume animation")
    print("  R: Regenerate city")
    print("  1: Top view")
    print("  2: Street view")
    print("  3: 45° view")
    print("  +/-: Zoom in/out")
    print("  ESC: Exit")
    print("\nStarting simulation...")
    print("=" * 50)
    
    # Create simulation
    simulation = CitySimulation()
    
    # Create and run GUI in separate thread
    gui = ControlGUI(simulation)
    gui_thread = threading.Thread(target=gui.run, daemon=True)
    gui_thread.start()
    
    # Run simulation
    try:
        simulation.run()
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        sys.exit(0)


if __name__ == "__main__":
    main()
