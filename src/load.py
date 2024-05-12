import os
import argparse

from . import csv_parser

def load():
    argparser = argparse.ArgumentParser()
    argparser.add_argument('nama_folder', help='Nama folder tempat data tersimpan')
    args = argparser.parse_args()
    directory = args.nama_folder
    
    if os.path.isdir(directory):
        print("Selamat datang di program OWCA!")
        user_data = csv_parser.parse_csv(os.path.join(directory, 'user.csv'))
        monster_data = csv_parser.parse_csv(os.path.join(directory, 'monster.csv'))
        monster_shop_data = csv_parser.parse_csv(os.path.join(directory, 'monster_shop.csv'))
        monster_inventory_data = csv_parser.parse_csv(os.path.join(directory, 'monster_inventory.csv'))
        item_shop_data = csv_parser.parse_csv(os.path.join(directory, 'item_shop.csv'))
        item_inventory_data = csv_parser.parse_csv(os.path.join(directory, 'item_inventory.csv'))
        return user_data, monster_data, monster_shop_data, monster_inventory_data, item_shop_data, item_inventory_data
    else:
        return [], [], [], [], [], []