"""
OpenGL Renderer for 3D city simulation
Handles rendering setup and scene drawing
"""
from OpenGL.GL import *
from OpenGL.GLU import *
import pygame


class Renderer:
    def __init__(self, width=800, height=600):
        """
        Initialize renderer
        Args:
            width: Window width
            height: Window height
        """
        self.width = width
        self.height = height
        self.display = None
        
    def init_pygame(self):
        """Initialize pygame and OpenGL context"""
        pygame.init()
        
        # Create OpenGL-enabled pygame window
        self.display = pygame.display.set_mode(
            (self.width, self.height),
            pygame.DOUBLEBUF | pygame.OPENGL
        )
        pygame.display.set_caption("3D City Simulation")
        
        # Setup OpenGL viewport and perspective
        self.setup_perspective()
        
        # Enable smooth shading
        glShadeModel(GL_SMOOTH)
        
        # Set background color (sky blue)
        glClearColor(0.53, 0.81, 0.92, 1.0)
        
    def setup_perspective(self):
        """Configure OpenGL perspective projection"""
        glViewport(0, 0, self.width, self.height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        
        # Set perspective: FOV=45, aspect ratio, near=0.1, far=500.0
        gluPerspective(45, self.width / self.height, 0.1, 500.0)
        
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
    
    def clear_screen(self):
        """Clear screen and depth buffer before rendering"""
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    def swap_buffers(self):
        """Display the rendered frame"""
        pygame.display.flip()
