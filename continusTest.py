from module_watcher import ModuleWatcher
import test

import sys

def callback(modName):
    if modName is "test":
        test.init(mw)
        mw.watch_module('test')
        print("="*80)
        print("Reloaded modules, press Enter to exit")
        print("="*80)


         

mw = ModuleWatcher()
mw.watch_module('test')
mw.start_watching()

try:
    input('Press ENTER to exit')
finally:
    mw.stop_watching()
    sys.exit(0)
