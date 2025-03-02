from tipedata.tipedata import tipedata


class DictType(tipedata):
    def __init__(self):
        self.name = "Dictionary"

    def get_info(self):
        return """Dictionary adalah tipe data yang menyimpan pasangan key-value.
Setiap elemen dalam dictionary memiliki key unik yang digunakan untuk mengakses value."""

    def show_example(self):
        return """# Membuat dictionary
person = {
    'name': 'John',
    'age': 25,
    'city': 'Jakarta'
}

# Mengakses dan mengubah nilai
print(person['name'])     # Output: John
person['age'] = 26       # Mengubah nilai
person['job'] = 'Dev'    # Menambah key-value baru"""

    def common_operations(self):
        return """Operasi umum pada Dictionary:
- Mengakses value: dict[key]
- Menambah/mengubah item: dict[key] = value
- Menghapus item: del dict[key]
- Mendapatkan semua keys: dict.keys()
- Mendapatkan semua values: dict.values()"""
