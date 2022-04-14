def consulta(message):
    ###################
    dados = {
        'nome': message.split('NOME: ')[1].split('\n')[0],
        'cpf': message.split('CPF: ')[1].split('\n')[0],
        'cns': message.split('CNS: ')[1].split('\n')[0],
        'mae': message.split('MÃE: ')[1].split('\n')[0],
        'pai': message.split('PAI: ')[1].split('\n')[0],
    }
    ###################
    return dados
