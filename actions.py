# Imports
import voicemeeter as vm

# Exit action
def actExit(*args):
    print(f"Exiting from button push {args}")
    return False

# Skipped action
def actNone(*args):
    return True

# Voicemeeter actions
kind = 'potato'

# Restart the VM Audio Engine - Needed w/ Index VR to get headset audio
def actVMRestart(*args):
    print("Restarting audio engine")
    with vm.remote(kind) as vmr:
        vmr.restart()
    return True

# Mute VM channels
# Need to figure out how to make this take options as a string
def actVMMute(*args):
    with vm.remote(kind) as vmr:
        newstate = not vmr.outputs[5].mute
        vmr.outputs[5].mute = newstate
        vmr.outputs[6].mute = newstate
        if vmr.outputs[5].mute:
            print("Mic channels now muted")
            lp.LedCtrlXY(8,2,3,3)
        else:
            print("Mic channels are hot")
            lp.LedCtrlXY(8,2,0,0)
    return True