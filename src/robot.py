import wpilib
#import ctre

from wpilib.drive import DifferentialDrive

class MyRobot(wpilib.IterativeRobot):
	#Motors canbus
	Left_Motor_Front 	= 8
	Right_Motor_Front 	= 7
	Left_Motor_Back 	= 9
	Right_Motor_Back 	= 6
	
	Front_Intake = 3
	
	#Joystick
	Joystick_Channel = 0
	def robotInit(self):
		#Mechanisms
		#self.F_Intake = ctre.WPI_TalonSRX(self.Front_Intake)
		
		#Joysticks
		self.Joystick = wpilib.Joystick(self.Joystick_Channel)
		
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
		pass
		#self.F_Intake.disable()
    
	def autonomousPeriodic(self):
		pass
    
	def teleopInit(self):
		self.My_Robot.setSafetyEnabled(True)
		
	#The function will get called around 50 times a second	
	def teleopPeriodic(self):
		self.My_Robot.tankDrive(self.Joystick.getY() * -1, self.Joystick.getY() * -1)
		
		#if self.Joystick.getButton(1):
		#	self.F_Intake.set(0.5)
		#else:
		#	self.F_Intake.set(0)
		
    
if __name__ == '__main__':
    wpilib.run(MyRobot)
