def consulta(message):
    resultado = {}
    #################
    resultado['placa'] = message.split('PLACA: ')[1].split('\n')[0]
    resultado['placaAntiga'] = message.split('PLACA ANTIGA: ')[1].split('\n')[0]
    resultado['placaNova'] = message.split('PLACA NOVA: ')[1].split('\n')[0]
    resultado['placaModelo'] = message.split('PLACA MODELO: ')[1].split('\n')[0]
    resultado['chassi'] = message.split('CHASSI: ')[1].split('\n')[0]
    resultado['renavam'] = message.split('RENAVAM: ')[1].split('\n')[0]
    resultado['anoFabricacao'] = message.split('ANO FABRICAÇÃO: ')[1].split('\n')[0]
    resultado['municipio'] = message.split('MUNICIO: ')[1].split('\n')[0]
    resultado['placaUf'] = message.split('PLACA UF: ')[1].split('\n')[0]
    resultado['modelo'] = message.split('MODELO: ')[1].split('\n')[0]
    resultado['combustivel'] = message.split('COMBUSTIVEL: ')[1].split('\n')[0]
    resultado['potencia'] = message.split('POTENCIA: ')[1].split('\n')[0]
    resultado['tipoVeiculo'] = message.split('TIPO VEICULO: ')[1].split('\n')[0]
    resultado['especieVeiculo'] = message.split('ESPECIE VEICULO: ')[1].split('\n')[0]
    resultado['cor'] = message.split('COR: ')[1].split('\n')[0]
    resultado['quantidadePassageiros'] = message.split('QUANTIDADE PASSAGEIROS: ')[1].split('\n')[0]
    resultado['tipoDocumento'] = message.split('TIPO DOCUMENTO: ')[1].split('\n')[0]
    resultado['cpfCnpj'] = message.split('CPF/CNPJ: ')[1].split('\n')[0]
    #################
    return resultado
