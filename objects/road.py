"""
Road class for 3D city simulation
Renders roads as planes with lines
"""
from OpenGL.GL import *


class Road:
    def __init__(self):
        """Initialize road parameters"""
        # Road color (dark gray asphalt)
        self.color = (0.2, 0.2, 0.2)
        self.line_color = (0.9, 0.9, 0.0)  # Yellow lane markers
        
        # Road dimensions
        self.width = 60.0
        self.length = 60.0
        
    def draw(self):
        """Render the road network"""
        # Draw main horizontal road (extends in X direction)
        self.draw_road_segment(-self.length/2, 0, 4, self.length, 'horizontal')
        
        # Draw main vertical road (extends in Z direction)
        self.draw_road_segment(0, -self.width/2, 4, self.width, 'vertical')
        
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
            glVertex3f(x, 0.05, z - width/2)
            glVertex3f(x + length, 0.05, z - width/2)
            glVertex3f(x + length, 0.05, z + width/2)
            glVertex3f(x, 0.05, z + width/2)
        else:  # vertical
            glVertex3f(x - width/2, 0.05, z)
            glVertex3f(x + width/2, 0.05, z)
            glVertex3f(x + width/2, 0.05, z + length)
            glVertex3f(x - width/2, 0.05, z + length)
        
        glEnd()
        
        # Draw center line
        glColor3f(*self.line_color)
        glLineWidth(2.0)
        glBegin(GL_LINES)
        
        if orientation == 'horizontal':
            # Dashed center line
            num_dashes = int(length / 2)
            for i in range(num_dashes):
                start_x = x + i * 2
                end_x = start_x + 1
                if end_x <= x + length:
                    glVertex3f(start_x, 0.06, z)
                    glVertex3f(end_x, 0.06, z)
        else:  # vertical
            # Dashed center line
            num_dashes = int(length / 2)
            for i in range(num_dashes):
                start_z = z + i * 2
                end_z = start_z + 1
                if end_z <= z + length:
                    glVertex3f(x, 0.06, start_z)
                    glVertex3f(x, 0.06, end_z)
        
        glEnd()
        glLineWidth(1.0)
        
        glPopMatrix()
