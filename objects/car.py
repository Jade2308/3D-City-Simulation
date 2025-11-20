"""
Car class for 3D city simulation
Renders and animates cars moving along roads
"""
from OpenGL.GL import *
import math


class Car:
    def __init__(self, path_type='horizontal', color=None):
        """
        Create a car that moves along a path
        Args:
            path_type: 'horizontal' or 'vertical' path
            color: Car color tuple (random if None)
        """
        self.path_type = path_type
        
        # Car dimensions
        self.width = 1.0
        self.height = 0.8
        self.length = 2.0
        
        # Car color
        if color:
            self.color = color
        else:
            # Random bright car colors
            import random
            colors = [
                (1.0, 0.0, 0.0),  # Red
                (0.0, 0.0, 1.0),  # Blue
                (1.0, 1.0, 0.0),  # Yellow
                (0.0, 1.0, 0.0),  # Green
                (1.0, 0.5, 0.0),  # Orange
            ]
            self.color = random.choice(colors)
        
        # Movement properties
        self.position = 0.0
        self.speed = 0.05  # Units per frame
        
        # Path parameters
        if path_type == 'horizontal':
            self.path_start = -30.0
            self.path_end = 30.0
            self.lane_offset = 1.0  # Drive on right side
        else:  # vertical
            self.path_start = -30.0
            self.path_end = 30.0
            self.lane_offset = 1.0
    
    def update(self, speed_multiplier=1.0):
        """
        Update car position
        Args:
            speed_multiplier: Multiplier for car speed
        """
        self.position += self.speed * speed_multiplier
        
        # Loop back when reaching end
        if self.position > self.path_end:
            self.position = self.path_start
    
    def draw(self):
        """Render the car"""
        glPushMatrix()
        
        # Position car based on path type
        road_height = 0.25  # Match road elevation
        if self.path_type == 'horizontal':
            glTranslatef(self.position, road_height + self.height / 2, self.lane_offset)
            glRotatef(90, 0, 1, 0)  # Rotate to face along x-axis
        else:  # vertical
            glTranslatef(self.lane_offset, road_height + self.height / 2, self.position)
            # No rotation needed for vertical (already facing along z-axis)
        
        # Set car color
        glColor3f(*self.color)
        
        # Draw car body (simplified box)
        w, h, l = self.width / 2, self.height / 2, self.length / 2
        
        # Main body
        glBegin(GL_QUADS)
        
        # Front face
        glNormal3f(0, 0, 1)
        glVertex3f(-w, -h, l)
        glVertex3f(w, -h, l)
        glVertex3f(w, h, l)
        glVertex3f(-w, h, l)
        
        # Back face
        glNormal3f(0, 0, -1)
        glVertex3f(-w, -h, -l)
        glVertex3f(-w, h, -l)
        glVertex3f(w, h, -l)
        glVertex3f(w, -h, -l)
        
        # Left face
        glNormal3f(-1, 0, 0)
        glVertex3f(-w, -h, -l)
        glVertex3f(-w, -h, l)
        glVertex3f(-w, h, l)
        glVertex3f(-w, h, -l)
        
        # Right face
        glNormal3f(1, 0, 0)
        glVertex3f(w, -h, -l)
        glVertex3f(w, h, -l)
        glVertex3f(w, h, l)
        glVertex3f(w, -h, l)
        
        # Top face
        glNormal3f(0, 1, 0)
        glVertex3f(-w, h, -l)
        glVertex3f(-w, h, l)
        glVertex3f(w, h, l)
        glVertex3f(w, h, -l)
        
        # Bottom face
        glNormal3f(0, -1, 0)
        glVertex3f(-w, -h, -l)
        glVertex3f(w, -h, -l)
        glVertex3f(w, -h, l)
        glVertex3f(-w, -h, l)
        
        glEnd()
        
        # Draw cab/roof (smaller box on top)
        glPushMatrix()
        glTranslatef(0, h * 1.2, -l * 0.3)
        
        # Darker color for roof
        glColor3f(self.color[0] * 0.7, self.color[1] * 0.7, self.color[2] * 0.7)
        
        cab_w, cab_h, cab_l = w * 0.9, h * 0.6, l * 0.5
        
        glBegin(GL_QUADS)
        
        # Front
        glNormal3f(0, 0, 1)
        glVertex3f(-cab_w, -cab_h, cab_l)
        glVertex3f(cab_w, -cab_h, cab_l)
        glVertex3f(cab_w, cab_h, cab_l)
        glVertex3f(-cab_w, cab_h, cab_l)
        
        # Back
        glNormal3f(0, 0, -1)
        glVertex3f(-cab_w, -cab_h, -cab_l)
        glVertex3f(-cab_w, cab_h, -cab_l)
        glVertex3f(cab_w, cab_h, -cab_l)
        glVertex3f(cab_w, -cab_h, -cab_l)
        
        # Left
        glNormal3f(-1, 0, 0)
        glVertex3f(-cab_w, -cab_h, -cab_l)
        glVertex3f(-cab_w, -cab_h, cab_l)
        glVertex3f(-cab_w, cab_h, cab_l)
        glVertex3f(-cab_w, cab_h, -cab_l)
        
        # Right
        glNormal3f(1, 0, 0)
        glVertex3f(cab_w, -cab_h, -cab_l)
        glVertex3f(cab_w, cab_h, -cab_l)
        glVertex3f(cab_w, cab_h, cab_l)
        glVertex3f(cab_w, -cab_h, cab_l)
        
        # Top
        glNormal3f(0, 1, 0)
        glVertex3f(-cab_w, cab_h, -cab_l)
        glVertex3f(-cab_w, cab_h, cab_l)
        glVertex3f(cab_w, cab_h, cab_l)
        glVertex3f(cab_w, cab_h, -cab_l)
        
        glEnd()
        
        glPopMatrix()
        glPopMatrix()
