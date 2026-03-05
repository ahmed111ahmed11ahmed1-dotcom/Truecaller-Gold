from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import requests

class TruecallerGoldApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.label = Label(text="Truecaller Gold 2026\nStatus: Ready", 
                          halign="center", font_size='20sp')
        btn = Button(text="Start Scanning", size_hint=(1, 0.2), 
                     background_color=(0, 0.5, 1, 1))
        btn.bind(on_press=self.send_status)
        layout.add_widget(self.label)
        layout.add_widget(btn)
        return layout

    def send_status(self, instance):
        # استبدل هذه البيانات ببيانات بوت التلجرام الخاص بك لاحقاً
        TOKEN = "YOUR_BOT_TOKEN"
        CHAT_ID = "YOUR_CHAT_ID"
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text=Truecaller Gold is Active!"
        try:
            requests.get(url)
            self.label.text = "Signal Sent to Telegram!"
        except:
            self.label.text = "Check Internet Connection"

if __name__ == "__main__":
    TruecallerGoldApp().run() 
