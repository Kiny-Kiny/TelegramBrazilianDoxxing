from requests import Session
from json import loads, dumps
from os import system, path
from sys import argv
from telethon import TelegramClient, connection, sync, events
from telethon.tl.functions.channels import JoinChannelRequest
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

def placa_prodata(message):
    dados = {}
    ####################
    dados['dadosGerais'] = {
        'placaAtual': message.split('PLACA ATUAL: ')[1].split('\n')[0],
        'placaNova': message.split('PLACA NOVA: ')[1].split('\n')[0],
        'placaAntiga': message.split('PLACA ANTIGA: ')[1].split('\n')[0],
        'restricoes': message.split('RESTRIÇÕES: ')[1].split('\n')[0],
        'renavam': message.split('RENAVAM: ')[1].split('\n')[0],
        'chassi': message.split('CHASSI: ')[1].split('\n')[0]
    }
    dados['marcaModelo'] = {
        'modelo': message.split('MODELO: ')[1].split('\n')[0],
        'marca': message.split('MARCA: ')[1].split('\n')[0],
        'segmento': message.split('SEGMENTO: ')[1].split('\n')[0],
        'subSegmento': message.split('SUB-SEGMENTO: ')[1].split('\n')[0],
        'grupo': message.split('GRUPO: ')[1].split('\n')[0],
    }
    dados['composicao'] = {
        'combustivel': message.split('COMBUSTÍVEL: ')[1].split('\n')[0],
        'potencia': message.split('POTÊNCIA: ')[1].split('\n')[0],
        'potenciaDeCarga': message.split('POTÊNCIA DE CARGA: ')[1].split('\n')[0],
        'motor': message.split('MOTOR: ')[1].split('\n')[0],
        'eixos': message.split('EIXOS: ')[1].split('\n')[0]
    }
    dados['fabricacao'] = {
        'anoModelo': message.split('ANO MODELO: ')[1].split('\n')[0],
        'anoFabricacao': message.split('ANO FABRICAÇÃO: ')[1].split('\n')[0],
        'nacionalidadeFab': message.split('NACIONALIDAE FAB.: ')[1].split('\n')[0],
        'linhaFab': message.split('LINHA FAB.: ')[1].split('\n')[0],
        'motorFab': message.split('MOTOR FAB.: ')[1].split('\n')[0],
        'tipoCarroceria': message.split('TIPO CARROCERIA: ')[1].split('\n')[0]
    }
    dados['localizacao'] = {
        'estado': message.split('ESTADO (UF): ')[1].split('\n')[0],
        'municipio': message.split('MUNICIPIO: ')[1].split('\n')[0],
        'municipioEmplacado': message.split('MUNICIPIO EMPLACADO: ')[1].split('\n')[0]
    }
    dados['dadosCondutor'] = {
        'tipoDocumento': message.split('TIPO DOCUMENTO: ')[1].split('\n')[0],
        'documento': message.split('DOCUMENTO: ')[2].split('\n')[0],
        'nomeCompleto': message.split('NOME COMPLETO: ')[1].split('\n')[0]
    }
    return dados
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
         
        client.sign_in(numero, codigo)
        
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
                            
                dados = {"status": 200, "message": func(msg)}
            except Exception:
                dados = {"status": 400, "message": errorMessage[args[0]]}
    except:
        dados =  {"status": 500, "message": "ERRO NO SERVIDOR"}
        
    try:
        client.delete_dialog(entity)
    except Exception as e:
        print({'error': str(e)})
        
    return dados

############################################
     
def start():
    with open('consulta.json', 'w+') as v:
        retorno = main(argv[1:])
        return v.write(dumps(retorno))
        
if __name__ == '__main__': start() 
