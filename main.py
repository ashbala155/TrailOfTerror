from abc import ABC, ABCMeta, abstractmethod

import turtle
import time

import random
import math

from threading import Thread
from platform import system

end_game = False 
level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "         HHHL AQ        ",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP XXXXXX   D      XXX KX",
    "X      FX   XXXX     X  X",
    "XXXX    X      X     X  X",
    "XK      X   X  X       FX",
    "XXXXXX  X   XK X   XXXXXX",
    "XE  XX  XXXDXXXXX  XXXXXX",
    "X   XX       EXXE      XX",
    "X   XXXXXXXXXXXXXXDXXXXXX",
    "X         XXXXXX       FX",
    "X                  XXXXXX",
    "X  XXXXXDXXXXXXXXXXXXX EX",
    "XK XXXF          XXXXK  X",
    "XXXXXXXXXXXXXXX         X",
    "XF            D         X",
    "XXXXX       XXXX   XXXXXX",
    "XXK     XXXDXXXXXXXXXXXXX",
    "XXXXXXXXXX    E         X",
    "XXX              XXXXX KX",
    "XF   XXXXXXXXXXXXX   EXXX",
    "XX    XX  KXXX  FXX     X",
    "XX                D     W",
    "XXXXXXXXXXXXXXXXXXX     X",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"
]

def end_game_function():
    global end_game
    end_game = True


window = turtle.Screen()  
window.title("TRAIL OF TERROR")
window.bgcolor("black")    
window.setup(700, 700)  
window.tracer(0)  

turtle.register_shape(r"A.gif")
turtle.register_shape(r"B.gif")
turtle.register_shape(r"C.gif")

turtle.register_shape(r"background.gif")
turtle.register_shape(r"wall.gif")
turtle.register_shape(r"door.gif")

turtle.register_shape(r"player_right.gif")
turtle.register_shape(r"player_left.gif")
turtle.register_shape(r"enemy_left.gif")
turtle.register_shape(r"enemy_right.gif")

turtle.register_shape(r"heart.gif")
turtle.register_shape(r"key.gif")
turtle.register_shape(r"cros.gif")
turtle.register_shape(r"cross.gif")
turtle.register_shape(r"black_square.gif")

turtle.register_shape(r"one.gif")
turtle.register_shape(r"two.gif")
turtle.register_shape(r"three.gif")

turtle.register_shape(r"winner.gif")
turtle.register_shape(r"loser.gif")
turtle.register_shape(r"exit.gif")


for i in range(4):
    window.bgpic(r"A.gif")  
    window.update()  
    time.sleep(0.5)  
    window.bgpic(r"B.gif") 
    window.update()  
    time.sleep(0.5) 
    window.bgpic(r"C.gif")  
    window.update()  
    time.sleep(0.5)  

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape(r"wall.gif")
        self.penup()
        self.speed(0)

