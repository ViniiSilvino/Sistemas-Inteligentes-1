##  Grupo 8 - github: https://github.com/ViniiSilvino/Sistemas-Inteligentes-1
#
#   Thiago Tieghi           2272083
#   Rafael Ribas de Lima    2461650
#   Vinicius Lopes Silvino  2461684

import collections

einicial = (3,5,8,2,1,7,4,0,6)
eobjetivo = (1, 2, 3, 8, 0, 4, 7, 6, 5)

def imprimir_tabuleiro(estado):
    for i in range(3):
        linha = estado[i*3:i*3+3]
        print(f"{linha[0]:2} {linha[1]:2} {linha[2]:2}")
    print("-" * 8)

def obter_posicao_vazia(estado):
    return estado.index(0)

def gerar_sucessores(estado): #esquerda, cima, direita, baixo.
    sucessores = []
    pos_vazia = obter_posicao_vazia(estado)
    pos_vazia_x, pos_vazia_y = divmod(pos_vazia, 3)

    movimentos_possiveis = []

    if pos_vazia_y > 0: #esquerda
        movimentos_possiveis.append(pos_vazia - 1)
    if pos_vazia_x > 0: #cima
        movimentos_possiveis.append(pos_vazia - 3)
    if pos_vazia_y < 2: #direita
        movimentos_possiveis.append(pos_vazia + 1)
    if pos_vazia_x < 2: #baixo
        movimentos_possiveis.append(pos_vazia + 3)

    elista = list(estado)
    for nova_pos in movimentos_possiveis:
        novo_elista = elista[:]
        novo_elista[pos_vazia], novo_elista[nova_pos] = (
            novo_elista[nova_pos],
            novo_elista[pos_vazia],
        )
        sucessores.append(tuple(novo_elista))

    return sucessores



def bfs(einicial, eobjetivo):# =================== Busca em Largura (BFS)===================

    abertos = collections.deque([(einicial, 0, [einicial])]) # (estado, profundidade, caminho)
    fechados = {einicial}
    iteracoes = 0
    
    while abertos:
        iteracoes += 1
        estado_atual, profundidade, caminho = abertos.popleft()
        
        if estado_atual == eobjetivo:
            print(f"Solução encontrada em {iteracoes} iterações.")
            print(f"Caminho da solução (Profundidade: {profundidade}):")
            for i, passo in enumerate(caminho):
                print(f"Passo {i}:")
                imprimir_tabuleiro(passo)
            return True
        
        sucessores = gerar_sucessores(estado_atual)
        for sucessor in sucessores:
            if sucessor not in fechados:
                fechados.add(sucessor)
                novo_caminho = caminho + [sucessor]
                abertos.append((sucessor, profundidade + 1, novo_caminho))

    print(f"Solução não encontrada após {iteracoes} iterações.")
    return False


def dfs_com_limite(einicial, eobjetivo, limite=5):# =========== Algoritmo de Busca em Profundidade com Limite (DFS) ===========

    abertos = [(einicial, 0, [einicial])] # (estado, profundidade, caminho)
    iteracoes = 0
    
    while abertos:
        iteracoes += 1
        estado_atual, profundidade, caminho = abertos.pop() # pop pq é pilha (LIFO)
        
        if estado_atual == eobjetivo:
            print(f"Solução encontrada em {iteracoes} iterações.")
            print(f"Caminho da solução (Profundidade: {profundidade}):")
            for i, passo in enumerate(caminho):
                print(f"Passo {i}:")
                imprimir_tabuleiro(passo)
            return True
        
        if profundidade < limite:
            sucessores = gerar_sucessores(estado_atual)
            # adiciona sucessores na pilha pra não revisitar estados 
            for sucessor in sucessores[::-1]:  # inverte a ordem
                if sucessor not in set(caminho):  
                    novo_caminho = caminho + [sucessor]
                    abertos.append((sucessor, profundidade + 1, novo_caminho))

    print(f"Solução não encontrada no limite de profundidade {limite} após {iteracoes} iterações.")
    return False


if __name__ == "__main__":
    print("=== Executando BFS (Busca em Largura) ===")
    bfs(einicial, eobjetivo)
    print("\n" + "="*50 + "\n")
    print("=== Executando DFS (Busca em Profundidade) com Limite de Profundidade 5 ===")
    dfs_com_limite(einicial, eobjetivo, limite=5)