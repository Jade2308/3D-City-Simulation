"""
Road class for 3D city simulation
Renders roads as planes with lines
"""
from OpenGL.GL import *


class Road:
    def __init__(self):
        """Initialize road parameters"""
        # Road color (medium gray asphalt - lighter for better visibility when zoomed out)
        self.color = (0.3, 0.3, 0.3)
        self.line_color = (0.9, 0.9, 0.0)  # Yellow lane markers
        self.edge_color = (0.9, 0.9, 0.9)  # White edge markers
        
        # Road dimensions - expanded for larger city
        self.road_width = 8.0  # Width of each road
        self.road_length = 150.0  # Length of each road (expanded from 60)
        self.grid_spacing = 50.0  # Spacing between parallel roads
        
    def draw(self):
        """Render the road network - expanded grid layout"""
        # Draw horizontal roads (east-west)
        for offset in [-self.grid_spacing, 0, self.grid_spacing]:
            self.draw_road_segment(-self.road_length/2, offset, self.road_width, self.road_length, 'horizontal')
        
        # Draw vertical roads (north-south)
        for offset in [-self.grid_spacing, 0, self.grid_spacing]:
            self.draw_road_segment(offset, -self.road_length/2, self.road_width, self.road_length, 'vertical')
        
    def draw_road_segment(self, x, z, width, length, orientation):
        """
        Draw a single road segment
        Args:
            x, z: Position
            width, length: Dimensions
            orientation: 'horizontal' or 'vertical'
        """
        glPushMatrix()
        
        # Draw road surface
        glColor3f(*self.color)
        glBegin(GL_QUADS)
        glNormal3f(0, 1, 0)
        
        if orientation == 'horizontal':
            glVertex3f(x, 0.35, z - width/2)
            glVertex3f(x + length, 0.35, z - width/2)
            glVertex3f(x + length, 0.35, z + width/2)
            glVertex3f(x, 0.35, z + width/2)
        else:  # vertical
            glVertex3f(x - width/2, 0.35, z)
            glVertex3f(x + width/2, 0.35, z)
            glVertex3f(x + width/2, 0.35, z + length)
            glVertex3f(x - width/2, 0.35, z + length)
        
        glEnd()
        
        # Draw edge lines (white) for better visibility when zoomed out
        glColor3f(*self.edge_color)
        glLineWidth(3.0)
        glBegin(GL_LINES)
        
        if orientation == 'horizontal':
            # Top edge
            glVertex3f(x, 0.37, z + width/2)
            glVertex3f(x + length, 0.37, z + width/2)
            # Bottom edge
            glVertex3f(x, 0.37, z - width/2)
            glVertex3f(x + length, 0.37, z - width/2)
        else:  # vertical
            # Left edge
            glVertex3f(x - width/2, 0.37, z)
            glVertex3f(x - width/2, 0.37, z + length)
            # Right edge
            glVertex3f(x + width/2, 0.37, z)
            glVertex3f(x + width/2, 0.37, z + length)
        
        glEnd()
        
        # Draw center line (yellow) - increased width for better visibility
        glColor3f(*self.line_color)
        glLineWidth(3.0)
        glBegin(GL_LINES)
        
        if orientation == 'horizontal':
            # Dashed center line
            num_dashes = int(length / 2)
            for i in range(num_dashes):
                start_x = x + i * 2
                end_x = start_x + 1
                if end_x <= x + length:
                    glVertex3f(start_x, 0.36, z)
                    glVertex3f(end_x, 0.36, z)
        else:  # vertical
            # Dashed center line
            num_dashes = int(length / 2)
            for i in range(num_dashes):
                start_z = z + i * 2
                end_z = start_z + 1
                if end_z <= z + length:
                    glVertex3f(x, 0.36, start_z)
                    glVertex3f(x, 0.36, end_z)
        
        glEnd()
        glLineWidth(1.0)
        
        glPopMatrix()
