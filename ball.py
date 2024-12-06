import turtle

class Balls:
    def __init__(self, size, x, y, vx, vy, color, id):
        self.size = size
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.mass = 100*size**2
        self.count = 0
        self.id = id
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        self.ball_radius = 0.05 * self.canvas_width

    def draw_ball(self):
        # draw a circle of radius equals to size centered at (x, y) and paint it with color
        turtle.penup()
        turtle.color(self.color)
        turtle.fillcolor(self.color)
        turtle.goto(self.x, self.y - self.size)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.size)
        turtle.end_fill()

    def move_ball(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

    def update_ball_velocity(self):
        # if the ball hits the side walls, reverse the vx velocity
        if abs(self.x[i]) > (self.canvas_width - self.ball_radius):
            self.vx[i] = -self.vx[i]

        # if the ball hits the ceiling or the floor, reverse the vy velocity
        if abs(self.y[i]) > (self.canvas_height - self.ball_radius):
            self.vy[i] = -self.vy[i]







