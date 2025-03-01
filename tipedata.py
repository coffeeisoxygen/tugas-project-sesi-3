class tipedata:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def get_info(self):
        return f"Tipe: {self.name}\nDeskripsi: {self.description}"

    def show_example(self):
        pass  # To be implemented by child classes
