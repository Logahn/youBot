"""
Conveyor controller: Moves the conveyor belt until the 
cube reaches a specified position.
"""

from controller import Robot

robot = Robot()

motor = robot.getDevice("belt motor")
motor.setVelocity(0.2)
motor.setPosition(0.75)
