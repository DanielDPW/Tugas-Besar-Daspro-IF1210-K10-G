import time
from typing import *

from . import utils
from . import inventory
from . import battle
from .types import *

def print_healing_fountain():
    print("""
██░░░██░▄█████░▄████▄░██░░░░░██████░██████▄░▄██████░░░██████░▄█████▄░██░░░██░██████▄░████████░▄████▄░██████░██████▄
██░░░██░██░░░░░██░░██░██░░░░░░░██░░░██░░░██░██░░░░░░░░██░░░░░██░░░██░██░░░██░██░░░██░░░░██░░░░██░░██░░░██░░░██░░░██
███████░█████░░██░░██░██░░░░░░░██░░░██░░░██░██░░███░░░█████░░██░░░██░██░░░██░██░░░██░░░░██░░░░██░░██░░░██░░░██░░░██
██░░░██░██░░░░░██████░██░░░░░░░██░░░██░░░██░██░░░██░░░██░░░░░██░░░██░██░░░██░██░░░██░░░░██░░░░██████░░░██░░░██░░░██
██░░░██░▀█████░██░░██░██████░██████░██░░░██░▀█████▀░░░██░░░░░▀█████▀░▀█████▀░██░░░██░░░░██░░░░██░░██░██████░██░░░██
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
""")
    
def healingfountain(current_user : Array, user_id : str, user_data : Matrix, monster_inventory_data : Matrix, monster_data : Matrix) -> Tuple[Matrix, Matrix]:
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
        utils.clear_terminal()
        print_healing_fountain()
        user_index = utils.find_row(utils.slice_matrix(user_data, row_start = 1), 0, user_id) + 1
        print(f"Jumlah OWCA Coins Anda sekarang adalah {user_data[user_index][4]}")
        monster_dict = inventory.load_user_monsters(user_id, monster_inventory_data, monster_data)
        can_heal = False
        count = 0
        for monster in monster_dict:
            if monster['hp'] != monster['max_hp']:
                can_heal = True
                count = count + 1
        if not can_heal:
            print("Monster Anda tidaklah terluka")
        else:
            price = int(count * 25)
            while True:
                prompt = utils.strip(input(f"Apakah Anda mau membayar {price} untuk menyembuhkan semua monster Anda (y/n): "))
                if prompt.lower() == 'y':
                    if int(user_data[user_index][4]) >= price:
                        user_data[user_index][4] = str(int(user_data[user_index][4]) - price)
                        for monster in monster_dict:
                            if monster['hp'] != monster['max_hp']:
                                monster['hp'] = monster['max_hp']
                        print("Monster Anda telah disembuhkan")
                        monster_inventory_data = battle.update_monster_inventory_data(user_id,monster_dict, monster_inventory_data)
                        break
                    else:
                        print("OC Anda tidak cukup")
                        break
                elif prompt.lower() == 'n':
                    break
                else:
                    print("Masukkan input yang valid")
                    time.sleep(1)
                    utils.remove_x_line_above(2)
        time.sleep(1)
        utils.clear_terminal()
        return monster_inventory_data, user_data
