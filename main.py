#-------------------------------------------------------------------------------------------------
# TikDown v4 by Tekky
# Copyright (c) 2022 Tekky. All rights reserved.
# I am not responsible for any damage caused by your use of this software.
#-------------------------------------------------------------------------------------------------

from imp import acquire_lock
from msilib.schema import Error
from re import S


try:
    import os
    import requests
    import random
    from threading import Thread
    from pystyle import *
    from time import sleep, time
except ModuleNotFoundError as e:
    print(f'ERROR [{e}]')


def download(id):
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    }

    try:
        r = requests.get(f'https://api.tiktokv.com/aweme/v1/multi/aweme/detail/?aweme_ids=%5B{id}%5D', headers=headers).json()["aweme_details"][0]["video"]["play_addr"]["url_list"][0]
        with open(f'./tiktok_vids/tiktok{random.randint(1000, 9999)}.mp4', 'wb') as out_file:
            content = requests.get(f'{r}.mp4', stream=True).content
            out_file.write(content)
            print(Colorate.Horizontal(Colors.green_to_white,f"       [*] Downloaded [id={id}] [folder=tiktok_vids]\n", 1))

    except:
        sleep(1)
        try:
            r = requests.get(f'https://api.tiktokv.com/aweme/v1/multi/aweme/detail/?aweme_ids=%5B{id}%5D', headers=headers).json()["aweme_details"][0]["video"]["play_addr"]["url_list"][0]
            with open(f'./tiktok_vids/tiktok{random.randint(1000, 9999)}.mp4', 'wb') as out_file:
                content = requests.get(f'{r}.mp4', stream=True).content
                out_file.write(content)
                print(Colorate.Horizontal(Colors.green_to_white,f"       [*] Downloaded [id={id}] [folder=tiktok_vids]\n", 1))

        except Error as e:
            print(Colorate.Horizontal(Colors.red_to_white,f"       [x] ERROR: Unable to download [id={id}] [{e}]\n", 1))
            pass


def main(user):

    global headers

    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    }

    if requests.get(f'https://www.tiktok.com/@{user}', headers=headers).status_code == 404:
        Write.Print('       [*] This account is Unavailable!!', Colors.red_to_white, interval=0.01)
        input()
        start()


    r = requests.get(f'https://www.tiktok.com/node/share/user/@{user}', headers=headers).json()
    
    if r["userInfo"]['user']['privateAccount'] == 'True':
        Write.Print('       [*] This account is Private!!', Colors.red_to_white, interval=0.01)
        input()
        start()

    if r["userInfo"]['stats']['videoCount'] == '0':
        Write.Print('       [*] This user has no visdeos!!', Colors.red_to_white, interval=0.01)
        input()
        start()
    
    secUid = r["userInfo"]['user']['secUid']
    userid = r["userInfo"]['user']['id']

    r = requests.get(f'https://www.tiktok.com/share/item/list?secUid={secUid}&id={userid}&type=1&count=999&minCursor=0&maxCursor=0&shareUid=&lang=&_signature=lMPjwgAgEB3hMmicFQVIApTD4tAAMqU', headers=headers).json()


    for no in r["body"]['itemListData']:
        id = no["itemInfos"]['id']
        Thread(target=download, args=(id,)).start()


def start():
        os.system('cls' if os.name == 'nt' else 'clear')

        
        
        txt = '''
        
        
                                                    ╔╦╗┬┬┌─  ╔╦╗┌─┐┬ ┬┌┐┌
                                                     ║ │├┴┐   ║║│ │││││││ 
                                                     ╩ ┴┴ ┴  ═╩╝└─┘└┴┘┘└┘
                                                        V4 By Tekky#9999
                                                            '''

        print(Colorate.Horizontal(Colors.blue_to_purple, txt, 1))
        print('\n')

        # how many links
        Write.Print("       [?] Download from profile [y/n] ↓\n", Colors.blue_to_purple, interval=0.001)
        choice = Write.Input("        >  ", Colors.blue_to_purple, interval=0.0001, hide_cursor=True)
        print('\n')


        if choice == 'y':
            Write.Print("       [?] Username [@xxxx] ↓\n", Colors.blue_to_purple, interval=0.001)
            user = Write.Input("        >  ", Colors.blue_to_purple, interval=0.0001, hide_cursor=True)
            
            if '@' in user:
                user.replace('@', '')
            
            print('\n')
            start_time = time()
            
            main(user)
            
            input()
            start()

        if choice == 'n':
            link_list = []
            Write.Print("       [?] How many links [1 to ∞] ↓\n", Colors.blue_to_purple, interval=0.001)
            links = Write.Input("        >  ", Colors.blue_to_purple, interval=0.0001, hide_cursor=True)
            links = int(links)
            print('\n')

            for i in range(links):
                #url input
                Write.Print(f"       [?] TikTok URL [{i}] ↓\n", Colors.blue_to_purple, interval=0.001)
                link_id = Write.Input("        >  ", Colors.blue_to_purple, interval=0.001, hide_cursor=True)
                raw_link = link_id

                try:
                    if "vm.tiktok.com" in link_id or "vt.tiktok.com" in link_id:
                        link_id = requests.head(link_id, stream=True, allow_redirects=True, timeout=5).url.split("/")[5].split("?", 1)[0]
                        link_list.append(link_id)
                    else:
                        link_id = link_id.split("/")[5].split("?", 1)[0]
                        link_list.append(link_id)
                except:       
                    Write.Print('       [*] Link not supported!!', Colors.red_to_white, interval=0.01)
                    input()
                    start()
            
            
                
            print('\n\n')
            start_time = time()
            
            for z in range(links):
                id = link_list[z]
                Thread(target=download, args=(id,)).start()
            
            input()

            
            
            
        else:
            Write.Print("       [x] Invalid choice, redirecting... \n", Colors.white_to_red, interval=0.0001)
            sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            start()

if __name__ == "__main__":
    os.system('title Tekky © 2022 ^| TikDown' if os.name == 'nt' else '')
    newpath = r'./tiktok_vids'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    start()
