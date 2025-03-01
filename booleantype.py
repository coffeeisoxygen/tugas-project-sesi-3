from tipedata import tipedata


class BooleanType(tipedata):
    def __init__(self):
        super().__init__(
            "Boolean", "Merepresentasikan satu dari dua nilai: True atau False"
        )

    def show_example(self) -> str:
        return "Contoh:\na = True\nb = False\nc = (5 > 3)  # Ini akan bernilai True"

    def common_operations(self) -> str:
        return """Operasi boolean:
- and: Operator logika AND (True jika keduanya True)
- or: Operator logika OR (True jika salah satu True)
- not: Operator negasi (membalikkan nilai boolean)
- ==, !=, <, >, <=, >=: Operator perbandingan"""
