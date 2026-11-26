import flet as ft
import asyncio

async def main(page: ft.Page):
    ages = ("baby", "teen", "adult")
    current_age = ages[0]
    page.title = "BleBot"
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
    experience = bar("Experience", 0)

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

    def gain_exp():
        print("Gaining exp")
        if current_age == ages[0]:
            if hunger.bar.value > 0.8 and emotions.bar.value > 0.8:
                experience.bar.value = min(experience.bar.value + 0.1, 1)
                print(f"Experience: {experience.bar.value}")
                page.update()

    def level_up():
        nonlocal current_age
        if experience.bar.value >= 1:
            print("Blebot leveled up")
            if current_age == ages[0]:
                current_age = ages[1]
                age_teen()
            elif current_age == ages[1]:
                age_adult()
                current_age = 2
            experience.bar.value = 0

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
        blebot,
        ft.Text(hunger.label),
        hunger.bar,
        ft.Button("Feed", on_click=feed),
        ft.Text(emotions.label),
        emotions.bar,
        ft.Button("Pet", on_click=pet),
        experience.bar
        )
    if current_age == ages[0]:
        age_baby()
    if current_age == ages[1]:
        age_teen()
    if current_age == ages[2]:
        age_adult()
    while True:
        await asyncio.sleep(2)
        hunger.bar.value = max(hunger.bar.value - 0.02, 0)
        emotions.bar.value = max(emotions.bar.value - 0.01, 0)
        gain_exp()
        level_up()
        page.update()
ft.run(main, assets_dir="imgs")