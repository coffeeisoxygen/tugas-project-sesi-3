from tipedata.tipedata import tipedata


class ListType(tipedata):
    def __init__(self):
        super().__init__(
            "List", "Merepresentasikan kumpulan item yang berurutan dan dapat diubah"
        )

    def show_example(self) -> str:
        return "Contoh:\nbuah = ['apel', 'pisang', 'jeruk']\nnomor = [1, 2, 3, 4]\ndata_campur = [1, 'dua', 3.0, True]"

    def common_operations(self) -> str:
        return """Operasi list:
- Akses elemen: list[index]
- Slicing: list[start:end]
- Penambahan: append(), extend(), insert()
- Penghapusan: pop(), remove(), clear()
- Lainnya: sort(), reverse(), count(), index()"""
