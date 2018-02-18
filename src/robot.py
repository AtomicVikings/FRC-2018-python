import wpilib
import ctre

from wpilib.drive import DifferentialDrive

class MyRobot(wpilib.IterativeRobot):
	#Motors pwm
	Left_Motor_Front 	= 8
	Right_Motor_Front 	= 7
	Left_Motor_Back 	= 9
	Right_Motor_Back 	= 6
	
	#Motors can
	Elevator_Motor 		= 1
	Left_Front_Intake 	= 2
	Right_Front_Intake 	= 3
	Climber_Motor		= 4
	
	#Joystick
	Joystick_Channel 		= 0
	Sec_Joystick_Channel 	= 1
	def robotInit(self):
		#Mechanisms
		self.Elevator = ctre.WPI_TalonSRX(self.Elevator_Motor)
		self.LF_Intake = ctre.WPI_TalonSRX(self.Left_Front_Intake)
		self.RF_Intake = ctre.WPI_TalonSRX(self.Right_Front_Intake)
		self.Climber = ctre.WPI_TalonSRX(self.Climber_Motor)
		
		#Joysticks
		self.Joystick = wpilib.Joystick(self.Joystick_Channel)
		self.Sec_Joystick = wpilib.Joystick(self.Sec_Joystick_Channel)
		
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
	
	def disabledPeriodic(self):
		self.Elevator.disable()
		self.LF_Intake.disable()
		self.RF_Intake.disable()
		self.Climber.disable()
    
	def autonomousPeriodic(self):
		pass
    
	def teleopInit(self):
		self.My_Robot.setSafetyEnabled(True)
		
	#The function will get called around 50 times a second	
	def teleopPeriodic(self):
		self.My_Robot.tankDrive(self.Joystick.getY() * -1, self.Joystick.getY() * -1)
		
		if self.Sec_Joystick.getRawButton(5):
			self.LF_Intake.set(0.5)
		elif self.Sec_Joystick.getRawButton(7):
			self.LF_Intake.set(-0.5)
		else:
			self.LF_Intake.set(0)
			
		if self.Sec_Joystick.getRawButton(6):
			self.RF_Intake.set(0.5)
		elif self.Sec_Joystick.getRawButton(8):
			self.RF_Intake.set(-0.5)
		else:
			self.RF_Intake.set(0)
			
		if self.Sec_Joystick.getRawButton(2):
			self.Elevator.set(0.5)
		elif self.Sec_Joystick.getRawButton(3):
			self.Elevator.set(-0.5)
		else:
			self.Elevator.set(0)
		
		if self.Sec_Joystick.getRawButton(1):
			self.Climber.set(0.5)
		elif self.Sec_Joystick.getRawButton(4):
			self.Climber.set(-0.5)
		else:
			self.Climber.set(0)
		
    
if __name__ == '__main__':
    wpilib.run(MyRobot)
