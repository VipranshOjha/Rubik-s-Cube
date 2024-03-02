import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class RubiksCube3D:
    def __init__(self):
        self.window_width = 800
        self.window_height = 600
        self.angle_x = 0
        self.angle_y = 0

        self.face_rotation_angle = 0
        self.face_rotation_axis = (0, 0, 0)

        self.colors = {
            'white': (1, 1, 1),
            'yellow': (1, 1, 0),
            'blue': (0, 0.5, 1),
            'green': (0, 1, 0),
            'red': (1, 0, 0),
            'orange': (1, 0.5, 0),
            'black': (0, 0, 0)
        }

        pygame.init()
        pygame.display.set_mode((self.window_width, self.window_height), DOUBLEBUF | OPENGL | OPENGLBLIT)
        glEnable(GL_DEPTH_TEST)
        glMatrixMode(GL_PROJECTION)
        gluPerspective(45, (self.window_width / self.window_height), 0.1, 50.0)
        glMatrixMode(GL_MODELVIEW)
        glTranslatef(0.0, 0.0, -5)

    def draw_small_cube(self, color):
        glBegin(GL_QUADS)
        glColor3fv(color)

        glVertex3fv((-0.5, -0.5, -0.5))
        glVertex3fv((0.5, -0.5, -0.5))
        glVertex3fv((0.5, 0.5, -0.5))
        glVertex3fv((-0.5, 0.5, -0.5))

        glVertex3fv((0.5, -0.5, -0.5))
        glVertex3fv((0.5, -0.5, 0.5))
        glVertex3fv((0.5, 0.5, 0.5))
        glVertex3fv((0.5, 0.5, -0.5))

        glVertex3fv((-0.5, -0.5, 0.5))
        glVertex3fv((0.5, -0.5, 0.5))
        glVertex3fv((0.5, 0.5, 0.5))
        glVertex3fv((-0.5, 0.5, 0.5))

        glVertex3fv((-0.5, -0.5, -0.5))
        glVertex3fv((-0.5, -0.5, 0.5))
        glVertex3fv((-0.5, 0.5, 0.5))
        glVertex3fv((-0.5, 0.5, -0.5))

        glVertex3fv((-0.5, 0.5, -0.5))
        glVertex3fv((0.5, 0.5, -0.5))
        glVertex3fv((0.5, 0.5, 0.5))
        glVertex3fv((-0.5, 0.5, 0.5))

        glVertex3fv((-0.5, -0.5, -0.5))
        glVertex3fv((0.5, -0.5, -0.5))
        glVertex3fv((0.5, -0.5, 0.5))
        glVertex3fv((-0.5, -0.5, 0.5))
        glEnd()

        # Draw black outlines
        glLineWidth(2)
        glColor3fv(self.colors['black'])
        glBegin(GL_LINES)
        glVertex3fv((-0.5, -0.5, -0.5))
        glVertex3fv((0.5, -0.5, -0.5))

        glVertex3fv((0.5, -0.5, -0.5))
        glVertex3fv((0.5, 0.5, -0.5))

        glVertex3fv((0.5, 0.5, -0.5))
        glVertex3fv((-0.5, 0.5, -0.5))

        glVertex3fv((-0.5, 0.5, -0.5))
        glVertex3fv((-0.5, -0.5, -0.5))

        glVertex3fv((0.5, -0.5, -0.5))
        glVertex3fv((0.5, -0.5, 0.5))

        glVertex3fv((0.5, -0.5, 0.5))
        glVertex3fv((0.5, 0.5, 0.5))

        glVertex3fv((0.5, 0.5, 0.5))
        glVertex3fv((-0.5, 0.5, 0.5))

        glVertex3fv((-0.5, 0.5, 0.5))
        glVertex3fv((-0.5, -0.5, 0.5))

        glVertex3fv((-0.5, -0.5, 0.5))
        glVertex3fv((-0.5, -0.5, -0.5))

        glVertex3fv((-0.5, -0.5, 0.5))
        glVertex3fv((0.5, -0.5, 0.5))

        glVertex3fv((-0.5, 0.5, 0.5))
        glVertex3fv((0.5, 0.5, 0.5))

        glVertex3fv((0.5, -0.5, 0.5))
        glVertex3fv((0.5, -0.5, -0.5))
        glEnd()

    def draw_face(self, color):
        glPushMatrix()
        for i in range(3):
            glPushMatrix()
            for j in range(3):
                self.draw_small_cube(color)
                glTranslatef(1, 0, 0)
            glPopMatrix()
            glTranslatef(0, 1, 0)
        glPopMatrix()

    def draw_cube(self):
        glPushMatrix()
        glRotatef(self.angle_x, 1, 0, 0)
        glRotatef(self.angle_y, 0, 1, 0)

        # Draw front face
        glPushMatrix()
        glTranslatef(-1, -1, -1)
        self.draw_face(self.colors['white'])  # White
        glPopMatrix()

        # Draw back face
        glPushMatrix()
        glTranslatef(1, -1, 1)
        glRotatef(180, 0, 1, 0)
        self.draw_face(self.colors['yellow'])  # Yellow
        glPopMatrix()

        # Draw top face
        glPushMatrix()
        glTranslatef(-1, 1, 1)
        glRotatef(270, 1, 0, 0)
        self.draw_face(self.colors['blue'])  # Blue
        glPopMatrix()

        # Draw bottom face
        glPushMatrix()
        glTranslatef(-1, -1, -1)
        glRotatef(90, 1, 0, 0)
        self.draw_face(self.colors['green'])  # Green
        glPopMatrix()

        # Draw right face
        glPushMatrix()
        glTranslatef(1, -1, -1)
        glRotatef(270, 0, 1, 0)
        self.draw_face(self.colors['red'])  # Red
        glPopMatrix()

        # Draw left face
        glPushMatrix()
        glTranslatef(-1, -1, 1)
        glRotatef(90, 0, 1, 0)
        self.draw_face(self.colors['orange'])  # Orange
        glPopMatrix()

        glPopMatrix()

    def rotate_face_clockwise(self):
        glPushMatrix()
        glLoadIdentity()
        glRotatef(self.face_rotation_angle, *self.face_rotation_axis)
        self.angle_y += self.face_rotation_angle
        glMultMatrixf(glGetFloatv(GL_MODELVIEW_MATRIX))
        self.face_rotation_angle = 0
        glPopMatrix()

    def main_loop(self):
        while True:
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.face_rotation_angle = -90
                        self.face_rotation_axis = (0, 1, 0)
                    elif event.key == pygame.K_RIGHT:
                        self.face_rotation_angle = 90
                        self.face_rotation_axis = (0, 1, 0)
                    elif event.key == pygame.K_UP:
                        self.face_rotation_angle = -90
                        self.face_rotation_axis = (1, 0, 0)
                    elif event.key == pygame.K_DOWN:
                        self.face_rotation_angle = 90
                        self.face_rotation_axis = (1, 0, 0)

            self.draw_cube()
            self.rotate_face_clockwise()
            pygame.display.flip()
            pygame.time.wait(10)

if __name__ == "__main__":
    cube = RubiksCube3D()
    cube.main_loop()  # This line invokes the main_loop method
