import time

from . import utils
from . import save

def exit(user_data, monster_data, monster_shop_data, monster_inventory_data, item_shop_data, item_inventory_data):
    save_prompt = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (Y/N): ")
    while save_prompt.lower() != 'y' and save_prompt.lower() != 'n':
        print("Masukkan input yang valid")
        time.sleep(1)
        utils.remove_xth_line_above(2)
        save_prompt = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (Y/N): ")
    if save_prompt.lower() == 'y':
        save.save(user_data, monster_data, monster_shop_data, monster_inventory_data, item_shop_data, item_inventory_data)