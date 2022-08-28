import random
import turtle
from turtle import Turtle, Screen
import _tkinter
from time import sleep

# CONSTANTS
#SNOW_BALL_SIZE_LIST =[0.01,0.1,0.2,0.3]
INVADERS_POS_XY_DIC ={'invader1':[(-175,250),(-125,250),(-75,250),(-25,250),(25,250),(75,250),(125,250),(175,250)]
                      ,'invader2':[(-175,200),(-125,200),(-75,200),(-25,200),(25,200),(75,200),(125,200),(175,200)]
                      ,'invader3':[(-175,150),(-125,150),(-75,150),(-25,150),(25,150),(75,150),(125,150),(175,150)]
                    }
#SPEED_INVADER_LIST  =[5,10,15,20]
#SPEED_INVADER_LIST  =[2,4,6,8]
SPEED_INVADER_LIST  =[10,15,20,25]
BARRIER_BRICK_POS   =[(-270,-30),(-220,-10),(-150,-30),(-60,-10),(10,-30),(70,-10),(120,-30),(180,-10),(270,-30)]
BARRIER_BRICK_SIZE  =[(0.25,1),(0.25,2),(0.25,3),(0.25,4),(0.25,2),(0.25,3), (0.25,1),(0.25,4),(0.25,1)]
SPEED_NAVE          =6
SPEED_NAVE_SHOOT    =5
SPEED_INVADER_BULLET =2

