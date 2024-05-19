import time

from . import utils
from . import inventory

def print_shop():
    print("""
▄██████░██░░░██░▄█████▄░█████▄
██░░░░░░██░░░██░██░░░██░██░░██
▀█████▄░███████░██░░░██░█████▀
░░░░░██░██░░░██░██░░░██░██░░░░
██████▀░██░░░██░▀█████▀░██░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
""")

def load_monster_shop(monster_shop_data,monster_data):
    monster_shop_dict = []

    for row in utils.slice_matrix(monster_shop_data,row_start = 1):
        monster_index = utils.find_row(monster_data, index = 0, element = row[0])
        monster_id = row[0]
        monster_type = monster_data[monster_index][1]
        atk_power = monster_data[monster_index][2]
        def_power = monster_data[monster_index][3]
        hp = monster_data[monster_index][4]
        speed = monster_data[monster_index][5]
        stock = int(row[1])
        price = int(row[2])

        monster = {'type' : monster_type, 'id' : monster_id, 'atk_power'  : atk_power, 'def_power' : def_power, 'hp' : hp, 'speed' : speed, 'stock' : stock, 'price' : price}
        monster_shop_dict.append(monster)
        
    return monster_shop_dict

def load_item_shop(item_shop_data):
    item_shop_dict = []

    for i,row in enumerate(utils.slice_matrix(item_shop_data,row_start = 1)):
        item_id = str(i + 1)
        item_type = row[0]
        stock = int(row[1])
        price = int(row[2])

        item = {'id' : item_id, 'type' : item_type, 'stock' : stock, 'price' : price}
        item_shop_dict.append(item)
        
    return item_shop_dict

def shop(current_user,user_id,user_data,item_inventory_data,monster_inventory_data,item_shop_data,monster_shop_data,monster_data):
    if utils.is_empty(current_user):
        print("Anda belum login")
        time.sleep(1)
        utils.remove_x_line_above(2)
        return user_data,item_inventory_data,monster_inventory_data,item_shop_data,monster_shop_data
    elif utils.strip(current_user[3]) != 'agent':
        print("Anda bukan Agent")
        time.sleep(1)
        utils.remove_x_line_above(2)
        return user_data,item_inventory_data,monster_inventory_data,item_shop_data,monster_shop_data
    else:
        utils.clear_terminal()
        print_shop()
        user_index = utils.find_row(utils.slice_matrix(user_data, row_start = 1), 0, user_id) + 1
        item_shop_dict = load_item_shop(item_shop_data)
        monster_shop_dict = load_monster_shop(monster_shop_data,monster_data)
        while True:
            prompt = utils.strip(input("Pilih aksi (lihat/beli/keluar):"))
            if prompt == "lihat":
                look(item_shop_dict,monster_shop_dict)
            elif prompt == "beli":
                user_data, item_inventory_data, item_shop_data, item_shop_dict, monster_inventory_data, monster_shop_data, monster_shop_dict = buy(user_id,user_index, user_data,item_inventory_data,monster_inventory_data,item_shop_data, monster_shop_data, item_shop_dict,monster_shop_dict)
            elif prompt == "keluar":
                utils.clear_terminal()
                return user_data,item_inventory_data,monster_inventory_data,item_shop_data,monster_shop_data

def look(item_shop_dict,monster_shop_dict):
    while True:
        prompt = utils.strip(input("Mau lihat apa? (item/monster): "))
        if prompt == "item":
            look_item(item_shop_dict)
            return
        elif prompt == "monster":
            look_monster(monster_shop_dict)
            return

def look_item(item_shop_dict):
    utils.clear_terminal()
    print_shop()
    print(f"{'ID':<10}{'Type':<20}{'Stock':<10}{'Price':<10}")
    for item in item_shop_dict:
        if item['type'] == 'strength':
            item_name = 'Strength Potion'
        elif item['type'] == 'speed':
            item_name = 'Speed Potion'
        elif item['type'] == 'resilience':
            item_name = 'Resilience Potion'
        elif item['type'] == 'healing':
            item_name = 'Healing Potion'
        elif item['type'] == 'monsterball':
            item_name = 'Monster Ball'
        print(f"{item['id']:<10}{item_name:<20}{item['stock']:<10}{item['price']:<10}")

def look_monster(monster_shop_dict):
    utils.clear_terminal()
    print_shop()
    print(f"{'ID':<10}{'Type':<20}{'ATK Power':<10}{'DEF Power':<10}{'HP':<10}{'Speed':<10}{'Stock':<10}{'Price':<10}")
    for monster in monster_shop_dict:
        print(f"{monster['id']:<10} {monster['type']:<20}{monster['atk_power']:<10}{monster['def_power']:<10}{monster['hp']:<10}{monster['speed']:<10}{monster['stock']:<10}{monster['price']:<10}")

def buy(user_id,user_index, user_data,item_inventory_data,monster_inventory_data,item_shop_data, monster_shop_data, item_shop_dict,monster_shop_dict):
    print(f"Jumlah OWCA Coins mu sekarang adalah {user_data[user_index][4]}")
    while True:
        prompt = utils.strip(input("Mau beli apa? (item/monster): "))
        if prompt == "item":
            user_data, item_inventory_data, item_shop_data, item_shop_dict = buy_item(user_id, user_index,user_data,item_inventory_data,item_shop_data, item_shop_dict)
            break
        elif prompt == "monster":
            user_data, monster_inventory_data, monster_shop_data, monster_shop_dict = buy_monster(user_id, user_index,user_data,monster_inventory_data,monster_shop_data, monster_shop_dict)
            break
        else:
            print("Masukkan input yang valid")
            utils.remove_x_line_above(2)
    return user_data, item_inventory_data, item_shop_data, item_shop_dict, monster_inventory_data, monster_shop_data, monster_shop_dict

