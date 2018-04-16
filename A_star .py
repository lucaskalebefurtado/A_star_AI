#coding: utf-8

class No(object):
    def __init__(self, nome):
        self.nome = nome
        
    
    def add_cidades(self, cidades):
        self.cidades = cidades

    def estimativa(estimativa):
        self.estimativa = estimativa

    def __repr__(self):
        return self.nome


joao_pessoa = No("João Pessoa")
joao_pessoa.estimativa = 460
campina_grande = No("Campina Grande")
campina_grande.estimativa =300 
itabaiana = No("Itabaiana")
itabaiana.estimativa = 360
santa_rita = No("Santa Rita")
santa_rita.estimativa = 451
mamanguape = No("Mamanguape")
mamanguape.estimativa = 380
guarabira = No("Guarabira")
guarabira.estimativa = 340
areia = No("Areia")
areia.estimativa = 316
picui = No("Picui")
picui.estimativa = 250
soledade = No("Soledade")
soledade.estimativa = 243 
coxixola = No("Coxixola")
coxixola.estimativa = 232
patos = No("Patos")
patos.estimativa = 122
monteiro = No("Monteiro")
monteiro.estimativa = 195
catole = No("Catolé do Rocha")
catole.estimativa = 110
pombal = No("Pombal")
pombal.estimativa = 55
itaporanga = No("Itaporanga")
itaporanga.estimativa = 65
sousa = No("Sousa")
sousa.estimativa = 20
cajazeiras = No("Cajazeiras")
cajazeiras.estimativa = 0

joao_pessoa.add_cidades([[itabaiana, 68], [campina_grande, 125], [santa_rita, 26]])
itabaiana.add_cidades([[joao_pessoa, 68], [campina_grande, 65]])
santa_rita.add_cidades([[joao_pessoa, 26], [mamanguape, 38]])
campina_grande.add_cidades([[joao_pessoa, 125], [itabaiana, 65], [coxixola, 128], [areia, 40], [soledade, 58]])
mamanguape.add_cidades([[santa_rita, 38], [guarabira, 42]])
guarabira.add_cidades([[mamanguape, 42], [areia, 41]])
areia.add_cidades([[guarabira, 41], [campina_grande, 40]])
soledade.add_cidades([[campina_grande, 58], [picui, 69], [patos, 117]])
coxixola.add_cidades([[campina_grande, 128], [monteiro, 83]])
picui.add_cidades([[soledade, 69]])
patos.add_cidades([[soledade, 117], [pombal, 71], [itaporanga, 108]])
monteiro.add_cidades([[coxixola, 83], [itaporanga, 224]])
pombal.add_cidades([[patos, 71], [catole, 57], [sousa, 56]])
catole.add_cidades([[pombal, 57]])
itaporanga.add_cidades([[patos, 108], [cajazeiras, 121], [monteiro, 224]])
sousa.add_cidades([[pombal, 56], [cajazeiras, 43]])
cajazeiras.add_cidades([[sousa, 43], [itaporanga, 121]])



def busca( estado_inicial, estado_final):
    cont = 1
    fronteira = [[estado_inicial, 0]]
    explorado = set()
    
    while True:     
        if len(fronteira)== 0:
            break
        
        print("PASSO " + str(cont))
        print (criaStringFronteira(fronteira))

        

        proximoEstado = escolheEstado(fronteira)
        explorado.add(proximoEstado[0])
        print ("Explorado: "+ str(proximoEstado[0])+"\n")

        if proximoEstado[0] == estado_final:
            return proximoEstado
        
        for estado in proximoEstado[0].cidades:
            proximosEstados = estado[0]
            custo = estado[1]

            if proximosEstados not in explorado:
                if naFronteira( fronteira, proximosEstados):
                    mudaFronteira( fronteira, proximosEstados, custo + proximoEstado[1])
                else:
                    fronteira.append([proximosEstados,custo + proximoEstado[1]])
    
        cont += 1


def escolheEstado(fronteira):
    distancia = fronteira[0][1]
    estimativa = fronteira[0][0].estimativa
    menorValor = distancia + estimativa
    posicaoEstado = 0
     
    for i in range(len(fronteira)):
        estado = fronteira[i]
        custo = estado[1] + estado[0].estimativa
       
        if custo < menorValor:
            menorValor = custo
            posicaoEstado = i

    return fronteira.pop(posicaoEstado)


def naFronteira(fronteira, proximosEstados):
    for estado in fronteira:
        if proximosEstados == estado[0]:
            return True
    return False


def mudaFronteira(fronteira,proximosEstados, custo):
    for estado in fronteira:
        if proximosEstados == estado[0]:
            if custo + estado[0].estimativa < estado[1]+ estado[0].estimativa:
                estado[1] = custo
	


def criaStringFronteira(fronteira):
    retorno = ""
    for i in range(len(fronteira)):
        cidade = fronteira[i][0]
        estimativa = fronteira[i][1]+cidade.estimativa
        if (i == 0):
            retorno += "Fronteira: "
        if i == len(fronteira)-1:
            retorno += str(cidade) + ": " + str(estimativa)
        else:
            retorno += str(cidade) + ": " + str(estimativa)+ ", "
        
    
    return retorno
        
        


busca(joao_pessoa, cajazeiras)