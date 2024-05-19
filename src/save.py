import os
from typing import *

from . import csv_parser
from .types import *

def save(user_data : Matrix, monster_data : Matrix, monster_shop_data : Matrix, monster_inventory_data : Matrix, item_shop_data : Matrix, item_inventory_data : Matrix):
    directory = input("Masukkan nama folder penyimpanan: ")

    if os.path.isdir(directory):
        csv_parser.generate_csv(user_data, directory +'/user.csv')
        csv_parser.generate_csv(monster_data, directory + '/monster.csv')
        csv_parser.generate_csv(monster_shop_data, directory +'/monster_shop.csv')
        csv_parser.generate_csv(monster_inventory_data, directory + '/monster_inventory.csv')
        csv_parser.generate_csv(item_shop_data, directory + '/item_shop.csv')
        csv_parser.generate_csv(item_inventory_data, directory + '/item_inventory.csv')
    else:
        os.mkdir(directory)
        print(f"Folder tidak ditemukan sehingga dibuat folder pada {directory}")
        csv_parser.generate_csv(user_data, directory +'/user.csv')
        csv_parser.generate_csv(monster_data, directory + '/monster.csv')
        csv_parser.generate_csv(monster_shop_data, directory +'/monster_shop.csv')
        csv_parser.generate_csv(monster_inventory_data, directory + '/monster_inventory.csv')
        csv_parser.generate_csv(item_shop_data, directory + '/item_shop.csv')
        csv_parser.generate_csv(item_inventory_data, directory + '/item_inventory.csv')