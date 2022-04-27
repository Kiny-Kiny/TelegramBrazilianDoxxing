from requests import Session
from os import system
from random import randint
from json import loads, dumps

s = Session()

def start():
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
                    'app_title': 'Kiny_Crimson'+str(randint(111111, 999999)),
                    'app_shortname': 'ByKiny'+str(randint(111111, 999999)),
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
