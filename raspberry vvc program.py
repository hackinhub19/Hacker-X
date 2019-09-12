Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import RPi.GPIO as GPIO
from google.cloud import storage

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name))
GPIO.setmode(GPIO.BCM)
GPIO.setup(MotL_A, GPIO.OUT)
GPIO.setup(MotL_B, GPIO.OUT)
GPIO.setup(MotR_A, GPIO.OUT)
GPIO.setup(MotR_B, GPIO.OUT)
server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
port = 1
server_socket.bind(("", port))
server_socket.listen(1)
client_socket, address = server_socket.accept()
print ("Accepted connection from "), address


def Forward():
    GPIO.output(MotL_A, 1)
    GPIO.output(MotL_B, 0)
    GPIO.output(MotR_A, 0)
    GPIO.output(MotR_A, 1)


def Backward():
    GPIO.output(MotL_A, 0)
    GPIO.output(MotL_B, 1)
    GPIO.output(MotR_A, 1)
    GPIO.output(MotR_A, 0)


def Left():
    GPIO.output(MotL_A, 0)
    GPIO.output(MotL_B, 0)
    GPIO.output(MotR_A, 0)
    GPIO.output(MotR_A, 1)


def Right():
    GPIO.output(MotL_A, 1)
    GPIO.output(MotL_B, 0)
    GPIO.output(MotR_A, 0)
    GPIO.output(MotR_A, 0)


def Stop():
    GPIO.output(MotL_A, 0)
    GPIO.output(MotL_B, 0)
    GPIO.output(MotR_A, 0)
    GPIO.output(MotR_A, 0)


data = ""
while (True):
    character= client_socket.recv(1024)
    print ("Received: %s") % character
    if (character== "F"): # Moving Forward
        Forward()
    elif (character== "B"): #Moving Backward
        Backward()
    elif (character== "L"): #Turning Left
        Left()
        time.sleep(1)
        Stop()
    elif (character== "R"): #Turning Right
        Right()
        time.sleep(1)
        Stop()
    elif(character=="C"): #Rotating Clockwise
        Right()
    elif(character="A"):  #Rotating Anticlockwise
        Left()
    elif (data == "S"):    #Robot Stop
        Stop()

client_socket.close()
server_socket.close()
