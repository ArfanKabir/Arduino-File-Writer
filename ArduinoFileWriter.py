#Reading data from the Arduino program
import serial 
from datetime import datetime
import matplotlib.pyplot as plt
def graphData():
    arduinoFile = open("arduinoData.txt", "r"); #Opens the code that the arduino data was written into
    timeFile = open("Python36-32\\timeData.txt","r");#Opens the code that the time data was written into
    timeArray=[];#Time Data will be read into here
    arduinoArray = [];#Arduino Data will be read into here
    timeArray.append(0);#The index starts at 0
    arduinoArray.append(0);#The first thing read in will be a 0
    for line in timeFile:
        newLine = line.strip('\n');
        timeArray.append(newLine[17:19]);#This strips off all the arbitrary 
    counter = 0;#This counter is going to be needed for reading from the arduino file because there are spaces every even line
    print(timeArray);
    for line in arduinoFile:
        counter = counter+1;#Keeps track of the page line for readable data 
        print(line)
        if (counter%2==1):
            data = line.strip('\n');
            arduinoArray.append(data);#Makes sure that 
    print(arduinoArray);
    
    arduinoFile.close();
    timeFile.close();
    plt.xlabel("time(seconds)");
    plt.ylabel("Number of people");
    plt.suptitle('Bidirectional Counter',fontsize=20);
    plt.plot(timeArray,arduinoArray);
    plt.show();

ser = serial.Serial('COM8', baudrate = 9600);#Opens up the arduino so that it can be used by the game
arduinoFile = open("C:\\Python36-32\\arduinoData.txt", "w");
#Creates a file that the data writes into
timeFile = open("C:\\Python36-32\\timeData.txt","w");
try:
    while 1:
        arduinoData=ser.readline().decode('ascii');#While the loop runs, the data is going to be read into this variable
        #Decode allows the data to be read as number instead of in bits
        print(arduinoData+"\n");
        arduinoFile.write(arduinoData);#This writes into the file
        time=datetime.now();
        timeFile.write(str(time)+"\n");
except KeyboardInterrupt:
    arduinoFile.close();#The file in then closed.
    timeFile.close();
    graphData();
    
    
