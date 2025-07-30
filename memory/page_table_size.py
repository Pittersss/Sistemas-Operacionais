import math

def paging_translation(address_acess: int, address_space: int, physical_address_space: int, page_size: int):
    address_acess_bin = bin(address_acess)[2:] #without prefix 0b
    address_size = math.log2(address_space)
    pages_quantity = address_space / page_size
    page_frame_quantity = physical_address_space / page_size

    page_table = generate_table(address_acess, physical_address_space ,page_size)

    while len(address_acess_bin) != address_size:
        address_acess_bin = "0" + address_acess_bin
    


    return type(address_acess_bin)

def generate_table(address_space: int, physical_address_space: int ,page_size: int):
    number_of_pages = address_space/page_size
    page_table_entrys = number_of_pages
    number_of_pages_frames = physical_address_space/page_size
    page_table_entrys_size = math.log2(number_of_pages_frames)

    page_table_size = page_table_entrys * page_table_entrys_size
    #for i in range(0, int(page_table_entrys_size)):



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