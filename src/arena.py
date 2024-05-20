import time
from typing import *

from . import utils
from . import battle
from .types import *

def arena(current_user : Array, user_data : Matrix, user_id : str, monster_inventory_data : Matrix, item_inventory_data : Matrix, monster_data : Matrix) -> Tuple[Matrix,Matrix]:
    total_damage_dealt = 0
    total_damage_taken = 0
    stage_cleared = 0

    # Cek apakah user sudah login atau merupakan agen
    if utils.is_empty(current_user):
        print("Anda belum login")
        time.sleep(1)
        utils.remove_x_line_above(2)
        return item_inventory_data,monster_inventory_data
    elif utils.strip(current_user[3]) != 'agent':
        print("Anda bukan Agent")
        time.sleep(1)
        utils.remove_x_line_above(2)
        return item_inventory_data,monster_inventory_data
    else:
        utils.clear_terminal()
        for i in range(5):
            print(f"Stage {i + 1}") # Print nomor stage
            time.sleep(2)
            monster_level = i + 1
            damage_dealt, damage_taken, victory,item_inventory_data,monster_inventory_data = battle.battle(current_user, monster_level, user_data, user_id, monster_inventory_data, item_inventory_data, monster_data, True)
            total_damage_dealt = total_damage_dealt + damage_dealt
            total_damage_taken = total_damage_taken + damage_taken
            if not victory:
                break
            else:
                stage_cleared = stage_cleared + 1
        
        # Hitung reward
        if stage_cleared == 0:
            reward = 0
        else:
            reward = 50 * (2 ** (stage_cleared - 1))

        # Update OC user
        user_index = utils.find_row(user_data, index = 0, element = user_id)
        user_data[user_index][4] = str(int(user_data[user_index][4]) + int(reward))

        # Print hasil
        print(f"Total damage dealt : {total_damage_dealt}")
        print(f"Total damage taken : {total_damage_taken}")
        print(f"Stage cleared: {stage_cleared}")
        if reward > 0:
            print(f"Anda mendapat reward {reward} OWCA Coins")
        else:
            print("Anda tidak mendapat OWCA Coins")
        time.sleep(3)
        utils.clear_terminal()
        return item_inventory_data,monster_inventory_data