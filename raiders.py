import numpy as np

class Cube():
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class Bag():
    def __init__(self, pool):
        # Initialize variables
        self.cubes =  []
        self.pool = pool

        # Populate the cubes list and shuffle it
        self.populate()
        self.shuffle()
        
    def populate(self):
        # Add components to cubes[]
        for component in self.pool:
            name, count = pool[component]

            if count == 0:
                print("[INFO] Skipping ", name)
                continue

            for i in range(0, count):
                self.cubes.append(Cube(name))

        print("[INFO] Total amount of cubes in the bag: ", len(self.cubes))

    def shuffle(self):
        np.random.shuffle(self.cubes)

    def draw_cube(self):
        # Return the last item from the list
        # and remove it
        return self.cubes.pop()


class Location():
    def __init__(self, name, slots):
        self.name = name
        self.slots = slots
        self.cubes = []

        self.populate()

    def populate(self):
        # For each slots in the location, 
        # get a cube from the Bag.
        for i in range(0, self.slots):
            cube = bag.draw_cube()
            self.cubes.append(cube)

    def __repr__(self):
        return "{} with items {}".format(self.name, self.cubes)



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

            # Create a list of cube names 
            # e.g. ['Valkyrie', 'Gold']
            cubes = []
            for cube in loc.cubes:
                cubes.append(cube.name)

            # Find all unique names and count them
            uniques = set(cubes)
            for unique in uniques:
                c = cubes.count(unique)
                addition = "{}x {}    ".format(c, unique)
                line_to_print = line_to_print + addition

            print(line_to_print)

def menu():
    # Set default values
    golds = 18
    meads = 0
    jarls = 0

    query = input("Are you playing with Hall of Heroes: [y/n]: ")
    hallOfHeroes = True if query.lower() == "y" else False

    query = input("Are you playing with Fields of Fame: [y/n]: ")
    fieldOfFame = True if query.lower() == "y" else False

    print("[INFO] Playing with Hall of Heroes: ", hallOfHeroes)
    print("[INFO] Playing with Fields of Fame: ",fieldOfFame)

    if hallOfHeroes:
        golds = golds + 5
        meads = 40

    if fieldOfFame:
        jarls = 12

    pool = {1: ("Valk", 18), 
            2: ("Gold", golds),
            3: ("Iron", 18),
            4: ("Cows", 26), 
            5: ("Mead", meads),
            6: ("Jarl", jarls) }

    # Generate a pool of locations with their item slots
    location_pool = {1: ("Fortress", 2),
                     2: ("Fortress", 3),
                     3: ("Fortress", 2),
                     4: ("Fortress", 2),
                     5: ("Fortress", 2),
                     6: ("Fortress", 3),
                     7: ("Monastery", 3),
                     8: ("Monastery", 2),
                     9: ("Outpost", 3),
                     10: ("Outpost", 3), 
                     11: ("Monastery", 2), 
                     12: ("Monastery", 3), 
                     13: ("Harbour", 4),
                     14: ("Harbour", 3),
                     15: ("Harbour", 4),
                     16: ("Outpost", 4),
                     17: ("Outpost", 3),
                     18: ("Harbour", 3),
                     19: ("Harbour", 4),
                     20: ("Harbour", 4),
                     21: ("Harbour", 4),
                     22: ("Harbour", 3),
                     23: ("Harbour", 4)}

    return pool, location_pool

pool, location_pool = menu()

bag = Bag(pool)
board = Board(location_pool)

board.report()