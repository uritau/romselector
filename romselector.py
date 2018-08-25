from os import listdir
from os.path import isfile, join
import sys
import re

def read_work_dir( roms_dir ):
    return roms_dir

def read_params():
    work_dir = read_work_dir(sys.argv[1])
    return work_dir

def list_files(work_dir):
    roms_list = [f for f in listdir(work_dir) if isfile(join(work_dir, f))]
    return roms_list

def split_rom_name( rom_name ):
    ar_rom_info = rom_name.replace(".zip", "")
    ar_rom_info = ar_rom_info.replace(") ", "")
    ar_rom_info = ar_rom_info.replace(")", "")
    ar_rom_info = ar_rom_info.replace(" (", "(")
    ar_rom_info = ar_rom_info.split("(")
    ar_rom = []
    ar_rom.append(rom_name)
    ar_rom_info.insert(0,rom_name)
    return ar_rom_info

def split_rom_names (rom_list): 
    rom_list_splitted = []
    for rom in rom_list:
        rom_list_splitted.append(split_rom_name(rom))
    return rom_list_splitted

def trim_files( roms_list ):
    ar_names = split_rom_names( roms_list )
    return ar_names

def list_tags(roms_list):
    tag_list = []
    for rom in roms_list:
        for i in range (2,len(rom)):
            if rom[i] not in tag_list:
                tag_list.append(rom[i])
    return tag_list

def count_games_tag(tag,roms):
    tag_count = 0
    for rom in roms:
        if any(tag in rom_tags for rom_tags in rom):
            tag_count=tag_count+1
    return tag_count

def count_games_tags(tag_list,roms):
    for tag in tag_list:
        #print (tag)
        tag_count = count_games_tag(tag,roms)
        #print(tag_count)

def message_welcome():
    print ("Start program")


def import_tag_selector(tags):
    tag = tags[0]
    print (tags)
    answer = ""
    while (answer != 'y') & (answer != 'n'):
        answer = input("Do you would to import games under tag \"{}\"? (y/n)\n".format(tag))
        if answer == 'y':
            print("YUHUUU YES!")
        elif answer == 'n':
            print("Oh no, wtf")
        # else:
        #     print ("error!")


def main():
    message_welcome()
    roms_dir = read_params()
    roms_list = list_files(roms_dir)
    splitted_roms = trim_files(roms_list)
    tag_list = list_tags(splitted_roms)
    count_games_tags(tag_list,splitted_roms)
    import_tag_selector(tag_list)

if __name__== "__main__":
  main()

