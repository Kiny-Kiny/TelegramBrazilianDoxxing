from requests import Session
from json import loads, dumps
from os import system, path
from sys import argv
from telethon import TelegramClient, connection, sync, events
from time import sleep

s = Session();

############################################

def tel_prodata(message):
    message = message.replace('*', '').replace('`', '').replace('_', '').replace('› ', '').replace('• ', '')
    message = message.split('[+] DADOS PESSOAIS [+]\n\n')[1].replace('\n\n[+] DADOS TELEFONE [+]\n\n', '\n').split('\n\nUSUÁRIO')[0].replace('\n\n', '\n')
    resultado = {}
    ##################
    resultado['cpf'] = message.split('CPF/CNPJ: ')[1].split('\n')[0]
    resultado['nome'] = message.split('NOME COMPLETO: ')[1].split('\n')[0]
    resultado['nascimento'] = message.split('NASCIMENTO: ')[1].split('\n')[0]
    resultado['telefone'] = message.split('TELEFONE: ')[1].split('\n')[0]
    resultado['dataAtivacao'] = message.split('DATA ATIVAÇÃO: ')[1].split('\n')[0]
    resultado['operadora'] = message.split('OPERADORA')[1].split('\n')[0]
    resultado['email'] = message.split('EMAIL: ')[1].split('\n')[0]
    resultado['extra'] = message.split('EXTRA: ')[1].split('\n')[0]
    ##################
    return resultado

def cpf_prodata(message):
    message = message.replace('*', '').replace('`', '').replace('_', '').replace('› ', '').replace('• ', '')
    resultado = {}
    ##################
    resultado['grauDeQualidade'] = message.split('GRAU DE QUALIDADE: ')[1].split('\n')[0]
    resultado['cpf'] = message.split('CPF: ')[1].split('\n')[0]
    resultado['cns'] = message.split('CNS: ')[1].split('\n')[0]
    resultado['score'] = message.split('SCORE: ')[1].split('\n')[0]
    resultado['nome'] = message.split('NOME: ')[1].split('\n')[0]
    resultado['nascimento'] = message.split('DATA NASCIMENTO: ')[1].split('\n')[1]
    resultado['sexo'] = message.split('SEXO: ')[1].split('\n')[0]
    resultado['mae'] = message.split('MÃE: ')[1].split('\n')[0]
    resultado['pai'] = message.split('PAI: ')[1].split('\n')[0]
    
    try:
        result = message.split('[+] ENDEREÇO RECENTE [+]\n\n')[1].split('\n\n[+] TELEFONES REGISTRADOS [+]')[0].split('\n\n')
        result_list = []
        
        for k in result:
            msg = {}
            for v in k.split('\n'):
                resp = v.split(': ')
                msg[resp[0].lower()] = resp[1]
            result_list.append(msg)
            
        resultado['enderecoRecente'] = result_list
    except:
        resultado['enderecoRecente'] = message.split('[+] ENDEREÇO RECENTE [+]\n\n')[1].split('\n\n')[0]
    
    try:
        result = message.split('[+] TELEFONES REGISTRADOS [+]\n\n')[1].split('\n\n[+] EMAILS REGISTRADOS [+]')[0].split('\n\n')
        result_list = []
        
        for k in result:
            msg = {}
            for v in k.split('\n'):
                resp = v.split(': ')
                msg[(resp[0].lower()).replace('ú', 'u')] = resp[1]
            result_list.append(msg)
            
        resultado['telefonesRegistrados'] = result_list
    except:
        resultado['telefonesRegistrados'] = message.split('[+] TELEFONES REGISTRADOS [+]\n\n')[1].split('\n\n')[0]
    
    try:
        result = message.split('[+] EMAILS REGISTRADOS [+]\n\n')[1].split('\n\n[+] VACINAS REGISTRADAS [+]')[0].split('\n\n')
        result_list = []
        
        for k in result:
            msg = {}
            for v in k.split('\n'):
                resp = v.split(': ')
                msg[resp[0].lower()] = resp[1]
            result_list.append(msg)
            
        resultado['emailsRegistrados'] = result_list
    except:
        resultado['emailsRegistrados'] = message.split('[+] EMAILS REGISTRADOS [+]\n\n')[1].split('\n\n')[0]
    
    try:
        result = message.split('[+] VACINAS REGISTRADAS [+]\n\n')[1].split('\n\n[+] RECEITA FEDERAL [+]')[0].split('\n\n')
        result_list = []
        
        for k in result:
            msg = {}
            for v in k.split('\n'):
                resp = v.split(': ')
                msg[resp[0].lower()] = resp[1]
            result_list.append(msg)
            
        resultado['vacinasRegistradas'] = result_list
    except:
        resultado['vacinasRegistradas'] = 'NENHUMA VACINA REGISTRADA'
    
    try:
        result = message.split('[+] RECEITA FEDERAL [+]\n\n')[1].split('\n\nUSUÁRIO:')[0].split('\n\n')
        result_list = []
        
        for k in result:
            msg = {}
            for v in k.split('\n'):
                resp = v.split(': ')
                msg[resp[0].lower().replace('º ', 'umero_').replace('ã', 'a').replace(' ', '_')] = resp[1]
            result_list.append(msg)
            
        resultado['receitaFederal'] = result_list
    except:
        resultado['receitaFederal'] = message.split('[+] RECEITA FEDERAL [+]\n\n')[1].split('\n\n')[0]
    ###################
    return resultado

