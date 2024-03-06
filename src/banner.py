import os
import platform
from colorama import Fore , Back , init , just_fix_windows_console

init()
just_fix_windows_console()

def banners():
    system = platform.system()
    if system == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
    print(Fore.CYAN +"""
                     _    ______                __            
   _  __      __  __(_)  / ____/________ ______/ /_____  _____
  | |/_/_____/ / / / /  / /   / ___/ __ `/ ___/ //_/ _ \/ ___/
 _>  </_____/ /_/ / /  / /___/ /  / /_/ / /__/ ,< /  __/ /    
/_/|_|      \__,_/_/   \____/_/   \__,_/\___/_/|_|\___/_/     
                                                              
""")