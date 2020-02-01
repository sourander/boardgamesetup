class Board():
    def __init__(self, location_pool):
        self.location_pool = location_pool
        self.locations = []

        self.populate_locations()

    def populate_locations(self):
        for loc in self.location_pool:
            name, slots = self.location_pool[loc]

            # Initialize the location and add it to list
            this_location = Location(name, slots)

            # Append the location also to the list so that we can access it easier
            self.locations.append(this_location)

    def report(self):
        for i, loc in enumerate(self.locations):
            name = loc.name
            
            line_to_print = name + ": \t"
            
            if i % 6 == 0:
                print(" ")

            # Create a list of token names 
            # e.g. ['Valkyrie', 'Gold']
            tokens = []
            for token in loc.tokens:
                tokens.append(token.name)

            # Find all unique names and count them
            uniques = set(tokens)
            for unique in uniques:
                c = tokens.count(unique)
                addition = "{}x {}    ".format(c, unique)
                line_to_print = line_to_print + addition

            print(line_to_print)