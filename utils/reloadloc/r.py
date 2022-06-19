import sys
from os import system

system("cp ../../it.po ../")
system("ruby ../mklang.rb ../it.po ../it.loc")
system("mv ../it.loc '/Users/imjstnick/Library/Application Support/Steam/steamapps/common/OneShot/Languages/en.loc'")
system("mv ../it.po '/Users/imjstnick/Library/Application Support/Steam/steamapps/common/OneShot/Languages/en.po'")