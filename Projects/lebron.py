#Section 1 - Setup
import codesters, random
from codesters import StageClass
stage = StageClass()
stage.disable_floor()

object = codesters.Sprite("lehairline.png")
object.set_width(100)
object.set_height(100)
stage.set_background("legreatnessdriveway.png")

# Section 4 - Controls
def move_up(sprite):
	sprite.move_up(1)
   	 
def move_down(sprite):
	sprite.move_down(1)
    
def move_left(sprite):
	sprite.move_left(1)
    
def move_right(sprite):    
	sprite.move_right(1)
	
object.event_key("up", move_up)
object.event_key("down", move_down)
object.event_key("left", move_left)
object.event_key("right", move_right)