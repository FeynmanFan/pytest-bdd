Feature: Slow down when object nearby
If the sensor detects an object in the near field of the sensor range, reduce the speed 
by 1 m/s with a zero bound.

Background:
	Given the near field sensor detects an object

@factoryfloor
Scenario Outline: Robot detects object while in motion
	Given the robot is traveling at <initialSpeed>m/s
	When motion evaluation fires
	Then speed should be <finalSpeed>m/s

	Examples: speeds
	|	initialSpeed	|	finalSpeed	|
	|	10				|	9			|
	|	38				|	37			|
	|	1000			|	999			|
	|	22				|	21			|
	|	0				|	0			|
