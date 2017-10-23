import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.anchorlayout import AnchorLayout

class InitializationScreen(Screen):
    pass

class SplashScreen(Screen):
    pass

class MenuScreen(Screen):
    pass

class SystemInfo(Screen):
    pass

class Parameters(Screen):
    pass

class ExecScreen(Screen):
    pass

Builder.load_string("""
<SplashScreen>:
    AnchorLayout:
        Button:
            on_press: root.manager.current = "main"
            size: self.width, self.height
            Image:
                source: 'sprout.png'
                y: self.parent.y
                x: self.parent.x
                size: 750, 550
                allow_stretch: True
        Label:
            text: 'Test'
            font_size: 55
            bold: 1
            color: [0,0.9,0.2,1]

<MenuScreen>:
    GridLayout:
        cols: 3
        Button:
            id: main
            text:'Start Grow'
            on_press:
                root.manager.transition.direction= 'right'
                root.manager.current= 'initprocess'
        Button:
            id: sysinfo
            text: 'System Information'
            on_press: root.manager.current= 'sysinfo'

<SystemInfo>:
    GridLayout:
        cols:4
        rows:2
        Label:
            text: 'Temperature'
        Label:
            text: 'Humidity'
        Label:
            text: 'Network Addr.'
        Label:
            text: 'Reset'

<InitializationScreen>:
    GridLayout:
        rows: 2
        cols: 2
        Label:
            text: 'Strain Name'
        TextInput:
            id: strainname
        Label:
            text: 'Parameters'
        TextInput:
            id: spaceholder



 """)

# class SplashScreen(GridLayout):
#
#     def __init__(self, **kwargs):
#         super(LoginScreen, self).__init__(**kwargs)
#         self.rows = 2
#
#         self.add_widget(Label(text='Welcome',font_size=150 ))
#
#         Button:
#         img = Image(source="sprout.png")
#         self.add_widget(img)
#
#
#
# class MainMenu(GridLayout):
#     def __init__(self, **kwargs):
#         super(MainMenu, self).__init__(**kwargs)
#         self.rows = 1
#
#         self.add_widget(Label(text='Main Menu'))

class MyApp(App):


    screens = ["splash", "main", "initprocess", "sysinfo", "parameters", "execproc"]

    def build(self):
        sm = ScreenManager()
        screens = ["splash","main", "initprocess", "sysinfo", "parameters", "execproc"]
        sm.add_widget(SplashScreen(name=screens[0]))
        sm.add_widget(MenuScreen(name=screens[1]))
        sm.add_widget(InitializationScreen(name=screens[2]))
        sm.add_widget(SystemInfo(name=screens[3]))
        sm.add_widget(Parameters(name=screens[4]))
        sm.add_widget(ExecScreen(name=screens[5]))

        sm.current = screens[0]
        return sm

if __name__ == '__main__':
    MyApp().run()

