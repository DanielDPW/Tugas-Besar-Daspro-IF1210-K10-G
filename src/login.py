from . import arr

def login(user_data, current_user):
    if not arr.is_empty(current_user):
        print(f"Anda telah login dengan username {current_user[1]}, silahkan lakukan 'LOGOUT' sebelum melakukan register.")
    else:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        user_id = arr.find_row(arr.slice_matrix(user_data, row_start = 1), 1, username) + 1

        if not arr.is_in_column(arr.slice_matrix(user_data, row_start = 1), 1, username):
            print(f"Username tidak terdaftar!")
        elif not arr.is_in_row(user_data[user_id], 2, password):
            print("Password salah!")
        else:
            current_user = arr.copy_array(user_data[user_id])
    
    return current_user

def logout(current_user):
    if arr.is_empty(current_user):
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
    else:
        current_user = []
    
    return current_user