"""
Settings we use for production. Some of these could eventually be moved into a settings.ini file
"""
from .base_settings import *
TELNET_INTERFACES = ['45.33.87.194']
WEBSOCKET_CLIENT_INTERFACE = '45.33.87.194'
ALLOWED_HOSTS = ['.ithirMUSH.org']
WEBSERVER_PORTS = [(8000, 5001)]
WEBSOCKET_CLIENT_PORT = 8001
SSH_PORTS = [8022]
SSL_PORTS = [4001]
AMP_PORT = 5000
SITE_HEADER = "ArxPrime Admin"
INDEX_TITLE = "ArxPrime Admin"
IDMAPPER_CACHE_MAXSIZE = 4000
CHECK_VPN = True
MAX_CHAR_LIMIT = 8000
SERVERTZ = 'US/Pacific'

