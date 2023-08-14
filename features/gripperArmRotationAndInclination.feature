Feature: when the rotate feature is called when the inclination of the gripper arm is 25 degrees or greater and the grip state is closed or closing, the auto-orient function of the gripper will be called and no error state will be populated
The gripper arm is mounted using a bearing which can rotate as long as the gripping clamp is not oriented at a greater than twenty-five degree angle. Currently, the function will fail and produce an error message that the arm needs to be oriented - this feature will implement calling the auto-orient function to make that unnecessary.

Scenario Outline: The rotate feature is called when the arm is closed and with different inclination values
    Given the gripper arm inclination is <inclination>
    And the gripstate is 'closed'
    When the rotate feature is called
    Then the auto-orient function is called
    And the errorState is 'None'

    Examples: 
    |   inclination |
    |   25          |
    |   26          |
    |   90          |

Scenario Outline: The rotate feature is called when the arm is open and with different inclination values           
    Given the gripper arm inclination is <inclination>
    And the gripstate is 'open'
    When the rotate feature is called
    Then the auto-orient function is not called
    And the errorState is 'None'

    Examples: 
    |   inclination |
    |   25          |
    |   26          |
    |   90          |
