import pygame as pg
from objects.object import Object

try:
    from OpenGL.GL import *
    from OpenGL.GLU import *
except ImportError:
    print("The GLCUBE example requires PyOpenGL")
    raise SystemExit


obj = Object()
obj.make_object()
CUBE_POINTS = obj.dfv()
CUBE_COLORS = obj.dfvc()
CUBE_QUAD_VERTS = obj.dff()
CUBE_EDGES = obj.dfe()

# CUBE_EDGES,CUBE_POINTS,CUBE_QUAD_VERTS,CUBE_COLORS = obj.example_cube()

def drawcube():
    "draw the cube"
    allpoints = list(zip(CUBE_POINTS, CUBE_COLORS))

    glBegin(GL_QUADS)
    for face in CUBE_QUAD_VERTS:
        for vert in face:
            pos, color = allpoints[vert]
            glColor3fv(color)
            glVertex3fv(pos)
    glEnd()

    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINES)
    for line in CUBE_EDGES:
        for vert in line:
            pos, color = allpoints[vert]
            glVertex3fv(pos)

    glEnd()


def init_gl_stuff():
    glEnable(GL_DEPTH_TEST)  # use our zbuffer
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, 640 / 480.0, 0.1, 100.0)  # setup lens
    glTranslatef(0.0, 0.0, -3.0)  # move back
    glRotatef(25, 1, 0, 0)  # orbit higher


def main():
    "run the demo"
    # initialize pygame and setup an opengl display
    pg.init()

    fullscreen = True
    pg.display.set_mode((640, 480), pg.OPENGL | pg.DOUBLEBUF )

    init_gl_stuff()

    going = True
    while going:
        # check for quit'n events
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT or (
                event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
            ):
                going = False

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_f:
                    if not fullscreen:
                        print("Changing to FULLSCREEN")
                        pg.display.set_mode(
                            (640, 480), pg.OPENGL | pg.DOUBLEBUF | pg.FULLSCREEN
                        )
                    else:
                        print("Changing to windowed mode")
                        pg.display.set_mode((640, 480), pg.OPENGL | pg.DOUBLEBUF)
                    fullscreen = not fullscreen
                    init_gl_stuff()

        # clear screen and move camera
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # orbit camera around by 1 degree
        glRotatef(1, 0, 1, 0)

        drawcube()
        pg.display.flip()
        pg.time.wait(10)


if __name__ == "__main__":
    main()
