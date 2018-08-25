from os import listdir
from os.path import isfile, join
import sys
import re

def read_work_dir( roms_dir ):
    #print("This is the file of the roms: ", roms_dir )
    return roms_dir

#Read params and assign to variables
def read_params():
    work_dir = read_work_dir(sys.argv[1])
    #print ("this is the work dir", work_dir)
    return work_dir

#List files in dir
def list_files(work_dir):
    roms_list = [f for f in listdir(work_dir) if isfile(join(work_dir, f))]
    #print("This is the rom list: ", roms_list )
    return roms_list


def split_rom_name( rom_name ):
    rom_name = rom_name.replace(".zip", "")
    rom_name = rom_name.replace(") ", "")
    rom_name = rom_name.replace(")", "")
    rom_name = rom_name.replace(" (", "(")
    rom_name = rom_name.split("(")    
    return rom_name

def split_rom_names (rom_list): 
    rom_list_splitted = []
    for rom in rom_list:
        rom_list_splitted.append(split_rom_name(rom))
    return rom_list_splitted

def parse_rom_name(rom ):
    return 0

def unique (roms_list):
    unique_list = []
    for rom in roms_list:
        is_unique = 0
        for compare_rom in roms_list:
            if rom[0] == compare_rom[0]:
                is_unique = is_unique + 1
        if is_unique == 1:
            unique_list.append(rom)
    return unique_list



def trim_files( roms_list ):
    ar_names = split_rom_names( roms_list )
    #print ("AR_NAMES", ar_names)
    #for rom in roms_list:
        #is_unique (rom,roms_list)
    return ar_names
        

def list_tags(roms_list):
    tag_list = []
    for rom in roms_list:
        for i in range (1,len(rom)):
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
        print (tag)
        tag_count = count_games_tag(tag,roms)
        print(tag_count)


def main():
  roms_dir = read_params()
  roms_list = list_files(roms_dir)
  splitted_roms = trim_files(roms_list)
  unique_list = unique(splitted_roms)
  tag_list = list_tags(splitted_roms)
  count_games_tags(tag_list,splitted_roms)
  print ("Welcome, we will check")

if __name__== "__main__":
  main()

