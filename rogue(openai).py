import random

# Game settings
MAP_SIZE = 8
PLAYER = "P"
EMPTY = "."
ENEMY = "E"
TREASURE = "T"

# Initialize the map
game_map = [[EMPTY for _ in range(MAP_SIZE)] for _ in range(MAP_SIZE)]

# Place the player
player_position = [MAP_SIZE // 2, MAP_SIZE // 2]
game_map[player_position[0]][player_position[1]] = PLAYER

# Place enemies and treasures
for _ in range(5):
    enemy_position = [random.randint(0, MAP_SIZE - 1), random.randint(0, MAP_SIZE - 1)]
    treasure_position = [random.randint(0, MAP_SIZE - 1), random.randint(0, MAP_SIZE - 1)]
    game_map[enemy_position[0]][enemy_position[1]] = ENEMY
    game_map[treasure_position[0]][treasure_position[1]] = TREASURE

def print_map():
    for row in game_map:
        print(" ".join(row))
    print("\n")

def move_player(direction):
    global player_position
    game_map[player_position[0]][player_position[1]] = EMPTY
    if direction == "w" and player_position[0] > 0:
        player_position[0] -= 1
    elif direction == "s" and player_position[0] < MAP_SIZE - 1:
        player_position[0] += 1
    elif direction == "a" and player_position[1] > 0:
        player_position[1] -= 1
    elif direction == "d" and player_position[1] < MAP_SIZE - 1:
        player_position[1] += 1
    game_map[player_position[0]][player_position[1]] = PLAYER

# Game loop
while True:
    print_map()
    move = input("Move (w/a/s/d): ")
    move_player(move)
