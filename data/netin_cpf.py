def consulta(message):
    dados = {}
    ###################
    dados['dadosCadastrais'] = {
        'nome': message.split('NOME: ')[1].split('\n')[0],
        'cpf': message.split('CPF: ')[1].split('\n')[0],
        'cns': message.split('CNS: ')[1].split('\n')[0],
        'dataDeNascimento': message.split('DATA DE NASCIMENTO: ')[1].split('\n')[0],
        'sexo': message.split('SEXO: ')[1].split('\n')[0],
        'cor': message.split('COR: ')[1].split('\n')[0],
        'numeroDoPis': message.split('NÚMERO DO PIS: ')[1].split('\n')[0],
        'nomeDoPai': message.split('NOME DO PAI: ')[1].split('\n')[0],
        'nomeDaMae': message.split('NOME DA MÃE: ')[1].split('\n')[0]
    }
    dados['enderecos'] = {
        'estado': message.split('ESTADO: ')[1].split('\n')[0],
        'municipio': message.split('MUNICÍPIO: ')[1].split('\n')[0],
        'bairro': message.split('BAIRRO: ')[1].split('\n')[0],
        'cep': message.split('CEP: ')[1].split('\n')[0],
        'logradouro': message.split('LOGRADOURO: ')[1].split('\n')[0],
        'complemento': message.split('COMPLEMENTO: ')[1].split('\n')[0],
        'numero': message.split('NÚMERO: ')[1].split('\n')[0]
    }
    dados['contatos'] = {
        'celular': message.split('CELULAR: ')[1].split('\n')[0],
        'telefone': message.split('TELEFONE: ')[1].split('\n')[0],
        'residencial': message.split('RESIDENCIAL: ')[1].split('\n')[0]
    }
    dados['nascimento'] = {
        'estadoDeNascimento': message.split('ESTADO DE NASCIMENTO: ')[1].split('\n')[0],
        'municipioDeNascimento': message.split('MUNICÍPIO DE NASCIMENTO: ')[1].split('\n')[0]
    }
    ###################
    return dados
