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

borderleft_x = 300
borderright_x = 800
base_x = borderleft_x 
base_y = 400
pet_speed = 0.05
direction = 1

dragging = False
drag_offset_x = 0
drag_offset_y = 0

bob_height = 2
bob_speed = 3

# def change_image():
#     global current
#     choices = [i for i in range(len(images)) if i != current]
#     current = random.choice(choices)
#     label.config(image=images[current])
#     window.after(random.randint(800, 3000), change_image)

def start_drag(event):
    global dragging, drag_offset_x, drag_offset_y
    dragging = True
    drag_offset_x = event.x_root - base_x
    drag_offset_y = event.y_root - base_y

def do_drag(event):
    global base_x, base_y
    base_x = event.x_root - drag_offset_x
    base_y = event.y_root - drag_offset_y

def stop_drag(event):
    global dragging
    dragging = False

label.bind('<Button-1>', start_drag)
label.bind('<B1-Motion>', do_drag)
label.bind('<ButtonRelease-1>', stop_drag)

def move():
    '''moves the pet from one side of the screen to the other, through changing direction depending on
    if pet is closest to right side or left side'''
    global base_x, direction
    if not dragging:
        base_x += pet_speed * direction
    if base_x >= borderright_x:
        direction = -1
    elif base_x <= borderleft_x:
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