import os

from . import csv_parser

def save(user_data, monster_data, monster_shop_data, monster_inventory_data, item_shop_data, item_inventory_data):
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