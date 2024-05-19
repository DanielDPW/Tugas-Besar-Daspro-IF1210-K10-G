import time

from . import utils
from . import inventory

def print_laboratory():
    print("""
██░░░░░▄████▄░█████▄░▄█████▄░█████▄░▄████▄░████████░▄█████▄░█████▄░██░░██
██░░░░░██░░██░██░░██░██░░░██░██░░██░██░░██░░░░██░░░░██░░░██░██░░██░██░░██
██░░░░░██░░██░█████░░██░░░██░█████▀░██░░██░░░░██░░░░██░░░██░█████▀░▀████▀
██░░░░░██████░██░░██░██░░░██░██░░██░██████░░░░██░░░░██░░░██░██░░██░░░██░░
██████░██░░██░█████▀░▀█████▀░██░░██░██░░██░░░░██░░░░▀█████▀░██░░██░░░██░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
""")

def laboratory(current_user, user_id, monster_inventory_data, monster_data, user_data):
    if utils.is_empty(current_user):
        print("Anda belum login")
        time.sleep(1)
        utils.remove_x_line_above(2)
        return monster_inventory_data, user_data
    elif utils.strip(current_user[3]) != 'agent':
        print("Anda bukan Agent")
        time.sleep(1)
        utils.remove_x_line_above(2)
        return monster_inventory_data, user_data
    else:
        print_laboratory()
        while True:
            user_index = utils.find_row(utils.slice_matrix(user_data, row_start = 1), 0, user_id) + 1
            user_oc = user_data[user_index][4]
            print(f"Jumlah OWCA Coins Anda sekarang: {user_oc}")
            monster_dict = inventory.load_user_monsters(user_id,monster_inventory_data,monster_data)
            print(f"{'No.':<4}{'Name':<20}{'Type':<20}{'Level':<10}{'HP':<10}")
            for i, monster in enumerate(monster_dict):
                print(f"{i + 1:<4}{utils.title(monster['name']):<20}{monster['type']:<10}{monster['level']:<10}{monster['hp']}/{monster['max_hp']}")
            options = [str(i + 1) for i in range(len(monster_dict))]
            print("Upgrade Price")
            print("Level 1 -> Level 2: 300 OC")
            print("Level 2 -> Level 3: 500 OC")
            print("Level 3 -> Level 4: 700 OC")
            print("Level 4 -> Level 5: 900 OC")
            while True:
                a = utils.strip(input("Pilih monster atau x untuk keluar:"))
                if a in options:
                    monster_inventory_data,user_data = level_up(user_oc,user_index,user_id,user_data,monster_dict,monster_inventory_data,monster_data,a)
                    break
                elif a == 'x':
                    utils.clear_terminal()
                    return monster_inventory_data, user_data
                else:
                    print("Masukkan input yang valid")
                    time.sleep(1)
                    utils.remove_x_line_above(2)

def level_up(user_oc, user_index, user_id, user_data, monster_dict, monster_inventory_data,monster_data,index):
    index = int(index) - 1
    monster = monster_dict[index]
    if int(monster['level']) >= 5:
        print("Maaf, monster yang Anda pilih sudah memiliki level maksimum")
        time.sleep(1)
        utils.clear_terminal()
    else:
        price = 300 + 200 * (int(monster['level'])-1)
        print(f"{monster['name']} akan diupgrade ke level {monster['level'] + 1}.")
        print(f"Harga untuk melakukan upgrade {monster['name']} adalah {price}")
        while True:
            prompt = utils.strip(input("Lanjutkan upgrade? (Y/N) "))
            if prompt.lower() == 'y':
                utils.remove_xth_line_above(1)
                if int(user_oc) >= price:
                    user_data[user_index][4] = str(int(user_data[user_index][4]) - price)
                    monster['level'] = str(int(monster['level']) + 1)
                    monster_inventory_data = change_level(user_id,monster,monster_inventory_data,monster_data)
                    print(f"Selamat, {monster['name']} berhasil diupgrade ke level ke level {monster['level']}")
                    break
                else:
                    print("OC Anda tidak cukup")
                time.sleep(1)
            elif prompt.lower() == 'n':
                break
            else:
                print("Masukkan input yang valid")
                time.sleep(1)
                utils.remove_x_line_above(2)
        utils.clear_terminal()
        print_laboratory()
    return monster_inventory_data,user_data

def change_level(user_id, monster, monster_inventory_data,monster_data):
    max_hp = int((1 + 0.1 *(int(monster['level']) - 1)) * int(monster_data[utils.find_row(monster_data,index = 0, element = monster['id'])][4]))
    for i in monster_inventory_data:
        if i[0] == user_id and i[3] == monster['name']:
            i[2] = monster['level']
            i[4] = str(max_hp)
            return monster_inventory_data
    return monster_inventory_data