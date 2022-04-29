class Menu:
    def __init__(self):
        pass

    def start(self):
        pass

    def options(self):
        pass

    def about(self):
        pass

    def quit(self):
        pass

    def menu_buttons(self):
        pass

class InGameMenu(Menu):
    def __init__(self):
        super().__init__()

    def resume(self):
        pass

    def main_menu(self):
        pass

    def options(self):
        return super().options()

    def quit(self):
        return super().quit()

    def menu_buttons(self):
        return super().menu_buttons()