class Door(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape(r"door.gif")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

class Health(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape(r"heart.gif")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

class Key(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape(r"key.gif")
        self.penup()
        self.speed(0)
        self.key = True
        self.goto(x, y)
    
    def destroy(self):
        self.goto(3000, 3000)
        self.hideturtle()

class Key_Notif(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape(r"key.gif")
        self.penup()
        self.speed(0)

class BlackSquare(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape(r"black_square.gif")
        self.penup()
        self.speed(0)

class cross(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape(r"cross.gif")
        self.penup()
        self.speed(0)

class crossNumber(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape(r"one.gif")
        self.penup()
        self.speed(0)

class Player(turtle.Turtle):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Player, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape(r"player_right.gif")  
        self.penup()  
        self.speed(0)  
        self.key = False 
        self.cross = False 
        self.cross_count = 0

    def go_up(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor() + 24

        if (move_to_x, move_to_y) not in walls and (move_to_x, move_to_y) not in doors_locations \
                and (move_to_x, move_to_y) not in crosses_location:
            self.goto(move_to_x, move_to_y)

    def go_down(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor() - 24

        if (move_to_x, move_to_y) not in walls and (move_to_x, move_to_y) not in doors_locations\
                and (move_to_x, move_to_y) not in crosses_location:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        move_to_x = self.xcor() - 24
        move_to_y = self.ycor()
        self.shape(r"player_left.gif")
        if (move_to_x, move_to_y) not in walls and (move_to_x, move_to_y) not in doors_locations \
                and (move_to_x, move_to_y) not in crosses_location:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        move_to_x = self.xcor() + 24
        move_to_y = self.ycor()
        self.shape(r"player_right.gif")
        if (move_to_x, move_to_y) not in walls and (move_to_x, move_to_y) not in doors_locations \
                and (move_to_x, move_to_y) not in crosses_location:
            self.goto(move_to_x, move_to_y)

    def is_collision(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 26:
            return True
        else:
            return False

class Enemy(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape(r"enemy_left.gif")
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.direction = random.choice(["down", "up", "left", "right"])

    def move(self):
        if self.direction == "up":
            dx = 0
            dy = 24
        elif self.direction == "down":
            dx = 0
            dy = -24
        elif self.direction == "left":
            dx = -24
            dy = 0
            self.shape(r"enemy_left.gif")
        elif self.direction == "right":
            dx = 24
            dy = 0
            self.shape(r"enemy_right.gif")
        else:
            dx = 0
            dy = 0
        if self.is_close(player):
            if player.xcor() < self.xcor():
                self.direction = "left"
            elif player.xcor() > self.xcor():
                self.direction = "right"
            elif player.ycor() < self.ycor():
                self.direction = "down"
            elif player.ycor() > self.ycor():
                self.direction = "up"

        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        if (move_to_x, move_to_y) not in walls and (move_to_x, move_to_y) not in doors_locations \
                and (move_to_x, move_to_y) not in crosses_location:
            self.goto(move_to_x, move_to_y)
        else:
            self.direction = random.choice(["down", "up", "left", "right"])

        turtle.ontimer(self.move, t=random.randint(100, 300))

    def is_close(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 100:
            return True
        else:
            return False

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

class mainCross(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape(r"cros.gif")
        self.penup()
        self.speed(0)
        self.cross = True
        self.goto(x, y)
    
    def destroy(self):
        self.goto(3000, 3000)
        self.hideturtle()


class GameEnd(turtle.Turtle):

    __meta__ = ABCMeta
    @abstractmethod
    def __init__(self):
        pass

class GameOver(GameEnd):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)


class GameWin(GameEnd):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape(r"exit.gif")
        self.penup()
        self.speed(0)
        self.goto(x, y)

if __name__ == '__main__':
    levels = [""]
    current_level = 1

    walls = []
    doors = []
    doors_locations = []

    pen = Pen()

    key_notif = Key_Notif()
    keys = []
    keys_locations = []
    cross = cross()
    cross_number = crossNumber()
    crosses = []
    crosses_location = []

    player = Player()
    enemies = []
    start_point = []
    hearts = []
    hearts_x_cor = []

    game_win = GameWin(3000, 3000)
    game_over = GameOver()

    for y_H in range(len(level_1)):
        for x_H in range(len(level_1[y_H])):
            character_H = level_1[y_H][x_H]
            screen_x_H = -288 + (x_H * 24)
            screen_y_H = 288 - (y_H * 24)
            if character_H == "H":
                hearts_x_cor.append(screen_x_H)
                hearts.append(Health(screen_x_H, screen_y_H))

    def setup_maze(level: list) -> None:
        game_over.goto(2000, 2000)
        for y in range(len(level)):
            for x in range(len(level[y])):
                character = level[y][x]
                screen_x = -288 + (x * 24)
                screen_y = 288 - (y * 24)
                if character == "X":
                    pen.goto(screen_x, screen_y)
                    pen.stamp()
                    walls.append((screen_x, screen_y))
                if character == "D":
                    doors.append(Door(screen_x, screen_y))
                    doors_locations.append((screen_x, screen_y))
                if character == "L":
                    key_notif.goto(screen_x, screen_y)
                    key_notif.hideturtle()
                if character == "A":
                    cross.goto(screen_x, screen_y)
                    cross.hideturtle()
                if character == "K":
                    keys.append(Key(screen_x, screen_y))
                    keys_locations.append((screen_x, screen_y))
                if character == "Q":
                    cross_number.goto(screen_x, screen_y)
                    cross_number.hideturtle()
                if character == "P":
                    player.goto(screen_x, screen_y)
                    start_point.append([screen_x, screen_y])
                if character == "E":
                    enemies.append(Enemy(screen_x, screen_y))
                if character == "F":
                    crosses.append(mainCross(screen_x, screen_y))
                    crosses_location.append((screen_x, screen_y))
                if character == "W":
                    global game_win
                    game_win = GameWin(screen_x, screen_y)
                if character == "G":
                    game_over.goto(screen_x, screen_y)
                    game_over.stamp()


    levels.append(level_1)

    window.bgpic(r"background.gif")

    setup_maze(levels[1])

    turtle.listen()
    turtle.onkeypress(player.go_left, "Left")
    turtle.onkeypress(player.go_right, "Right")
    turtle.onkeypress(player.go_down, "Down")
    turtle.onkeypress(player.go_up, "Up")
    turtle.onkeypress(end_game_function, "q")

    window.tracer(0)

    for enemy in enemies:
        turtle.ontimer(enemy.move, t=250)


    while True:
        if end_game: 
            break

        if player.key:
            key_notif.showturtle()
        else:
            key_notif.hideturtle()

        if player.cross_count:
            cross.showturtle()
            cross_number.showturtle()
        else:
            cross.hideturtle()
            cross_number.hideturtle()

        if player.cross_count == 1:
            cross_number.shape(r"one.gif")
        elif player.cross_count == 2:
            cross_number.shape(r"two.gif")
        elif player.cross_count == 3:
            cross_number.shape(r"three.gif")
        else:
            cross_number.hideturtle()

        if player.is_collision(game_win):
            player.goto(2000, 2000)
            window.update()
            time.sleep(1)
            window.clear()
            window.bgpic(r"winner.gif")
            turtle.listen()
            turtle.onkeypress(end_game_function, "q")

        for door in doors:
            if player.is_collision(door) and player.key is True:
                x_coord = door.xcor()
                y_coord = door.ycor()
                door.destroy()
                doors.remove(door)
                doors_locations.remove((x_coord, y_coord))
                player.key = False


        for cros in crosses:
            if player.is_collision(cros):
                x_coord = cros.xcor()
                y_coord = cros.ycor()
                player.cross = True
                if player.cross_count < 5:
                    player.cross_count += 1
                cros.cross = False
                cros.destroy()
                crosses.remove(cros)
        
        for key in keys:
            if player.is_collision(key):
                x_coord = key.xcor()
                y_coord = key.ycor()
                player.key = True
                key.key = False 
                key.destroy()
                keys.remove(key)

        for enemy in enemies:
            if player.is_collision(enemy):
                if player.cross_count:
                    enemy.destroy()
                    enemies.remove(enemy)
                    player.cross_count -= 1  
                    continue
                for heart in hearts:
                    if heart.xcor() == max(hearts_x_cor):
                        black_square = BlackSquare()
                        black_square.goto(heart.xcor(), heart.ycor())
                        black_square.stamp()
                        heart.destroy()
                        hearts.remove(heart)
                        hearts_x_cor.remove(max(hearts_x_cor))
                        player.goto(start_point[0][0], start_point[0][1])
                if not len(hearts):
                    player.goto(2000, 2000)
                    window.clear()
                    window.bgpic(r"loser.gif")
                    window.title("Trail of Terror")
                    window.setup(700, 700)
                    turtle.listen()
                    turtle.onkeypress(player.go_left, "Left")
                    turtle.onkeypress(player.go_right, "Right")
                    turtle.onkeypress(player.go_down, "Down")
                    turtle.onkeypress(player.go_up, "Up")
                    turtle.onkeypress(end_game_function, "q")
                    

        window.update()
    window.bye()
