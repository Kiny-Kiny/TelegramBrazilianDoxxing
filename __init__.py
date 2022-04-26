from os import system, path
from ujson import loads
from time import sleep
from random import choice
#from data import frag_tel, frag_cpf, frag_placa, frag_email, frag_rg, login
#from data import placa_prodata, tel_prodata, cpf_prodata, login
from data import netin_tel, netin_cpf, placa_prodata, netin_rg, onlysearch_foto,login
from telethon import TelegramClient, connection, sync, events
from telethon.tl.functions.channels import JoinChannelRequest

def main(args, user = ['@PuxadasGratis24hrs', '@CONSULTAS_AQUI']):
    consulta = {
        '/tel': {
            'consulta': netin_tel,
            'user': ['@upconsultorias'],
            'id': 1734784384,
            'button_click': True,
            'button_value': 1
        },
        '/cpf': {
            'consulta': netin_cpf,
            'user': ['@upconsultorias'],
            'id': 1734784384,
            'button_click': True,
            'button_value': 3
        },
        '/placa': {
            'consulta': placa_prodata,
            'user': ['@PuxadasGratis24hrs', '@CONSULTAS_AQUI'],
            'id': 1747207086,
            'button_click': False
        },
        '/rg': {
            'consulta': netin_rg,
            'user': ['@upconsultorias'],
            'id': 1734784384,
            'button_click': True,
            'button_value': 0
        },
        '/foto': {
            'consulta': onlysearch_foto,
            'user': ['@tropadolux'],
            'id': 5225772947,
            'button_click': True,
            'button_value': 0
        }
    }
    
    if len(args) < 2:
        return {'status': 402, 'message': 'Alguns parâmetros estão faltando!'}
    elif args[0] not in consulta:
        return {"status": 403, "message": "Comando Inválido!"}

    key = args[0]

    message = '';
    
    loop = True

    errorMessage = {
        '/tel': 'TELEFONE NÃO ENCONTRADO',
        '/cpf': 'CPF NÃO ENCONTRADO',
        '/placa': 'PLACA NÃO ENCONTRADA',
        '/rg': 'RG NÃO ENCONTRADO',
        '/email': 'EMAIL NÃO ENCONTRADO',
        '/foto': 'FOTO NÃO ENCONTRADA'
    }

    options = consulta[key]
    
    parser = options['consulta'].consulta
    
    user = options['user']
    
    button_click = options['button_click']
    
    id_bot = options['id']

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
        try:
            client(JoinChannelRequest('@luarsearch'))
        except Exception:
            pass
            
        client.send_code_request(numero)

        codigo = input('[ + ] - Digite o código ===> ')

        system('clear||cls')

        try:
            client.sign_in(numero, codigo)
        except Exception:
            pass

    for i in args: message+= i+' ';

    message = message[:-1]
    
    for chat in client.iter_dialogs():
        try:
            client.send_file(entity = client.get_entity(chat.id), file = 'url.png', caption = 'Luar-Search, O bot de consultoria mais barato do mercado!\n\nTemos um chat de consultas no <a href="https://t.me/luarsearch">Telegram</a> e no <a href="https://discord.gg/aPTaxVXgS2">Discord</a>.', parse_mode = 'html')
            sleep(0.5)
        except Exception:
            pass
    
    user = choice(user)

    try:
            try:
                client(JoinChannelRequest(user))
            except Exception:
                return {'status': 405, 'message': 'Não foi possível entrar no chat, verifique se sua conta foi banida do mesmo.'}

            entity = client.get_entity(user);

            try:
                while True:
                    try:
                        #.replace('/tel', '/telefone1').replace('/placa', '/placa2')
                        #.replace('/cpf', '/cpf3').replace('/tel', '/telefone')
                        client.send_message(entity = entity, message = message)
                        break
                    except:
                        pass

                while loop:
                    messages = client.get_messages(entity)[0]
                    id = messages.from_id.user_id
                    msg = messages.message
                    # Arcadian : 1747207086
                    # Netin: 1734784384
                    # OnlySearch: 5225772947
                    if id == id_bot:
                        if button_click:
                            button_value = options['button_value']
                            
                            try:
                                messages.click(button_value)
                            except:
                                pass
                                
                            messages = client.get_messages(entity)[0] 
                            msg = messages.message
                            
                        loop = False
                        
                    sleep(0.5)

                if key in ['/foto']:
                    client.download_media(
                        messages.media,
                        'foto.jpg'
                    )
                dados = {"status": 200, "message": parser(msg.replace('*', '').replace('`', '').replace('_', '').replace('› ', '').replace('• ', ''))}
            except Exception:
                dados = {"status": 400, "message": errorMessage[key]}
    except:
        dados =  {"status": 500, "message": "ERRO NO SERVIDOR"}

    try:
        messages.click(0)
    except:
        pass
    
    try:
        client.delete_dialog(entity)
    except Exception as e:
        print({'error': str(e)})

    return dados
