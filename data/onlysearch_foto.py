def consulta(message):
    dados = {}
    with open('foto.jpg', 'rb') as f:
      foto = f.read()
    ################
    dados['dadosPessoais'] = {
        'nome': message.split('NOME: ')[1].split('\n')[0],
        'nascimento': message.split('NASCIMENTO: ')[1].split('\n')[0],
        'pai': message.split('PAI: ')[1].split('\n')[0],
        'mae': message.split('MÃE: ')[1].split('\n')[0]
     }
    dados['foto'] = foto
    ################
    return dados
