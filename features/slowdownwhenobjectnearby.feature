Feature: Slow down when object nearby
When the sensor detects an object in the near field of the sensor range, reduce the speed 
by 1 m/s with a zero bound.

Background:
	Given the near field sensor detects an object

Scenario: Robot detects object while in motion
	Given the robot is traveling at 10m/s
	When motion evaluation fires
	Then speed should be 9m/s
	
Scenario: Robot detects object while in motion at any speed
	Given the robot is moving at a speed > 0
	When motion evaluation fires
	Then speed should be decreased by one meter per second
	
Scenario: Robot detects object while at rest
	Given the robot is moving at a speed == 0
	When motion evaluation fires
	Then the robot should remain at rest
