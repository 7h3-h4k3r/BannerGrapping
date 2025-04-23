from __init__ import Banner
import argparse
class output:
    def __init__(self):
        self.ascii_art = r"""
       _          (`-. 
       \`----.    ) ^_`)
,__     \__   `\_/  ( `
 \_\      \__  `|   }
    \  .--' \__/    }    D3vOps : Sridharanitharan.B
     ))/   \__,<  /_/    Version : 0.1
     ((|  _/_/ `\ \_\_   Module : beta
      `\_____\  )__\_"""
        print(self.ascii_art)
        self.parser = argparse.ArgumentParser(description="Banner Grapping Tool")
    def __asciiArt(self):
        print("ascii")
    def _argscheck(self):
        self.parser.add_argument("--ip", help="Give a Target IP or Domain ")
        self.parser.add_argument("--port", type=int, help="Give a Target port")
        args = self.parser.parse_args()
        data = Banner(args.ip,args.port)
        print(data._get_Banner())
        


ban = output()._argscheck()
