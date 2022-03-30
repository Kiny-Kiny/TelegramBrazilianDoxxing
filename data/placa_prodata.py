def placa_prodata(message):
    dados = {}
    ####################
    dados['dadosGerais'] = {
        'placaAtual': message.split('PLACA ATUAL: ')[1].split('\n')[0],
        'placaNova': message.split('PLACA NOVA: ')[1].split('\n')[0],
        'placaAntiga': message.split('PLACA ANTIGA: ')[1].split('\n')[0],
        'restricoes': message.split('RESTRIÇÕES: ')[1].split('\n')[0],
        'renavam': message.split('RENAVAM: ')[1].split('\n')[0],
        'chassi': message.split('CHASSI: ')[1].split('\n')[0]
    }
    dados['marcaModelo'] = {
        'modelo': message.split('MODELO: ')[1].split('\n')[0],
        'marca': message.split('MARCA: ')[1].split('\n')[0],
        'segmento': message.split('SEGMENTO: ')[1].split('\n')[0],
        'subSegmento': message.split('SUB-SEGMENTO: ')[1].split('\n')[0],
        'grupo': message.split('GRUPO: ')[1].split('\n')[0],
    }
    dados['composicao'] = {
        'combustivel': message.split('COMBUSTÍVEL: ')[1].split('\n')[0],
        'potencia': message.split('POTÊNCIA: ')[1].split('\n')[0],
        'potenciaDeCarga': message.split('POTÊNCIA DE CARGA: ')[1].split('\n')[0],
        'motor': message.split('MOTOR: ')[1].split('\n')[0],
        'eixos': message.split('EIXOS: ')[1].split('\n')[0]
    }
    dados['fabricacao'] = {
        'anoModelo': message.split('ANO MODELO: ')[1].split('\n')[0],
        'anoFabricacao': message.split('ANO FABRICAÇÃO: ')[1].split('\n')[0],
        'nacionalidadeFab': message.split('NACIONALIDAE FAB.: ')[1].split('\n')[0],
        'linhaFab': message.split('LINHA FAB.: ')[1].split('\n')[0],
        'motorFab': message.split('MOTOR FAB.: ')[1].split('\n')[0],
        'tipoCarroceria': message.split('TIPO CARROCERIA: ')[1].split('\n')[0]
    }
    dados['localizacao'] = {
        'estado': message.split('ESTADO (UF): ')[1].split('\n')[0],
        'municipio': message.split('MUNICIPIO: ')[1].split('\n')[0],
        'municipioEmplacado': message.split('MUNICIPIO EMPLACADO: ')[1].split('\n')[0]
    }
    dados['dadosCondutor'] = {
        'tipoDocumento': message.split('TIPO DOCUMENTO: ')[1].split('\n')[0],
        'documento': message.split('DOCUMENTO: ')[2].split('\n')[0],
        'nomeCompleto': message.split('NOME COMPLETO: ')[1].split('\n')[0]
    }
    return dados
