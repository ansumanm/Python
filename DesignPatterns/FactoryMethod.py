"""
The Button Objects
"""
class Button:
    def render(self):
        pass

    def onClick(self):
        pass

class WindowsButton(Button):
    def render(self):
        return "Rendering Windows button"

    def onClick(self):
        return "Handle click on Windows button"

class HTMLButton(Button):
    def render(self):
        return "Rendering HTML button"

    def onClick(self):
        return "Handle click on HTML button"

"""
The dialogue objects -- factory methods that create the button objects
"""
class Dialog:
    def createButton(self):
        pass

    def render(self):
        # Call the factory method to create a product object.
        button = self.createButton()
        # Now use the product.
        result = button.render()
        return result

class WindowsDialog(Dialog):
    def createButton(self):
        return WindowsButton()

class WebDialog(Dialog):
    def createButton(self):
        return HTMLButton()

"""
Usage of factory pattern:-
client recieves the base Dialog object, and calls its render.

Based on what type of Dialog object was passed to client, the button object is created.
"""
# Client code
def client_code(dialog: Dialog):
    print(dialog.render())

# Using WindowsDialog
windows_dialog = WindowsDialog()
client_code(windows_dialog)

# Using WebDialog
web_dialog = WebDialog()
client_code(web_dialog)
