import tkinter as tk
import random
import math
import time

window = tk.Tk()
window.overrideredirect(True)
window.attributes('-topmost', True)
window.attributes('-alpha', '1.0')

label = tk.Label(window, bd=0, bg='black')
label.pack()

BleBotLeft1 = tk.PhotoImage(file='imgs/BleBotFrame1.png')

images = [BleBotLeft1]
current = 0
label.config(image=images[current])

left_x = 300
right_x = 800
base_x = left_x 
base_y = 400
pet_speed = 0.1
direction = 1

bob_height = 5
bob_speed = 3

# def change_image():
#     global current
#     choices = [i for i in range(len(images)) if i != current]
#     current = random.choice(choices)
#     label.config(image=images[current])
#     window.after(random.randint(800, 3000), change_image)

def move():
    '''moves the pet from one side of the screen to the other, through changing direction depending on
    if pet is closest to right side or left side'''
    global base_x, direction
    base_x += pet_speed * direction
    if base_x >= right_x:
        direction = -1
    elif base_x <= left_x:
        direction = 1
    window.after(16, move)

def bob():
    offset = math.sin(time.time() * bob_speed) * bob_height
    window.geometry(f"+{int(base_x)}+{int(base_y+offset)}")
    window.after(16, bob)
# change_image()
move()
bob()

window.mainloop()