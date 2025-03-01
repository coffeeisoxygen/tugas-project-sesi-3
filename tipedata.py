class tipedata:
    """
    Kelas tipedata merepresentasikan tipe data dengan nama dan deskripsi.
    Attributes:
        name (str): Nama dari tipe data.
        description (str): Deskripsi dari tipe data.
    Methods:
        get_info() -> str:
            Mengembalikan informasi tipe data dalam format string.
        show_example() -> str:
            Mengembalikan contoh penggunaan tipe data. Akan diimplementasikan oleh kelas turunan.
        common_operations() -> str:
            Mengembalikan operasi umum untuk tipe data ini. Akan diimplementasikan oleh kelas turunan.
    """

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def get_info(self) -> str:
        return f"Tipe: {self.name}\nDeskripsi: {self.description}"

    def show_example(self) -> str:
        """Mengembalikan contoh penggunaan tipe data"""
        return ""  # Akan diimplementasikan oleh kelas turunan

    def common_operations(self) -> str:
        """Mengembalikan operasi umum untuk tipe data ini"""
        return ""  # Akan diimplementasikan oleh kelas turunan
