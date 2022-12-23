import os
import time
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
KV = """
MyBL:
        orientation: "vertical"
        size_hint: (0.95, 0.95)
        pos_hint: {"center_x": 0.5, "center_y":0.5}
        
        Label:
                font_size: "30sp"
                text: root.data_label
    
        TextInput:
                id: Inp
                multiline: False
                padding_y: (5,5)
                size_hint: (1,0.5)
                on_text: app.process()
        Button:
                text: "Почати перевірку"
                bold: True
                background_color:'00FFCE'
                size_hint: (1,0.5)
                on_press: root.callback()
                
                
"""
class MyBL(BoxLayout):
    
    data_label = StringProperty("Server check")
    
    def callback(self):
        
        while True:
            ip = [self.ids.Inp.text]
            for val in ip:
                response = os.system('ping -n 1 ' + val)
            if response == 0:
                print(val + ' is up!')
            else:
                print(val + ' is down!')
            time.sleep(1)
        
class MyApp(App):
    running = True
    def process(self):
        text = self.root.ids.Inp.text
        
    def build(self):
        return Builder.load_string(KV)
    
    def on_stop(self):
        self.running = False
        
MyApp().run()
