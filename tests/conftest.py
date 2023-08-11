#conftest.py

def pytest_bdd_before_scenario(request, feature, scenario):
    #print("Before_scenario")
    #print("Feature: " + feature.name)
    #print("Scenario: " + scenario.name)
    pass

def pytest_bdd_after_step(request, feature, scenario, step, step_func, step_func_args):
    #print('whatever is going on')
    # log changes in state
    pass