from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("rm brain*.nndf")
        os.system("rm fitness*.nndf")
        self.parents = {}
        self.nextAvailableID = 0
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
        
    
    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
                
        self.Show_Best()
        
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        # self.Print()
        self.Select()
        
    def Spawn(self):
        self.children = {}
        for i in self.parents:
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        for i in self.children:
            self.children[i].Mutate()

    def Evaluate(self, solutions):
        for i in range(c.populationSize):
            solutions[i].Start_Simulation('DIRECT')
            
        for j in range(c.populationSize):
            solutions[j].Wait_For_Simulation_To_End()
        
    
    def Select(self):
        for i in self.parents:
            if self.parents[i].fitness > self.children[i].fitness:
                self.parents[i]=self.children[i]
            
    def Show_Best(self):
        lowest_fitness = 999
        best = 999
        for i in self.parents:
            if self.parents[i].fitness < lowest_fitness:
                lowest_fitness = self.parents[i].fitness
                best = i
        self.parents[best].Start_Simulation("GUI")
        self.parents[best].Wait_For_Simulation_To_End()
        
    def Print(self):
        for i in self.parents:
            print("\n")
            print(i, self.parents[i].fitness, self.children[i].fitness)
            print("\n")