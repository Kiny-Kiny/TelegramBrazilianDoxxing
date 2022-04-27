def consulta(message):
    resultado = {}
    #################
    resultado['email'] = message.split('EMAIL: ')[1].split('\n')[0]
    resultado['cpf'] = message.split('CPF: ')[1].split('\n')[0]
    #################
    return resultado
