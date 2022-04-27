def consulta(message):
    dados = {}
    ################
    dados['dadosPessoais'] = {
        'nome': message.split('NOME: ')[1].split('\n')[0],
        'idade': message.split('IDADE: ')[1].split('\n')[0],
        'nascimento': message.split('NASCIMENTO: ')[1].split('\n')[0],
        'cidade': message.split('CIDADE: ')[1].split('\n')[0],
        'signo': message.split('SIGNO: ')[1].split('\n')[0],
        'genero': message.split('GÊNERO: ')[1].split('\n')[0],
        'situacao': message.split('SITUAÇÃO: ')[1].split('\n')[0],
        'cpf': message.split('CPF: ')[1].split('\n')[0],
        'regiao': message.split('REGIÃO: ')[1].split('\n')[0],
        'obito': message.split('OBÍTO: ')[1].split('\n')[0],
        'estadoCivil': message.split('ESTADO CÍVIL: ')[1].split('\n')[0],
     }
    dados['familiares'] = {
        'pai': message.split('PAI: ')[1].split('\n')[0],
        'mae': message.split('MÃE: ')[1].split('\n')[0]
     }
    dados['registroGeral'] = {
         'numero': message.split('NÚMERO: ')[1].split('\n')[0],
         'emissor': message.split('EMISSOR: ')[1].split('\n')[0],
         'dataDeEmissao': message.split('DATA DE EMISSÃO: ')[1].split('\n')[0],
         'uf': message.split('UF: ')[1].split('\n')[0],
    }
    
    try:
        endereco = message.split('「🏡」ENDEREÇOS\n \n')[1].split('\n\n\n「💰」INFORMAÇÕES BANCÁRIAS')[0].split('\n\n')
        _endereco = []
        for i in endereco:
            info = {}
            info['estado'] = i.split('ESTADO: ')[1].split('\n')[0]
            info['cidade'] = i.split('CIDADE: ')[1].split('\n')[0]
            info['cep'] = i.split('CEP: ')[1].split('\n')[0]
            info['bairro'] = i.split('BAIRRO: ')[1].split('\n')[0]
            info['logradouro'] = i.split('LOGRADOURO: ')[1].split('\n')[0]
            info['tipo'] = i.split('TIPO: ')[1].split('\n')[0]
            info['complemento'] = i.split('COMPLEMENTO: ')[1].split('\n')[0]
            info['numero'] = i.split('NÚMERO: ')[1].split('\n')[0]
            _endereco.append(info)
        dados['enderecos'] = _endereco
    except:
        dados['enderecos'] = []
        
    try:
        infob = message.split('「💰」INFORMAÇÕES BANCÁRIAS\n \n')[1].split('\n\n\n「💰」RENDA ESTIMADA')[0].split('\n\n')
        _infob = []
        for i in infob:
            info = {}
            info['banco'] = i.split('BANCO: ')[1].split('\n')[0]
            info['status'] = i.split('STATUS: ')[1].split('\n')[0]
            info['ano'] = i.split('ANO: ')[1].split('\n')[0]
            _infob.append(info)
        dados['informacoesBancarias'] = _infob
    except:
        dados['informacoesBancarias'] = []
    
    try:
        renda = message.split('「💰」RENDA ESTIMADA\n\n')[1].split('\n\nObs:')[0].split('\n')
        _renda = []
        for i in renda:
            _renda.append(i)
        dados['rendaEstimada'] = _renda
    except:
        dados['rendaEstimada'] = []
    
    try:
        telefones = message.split('「📱」TELEFONES\n \n')[1].split('\n\n「📧」E-MAILS')[0].split('\n')
        _telefones = []
        for i in telefones:
            _telefones.append(i.split(': ')[1])
        dados['telefones'] = _telefones
    except:
        dados['telefones'] = []
    
    try:
        emails = message.split('「📧」E-MAILS\n \n')[1].split('\n\nUSUÁRIO')[0].split('\n')
        _emails = []
        for i in emails:
            _emails.append(i.split(': ')[1])
        dados['emails'] = _emails
    except:
        dados['emails'] = []
    ################
    return dados
