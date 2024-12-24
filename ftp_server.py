from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib.log import config_logging
import logging

# Konfigurasi logging
config_logging(level=logging.INFO)

class CustomFTPHandler(FTPHandler):
    connected_clients = 0
    
    def on_connect(self):
        CustomFTPHandler.connected_clients += 1
        print(f"[+] New connection from {self.remote_ip}:{self.remote_port}")
        print(f"[+] Current connected users: {CustomFTPHandler.connected_clients}")

    def on_disconnect(self):
        CustomFTPHandler.connected_clients -= 1
        print(f"[-] Disconnected from {self.remote_ip}:{self.remote_port}")
        print(f"[+] Current connected users: {CustomFTPHandler.connected_clients}")

# Buat pengguna dan izin
authorizer = DummyAuthorizer()
authorizer.add_user("admin", "admin", "/sdcard/FTP-SERVER/Admin", perm="elradfmwMT")
authorizer.add_anonymous("/sdcard/FTP-SERVER/Guest", perm="elr")

# Konfigurasi handler FTP
handler = CustomFTPHandler
handler.authorizer = authorizer

# Tentukan alamat dan port server
server_address = ("192.168.43.1", 8022)
server = FTPServer(server_address, handler)

# Tampilkan notifikasi saat server berjalan
print(f"[✓] Running on {server_address[0]}:{server_address[1]}")
print(f"[+] User {len(authorizer.user_table)}")

# Jalankan server
server.serve_forever()
