def consulta(message):
    dados = {}
    foto = message.media.photo.sizes[0].bytes
    message = (message.message).replace('*', '').replace('`', '').replace('_', '').replace('› ', '').replace('• ', '')
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
