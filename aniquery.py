import requests
import keyboard as key
from fake_useragent import UserAgent
import subprocess
import time
from components import Res
import logging
from pprint import pprint

ua = UserAgent()

consumet = "http://172.22.56.187:3000"

def watch(query: str, episode_number: int):
    ep_num = f"-episode-{episode_number}"

    url = f"{consumet}/anime/gogoanime/watch/{query}{ep_num}"
    response = requests.get(url, params={"server": "gogocdn"}, headers={"User-Agent": str(ua.random)})
    status = response.raise_for_status()
    if response.status_code != 204:
        data = str(response.json())
        new_query = query.replace(":", "-")
        
        with open(f"{new_query}({ep_num}).txt", "w") as f:
            f.write(data.replace("}", "\n"))
            f.close()
        
        time.sleep(0.5)
        subprocess.call(["cmd", "/c", "cls"])
        time.sleep(0.5)

        res = Res(f"{new_query}({ep_num}).txt", "1080p", "720p")
        uri: str = res.find()
        print(uri)
        time.sleep(1)
        if uri:
            subprocess.call(['cmd', '/c', f'vlc {uri}'])
            subprocess.call(["cmd", "/c", f"del {new_query}({ep_num}).txt"])
        else:
            chosen_one = str(input("Input chosen url: "))
            subprocess.call(['cmd', '/c', f'vlc {chosen_one}'])
            subprocess.call(["cmd", "/c", f"del {new_query}({ep_num}).txt"])

        while True:
            if key.is_pressed("q"):
                exit(0)
            else:
                pass
        
    else:
        logging.error(f"Request timed out: [Error code: {status}]")
        exit(1)

def info(query):
    url = f"{consumet}/anime/gogoanime/info/{query}"
    response = requests.get(url, headers={"User-Agent": str(ua.random)})
    data = response.json()

    pprint(data)

def help():
        print('''
    Help menu:
        -h: help
        -i: info (shows you info about the anime)
        -w: watch
        ''')

def main():
    mode = str(input("What mode would you like to use? (-h for help): "))

    try:
        if mode == "-h":
            help()
            main()
        if mode == "-i":
            aniquery = input("What anime would you like to lookup?: ").replace(" ", "-")
            info(aniquery)
            main()
        if mode == "-w":
            aniquery = input("What anime would you like to watch? (enter full name): ").replace(" ", "-").replace("}", "\n")
            episode_number = input("What episode would you like to watch?: ")
            watch(aniquery, episode_number)
    except KeyboardInterrupt as Err:
        subprocess.call(["cmd", "/c", "cls"])
        print(f"Error: {Err}")
        exit(0)

if __name__ == "__main__":
    main()