############################################

def login():
    numero = input('[ * ] - Digite o número de telefone ===> ')
    while True:
        system('clear||cls')
        res = s.post('https://my.telegram.org/auth/send_password',
            data = 'phone=%s'%numero)
        
        res = res.text 
        if res == 'Sorry, too many tries. Please try again later.':
            return {'status': 403, 'message': 'Muitas tentativas, tente novamente mais tarde.'}
        
        res = loads(res)
        
        senha = input('[ * ] - Digite o número de telefone ===> %s\n[ * ] - Digite a senha ===> '%numero)
        
        res = s.post('https://my.telegram.org/auth/login',
            data = {
            'phone': numero,
            'random_hash': res["random_hash"],
            'password': senha
            })
            
        res = res.text
        if res == 'true':
            
            try:
                token = s.get('https://my.telegram.org/apps')
                toke = token.text
                
                token = token.split(
                    '<input type="hidden" name="hash" value="')[1].split(
                        '"/>')[0]
                
                s.post('https://my.telegram.org/apps/create',
                    data = {
                    'hash': token,
                    'app_title': 'Kiny_Crimson',
                    'app_shortname': 'ByKiny',
                    'app_url': '',
                    'app_platform': 'android',
                    'app_desc': ''
                    })
            except:
                pass
            
            res = s.get('https://my.telegram.org/apps')
            res = res.text
            
            dados = {
            'numero': numero,
            'api_id': res.split(
                'onclick="this.select();"><strong>')[1].split(
                    '</strong></span>')[0],
            'api_hash': res.split(
                'onclick="this.select();">')[2].split(
                    '</span>')[0]
            }

            with open('dados.json', 'w+') as f:
                f.write(
                dumps(
                  dados
                )
                )
            return {'status': 200, 'message': 'Logado com sucesso!'}

############################################

def main(args, link = "https://t.me/PuxadasGratis24hrs"):
    if len(args) < 2:
        return {'status': 402, 'message': 'Alguns parâmetros estão faltando!'}
    elif args[0] not in ['/cpf', '/tel']:
        return {"status": 403, "message": "Comando Inválido!"}
        
    message = '';
    
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
         
        client.sign_in(numero, codigo)
        
    for i in args: message+= i+' ';
    
    try:
            message = message[:-1];entity = client.get_entity(link);
            
            try:
                while True:
                    try:
                        client.send_message(entity = entity, message = message.replace('/cpf', '/cpf3').replace('/tel', '/telefone1'))
                        break
                    except:
                        pass
                
                while True:
                    for messages in client.get_messages(entity):
                        id = messages.from_id.user_id
                        msg = messages.message
                    sleep(1)
                    if id == 1747207086:
                        func = {
                        '/cpf': cpf_prodata,
                        '/tel': tel_prodata
                        }[args[0]]
                        
                        msg = func(msg)
                        break
                            
                return {"status": 200, "message": msg}
            except Exception as e:
                return {"status": 400, "message": str(e)}
    except:
        return  {"status": 500, "message": "ERRO NO SERVIDOR"}

############################################
     
def start():
    with open('consulta.json', 'w+') as v:
        retorno = main(argv[1:])
        return v.write(str(retorno))
        
if __name__ == '__main__': start()
