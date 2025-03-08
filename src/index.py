from utilities.rsa import RSA
from utilities.filehelper import FileHelper
from utilities.messagehelper import MessageHelper
from utilities.randomhelper import RandomHelper
from ui import UI


random_handler = RandomHelper()
rsa_handler = RSA(random_handler)
file_handler = FileHelper()
message_handler = MessageHelper()
ui = UI(rsa_handler, file_handler, message_handler)

ui.start()
