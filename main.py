import http.client
import json
import random
from urllib import request
from pystyle import *
import requests
import os
from time import time

def title(Content):
    global DebugMode
    if os.name in ('posix', 'ce', 'dos'):
        pass
    elif os.name == 'nt':
        os.system(f"title {Content}")
        return False
    else:
        pass


def getVideoUrl(vid):
    Write.Print("[*] Retrieving Url...\n", Colors.blue_to_purple, interval=0.001)
    conn = http.client.HTTPSConnection("api.tiktokv.com") #
    payload = ''
    headers = {
    }
    conn.request("GET", "/aweme/v1/multi/aweme/detail/?aweme_ids=%5B" + vid + "%5D", payload, headers) #
    res = conn.getresponse()
    data = res.read()
    obj = json.loads(data.decode("utf-8"))
    Write.Print("[*] Removing Watermark...\n", Colors.blue_to_purple, interval=0.001)
    return obj["aweme_details"][0]["video"]["play_addr"]["url_list"][0];


if __name__ == "__main__":
    title(f"Tekky © 2022 - Tik Down")
    try:
        os.system('clear')
        os.system('cls')
    except:
        pass
    r = requests.Session()
    newpath = r'./tiktok_vids'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    raw_link = ''
    link_id = ''
    links_list = []
    print(' ')
    txt = r'''
                        ████████────▀██  ▄▄▄█████▓ ██▓ ██ ▄█▀   ▓█████▄  ▒█████   █     █░███▄    █ TM
                        ████████──█▄──█  ▓  ██▒ ▓▒▓██▒ ██▄█▒    ▒██▀ ██▌▒██▒  ██▒▓█░ █ ░█░██ ▀█   █  
                        ███▀▀▀██──█████  ▒ ▓██░ ▒░▒██▒▓███▄░    ░██   █▌▒██░  ██▒▒█░ █ ░█▓██  ▀█ ██▒
                        █▀──▄▄██──█████  ░ ▓██▓ ░ ░██░▓██ █▄    ░▓█▄   ▌▒██   ██░░█░ █ ░█▓██▒  ▐▌██▒
                        █──█████──█████    ▒██▒ ░ ░██░▒██▒ █▄   ░▒████▓ ░ ████▓▒░░░██▒██▓▒██░   ▓██░
                        █▄──▀▀▀──▄█████    ▒ ░░   ░▓  ▒ ▒▒ ▓▒    ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▓░▒ ▒ ░ ▒░   ▒ ▒ 
                        ╔══╦╦╦╗╔══╦═╦╦╗      ░     ▒ ░░ ░▒ ▒░    ░ ▒  ▒   ░ ▒ ▒░   ▒ ░ ░ ░ ░░   ░ ▒░
                        ╚╗╔╣║═╣╚╗╔╣║║═╣     ░       ▒ ░░ ░░ ░     ░ ░  ░ ░ ░ ░ ▒    ░   ░    ░   ░ ░ 
                         ╚╝╚╩╩╝ ╚╝╚═╩╩╝       ░  ░  ░  v.2    ░.gg/onlp░ ░      ░ T E K K Y  ░   
                        ─═════════════════════════════════════☆☆═════════════════════════════════════─
                               Copyright: ONLP™ x Tekky © 2022 | Discord: .gg/onlp / Tekky#9999                       
                        ─═════════════════════════════════════☆☆═════════════════════════════════════─'''
    print(Colorate.Horizontal(Colors.blue_to_purple, txt, 1))
    print('\n')

    #how many links
    Write.Print("[?] How many links [1 to ∞] ↓\n", Colors.blue_to_purple, interval=0.001)
    links = Write.Input(" >  ", Colors.blue_to_purple, interval=0.5, hide_cursor=True)
    links = int(links)
    print('\n')

    for i in range(links):
        #url input
        Write.Print(f"[?] TikTok URL [{i}] ↓\n", Colors.blue_to_purple, interval=0.001)
        link_id = Write.Input(" >  ", Colors.blue_to_purple, interval=0.5, hide_cursor=True)
        raw_link = link_id

        try:
            if "vm.tiktok.com" in link_id or "vt.tiktok.com" in link_id:
                link_id = r.head(link_id, stream=True, allow_redirects=True, timeout=5).url.split("/")[5].split("?", 1)[0]
                links_list.append(link_id)
            else:
                link_id = link_id.split("/")[5].split("?", 1)[0]
                links_list.append(link_id)
        except:
            Write.Print('[*] Link not supported!!', Colors.red_to_white, interval=0.01)

            quit()


    #Write.Print(f'[*] Downloading: [{raw_link}]\n', Colors.blue_to_purple, interval=0.001)
    start_time = time()

    for z in range(links):
        Write.Print(f'[*] Downloading [{z}/{links}]: [ id = {links_list[z]} ]\n', Colors.blue_to_purple, interval=0.001)
        videoUrl = getVideoUrl(links_list[z])
        response = request.urlretrieve(videoUrl, f"./tiktok_vids/tiktok{random.randint(1000, 9999)}.mp4")
    Write.Print(f'[*] Status > Success [{links}/{links}] (Check "tiktok_vids" folder) | TTC > {round(time() - start_time, 1)}s\n',Colors.green_to_white, interval=0.001)

