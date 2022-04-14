def consulta(message):
    dados = {}
    ################
    dados['dadosPessoais'] = {
        'nome': message.split('NOME: ')[1].split('\n')[0],
        'nascimento': message.split('NASCIMENTO: ')[1].split('\n')[0],
        'sexo': message.split('SEXO: ')[1].split('\n')[0],
        'cpf': message.split('CPF: ')[1].split('\n')[0],
        'cns': message.split('CNS: ')[1].split('\n')[0],
        'rg': message.split('RG: ')[1].split('\n')[0],
        'emissor': message.split('EMISSOR: ')[1].split('\n')[0],
        'dataDeEmissao': message.split('DATA de Emissão: ')[1].split('\n')[0],
        'ufDoRg': message.split('UF do RG: ')[1].split('\n')[0]
    }
    dados['parentes'] = {
        'mae': message.split('MÃE: ')[1].split('\n')[0],
        'pai': message.split('PAI: ')[1].split('\n')[0]
    }
    dados['endereco'] = {
        'municipio': message.split('MUNICÍPIO: ')[1].split('\n')[0],
        'bairro': message.split('BAIRRO: ')[1].split('\n')[0],
        'logradouro': message.split('LOGRADOURO: ')[1].split('\n')[0],
        'numero': message.split('Nº: ')[1].split('\n')[0],
        'cep': message.split('CEP: ')[1].split('\n')[0]
    }
    dados['municipioDeNascimento'] = message.split('MUNICÍPIO DE NASCIMENTO: ')[1].split('\n')[0]
    dados['telefone'] = message.split('❲ 📱 - TELEFONE ❳ ')[1].split('\n')[0]
    ################
    return dados
