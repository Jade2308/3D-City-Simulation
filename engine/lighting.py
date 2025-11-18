"""
Lighting setup for 3D city simulation
Provides basic OpenGL lighting configuration
"""
from OpenGL.GL import *


class Lighting:
    def __init__(self):
        """Initialize lighting parameters"""
        # Ambient light (overall scene brightness)
        self.ambient = [0.3, 0.3, 0.3, 1.0]
        
        # Diffuse light (main directional light)
        self.diffuse = [0.8, 0.8, 0.8, 1.0]
        
        # Specular light (reflections)
        self.specular = [1.0, 1.0, 1.0, 1.0]
        
        # Light position (sun-like from above and angle)
        self.position = [10.0, 20.0, 10.0, 1.0]
        
    def setup(self):
        """Configure OpenGL lighting"""
        # Enable lighting
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        
        # Enable depth testing for proper 3D rendering
        glEnable(GL_DEPTH_TEST)
        
        # Enable color material so we can use glColor
        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
        
        # Set light properties
        glLightfv(GL_LIGHT0, GL_AMBIENT, self.ambient)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, self.diffuse)
        glLightfv(GL_LIGHT0, GL_SPECULAR, self.specular)
        glLightfv(GL_LIGHT0, GL_POSITION, self.position)
        
        # Set material properties
        glMaterialfv(GL_FRONT, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
        glMaterialfv(GL_FRONT, GL_SHININESS, [50.0])
    
    def update_position(self):
        """Update light position (call each frame if light moves)"""
        glLightfv(GL_LIGHT0, GL_POSITION, self.position)
