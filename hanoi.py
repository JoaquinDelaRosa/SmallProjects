from copy import deepcopy
import heapq

PEGS = 3

class Disc:
    def __init__(self, size):
        self.size = size

class Peg:
    def __init__(self):
        self.discs = []
    
    def print(self):
        arr = []
        for i in range(0, len(self.discs)):
            arr.append(self.discs[i].size)
        
        print(arr)


# Configure hanoi
class Game:
    def __init__(self, pegs, discs):
        self.discs = discs
        self.pegs = [Peg() for i in range(0, pegs)]
        self.depth = 1000000
        self.index = -1
        self.neighbors = []
        self.done = False
        self.parent = None

    def initializeState(self):
        for i in range(self.discs, 0, -1): 
            self.pegs[0].discs.append(Disc(i))

    def initializeWinning(self):
         for i in range(self.discs, 0, -1): 
            self.pegs[2].discs.append(Disc(i))

    def isEqual(self, other):
        if len(other.pegs) != len(self.pegs):
            return False

        for i in range(0, len(self.pegs)):
            if(len(self.pegs[i].discs) != len(other.pegs[i].discs)):
                return False
            for d in range(0, len(self.pegs[i].discs)):
                if(self.pegs[i].discs[d].size != other.pegs[i].discs[d].size):
                    return False

        return True

    def __lt__(self, other):
        return self.depth < other.depth

    def printGame(self):
        print("-------------")
        for p in self.pegs:
            p.print()
        print("-------------")

    def generateCopy(self):
        return deepcopy(self.pegs)

class GameSolver:
    def __init__(self):
        self.currentState = None
        self.goal = None
        self.generatorStack = []
        self.visitedStates = []
        self.finishedStates = []
        self.graph = [[]  for j in range(0, 10000000)]

    def generateGraph(self, g):
        self.generatorStack.append(g)

        while(len(self.generatorStack) !=0):
            self.currentState = self.generatorStack.pop(0)
            isFound = False

            for game in self.finishedStates:
                if(game.isEqual(self.currentState)):
                    isFound = True
                    break
                
            if isFound:
                continue

            self.finishedStates.append(self.currentState)

            if self.currentState.index == -1:
                self.currentState.index = len(self.finishedStates) - 1
                print(self.currentState.index)

            moves = self.generateMoves()
            for m in moves:
                finished = False
                for game in self.finishedStates:
                    if game.isEqual(m) and game.index != -1:
                        self.graph[game.index].append(self.currentState.index)
                        self.graph[self.currentState.index].append(game.index)
                        finished = True
                        break
                # If not finished add to exploration list
                if not finished:
                    self.generatorStack.insert(0, m)


    def solveGame(self, goal):
        self.visitedStates = self.finishedStates
        self.findGoal(goal)
        # Use Dijkstra's to find the shortest path in the graph starting at the first point
        self.visitedStates[0].depth = 0
        examine = [self.visitedStates[0]]
        finished = []

        while(len(self.visitedStates) != 0 and len(examine) != 0):
            curr = examine.pop(0)

            if curr.isEqual(self.visitedStates[self.goal]):
                print("Finished solving. Displaying path...")
                self.printPath(curr)
                return curr.depth

            for n in self.graph[curr.index]:
                if not self.visitedStates[n] in finished:
                    if(self.visitedStates[n].depth >= curr.depth + 1):
                        self.visitedStates[n].parent = curr
                
                    self.visitedStates[n].depth = min(self.visitedStates[n].depth, curr.depth + 1)
                    heapq.heappush(examine, self.visitedStates[n])

            #Remove unnecessary elements. This optimizes the search time
            for game in examine:
                if game.done:
                    examine.remove(game)
                
            heapq.heapify(examine)

            finished.append(curr)
            curr.done = True

        return -1

    def printPath(self, g):
        if g != None:
            self.printPath(g.parent)
            g.printGame()

    def findGoal(self, goal):
        for states in self.visitedStates:
            if(states.isEqual(goal)):
                self.goal = self.visitedStates.index(states)
                return

    def generateMoves(self):
        p = len(self.currentState.pegs)
        moves = []
        for i in range(0, p):
            currDisc = len(self.currentState.pegs[i].discs) - 1
            for j in range(0, p):
                if i == j:
                    continue
                otherDisc = len(self.currentState.pegs[j].discs) - 1
                if currDisc < 0:
                    continue
                elif otherDisc < 0:
                    # Move to empty peg
                    newState = Game(PEGS , self.currentState.discs)
                    newState.pegs = self.currentState.generateCopy()
                    move = newState.pegs[i].discs.pop()
                    newState.pegs[j].discs.append(move)
                    moves.append(newState)
                else:
                    x = self.currentState.pegs[i].discs[currDisc].size
                    y = self.currentState.pegs[j].discs[otherDisc].size

                    # Condition for the problem
                    if(y %2 == 1 and (x < y or y == x - 1) )  or ((y % 2 == 0 and x < y )) :
                        # Initialize new game state
                        newState = Game(PEGS , self.currentState.discs)
                        newState.pegs = self.currentState.generateCopy()
                        move = newState.pegs[i].discs.pop()
                        newState.pegs[j].discs.append(move)
                        moves.append(newState)

        return moves

    
def main():
    game = Game(3, 8)
    win = Game(3, 8)
    gamesolver = GameSolver()
    game.initializeState()
    win.initializeWinning()
    gamesolver.generateGraph(game)
    print("Done generating graph with " + str(len(gamesolver.finishedStates)) + " states detected...")
    print(gamesolver.solveGame(win))

main()