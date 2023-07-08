# Author: Mujtaba
# Date: July 1, 2023

import sys
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.splitter import Splitter
from kivy.uix.statusbar import StatusBar
from kivy.uix.docklayout import DockLayout
from kivy.uix.textinput import TextInput
from kivy.uix.docklayout import DockLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.actionbar import ActionButton
from kivy.uix.menu import Menu, MenuItem
from kivy.uix.popup import Popup
from kivy.core.window import Window


class SidebarOption(BoxLayout):
    def __init__(self, label, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        label_widget = Label(text=label)
        self.add_widget(label_widget)

        row_layout = BoxLayout(orientation='horizontal')
        self.add_widget(row_layout)

        input_widget = TextInput()
        row_layout.add_widget(input_widget)

        add_button = Button(text="ADD")
        row_layout.add_widget(add_button)


class MainWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        menubar = Menu()

        # File menu
        file_menu = Menu()
        file_menu.add_widget(MenuItem(text="New"))
        file_menu.add_widget(MenuItem(text="Open"))
        file_menu.add_widget(MenuItem(text="Save"))
        menubar.add_widget(file_menu)

        # Options menu
        options_menu = Menu()
        options_menu.add_widget(MenuItem(text="Preferences"))
        options_menu.add_widget(MenuItem(text="Settings"))
        menubar.add_widget(options_menu)

        # Tools menu
        tools_menu = Menu()
        tools_menu.add_widget(MenuItem(text="Calculator"))
        tools_menu.add_widget(MenuItem(text="Notepad"))
        tools_menu.add_widget(MenuItem(text="Terminal"))
        menubar.add_widget(tools_menu)

        # Extensions menu
        extensions_menu = Menu()
        extensions_menu.add_widget(MenuItem(text="Plugin 1"))
        extensions_menu.add_widget(MenuItem(text="Plugin 2"))
        menubar.add_widget(extensions_menu)

        # Support us menu
        support_menu = Menu()
        support_menu.add_widget(MenuItem(text="Donate"))
        support_menu.add_widget(MenuItem(text="Feedback"))
        menubar.add_widget(support_menu)

        self.add_widget(menubar)

        toolbar = BoxLayout()
        self.add_widget(toolbar)

        action_menu = ActionButton()
        action_menu.text = 'Menu'
        action_menu.bind(on_press=self.open_list_menu)
        toolbar.add_widget(action_menu)

        for i in range(1, 11):
            action = ActionButton()
            action.text = f"Action {i}"
            toolbar.add_widget(action)

        splitter = Splitter()

        left_sidebar = BoxLayout(orientation='vertical')
        left_sidebar.size_hint_x = 0.25

        for i in range(1, 21):
            option = SidebarOption(f"Option {i}")
            left_sidebar.add_widget(option)

        left_scroll_area = ScrollView()
        left_scroll_area.add_widget(left_sidebar)

        splitter.add_widget(left_scroll_area)

        text_editor = TextInput()
        splitter.add_widget(text_editor)

        right_sidebar = BoxLayout(orientation='vertical')
        right_sidebar.size_hint_x = 0.25

        for i in range(1, 11):
            option = SidebarOption(f"Option {i}")
            right_sidebar.add_widget(option)

        right_scroll_area = ScrollView()
        right_scroll_area.add_widget(right_sidebar)

        splitter.add_widget(right_scroll_area)

        self.add_widget(splitter)

        status_bar = StatusBar()
        status_bar.text = "Status message goes here"
        self.add_widget(status_bar)

        bottom_bar = DockLayout(size_hint_y=0.15)

        terminal = TextInput()
        bottom_bar.add_widget(terminal)

        self.add_widget(bottom_bar)

        enable_copilot_button = Button(text="Copilot: Enabled")
        enable_copilot_button.background_color = (0, 1, 0, 1)
        enable_copilot_button.bind(on_press=self.toggle_copilot)
        status_bar.add_widget(enable_copilot_button)

    def open_list_menu(self, instance):
        menu = Menu()

        num_items = 20  # Number of menu items

        for index in range(1, num_items + 1):
            menu_item = MenuItem(text=f"Menu Option {index}")
            menu_item.bind(on_press=self.menu_option_clicked)
            menu.add_widget(menu_item)

        popup = Popup(title='Menu', content=menu, size_hint=(None, None), size=(400, 400))
        popup.open()

    def menu_option_clicked(self, instance):
        print(f"Menu option clicked: {instance.text}")

    def toggle_copilot(self, instance):
        if instance.text == "Copilot: Enabled":
            instance.text = "Copilot: Disabled"
            instance.background_color = (1, 0, 0, 1)
        else:
            instance.text = "Copilot: Enabled"
            instance.background_color = (0, 1, 0, 1)


class MyApp(App):
    def build(self):
        Window.size = (1320, 600)
        return MainWindow()


if __name__ == "__main__":
    MyApp().run()
