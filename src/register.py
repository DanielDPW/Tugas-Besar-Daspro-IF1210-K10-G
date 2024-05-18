from . import utils
from . import inventory

def check_valid_characters(x : str) -> bool:
    valid_character = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-"
    if len(x) == 0:
        return False
    else:
        for char in x:
            if char not in valid_character:
                return False
        return True

def generate_user_id(user_data):
    existing_id = utils.ascending_sort([user_data[i][0] for i in range(1, len(user_data)) if not utils.is_space(user_data[i][0])])
    num = 1
    while str(num) in existing_id:
        num = num + 1
    return str(num)

def register(user_data, current_user, monster_data, monster_inventory_data):
    if not utils.is_empty(current_user):
        print(f"Anda telah login dengan username {current_user[1]}, silahkan lakukan 'LOGOUT' sebelum melakukan register.")
    else:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        if utils.is_space(username) or utils.is_space(password):
            print("Username atau password tidak boleh kosong!")
        elif utils.is_in_column(utils.slice_matrix(user_data, row_start = 1), 1, username):
            print(f"Username {username} telah terpakai, silahkan gunakan username lain!")
        elif not check_valid_characters(username):
            print("Username hanya boleh berisi alfabet, angka, underscore, dan strip!")
        else:
            id = generate_user_id(user_data)
            new_user_data = [id, username, password, 'agent', '0']
            user_data.append(new_user_data)
            print(f"Anda telah mendaftarkan user {username}")
            monster_inventory_data = choose_starter(id, monster_data, monster_inventory_data)
    
    return user_data, monster_inventory_data

def choose_starter(user_id, monster_data, monster_inventory_data):
    monster_list = utils.slice_matrix(monster_data,row_start = 1)
    if len(monster_list) == 0:
        print("Tidak ada monster di database")
    else:
        starter_range = utils.min(len(monster_list), 3)
        starter_ids = []
        for i in range(starter_range):
            print(f"{monster_list[i][0]} {monster_list[i][1]} ATK Power: {monster_list[i][2]} DEF Power: {monster_list[i][3]} HP: {monster_list[i][4]} Speed: {monster_list[i][5]}")
            starter_ids.append(monster_list[i][0])
        while True:
            prompt = utils.strip(input("Masukkan ID: "))
            if utils.strip(prompt) not in starter_ids:
                print("Masukkan ID yang valid")
            else:
                monster_index = utils.find_row(monster_list ,0, prompt)
                monster_inventory_data.append([user_id, monster_list[monster_index][0], '1',inventory.name_monster(user_id,monster_inventory_data),monster_list[monster_index][4]])
                return monster_inventory_data