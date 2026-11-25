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

    hunger_bar = ft.ProgressBar(value=0.5, width=200)

    def feed(e):
        hunger_bar.value = min(hunger_bar.value + 0.1, 1)
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
        ft.Button("Feed", on_click=feed)
    )

ft.run(main, assets_dir="imgs")