import time

from . import utils
from . import shop

def print_shop_management():
    print("""
▄██████░██░░░██░▄█████▄░█████▄░░░▄██▄▄██▄░▄████▄░██████▄░▄████▄░▄██████░▄█████░▄██▄▄██▄░▄█████░██████▄░████████
██░░░░░░██░░░██░██░░░██░██░░██░░░██░██░██░██░░██░██░░░██░██░░██░██░░░░░░██░░░░░██░██░██░██░░░░░██░░░██░░░░██░░░
▀█████▄░███████░██░░░██░█████▀░░░██░██░██░██░░██░██░░░██░██░░██░██░░███░█████░░██░██░██░█████░░██░░░██░░░░██░░░
░░░░░██░██░░░██░██░░░██░██░░░░░░░██░██░██░██████░██░░░██░██████░██░░░██░██░░░░░██░██░██░██░░░░░██░░░██░░░░██░░░
██████▀░██░░░██░▀█████▀░██░░░░░░░██░██░██░██░░██░██░░░██░██░░██░▀█████▀░▀█████░██░██░██░▀█████░██░░░██░░░░██░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
""")
def shop_management(current_user,item_shop_data, monster_shop_data, monster_data):
    if utils.is_empty(current_user):
        print("Anda belum login")
        time.sleep(1)
        utils.remove_x_line_above(2)
        return item_shop_data, monster_shop_data
    elif utils.strip(current_user[3]) != 'admin':
        print("Anda bukan Admin")
        time.sleep(1)
        utils.remove_x_line_above(2)
        return item_shop_data, monster_shop_data
    else:
        utils.clear_terminal()
        print_shop_management()
        item_shop_dict = shop.load_item_shop(item_shop_data)
        monster_shop_dict = shop.load_monster_shop(monster_shop_data,monster_data)
        while True:
            prompt = utils.strip(input("Pilih aksi (lihat/tambah/ubah/hapus/keluar): "))
            if prompt == 'lihat':
                shop.look(item_shop_dict,monster_shop_dict)
            elif prompt == 'tambah':
                item_shop_data, item_shop_dict, monster_shop_data, monster_shop_dict = add(item_shop_data, monster_shop_data, monster_data, item_shop_dict,monster_shop_dict)
            elif prompt == 'ubah':
                item_shop_data, item_shop_dict, monster_shop_data, monster_shop_dict = change(item_shop_data, monster_shop_data, item_shop_dict, monster_shop_dict)
            elif prompt == 'hapus':
                item_shop_data, item_shop_dict, monster_shop_data, monster_shop_dict = remove(item_shop_data,item_shop_dict,monster_shop_data,monster_shop_dict)
            elif prompt == 'keluar':
                utils.clear_terminal()
                return item_shop_data, monster_shop_data

def add(item_shop_data, monster_shop_data, monster_data, item_shop_dict,monster_shop_dict):
    while True:
        prompt = utils.strip(input("Mau menambah apa? (item/monster): "))
        if prompt == "item":
            item_shop_data, item_shop_dict = add_item(item_shop_data, item_shop_dict)
            break
        elif prompt == "monster":
            monster_shop_data, monster_shop_dict = add_monster(monster_shop_data, monster_data, monster_shop_dict)
            break
        else:
            print("Masukkan input yang valid")
            time.sleep(1)
            utils.remove_x_line_above(2)
    return item_shop_data, item_shop_dict, monster_shop_data, monster_shop_dict

