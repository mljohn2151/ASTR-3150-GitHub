from math import pi
from random import randint

def setup():
    global sphere_size
    size(500,500,P3D)
    sphere_size = randint(100,200)
    
def draw():
    global sphere_size
    background(0)
    translate(width/2,height/2,0)
    rotateY(float(frameCount)/200)
    fill(255,0,0)
    stroke(255)
    sphere(sphere_size)
    
    
