from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import builder
from kivymd.app import MDApp


class MyApp(App):
    def build(self):
        # Ana düzen
        layout = BoxLayout(orientation='vertical')

        # Bir etiket ve bir buton ekleyelim
        self.label = Label(text='Merhaba Dünya!', font_size=24)
        button = Button(text='Bana Tıkla!', size_hint=(1, 0.2))
        button.bind(on_press=self.on_button_press)

        # Düzen içerisine ekle
        layout.add_widget(self.label)
        layout.add_widget(button)

        return layout

    def on_button_press(self, instance):
        # Butona tıklandığında yapılacak işlem
        self.label.text = 'SOZ TEST PROJESİ!'


if __name__ == '__main__':
    MyApp().run()
