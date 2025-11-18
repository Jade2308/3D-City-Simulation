"""
Tree class for 3D city simulation
Renders simple trees using cylinders (trunk) and spheres (foliage)
"""
from OpenGL.GL import *
from OpenGL.GLU import *
import math


class Tree:
    def __init__(self, x, z):
        """
        Create a tree at position (x, z)
        Args:
            x: X position
            z: Z position
        """
        self.x = x
        self.z = z
        
        # Tree properties
        self.trunk_height = 2.0
        self.trunk_radius = 0.2
        self.foliage_radius = 1.0
        
        # Colors
        self.trunk_color = (0.4, 0.25, 0.1)  # Brown
        self.foliage_color = (0.1, 0.6, 0.1)  # Green
        
    def draw(self):
        """Render the tree"""
        glPushMatrix()
        glTranslatef(self.x, 0, self.z)
        
        # Draw trunk (cylinder)
        self.draw_trunk()
        
        # Draw foliage (sphere)
        self.draw_foliage()
        
        glPopMatrix()
    
    def draw_trunk(self):
        """Draw tree trunk as a cylinder"""
        glPushMatrix()
        glColor3f(*self.trunk_color)
        
        # Rotate to make cylinder vertical
        glRotatef(-90, 1, 0, 0)
        
        # Create quadric object for cylinder
        quad = gluNewQuadric()
        gluCylinder(quad, self.trunk_radius, self.trunk_radius, self.trunk_height, 16, 1)
        gluDeleteQuadric(quad)
        
        glPopMatrix()
    
    def draw_foliage(self):
        """Draw tree foliage as a sphere"""
        glPushMatrix()
        glColor3f(*self.foliage_color)
        
        # Position foliage at top of trunk
        glTranslatef(0, self.trunk_height + self.foliage_radius * 0.5, 0)
        
        # Create quadric object for sphere
        quad = gluNewQuadric()
        gluSphere(quad, self.foliage_radius, 16, 16)
        gluDeleteQuadric(quad)
        
        glPopMatrix()
