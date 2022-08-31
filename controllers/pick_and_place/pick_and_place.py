"""youBot controller for picking a cube from the conveyor and placing it in a box."""

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
# These sensors can be used to get the current joint position and monitor the joint movements.
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
def forward():
    for wheel in wheels:
        wheel.setVelocity(7.0) # maxVelocity = 14.81

#! Generic stop function
def halt():
    for wheel in wheels:
        wheel.setVelocity(0.0)

def fold_arms():
    armMotors[0].setPosition(-2.9)
    armMotors[1].setPosition(1.5)
    armMotors[2].setPosition(-2.6)
    armMotors[3].setPosition(1.7)
    armMotors[4].setPosition(0)

def stretch_arms():
    armMotors[0].setPosition(2.9)
    armMotors[1].setPosition(-1.0)
    armMotors[2].setPosition(2.5)
    armMotors[3].setPosition(-1.7)
    armMotors[4].setPosition(0)

def turn_around():
#TODO: robot.step(70 * timestep) - produces a 90 degrees turn
    wheels[0].setVelocity(14)
    wheels[1].setVelocity(-14)
    wheels[2].setVelocity(14)
    wheels[3].setVelocity(-14)
    robot.step(70 * timestep)
    # forward()

def pick_up():
    armMotors[1].setPosition(-0.55)
    armMotors[2].setPosition(-0.9)
    armMotors[3].setPosition(-1.5)
    finger1.setPosition(fingerMaxPosition)
    finger2.setPosition(fingerMaxPosition)

#TODO: youBot default position:
#TODO: x: -2.4; y: 0; z: 0.101
#TODO: robot.step(70 * timestep) - produces a 90 degrees turn
# Move arm and open gripper.
#? arm[0] maxPosition = 2.9 || -2.9
#? arm[1] maxPosition = 1.5 || -1.0
#? arm[2] maxPosition = 2.5 || -2.6
#? arm[3] maxPosition = 1.7 || -1.7
#? arm[4] maxPosition = 2.9 || -2.9
# x = True
# while x: 
#     # halt()
#     turn_around()
#     robot.step(210 * timestep)
#     halt()
#     stretch_arms()
#     robot.step(200 * timestep)
#     fold_arms()
#     robot.step(200 * timestep)
#     # forward()
#     # robot.step(100 * timestep)

#! Functions call start here
forward()
robot.step(520 * timestep)# Wait until the robot is in front of the box.
halt()
pick_up()




# Monitor the arm joint position to detect when the motion is completed.
while robot.step(timestep) != -1:
    if abs(armPositionSensors[3].getValue() - (-1.2)) < 0.01:
        # Motion completed.
        break

# Close gripper.
finger1.setPosition(0.013)
finger2.setPosition(0.013)
# Wait until the gripper is closed.
robot.step(50 * timestep)

# Lift arm.
armMotors[1].setPosition(0)
# Wait until the arm is lifted.
robot.step(200 * timestep)
# turn_around()
# Rotate the robot.
wheels[0].setVelocity(7)
wheels[1].setVelocity(-7)
wheels[2].setVelocity(7)
wheels[3].setVelocity(-7)
# Wait for a fixed amount to step that the robot rotates.
robot.step(280 * timestep)
# robot.step(6900 * timestep)

#! -------------------------
#! PICK UP FROM HERE
#! -------------------------

# robot.step(690 * timestep)

# Move forward.
wheels[1].setVelocity(2.5)
wheels[3].setVelocity(2.5)
robot.step(900 * timestep)

# Rotate the robot.
wheels[0].setVelocity(1.0)
wheels[1].setVelocity(-1.0)
wheels[2].setVelocity(1.0)
wheels[3].setVelocity(-1.0)
robot.step(200 * timestep)

# Move forward.
wheels[1].setVelocity(1.0)
wheels[3].setVelocity(1.0)
robot.step(300 * timestep)

# Rotate the robot.
wheels[0].setVelocity(1.0)
wheels[1].setVelocity(-1.0)
wheels[2].setVelocity(1.0)
wheels[3].setVelocity(-1.0)
robot.step(130 * timestep)

# Move forward.
wheels[1].setVelocity(1.0)
wheels[3].setVelocity(1.0)
robot.step(310 * timestep)

# Stop.
for wheel in wheels:
    wheel.setVelocity(0.0)

# Move arm down
armMotors[3].setPosition(0)
armMotors[2].setPosition(-0.3)
robot.step(200 * timestep)

armMotors[1].setPosition(-1.0)
robot.step(200 * timestep)

armMotors[3].setPosition(-1.0)
robot.step(200 * timestep)

armMotors[2].setPosition(-0.4)
robot.step(50 * timestep)

# Open gripper.
finger1.setPosition(fingerMaxPosition)
finger2.setPosition(fingerMaxPosition)
robot.step(50 * timestep)
