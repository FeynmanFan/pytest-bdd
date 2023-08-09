from velocity import velocity
import pytest

pytestmark = pytest.mark.framework

def test_createSimpleVelocity():
    vel = velocity(90, 10) # due east at ten meters/sec

    assert vel.heading  == 90
    assert vel.speed == 10

def test_createVelocityWithNegativeSpeed():
    with pytest.raises(Exception) as e:
        vel = velocity(90, -10) # due west at ten meters /sec, but this is not allowed
    
    assert str(e.value) == "Speed cannot be negative"
    
def test_createVelocityWithCompoundHeading():
    vel = velocity(405, 10) # northwest at ten meters / sec

    assert vel.heading == 45
    assert vel.speed == 10
