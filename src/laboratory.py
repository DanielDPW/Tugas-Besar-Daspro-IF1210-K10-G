from . import utils
from . import inventory

def laboratory(user_id, monster_inventory_data, monster_data, user_data):
    while True:
        print("Laboratory")
        user_index = utils.find_row(utils.slice_matrix(user_data, row_start = 1), 0, user_id) + 1
        user_oc = user_data[user_index][4]
        print(f"Jumlah OWCA Coins Anda sekarang: {user_oc}")
        monster_dict = inventory.load_user_monsters(user_id,monster_inventory_data,monster_data)
        for i, monster in enumerate(monster_dict):
            print(f"{i + 1}. {(monster['name']).title()} (Type: {monster['type']} Level: {monster['level']} HP: {monster['hp']}/{monster['max_hp']}")
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
                return monster_inventory_data, user_data

def level_up(user_oc, user_index, user_id, user_data, monster_dict, monster_inventory_data,monster_data,index):
    index = int(index) - 1
    monster = monster_dict[index]
    if int(monster['level']) >= 5:
        print("Maaf, monster yang Anda pilih sudah memiliki level maksimum")
    else:
        price = 300 + 200 * (int(monster['level'])-1)
        print(f"{monster['name']} akan diupgrade ke level {monster['level'] + 1}.")
        print(f"Harga untuk melakukan upgrade {monster['name']} adalah {price}")
        while True:
            x = utils.strip(input("Lanjutkan upgrade? (Y/N) "))
            if x.lower() == 'y':
                if int(user_oc) >= price:
                    user_data[user_index][4] = str(int(user_data[user_index][4]) - price)
                    monster['level'] = str(int(monster['level']) + 1)
                    monster_inventory_data = change_level(user_id,monster,monster_inventory_data,monster_data)
                    print(f"Selamat, {monster['name']} berhasil diupgrade ke level ke level {monster['level']}")
                    break
                else:
                    print("OC Anda tidak cukup")
            elif x.lower() == 'n':
                break
            else:
                print("Invalid")
    return monster_inventory_data,user_data

def change_level(user_id, monster, monster_inventory_data,monster_data):
    max_hp = int((1 + 0.1 *(int(monster['level']) - 1)) * int(monster_data[utils.find_row(monster_data,index = 0, element = monster['id'])][4]))
    for i in monster_inventory_data:
        if i[0] == user_id and i[3] == monster['name']:
            i[2] = monster['level']
            i[4] = str(max_hp)
            return monster_inventory_data
    return monster_inventory_data