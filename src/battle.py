import time

from . import utils
from . import rng
from . import inventory
from . import monster_ball

def print_user_monster():
    print("""
⠀⠀⠀⡰⡏⠀⠀⠀⠀⠀⢀⣤⠛⣠⢇⠔⣇⣀⠴⠀⠀⠀⠀⠀⡤⡀⠀⠀⠀⠀
⠀⠀⠸⠥⠵⣄⡀⠀⠀⠀⢣⣹⣠⠣⠈⣀⣉⠏⠀⠆⠀⠀⠀⠀⡀⠓⡀⠀⠀⠀
⠀⠀⢰⠒⠈⡠⢈⡰⠒⠈⠉⠀⠀⠀⠀⠀⠀⠉⠘⠂⢄⡤⡖⠙⢅⠒⡇⠀⠀⠀
⠀⠀⠀⠱⡉⢠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢎⠂⠤⡰⠁⠀⠀⠀
⠀⠀⠀⠀⡨⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢦⠊⠀⠀⠀⠀⠀
⠀⠀⠀⢠⠁⢠⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠠⡦⠀⢸⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠸⡰⣘⠄⡏⢩⢆⣀⢦⣀⡶⣈⡹⠭⠽⠶⠾⠀⠘⠍⢺⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠣⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢉⣢⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠊⢹⠢⡀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⠔⠁⡆⠀⠀⠀⠉⠀⣀⠀⠄⢀⡀⠀⠀⠀⠀⠀⠀⠇⠈⠢⡀⠀⠀⠀
⠀⢀⠔⠁⠀⢰⠁⠀⠀⠀⡠⠊⠀⠀⠀⠀⠀⠑⠄⠀⠀⠀⠀⢸⠀⠀⠈⢆⠀⠀
⢀⠃⠀⠀⠀⡌⠀⠀⠀⢰⠁⠀⠀⠀⠀⠀⠀⠀⠈⢆⠀⠀⠀⠀⡇⠀⠀⠀⠢⠀
⢸⠀⠀⠀⢀⠃⠀⠀⢀⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢆⠀⠀⠀⢰⠀⠀⠀⠀⡇
⠀⠑⠤⠄⢺⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡄⠀⠀⢸⢄⠀⠀⡠⠃
⠀⠀⠀⠀⠘⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀⢸⠀⠈⠁⠀⠀
⠀⠀⠀⠀⠀⢃⠀⠀⠀⢃⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠃⠀⠀⡘⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠑⢄⠀⠀⠈⠁⠒⠂⠠⠤⠄⠒⠊⠁⠀⠀⠀⡐⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠗⠢⢄⡀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠔⠊⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠸⡀⠀⠀⢉⡱⠐⠒⠀⠈⠫⣀⣀⣀⣠⠁⠀⠀⠀⠀⠀⠀
""")
    
def print_enemy_monster():
    print("""
              ,   .-'"'=;_  ,
              |\.'-~`-.`-`;/|
              \.` '.'~-.` './
              (\`,__=-'__,'/)
           _.-'-.( d\_/b ).-'-._
         /'.-'   ' .---. '   '-.`\\
       /'  .' (=    (_)    =) '.  `\\
      /'  .',  `-.__.-.__.-'  ,'.  `\\
     (     .'.   V       V  ; '.     )
     (    |::  `-,__.-.__,-'  ::|    )
     |   /|`:.               .:'|\\   |
     |  / | `:.              :' |`\\  |
     | |  (  :.             .:  )  | |
     | |   ( `:.            :' )   | |
     | |    \\ :.           .: /    | |
     | |     \\`:.         .:'/     | |
     ) (      `\\`:.     .:'/'      ) (
     (  `)_     ) `:._.:' (     _(`  )
     \\  ' _)  .'           `.  (_ `  /
      \\  '_) /   .'"```"'.   \\ (_`  /
       `'"`  \\  (         )  /  `"'`
   ___        `.`.       .'.'        ___
 .`   ``"""'''--`_)     (_'--'''"""``   `.
(_(_(___...--'"'`         `'"'--...___)_)_)
""")

