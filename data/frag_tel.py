def consulta(message):
    resultado = {}
    #################
    resultado['telefone'] = message.split('TELEFONE: ')[1].split('\n')[0]
    resultado['nome'] = message.split('NOME: ')[1].split('\n')[0]
    resultado['cpfCnpj'] = message.split('CPF/CNPJ: ')[1].split('\n')[0]
    resultado['operadora'] = message.split('OPERADORA: ')[1].split('\n')[0]
    resultado['ativacao'] = message.split('ATIVAÇÃO: ')[1].split('\n')[0]
    #################
    return resultado
