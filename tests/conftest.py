#conftest.py
import pandas as pd
import os

def pytest_bdd_before_scenario(request, feature, scenario):
    if ("data-driven" not in scenario.tags):
        return
    
    dataFile = ''

    print('\n\nscenario:' + str(vars(scenario)))

    for tag in scenario.tags:
        #print (str(tag))
        if (tag.startswith("datafile_")):
            dataFile = tag.split('_')[1]

    if (dataFile == ''):
        return

    dir, null = os.path.split(str(request.path))
    fileName = dir + "\\resources\\" + dataFile

    df = pd.read_excel(io=fileName, sheet_name="data")

    examples = scenario.feature.scenarios[scenario.name].examples.examples

    # clear existing examples
    examples = []
    for index, row in df.iterrows():
        examples.append({row[0], row[1]})

    scenario.feature.scenarios[scenario.name].examples.examples = examples

def pytest_bdd_after_step(request, feature, scenario, step, step_func, step_func_args):
    #print('whatever is going on')
    # log changes in state
    pass