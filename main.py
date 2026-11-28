import flet as ft
import math
import time
import asyncio

async def main(page: ft.Page):
    ages = ("BleBot-Baby", "BleBot-Teen", "BleBot-Adult")
    current_age = ages[0]
    sleeping = False
    def sleep(event):
        print("sleeping")
        nonlocal sleeping
        if sleeping == False:
            sleepbutton.content = "Stop Sleeping"
            hunger_button.disabled = True
            pet_button.disabled = True
            sleeping = True
        elif sleeping == True:
            sleepbutton.content = "Sleep"
            hunger_button.disabled = False
            pet_button.disabled = False
            sleeping = False
        page.update()
    currentageText = ft.Text(current_age)
    sleepbutton = ft.Button("Sleep", on_click=sleep)
    page.title = "BleBot"
    bob_height = 0.05
    bob_speed = 3
    hunger_multiplier = 1
    emotions_multiplier = 1
    page.window.min_width = 300
    page.window.max_width = 300
    page.window.min_height = 550
    page.window.max_height = 550
    page.window.maximized = False
    page.window.always_on_top = True
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    class bar:
        def __init__(self, name, value):
            self.label = name
            self.bar = ft.ProgressBar(value=value, width=200)

    hunger = bar("Hunger", 0.5)
    emotions = bar("Emotions", 0.5)
    energy = bar("Energy", 0.5)
    experience = bar("Experience", 0)

    async def bob():
        while True:
            offset_y = math.sin(time.time() * bob_speed) * bob_height
            blebot.offset = ft.Offset(0, offset_y)
            page.update()
            await asyncio.sleep(0.03)

    def feed(event):
        print(event)
        hunger.bar.value = min(hunger.bar.value + 0.1, 1)
        print(f"Hunger: {hunger.bar.value}")
        page.update()

    def pet(event):
        print(event)
        emotions.bar.value = min(emotions.bar.value + 0.1, 1)
        print(f"Emotions: {emotions.bar.value}")
        page.update()

    hunger_button = ft.Button("Feed", on_click=feed)
    pet_button = ft.Button("Pet", on_click=pet)

    def gain_exp():
        print("Gaining exp")
        if current_age != ages[2]:
            if current_age == ages[0] and hunger.bar.value > 0.8 and emotions.bar.value > 0.8:
                experience.bar.value = min(experience.bar.value + 0.05, 1)
                print(f"Experience: {experience.bar.value}")
                page.update()
            elif current_age == ages[1] and hunger.bar.value > 0.8 and emotions.bar.value > 0.8:
                experience.bar.value = min(experience.bar.value + 0.025, 1)
                print(f"Experience: {experience.bar.value}")
                page.update()

    def level_up():
        nonlocal current_age
        if experience.bar.value >= 0.95:
            print("Blebot leveled up")
            if current_age == ages[0]:
                current_age = ages[1]
                age_teen()
            elif current_age == ages[1]:
                age_adult()
                current_age = ages[2]
            experience.bar.value = 0
            currentageText.value = (current_age)

    def tiredness():
        nonlocal hunger_multiplier, emotions_multiplier
        if energy.bar.value <= 0.4:
            hunger_multiplier = 3
            emotions_multiplier = 3
        else:
            hunger_multiplier = 1
            emotions_multiplier = 1

    def age_baby():
        blebot.width = 100
        blebot.height = 100
    def age_teen():
        blebot.width = 180
        blebot.height = 180
    def age_adult():
        blebot.width = 250
        blebot.height = 250

    blebot = ft.Image(
            src="BleBotFrame1.png",
            width=250, 
            height=250,
            fit=ft.BoxFit.CONTAIN,
            filter_quality=ft.FilterQuality.NONE
        )
    page.add(
        currentageText,
        blebot,
        ft.Text(hunger.label),
        hunger.bar,
        hunger_button,
        ft.Text(emotions.label),
        emotions.bar,
        pet_button,
        ft.Text(energy.label),
        energy.bar,
        sleepbutton,
        experience.bar,
        ft.Text(experience.label)
        )
    if current_age == ages[0]:
        age_baby()
    if current_age == ages[1]:
        age_teen()
    if current_age == ages[2]:
        age_adult()
    while True:
        page.run_task(bob)
        await asyncio.sleep(2)
        hunger.bar.value = max(hunger.bar.value - (0.02 * hunger_multiplier), 0)
        emotions.bar.value = max(emotions.bar.value - (0.01 * emotions_multiplier), 0)
        gain_exp()
        level_up()
        page.update()
        tiredness()
        if sleeping:
            energy.bar.value = min(energy.bar.value + 0.02, 1)
        else:
            energy.bar.value = max(energy.bar.value - 0.005, 0)
ft.run(main, assets_dir="imgs")