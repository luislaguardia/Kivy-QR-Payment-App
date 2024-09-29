import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window


Window.size = (500, 700)  

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        profile_button = Button(text="Profile", size_hint=(1, 0.5))
        profile_button.bind(on_press=self.go_to_profile)
        layout.add_widget(profile_button)

        scan_button = Button(text="Scan", size_hint=(1, 0.5))
        scan_button.bind(on_press=self.go_to_scan)
        layout.add_widget(scan_button)

        self.add_widget(layout)

    def go_to_profile(self, instance):
        self.manager.current = 'profile'

    def go_to_scan(self, instance):
        self.manager.current = 'scan'


class ProfileScreen(Screen):
    def __init__(self, **kwargs):
        super(ProfileScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        profile_label = Label(text="This is the Profile Page", size_hint=(1, 0.8))
        layout.add_widget(profile_label)

        back_button = Button(text="Back to Home", size_hint=(1, 0.2))
        back_button.bind(on_press=self.go_back_home)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def go_back_home(self, instance):
        self.manager.current = 'home'

class ScanScreen(Screen):
    def __init__(self, **kwargs):
        super(ScanScreen, self).__init__(**kwargs)

        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        top_bar = AnchorLayout(anchor_x='right', anchor_y='top')

        done_button = Button(text="Done", size_hint=(0.2, 0.1))
        done_button.bind(on_press=self.go_back_home)
        top_bar.add_widget(done_button)

        main_layout.add_widget(top_bar)

        self.payment_status = Label(text="Scan the QR Code to Pay", size_hint=(1, 0.8))
        main_layout.add_widget(self.payment_status)

        scan_button = Button(text="Simulate QR Scan", size_hint=(1, 0.2))
        scan_button.bind(on_press=self.simulate_scan)
        main_layout.add_widget(scan_button)

        self.add_widget(main_layout)

    def simulate_scan(self, instance):
        self.payment_status.text = "Payment Successful"

    def go_back_home(self, instance):
        self.manager.current = 'home'

class QRPaymentApp(App):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(ProfileScreen(name='profile'))
        sm.add_widget(ScanScreen(name='scan'))

        return sm

if __name__ == '__main__':
    QRPaymentApp().run()
