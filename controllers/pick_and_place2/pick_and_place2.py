"""youBot controller for picking a cube from the robot carrier and 
    placing it in the box."""

from controller import Robot

# Create the Robot instance.
robot = Robot()

# Get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

#! Inizialize base motors.
wheels = []
wheels.append(robot.getDevice("wheel1"))
wheels.append(robot.getDevice("wheel2"))
wheels.append(robot.getDevice("wheel3"))
wheels.append(robot.getDevice("wheel4"))
for wheel in wheels:
    # Activate controlling the motors setting the velocity.
    # Otherwise by default the motor expects to be controlled in force or position,
    # and setVelocity will set the maximum motor velocity instead of the target velocity.
    wheel.setPosition(float('+inf'))

#! Initialize arm motors.
armMotors = []
armMotors.append(robot.getDevice("arm1"))
armMotors.append(robot.getDevice("arm2"))
armMotors.append(robot.getDevice("arm3"))
armMotors.append(robot.getDevice("arm4"))
armMotors.append(robot.getDevice("arm5"))
# Set the maximum motor velocity.
armMotors[0].setVelocity(1.5) # maxVelocity = 1.5
armMotors[1].setVelocity(1.5)
armMotors[2].setVelocity(1.5)
armMotors[3].setVelocity(0.5)
armMotors[4].setVelocity(1.5)

#! Initialize arm position sensors.
# These sensors can be used to get the current 
# joint position and monitor the joint movements.
armPositionSensors = []
armPositionSensors.append(robot.getDevice("arm1sensor"))
armPositionSensors.append(robot.getDevice("arm2sensor"))
armPositionSensors.append(robot.getDevice("arm3sensor"))
armPositionSensors.append(robot.getDevice("arm4sensor"))
armPositionSensors.append(robot.getDevice("arm5sensor"))
for sensor in armPositionSensors:
    sensor.enable(timestep)

#! Initialize gripper motors.
finger1 = robot.getDevice("finger1")
finger2 = robot.getDevice("finger2")
# Set the maximum motor velocity.
finger1.setVelocity(1.5)
finger2.setVelocity(1.5) # 0.03
# Read the miminum and maximum position of the gripper motors.
fingerMinPosition = finger1.getMinPosition()
fingerMaxPosition = finger1.getMaxPosition()

#! Generic forward motion function
def forward(time):
    for wheel in wheels:
        wheel.setVelocity(7.0) # maxVelocity = 14.81
    robot.step(time * timestep)

#! Generic stop function
def halt():
    for wheel in wheels:
        wheel.setVelocity(0.0)

def pick_up():
    armMotors[0].setPosition(1.7)
    armMotors[1].setPosition(-1)
    armMotors[2].setPosition(-1)
    armMotors[3].setPosition(0)
    finger1.setPosition(fingerMaxPosition)
    finger2.setPosition(fingerMaxPosition)

def close_grippers():
    finger1.setPosition(0.013)     # Close gripper.
    finger2.setPosition(0.013)

def hand_up():
    armMotors[0].setPosition(0)
    armMotors[1].setPosition(0)
    armMotors[2].setPosition(0)
    armMotors[3].setPosition(0)
    armMotors[4].setPosition(0)

def fold_arms():
    armMotors[0].setPosition(-2.9)
    armMotors[1].setPosition(1.5)
    armMotors[2].setPosition(-2.6)
    armMotors[3].setPosition(1.7)
    armMotors[4].setPosition(0)

def drop():
    # Move arm down
    armMotors[3].setPosition(0)
    armMotors[2].setPosition(-0.3)
    robot.step(100 * timestep)

    armMotors[1].setPosition(-1.0)
    robot.step(100 * timestep)

    armMotors[3].setPosition(-1.5)
    robot.step(100 * timestep)

    armMotors[2].setPosition(-0.4)
    robot.step(50 * timestep)
    armMotors[4].setPosition(-1)

    # Open gripper.
    finger1.setPosition(fingerMaxPosition)
    finger2.setPosition(fingerMaxPosition)
    robot.step(50 * timestep)

halt()
robot.step(1100 * timestep)
pick_up()
robot.step(400 * timestep)
close_grippers()
robot.step(100 * timestep)
hand_up()
# forward(20)
# halt()
drop()
# hand_up()
fold_arms()


