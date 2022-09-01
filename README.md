# youBot

## Overview:
 
Program developed to control a KUKA youBot robot to pick a cube and move it to a target position.

## Metrics:
                                t = 00:00:00

The metric is the time t spent by the robot to pick the green cube and place it in the empty slot of the box located on the cart. The timer starts as soon as the simulation start and stops when the cube is in the slot. At this point, the simulation time is recorded as the performance of the robot.

## Controller:

The controller is an open-loop algorithm that reduces the metric thereby reducing the execution time by:
* Increasing the motor velocity.
* Adjusting the duration of steps.
* Parallelizing the motions.

## Pre-defined values:

Some information about the environment and the robot that can be useful to improve the controller:

* The initial robot position is [x: -2.4, z: 0.0] m. 
* The cube position is [x: 1.0, y: 0.205, z: 0.0] m after the conveyor belt stops.
* The target position is [x: -2.185, y: 0.140, z: -0.813] m.
* The robot's wheel radius is 5cm.

## Demonstration
![](https://github.com/Logahn/youBot/blob/master/documentation/youBot1.gif?raw=true)
