import random
import math
import heapq
import time
import statistics

# Defina a semente para tornar os resultados reproduzíveis
seed = 20
random.seed(seed)


class PontodeVisita:
    def __init__(self, numero, coordX, coordY):
        self.numero = numero
        self.coordX = coordX
        self.coordY = coordY


listaPontosdeVisita = [
PontodeVisita(0, 565.0, 575.0),
 PontodeVisita(1, 25.0, 185.0),
 PontodeVisita(2, 345.0, 750.0),
 PontodeVisita(3, 945.0, 685.0),
 PontodeVisita(4, 845.0, 655.0),
 PontodeVisita(5, 880.0, 660.0),
 PontodeVisita(6, 25.0, 230.0),
 PontodeVisita(7, 525.0, 1000.0),
 PontodeVisita(8, 580.0, 1175.0),
 PontodeVisita(9, 650.0, 1130.0),
 PontodeVisita(10, 1605.0, 620.0),
 PontodeVisita(11, 1220.0, 580.0),
 PontodeVisita(12, 1465.0, 200.0),
 PontodeVisita(13, 1530.0, 5.0),
 PontodeVisita(14, 845.0, 680.0),
 PontodeVisita(15, 725.0, 370.0),
 PontodeVisita(16, 145.0, 665.0),
 PontodeVisita(17, 415.0, 635.0),
 PontodeVisita(18, 510.0, 875.0),
 PontodeVisita(19, 560.0, 365.0),
 PontodeVisita(20, 300.0, 465.0),
 PontodeVisita(21, 520.0, 585.0),
 PontodeVisita(22, 480.0, 415.0),
 PontodeVisita(23, 835.0, 625.0),
 PontodeVisita(24, 975.0, 580.0),
 PontodeVisita(25, 1215.0, 245.0),
 PontodeVisita(26, 1320.0, 315.0),
 PontodeVisita(27, 1250.0, 400.0),
 PontodeVisita(28, 660.0, 180.0),
 PontodeVisita(29, 410.0, 250.0),
 PontodeVisita(30, 420.0, 555.0),
 PontodeVisita(31, 575.0, 665.0),
 PontodeVisita(32, 1150.0, 1160.0),
 PontodeVisita(33, 700.0, 580.0),
 PontodeVisita(34, 685.0, 595.0),
 PontodeVisita(35, 685.0, 610.0),
 PontodeVisita(36, 770.0, 610.0),
 PontodeVisita(37, 795.0, 645.0),
 PontodeVisita(38, 720.0, 635.0),
 PontodeVisita(39, 760.0, 650.0),
 PontodeVisita(40, 475.0, 960.0),
 PontodeVisita(41, 95.0, 260.0),
 PontodeVisita(42, 875.0, 920.0),
 PontodeVisita(43, 700.0, 500.0),
 PontodeVisita(44, 555.0, 815.0),
 PontodeVisita(45, 830.0, 485.0),
 PontodeVisita(46, 1170.0, 65.0),
 PontodeVisita(47, 830.0, 610.0),
 PontodeVisita(48, 605.0, 625.0),
 PontodeVisita(49, 595.0, 360.0),
 PontodeVisita(50, 1340.0, 725.0),
 PontodeVisita(51, 1740.0, 245.0)
]

tamanhoDaLista = len(listaPontosdeVisita)

# Parâmetros do algoritmo genético
tamanhoDaPopulacao = 50
qtdGeracao = 500
tamanhoCorte = int(tamanhoDaLista * 0.95)
numeroMaximoDeTentativas = 1000


class Cromossomo:
    caminho = []
    valorFitness = -1

    def __lt__(self, other):
        return self.calculaFitness() < other.calculaFitness()

    def calculaFitness(self):
        global listaPontosdeVisita
        global tamanhoDaLista

        if self.valorFitness == -1:
            soma = 0
            for x in range(tamanhoDaLista - 1):
                verticeUmDaVez = listaPontosdeVisita[self.caminho[x]]
                verticeDoisDaVez = listaPontosdeVisita[self.caminho[x + 1]]
                soma += math.sqrt(((verticeUmDaVez.coordX - verticeDoisDaVez.coordX) ** 2) + (
                            (verticeUmDaVez.coordY - verticeDoisDaVez.coordY) ** 2))

            
            ultimo_ponto = listaPontosdeVisita[self.caminho[-2]]
            ponto_retorno = listaPontosdeVisita[0]
            soma += math.sqrt(((ponto_retorno.coordX - ultimo_ponto.coordX) ** 2) + (
                        (ponto_retorno.coordY - ultimo_ponto.coordY) ** 2))

            self.valorFitness = round(soma, 4)

        return self.valorFitness


inicializadorDaPopulacao = []
for x in range(1, tamanhoDaLista):
    inicializadorDaPopulacao.append(x)


def geraPopulacao():
    populacao = []

    for x in range(tamanhoDaPopulacao):
        cromossomo = Cromossomo()
        cromossomo.caminho = inicializadorDaPopulacao[:]
        random.shuffle(cromossomo.caminho)
        cromossomo.caminho = [0] + cromossomo.caminho + [0]  
        heapq.heappush(populacao, cromossomo)
    return populacao


