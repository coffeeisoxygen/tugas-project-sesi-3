from tipedata.tipedata import tipedata


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

    def show_example(self) -> str:
        if self.name == "Integer":
            return "Contoh:\na = 10\nb = -5\nc = 0"
        elif self.name == "Float":
            return "Contoh:\na = 10.5\nb = -3.14\nc = 0.0"
        elif self.name == "Complex":
            return "Contoh:\na = 3+4j\nb = complex(3, 4)"
        else:
            return "Lihat tipe numerik spesifik untuk contohnya"

    def common_operations(self) -> str:
        if self.name == "Integer" or self.name == "Float":
            return """Operasi numerik:
- Aritmatika: +, -, *, /, //, %, **
- Perbandingan: ==, !=, <, >, <=, >=
- Metode: abs(), round()"""
        elif self.name == "Complex":
            return """Operasi bilangan kompleks:
- Aritmatika: +, -, *, /
- Atribut: real, imag
- Metode: conjugate()"""
        else:
            return "Lihat tipe numerik spesifik untuk operasinya"
