from . import utils

def get_user_monsters(user_id : str, monster_inventory_data):
    user_monsters = []
    monster_inventory = utils.slice_matrix(monster_inventory_data, row_start = 1)
    int_data = ['level','hp']

    for row in monster_inventory:
        if user_id == row[0]:
            for i in range(len(row)):
                if monster_inventory_data[0][i] in int_data:
                    row[i] = int(row[i])
            user_monsters.append(row)
    
    return user_monsters

def load_user_monsters(user_id, monster_inventory_data, monster_data):
    monster_dict = []
    user_monsters = get_user_monsters(user_id, monster_inventory_data)

    for row in user_monsters:
        monster_index = utils.find_row(monster_data, index = 0, element = row[1])
        if int(row[4]) > 0:
            monster_id = row[1]
            monster_level = row[2]
            monster_name = row[3]
            type = monster_data[monster_index][1]
            atk_power = int(int(monster_data[monster_index][2]) * (1 + (monster_level - 1) * 0.1))
            def_power = min(int(int(monster_data[monster_index][3]) * (1 + (monster_level - 1) * 0.1)), 50)
            hp = int(row[4])
            max_hp = int(int(monster_data[monster_index][4]) * (1 + (monster_level - 1) * 0.1))
            speed = min(int(int(monster_data[monster_index][5]) * (1 + (monster_level - 1) * 0.1)), 50)

            user_monster = {'name' : monster_name, 'type' : type, 'id' : monster_id, 'level' : monster_level, 'atk_power'  : atk_power, 'def_power' : def_power, 'hp' : hp, 'max_hp' : max_hp, 'speed' : speed}
            monster_dict.append(user_monster)
        
    return monster_dict

def get_user_inventory(user_id : str, item_inventory_data):
    user_items = []
    item_inventory = utils.slice_matrix(item_inventory_data, row_start = 1)
    int_data = ['quantity']

    for row in item_inventory:
        if user_id == row[0]:
            for i in range(len(row)):
                if item_inventory_data[0][i] in int_data:
                    if row[i] > int('0'):
                        row[i] = int(row[i])
            user_items.append(row)
    
    return user_items

def name_monster(user_id, monster_inventory_data):
    valid_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    user_monsters = get_user_monsters(user_id,monster_inventory_data)
    used_name = [user_monsters[i][3] for i in range(len(user_monsters))]
    while True:
        name = input("Nama monster: ")
        if len(name) == 0 or utils.is_space(name):
            print("Name tidak boleh kosong")
        elif name in used_name:
            print("Nama sudah Anda pakai")
        else:
            contains_invalid_char = False
            for char in name:
                if char not in valid_characters:
                    contains_invalid_char = True
            if contains_invalid_char:
                print("Name hanya berupa alfabet")
            else:
                return name
            
def show_items(user_id, user_data, user_items):
    print(f"Inventory (User ID: {user_id})")
    user_index = utils.find_row(utils.slice_matrix(user_data, row_start = 1), 0, user_id)
    print(f"Jumlah OWCA Coins Anda sekarang: {user_data[user_index][4]}")
    for i, user_item in enumerate(user_items):
        print(f"{i + 1}. {(user_item[1]).title()} {user_item[2]}")

def show_monsters(user_id, monster_inventory_data, monster_data, user_data):
    print(f"Inventory (User ID: {user_id})")
    user_index = utils.find_row(utils.slice_matrix(user_data, row_start = 1), 0, user_id)
    print(f"Jumlah OWCA Coins Anda sekarang: {user_data[user_index][4]}")
    monster_dict = load_user_monsters(user_id,monster_inventory_data,monster_data)
    for i, monster in enumerate(monster_dict):
        print(f"{i + 1}. {(monster['name']).title()} (Type: {monster['type']} Level: {monster['level']} HP: {monster['hp']}/{monster['max_hp']}")