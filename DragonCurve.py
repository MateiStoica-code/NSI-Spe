from audioop import reverse
from turtle import *

t = Turtle()
s = getscreen()
old = ['r']
new = old

nb_i = int(input("How many iterations do you wish to have ? (Please input a positive, non-zero integer)"))
length = int(input("How long (in pixels) do you wish your lines to be ? (50px recommended for a number of iterations under 10 ; 10px or lower for higher iterations) (Please input a positive, non-zero integer) "))
b_color, p_color = input("What colour do you wish your curve to be ? (No capitalisation)"), input("What colour do you wish your background to be ? (No capitalisation)")


def draw(elt) :
    if elt == "l" :
        t.lt(90)
        t.fd(length)
    elif elt == 'r' :
        t.rt(90)
        t.fd(length)

def reverse_and_flip(table):
    for item in table:
        if item == 'r':
            item = 'l'
        elif item == 'l':
            item = 'r'
        
