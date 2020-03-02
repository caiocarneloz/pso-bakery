from inspyred import ec
import numpy as np

class BakeryProblem:

    def __init__(self, available_ingredients, products_price, products_consumption):
        
        self.maximize              = True
        
        self.available_ingredients = available_ingredients
        self.products_price        = products_price
        self.products_consumption  = products_consumption 
        
        mins = []
        maxs = []

        for product in self.products_price.keys():
            mins.append(0)
            maxs.append(np.min(self.available_ingredients/self.products_consumption[product]))
            
        self.bounder               = ec.Bounder(lower_bound=mins, upper_bound=maxs)
    
    def generator(self, random, args):
        
        particle = []

        for i in range(0,len(self.products_price)):
            particle.append(random.uniform(self.bounder.lower_bound[i], self.bounder.upper_bound[i]))

        return particle

    def evaluator(self, candidates, args):

            fitness = []

            for c in candidates:
                
                ingredient_use = np.zeros(shape=(len(self.available_ingredients)))
                
                for index in range(0,len(c)):
                    ingredient_use += int(c[index])*self.products_consumption[list(self.products_consumption.keys())[index]]
                    
                ingredient_use = self.available_ingredients - ingredient_use
                
                metric = sum(ingredient_use[ingredient_use < 0])*sum(c)
                
                metric += sum(c*np.array(list(self.products_price.values()), dtype=float))
                
                fitness.append(metric)

            return fitness
