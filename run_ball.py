import turtle
import ball
import random

class RunBalls:
    def __init__(self):
        self.num_balls = 5
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        #print(canvas_width, canvas_height)
        self.ball_radius = 0.05 * self.canvas_width
        turtle.colormode(255)
        self.xpos = []
        self.ypos = []
        self.vx = []
        self.vy = []
        self.ball_color = []
        self.dt = 0.2 # time step

    def random_balls(self):
        for i in range(self.num_balls):
            self.xpos.append(random.uniform(-1 * self.canvas_width + self.ball_radius, self.canvas_width - self.ball_radius))
            self.ypos.append(random.uniform(-1 * self.canvas_height + self.ball_radius, self.canvas_height - self.ball_radius))
            self.vx.append(10 * random.uniform(-1.0, 1.0))
            self.vy.append(10 * random.uniform(-1.0, 1.0))
            self.ball_color.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        for i in range(self.num_balls):
            the_ball = Balls()
            ball.draw_ball(self.ball_color[i], self.ball_radius, self.xpos[i], self.ypos[i])
            ball.move_ball(i, self.xpos, self.ypos, self.vx, self.vy, self.dt)
            ball.update_ball_velocity(i, self.xpos, self.ypos, self.vx, self.vy, self.canvas_width, self.canvas_height, self.ball_radius)

    def draw_border(self):
        turtle.penup()
        turtle.goto(-self.canvas_width, -self.canvas_height)
        turtle.pensize(10)
        turtle.pendown()
        turtle.color((0, 0, 0))
        for i in range(2):
            turtle.forward(2 * self.canvas_width)
            turtle.left(90)
            turtle.forward(2 * self.canvas_height)
            turtle.left(90)


if __name__ == "__main__":
    simulation = RunBalls()
    while (True):
        turtle.clear()
        simulation.draw_border()
        simulation.random_balls()
        turtle.update()
    # hold the window; close it by clicking the window close 'x' mark
    turtle.done()

