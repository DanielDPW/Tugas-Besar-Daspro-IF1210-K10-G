from . import utils

def help(current_user):
    if utils.is_empty(current_user):
        message = f"""
=================================================================================
===================================== HELP ======================================
=================================================================================

Kamu belum login sebagai role apapun. Silahkan login terlebih dahulu.

Login    : Masuk ke dalam akun yang sudah terdaftar
Register : Membuat akun baru
Exit     : Keluar dari aplikasi

Footnote: 
Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar
Jangan lupa untuk memasukkan input yang valid

=================================================================================
    """
    elif current_user[3] == 'agent':
        message = f"""
=================================================================================
===================================== HELP ======================================
=================================================================================

Halo Agen {current_user[1]}. Kamu memanggil command HELP. Kamu memilih jalan 
yang benar, semoga kamu tidak sesat kemudian. Berikut adalah hal-hal yang dapat 
kamu lakukan sekarang:

Logout     : Keluar dari akun yang sedang digunakan
Inventory  : Melihat owca-dex yang dimiliki oleh agen
Battle     : Memulai pertarungan dengan monster
Arena      : Bertanding dalam arena
Heal       : Mengunjungi Healing Fountain
Shop       : Membeli barang di Superduper Mega Superstore
Laboratory : Melakukan upgrade kepada monster
Exit       : Keluar dari aplikasi

Footnote: 
Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar
Jangan lupa untuk memasukkan input yang valid

=================================================================================
    """
    elif current_user[3] == 'admin':
        message = f"""
=================================================================================
===================================== HELP ======================================
=================================================================================

Selamat datang, Admin. Berikut adalah hal-hal yang dapat kamu lakukan:

Logout : Keluar dari akun yang sedang digunakan
Shop   : Melakukan manajemen pada SHOP sebagai tempat jual beli peralatan Agent
Monster: Melakukan manajemen pada database monster
Exit   : Keluar dari aplikasi

Footnote: 
Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar
Jangan lupa untuk memasukkan input yang valid

=================================================================================
    """
    print(message)
