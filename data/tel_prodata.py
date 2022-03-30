def consulta(message):
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
