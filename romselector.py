from os import listdir
from os.path import isfile, join
import sys
import re


def read_params():
    work_dir = sys.argv[1]
    dest_dir = sys.argv[2]
    return work_dir, dest_dir

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
    if not len(tag_list):
        print("\n########################################################## WARNING ######################################################")
        print("There are no files in the origin folder that follows the no_intro naming, confirm the folder is correct and launch again.")
        print("#########################################################################################################################\n\n")
        exit()
    return tag_list

def count_games_tag(tag,roms):
    tag_count = 0
    for rom in roms:
        if any(tag in rom_tags for rom_tags in rom):
            tag_count=tag_count+1
    return tag_count

def count_games_tags(tag_list,roms):
    for tag in tag_list:
        tag_count = count_games_tag(tag,roms)

def welcome_message():
    print ("Starting Rom Selector, welcome ^^!!")

def choose_selection_mode():
    print ("You can choose the easy selector, that will import all games but only one version (European or USA or Japanese or others)\
and will let you choose only if you would to import Beta games ")
    print ("Or you can choose the advanced selector, that will let you select which game tags will be imported.")
    answer = ""
    answer = input("What do you preffer?\nEasy (E) or\nAdvanced (A)?\n")
    if (answer == 'A') | (answer == 'a') | (answer == 'Advanced') | (answer == 'ADVANCED') | (answer == 'Advanced (A)'):
        print ("You have selected the Advanced way")
        mode = "advanced"
    else:
        print ("You have selected the Easy way")
        mode = "easy"
    return mode

def print_tags(tags):
    print ("Tag list:")
    print ("{}\n\n".format(tags))

def import_tag_selector(tags):
    selected_tags = []

    for tag in tags:
        answer = ""
        answer = input("Do you would to import games under tag \"{}\"? (No to cancel)\n".format(tag))
        if (answer == 'n') | (answer == 'no') | (answer == 'N') | (answer == 'No') | (answer == 'NO'):
            print("Oh no, wtf")
        else:
            selected_tags.append(tag)
            print("yuju!")
    return (selected_tags)


def rom_has_tags(tags, rom):
    intersection = 0
    if (set(rom).intersection(set(tags))):
        intersection = 1
    return intersection

def select_games (tags, roms):
    selected_roms = []
    for rom in roms:
        if rom_has_tags(tags, rom):
            selected_roms.append(rom)
    return selected_roms

def check_params():
    if (len(sys.argv) != 3):
        print ("romselector.py: missing file\nusage python3 romselector.py originfolder destinationfolder\nEnter the origin and the destination folder.\n\n")
        exit()

def unique_selector(tags, roms):
    selected_roms = []
    limited_countries = []
    print ("Unique selector")
    #print ("Tag list {} roms list {}".format(tags,roms))
    for rom in roms:
        if rom_has_tags(['Europe', 'World', 'USA, Europe'], rom) & (len(rom) == 3):  
            selected_roms.append(rom)
    for rom in roms:
        #print (rom)
        if (not rom_has_tags(['Europe', 'World', 'USA, Europe'], rom)) & (len(rom) == 3):
            if (rom[2] not in limited_countries):
                limited_countries.append(rom[2])
    
    print ("We have added all the unique games with Europe, World and \"USA, Europe\" Versions ")
    print ("There are some other unique games that maybe you would add too. The pending countries are the following:")
    print (limited_countries)


    # for rom in selected_roms:
    #     print ("ROM: {} and lenght {}".format(rom,len(rom)))



def main():
    check_params()
    welcome_message()
    roms_dir, dest_dir = read_params()
    roms_list = list_files(roms_dir)
    splitted_roms = trim_files(roms_list)
    tag_list = list_tags(splitted_roms)
    count_games_tags(tag_list,splitted_roms)
    print_tags(tag_list)
    mode=choose_selection_mode()
    if (mode == 'easy'):
        unique_selector(tag_list,splitted_roms)
        exit()
    else:
        selected_tags = import_tag_selector(tag_list)
        selected_games = select_games(selected_tags, splitted_roms)
        exit()
    print("################# Lista de juegos añadidos #################")
    for rom in selected_games:
        print ("## {}".format(rom[1]))
    print("#############################################################")
    print ("De un total de {} juegos has añadido {})".format(len(roms_list), len(selected_games)))



if __name__== "__main__":
  main()

