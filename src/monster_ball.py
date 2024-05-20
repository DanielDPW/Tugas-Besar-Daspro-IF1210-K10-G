import time
from typing import *

from . import rng
from . import inventory
from . import utils
from .types import *

def catch(user_id : str,enemy : Dictionary, monster_inventory_data : Matrix):
    odds = rng.rng(1,100) # Mencari angka dari 1-100
    
    # Makin renadah hp musuh, makin tinggi peluang menangkapnya
    if enemy['level'] == 1:
        if odds < int((1-(enemy['hp']/enemy['max_hp'])) * 75):
            print("Monster berhasil ditangkap")
            name = inventory.name_monster(user_id,monster_inventory_data)
            monster_inventory_data.append([user_id, enemy['id'], enemy['level'], name, enemy['hp']])
            enemy['hp'] = 0
        else:
            print("Monster lepas dari Monster Ball")
    elif enemy['level'] == 2:
        if odds < int((1-(enemy['hp']/enemy['max_hp'])) * 50):
            print("Monster berhasil ditangkap")
            name = inventory.name_monster(user_id,monster_inventory_data)
            monster_inventory_data.append([user_id, enemy['id'], enemy['level'], name, enemy['hp']])
            enemy['hp'] = 0
        else:
            print("Monster lepas dari Monster Ball")
    elif enemy['level'] == 3:
        if odds < int((1-(enemy['hp']/enemy['max_hp'])) * 25):
            print("Monster berhasil ditangkap")
            name = inventory.name_monster(user_id,monster_inventory_data)
            monster_inventory_data.append([user_id, enemy['id'], enemy['level'], name, enemy['hp']])
            enemy['hp'] = 0
        else:
            print("Monster lepas dari Monster Ball")
    elif enemy['level'] == 4:
        if odds < int((1-(enemy['hp']/enemy['max_hp'])) * 10):
            print("Monster berhasil ditangkap")
            name = inventory.name_monster(user_id,monster_inventory_data)
            monster_inventory_data.append([user_id, enemy['id'], enemy['level'], name, enemy['hp']])
            enemy['hp'] = 0
        else:
            print("Monster lepas dari Monster Ball")
    elif enemy['level'] == 5:
        if odds < int((1-(enemy['hp']/enemy['max_hp'])) * 5):
            print("Monster berhasil ditangkap")
            name = inventory.name_monster(user_id,monster_inventory_data)
            monster_inventory_data.append([user_id, enemy['id'], enemy['level'], name, enemy['hp']])
            enemy['hp'] = 0
        else:
            print("Monster lepas dari Monster Ball")

def monster_ball(user_id : str, enemy : Dictionary, user_items : Matrix, monster_inventory_data : Matrix) -> bool:
    monster_ball_index = utils.find_row(user_items, 1, 'monsterball') # Cari index monster ball di inventory
    if monster_ball_index != -1 and user_items[monster_ball_index][2] > 0:
        print(f"Monster Ball (Quantity: {user_items[monster_ball_index][2]})") # Print jumlah monster ball
        while True:
            x = utils.strip(input("Catch? (Y/N) "))
            if x.lower() == 'y':
                print("Kamu melempar Monster Ball")
                user_items[monster_ball_index][2] = user_items[monster_ball_index][2] - 1
                time.sleep(1)
                utils.remove_x_line_above(3)
                time.sleep(3)
                catch(user_id,enemy,monster_inventory_data)
                return True
            elif x.lower() == 'n':
                utils.remove_x_line_above(2)
                return False
            else:
                print("Masukkan input yang valid")
                time.sleep(1)
                utils.remove_x_line_above(2)
    else:
        print("Anda tidak memiliki monster ball")
        time.sleep(1)
        utils.remove_x_line_above(1)
        return False