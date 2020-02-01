import numpy as np
from modules.resourcetoken import ResourceToken

class Bag():
    def __init__(self, pool):
        # Initialize variables
        self.tokens =  []
        self.pool = pool

        # Populate the tokens list and shuffle it
        self.populate()
        self.shuffle()
        
    def populate(self):
        # Add components to tokens[]
        for component in self.pool:
            name, count = self.pool[component]

            if count == 0:
                print("[INFO] Skipping ", name)
                continue

            for i in range(0, count):
                self.tokens.append(ResourceToken(name))

        print("[INFO] Total amount of tokens in the bag: ", len(self.tokens))

    def shuffle(self):
        np.random.shuffle(self.tokens)

    def draw_token(self):
        # Return the last item from the list
        # and remove it
        return self.tokens.pop()