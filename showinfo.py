import os, socket, psutil, math
from requests import get

class colores():
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def getHostName():
    hostname = socket.gethostbyaddr(socket.gethostname())[0]
    return hostname


def getIpAddress():
    try: 
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return (colores.FAIL + "Hubo un problema obteniendo la ip" + colores.ENDC)


def publicIp():
    #pub_ip = json.loads(urllib.request.urlopen('https://ifconfig.me/').read())[0]
    miIp = get("https://api.ipify.org").text
    return miIp


def getRam():
    maxRam = (psutil.virtual_memory().total / 1000 / 1000).__trunc__()
    usedRam = (psutil.virtual_memory().used / 1000 / 1000).__trunc__()
    # Este seria la RAM disponible contando la cacheada
    #usedRam = (psutil.virtual_memory().free / 1000 / 1000).__trunc__()
    return maxRam, usedRam


host = getHostName()
ip = getIpAddress()
pubIp= publicIp()
maxRam = getRam()[0]
usedRam = getRam()[1]

print(f"""
Public IP: {colores.OKGREEN + pubIp + colores.ENDC}
IP: {colores.OKGREEN + ip + colores.ENDC}
Hostname: {colores.OKGREEN + host + colores.ENDC}

Max ram: {colores.WARNING + str(maxRam) + colores.ENDC} MB
Used ram: {colores.WARNING + str(usedRam) + colores.ENDC} MB
""")