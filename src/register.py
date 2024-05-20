import time
from typing import *

from . import utils
from . import inventory
from .types import *

def check_valid_characters(x : str) -> bool:
    valid_character = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-"
    if len(x) == 0:
        return False
    else:
        for char in x:
            if char not in valid_character:
                return False
        return True

def generate_user_id(user_data : Matrix) -> str:
    existing_id = utils.ascending_sort([user_data[i][0] for i in range(1, len(user_data)) if not utils.is_space(user_data[i][0])])
    num = 1
    while str(num) in existing_id:
        num = num + 1
    return str(num)

def register(user_data : Matrix, current_user : Matrix, monster_data : Matrix, monster_inventory_data : Matrix) -> Tuple[Matrix, Matrix]:
    
    # Cek apakah tidak ada user yang sendang menggunakan program
    if not utils.is_empty(current_user):
        print(f"Anda telah login dengan username {current_user[1]}, silahkan lakukan 'LOGOUT' sebelum melakukan register.")
        time.sleep(1)
        utils.clear_terminal()
    else:
        while True:
            username = utils.strip(input("Masukkan username: "))
            if utils.is_space(username):
                print("Username tidak boleh kosong")
                time.sleep(1)
                utils.remove_x_line_above(2)
            else:
                break
        while True:
            password = utils.strip(input("Masukkan password: "))
            if utils.is_space(password):
                print("Password tidak boleh kosong")
                time.sleep(1)
                utils.remove_x_line_above(2)
            else:
                break
        # Jika sudah ada username yang terpakai
        if utils.is_in_column(utils.slice_matrix(user_data, row_start = 1), 1, username):
            print(f"Username {username} telah terpakai, silahkan gunakan username lain!")
            time.sleep(1)
            utils.clear_terminal()
        elif not check_valid_characters(username):
            print("Username hanya boleh berisi alfabet, angka, underscore, dan strip!")
            time.sleep(1)
            utils.clear_terminal()
        else:
            # Jika tidak, maka digenerate hal yang diperlukan
            id = generate_user_id(user_data)
            new_user_data = [id, username, password, 'agent', '0']
            user_data.append(new_user_data)
            print(f"Anda telah mendaftarkan user {username}")
            time.sleep(1)
            utils.clear_terminal()
            monster_inventory_data = choose_starter(id, monster_data, monster_inventory_data)
    
    return user_data, monster_inventory_data

def choose_starter(user_id : str, monster_data : Matrix, monster_inventory_data : Matrix):
    monster_list = utils.slice_matrix(monster_data,row_start = 1)

    # Jika tidak ada monster di database, maka program diterminasi
    if len(monster_list) == 0:
        print("Tidak ada monster di database")
        time.sleep(1)
        utils.remove_xth_line_above(1)
        return monster_inventory_data
    else:
        # Ambil maksimal 3 monster untuk pilihan pertama
        starter_range = utils.min(len(monster_list), 3)
        starter_ids = []
        print(f"{'ID':<10}{'Type':<20}{'ATK Power':<10}{'DEF Power':<10}{'HP':<10}{'Speed':<10}")
        for i in range(starter_range):
            print(f"{monster_list[i][0]:<10}{monster_list[i][1]:<20}{monster_list[i][2]:<10}{monster_list[i][3]:<10}{monster_list[i][4]:<10}{monster_list[i][5]:<10}")
            starter_ids.append(monster_list[i][0])
        while True:
            while True:
                prompt = utils.strip(input("Masukkan ID: "))
                if utils.strip(prompt) not in starter_ids:
                    print("Masukkan ID yang valid")
                    time.sleep(1)
                    utils.remove_x_line_above(2)
                else:
                    break
            id = prompt

            while True:
                prompt = utils.strip(input("Apakah Anda yakin? (Y/N): "))
                if prompt.lower() == 'y':
                    monster_index = utils.find_row(monster_list ,0, id)
                    monster_inventory_data.append([user_id, monster_list[monster_index][0], '1',inventory.name_monster(user_id,monster_inventory_data),monster_list[monster_index][4]])
                    utils.remove_x_line_above(2)
                    print("Selamat! Anda telah mendapatkan monster pertama Anda")
                    time.sleep(1.5)
                    utils.clear_terminal()
                    return monster_inventory_data
                elif prompt.lower() == 'n':
                    utils.remove_x_line_above(3)
                    break
                