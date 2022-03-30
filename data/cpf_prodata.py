def consulta(message):
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