def buy_item(user_id, user_index,user_data,item_inventory_data,item_shop_data, item_shop_dict):
    item_ids = [item_shop_dict[i]['id'] for i in range(len(item_shop_dict))]
    if len(item_ids) != 0:
        while True:
            prompt = utils.strip(input("Masukkan ID: "))
            if prompt in item_ids:
                item_id = prompt
                break
            else:
                print("Masukkan ID yang valid")
                time.sleep(1)
                utils.remove_x_line_above(2)
        item_index = utils.find_dict_index(item_shop_dict, key = 'id' , value = item_id)
        while True:
            prompt = utils.strip(input("Masukkan jumlah item: "))
            if utils.is_digit(prompt) and int(prompt) > 0:
                if int(prompt) > item_shop_dict[item_index]['stock']:
                    print("Stock tidak cukup")
                    time.sleep(1)
                    utils.remove_x_line_above(2)
                    return user_data, item_inventory_data, item_shop_data, item_shop_dict
                elif int(prompt) * item_shop_dict[item_index]['price'] > int(user_data[user_index][4]):
                    print("OC Anda tidak cukup")
                    time.sleep(1)
                    utils.remove_x_line_above(2)
                    return user_data, item_inventory_data, item_shop_data, item_shop_dict
                else:
                    break
        amt_bought = int(prompt)
        total_price = amt_bought * item_shop_dict[item_index]['price']
        while True:
            prompt = utils.strip(input("Yakin? (Y/N): "))
            if prompt.lower() == 'y':
                print(f"Anda berhasil membeli {amt_bought} {item_shop_dict[item_index]['type']} seharga {total_price}")
                item_inventory_index = utils.find_row(item_inventory_data,1,item_shop_dict[item_index]['type'])
                if item_inventory_index != -1:
                    item_inventory_data[item_inventory_index][2] = str(int(item_inventory_data[item_inventory_index][2]) + amt_bought)
                else:
                    item_inventory_data.append([user_id,item_shop_dict[item_index]['type'],str(amt_bought)])
                user_data[user_index][4] = str(int(user_data[user_index][4]) - total_price)
                item_shop_dict[item_index]['stock'] = item_shop_dict[item_index]['stock'] - amt_bought
                utils.remove_xth_line_above(2)
                time.sleep(2)
                break
            elif prompt.lower() == 'n':
                break
            else:
                print("Masukkan input yang valid")
                time.sleep(1)
                utils.remove_x_line_above(2)
        utils.clear_terminal()
        print_shop()
        item_shop_data = update_shop_data(item_shop_data,item_shop_dict,"item")
    return user_data, item_inventory_data, item_shop_data, item_shop_dict

def buy_monster(user_id, user_index,user_data,monster_inventory_data,monster_shop_data, monster_shop_dict):
    monster_ids = [monster_shop_dict[i]['id'] for i in range(len(monster_shop_dict))]
    if len(monster_ids) != 0:
        while True:
            prompt = utils.strip(input("Masukkan ID: "))
            if prompt in monster_ids:
                monster_id = prompt
                break
            else:
                print("Masukkan ID yang valid")
                time.sleep(1)
                utils.remove_x_line_above(2)
        monster_index = utils.find_dict_index(monster_shop_dict, key = 'id' , value = monster_id)
        if monster_shop_dict[monster_index]['stock'] <= 0:
            print("Stock tidak cukup")
            time.sleep(1)
            utils.clear_terminal()
            return user_data, monster_inventory_data, monster_shop_data, monster_shop_dict
        elif int(user_data[user_index][4]) < monster_shop_dict[monster_index]['price']:
            print("OC Anda tidak cukup")
            time.sleep(1)
            utils.clear_terminal()
            return user_data, monster_inventory_data, monster_shop_data, monster_shop_dict
        else:
            while True:
                prompt = utils.strip(input("Yakin? (Y/N): "))
                if prompt.lower() == 'y':
                    utils.remove_x_line_above(2)
                    print(f"Anda berhasil membeli {monster_shop_dict[monster_index]['type']} seharga {monster_shop_dict[monster_index]['price']}")
                    monster_inventory_data.append([user_id,monster_shop_dict[monster_index]['id'],'1',inventory.name_monster(user_id,monster_inventory_data), monster_shop_dict[monster_index]['hp']])
                    user_data[user_index][4] = str(int(user_data[user_index][4]) - int(monster_shop_dict[monster_index]['price']))
                    monster_shop_dict[monster_index]['stock'] = monster_shop_dict[monster_index]['stock'] - 1
                    time.sleep(1.5)
                    break
                elif prompt.lower() == 'n':
                    break
                else:
                    print("Masukkan input yang valid")
                    time.sleep(1)
                    utils.remove_x_line_above(2)
            utils.clear_terminal()
            print_shop()
            monster_shop_data = update_shop_data(monster_shop_data,monster_shop_dict,"monster")
        return user_data, monster_inventory_data, monster_shop_data, monster_shop_dict

def update_shop_data(shop_data, shop_dict, shop_type):
    for i, row in enumerate(shop_dict):
        if shop_type == 'item':
            shop_data[i + 1][0], shop_data[i + 1][1], shop_data[i + 1][2] = row['type'], str(row['stock']), str(row['price'])
        elif shop_type == 'monster':
            shop_data[i + 1][0], shop_data[i + 1][1], shop_data[i + 1][2] = row['id'], str(row['stock']), str(row['price'])
    return shop_data