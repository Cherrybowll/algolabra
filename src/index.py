from utilities.rsa import RSA
from utilities.filehelper import FileHelper
from utilities.messagehelper import MessageHelper
from ui import UI

rsa_handler = RSA()
file_handler = FileHelper()
message_handler = MessageHelper()
ui = UI(rsa_handler, file_handler, message_handler)

ui.start()
