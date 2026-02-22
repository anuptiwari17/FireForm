from file_manipulator import FileManipulator

class Controller:
    def __init__(self):
        self.file_manipulator = FileManipulator()

    def fill_form(self, user_input: str, definitions: list, pdf_form_path: str):
        self.file_manipulator.fill_form(user_input, definitions, pdf_form_path)