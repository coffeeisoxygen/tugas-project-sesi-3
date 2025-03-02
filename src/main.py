# Dosenn : Shinta Ayuningtias, S.Kom., M.Kom
# Mata Kuliah : Dasar Pemerograman
# Mahasiswa : Ahmad Hasan Maki
# Nim : 20240040032
# Telp : 085777076575
# Kelas : TI24B
# Pertemuan : 6

import os
from typing import Optional

from src.tipedata.booleantype import BooleanType
from src.tipedata.dicttype import DictType
from src.tipedata.listtype import ListType
from src.tipedata.numerictype import NumericType
from src.tipedata.tekstype import TextType
from src.tipedata.tipedata import tipedata
from src.tipedata.tupletype import TupleType
from src.utils.colors import Colors


def show_version_info():
    print(Colors.subtitle("Versi: 1.0.0"))
    print(Colors.subtitle("© 2024 Ahmad Hasan Maki"))


def confirm_exit() -> bool:
    while True:
        answer = input("Anda yakin ingin keluar? (y/n): ").lower()
        if answer in ("y", "n"):
            return answer == "y"


def show_loading():
    import time

    print(Colors.colorize("Loading", Colors.BRIGHT_CYAN), end="")
    for _ in range(3):
        time.sleep(0.2)
        print(Colors.colorize(".", Colors.BRIGHT_CYAN), end="", flush=True)
    print()


def clear_screen():
    """Membersihkan layar terminal"""
    os.system("cls" if os.name == "nt" else "clear")


def print_separator():
    """Mencetak garis pemisah"""
    print("\n" + "=" * 40 + "\n")


def display_menu():
    """Menampilkan menu utama"""
    clear_screen()
    print(Colors.title("=== PENJELASAN TIPE DATA PYTHON ==="))
    print(Colors.subtitle("Pilih tipe data untuk dipelajari:"))
    print("1. " + Colors.highlight("Boolean"))
    print("2. " + Colors.highlight("String"))
    print("3. " + Colors.highlight("Integer"))
    print("4. " + Colors.highlight("Float"))
    print("5. " + Colors.highlight("Complex"))
    print("6. " + Colors.highlight("List"))
    print("7. " + Colors.highlight("Tuple"))
    print("8. " + Colors.highlight("Dictionary"))
    print("0. " + Colors.highlight("Keluar"))


def get_data_type(choice: str) -> Optional[tipedata]:
    """Mengembalikan objek tipe data berdasarkan pilihan"""
    if choice == "1":
        return BooleanType()
    elif choice == "2":
        return TextType()
    elif choice == "3":
        return NumericType("int")
    elif choice == "4":
        return NumericType("float")
    elif choice == "5":
        return NumericType("complex")
    elif choice == "6":
        return ListType()
    elif choice == "7":
        return TupleType()
    elif choice == "8":
        return DictType()
    else:
        return None


def show_data_type_info(data_type: tipedata):
    """Menampilkan informasi tipe data"""
    clear_screen()
    print(Colors.title(f"=== {data_type.name.upper()} ==="))
    print_separator()

    # Informasi dasar
    info = data_type.get_info().split("\n")
    print(Colors.subtitle(info[0]))
    print(info[1])

    print_separator()

    # Contoh kode
    print(Colors.subtitle("Contoh:"))
    example = data_type.show_example().replace("Contoh:\n", "")
    print(Colors.code(example))

    print_separator()

    # Operasi umum
    print(Colors.subtitle("Operasi Umum:"))
    print(data_type.common_operations().replace("Operasi", "").strip())

    input("\nTekan Enter untuk kembali ke menu utama...")


def main():
    while True:
        display_menu()
        choice = input("\nMasukkan pilihan Anda (0-8): ")

        if choice == "0":
            clear_screen()
            print("Terima kasih!")
            break

        data_type = get_data_type(choice)
        if data_type:
            show_data_type_info(data_type)
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")
            input("Tekan Enter untuk melanjutkan...")


if __name__ == "__main__":
    main()
