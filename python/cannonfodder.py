import sys

sys.path.insert(0, "./")

import engine.play as pl 
import engine.actor as act
import engine.ui as ui 
import engine.utility as ut
import engine.physics as phys
import random
from pygame import time
from pygame.locals import *

#generates a random position
def random_pos():

   #ranges selected to help match demo as much as possible
   randomX = random.randrange(10, 600)  
   randomY = random.randrange(10, 650)  
   return (randomX, randomY)

#generates a random color
def random_color():
   randomRed = random.randrange(50, 255)
   randomGreen = random.randrange(50, 255)
   randomBlue = random.randrange(50, 255)
   return(randomRed, randomGreen, randomBlue)

#creates the amount of circles indicated by "nb"
def get_circles(nb):
   circles = []
   radius = 10
   for i in range(0, nb):
      circle_bounds = random_pos()
      circle_color = random_color()
      circle = act.make_circ(circle_bounds[0], circle_bounds[1], radius, circle_color[0], circle_color[1], circle_color[2])
      circle.name = "circle " + str(i)
      circle.verbose = True
      circle.insert_action(act.make_draw_circ())
      circles.append(circle)
   return circles

#Creating each of the colliders
pillarOne_collider = phys.make_rectangle_collider([715,0], [795, 250])
collisions2 = phys.make_outside_rectangle_collision()
pillarOne_collider.insert_action(collisions2)

pillarTwo_collider = phys.make_rectangle_collider([715,250], [795, 330])
collisions3 = phys.make_outside_rectangle_collision()
pillarTwo_collider.insert_action(collisions3)

pillarThree_collider = phys.make_rectangle_collider([715,325] , [795,730])
collisions4 = phys.make_outside_rectangle_collision()
pillarThree_collider.insert_action(collisions4)

rectangleOne_collider = phys.make_rectangle_collider([985, 520] , [1170, 540])
collisions5 = phys.make_outside_rectangle_collision()
rectangleOne_collider.insert_action(collisions5)

rectangleTwo_collider = phys.make_rectangle_collider([890, 620] , [1070, 640])
collisions6 = phys.make_outside_rectangle_collision()
rectangleTwo_collider.insert_action(collisions6)

#making of the is_inside_action()s
insideAction_right = act.make_is_inside_action()
insideAction_left = act.make_is_inside_action()

#making of the activate and deactivate actions (physics engine version):
phys_activate = phys.make_activate_action()
phys_deactivate = phys.make_deactivate_action()

#appending (physics) deactivate to the 2 inside_action()s children
insideAction_right.children.append(phys_deactivate)
insideAction_left.children.append(phys_deactivate)

def get_particles(init_data):
   import engine.physics as phys
   particles = []

   parts = phys.make_particles()
   particles.append(parts)

   #appending physics activate and deactivate to the particles children
   parts.insert_action(phys_deactivate)
   parts.insert_action(phys_activate)

   for d in init_data:
      position = list(d.position)
      velocity = [(2.0 * random.random() + 15), (2.0 * random.random() - 4.75)] 
      mass = 1.0
      parts.add_particle(position, velocity, mass)

   #force. In this case, simple gravity
   gravity = phys.make_gravity_force()
   gravity.gravity = [0.0, 0.0002] 
   grav_action = phys.make_gravity_action()
   gravity.insert_action(grav_action)

   grav_action.children.append(insideAction_right)
   grav_action.children.append(phys_activate)

   #drag force
   drag = phys.make_drag_force()
   drag.drag_constant = 0.009 
   drag_action = phys.make_drag_action()
   drag.insert_action(drag_action)

   drag_action.children.append(insideAction_left)
   drag_action.children.append(phys_activate)

   #spring force
   spring = phys.make_spring_force()
   spring_action = phys.make_spring_action()
   spring.insert_action(spring_action)

   spring_action.children.append(insideAction_right)
   spring_action.children.append(phys_activate)

   #position solver
   psolve = phys.make_position_solve_action()
   parts.insert_action(psolve)

   #velocity solver
   vsolve = phys.make_velocity_solve()
   parts.insert_action(vsolve)
   
   #appending the forces to vsolve
   vsolve.children.append(spring_action)
   vsolve.children.append(grav_action)

   #drag action works, but due to an appending issue (or something else)
   #it is causing things to not work whenever this line isn't commented out
   #vsolve.children.append(drag_action)
   
   #euler solver
   esolve = phys.make_euler_solve_action()
   esolve.dt = 0.1
   parts.insert_action(esolve)
   esolve.children.append(psolve)
   esolve.children.append(vsolve)
   esolve.types.append("loop")
   
   #connect particle positions to circle positions
   for i in range(0, len(init_data)):
      pick = phys.make_pick_position_action(i)
      put = act.make_put_position_action()

      parts.insert_action(pick)
      init_data[i].insert_action(put)
      pick.children.append(put)

      esolve.children.append(pick)
   
   #collisions with the window frame
   window_frame_collider = phys.make_rectangle_collider([0,0], [screenX, screenY])
   collisions = phys.make_inside_rectangle_collision()
   window_frame_collider.insert_action(collisions)
   psolve.children.append(collisions)

   #appending colliders for the 3 rectangles that divide right and left side
   #to psolve
   psolve.children.append(collisions2)
   psolve.children.append(collisions3)
   psolve.children.append(collisions4)

   #appending colliders for the two rectangles on the right side to psolve
   psolve.children.append(collisions5)
   psolve.children.append(collisions6)

   return particles

