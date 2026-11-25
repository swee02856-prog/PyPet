import flet as ft

def main(page: ft.Page):
    page.title = "BleBot"
    page.window.min_width = 300
    page.window.max_width = 300
    page.window.min_height = 450
    page.window.max_height = 450
    page.window.maximized = False
    page.window.always_on_top = True
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(
        ft.Image(src="BleBotFrame1.png",
        width=250, 
        height=250,
        fit=ft.BoxFit.CONTAIN,
        filter_quality=ft.FilterQuality.NONE
        ),
        ft.Text("Hunger"),
        ft.ProgressBar(value=0.5, width=200),
        ft.Text("Emotions"),
        ft.ProgressBar(value=0.5, width=200),
        ft.Text("Energy"),
        ft.ProgressBar(value=0.5, width=200)
    )

ft.run(main, assets_dir="imgs")