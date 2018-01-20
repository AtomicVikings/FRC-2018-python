import wpilib
import ctre

from wpilib import RobotDrive

class MyRobot(wpilib.IterativeRobot):
	#Motors canbus
	Left_Motor = 1
	Right_Motor = 2
	Front_Intake = 3
	
	#Joystick
	Joystick_Channel = 0
    def robotInit(self):
		self.F_Intake = ctre.WPI_TalonSRX(Front_Intake)
		self.Joystick = wpilib.Joystick(Joystick_Channel)
		
	def disabledPeriodic(self):
		self.F_Intake.disable()
    
    def autonomousPeriodic(self):
        pass
    
    def teleopInit(self):
        pass
    
    def teleopPeriodic(self):
		if Joystick.getButton(1):
			self.F_Intake.set(0.5)
		else:
			self.F_Intake.set(0)
		
    
if __name__ == '__main__':
    wpilib.run(MyRobot)
