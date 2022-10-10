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

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    no = {'estado':problem.getStartState(),'cost':0}
    if problem.isGoalState(no['estado']):
        return []
    abertos = []
    abertos.append(no)
    fechados = set()
    while True:
        if not abertos:
            raise Exception('falha na busca')
        no = abertos.pop()
        fechados.add(no['estado'])
        filhos = problem.getSuccessors(no['estado'])
        for filho in filhos:
            child = {'estado':filho[0],'acao':filho[1],'custo':filho[2],'pai':no}
            if child['estado']not in fechados:
                if problem.isGoalState(child['estado']):
                    acao = []
                    no = child
                    while 'pai' in no:
                        acao.append(no['acao'])
                        no = no['pai']
                    acao.reverse()
                    return acao
                abertos.insert(0,child)

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    no = {'estado':problem.getStartState(),'cost':0}
    if problem.isGoalState(no['estado']):
        return []
    abertos = util.Queue()
    abertos.push(no)
    fechados = set()
    while True:
        if abertos.isEmpty():
            raise Exception('falha na busca')
        no = abertos.pop()
        fechados.add(no['estado'])
        filhos = problem.getSuccessors(no['estado'])
        for filho in filhos:
            child = {'estado':filho[0],'acao':filho[1],'custo':filho[2],'pai':no}
            if child['estado']not in fechados:
                if problem.isGoalState(child['estado']):
                    acao = []
                    no = child
                    while 'pai' in no:
                        acao.append(no['acao'])
                        no = no['pai']
                    acao.reverse()
                    return acao
                abertos.push(child)

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    abertos = util.PriorityQueue()
    abertos.push((problem.getStartState(), [], 0), 0)
    fechados = []
    while not abertos.isEmpty():
        filho, caminhos, valor = abertos.pop()
        if(not filho in fechados):
            fechados.append(filho)
            if problem.isGoalState(filho):
                return caminhos
            for child, direcao, heurisValue in problem.getSuccessors(filho):
                abertos.push((child, caminhos+[direcao], valor + heurisValue), valor + heurisValue)
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    abertos = util.PriorityQueue()
    abertos.push( (problem.getStartState(), [], 0), heuristic(problem.getStartState(), problem) )
    fechados = []
    while not abertos.isEmpty():
        filhos, caminhos, valor = abertos.pop()
        if(not filhos in fechados):
            fechados.append(filhos)
            if problem.isGoalState(filhos):
                return caminhos
            for child, direcao, heurisValue in problem.getSuccessors(filhos):
                g = valor + heurisValue
                abertos.push((child, caminhos+[direcao], valor + heurisValue), g + heuristic(child, problem))
    return []

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch