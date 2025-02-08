from utilities.rsa import RSA
from utilities.filehelper import FileHelper
from ui import UI

rsa_handler = RSA()
file_handler = FileHelper()
ui = UI(rsa_handler, file_handler)

ui.start()
