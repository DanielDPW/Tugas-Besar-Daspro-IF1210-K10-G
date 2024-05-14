import os
import argparse

from . import csv_parser

def load():
    argparser = argparse.ArgumentParser()
    argparser.add_argument('nama_folder', help='Nama folder tempat data tersimpan')
    args = argparser.parse_args()
    directory = args.nama_folder
    if directory is None:
        print("Tidak ada nama folder yang diberikan")
    else:
        if os.path.isdir(directory):
            print("Selamat datang di program OWCA!")
            user_data = csv_parser.parse_csv(directory + '/user.csv')
            monster_data = csv_parser.parse_csv(directory +'/monster.csv')
            monster_shop_data = csv_parser.parse_csv(directory + '/monster_shop.csv')
            monster_inventory_data = csv_parser.parse_csv(directory + '/monster_inventory.csv')
            item_shop_data = csv_parser.parse_csv(directory + '/item_shop.csv')
            item_inventory_data = csv_parser.parse_csv(directory + '/item_inventory.csv')
            return user_data, monster_data, monster_shop_data, monster_inventory_data, item_shop_data, item_inventory_data
        else:
            print(f"Folder {directory} tidak ditemukan")
            return [], [], [], [], [], []