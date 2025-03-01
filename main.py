# Ahmad Hasan Maki
# 20240040032
# 085777076575

import os
from typing import Optional

from booleantype import BooleanType
from listtype import ListType  # Tipe data baru
from numerictype import NumericType
from tekstype import TextType
from tipedata import tipedata


def clear_screen():
    """Membersihkan layar terminal"""
    os.system("cls" if os.name == "nt" else "clear")


def print_separator():
    """Mencetak garis pemisah"""
    print("\n" + "=" * 40 + "\n")


def display_menu():
    """Menampilkan menu utama"""
    clear_screen()
    print("=== PENJELASAN TIPE DATA PYTHON ===")
    print("Pilih tipe data untuk dipelajari:")
    print("1. Boolean")
    print("2. String")
    print("3. Integer")
    print("4. Float")
    print("5. Complex")
    print("6. List")  # Tipe data baru
    print("0. Keluar")


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
        return ListType()  # Tipe data baru
    else:
        return None


def show_data_type_info(data_type: tipedata):
    """Menampilkan informasi tipe data"""
    clear_screen()
    print(f"=== {data_type.name.upper()} ===")
    print_separator()
    print(data_type.get_info())
    print_separator()
    print(data_type.show_example())
    print_separator()
    print(data_type.common_operations())

    input("\nTekan Enter untuk kembali ke menu utama...")


def main():
    while True:
        display_menu()
        choice = input("\nMasukkan pilihan Anda (0-6): ")

        if choice == "0":
            clear_screen()
            print("Terima kasih telah menggunakan Penjelasan Tipe Data Python!")
            break

        data_type = get_data_type(choice)
        if data_type:
            show_data_type_info(data_type)
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")
            input("Tekan Enter untuk melanjutkan...")


if __name__ == "__main__":
    main()
