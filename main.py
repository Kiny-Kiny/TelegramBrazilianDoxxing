from json import dumps
from sys import argv
from __init__ import main
def start():
    with open('consulta.json', 'w+') as v:
        retorno = main(argv[1:])
        return v.write(dumps(retorno))
        
if __name__ == '__main__': start() 