def add_item(item_shop_data, item_shop_dict):
    unadded_item_dict = load_unadded_item(item_shop_dict)
    print(unadded_item_dict)
    item_ids = [unadded_item_dict[i]['id'] for i in range(len(unadded_item_dict))]
    for row in unadded_item_dict:
        if row['type'] == 'strength':
            item_name = 'Strength Potion'
        elif row['type'] == 'speed':
            item_name = 'Speed Potion'
        elif row['type'] == 'resilience':
            item_name = 'Resilience Potion'
        elif row['type'] == 'healing':
            item_name = 'Healing Potion'
        elif row['type'] == 'monsterball':
            item_name = 'Monster Ball'
        print(f"{row['id']} {item_name}")
    item_id,stock,price = add_input_id_stock_price(item_ids)
    while True:
        prompt = utils.strip(input("Tambahkan Item ke shop? (Y/N): "))
        if prompt.lower() == 'y':
            utils.remove_x_line_above(2)
            index = utils.find_dict_index(unadded_item_dict,'id', item_id)
            if unadded_item_dict[index]['type'] == 'strength':
                item_name = 'Strength Potion'
            elif unadded_item_dict[index]['type'] == 'speed':
                item_name = 'Speed Potion'
            elif unadded_item_dict[index]['type'] == 'resilience':
                item_name = 'Resilience Potion'
            elif unadded_item_dict[index]['type'] == 'healing':
                item_name = 'Healing Potion'
            elif unadded_item_dict[index]['type'] == 'monsterball':
                item_name = 'Monster Ball'
            print(f"{item_name} telah berhasil ditambahkan ke dalam shop!")
            time.sleep(1)
            break
        elif prompt.lower() == 'n':
            break
        else:
            print("Masukkan input yang valid")
            time.sleep(1)
            utils.remove_x_line_above(2)
    utils.clear_terminal()
    print_shop_management()
    item_shop_data.append([unadded_item_dict[index]['type'],stock,price])
    item_shop_dict = shop.load_item_shop(item_shop_data)
    return item_shop_data, item_shop_dict

def add_input_id_stock_price(ids):
    while True:
        prompt = utils.strip(input("Masukkan ID: "))
        if prompt not in ids:
            print("Masukkan ID yang valid")
            time.sleep(1)
            utils.remove_x_line_above(2)
        else:
            break
    id = prompt
    while True:
        prompt = utils.strip(input(f"Masukkan stok: "))
        if not utils.is_int(prompt):
            print("Masukkan input bertipe Integer, coba lagi!")
            time.sleep(1)
            utils.remove_x_line_above(2)
        elif int(prompt) < 0:
            print("Stok tidak bisa kurang dari 0.")
            time.sleep(1)
            utils.remove_x_line_above(2)
        else:
            break
    stock = prompt
    while True:
        prompt = utils.strip(input(f"Masukkan harga: "))
        if not utils.is_int(prompt):
            print("Masukkan input bertipe Integer, coba lagi!")
            time.sleep(1)
            utils.remove_x_line_above(2)
        elif int(prompt) < 0:
            print("Harga tidak bisa kurang dari 0.")
            time.sleep(1)
            utils.remove_x_line_above(2)
        else:
            break
    price = prompt
    return id, stock, price

def add_monster(monster_shop_data, monster_data, monster_shop_dict):
    unadded_monster_dict = load_unadded_monster(monster_shop_dict,monster_data)
    monster_ids = [unadded_monster_dict[i]['id'] for i in range(len(unadded_monster_dict))]
    print(f"{'ID':<10}{'Type':<20}{'ATK Power':<10}{'DEF Power':<10}{'HP':<10}{'Speed':<10}")
    for row in unadded_monster_dict:
        print(f"{row['id']:<10} {row['type']:<20} {row['atk_power']:<10} {row['def_power']:<10} {row['hp']:<10} {row['speed']:<10}")
    monster_id,stock,price = add_input_id_stock_price(monster_ids)
    while True:
        prompt = utils.strip(input("Tambahkan Monster ke shop? (Y/N): "))
        if prompt.lower() == 'y':
            utils.remove_xth_line_above(1)
            index = utils.find_dict_index(unadded_monster_dict,'id', monster_id)
            print(f"{unadded_monster_dict[index]['type']} telah berhasil ditambahkan ke dalam shop!")
            time.sleep(1)
            break
        elif prompt.lower() == 'n':
            break
        else:
            print("Masukkan input yang valid")
            time.sleep(1)
            utils.remove_x_line_above(2)
    utils.clear_terminal()
    print_shop_management()
    monster_shop_data.append([monster_id,stock,price])
    monster_shop_dict = shop.load_monster_shop(monster_shop_data,monster_data)
    return monster_shop_data, monster_shop_dict

