from __future__ import print_function
import serial

connected = False

locations = ["/dev/ttyACM0","/dev/ttyACM1"]

for device in locations:
  try:
    print('trying',device)
    ser = serial.Serial(device,9600)
    print("Connected OK")
    break
  except:
    print("Failed to connect")

# This loop looks spurious
while not connected:
  serin = ser.read()
  connected = True

test_file = open("logging_data.txt",'w')

while True:
  try:
    if(ser.inWaiting()):
      x = ser.readline()
      print(x,end="")
      test_file.write(x)
      test_file.flush()
  except:
    print("Bye")
    break

test_file.close()
ser.close()
