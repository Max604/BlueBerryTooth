from threading import Thread
import socket, time

verbose = True
ip_address = "127.0.0.1"
port = 22000

def debug(text):
    if verbose:
        print("Debug:--- %s", text)

class Receiver(Thread):
    def run(self):
        debug("Receiver thread started")
        while True:
            try:
                rxData = self.readServerData()
            except:
                debug("Exception in Receiver.run()")
                isReceiverRunning = False
                closeConnection()
                break
        debug("Receiver thread terminated")

    def readServerData(self):
        debug("Calling readResponse")
        bufSize = 4096
        data = ""
        while data[-1:] != "\0":
            try:
                blk = sock.recv(bufSize)
                if blk != None:
                    blk = blk.decode("utf-8")[:-1]
                    debug("Received data block from server, " + blk + " len: " + \
                          str(len(blk)))
                else:
                    debug("sock.recv() returned with None")
            except:
                raise Exception("Exception from blocking sock.recv()")
            data += blk
        print("Data received:", data)

def startReceiver():
    debug("Starting Receiver thread")
    receiver = Receiver()
    receiver.start()

def sendCommand(cmd):
    debug("sendCommand() with cmd = " + cmd)
    try:
        # append \0 as end-of-message indicator
        sock.sendall((cmd + "\0").encode("utf-8"))
    except socket.error as msg:
        debug("Exception in sendCommand()" + msg[0])
        closeConnection()

def closeConnection():
    global isConnected
    debug("Closing socket")
    sock.close()
    isConnected = False

def connect():
    global sock
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    debug("Connecting...")
    try:
        sock.connect((ip_address, port))
    except:
        debug("Connection failed.")
        return False
    startReceiver()
    return True

sock = None
isConnected = False

if connect():
    isConnected = True
    print("Connection established")
    time.sleep(1)
    while isConnected:
        print("Sending command: go...")
        sendCommand("go")
        time.sleep(2)
else:
    print("Connection to %s:%d failed" % (ip_address, port))
print("Done")