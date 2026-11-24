import flet as ft 
import asyncio

async def main(page: ft.Page):
    page.window.frameless = True
    page.window.always_on_top = True
    page.window.bgcolor = ft.Colors.TRANSPARENT
    page.bgcolor = ft.Colors.TRANSPARENT
    page.padding = 0
    page.window.width = 200
    page.window.height = 200

    page.add(ft.Image(src="BleBotFrame1.png"))

ft.run(main,assets_dir="imgs")