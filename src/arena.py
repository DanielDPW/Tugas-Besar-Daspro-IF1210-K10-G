from . import utils
from . import battle
from . import rng
from . import inventory

def arena(user_data, user_id, monster_inventory_data, item_inventory_data, monster_data):
    total_damage_dealt = 0
    total_damage_taken = 0
    stage_cleared = 0
    for i in range(5):
        print(f"Stage {i + 1}")
        monster_level = i + 1
        damage_dealt, damage_taken, victory,item_inventory_data,monster_inventory_data = battle.battle(monster_level, user_data, user_id, monster_inventory_data, item_inventory_data, monster_data, True)
        total_damage_dealt = total_damage_dealt + damage_dealt
        total_damage_taken = total_damage_taken + damage_taken
        if not victory:
            break
        else:
            stage_cleared = stage_cleared + 1
    reward = max(0,50 * (2 ** (stage_cleared - 1)))
    user_index = utils.find_row(user_data, index = 0, element = user_id)
    user_data[user_index][4] = str(int(user_data[user_index][4]) + reward)
    print(f"Total damage dealt : {total_damage_dealt}")
    print(f"Total damage taken : {total_damage_taken}")
    print(f"Stage cleared: {stage_cleared}")
    if reward > 0:
        print(f"Anda mendapat reward {reward} OWCA Coins")
    else:
        print("Anda tidak mendapat OWCA Coins")
    return total_damage_dealt,total_damage_taken,stage_cleared,item_inventory_data,monster_inventory_data