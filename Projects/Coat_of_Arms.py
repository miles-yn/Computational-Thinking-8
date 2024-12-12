###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("static")


q1 = codesters.Square(100, 100, 200, 'blue')
q2 = codesters.Square(-100, 100, 200, 'yellow')
q3 = codesters.Square(-100, -100, 200, 'red')
q4 = codesters.Square(100,-100, 200, 'green')


s1 = codesters.Sprite("L", 100, 100)
s1.set_size (1.1)
s2 = codesters.Sprite("P", -100, -100)
s2.set_size(0.5)
s3 = codesters.Sprite("L", 100, -100)
s3.set_size(1.1)
s4 = codesters.Sprite("P", -100, 100)
s4.set_size(0.5)


message1 = codesters.Text("This is my king", -100, 100)
message2 = codesters.Text("Boy oh boy where do I even begin...",0,-220,"white")