def load_unadded_monster(monster_shop_dict,monster_data):
    unadded_monster_dict = []

    for row in utils.slice_matrix(monster_data,row_start = 1):
        if not utils.is_in_dict(monster_shop_dict, 'id',row[0]):
            monster_id, monster_type,atk_power, def_power, hp, speed = row[0], row[1], row[2], row[3], row[4], row[5]
            monster = {'type' : monster_type, 'id' : monster_id, 'atk_power'  : atk_power, 'def_power' : def_power, 'hp' : hp, 'speed' : speed}
            unadded_monster_dict.append(monster)
    return unadded_monster_dict

def load_unadded_item(item_shop_dict):
    unadded_item_dict = []
    item_list = ['strength', 'speed', 'resilience', 'healing', 'monsterball']

    for i in range(5):
        item_id = str(i + 1)
        if not utils.is_in_dict(item_shop_dict, 'id', item_id):
            for type in item_list:
                if not utils.is_in_dict(item_shop_dict, 'type', type):
                    unadded_item_dict.append({'id': item_id, 'type': type})
                    item_list = utils.remove_value(item_list, type)
                    break

    return unadded_item_dict

def change(item_shop_data, monster_shop_data, item_shop_dict,monster_shop_dict):
    while True:
        prompt = utils.strip(input("Mau ubah apa? (item/monster): "))
        if prompt == "item":
            item_shop_data, item_shop_dict = edit('item', item_shop_data, item_shop_dict)
            break
        elif prompt == "monster":
            monster_shop_data, monster_shop_dict = edit('monster', monster_shop_data, monster_shop_dict)
            break
        else:
            print("Masukkan input yang valid")
            time.sleep(1)
            utils.remove_x_line_above(2)
    return item_shop_data, item_shop_dict, monster_shop_data, monster_shop_dict

def edit_input_id_stock_price(ids):
    while True:
        prompt = utils.strip(input("Masukkan ID: "))
        if prompt not in ids:
            print("Masukkan ID yang valid")
            time.sleep(1)
            utils.remove_x_line_above(2)
        else:
            break
    id = prompt
    while True:
        prompt = utils.strip(input(f"Masukkan stok: "))
        if utils.is_space(prompt):
            break
        elif not utils.is_int(prompt):
            print("Masukkan input bertipe Integer, coba lagi!")
            time.sleep(1)
            utils.remove_x_line_above(2)
        elif int(prompt) < 0:
            print("Stok tidak bisa kurang dari 0.")
            time.sleep(1)
            utils.remove_x_line_above(2)
        else:
            break
    stock = prompt
    while True:
        prompt = utils.strip(input(f"Masukkan harga: "))
        if utils.is_space(prompt):
            break
        elif not utils.is_int(prompt):
            print("Masukkan input bertipe Integer, coba lagi!")
            time.sleep(1)
            utils.remove_x_line_above(2)
        elif int(prompt) < 0:
            print("Harga tidak bisa kurang dari 0.")
            time.sleep(1)
            utils.remove_x_line_above(2)
        else:
            break
    price = prompt
    return id, stock, price

