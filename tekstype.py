from tipedata import tipedata


class TextType(tipedata):
    def __init__(self):
        super().__init__(
            "String", "Merepresentasikan data teks sebagai rangkaian karakter"
        )

    def show_example(self) -> str:
        return 'Contoh:\nnama = "John Doe"\npesan = \'Halo Dunia\'\nmulti_baris = """Ini adalah\nteks multi baris"""'

    def common_operations(self) -> str:
        return """Operasi string:
- Concatenation (+): "Hello" + " World" = "Hello World"
- Repetition (*): "Hi" * 3 = "HiHiHi"
- Slicing: teks[0:5]
- Metode: upper(), lower(), strip(), split(), replace()"""
