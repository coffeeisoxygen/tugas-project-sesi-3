from tipedata import tipedata


class BooleanType(tipedata):
    """Merepresentasikan tipe data boolean."""

    def __init__(self):
        super().__init__(
            "Boolean", "Merepresentasikan satu dari dua nilai: True atau False"
        )

    def show_example(self) -> str:
        """Menampilkan contoh penggunaan tipe data boolean."""
        return "Contoh:\na = True\nb = False\nc = (5 > 3)  # Ini akan bernilai True"

    def common_operations(self) -> str:
        """Menampilkan operasi umum untuk tipe data boolean."""
        return """Operasi boolean:
- and: Operator logika AND (True jika keduanya True)
- or: Operator logika OR (True jika salah satu True)
- not: Operator negasi (membalikkan nilai boolean)
- ==, !=, <, >, <=, >=: Operator perbandingan"""