def randomize_enemy_level():
    odds = rng.rng(1,15)
    if odds == 1:
        return 5
    elif odds <= 3:
        return 4
    elif odds <= 6:
        return 3
    elif odds <= 10:
        return 2
    elif odds <= 15:
        return 1    
    
def randomize_enemy(monster_data):
    monster_ids = []

    for i in range(1, len(monster_data)):
        monster_ids.append(monster_data [i][0])
    monster_id = monster_ids[rng.rng(0, len(monster_ids) - 1)]

    return monster_id

def load_enemy(monster_data, monster_level):
    monster_id = randomize_enemy(monster_data)
    monster_index = utils.find_row(monster_data, index=0, element=monster_id)
    
    type = monster_data[monster_index][1]
    name = 'Enemy' + type
    atk_power = int(int(monster_data[monster_index][2]) * (1 + (monster_level - 1) * 0.1))
    def_power = utils.min(int(int(monster_data[monster_index][3]) * (1 + (monster_level - 1) * 0.1)), 50)
    hp = int(int(monster_data[monster_index][4]) * (1 + (monster_level - 1) * 0.1))
    speed = utils.min(int(int(monster_data[monster_index][5]) * (1 + (monster_level - 1) * 0.1)), 50)
    enemy_dict = {'name' : name, 'type' : type, 'id': monster_id, 'level': monster_level, 'atk_power': atk_power, 'def_power': def_power, 'hp': hp, 'max_hp' : hp, 'speed' : speed}
    return enemy_dict

def switch_monster(monster_dict, current_monster_index = None):
    monster_indices = []
    for i in range(len(monster_dict)):
        if i != current_monster_index:
            monster_indices.append(str(i + 1))
    print("Pilih monstermu")
    for i, monster in enumerate(monster_dict):
        print(f"{i + 1}. {monster['name']}")

    while True:
        x = utils.strip(input(">>> "))
        if x in monster_indices:
            while True:
                y = utils.strip(input("Apakah kamu yakin? (Y/N): "))
                if y.lower() == 'y':
                    utils.remove_xth_line_above(1)
                    break
                elif y.lower() == 'n':
                    if current_monster_index == None:
                        utils.remove_x_line_above(2)
                        print("Pilih monster")
                        while True:
                            x = utils.strip(input(">>> "))
                            if x not in monster_indices:
                                print("Masukkan input yang valid")
                                time.sleep(1)
                                utils.remove_x_line_above(2)
                            else:
                                break
                    else:
                        utils.remove_x_line_above(2)
                        return current_monster_index,monster_dict[current_monster_index],False
                else:
                    print("Masukkan input yang valid")
                    time.sleep(1)
                    utils.remove_x_line_above(2)
            
            utils.clear_terminal()
            print_user_monster()
            current_monster_index = int(x) - 1
            print(f"{monster_dict[int(current_monster_index)]['name']}, Aku memilih kamu")
            break
        else:
            print("Masukkan input yang valid")
            time.sleep(1)
            utils.remove_x_line_above(2)
    time.sleep(1.5)
    utils.clear_terminal()
    return current_monster_index,monster_dict[current_monster_index],True

def show_stat(monster,status_effect,current_monster_index):
    def calculate_increase(stat_name, monster, max_value=None):
        if stat_name in status_effect[current_monster_index]:
            increase = int(0.05 / 1.05 * monster[stat_name])
            if increase == 0:
                increase = 1
            if max_value is not None:
                new_stat_value = utils.min(monster[stat_name] + increase, max_value)
                increase = new_stat_value - monster[stat_name]
            return f" (+{increase})"
        else:
            return ""

    print(f"""{'Player'}
{'Name':<15}: {monster['name']}
{'Type':<15}: {monster['type']}
{'Level':<15}: {monster['level']}
{'Attack Power':<15}: {monster['atk_power']}{calculate_increase('atk_power', monster)}
{'Defense Power':<15}: {monster['def_power']}{calculate_increase('def_power', monster,50)}
{'Speed':<15}: {monster['speed']}{calculate_increase('speed', monster,50)}
{'HP':<15}: {f"{monster['hp']}/{monster['max_hp']}"}""")
    
