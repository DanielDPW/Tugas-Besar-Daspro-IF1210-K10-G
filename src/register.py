from . import utils

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

def register(user_data, current_user):
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
    
    return user_data