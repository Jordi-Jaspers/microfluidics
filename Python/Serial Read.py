import serial
import csv

file = 'ArduinoData_Jordi_Jaspers.csv'

port = 'COM3'
baudRate = 9600
fileMode = 'w'

arduino = serial.Serial(port, baudRate) 
arduino.flush()
arduino.reset_input_buffer()

print("Arduino Connected @ COM3!")

with open(file, fileMode, newline = '') as WriteFile:
	writer = csv.writer(WriteFile)
	print('file opened!')
	while (True):
		while (arduino.inWaiting() == 0):
			pass
		try:
			arduinoData = arduino.readline()
			inputArray = arduinoData.decode().rstrip().split(',')
			inputArray = list(map(int, inputArray))
			arduino.reset_input_buffer()
			print(inputArray)
			if(len(inputArray) > 10):
				writer.writerow(inputArray)
			else:
				print('Need more data!')
		except (KeyboardInterrupt, SystemExit, IndexError, ValueError):
			pass
			WriteFile.close()
			break