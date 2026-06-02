# Create a class player with:
# •a class variable player_count 
# •instance variables name and level 
# Track how many players were created.
class Player:
    player_count = 0

    def __init__(self, name, level):
        self.name = name
        self.level = level
        Player.player_count += 1

    def display(self):
        print("Name:", self.name)
        print("Level:", self.level)


p1 = Player("Kookie", 10)
p2 = Player("Tae", 15)
p3 = Player("Chimchim", 20)

p1.display()
p2.display()
p3.display()

print("Total Players:", Player.player_count)