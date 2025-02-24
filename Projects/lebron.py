import codesters, random
from codesters import StageClass
stage = StageClass()
stage.disable_floor()

stage.set_background("cool_dog.png")

def falling_object():
    global object_speed, lives

    if lives > 0:
        x_position = random.randint(-250,250)
        object = codesters.Sprite("P.png")
        object.set_size(0.4)
        object.set_y_speed(object_speed)
        object_speed = 0.5

stage.event_interval(falling_object, 0.5)