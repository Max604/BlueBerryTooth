from threading import Thread
import socket
import time
import sys

verbose = True
port = 22000

def debug(text):
    if verbose:
        print("Debug---:%s" % text)

class SocketHandler(Thread):
    def __init__(self, conn):
        Thread.__init__(self)
        self.conn = conn

    def run(self):
        global isConnected
        debug("SocketHandler started")
        while True:
            cmd = []
            try:
                debug("Calling blocking conn.recv()")
                cmd = self.conn.recv(1024)
            except:
                debug("exception in conn.recv()")
                break
            debug("Received cmd: " + cmd.decode("utf-8") + " len: " + cmd.decode("utf-8"))
            if len(cmd.decode("utf-8")) == 0:
                break
            self.executeCommand(cmd.decode("utf-8"))
        conn.close()
        print("Client disconnected. Waiting for next client...")
        isConnected = False
        debug("SocketHandler terminated")

    def executeCommand(self, cmd):
        debug("Calling executeCommand() with cmd: ")
        if cmd[:-1] == "go":
            print("Reporting that command 'go' was received")
            self.conn.sendall(("go was received by the server" + "\0").encode("utf-8"))


serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
debug("Socket Created")
hostname = ""
try:
    serverSocket.bind((hostname, port))
except socket.error as msg:
    print("Bind failed", msg[0], msg[1])
    sys.exit()
serverSocket.listen(10)

print("Waiting for a connecting client...")
isConnected = False
while True:
    debug("Calling blocking accept()...")
    conn, addr = serverSocket.accept()
    print("Connected with client at " + addr[0])
    isConnected = True
    socketHandler = SocketHandler(conn)
    socketHandler.setDaemon(True)
    socketHandler.start()
    t = 0
    while isConnected:
        print("Server connected at", t, "s")
        time.sleep(10)
        t += 10