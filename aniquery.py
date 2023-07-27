import requests
from fake_useragent import UserAgent
import subprocess
import time
from components import Get

ua = UserAgent()

consumet = "https://api.consumet.org"

def info(query):
    url = f"{consumet}/anime/gogoanime/info/{query}"
    response = requests.get(url, headers={"User-Agent": str(ua.chrome)})
    data = response.json()

    print(data)

def watch(query: str, episode_number: int):
    ep_num = f"-episode-{episode_number}"

    url = f"{consumet}/anime/gogoanime/watch/{query}{ep_num}"
    response = requests.get(url, params={"server": "gogocdn"}, headers={"User-Agent": str(ua.chrome)})
    data = str(response.json())
    new_query = query.replace(":", "-")
    
    with open(f"{new_query}({ep_num}).txt", "w") as f:
        f.write(data.replace("}", "\n"))
        f.close()
    
    time.sleep(0.5)
    subprocess.call(["cmd", "/c", "cls"])
    time.sleep(0.5)

    uri = Get.text(f"{new_query}({ep_num}).txt")
    print(uri)
    chosen_one = str(input("Input chosen url: "))
    subprocess.call(["cmd", "/c", f"del {new_query}({ep_num}).txt"])
    time.sleep(1)
    subprocess.call(['cmd', '/c', f'C:/VLC/vlc.exe {chosen_one}'])

    while True:
        pass


mode = str(input("What mode would you like to use? (-h for help): "))

try:
    if mode == "-h":
        print('''
    Help menu:
        -h: help
        -i: info (shows you info about the anime)
        -w: watch
        ''')
        exit()
    if mode == "-i":
        aniquery = input("What anime would you like to lookup?: ").replace(" ", "-")
        info(aniquery)
    if mode == "-w":
        aniquery = input("What anime would you like to watch? (enter full name): ").replace(" ", "-").replace("}", "\n")
        episode_number = input("What episode would you like to watch?: ")
        watch(aniquery, episode_number)
except KeyboardInterrupt:
    subprocess.call(["cmd", "/c", "cls"])
    exit()