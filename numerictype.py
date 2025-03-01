from tipedata import tipedata


class NumericType(tipedata):
    def __init__(self, specific_type: str = ""):
        if specific_type == "int":
            super().__init__(
                "Integer", "Merepresentasikan bilangan bulat tanpa titik desimal"
            )
        elif specific_type == "float":
            super().__init__("Float", "Merepresentasikan bilangan dengan titik desimal")
        elif specific_type == "complex":
            super().__init__(
                "Complex",
                "Merepresentasikan bilangan kompleks dengan bagian real dan imajiner",
            )
        else:
            super().__init__(
                "Numeric",
                "Merepresentasikan berbagai jenis angka (int, float, complex)",
            )

    def show_example(self):
        if self.name == "Integer":
            print("Contoh:\na = 10\nb = -5\nc = 0")
        elif self.name == "Float":
            print("Contoh:\na = 10.5\nb = -3.14\nc = 0.0")
        elif self.name == "Complex":
            print("Contoh:\na = 3+4j\nb = complex(3, 4)")
        else:
            print("Lihat tipe numerik spesifik untuk contohnya")
