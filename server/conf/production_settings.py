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

######################################################################
# Contrib config
######################################################################
if SEND_GAME_INDEX:
    GAME_INDEX_LISTING = {
        'game_status': 'pre-alpha',
        # Optional, comment out or remove if N/A
        'game_website': 'http://ithirmush.org',
        'short_description': 'High fantasy MUSH in an original setting',
        # Optional but highly recommended. Markdown is supported.
        'long_description': (
            "Ithir is a MUX-style game in an original high-fantasy setting, "
            "inspired by Tolkien and set in an Elven society at odds. "
        ),
        'listing_contact': 'admin@ithirmush.org',
        # At minimum, specify this or the web_client_url options. Both is fine, too.
        'telnet_hostname': 'ithirmush.org',
        'telnet_port': 4000,
        # At minimum, specify this or the telnet_* options. Both is fine, too.
        'web_client_url': 'http://ithirmush.org/webclient/',
    }
