import pyfiglet
import sys
import socket
from datetime import datetime
asc_banner = pyfiglet.figlet_format('ICECOOL 2')
print(asc_banner)
if len(sys.argv)==2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print('invalido argumento')

print('__'*50)
print(' Scaneando Target:'+target)
print(' scaneamento iniciado :'+ str(datetime.now()))
print('_'*50)
