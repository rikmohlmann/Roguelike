class Game:
    def __init__(self):
        self.map_size = 18  # Increase the map size
        self.player_position = [0, 0]
        self.treasure_position = [self.map_size - 1, self.map_size - 1]
        self.enemies_positions = [[1, 1], [2, 2], [3, 3]]  # Add more enemies as needed


    def draw_map(self):
        for y in range(self.map_size):
            for x in range(self.map_size):
                if self.player_position == [x, y]:
                    print('P', end='')
                elif [x, y] in self.enemies_positions:
                    print('E', end='')
                elif self.treasure_position == [x, y]:
                    print('T', end='')
                else:
                    print('.', end='')
                print(' ', end='')
            print()

    def move_player(self, direction):
        if direction == 'up':
            self.player_position[1] = max(0, self.player_position[1] - 1)
        elif direction == 'down':
            self.player_position[1] = min(self.map_size - 1, self.player_position[1] + 1)
        elif direction == 'left':
            self.player_position[0] = max(0, self.player_position[0] - 1)
        elif direction == 'right':
            self.player_position[0] = min(self.map_size - 1, self.player_position[0] + 1)

    def play(self):
        while True:
            self.draw_map()
            direction = input("Enter direction (up, down, left, right): ")
            self.move_player(direction)
            if self.player_position == self.treasure_position:
                print("You found the treasure!")
                break
            elif self.player_position in self.enemies_positions:
                print("You were eaten by an enemy!")
                break

game = Game()
game.play()