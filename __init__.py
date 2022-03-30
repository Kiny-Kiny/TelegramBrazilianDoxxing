from os import system, path
from json import loads
from time import sleep
from data import cpf_prodata, placa_prodata, tel_prodata, login
from telethon import TelegramClient, connection, sync, events
from telethon.tl.functions.channels import JoinChannelRequest

def main(args, user = "@PuxadasGratis24hrs"):
    if len(args) < 2:
        return {'status': 402, 'message': 'Alguns parâmetros estão faltando!'}
    elif args[0] not in ['/cpf', '/tel', '/placa']:
        return {"status": 403, "message": "Comando Inválido!"}
        
    message = '';
    
    errorMessage = {
        '/tel': 'TELEFONE NÃO ENCONTRADO',
        '/cpf': 'CPF NÃO ENCONTRADO',
        '/placa': 'PLACA NÃO ENCONTRADA'
    }
    
    if not path.exists('dados.json'):
        retorno = login()
        if retorno['status'] != 200:
            return retorno
    
    with open('dados.json', 'r') as c:
        dados = loads(c.read())
        
    numero = dados['numero']
    api_id = dados['api_id']
    api_hash = dados['api_hash']
     
    client = TelegramClient(
         numero,
         api_id,
         api_hash,
         connection = connection.ConnectionTcpMTProxyRandomizedIntermediate,
        proxy = ('charge.Iran-Cell.dynu.com', 443, 'dd00000000000000000000000000000000'))
    client.connect()
     
    while not client.is_user_authorized():
        client.send_code_request(numero)
         
        codigo = input('[ + ] - Digite o código ===> ')
        
        system('clear||cls')
        
        try:
            client.sign_in(numero, codigo)
        except Exception:
            pass
        
    for i in args: message+= i+' ';
    
    try:
            try:
                client(JoinChannelRequest(user))
            except Exception:
                pass
                
            message = message[:-1];entity = client.get_entity(user);
            
            try:
                while True:
                    try:
                        client.send_message(entity = entity, message = message.replace('/cpf', '/cpf3').replace('/tel', '/telefone1').replace('/placa', '/placa2'))
                        break
                    except:
                        pass
                
                while True:
                    for messages in client.get_messages(entity):
                        id = messages.from_id.user_id
                        msg = messages.message
                    sleep(0.5)
                    if id == 1747207086:
                        messages.click(0)
                        func = {
                        '/cpf': cpf_prodata,
                        '/tel': tel_prodata,
                        '/placa': placa_prodata
                        }[args[0]]
                        break
                            
                dados = {"status": 200, "message": func(msg.replace('*', '').replace('`', '').replace('_', '').replace('› ', '').replace('• ', ''))}
            except Exception:
                dados = {"status": 400, "message": errorMessage[args[0]]}
    except:
        dados =  {"status": 500, "message": "ERRO NO SERVIDOR"}
        
    try:
        client.delete_dialog(entity)
    except Exception as e:
        print({'error': str(e)})
        
    return dados
