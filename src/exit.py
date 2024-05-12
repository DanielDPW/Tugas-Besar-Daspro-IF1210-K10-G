from . import save

def exit(user_data, monster_data, monster_shop_data, monster_inventory_data, item_shop_data, item_inventory_data):
    save_prompt = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    while save_prompt.lower() != 'y' and save_prompt.lower() != 'n':
        save_prompt = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    if save_prompt.lower() == 'y':
        save.save(user_data, monster_data, monster_shop_data, monster_inventory_data, item_shop_data, item_inventory_data)