################## Viewer ############################################# 

#the x and y dimensions of the screen
screenX = 1280
screenY = 720

#creates the frame and adds all the necessary actions to it (screen updater, game/frame closer, resizer)
display = pl.make_screen_display_action()
resizer = pl.make_screen_resize_action()
viewer = pl.make_frame_viewer(screenX, screenY)
viewer.set_title("cannonfodder")
viewer.insert_action(pl.make_terminate_action())
viewer.insert_action(display)
viewer.insert_action(resizer)
game_content = [viewer]

#creates a rectangle that is used to help with appyling certain forces
#on the particles that make it to the right side of the screen
right_side_rectangle = act.make_rect(795,0, 485, 720, 0, 0, 0)
right_side_rectangle.insert_action(act.make_draw_rect())
right_side_rectangle.insert_action(insideAction_right)
right_side_rectangle.verbose = True
right_side_rectangle.active = True
display.insert_entity(right_side_rectangle)
game_content.append(right_side_rectangle)

#creates a rectangle that is used to help with applying certain forces
#on the particles that are on the left side of the screen
left_side_rectangle = act.make_rect(0,0, 795, 720, 0, 0, 0) #change 4th back to 730 if they collect in the bottom left corner again
left_side_rectangle.insert_action(act.make_draw_rect())
left_side_rectangle.insert_action(insideAction_left)
left_side_rectangle.verbose = True
left_side_rectangle.active = True
display.insert_entity(left_side_rectangle)
game_content.append(left_side_rectangle)

#creates the circles
circs = get_circles(100)

#creates particles for every circle that was created, adds the necessary forces,
#and connects the circles to each of the particles
particles = get_particles(circs)

#adds the circles and particles to the game content
game_content = game_content + circs + particles

#makes each of the circles visible
for b in circs:
   display.insert_entity(b)

#creating rectangle column that divides the left and right sides of the frame/screen (pillarsOne-pillarThree)
pillarOne = act.make_rect(725,0, 70, 250, 255, 255, 255)
pillarOne.insert_action(act.make_draw_rect())
pillarOne.verbose = True
display.insert_entity(pillarOne)
game_content.append(pillarOne)

pillarTwo = act.make_rect(725,250, 70, 75, 255, 255, 255)
pillarTwo.insert_action(act.make_draw_rect())
pillarTwo.verbose = True

#initally sets the rectangles active to false so that, the particles may pass through
pillarTwo.active = False
pillarTwo_collider.active = False
display.insert_entity(pillarTwo)
game_content.append(pillarTwo)

### Timer ###
rectangle_timer = ut.make_timer(9000, 0, 0, 0)
timer_action = ut.start_timer_action()
update_timer = ut.update_timer_action()
activate_action = ut.activate_action()
deactivate_action = ut.deactivate_action()
 
rectangle_timer.insert_action(timer_action)
rectangle_timer.insert_action(update_timer)

game_content.append(rectangle_timer)                     

#resets timer if the alarm goes off
timer_alarm = ut.alarm_action(rectangle_timer.alotted_time)
rectangle_timer.insert_action(timer_alarm) 

#add all the child actions the alarm needs to work correctly 
timer_alarm.children.append(timer_action)
timer_alarm.children.append(activate_action)

#makes sure that the rectangle reactivates after the alarm goes off
pillarTwo.insert_action(activate_action)
pillarTwo.insert_action(deactivate_action)

### Collision3 Timer ###

# Timer is designed to activate the collisions of the middle rectangle
#in the pillar once it appears again
collision3_timer = ut.make_timer(9000, 0, 0, 0)
collision_timer_action = ut.start_timer_action()
collision_update_timer = ut.update_timer_action()
collision_activate_action = ut.activate_action()
collision_deactivate_action = ut.deactivate_action()
 
collision3_timer.insert_action(collision_timer_action)
collision3_timer.insert_action(collision_update_timer)

game_content.append(collision3_timer)                     

#resets timer if the alarm goes off
collision_timer_alarm = ut.alarm_action(collision3_timer.alotted_time)
collision3_timer.insert_action(collision_timer_alarm) 

#add all the child actions the alarm needs to work correctly 
collision_timer_alarm.children.append(collision_timer_action)
collision_timer_alarm.children.append(collision_activate_action)
pillarTwo_collider.insert_action(collision_activate_action)
pillarTwo_collider.insert_action(collision_deactivate_action)

pillarThree = act.make_rect(725,325, 70, 395, 255, 255, 255)
pillarThree.insert_action(act.make_draw_rect())
pillarThree.verbose = True
display.insert_entity(pillarThree)
game_content.append(pillarThree)

#right side of screen rectangles
rectangleOne = act.make_rect(985, 520, 185, 20, 255, 255, 255)
rectangleOne.insert_action(act.make_draw_rect())
rectangleOne.verbose = True
display.insert_entity(rectangleOne)
game_content.append(rectangleOne)

rectangleTwo = act.make_rect(890, 620, 185, 20, 255, 255, 255)
rectangleTwo.insert_action(act.make_draw_rect())
rectangleTwo.verbose = True
display.insert_entity(rectangleTwo)
game_content.append(rectangleTwo)

################## Looper ############################################# 
game_looper = pl.make_game_looper(game_content)
game_looper.verbose = False
game_looper.loop()