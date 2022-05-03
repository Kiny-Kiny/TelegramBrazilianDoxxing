from ujson import dumps
from sys import argv
from __init__ import main
def start():
    with open('consulta.json', 'w+') as v:
        retorno = main(argv[1:])
        return v.write(dumps(retorno, indent = 4, sort_keys = True))
        
if __name__ == '__main__': start() 
