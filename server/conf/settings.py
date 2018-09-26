from base_settings import *
    
TELNET_PORTS = [4000]
WEBSERVER_PORTS = [(4001, 4002)]
SERVERNAME = "Ithir"
GAME_SLOGAN = "The Return to Glory"

try:
    from server.conf.secret_settings import *
except ImportError:
    print("secret_settings.py file not found or failed to import.")