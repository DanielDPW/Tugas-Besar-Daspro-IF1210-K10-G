import time

from src import rng as rng
from src import csv_parser as csv_parser
from src import utils as utils
from src import register as register
from src import login as login
from src import inventory as inventory
from src import battle as battle
from src import arena as arena
from src import shop as shop
from src import laboratory as laboratory
from src import shop_management as shop_management
from src import monster_management as monster_management
from src import load as load
from src import save as save
from src import exit as exit
from src import healingfountain as healingfountain
from src import help as help

user_data, monster_data, monster_shop_data, monster_inventory_data, item_shop_data, item_inventory_data = load.load()
current_user = []
user_id = ''
if None not in (user_data, monster_data, monster_shop_data, monster_inventory_data, item_shop_data, item_inventory_data):
    while True:
        prompt = utils.strip(input(">>> "))
        if prompt.lower() == "help":
            help.help(current_user)
        elif prompt.lower() == "register":
            user_data,monster_inventory_data = register.register(user_data, current_user, monster_data,monster_inventory_data)
        elif prompt.lower() == "login":
            current_user,user_id = login.login(user_data, current_user)
        elif prompt.lower() == "logout":
            current_user,user_id = login.logout(current_user)
        elif prompt.lower() == "inventory":
            inventory.inventory(current_user, user_id,user_data,item_inventory_data, monster_inventory_data,monster_data)
        elif prompt.lower() == "battle":
            total_damage_dealt, total_damage_taken, victory,item_inventory_data,monster_inventory_data = battle.battle(current_user,battle.randomize_enemy_level(),user_data, user_id, monster_inventory_data, item_inventory_data, monster_data, arena = False, reward = rng.rng(15,50))
        elif prompt.lower() == "arena":
            total_damage_dealt,total_damage_taken,stage_cleared,item_inventory_data,monster_inventory_data = arena.arena(current_user,user_data, user_id, monster_inventory_data, item_inventory_data, monster_data)
        elif prompt.lower() == "heal":
            monster_inventory_data, user_data = healingfountain.healingfountain(current_user,user_id,user_data,monster_inventory_data, monster_data)
        elif prompt.lower() == "shop":
            if utils.is_empty(current_user):
                print("Anda belum login")
                time.sleep(1)
                utils.remove_x_line_above(2)
            elif current_user[3] == 'agent':
                user_data,item_inventory_data,monster_inventory_data,item_shop_data,monster_shop_data = shop.shop(current_user,user_id,user_data,item_inventory_data,monster_inventory_data,item_shop_data,monster_shop_data,monster_data)
            elif current_user[3] == 'admin':
                item_shop_data, monster_shop_data = shop_management.shop_management(current_user,item_shop_data, monster_shop_data, monster_data)
        elif prompt.lower() == "laboratory":
            monster_inventory_data, user_data = laboratory.laboratory(current_user,user_id, monster_inventory_data, monster_data, user_data)
        elif prompt.lower() == "monster":
            monster_data, monster_inventory_data, monster_shop_data = monster_management.monster_management(current_user,monster_data, monster_inventory_data, monster_shop_data)
        elif prompt.lower() == "exit":
            exit.exit(user_data, monster_data, monster_shop_data, monster_inventory_data, item_shop_data, item_inventory_data)
            break
        else:
            print("Masukkan command yang benar!")
            time.sleep(0.5)
            utils.remove_x_line_above(2)