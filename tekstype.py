from tipedata import tipedata


class TextType(tipedata):
    def __init__(self):
        super().__init__(
            "String", "Merepresentasikan data teks sebagai rangkaian karakter"
        )

    def show_example(self):
        print('Contoh:\nnama = "John Doe"\npesan = \'Halo Dunia\'\nmulti_baris = """Ini adalah\nteks multi baris"""')
