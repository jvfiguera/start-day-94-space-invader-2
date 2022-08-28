from turtle import Screen
from spaceinvader import Spaceinvaders

SpaceInvader    = Spaceinvaders()
screen          = Screen()
screen.listen()

SpaceInvader.mth_deploying_invaders()
SpaceInvader.mth_deploy_barrier()
SpaceInvader.mth_deploy_space_nave()
screen.onkey(SpaceInvader.mth_move_space_nave_left, 'Left')
screen.onkey(SpaceInvader.mth_move_space_nave_right, 'Right')
screen.onkey(SpaceInvader.mth_move_space_nave_up, 'Up')
screen.onkey(SpaceInvader.mth_move_space_nave_down, 'Down')

if not SpaceInvader.bullet:
    screen.onkey(SpaceInvader.mth_shoot_bullets, 'space')

while not SpaceInvader.game_is_over :
    SpaceInvader.mth_shoot_invaders()
    if SpaceInvader.invader_move == 'left':
       SpaceInvader.mth_mov_invaders_left()
    else :
        SpaceInvader.mth_mov_invaders_right()


screen.mainloop()
#screen.exitonclick()