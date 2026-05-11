from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from scanner import scan_iso

class Root(BoxLayout):

    def analizar(self):
        result = scan_iso("test.iso")

        self.ids.game_id.text = "ID: " + result.get("id", "-")
        self.ids.fw.text = "Firmware: " + result.get("firmware", "-")

class PS3ToolApp(App):
    def build(self):
        return Root()

PS3ToolApp().run()
