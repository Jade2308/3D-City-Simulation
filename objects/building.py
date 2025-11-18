"""
Building class for 3D city simulation
Generates and renders random buildings (cubes and cuboids)
"""
from OpenGL.GL import *
import random


class Building:
    def __init__(self, x, z, width=None, height=None, depth=None, color=None):
        """
        Create a building at position (x, z)
        Args:
            x: X position
            z: Z position
            width: Building width (random if None)
            height: Building height (random if None)
            depth: Building depth (random if None)
            color: Building color tuple (random if None)
        """
        self.x = x
        self.z = z
        
        # Random dimensions if not provided
        self.width = width if width else random.uniform(2, 5)
        self.height = height if height else random.uniform(5, 20)
        self.depth = depth if depth else random.uniform(2, 5)
        
        # Random color if not provided (grayish building colors)
        if color:
            self.color = color
        else:
            gray = random.uniform(0.5, 0.8)
            self.color = (gray, gray, gray)
    
    def draw(self):
        """Render the building as a cuboid"""
        glPushMatrix()
        glTranslatef(self.x, self.height / 2, self.z)
        
        # Set building color
        glColor3f(*self.color)
        
        # Draw the building using quads
        w, h, d = self.width / 2, self.height / 2, self.depth / 2
        
        # Front face
        glBegin(GL_QUADS)
        glNormal3f(0, 0, 1)
        glVertex3f(-w, -h, d)
        glVertex3f(w, -h, d)
        glVertex3f(w, h, d)
        glVertex3f(-w, h, d)
        glEnd()
        
        # Back face
        glBegin(GL_QUADS)
        glNormal3f(0, 0, -1)
        glVertex3f(-w, -h, -d)
        glVertex3f(-w, h, -d)
        glVertex3f(w, h, -d)
        glVertex3f(w, -h, -d)
        glEnd()
        
        # Left face
        glBegin(GL_QUADS)
        glNormal3f(-1, 0, 0)
        glVertex3f(-w, -h, -d)
        glVertex3f(-w, -h, d)
        glVertex3f(-w, h, d)
        glVertex3f(-w, h, -d)
        glEnd()
        
        # Right face
        glBegin(GL_QUADS)
        glNormal3f(1, 0, 0)
        glVertex3f(w, -h, -d)
        glVertex3f(w, h, -d)
        glVertex3f(w, h, d)
        glVertex3f(w, -h, d)
        glEnd()
        
        # Top face
        glBegin(GL_QUADS)
        glNormal3f(0, 1, 0)
        glVertex3f(-w, h, -d)
        glVertex3f(-w, h, d)
        glVertex3f(w, h, d)
        glVertex3f(w, h, -d)
        glEnd()
        
        # Bottom face
        glBegin(GL_QUADS)
        glNormal3f(0, -1, 0)
        glVertex3f(-w, -h, -d)
        glVertex3f(w, -h, -d)
        glVertex3f(w, -h, d)
        glVertex3f(-w, -h, d)
        glEnd()
        
        glPopMatrix()
