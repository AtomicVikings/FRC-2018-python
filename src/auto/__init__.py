import wpilib
import time
import logging
import linecache

import drive

class Autonomous:
	def __init__(self, robotMain, startPos, autoMode):
		self.My_Robot = robotMain.My_Robot
		self.startPos = startPos
		self.autoMode = autoMode
		self.gameData = wpilib.DriverStation.getInstance().getGameSpecificMessage()
		self.gameData = str(self.gameData)
		
		self.startTime = time.time()
		
		if self.autoMode == 0:
			self.none()
		elif self.startPos == 1: #Left
			#self.readCode(robotMain, 1519486977.4369483)
			if self.autoMode == 1: #Scale
				if self.gameData[1] == 'L':
					pass
				elif self.gameData[1] == 'R':
					pass
				else:
					self.none()
			elif self.autoMode == 2: #Lever
				if self.gameData[0] == 'L':
					pass
				elif self.gameData[0] == 'R':
					pass
				else:
					self.none() 
			elif self.autoMode == 3: #Line
				pass 
		elif self.startPos == 2: #Middle
			if self.autoMode == 1: #Scale
				if self.gameData[1] == 'L':
					pass
				elif self.gameData[1] == 'R':
					pass
				else:
					self.none()
			elif self.autoMode == 2: #Lever
				if self.gameData[0] == 'L':
					pass
				elif self.gameData[0] == 'R':
					pass
				else:
					self.none() 
			elif self.autoMode == 3: #Line
				pass
		elif self.startPos == 3: #Right
			if self.autoMode == 1: #Scale
				if self.gameData[1] == 'L':
					pass
				elif self.gameData[1] == 'R':
					pass
				else:
					self.none()
			elif self.autoMode == 2: #Lever
				if self.gameData[0] == 'L':
					pass
				elif self.gameData[0] == 'R':
					pass
				else:
					self.none() 
			elif self.autoMode == 3: #Line
				pass
		else:
			self.none()
	def none(self):
		while wpilib.DriverStation.getInstance().isEnabled() and time.time() - self.startTime < 15:
			drive.drive(robotMain, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
	def writeCode(robotMain):
		timeVar = time.time()
		fileName = "/home/lvuser/auto.txt"
		
		file = open(fileName, "a")
		
		line = "[" + str(timeVar) + "\n"
		file.write(line)
		
		while wpilib.DriverStation.getInstance().isEnabled() and timeVar + 15 > time.time():
			line = str(robotMain.Joystick.getRawAxis(4)) + "," + str(robotMain.Joystick.getY()) + "," + str(int(robotMain.Sec_Joystick.getRawButton(1))) + "," + str(int(robotMain.Sec_Joystick.getRawButton(2))) + "," + str(int(robotMain.Sec_Joystick.getRawButton(3))) + "," + str(int(robotMain.Sec_Joystick.getRawButton(4))) + "," + str(int(robotMain.Sec_Joystick.getRawButton(5))) + "," + str(int(robotMain.Sec_Joystick.getRawButton(6))) + "," + str(int(robotMain.Sec_Joystick.getRawButton(7))) + "," + str(int(robotMain.Sec_Joystick.getRawButton(8))) + "\n"
			file.write(line)
			drive.drive(robotMain, robotMain.Joystick.getX(), robotMain.Joystick.getY(), robotMain.Sec_Joystick.getRawButton(1), robotMain.Sec_Joystick.getRawButton(2), robotMain.Sec_Joystick.getRawButton(3), robotMain.Sec_Joystick.getRawButton(4), robotMain.Sec_Joystick.getRawButton(5), robotMain.Sec_Joystick.getRawButton(6), robotMain.Sec_Joystick.getRawButton(7), robotMain.Sec_Joystick.getRawButton(8))

		while wpilib.DriverStation.getInstance().isEnabled() and timeVar + 15 < time.time():
			drive.drive(robotMain, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
			robotMain.My_Robot.tankDrive(0, 0)
	
		file.write("]\n")
		file.close()
	
	def readCode(self, robotMain, recTime):

		timeVar = time.time()
		fileName = "/home/lvuser/auto.txt"
	
		#debugFileName = "/home/lvuser/debug.txt"
		#debugFile = open(debugFileName, "a")
	
		startLine = 0
		endLine = 0
	
		completeTime=12.730631828308105
	
		count = 0
	
		recTimeString = "[" + str(recTime)
	
		with open(fileName) as file:
			for line in file:
				count += 1
				if recTimeString in line:
					startLine = count
				if startLine != 0 and endLine == 0 and "]" in line:
					endLine = count
					break
	
		count = 1
	
		while wpilib.DriverStation.getInstance().isEnabled() and timeVar + 15 > time.time() and count + startLine < endLine - 1:
			count += (completeTime / 15)
			line = linecache.getline(fileName, int(round(count + startLine)))
			lineList = line.split(',')
		
			drive.drive(robotMain, float(lineList[0]), float(lineList[1]), bool(int(lineList[2])), bool(int(lineList[3])), bool(int(lineList[4])), bool(int(lineList[5])), bool(int(lineList[6])), bool(int(lineList[7])), bool(int(lineList[8])), bool(int(lineList[9])))
		#debugFile.write(str(time.time() - timeVar) + "\n")
		#debugFile.close()
	
		timeEndVar = time.time() - timeVar
		while wpilib.DriverStation.getInstance().isEnabled() and timeVar + 15 > time.time():
			drive.drive(robotMain, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
			print(timeEndVar)
	
		linecache.clearcache()