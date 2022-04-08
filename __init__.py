from os import system, path
from ujson import loads
from time import sleep
from data import frag_tel, frag_cpf, frag_placa, frag_email, frag_rg, login
from telethon import TelegramClient, connection, sync, events
from telethon.tl.functions.channels import JoinChannelRequest

def main(args, user = "@Hashiro_Consultas_Gratis"):
    if len(args) < 2:
        return {'status': 402, 'message': 'Alguns parâmetros estão faltando!'}
    elif args[0] not in [ '/tel', '/cpf', '/placa', '/rg', '/email']:
        return {"status": 403, "message": "Comando Inválido!"}

    key = args[0]

    message = '';
    
    loop = True

    errorMessage = {
        '/tel': 'TELEFONE NÃO ENCONTRADO',
        '/cpf': 'CPF NÃO ENCONTRADO',
        '/placa': 'PLACA NÃO ENCONTRADA',
        '/rg': 'RG NÃO ENCONTRADO',
        '/email': 'EMAIL NÃO ENCONTRADO'
    }

    parser = {
        '/tel': frag_tel,
        '/cpf': frag_cpf,
        '/placa': frag_placa,
        '/rg': frag_rg,
        '/email': frag_email
    }[key].consulta

    if not path.exists('dados.json'):
        retorno = login.start()
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

    message = message[:-1]

    try:
            try:
                client(JoinChannelRequest(user))
            except Exception:
                return {'status': 403, 'message': 'Não foi possível entrar no chat, verifique se sua conta foi banida do mesmo.'}

            entity = client.get_entity(user);

            try:
                while True:
                    try:
                        #.replace('/tel', '/telefone1').replace('/placa', '/placa2')
                        client.send_message(entity = entity, message = message.replace('/cpf', '/cpf3').replace('/tel', '/telefone'))
                        break
                    except:
                        pass

                while loop:
                    for messages in client.get_messages(entity, limit = 3):
                        id = messages.from_id.user_id
                        msg = messages.message
                        # Arcadian : 1747207086
                        if id == 5047798512:
                            try:
                                messages.click(0)
                            except:
                                pass
                            
                            loop = False
                            break
                    sleep(0.5)

                dados = {"status": 200, "message": parser(msg.replace('*', '').replace('`', '').replace('_', '').replace('› ', '').replace('• ', ''))}
            except Exception as e:
                dados = {"status": 400, "message": errorMessage[key]};print(str(e))
    except:
        dados =  {"status": 500, "message": "ERRO NO SERVIDOR"}

    try:
        client.delete_dialog(entity)
    except Exception as e:
        print({'error': str(e)})

    return dados
