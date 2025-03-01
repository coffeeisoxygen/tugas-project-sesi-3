from tipedata import tipedata


class TupleType(tipedata):
    def __init__(self):
        self.name = "Tuple"

    def get_info(self):
        return """Tuple adalah tipe data yang mirip dengan list tetapi immutable (tidak bisa diubah).
Tuple dibuat dengan tanda kurung () dan elemen dipisahkan dengan koma."""

    def show_example(self):
        return """# Membuat tuple
coordinates = (10, 20)
person = ('John', 25, True)

# Mengakses elemen tuple
print(coordinates[0])  # Output: 10
print(person[1])      # Output: 25"""

    def common_operations(self):
        return """Operasi umum pada Tuple:
- Mengakses elemen dengan indeks: tuple[index]
- Menghitung panjang: len(tuple)
- Menggabungkan tuple: tuple1 + tuple2
- Mengecek keberadaan elemen: item in tuple"""
