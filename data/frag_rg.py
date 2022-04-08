def consulta(message):
    resultado = {}
    #################
    resultado['rg'] = message.split('RG: ')[1].split('\n')[0]
    resultado['nome'] = message.split('NOME: ')[1].split('\n')[0]
    resultado['cpf'] = message.split('CPF: ')[1].split('\n')[0]
    resultado['sexo'] = message.split('SEXO: ')[1].split('\n')[0]
    #################
    return resultado