def selecaoIndividuo(parametroPopulacao):
    valorRandomUm = random.randrange(tamanhoDaPopulacao // 2)
    valorRandomDois = random.randrange(tamanhoDaPopulacao // 2, tamanhoDaPopulacao)

    if parametroPopulacao[valorRandomUm].calculaFitness() < parametroPopulacao[valorRandomDois].calculaFitness():
        return parametroPopulacao[valorRandomUm]
    else:
        return parametroPopulacao[valorRandomDois]


def crossoverIndividuo(individuoUm, individuoDois):
    global tamanhoDaPopulacao
    global tamanhoDaLista

    listaNovosIndividuos = []
    contador = 0

    while contador < qtdGeracao:
        qtdGenesAdicionados = 0
        geneDosPaisParaFilho = individuoUm.caminho[:tamanhoCorte]

        for x in individuoDois.caminho:
            if qtdGenesAdicionados == (tamanhoDaLista - tamanhoCorte):
                break
            if x not in geneDosPaisParaFilho:
                geneDosPaisParaFilho.append(x)
                qtdGenesAdicionados += 1

        geneDosPaisParaFilho = mutacaoIndividuo(geneDosPaisParaFilho)
        novoIndividuo = Cromossomo()
        novoIndividuo.caminho = geneDosPaisParaFilho
        listaNovosIndividuos.append(novoIndividuo)
        contador += 1

    return listaNovosIndividuos


def mutacaoIndividuo(caminhoDoNovoFilhoGerado):
    geneUm = random.randrange(1, tamanhoDaLista)  
    geneDois = random.randrange(1, tamanhoDaLista)  
    caminhoDoNovoFilhoGerado[geneUm], caminhoDoNovoFilhoGerado[geneDois] = caminhoDoNovoFilhoGerado[geneDois], \
    caminhoDoNovoFilhoGerado[geneUm]
    return caminhoDoNovoFilhoGerado


melhorSolucao = True
numeroTentativas = 0


def atualizaPopulacao(parametroPopulacao, parametroListaDeNovosIndividuos):
    global melhorSolucao
    global numeroTentativas

    for x in parametroListaDeNovosIndividuos:
        individuoMaiorFitness = heapq.nlargest(1, parametroPopulacao)[0]
        menor = parametroPopulacao[0]

        xFitness = x.calculaFitness()
        if xFitness < individuoMaiorFitness.calculaFitness():
            parametroPopulacao.remove(individuoMaiorFitness)
            heapq.heappush(parametroPopulacao, x)
            heapq.heapify(parametroPopulacao)

            if xFitness < menor.calculaFitness():
                numeroTentativas = 0
            else:
                numeroTentativas += 1

        else:
            numeroTentativas += 1

        if numeroTentativas == numeroMaximoDeTentativas:
            melhorSolucao = False

    return parametroPopulacao


def obtemMelhor(parametroPopulacao):
    return parametroPopulacao[0]


populacao = geraPopulacao()

fitness_por_geracao = []

tempo_inicio = time.time()

melhor_fitness_geral = float('inf')
geracao_melhor_fitness_geral = 0

geracao = 1
while geracao <= qtdGeracao:
    individuoUm = selecaoIndividuo(populacao)
    individuoDois = selecaoIndividuo(populacao)
    novosIndividuosGerados = crossoverIndividuo(individuoUm, individuoDois)
    populacao = atualizaPopulacao(populacao, novosIndividuosGerados)

    melhor_fitness = obtemMelhor(populacao).calculaFitness()
    fitness_por_geracao.append(melhor_fitness)

    if melhor_fitness < melhor_fitness_geral:
        melhor_fitness_geral = melhor_fitness
        geracao_melhor_fitness_geral = geracao

    print(f'Geração {geracao}: Melhor Fitness = {melhor_fitness}')

    
    melhorIndividuo = obtemMelhor(populacao)

    
    if len(melhorIndividuo.caminho) > 1 and melhorIndividuo.caminho[-1] == 0:
        melhorIndividuo.caminho.pop()

    
    melhorIndividuo.caminho.append(0)

    print(f"Melhor indivíduo (Menor distância): {melhorIndividuo.caminho}")
    print(f"Fitness: {melhorIndividuo.calculaFitness()}")
    print()

    geracao += 1

tempo_fim = time.time()

melhorIndividuoGeral = obtemMelhor(populacao)
tempo_total = tempo_fim - tempo_inicio
desvio_padrao_fitness = statistics.stdev(fitness_por_geracao)

print(
    f"Melhor indivíduo geral (Menor distância) na Geração {geracao_melhor_fitness_geral}: {melhorIndividuoGeral.caminho}")
print(f"Fitness: {melhorIndividuoGeral.calculaFitness()}")
print(f"Tempo de execução total: {tempo_total} segundos")
print(f"Desvio Padrão do Fitness das Gerações: {desvio_padrao_fitness}")
