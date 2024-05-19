import time

from typing import *
from . import utils

def print_monster_management():
    print("""
▄██▄▄██▄░▄█████▄░██████▄░▄██████░████████░▄█████░█████▄░░░▄██▄▄██▄░▄████▄░██████▄░▄████▄░▄██████░▄█████░▄██▄▄██▄░▄█████░██████▄░████████
██░██░██░██░░░██░██░░░██░██░░░░░░░░░██░░░░██░░░░░██░░██░░░██░██░██░██░░██░██░░░██░██░░██░██░░░░░░██░░░░░██░██░██░██░░░░░██░░░██░░░░██░░░
██░██░██░██░░░██░██░░░██░▀█████▄░░░░██░░░░█████░░█████▀░░░██░██░██░██░░██░██░░░██░██░░██░██░░███░█████░░██░██░██░█████░░██░░░██░░░░██░░░
██░██░██░██░░░██░██░░░██░░░░░░██░░░░██░░░░██░░░░░██░░██░░░██░██░██░██████░██░░░██░██████░██░░░██░██░░░░░██░██░██░██░░░░░██░░░██░░░░██░░░
██░██░██░▀█████▀░██░░░██░██████▀░░░░██░░░░▀█████░██░░██░░░██░██░██░██░░██░██░░░██░██░░██░▀█████▀░▀█████░██░██░██░▀█████░██░░░██░░░░██░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
""")
    
def monster_management(current_user, monster_data, monster_inventory_data, monster_shop_data):
    if utils.is_empty(current_user):
        print("Anda belum login")
        time.sleep(1)
        utils.remove_x_line_above(2)
        return monster_data, monster_inventory_data, monster_shop_data
    elif utils.strip(current_user[3]) != 'admin':
        print("Anda bukan Admin")
        time.sleep(1)
        utils.remove_x_line_above(2)
        return monster_data, monster_inventory_data, monster_shop_data
    else:
        print_monster_management()
        while True:
            print("1. Tampilkan semua Monster")
            print("2. Tambah Monster baru")
            print("3. Hapus Monster")
            print("4. Keluar")
            prompt = utils.strip(input("Pilih aksi: "))
            if prompt == '1':
                show_monster(monster_data)
            elif prompt == '2':
                monster_data = add_monster(monster_data)
            elif prompt == '3':
                monster_data, monster_inventory_data, monster_shop_data = remove_monster(monster_data, monster_inventory_data, monster_shop_data)
            elif prompt == '4':
                return monster_data, monster_inventory_data, monster_shop_data
            else:
                print("Masukkan input yang valid")

def generate_monster_id(monster_data):
    existing_id = utils.ascending_sort([monster_data[i][0] for i in range(1, len(monster_data)) if not utils.is_space(monster_data[i][0])])
    num = 1
    while str(num) in existing_id:
        num = num + 1
    return str(num)


def show_monster(monster_data):
    utils.clear_terminal()
    print_monster_management()
    print(f"{'ID':<10}{'Type':<20}{'ATK Power':<10} {'DEF Power':<10}{'HP':<10}{'Speed':<10}")
    for row in utils.slice_matrix(monster_data,row_start = 1):
        print(f"{row[0]:<10} {row[1]:<20} {row[2]:<10} {row[3]:<10} {row[4]:<10} {row[5]:<10}")

def add_type(monster_data):
    while True:
        prompt = utils.strip(input("Masukkan Type: "))
        if len(prompt) == 0 or utils.is_space(prompt):
            print("Tipe tidak boleh kosong")
            time.sleep(1)
            utils.remove_x_line_above(2)
        elif utils.is_in_column(monster_data,index = 1, x = prompt):
            print("Tipe sudah terdaftar. Coba lagi!")
            time.sleep(1)
            utils.remove_x_line_above(2)
        elif len(prompt) > 20:
            print("Tipe tidak boleh melebihi 20 karakter")
            time.sleep(1)
            utils.remove_x_line_above(2)
        else:
            break
    return prompt

def add_stat(stat : str, idx : int, min : Optional[int] = None, max : Optional[int] = None):
    while True:
        prompt = utils.strip(input(f"Masukkan {stat}{f' {min} - {max}' if min is not None and max is not None else ''}: "))
        if len(prompt) == 0 or utils.is_space(prompt):
            print(f"{stat} tidak boleh kosong")
            time.sleep(1)
            utils.remove_x_line_above(2)
        elif not utils.is_int(prompt):
            print("Masukkan input bertipe Integer, coba lagi!")
            time.sleep(1)
            utils.remove_x_line_above(2)
        elif min != None and max != None and (int(prompt) < min or int(prompt) > max):
            print(f"{stat} harus bernilai {min}-{max}, coba lagi!")
            time.sleep(1)
            utils.remove_x_line_above(2)
        else:
            break
    return prompt

def add_monster(monster_data):
    type = add_type(monster_data)
    atk_power = add_stat("ATK Power",idx = 2, min = 0, max = 9999999999)
    def_power = add_stat("DEF Power",idx = 3, min = 0, max = 50)
    hp = add_stat("HP",idx = 4, min = 0, max = 9999999999)
    speed = add_stat("Speed",idx = 5, min = 0, max = 50)
    while True:
        prompt = utils.strip(input("Tambahkan Monster ke database? (Y/N): "))
        if prompt.lower() == 'y':
            utils.remove_xth_line_above(1)
            monster_data.append([generate_monster_id(monster_data),type,atk_power,def_power,hp,speed])
            print(f"Monster {type} telah ditambahkan ke database")
            time.sleep(1)
            break
        elif prompt.lower() == 'n':
            break
        else:
            print("Masukkan input yang valid")
            time.sleep(1)
            utils.remove_x_line_above(2)
    utils.clear_terminal()
    print_monster_management()
    return monster_data

def remove_monster(monster_data, monster_inventory_data, monster_shop_data):
    monster_ids = [monster_data[i][0] for i in range(1, len(monster_data))]
    while True:
        prompt = utils.strip(input("Masukkan ID monster: "))
        if prompt not in monster_ids:
            print("Tolong masukkan id yang valid!")
            time.sleep(1)
            utils.remove_x_line_above(2)
        else:
            break
    monster_id = prompt
    while True:
        prompt = utils.strip(input("Hapus Monster ke database? (Y/N): "))
        if prompt.lower() == 'y':
            utils.remove_xth_line_above(1)
            print("Monster telah dihapuskan dari database")
            monster_data = utils.remove_row(monster_data,index = 0,element = monster_id)
            monster_inventory_data = utils.remove_row(monster_inventory_data,index = 1, element = monster_id)
            monster_shop_data = utils.remove_row(monster_shop_data, index = 0, element = monster_id)
            time.sleep(1)
            break
        elif prompt.lower() == 'n':
            break
    utils.clear_terminal()
    print_monster_management()
    return monster_data,monster_inventory_data,monster_shop_data
    