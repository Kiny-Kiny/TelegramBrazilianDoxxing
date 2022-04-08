def consulta(message):
    resultado = {}
    #################
    resultado['cpf'] = message.split('CPF: ')[1].split('\n')[0]
    resultado['cns'] = message.split('CNS: ')[1].split('\n')[0]
    resultado['nome'] = message.split('NOME: ')[1].split('\n')[0]
    resultado['mae'] = message.split('MÃE: ')[1].split('\n')[0]
    resultado['pai'] = message.split('PAI: ')[1].split('\n')[0]
    resultado['sexo'] = message.split('SEXO: ')[1].split('\n')[0]
    resultado['nascimento'] = message.split('NASCIMENTO: ')[1].split('\n')[0]
    resultado['score'] = message.split('SCORE: ')[1].split('\n')[0]
    resultado['rendaPresumida'] = message.split('RENDA PRESUMIDA: ')[1].split('\n')[0]
    resultado['cep'] = message.split('CEP: ')[1].split('\n')[0]
    resultado['classeSocial'] = message.split('CLASSE SOCIAL: ')[1].split('\n')[0]
    resultado['profissao'] = message.split('PROFISSÃO: ')[1].split('\n')[0]
    resultado['poderAquisitivo'] = message.split('PODER AQUISITIVO: ')[1].split('\n')[0]
    resultado['rg'] = message.split('RG: ')[1].split('\n')[0]
    resultado['orgao'] = message.split('ORGÃO: ')[1].split('\n')[0]
    resultado['rgUf'] = message.split('RG - UF: ')[1].split('\n')[0]
    resultado['emissao'] = message.split('EMISSÃO: ')[1].split('\n')[0]
    resultado['cidade'] = message.split('CIDADE: ')[1].split('\n')[0]
    resultado['estado'] = message.split('ESTADO: ')[1].split('\n')[0]
    resultado['distrito'] = message.split('DISTRITO: ')[1].split('\n')[0]
    resultado['rua'] = message.split('RUA: ')[1].split('\n')[0]
    resultado['numero'] = message.split('NUMERO: ')[1].split('\n')[0]
    resultado['complemento'] = message.split('COMPLEMENTO: ')[1].split('\n')[0]
    resultado['cep'] = message.split('CEP: ')[1].split('\n')[0]
    #################
    return resultado
