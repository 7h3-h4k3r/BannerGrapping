from libs.__init__ import Banner
import argparse
import os
from colorama import Fore ,Style
class output:
    def __init__(self):
        self.__asciiArt()
        self.parser = argparse.ArgumentParser(description="Banner Grapping Tool")
        self._argscheck()
    def __asciiArt(self):
        ascii_art = Fore.MAGENTA+r"""

       _          (`-. 
       \`----.    ) ^_`)
,__     \__   `\_/  ( `
 \_\      \__  `|   }
    \  .--' \__/    }    D3vOps : Sridharanitharan.B
     ))/   \__,<  /_/    Version : 0.1
     ((|  _/_/ `\ \_\_   Model : Banner Grapping Tool 
      `\_____\  )__\"
      """ + Style.RESET_ALL
        print(ascii_art)
    def _argscheck(self):
        self.parser.add_argument("--ip", required=True,help="Give a Target IP or Domain ")
        self.parser.add_argument("--port", type=int,required=True, help="Give a Target port")
        args = self.parser.parse_args()
        self._bannerAbout(Banner(args.ip,args.port)._get_Banner(),args.ip,args.port)
        

    def _bannerAbout(self,msg,ip,port): 
        os.system('cls' if os.name == 'nt' else 'clear')
        self.__asciiArt()
        print(f"{Fore.RED}Host of Target : {ip} {Style.RESET_ALL}\n{Fore.WHITE}Port of Target : {port}{Style.RESET_ALL}\nBanner of Target : {Fore.GREEN}{msg}{Style.RESET_ALL}\n\n \t\t Analysis Finished")
{}
        
        

