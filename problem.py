from inspyred import ec
import numpy as np

class BakeryProblem:

    def __init__(self, available_ingredients, products_price, products_consumption):
        
        self.maximize              = True
        
        self.available_ingredients = available_ingredients
        self.products_price        = products_price
        self.products_consumption  = products_consumption 
        
        self.mins                  = []
        self.maxs                  = []

        for product in self.products_price.keys():
            self.mins.append(0)
            self.maxs.append(np.min(self.available_ingredients/self.products_consumption[product]))
            
        self.bounder               = ec.Bounder(self.mins, self.maxs)

    def fitness_func(self, candidate):
        
        metric = 0

        return metric        
    
    def generator(self, random, args):

            individual = []

            for i in range(0,len(self.products_price)):
                individual.append(random.uniform(self.mins[i], self.maxs[i]))

            return individual

    def evaluator(self, candidates, args):

            fitness = []

            for c in candidates:
                
                ingredient_use = np.zeros(shape=(len(self.available_ingredients)))
                for index in range(0,len(c)):
                    ingredient_use += int(c[index])*self.products_consumption[list(self.products_consumption.keys())[index]]
                    
                ingredient_use = self.available_ingredients - ingredient_use
                
                metric = sum(ingredient_use[ingredient_use < 0])*sum(c)
                for i in range(0, len(c)):
                    metric += int(c[i])*self.products_price[list(self.products_price.keys())[i]]
                
                fitness.append(metric)

            return fitness
