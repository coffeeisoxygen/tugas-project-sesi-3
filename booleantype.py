from tipedata import tipedata


class BooleanType(tipedata):
    def __init__(self):
        super().__init__(
            "Boolean", "Merepresentasikan satu dari dua nilai: True atau False"
        )

    def show_example(self):
        print("Contoh:\na = True\nb = False\nc = (5 > 3)  # Ini akan bernilai True")