def edit(shop_type : str, shop_data, shop_dict):
    ids = [shop_dict[i]['id'] for i in range(len(shop_dict))]
    if shop_type == 'item':
        shop.look_item(shop_dict)
    elif shop_type == 'monster':
        shop.look_monster(shop_dict)
    while True:
        id,stock,price = edit_input_id_stock_price(ids)
        if utils.is_empty(stock) and utils.is_empty(price):
            print("Tidak ada perubahan")
            time.sleep(1)
            utils.remove_x_line_above(2)
        else:
            break
    while True:
        prompt = utils.strip(input("Konfirmasi perubahan? (Y/N): "))
        if prompt.lower() == 'y':
            utils.remove_x_line_above(1)
            index = utils.find_dict_index(shop_dict,'id', id)
            if shop_type == "item":
                if shop_dict[index]['type'] == 'strength':
                    item_name = 'Strength Potion'
                elif shop_dict[index]['type'] == 'speed':
                    item_name = 'Speed Potion'
                elif shop_dict[index]['type'] == 'resilience':
                    item_name = 'Resilience Potion'
                elif shop_dict[index]['type'] == 'healing':
                    item_name = 'Healing Potion'
                elif shop_dict[index]['type'] == 'monsterball':
                    item_name = 'Monster Ball'
                print(
    f"{item_name} telah berhasil diubah dengan"
    f"{f' stok baru sejumlah {stock}' if stock != '' and stock != shop_dict[index]['stock'] else ''}"
    f"{' dan' if price != '' and price != shop_dict[index]['price'] and stock != '' and stock != shop_dict[index]['stock'] else ''}"
    f"{f' harga baru {price}' if price != '' and price != shop_dict[index]['price'] else ''}"
)
            elif shop_type == "monster":
                print(
    f"{shop_dict[index]['type']} telah berhasil diubah dengan"
    f"{f' stok baru sejumlah {stock}' if stock != '' and stock != shop_dict[index]['stock'] else ''}"
    f"{' dan' if price != '' and price != shop_dict[index]['price'] and stock != '' and stock != shop_dict[index]['stock'] else ''}"
    f"{f' harga baru {price}' if price != '' and price != shop_dict[index]['price'] else ''}"
)
            shop_dict[index]['stock'] = stock
            shop_dict[index]['price'] = price
            break
        elif prompt.lower() == 'n':
            break
        else:
            print("Masukkan input yang valid")
            time.sleep(1)
            utils.remove_x_line_above(2)
    utils.clear_terminal()
    print_shop_management()
    shop_data = shop.update_shop_data(shop_data, shop_dict, shop_type)
    return shop_data, shop_dict

def remove(item_shop_data, item_shop_dict, monster_shop_data, monster_shop_dict):
    while True:
        prompt = utils.strip(input("Mau hapus apa? (item/monster): "))
        if prompt == "item":
            item_shop_data, item_shop_dict = delete('item',item_shop_data,item_shop_dict)
            break
        elif prompt == "monster":
            monster_shop_data, monster_shop_dict = delete('monster',monster_shop_data,monster_shop_dict)
            break
        else:
            print("Masukkan input yang valid")
            time.sleep(1)
            utils.remove_x_line_above(2)
    return item_shop_data, item_shop_dict, monster_shop_data, monster_shop_dict

def delete(shop_type,shop_data,shop_dict):
    ids = [shop_dict[i]['id'] for i in range(len(shop_dict))]
    if shop_type == 'item':
        shop.look_item(shop_dict)
    elif shop_type == 'monster':
        shop.look_monster(shop_dict)
    while True:
        prompt = utils.strip(input("Masukkan ID: "))
        if prompt not in ids:
            print("Masukkan input yang valid")
            time.sleep(1)
            utils.remove_x_line_above(2)
        else:
            break
    id = prompt
    while True:
        prompt = utils.strip(input("Apakah Anda yakin? (Y/N): "))
        if prompt.lower() == 'y':
            utils.remove_x_line_above(1)
            index =  utils.find_dict_index(shop_dict,'id',id)
            if shop_type == "item":
                if shop_dict[index]['type'] == 'strength':
                    item_name = 'Strength Potion'
                elif shop_dict[index]['type'] == 'speed':
                    item_name = 'Speed Potion'
                elif shop_dict[index]['type'] == 'resilience':
                    item_name = 'Resilience Potion'
                elif shop_dict[index]['type'] == 'healing':
                    item_name = 'Healing Potion'
                elif shop_dict[index]['type'] == 'monsterball':
                    item_name = 'Monster Ball'
                print(f"{item_name} telah dihapus dari shop!")
            elif shop_type == "monster":
                print(f"{shop_dict[index]['type']} telah dihapus dari shop!")
            time.sleep(1)
            break
        elif prompt.lower() == 'n':
            break
        else:
            print("Masukkan input yang valid")
            time.sleep(1)
            utils.remove_x_line_above(2)
    utils.clear_terminal()
    print_shop_management()
    if shop_type == 'item':
        shop_data = utils.remove_row(shop_data,index = 0, element = shop_dict[index]['type'])
        shop_dict = shop.load_item_shop(shop_data)
    elif shop_type == 'monster':
        shop_data = utils.remove_row(shop_data,index = 0, element = id)
        shop_dict = shop.load_monster_shop(shop_data,shop_dict)
    return shop_data, shop_dict


