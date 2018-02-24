import wpilib
import ctre

from wpilib.drive import DifferentialDrive

import auto
import drive
import customParsing

# I moved all teleop code to a seporate drive.py file, so that we wouldn't have to change things in multiple files doing the read/write auton
# Deploying complains and errors, but the code itself works

class MyRobot(wpilib.IterativeRobot):
	#Motors pwm
	Left_Motor_Front 	= 8
	Right_Motor_Front 	= 7
	Left_Motor_Back 	= 9
	Right_Motor_Back 	= 6
	
	#Motors pwm 
	Climber_Motor 		= 5
	
	#Motors can
	Elevator_Motor 		= 1
	Left_Front_Intake 	= 2
	Right_Front_Intake 	= 3
	
	#Joystick
	Joystick_Channel 		= 0
	Sec_Joystick_Channel 	= 1
	def robotInit(self):
		#Joysticks
		self.Joystick = wpilib.Joystick(self.Joystick_Channel)
		self.Sec_Joystick = wpilib.Joystick(self.Sec_Joystick_Channel)
		
		#Magnetic Limit Switches
		self.switch1 = wpilib.DigitalInput(0)
		
		#Mechanisms
		self.Elevator = ctre.WPI_TalonSRX(self.Elevator_Motor)
		self.LF_Intake = ctre.WPI_TalonSRX(self.Left_Front_Intake)
		self.RF_Intake = ctre.WPI_TalonSRX(self.Right_Front_Intake)
		
		#PWM Mechanisms
		self.Climber = wpilib.Talon(self.Climber_Motor)
		
		#Drive Motors
		self.LMF = wpilib.Talon(self.Left_Motor_Front) 
		self.RMF = wpilib.Talon(self.Right_Motor_Front)
		self.LMB = wpilib.Talon(self.Left_Motor_Back)
		self.RMB = wpilib.Talon(self.Right_Motor_Back)
		
		self.Left = wpilib.SpeedControllerGroup(self.LMF, self.LMB)
		self.Right = wpilib.SpeedControllerGroup(self.RMF, self.RMB)
        
		#This is not the built-in robot drive 
		self.My_Robot = DifferentialDrive(self.Left, self.Right)
		self.My_Robot.setExpiration(0.1)
		
		#SmartDashboard
		self.spChooser = wpilib.SendableChooser()
		self.spChooser.addDefault("Left", 1)
		self.spChooser.addObject("Middle", 2)
		self.spChooser.addObject("Right", 3)
		wpilib.SmartDashboard.putData('StartingPosition', self.spChooser)
		
		self.amChooser = wpilib.SendableChooser()
		self.amChooser.addDefault("Scale", 1)
		self.amChooser.addObject("Other Lever", 2)
		self.amChooser.addObject("Line", 3)
		self.amChooser.addObject("None", 0)
		wpilib.SmartDashboard.putData('AutoMode', self.amChooser)
		
		self.writeAutoChooser = wpilib.SendableChooser()
		self.writeAutoChooser.addDefault("Read Auto", 0)
		self.writeAutoChooser.addObject("Write Auto", 1)
		wpilib.SmartDashboard.putData('WriteAuto', self.writeAutoChooser)
		
		self.infoChooser = wpilib.SendableChooser()
		self.infoChooser.addDefault("0", 0)
		for line in customParsing.read():
			self.infoChooser.addObject(line, line)
		wpilib.SmartDashboard.putData("InfoChooserChannel", self.infoChooser)
	
	def disabledPeriodic(self):
		self.Elevator.disable()
		self.LF_Intake.disable()
		self.RF_Intake.disable()
		self.Climber.disable()
    
	def autonomousPeriodic(self):
		self.startPos = self.spChooser.getSelected()
		self.autoMode = self.amChooser.getSelected()
		
		auto.Autonomous(self, self.startPos, self.autoMode)
    
	def teleopInit(self):
		self.My_Robot.setSafetyEnabled(True)
		
	#The function will get called around 50 times a second	
	def teleopPeriodic(self):
		print(self.switch1.get())
	
		if self.writeAutoChooser.getSelected() == 1:
			auto.Autonomous.writeCode(self)
		else:
			drive.drive(self, self.Joystick.getRawAxis(4), self.Joystick.getY(), self.Sec_Joystick.getRawButton(1), self.Sec_Joystick.getRawButton(2), self.Sec_Joystick.getRawButton(3), self.Sec_Joystick.getRawButton(4), self.Sec_Joystick.getRawButton(5), self.Sec_Joystick.getRawButton(6), self.Sec_Joystick.getRawButton(7), self.Sec_Joystick.getRawButton(8))
		
    
if __name__ == '__main__':
    wpilib.run(MyRobot)
