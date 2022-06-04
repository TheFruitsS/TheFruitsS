import Turtle3D
import math

n = Turtle3D.Turtle()
n.color('silver')
n.speed(10000)
n.shape('turtle')

for i in range(2000):
    n.forward(100)
    n.left(math.sin(i - 10) * 10)
    n.right(25)

n.end_fill()
Turtle3D.done()
