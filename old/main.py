from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
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
                         ╚╝╚╩╩╝ ╚╝╚═╩╩╝       ░  ░  ░  v.3    ░.gg/onlp░ ░        T E K K Y  ░   
                        ─═════════════════════════════════════☆☆═════════════════════════════════════─
                               Copyright: ONLP™ x Tekky © 2022 | Discord: .gg/onlp / Tekky#9999                       
                        ─═════════════════════════════════════☆☆═════════════════════════════════════─'''
    print(Colorate.Horizontal(Colors.blue_to_purple, txt, 1))
    print('\n')

    #how many links
    Write.Print("Do you want to download videos from a profile [y/n] ↓\n", Colors.blue_to_purple, interval=0.001)
    choice = Write.Input(" >  ", Colors.blue_to_purple, interval=0.5, hide_cursor=True)
    print('\n')

    if choice == 'y':
        # how many links
        Write.Print("[?] Username [@xxxx] ↓\n", Colors.blue_to_purple, interval=0.001)
        user = Write.Input(" >  ", Colors.blue_to_purple, interval=0.5, hide_cursor=True)

        print('\n')

        headers = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        }
        if "@" in user:
            req = Request(f"https://www.tiktok.com/{user}", headers=headers)
        else:
            req = Request(f"https://www.tiktok.com/@{user}", headers=headers)
        html_page = urlopen(req)
        soup = BeautifulSoup(html_page, "lxml")
        links = []
        for link in soup.findAll('a'):
            links.append(link.get('href'))
        x = 0

        for l in links:
            if len(l) >= 54:
                if "business" in l:
                    pass
                elif "legal" in l:
                    pass
                else:
                    l = l.split("/")[5].split("?", 1)[0]
                    links_list.append(l)
                    x += 1
        Write.Print(f"[*] Videos found: {x}\n", Colors.blue_to_purple, interval=0.001)

        start_time = time()

        for z in range(x):
            Write.Print(f'[*] Downloading [{z}/{x}]: [ id = {links_list[z]} ]\n', Colors.blue_to_purple, interval=0.001)
            videoUrl = getVideoUrl(links_list[z])
            response = request.urlretrieve(videoUrl, f"./tiktok_vids/tiktok_{user}_{random.randint(1000, 9999)}.mp4")
        Write.Print(f'[*] Status > Success [{x}/{x}] (Check "tiktok_vids" folder) | TTC > {round(time() - start_time, 1)}s\n', Colors.green_to_white, interval=0.001)
        quit()
    else:
        pass

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


    #Write.Print(f'[*] Downloading: [{raw_link}]\n', Colors.blue_to_purple, interval=0.001
    start_time = time()

    for z in range(links):
        Write.Print(f'[*] Downloading [{z}/{links}]: [ id = {links_list[z]} ]\n', Colors.blue_to_purple, interval=0.001)
        videoUrl = getVideoUrl(links_list[z])
        response = request.urlretrieve(videoUrl, f"./tiktok_vids/tiktok{random.randint(1000, 9999)}.mp4")
    Write.Print(f'[*] Status > Success [{links}/{links}] (Check "tiktok_vids" folder) | TTC > {round(time() - start_time, 1)}s\n',Colors.green_to_white, interval=0.001)
