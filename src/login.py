from . import utils

def login(user_data, current_user):
    if not utils.is_empty(current_user):
        print(f"Anda telah login dengan username {current_user[1]}, silahkan lakukan 'LOGOUT' sebelum melakukan register.")
        return current_user, None
    else:
        while True:
            username = input("Masukkan username: ")
            if utils.is_space(username):
                print("Username tidak boleh kosong")
            else:
                break
        while True:
            password = input("Masukkan password: ")
            if utils.is_space(password):
                print("Password tidak boleh kosong")
            else:
                break
        user_id = utils.find_row(utils.slice_matrix(user_data, row_start = 1), 1, username) + 1

        if not utils.is_in_column(utils.slice_matrix(user_data, row_start = 1), 1, username):
            print(f"Username tidak terdaftar!")
            return current_user, None
        elif not utils.is_in_row(user_data[user_id], 2, password):
            print("Password salah!")
            return current_user, None
        else:
            current_user = utils.copy_array(user_data[user_id])
            print(f"Anda telah login dengan user {current_user[1]}")
            return current_user,current_user[0]
        

def logout(current_user):
    if utils.is_empty(current_user):
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
    else:
        current_user = []
    
    return current_user, ''