def show_both_stat(monster1, monster2, status_effect, current_monster_index):

    def calculate_increase(stat_name, monster, max_value=None):
        if stat_name in status_effect[current_monster_index]:
            increase = int(0.05 / 1.05 * monster[stat_name])
            if increase == 0:
                increase = 1
            if max_value is not None:
                new_stat_value = utils.min(monster[stat_name] + increase, max_value)
                increase = new_stat_value - monster[stat_name]
            return f" (+{increase})"
        else:
            return ""

    print(f"""{'Player':<49} Enemy
{'Name':<15}: {monster1['name']:<32} {'Name':<15}: {monster2['name']:<32} 
{'Type':<15}: {monster1['type']:<32} {'Type':<15}: {monster2['type']:<32} 
{'Level':<15}: {monster1['level']:<32} {'Level':<15}: {monster2['level']:<32} 
{'Attack Power':<15}: {f"{monster1['atk_power']}{calculate_increase('atk_power', monster1)}":32} {'Attack Power':<15}: {monster2['atk_power']:<32}
{'Defense Power':<15}: {f"{monster1['def_power']}{calculate_increase('def_power', monster1,50)}":32} {'Defense Power':<15}: {monster2['def_power']:<32} 
{'Speed':<15}: {f"{monster1['speed']}{calculate_increase('speed', monster1,50)}":32} {'Speed':<15}: {monster2['speed']:<32} 
{'HP':<15}: {f"{monster1['hp']}/{monster1['max_hp']}":<32} {'HP':<15}: {f"{monster2['hp']}/{monster2['max_hp']}"}""")

def select_action(arena = False):
    options = ['1','2','3','4']
    if not arena:
        options.append('5')
    while True:
        print("Select Action:")
        print("1. Attack")
        print("2. Switch")
        print("3. Use Potion")
        print("4. Run")
        if not arena:
            print("5. Monster Ball")
        x = utils.strip(input(">>> "))
        if x in options:
            if arena:
                utils.remove_x_line_above(6)
            else:
                utils.remove_x_line_above(7)
            break
        else:
            print("Masukkan input yang valid")
            time.sleep(1)
            if arena:
                utils.remove_x_line_above(7)
            else:
                utils.remove_x_line_above(8)
    return x

