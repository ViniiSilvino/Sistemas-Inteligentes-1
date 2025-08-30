##  Grupo 8 - github: 
#
#   Thiago Thiegi           2272083
#   Rafael Ribas de Lima    2461650
#   Vinicius Lopes Silvino  2461684

import sys
INF = sys.maxsize #parte nula do grafo (A->A...)

class Backtracking:
    def __init__(self, grafo, V_inicial): # A=0, B=1, C=2, D=3, E=4 (vinicial)

        self.grafo = grafo
        self.V_inicial = V_inicial
        self.N_vertices = len(grafo)
        
        self.LE = [] #caminho atual
        self.LNE = [] #lista de novos estados
        self.BSS = [] #beco sem saída
    
    def get_vizinhos(self, vertice): 

        vizinhos = []
        for i in range(self.N_vertices):
            if self.grafo[vertice][i] > 0 and self.grafo[vertice][i] != INF:
                vizinhos.append(i)
        return vizinhos #lista de vizinhos do vertice
    
    def calcular_distancia_total(self, caminho):

        distancia_total = 0
        for i in range(len(caminho) - 1):
            vertice_atual = caminho[i]
            proximo_vertice = caminho[i+1]
            distancia_total += self.grafo[vertice_atual][proximo_vertice]
        
        return distancia_total

    def buscar_caminho(self): # usa o algoritmo da aula TSP
# comentarios maiusculo = pseudocodigo slide
        # inicialização as filas
        self.LE = [self.V_inicial]
        self.LNE = [self.V_inicial]
        self.BSS = []
        EC = self.V_inicial
        
        while self.LNE: # Enquanto LNE != [ ], faça:

            # Se EC == Objetivo (ou atende descrição do objetivo), então: 
            if len(self.LE) == self.N_vertices and self.grafo[EC][self.V_inicial] > 0 and self.grafo[EC][self.V_inicial] != INF:
                self.LE.append(self.V_inicial) # poe o vértice inicial no final tmb para fechar o ciclo
                return self.LE # Retorna LE; // Se houver sucesso, retorna a lista de estados no caminho

            # encontra os filhos de EC que ainda não foram visitados
            vizinhos = self.get_vizinhos(EC)
            novos_filhos = []
            for vizinho in vizinhos:
                # A regra é ignorar estados que já estão em LE
                if vizinho not in self.LE:
                    novos_filhos.append(vizinho)
            
            # Se EC não tem filhos, então:
            if novos_filhos:
                self.LNE.extend(novos_filhos)          # poe os novos filhos em LNE
                self.LNE.remove(EC)                    # tira o EC de LNE (porque ele já foi explorado)
                EC = self.LNE[0]                       # Define o próximo estado corrente como o primeiro da LNE
                # Adiciona o novo estado corrente ao LE (caminho atual)
                self.LE.append(EC)
            else:
                self.BSS.append(EC)                # acrescenta EC em BSS;

                while self.LE and EC == self.LE[-1]: # Enquanto LE não está vazio e EC == o primeiro elemento de LE [retrocesso]
                    self.LE.pop() # tira o BSS

                    if EC in self.LNE: #tira EC da LNE 
                        self.LNE.remove(EC)

                    if self.LE:  # O novo EC é o último elemento da LE
                        EC = self.LE[-1]
        
        return None # sem caminho possível


if __name__ == '__main__':
    
    grafo = [
        # A=0, B=1, C=2, D=3, E=4
        [INF, 100, 125, 100, 75],
        [100, INF, 50, 75, 125],
        [125, 50, INF, 100, 125],
        [100, 75, 100, INF, 50],
        [75, 125, 125, 50, INF]
    ]

    letras_vertices = ['A', 'B', 'C', 'D', 'E']
    
    # instancia o backtracking lancando o grafo e o primeiro vertice ===================================================== 
    solucao = Backtracking(grafo, 0) 
    caminho_imagem = solucao.buscar_caminho()  # inicia a busca

    if caminho_imagem:
        caminho_letras = [letras_vertices[v] for v in caminho_imagem]
        distancia_percorrida = solucao.calcular_distancia_total(caminho_imagem)

        print(f"\nCaminho encontrado: {' -> '.join(caminho_letras)}")
        print(f"Distância total percorrida: {distancia_percorrida}\n")
    else:
        print("\nNenhum caminho que percorra todos os vértices foi encontrado.\n")