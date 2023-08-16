Feature: Robots' performance envelopes fall within the values advertised in the spec sheet
Globomantics provides an industry spec sheet to interested buyers that outlines the capabilities of our products, and it is important to validate that the software meets the specifications.

	Scenario Outline: Robots' load values in software match the spec sheet
		Given the robot is model <robotModel>
		And the load meets the spec
		When the robot is loaded
		Then the loadState is within the cargo capacity of the model
	
		Examples:
		|robotModel	|
		|hercules	|
		|athena		|
		|hera		|
		|perseus	|
		|mercury	|
