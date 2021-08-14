from kivymd.app import MDApp
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget




class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Purple"

    def add_item(self, text):
        new_list_item = OneLineIconListItem(text=text)
        new_list_item.add_widget(
            IconLeftWidget(icon = "language-python")
            )
        self.root.ids.listcontainer.add_widget(new_list_item)
        self.root.ids.listinput.text = ''


if __name__ == "__main__":
    app = MainApp()
    app.run()