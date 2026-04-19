from kivy.app import App
from kivy.uix.label import Label
class LabApp(App):
    def build(self):
        return Label(text='Shivam Lab App - Logic Ready')
if __name__ == '__main__':
    LabApp().run()
