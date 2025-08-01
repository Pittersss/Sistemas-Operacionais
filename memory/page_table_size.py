import math
from random import randint

def paging_translation(address_acess: int, address_space: int, physical_address_space: int, page_size: int):
    address_acess_bin = bin(address_acess)[2:] #without prefix 0b 
    address_size = math.log2(address_space)
    pages_quantity = address_space / page_size 

    page_table = generate_table(address_acess, physical_address_space ,page_size)

    size_dif = (len(address_acess_bin) - int(address_size))
    address_acess_bin = ("0" * size_dif) + address_acess_bin
    page_id = int(address_acess_bin[:int(math.log2(pages_quantity)) + 1], 2)
    page_frame_id = search_in_page_table(page_id, page_size, page_table)

    return page_frame_id

def generate_table(address_space: int, physical_address_space: int ,page_size: int):
    number_of_pages = address_space/page_size
    page_table_entrys = number_of_pages
    number_of_pages_frames = physical_address_space/page_size
    page_table_entrys_size = math.log2(number_of_pages_frames)
    page_table_size = page_table_entrys * page_table_entrys_size
    page_table = []

    while(len(page_table) != page_table_size):
        elem = randint(0,  int(page_table_entrys_size) - 1)
        if elem not in page_table:
            size_dif = page_table_entrys_size - len(bin(elem)[2:])
            if size_dif != 0:
                page_table.append(("0" * int(size_dif)) + bin(elem)[2:])
            else:
                page_table.append(bin(elem)[2:])
    
    resul = "".join(page_table)

    show_page_table_structured(resul, int(number_of_pages_frames))
    
    return resul


def search_in_page_table(page_id: int, page_size: int ,page_table):
    start_address = page_id * page_size
    return int(page_table[start_address: (start_address + page_size)], 2)

def show_page_table_structured(page_table, pages_frames_quantity : int):
    print("Paging Table:\n")
    for i in range(0, int(len(page_table) / pages_frames_quantity)):
        start_pos = i * pages_frames_quantity
        print(str(i) + " | " + str(int(page_table[ start_pos : start_pos + pages_frames_quantity], 2)) + "\n--------------------")




def calc_page_table_size(address_space: int, page_size: int):
    number_of_pages = address_space/page_size
    number_of_pages_frames = number_of_pages #Assumindo
    page_table_address = number_of_pages_frames
    page_table_address_size = math.log2(page_table_address)
    resul = page_table_address * page_table_address_size
    return resul


def calc_page_table_size_adress_size(adress_size: int):
    return

print(generate_table(64,64,16))