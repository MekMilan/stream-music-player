from email.policy import default
import os
from pick import pick


def cls():
    os.system("cls")

cls()

def play():
    # system(f"mpv --no-video -playlist=playlist-{NOME}.txt")
    pass


def play_playlist():

    title = "Choose an Playlist"
    options = []
    directory_path = os.getcwd()

    for (dirpath, dirnames, filenames) in os.walk(f'{directory_path}\\playlists\\'):
        for file in filenames:
            if '.txt' in file:
                options.extend(filenames)
                break
    
    options.append('')
    options.append('Exit')
    option, index = pick(options, title, indicator='>', default_index=0)
    
    match option:
        case "Exit":
            return
        case "":
            return
        case _:
            os.system(f'mpv --no-video --playlist=playlists\{option}')
    pass


def queu():
    pass


def make_playlist():
    NOME            = input("Playlist name (without spaces): ")
    PLAYLIST_URL    = input("Input Playlist url (without '&start_radio=1'): ")

    PLAYLIST_URL = PLAYLIST_URL.split('&')

    link = PLAYLIST_URL[0] + '\"' + "&" + '\"' + PLAYLIST_URL[1]
    cls()
    print("Processing playlist videos please wait...")
    os.system(f"youtube-dl --get-id {link} >> temp-{NOME}.txt")

    count = -1
    list_of_url = []

    with open(f'temp-{NOME}.txt', 'r+') as line:
        f = line.readlines()
        for i in f:
            count += 1 
            f[count] = "https://www.youtube.com/watch?v=" + f[count]
            list_of_url.append(f[count])
        line.close()

    with open(f'playlist-{NOME}.txt', 'w') as txt_file:
        for line in list_of_url:
            txt_file.write("".join(line))

    os.remove(f'temp-{NOME}.txt')
    cls()
    print('Process done ! (type ENTER to continue)')
    input()
    start()


def start():
    title = "Choose an option"
    options = ['Make a Playlist', 'Play a Playlist', '', 'Exit']
    option, index = pick(options, title, indicator='>', default_index=0)
    
    match index:
        case 0:
            make_playlist()
        case 1:
            play_playlist()
        case 2:
            return
        case "":
            return
        case _:
            print('Invalid option')

start()
