import flet as ft
import asyncio

async def main(page: ft.Page):
    page.title = "BleBot"
    page.window.min_width = 300
    page.window.max_width = 300
    page.window.min_height = 550
    page.window.max_height = 550
    page.window.maximized = False
    page.window.always_on_top = True
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    hunger_bar = ft.ProgressBar(value=0.5, width=200)
    emotion_bar = ft.ProgressBar(value=0.5, width=200)

    def feed(event):
        print(event)
        hunger_bar.value = min(hunger_bar.value + 0.1, 1)
        page.update()

    def pet(event):
        print(event)
        emotion_bar.value = min(emotion_bar.value + 0.1, 1)
        page.update()

    page.add(
        ft.Image(src="BleBotFrame1.png",
        width=250, 
        height=250,
        fit=ft.BoxFit.CONTAIN,
        filter_quality=ft.FilterQuality.NONE
        ),
        ft.Text("Hunger"),
        hunger_bar,
        ft.Button("Feed", on_click=feed),
        ft.Text("Emotions"),
        emotion_bar,
        ft.Button("Pet", on_click=pet)
    )

    while True:
        await asyncio.sleep(2)
        hunger_bar.value = max(hunger_bar.value - 0.02, 0)
        emotion_bar.value = max(emotion_bar.value - 0.01, 0)
        page.update()
ft.run(main, assets_dir="imgs")