def select_potion(user_items,monster,current_monster_index,status_effect,monster_data):
    strength_index = utils.find_row(user_items, 1, 'strength')
    speed_index = utils.find_row(user_items, 1, 'speed')
    resilience_index = utils.find_row(user_items, 1, 'resilience')
    healing_index = utils.find_row(user_items, 1, 'healing')

    if user_items and (user_items[strength_index][2] != 0 or user_items[speed_index][2] !=0 or user_items[resilience_index][2] != 0 or user_items[healing_index][2] != 0):
        while True:
            print("Select Potion:")
            print(f"1. Strength (Quantity: {user_items[strength_index][2] if strength_index != -1 else 0})")
            print(f"2. Speed (Quantity: {user_items[speed_index][2] if speed_index != -1 else 0})")
            print(f"3. Resilience (Quantity: {user_items[resilience_index][2] if resilience_index != -1 else 0})")
            print(f"4. Healing (Quantity: {user_items[healing_index][2] if healing_index != -1 else 0})")
            print("5. Cancel")
            x = utils.strip(input(">>> "))
            if x in ['1','2','3','4','5']:
                if x == '1':
                    if strength_index != -1 and int(user_items[strength_index][2]) > 0:
                        if not 'atk_power' in status_effect[current_monster_index]:
                            user_items[strength_index][2] = user_items[strength_index][2] - 1
                            potion('atk_power',monster,current_monster_index,status_effect)
                            print(f"{monster['name']} meminum Strength Potion")
                            time.sleep(1)
                            utils.remove_x_line_above(8)
                            return True
                        else:
                            print(f"{monster['name']} sudah meminum Strength Potion")
                            time.sleep(1)
                            utils.remove_x_line_above(8)
                            return False
                            
                    else:
                        print("Anda tidak memiliki Strength Potion")
                        time.sleep(1)
                        utils.remove_x_line_above(8)
                        return False
                    
                elif x == '2':
                    if speed_index != -1 and int(user_items[speed_index][2]) > 0:
                        if not 'speed' in status_effect[current_monster_index]:
                            user_items[speed_index][2] = user_items[speed_index][2] - 1
                            potion('speed',monster,current_monster_index,status_effect,50)
                            print(f"{monster['name']} meminum Speed Potion")
                            time.sleep(1)
                            utils.remove_x_line_above(8)
                            return True
                        else:
                            print(f"{monster['name']} sudah meminum Speed Potion")
                            time.sleep(1)
                            utils.remove_x_line_above(8)
                            return False
                    else:
                        print("Anda tidak memiliki Speed Potion")
                        time.sleep(1)
                        utils.remove_x_line_above(8)
                        return False
                    
                elif x == '3':
                    if resilience_index != -1 and int(user_items[resilience_index][2]) > 0:
                        if not 'def_power' in status_effect[current_monster_index]:
                            user_items[resilience_index][2] = user_items[resilience_index][2] - 1
                            potion('def_power',monster,current_monster_index,status_effect,50)
                            print(f"{monster['name']} meminum Resilience Potion")
                            time.sleep(1)
                            utils.remove_x_line_above(8)
                            return True
                        else:
                            print(f"{monster['name']} sudah meminum Resilience Potion")
                            time.sleep(1)
                            utils.remove_x_line_above(8)
                            return False
                    else:
                        print("Anda tidak memiliki Resilience Potion")
                        time.sleep(1)
                        utils.remove_x_line_above(8)
                        return False
                    
                elif x == '4':
                    if healing_index != -1 and int(user_items[healing_index][2]) > 0:
                        if not 'healing' in status_effect[current_monster_index]:
                            user_items[healing_index][2] = user_items[healing_index][2] - 1
                            monster['hp'] = heal(monster,monster_data)
                            status_effect[current_monster_index].append('healing')
                            print(f"{monster['name']} meminum Healing Potion")
                            time.sleep(1)
                            utils.remove_x_line_above(8)
                            return True
                        else:
                            print(f"{monster['name']} sudah meminum Healing Potion")
                            time.sleep(1)
                            utils.remove_x_line_above(8)
                            return False
                    else:
                        print("Anda tidak memiliki Healing Potion")
                        time.sleep(1)
                        utils.remove_x_line_above(8)
                        return False
                elif x == '5':
                    time.sleep(1)
                    utils.remove_x_line_above(7)
                    return False

            else:
                print("Masukkan input yang valid")
                time.sleep(1)
                utils.remove_x_line_above(8)
                
    else:
        print("Anda tidak memiliki potion")
        time.sleep(1)
        utils.remove_xth_line_above(1)
        return False

def attack(attacker, defender, monster, enemy, status_effect, current_monster_index) -> int:

    def calculate_increase(stat) -> str:
        if stat < 0:
            return str(stat) + '%'
        elif stat > 0:
            return '+' + str(stat) + '%'
        else:
            return ''

    attack_multiplier = (rng.rng(70,130))
    attack_reduction = (100 - defender['def_power'])
    base_damage = int(attack_multiplier * attacker['atk_power'] * 0.01)
    damage = int(base_damage * attack_reduction * 0.01)
    damage_reduction = base_damage - damage
    speed_diff = defender['speed'] - attacker['speed']
    dodge_chance = max(speed_diff,0)
    
    print(f"Attack: {base_damage} ({calculate_increase(attack_multiplier - 100)}), Reduced by: {damage_reduction} ({defender['def_power']}%)")
    time.sleep(1)
    if rng.rng(1,100) > dodge_chance:
        print(f"{attacker['name']} attacks {defender['name']} for {damage} damage.")
        defender['hp'] = max(defender['hp'] - damage, 0)
    else:
        print(f"{attacker['name']} attacks {defender['name']} but missed.")
    
    time.sleep(0.75)
    utils.clear_terminal()
    show_both_stat(monster, enemy,status_effect,current_monster_index)

    return damage

