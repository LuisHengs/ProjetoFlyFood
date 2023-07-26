# Função para encontrar o menor percurso em blocos
def encontrar_menor_percurso(matriz, origem, pontos_de_entrega):
    pontos = pontos_de_entrega.copy()
    menor_percurso = None
    menor_custo = float('inf')

    # Gerar todas as permutações possíveis dos pontos de entrega
    permutacoes = gerar_permutacoes(pontos)

    for permutacao in permutacoes:
        percurso = [origem] + permutacao + [origem]
        custo = calcular_custo_percurso(matriz, percurso)
        if custo < menor_custo:  # Verifica se o percurso atual é o menor encontrado até agora
            menor_custo = custo
            menor_percurso = percurso

    return menor_percurso, menor_custo


# Função auxiliar para gerar todas as permutações possíveis
def gerar_permutacoes(pontos):
    if len(pontos) <= 1:
        return [pontos]

    permutacoes = []
    for i in range(len(pontos)):
        ponto_atual = pontos[i]
        pontos_restantes = pontos[:i] + pontos[i+1:]
        permutacoes_restantes = gerar_permutacoes(pontos_restantes)
        for permutacao_restante in permutacoes_restantes:
            permutacoes.append([ponto_atual] + permutacao_restante)

    return permutacoes

# Função auxiliar para calcular o custo de um percurso em blocos
def calcular_custo_percurso(matriz, percurso):
    custo = 0
    for i in range(len(percurso) - 1):
        ponto_atual = percurso[i]
        ponto_proximo = percurso[i + 1]
        custo += calcular_custo_entre_pontos(matriz, ponto_atual, ponto_proximo)
    return custo

# Função auxiliar para calcular o custo entre dois pontos em blocos
def calcular_custo_entre_pontos(matriz, ponto1, ponto2):
    return abs(ponto1[0] - ponto2[0]) + abs(ponto1[1] - ponto2[1])

# Função para ler o arquivo TXT e obter a matriz de entrada
def ler_arquivo(nome_arquivo):
    matriz = []
    origem = None
    pontos_de_entrega = []

    try:
        with open(nome_arquivo, 'r') as arquivo:
            for linha_numero, linha in enumerate(arquivo):
                linha = linha.strip().split()
                matriz.append(linha)
                for coluna, celula in enumerate(linha):
                    if celula == 'R':
                        origem = (linha_numero, coluna)
                    elif celula.isalpha():
                        pontos_de_entrega.append((linha_numero, coluna))

        return matriz, origem, pontos_de_entrega

    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado. Certifique-se de que o arquivo existe e está no diretório correto.")
        return None, None, None

# Função para encontrar a ordem de visita e o custo do menor percurso
def encontrar_ordem_visita(matriz, origem, pontos_de_entrega):
    menor_percurso, menor_custo = encontrar_menor_percurso(matriz, origem, pontos_de_entrega)
    ordem_de_entrega = [ponto for ponto in menor_percurso[1:-1]]
    return ordem_de_entrega, menor_custo


# Leitura do arquivo e execução do algoritmo
matriz, origem, pontos_de_entrega = ler_arquivo("grid_flyfood.txt")

if matriz is not None:
    ordem_de_entrega, custo_percurso = encontrar_ordem_visita(matriz, origem, pontos_de_entrega)
    print("Ordem dos pontos de entrega:", ordem_de_entrega)
    print("Ponto de origem:", origem)
    print("Custo do percurso em Dronômetros:", custo_percurso)
