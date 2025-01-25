from utilities.rsa import RSA
from ui import UI

rsa_handler = RSA()
ui = UI(rsa_handler)

ui.start()
