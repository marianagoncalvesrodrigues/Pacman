# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""
import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfcaminhos(self, caminhos):
        """
         caminhos: A list of caminhos to take

        This method returns the total cost of a particular sequence of caminhos.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()

def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):  """DFS"""
    
    no = {'estado':problem.getStartState(),'cost':0}  """Recebe o lugar onde nasce o pacman"""
    if problem.isGoalState(no['estado']): """Verifica se j?? est?? no destino"""
        return []
    abertos = []
    abertos.append(no) """Adiciona o no inicial em abertos"""
    fechados = set()
    while True:
        if not abertos: 
            raise Exception('falha na busca')
        no = abertos.pop() """Retiramos o no de abertos"""
        fechados.add(no['estado']) 
        filhos = problem.getSuccessors(no['estado']) """Buscamos todos os filhos desse n??"""
        for filho in filhos: """Verificamos filho a filho encontrado"""
            child = {'estado':filho[0],'acao':filho[1],'custo':filho[2],'pai':no} """Definimos um dicionario filho para que possamos comparar e encontrar o caminho"""
            if child['estado']not in fechados:  """Verifica????o para caso o filho n??o esteja em fechados"""
                if problem.isGoalState(child['estado']): """Verifica????o para caso o filho que est?? sendo avaliado seja o objetivo"""
                    acao = []
                    no = child
                    while 'pai' in no: """Encontrando caminho feito a partir dos pais"""
                        acao.append(no['acao'])
                        no = no['pai']
                    acao.reverse() """Inverte o array"""
                    return acao """Retorna o caminho"""
                abertos.insert(0,child)

def breadthFirstSearch(problem): """BFS"""
    no = {'estado':problem.getStartState(),'cost':0} """Recebe o lugar onde nasce o pacman"""
    if problem.isGoalState(no['estado']): """Verifica se j?? est?? no destino"""
        return []
    abertos = util.Queue() 
    abertos.push(no) """Adiciona o no inicial em abertos"""
    fechados = set()
    while True:
        if abertos.isEmpty():  """caso n??o aja mais caminhos a explorar retorna erro"""
            raise Exception('falha na busca')
        no = abertos.pop()  """Retiramos o no de abertos"""
        fechados.add(no['estado'])   
        filhos = problem.getSuccessors(no['estado'])  """Buscamos todos os filhos desse n??"""
        for filho in filhos:  """Verificamos filho a filho encontrado"""
            child = {'estado':filho[0],'acao':filho[1],'custo':filho[2],'pai':no} """Definimos um dicionario filho para que possamos comparar e encontrar o caminho"""
            if child['estado']not in fechados:  """Verifica????o para caso o filho n??o esteja em fechados"""
                if problem.isGoalState(child['estado']):  """Verifica????o para caso o filho que est?? sendo avaliado seja o objetivo"""
                    acao = []
                    no = child
                    while 'pai' in no: """Encontrando caminho feito a partir dos pais"""
                        acao.append(no['acao'])
                        no = no['pai']
                    acao.reverse() """Inverte o array"""
                    return acao """Retorna o caminho"""
                abertos.push(child)

def uniformCostSearch(problem): """Busca de custo uniforme"""
    abertos = util.PriorityQueue() """cria uma lista de estados que nao foram visitados"""
    fechados = []  """cria uma lista de estados que ja foram visitados"""
    abertos.push((problem.getStartState(), [], 0), 0) """add na fila um objeto que possui estado um antecessor um custo do estado"""
    while not abertos.isEmpty(): """enquanto a lista de itens nao visitados ainda conter estados"""
        pass
    return []
    """guarda o objeto nas variaveis"""
    aux = abertos.pop() 
    filho = aux
    caminhos = aux
    valor = aux
    if(not filho in fechados): """se o filho gerado visitado nao estiver na fila de visitados"""
        fechados.append(filho) """adiciona na lista de visitados"""
        if problem.isGoalState(filho): """se o problema atual for o objetivo"""
            return caminhos """retorna o caminho do estado de objeto"""
        for child, direcao, heurisValue in problem.getSuccessors(filho):
            """para cada crianca gerada, direcao e valor da heuristica no estado sucessor"""
            abertos.push((child, caminhos+[direcao], valor + heurisValue), valor + heurisValue)
            """adiciona na lista de nao visitados essas variaveis, o sucessor, o caminho + direcao, que e o pai de onde veio, e os valores heuristicos"""


def nullHeuristic(state, problem=None):
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    abertos = util.PriorityQueue() """cria uma lista de estados que nao foram visitados """
    abertos.push((problem.getStartState(), [], 0), heuristic(problem.getStartState(), problem) ) """add na fila um objeto que possui estado um antecessor um custo do estado"""
    fechados = []
    while not abertos.isEmpty(): """enquanto a lista de itens nao visitados ainda conter estados"""
        """guarda o objeto nas variaveis"""
        aux = abertos.pop()
        filhos = aux
        caminhos = aux
        valor = aux
        if(not filhos in fechados): """se o filho gerado visitado nao estiver na fila de visitados"""
            fechados.append(filhos) """adiciona na lista de visitados"""
            if problem.isGoalState(filhos):"""se o problema atual for o objetivo"""
                return caminhos #retorna o caminho do estado de objeto
            for child, direcao, heurisValue in problem.getSuccessors(filhos):
                """para cada crianca gerada, direcao e valor da heuristica no estado sucessor"""
                g = valor + heurisValue
               """adiciona um valor para a heuristica"""
                abertos.push((child, caminhos+[direcao], valor + heurisValue), g + heuristic(child, problem))
               """adiciona na lista de nao visitados essas variaveis, o sucessor, o caminho + direcao, que e o pai de onde veio, e os valores heuristicos"""
    return []

bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
