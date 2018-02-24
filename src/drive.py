import wpilib
import ctre

def drive(robotMain, JoyY, JoyX, b1, b2, b3, b4, b5, b6, b7, b8):
	robotMain.My_Robot.tankDrive(JoyY * 1 - JoyX, JoyY * -1 - JoyX)
		
	if b5 == True:
		robotMain.RF_Intake.set(-0.5)
	elif b7 == True:
		robotMain.RF_Intake.set(0.5)
	else:
		robotMain.RF_Intake.set(0)
		
	if b6 == True:
		robotMain.LF_Intake.set(0.5)
	elif b8 == True:
		robotMain.LF_Intake.set(-0.5)
	else:
		robotMain.LF_Intake.set(0)
		
	if b2 == True:
		robotMain.Elevator.set(0.5)
	elif b3 == True:
		robotMain.Elevator.set(-0.5)
	else:
		robotMain.Elevator.set(0)
	
	if b1 == True:
		robotMain.Climber.set(0.5)
	elif b4 == True:
		robotMain.Climber.set(-0.5)
	else:
		robotMain.Climber.set(0)