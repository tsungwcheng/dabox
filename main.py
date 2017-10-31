from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.config import Config

from kivy.uix.screenmanager import ScreenManager, Screen


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

    FloatLayout:
        size:500,300
        canvas.before:
            Color:
                rgba: 0,0,0.5,0.3
            Rectangle:
                pos: 0,0
                size:self.size
        Button:
            size_hint:(0.2,0.2)
            on_press: root.manager.current = "main"
            Image:
                source: 'sprout.png'
                size: 400,240
                pos:50,0

                halign : 'center'
                valign : 'center'
                allow_stretch: True
        Label:
            size_hint: (0.15,0.15)
            text: 'Test'
            text_size: self.size
            pos:250,150
            halign : 'center'
            valign : 'center'
            font_size: 20
            bold: 1
            color: [0,0.9,0.2,1]

<MenuScreen>:
    FloatLayout:
        size: 500, 300
        canvas.before:
            Color:
                rgba:0.65,0.65,0.65,1
            Rectangle:
                pos: 0,0
                size:self.size
            Color:
                rgba:1,1,1,1
            Rectangle:
                pos:240,0
                size:self.size
        Button:
            size_hint:(.15,.15)
            pos: (500,320)
            id: main
            text:'Update Watering Time'
            on_press:
                wateringtime.text = '2:00'
                #root.manager.transition.direction= 'right'
                #root.manager.current= 'initprocess'
        Label:
            pos: (60, 20)
            size_hint:(.15,.15)
            font_size: 35
            markup: True
            text: '[b]Temperature'

        Label:
            pos: (220, 20)
            size_hint:(.15,.15)
            font_size: 35
            markup: True
            id: tempval
            text: '45'

        Label:
            pos:(60,150)
            size_hint:(.15,.15)
            font_size: 35
            markup: True
            text: '[b]Humidity'

        Label:
            pos:(220,150)
            size_hint:(.15,.15)
            font_size: 35
            markup: True
            id: humidityval
            text: 'sowet'

        Label:
            pos:(60,280)
            size_hint:(.15,.15)
            font_size: 35
            markup: True
            text: '[b]Water in:'

        Label:
            pos:(220,280)
            size_hint:(.15,.15)
            font_size: 35
            markup: True
            id: wateringtime
            text: '1:55'


<SystemInfo>:
    GridLayout:
        size: 480, 320
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
        size: 480, 320
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
    Config.set('graphics', 'resizable', 0)
    Window.size = (500, 300)
    MyApp().run()

