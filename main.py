from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.core.window import Window
import random

class MAXApp(App):
    def build(self):
        # Чёрный экран
        Window.clearcolor = (0, 0, 0, 1)
        layout = BoxLayout()
        layout.canvas.before.add(Color(0, 0, 0, 1))
        layout.canvas.before.add(Rectangle(size=Window.size, pos=Window.pos))

        # Рандом ошибка сразу
        errors = [
            "Ошибка 404: Реальность не найдена",
            "MAX не выдержал нагрузки 😵",
            "Ошибка 418: Я — чайник ☕",
            "Код 500: Сервер спит 💤",
            "Фатальная ошибка: MAX устал 🥱",
            "Сбой: Перезагрузи вселенную 🔄",
            "Ошибка 0xDEAD: Душа не обнаружена 👻"
        ]
        error = random.choice(errors)

        # Popup
        content = BoxLayout(orientation='vertical')
        label = Label(text=error, size_hint_y=None, height=200)
        btn = Button(text='ОК', size_hint_y=None, height=50)
        btn.bind(on_press=self.stop)
        content.add_widget(label)
        content.add_widget(btn)

        popup = Popup(title='Ошибка!', content=content, size_hint=(0.8, 0.5))
        popup.open()

        return layout

MAXApp().run()