import time
from . import utils

def login(user_data, current_user):
    if not utils.is_empty(current_user):
        print(f"Anda telah login dengan username {current_user[1]}, silahkan lakukan 'LOGOUT' sebelum melakukan register.")
        time.sleep(1)
        utils.remove_x_line_above(2)
        return current_user, None
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
        user_index = utils.find_row(utils.slice_matrix(user_data, row_start = 1), 1, username) + 1
        user_id = user_data[user_index][0]

        if not utils.is_in_column(utils.slice_matrix(user_data, row_start = 1), 1, username):
            print(f"Username tidak terdaftar!")
            time.sleep(1)
            utils.remove_x_line_above(4)
            return current_user, None
        elif not password == user_data[user_index][2]:
            print("Password salah!")
            time.sleep(1)
            utils.remove_x_line_above(4)
            return current_user, None
        else:
            current_user = utils.copy_array(user_data[user_index])
            print(f"Anda telah login dengan user {current_user[1]}")
            time.sleep(1)
            utils.remove_x_line_above(4)
            return current_user,user_id
        

def logout(current_user):
    if utils.is_empty(current_user):
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
        time.sleep(1)
        utils.remove_x_line_above(3)
    else:
        print(f"Anda keluar dari akun {current_user[1]}")
        time.sleep(1)
        utils.remove_xth_line_above(1)
        current_user = []
    
    return current_user, ''