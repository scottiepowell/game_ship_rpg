# src/kivy_app/main.py
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class BridgeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        self.lbl = Label(text="You are on the Bridge of the ship.")
        btn = Button(text="Click me to test!")
        btn.bind(on_press=self.on_button)
        layout.add_widget(self.lbl)
        layout.add_widget(btn)
        self.add_widget(layout)

    def on_button(self, instance):
        self.lbl.text = "Button clicked — the ship acknowledges you!"

class ShipApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(BridgeScreen(name="bridge"))
        return sm

if __name__ == "__main__":
    print("Starting ShipApp…")       # console confirmation
    ShipApp().run()
    print("ShipApp ended.")