class Spaceinvaders(Turtle) :
    def __init__(self):
        super().__init__()
        # Parameters Windows
        self.windows        =''
        self.window_title   ='Space Invaders'
        self.window_width   =600
        self.window_height  =600
        # Invader parameters
        self.invader        =''
        self.invader_who_shoot = ''
        self.bullet_invader = ''
        self.invader_shape  =''
        self.invader1_img   = 'images/invader11.gif'
        self.invader2_img   = 'images/invader22.gif'
        self.invader3_img   = 'images/invader33.gif'
        self.invader_move   = 'left'
        self.speed_invader  = 0
        self.INVADER_OBJ_DICT ={}
        turtle.addshape(self.invader1_img)
        turtle.addshape(self.invader2_img)
        turtle.addshape(self.invader3_img)
        # Barrier parameters
        self.barrier_brick= ''
        self.barrier_shape  ='square'
        self.brick_color ='#FCF9C6'  #'#243A73'
        self.BARRIER_OBJ_LIST   =[]
        # Space nave parameters
        self.space_nave =''
        self.space_nave_img = 'images/player-1.gif'
        turtle.addshape(self.space_nave_img)
        # Shoots Bullets Parameters
        self.bullet = ''
        self.bullet_shape = 'square'
        self.bullet_color = '#FAC213'
        # Game is over parameter
        self.game_is_over = False
        self.game_msg_turtle=''
        # Collision parameters
        self.shoot_barrier_collision =False
        # Score and Life Parameters
        self.score_player       =0
        self.life_player        =0
        self.life_player_score  =3
        # Ejecutar metodos
        self.mth_setup_screen()

    def mth_setup_screen(self):
        self.windows =Screen()
        self.windows.setup(width=self.window_width,height=self.window_height)
        self.windows.title(titlestring=self.window_title)
        self.windows.bgpic(picname='images/space_img.gif')
        self.mth_show_score_player()
        self.mth_show_life_player()
        self.windows.update()
        self.windows.tracer(1)

    def mth_deploy_barrier(self):
        idx_cnt =0
        for bar_pos in BARRIER_BRICK_POS:
            self.barrier_brick = Turtle()
            self.barrier_brick.hideturtle()
            self.barrier_brick.shape(name=self.barrier_shape)
            self.barrier_brick.shapesize(stretch_wid=BARRIER_BRICK_SIZE[idx_cnt][0], stretch_len=BARRIER_BRICK_SIZE[idx_cnt][1])
            self.barrier_brick.penup()
            self.barrier_brick.color(self.brick_color)
            self.barrier_brick.goto(x=bar_pos[0], y=bar_pos[1])
            self.barrier_brick.showturtle()
            self.BARRIER_OBJ_LIST.append(self.barrier_brick)
            idx_cnt +=1

    def mth_deploying_invaders(self):
        INVADER_OBJ_LIST_TEMP =[]
        self.windows.tracer(2)
        for invader_key in INVADERS_POS_XY_DIC:
            for xy_pos in INVADERS_POS_XY_DIC[invader_key]:
                self.invader = Turtle()
                self.invader.hideturtle()
                if invader_key == 'invader1':
                    self.invader_shape =self.invader1_img
                elif invader_key == 'invader2':
                    self.invader_shape =self.invader2_img
                else:
                    self.invader_shape  =self.invader3_img

                self.invader.shape(name=self.invader_shape)
                self.invader.penup()
                self.invader.goto(x=xy_pos[0], y=xy_pos[1])
                self.invader.showturtle()
                INVADER_OBJ_LIST_TEMP.append(self.invader)
            self.INVADER_OBJ_DICT[invader_key] = INVADER_OBJ_LIST_TEMP[0:8]
            INVADER_OBJ_LIST_TEMP.clear()

    def mth_mov_invaders_left(self) :
        self.speed_invader = random.choice(SPEED_INVADER_LIST)
        for invader_key in self.INVADER_OBJ_DICT:
            for idx_inv in range(len(self.INVADER_OBJ_DICT[invader_key])):
                try:
                    self.invader = self.INVADER_OBJ_DICT[invader_key][idx_inv]
                    # self.invader.goto(x=self.invader.xcor() - self.speed_invader, y=self.invader.ycor())
                    self.invader.setx(x=self.invader.xcor() - self.speed_invader)
                except IndexError:
                    pass
            try:
                if self.invader_move =='left' and self.INVADER_OBJ_DICT[invader_key][0].xcor() <= -self.window_width // 2 + 30:
                    self.invader_move ='right'
            except IndexError:
                pass

    def mth_mov_invaders_right(self) :
        self.speed_invader = random.choice(SPEED_INVADER_LIST)
        for invader_key in self.INVADER_OBJ_DICT:
            for idx_inv in range(len(self.INVADER_OBJ_DICT[invader_key])):
                try :
                    self.invader = self.INVADER_OBJ_DICT[invader_key][idx_inv]
                    # self.invader.goto(x=self.invader.xcor() + self.speed_invader, y=self.invader.ycor())
                    self.invader.setx(x=self.invader.xcor() + self.speed_invader)
                except IndexError:
                    pass
            max_num_inv = len(self.INVADER_OBJ_DICT[invader_key]) - 1
            try:
                if self.invader_move == 'right' and self.INVADER_OBJ_DICT[invader_key][max_num_inv].xcor() >= self.window_width // 2 - 30:
                    self.invader_move ='left'
            except IndexError:
                pass

    def mth_deploy_space_nave(self):
        self.space_nave = Turtle()
        self.space_nave.hideturtle()
        self.space_nave.shape(name=self.space_nave_img)
        self.space_nave.penup()
        self.space_nave.goto(x=0, y=-250)
        self.space_nave.showturtle()

    def mth_move_space_nave_left(self):
        if self.space_nave.xcor() > -280 :
            self.space_nave.goto(x= self.space_nave.xcor() - SPEED_NAVE, y=self.space_nave.ycor()) #-250

    def mth_move_space_nave_right(self):
        if self.space_nave.xcor() < 270 :
            self.space_nave.goto(x= self.space_nave.xcor() + SPEED_NAVE, y=self.space_nave.ycor()) # -250

    def mth_move_space_nave_up(self):
        if self.space_nave.ycor() < -100 :
            self.space_nave.goto(x= self.space_nave.xcor(), y= self.space_nave.ycor() + SPEED_NAVE)

    def mth_move_space_nave_down(self):
        if self.space_nave.ycor() > -250 :
            self.space_nave.goto(x= self.space_nave.xcor(), y= self.space_nave.ycor() - SPEED_NAVE)

    def mth_shoot_bullets(self):
        self.shoot_barrier_collision =False
        self.windows.onkey(None, 'space')
        self.bullet = Turtle()
        self.bullet.hideturtle()
        self.bullet.shape(name=self.bullet_shape)
        self.bullet.shapesize(stretch_wid=0.25,stretch_len=0.10)
        self.bullet.penup()
        self.bullet.color(self.bullet_color)
        self.bullet.goto(x=self.space_nave.xcor(), y=self.space_nave.ycor())
        self.bullet.showturtle()

        while abs(self.bullet.ycor()) <= 290 and not self.shoot_barrier_collision :
            self.bullet.goto(x=self.bullet.xcor(), y=self.bullet.ycor() + SPEED_NAVE_SHOOT)
            self.mth_detect_shoot_barrier_collision()
            if not self.shoot_barrier_collision:
                self.mth_detect_shoot_invaders_collision()
        self.mth_show_score_player()
        self.bullet.reset() # Reset the shoot
        self.windows.onkey(self.mth_shoot_bullets, 'space')

    def mth_detect_shoot_barrier_collision(self):
        for self.barrier_brick in self.BARRIER_OBJ_LIST:
            if self.bullet.distance(self.barrier_brick) >=0 and self.bullet.distance(self.barrier_brick) <= 30:
                self.barrier_brick.reset()  # Reset the barrier
                self.BARRIER_OBJ_LIST.remove(self.barrier_brick)
                self.score_player   +=2
                self.shoot_barrier_collision = True

    def mth_detect_shoot_invaders_collision(self):
         for invader_key in self.INVADER_OBJ_DICT:
             for invader in self.INVADER_OBJ_DICT[invader_key]:
                 if self.bullet.distance(invader) >= 0 and self.bullet.distance(invader) <= 10:
                     invader.hideturtle()   #Reset the barrier
                     invader.clear()
                     self.INVADER_OBJ_DICT[invader_key].remove(invader)
                     self.score_player += 10
                     self.shoot_barrier_collision = True

         if len(self.INVADER_OBJ_DICT) == 0:
            self.mth_show_msg_game(pMsg='THE GAME IS OVER, YOU WON',pSize=40)
            self.game_is_over = True

    def mth_show_score_player(self) :
        self.clear()
        self.hideturtle()
        self.goto(200, 270)
        self.penup()
        self.color('#9EB23B')
        self.write(f'Score: {self.score_player}', align="center", font=("Courier", 15, "bold"))

    def mth_show_life_player(self) :
        self.life_player = Turtle()
        self.life_player.hideturtle()
        self.life_player.goto(-200, 270)
        self.life_player.penup()
        self.life_player.color('#9EB23B')
        self.life_player.write(f'Life Player: {self.life_player_score}', align="center", font=("Courier", 15, "bold"))

    def mth_show_msg_game(self, pMsg,pSize) :
        self.game_msg_turtle = Turtle()
        self.game_msg_turtle.clear()
        self.game_msg_turtle.hideturtle()
        self.game_msg_turtle.goto(0, 0)
        self.game_msg_turtle.penup()
        self.game_msg_turtle.color('#9EB23B')
        self.game_msg_turtle.write(f'{pMsg}', align="center", font=("Courier", pSize, "bold"))

    def mth_shoot_invaders(self):
        for invader_key in self.INVADER_OBJ_DICT :
            self.invader_who_shoot= random.choice(self.INVADER_OBJ_DICT[invader_key])
            self.bullet_invader = Turtle()
            self.bullet_invader.hideturtle()
            self.bullet_invader.shape(name=self.bullet_shape)
            self.bullet_invader.shapesize(stretch_wid=0.25,stretch_len=0.10)
            self.bullet_invader.penup()
            self.bullet_invader.color(self.bullet_color)
            invader_pos_y =self.invader_who_shoot.ycor()
            self.bullet_invader.goto(x=self.invader_who_shoot.xcor(),y=invader_pos_y)
            self.bullet_invader.showturtle()
            while self.bullet_invader.ycor() >= -235:
                invader_pos_y -= SPEED_NAVE_SHOOT
                self.bullet_invader.goto(x=self.invader_who_shoot.xcor(), y=invader_pos_y)
                if self.mth_detect_bullet_invader_nave_collision():
                    self.bullet_invader.hideturtle()
                    self.bullet_invader.clear()
                    self.space_nave.hideturtle()
                    self.space_nave.clear()
                    # self.mth_show_msg_game(pMsg='Your nave has been destroy',pSize=20)
                    if self.life_player_score >0 :
                        self.life_player_score -=1

                    self.life_player.reset()
                    self.mth_show_life_player()
                    # sleep(1)
                    # self.game_msg_turtle.reset()
                    if self.life_player_score <= 0:
                        self.windows.onkey(None, 'Left')
                        self.windows.onkey(None, 'Right')
                        self.windows.onkey(None, 'Up')
                        self.windows.onkey(None, 'Down')
                        self.windows.onkey(None, 'space')
                        self.mth_show_msg_game(pMsg='THE GAME IS OVER, YOU LOSE', pSize=20)
                        self.game_is_over = True
                    self.mth_deploy_space_nave()
            self.bullet_invader.reset()

    def mth_detect_bullet_invader_nave_collision(self):
        if self.bullet_invader.distance(self.space_nave) <= 25:
            return True
        else :
            return  False
