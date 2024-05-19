import time
from typing import *

from . import utils
from . import save
from .types import *

def exit(user_data : Matrix, monster_data : Matrix, monster_shop_data : Matrix, monster_inventory_data : Matrix, item_shop_data : Matrix, item_inventory_data : Matrix):
    save_prompt = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (Y/N): ")
    while save_prompt.lower() != 'y' and save_prompt.lower() != 'n':
        print("Masukkan input yang valid")
        time.sleep(1)
        utils.remove_xth_line_above(2)
        save_prompt = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (Y/N): ")
    if save_prompt.lower() == 'y':
        save.save(user_data, monster_data, monster_shop_data, monster_inventory_data, item_shop_data, item_inventory_data)