import launchpad_py as lppy
from itertools import chain
import yaml
import actions

def openLaunchpad(type="mini"):
    lp = lppy.Launchpad()
    if lp.Open(0, type):
        print("Launchpad Ready")
        lp.LedAllOn()
        lp.Reset()
        return lp
    else:
        print("Error opening Launchpad.   Exiting")
        exit

def lpSetInitialColors(buttons, lp):
    blist = chain.from_iterable(zip(*buttons))
    for b in blist:
        if b:
            lp.LedCtrlXY(b['x'], b['y'], b['color'][0], b['color'][1])

def buttonLoop(buttons, lp):
    print("Starting Button press loop")
    result = True
    while result:
        event = lp.ButtonStateXY()
        if len(event) > 0:
            x, y, state = event
            if state:
                print(f"Button at {x}, {y} was pressed")
                b = buttons[x][y]
                if b:
                    result = eval('actions.act' + b['action'] + '()')
            else:
                print(f"Button at {x}, {y} was released")

def loadButtonYaml(fname='buttons.yaml'):
    buttonXY = [[ None for y in range(9) ] for x in range(9) ]
    print(f"Loading Button definitions from {fname}")
    with open(r'buttons.yaml') as file:
        buttons = yaml.load(file, Loader=yaml.FullLoader)
    for b in buttons:
        buttonXY[b['x']][b['y']] = b
    return buttonXY

def main():
    buttonDict = loadButtonYaml()
    lp = openLaunchpad()
    lpSetInitialColors(buttonDict, lp)
    buttonLoop(buttonDict, lp)
    lp.Reset()
    lp.Close()

if __name__ == "__main__":
    main()