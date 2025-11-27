"""
Camera class for 3D city simulation
Handles camera position, rotation and view transformations
"""
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *


class Camera:
    def __init__(self):
        """Initialize camera with default position and orientation"""
        # Camera position
        self.position = np.array([0.0, 10.0, 30.0], dtype=np.float32)
        
        # Camera rotation angles (in degrees)
        self.yaw = 0.0    # Rotation around Y-axis (left/right)
        self.pitch = -20.0  # Rotation around X-axis (up/down)
        
        # Camera parameters - increased for larger city
        self.zoom = 80.0  # Start zoomed out more to see the expanded city
        self.min_zoom = 10.0
        self.max_zoom = 250.0  # Increased to see the larger city
        
        # Look at target
        self.target = np.array([0.0, 0.0, 0.0], dtype=np.float32)
        
    def apply_view(self):
        """Apply camera transformations to OpenGL"""
        glLoadIdentity()
        
        # Calculate camera position based on angles and zoom
        x = self.target[0] + self.zoom * np.cos(np.radians(self.pitch)) * np.sin(np.radians(self.yaw))
        y = self.target[1] + self.zoom * np.sin(np.radians(self.pitch))
        z = self.target[2] + self.zoom * np.cos(np.radians(self.pitch)) * np.cos(np.radians(self.yaw))
        
        # Set up the camera view
        gluLookAt(
            x, y, z,  # Camera position
            self.target[0], self.target[1], self.target[2],  # Look at point
            0.0, 1.0, 0.0  # Up vector
        )
    
    def rotate(self, delta_yaw, delta_pitch):
        """
        Rotate camera by given angles
        Args:
            delta_yaw: Change in yaw (left/right rotation)
            delta_pitch: Change in pitch (up/down rotation)
        """
        self.yaw += delta_yaw
        self.pitch += delta_pitch
        
        # Clamp pitch to prevent flipping
        self.pitch = max(-89.0, min(89.0, self.pitch))
        
    def zoom_camera(self, delta):
        """
        Zoom in/out
        Args:
            delta: Amount to zoom (positive = zoom out, negative = zoom in)
        """
        self.zoom += delta
        self.zoom = max(self.min_zoom, min(self.max_zoom, self.zoom))
    
    def set_preset_view(self, view_type):
        """
        Set camera to predefined view
        Args:
            view_type: 'top', 'street', or '45'
        """
        if view_type == 'top':
            # Top-down view - increased zoom for larger city
            self.yaw = 0.0
            self.pitch = -89.0
            self.zoom = 150.0
        elif view_type == 'street':
            # Street level view
            self.yaw = 0.0
            self.pitch = -5.0
            self.zoom = 25.0
        elif view_type == '45':
            # 45 degree angled view - increased zoom for larger city
            self.yaw = 45.0
            self.pitch = -30.0
            self.zoom = 100.0
    
    def move_target(self, dx, dz):
        """
        Move the camera target (pan the view)
        Args:
            dx: Movement in X direction
            dz: Movement in Z direction
        """
        self.target[0] += dx
        self.target[2] += dz
    
    def get_camera_position(self):
        """
        Get the current camera position in world coordinates
        Returns:
            tuple: (x, y, z) camera position
        """
        x = self.target[0] + self.zoom * np.cos(np.radians(self.pitch)) * np.sin(np.radians(self.yaw))
        y = self.target[1] + self.zoom * np.sin(np.radians(self.pitch))
        z = self.target[2] + self.zoom * np.cos(np.radians(self.pitch)) * np.cos(np.radians(self.yaw))
        return (x, y, z)