def execute_turn(first,second, monster, enemy,status_effect, current_monster_index):
    first_damage = attack(first,second, monster, enemy,status_effect, current_monster_index)
    if second['hp'] <= 0:
        print(f"{second['name']} fainted")
        return first_damage, 0
    second_damage = attack(second,first, monster, enemy,status_effect, current_monster_index)
    if first['hp'] <= 0:
        print(f"{first['name']} fainted")
        return first_damage, second_damage
    return first_damage, second_damage

def run(monster,enemy,escape_attempt):
    if monster['speed'] >= enemy['speed']:
        return True
    else:
        escape_odds = ((monster['speed'] * 128) // enemy['speed'] + 30 * escape_attempt) % 256
        print(escape_odds)
        if rng.rng(1,255) <= escape_odds:
            return True
        else:
            return False

def heal(monster, monster_data):
    monster_index = utils.find_row(monster_data, index = 0, element = monster['id'])
    max_hp = int(int(monster_data[monster_index][4]) * (1 + (monster['level'] - 1) * 0.1))
    return int(utils.min(monster['hp'] + 0.25 * max_hp, max_hp))

def potion(status : str,monster,current_monster_index,status_effect,max_value = None):
    status_effect[current_monster_index].append(status)
    if max_value is not None:
        if monster[status] <= 20:
            monster[status] = monster[status] + 1
        else:
            monster[status] = utils.min(int(1.05 * monster[status]),max_value)
    else:
        monster[status] = int(1.05 * monster[status])

def battle(current_user,monster_level,user_data, user_id, monster_inventory_data, item_inventory_data, monster_data, arena, reward = None):
    total_damage_taken = 0
    total_damage_dealt = 0
    victory = False
    if utils.is_empty(current_user):
        print("Anda belum login")
        time.sleep(1)
        utils.remove_x_line_above(2)
        return total_damage_dealt, total_damage_taken, victory, item_inventory_data,monster_inventory_data
    elif utils.strip(current_user[3]) != 'agent':
        print("Anda bukan Agent")
        time.sleep(1)
        utils.remove_x_line_above(2)
        return total_damage_dealt, total_damage_taken, victory, item_inventory_data,monster_inventory_data
    else:
        monster_dict = inventory.load_user_monsters(user_id,monster_inventory_data,monster_data, battle = True)
        enemy = load_enemy(monster_data,monster_level)
        user_items = inventory.get_user_inventory(user_id,item_inventory_data)
        if utils.is_empty(monster_dict):
            print("Anda tidak memiliki monster yang bisa bertarung")
            time.sleep(1)
            utils.remove_x_line_above(2)
            return 0, 0, False, item_inventory_data,monster_inventory_data
        else:
            
            status_effect = [[''] for i in range(len(monster_dict))]
            escape_attempt = 0
            print_enemy_monster()
            print(f"RAWRRR, Monster {enemy['type']} telah muncul")
            time.sleep(1.5)
            current_monster_index, monster, action_executed = switch_monster(monster_dict)
            while monster['hp'] > 0 and enemy['hp'] > 0:
                utils.clear_terminal()
                action_executed = False
                show_both_stat(monster, enemy,status_effect,current_monster_index)
                action = select_action(arena)
                if action == '1':
                    if monster['speed'] > enemy['speed']:
                        damage_dealt, damage_taken = execute_turn(monster,enemy,monster, enemy,status_effect, current_monster_index)
                        total_damage_dealt = total_damage_dealt + damage_dealt
                        total_damage_taken = total_damage_taken + damage_taken

                    elif monster['speed'] < enemy['speed']:
                        damage_taken, damage_dealt = execute_turn(enemy,monster,monster, enemy,status_effect, current_monster_index)
                        total_damage_dealt = total_damage_dealt + damage_dealt
                        total_damage_taken = total_damage_taken + damage_taken

                    else:
                        random_priority = rng.rng(1,2)

                        if random_priority == 1:
                            damage_taken, damage_dealt = execute_turn(enemy,monster,monster, enemy,status_effect, current_monster_index)
                            total_damage_dealt = total_damage_dealt + damage_dealt
                            total_damage_taken = total_damage_taken + damage_taken

                        elif random_priority == 2:
                            damage_dealt, damage_taken = execute_turn(monster,enemy,monster, enemy,status_effect, current_monster_index)
                            total_damage_dealt = total_damage_dealt + damage_dealt
                            total_damage_taken = total_damage_taken + damage_taken
                    time.sleep(1.5)

                elif action == '2':
                    if len(monster_dict) > 1:
                        current_monster_index,monster,action_executed = switch_monster(monster_dict, current_monster_index)
                    
                        if action_executed:
                            damage_taken = attack(enemy,monster,monster, enemy,status_effect, current_monster_index)
                            total_damage_taken = total_damage_taken + damage_taken
                    else:
                        print("Kamu tidak memiliki monster lain")
                    time.sleep(1.5)
                
                elif action == '3':
                    action_executed = select_potion(user_items,monster,current_monster_index,status_effect,monster_data)
                    if action_executed:
                        damage_taken = attack(enemy,monster,monster, enemy,status_effect, current_monster_index)
                        total_damage_taken = total_damage_taken + damage_taken
                    time.sleep(1.5)

                elif action == '4':
                    if run(monster,enemy,escape_attempt):
                        break
                    else:
                        print("Anda tidak bisa kabur")
                        time.sleep(1)
                        damage_taken = attack(enemy,monster,monster, enemy,status_effect, current_monster_index)
                        total_damage_taken = total_damage_taken + damage_taken
                    time.sleep(1.5)
                
                elif action == '5':
                    action_executed = monster_ball.monster_ball(user_id,enemy,user_items,monster_inventory_data)
                    if enemy['hp'] != 0 and action_executed:
                        damage_taken = attack(enemy,monster,monster, enemy,status_effect, current_monster_index)
                        total_damage_taken = total_damage_taken + damage_taken
                    time.sleep(1.5)
            if enemy['hp'] <= 0:
                print(f"Selamat Anda telah berhasil mengalahkan monster {enemy['type']}")
                victory = True
                if reward:
                    print(f"Total OC = {reward}")
                    user_data[utils.find_row(user_data, index = 0, element = user_id)][4] = str(int(user_data[utils.find_row(user_data, index = 0, element = user_id)][4]) + reward)
            elif monster['hp'] <= 0:
                print(f"Anda dikalahkan monster {enemy['type']}")
                victory = False
            else:
                print("Anda berhasil kabur dari battle")
                victory = False
            item_inventory_data = update_item_inventory_data(user_id, user_items, item_inventory_data)
            monster_inventory_data = update_monster_inventory_data(user_id, monster_dict, monster_inventory_data)
            monster_dict = []
            user_items = []
            enemy = {}
            time.sleep(2)
            utils.clear_terminal()
            return total_damage_dealt, total_damage_taken, victory, item_inventory_data,monster_inventory_data

def update_item_inventory_data(user_id, user_items, item_inventory_data):
    for item in item_inventory_data:
        if item[0] == user_id:
            for user_item in user_items:
                if item[1] == user_item[1]:
                    item[2] = str(user_item[2])
    return utils.remove_row(item_inventory_data, 2,'0')

def update_monster_inventory_data(user_id, monster_dict, monster_inventory_data):
    for monster in monster_inventory_data:
        if monster[0] == user_id:
            for user_monster in monster_dict:
                if user_monster['name'] == monster[3]:
                    monster[4] = str(user_monster['hp'])
    return monster_inventory_data