Feature: Robots have the proper amperage to power their sensors
In the past, engineers have loaded robots with too many sensors to operate all sensors simultaneously, so this test will validate that the sum of the amperage of the robot's sensors does not exceed the amperage limit for the unit

Scenario Outline: The robot has enough amperage to power all sensors	
	Given the robot is model <model>
	When the robot performs an amperage check
	Then the power state of the unit is ALL
	
	Examples:
	|model|
	|athena|
	|hera|
	|hercules|
	|mercury|
	|perseus|