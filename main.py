import pygame
from player import Player
from enemy import Enemy
from powerup import Bonus

print("hello")

pygame.init()

FONT = pygame.font.SysFont('Arial', 200)

#size of window and each tile

tile_size = 64

WIDTH = 960

HEIGHT = 960

#WHITE = (0, 0, 0)

#loading images
wall = pygame.image.load("images\wall_sprite_a.png")
ground = pygame.image.load("images\ground_sprite.png")
stone = pygame.image.load("images\stone_sprite.png")
hero = pygame.image.load("images\player_sprite.png")
hero2 = pygame.image.load("images\player2_sprite.png")
bomb_p = pygame.image.load("images\\bomb_sprite.png")
explosion_p = pygame.image.load("images\explosion_sprite.png")
enemy_ghost = pygame.image.load("images\enemy1_sprite.png")
enemy_circle = pygame.image.load("images\enemy2_sprite.png")
bomb_range = pygame.image.load("images\\bomb_range_sprite.png")
bomb_number = pygame.image.load("images\\bomb_number_sprite.png")

map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 3, 0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 6, 1],
    [1, 0, 1, 2, 1, 2, 1, 2, 1, 2, 1, 0, 1, 0, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1],
    [1, 2, 1, 2, 1, 0, 1, 2, 1, 2, 1, 2, 1, 2, 1],
    [1, 2, 2, 2, 0, 6, 0, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 2, 1, 0, 1, 2, 1, 2, 1, 2, 1, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 2, 1, 2, 1, 2, 1, 0, 1, 2, 1, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 0, 5, 0, 2, 2, 2, 1],
    [1, 2, 1, 2, 1, 2, 1, 2, 1, 0, 1, 2, 1, 2, 1],
    [1, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 0, 1, 0, 1, 2, 1, 2, 1, 2, 1, 2, 1, 0, 1],
    [1, 5, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 4, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

def game_over(result):
    death_t = 1500
    while True:
        if result == 0:
            game_over_text = FONT.render("Player2 wins", True, (200, 200, 200))
            screen.fill((0,0,0))
            screen.blit(game_over_text, (WIDTH/2 - (game_over_text.get_width()/2), HEIGHT/2 - game_over_text.get_height()/2))
            pygame.display.update()
            death_t -= 1
            if death_t == 0:
                pygame.quit()

        elif result == 1:
            game_over_text = FONT.render("Player1 wins", True, (200, 200, 200))
            screen.fill((0,0,0))
            screen.blit(game_over_text, (WIDTH/2 - (game_over_text.get_width()/2), HEIGHT/2 - game_over_text.get_height()/2))
            pygame.display.update()
            death_t -= 1
            if death_t == 0:
                pygame.quit()
        else:
            game_over_text = FONT.render("Draw", True, (200, 200, 200))
            screen.fill((0,0,0))
            screen.blit(game_over_text, (WIDTH/2 - (game_over_text.get_width()/2), HEIGHT/2 - game_over_text.get_height()/2))
            pygame.display.update()
            death_t -= 1
            if death_t == 0:
                pygame.quit()

#checks if any bombs have to explode
def update_bombs(bombs):
    for b in bombs:
        b.update()
        if b.timer < 1:
            b.explode(map)
            explosions[:] = b.get_sectors()
            check = b.marker
            bombs.remove(b)
            if(check == 1):
                player.bomb_limit+= 1
            else:
                player2.bomb_limit+= 1

#updates the game state
def update_map():
    #screen.fill(WHITE)
    for y in range(len(map)):
        for x in range(len(map[y])):
            if (map[x][y] == 1):
                screen.blit(wall, (x*tile_size, y*tile_size))
            if (map[x][y] == 0):
                screen.blit(ground, (x*tile_size, y*tile_size))
            if (map[x][y] == 2):
                screen.blit(stone, (x*tile_size, y*tile_size))
            if (map[x][y] == 3):
                screen.blit(hero, (x*tile_size, y*tile_size))
            if (map[x][y] == 4):
                screen.blit(hero2, (x*tile_size, y*tile_size))
            if (map[x][y] == 5):
                screen.blit(enemy_ghost, (x*tile_size, y*tile_size))
            if (map[x][y] == 6):
                screen.blit(enemy_circle, (x*tile_size, y*tile_size))
            if (map[x][y] == 7):
                screen.blit(bomb_range, (x*tile_size, y*tile_size))
            if (map[x][y] == 8):
                screen.blit(bomb_number, (x*tile_size, y*tile_size))
    for b in bombs:
        screen.blit(bomb_p, (b.x_plant*tile_size, b.y_plant*tile_size))
    for ex in explosions:
        screen.blit(explosion_p, (ex[0]*tile_size, ex[1]*tile_size))

        if (map[ex[0]][ex[1]] == 5 or map[ex[0]][ex[1]] == 6):
            map[ex[0]][ex[1]] = bonus.get_bonus()
        else:
            map[ex[0]][ex[1]] = 0

#checks if any player has died
def check_death_player(player,map):
    if map[player.x][player.y] == 0:
        player.alive = False

#checks if any enemy has died
def check_death_enemy(enemy,map):
    if map[enemy.x][enemy.y] == 0 or map[enemy.x][enemy.y] == 7 or map[enemy.x][enemy.y] == 8:
        enemy.alive = False


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bomberman")

#setup
player = Player(3, 1 , 1, 1)
player2 = Player(4, 13, 13 ,2)
enemy1 = Enemy(13 , 1 , 5)
enemy2 = Enemy(1 , 13 , 6)
enemy3 = Enemy(9 , 9 , 5)
enemy4 = Enemy(5 , 5 , 6)
bonus = Bonus()
enemy_move_time = 30
bombs = []
explosions = []

pygame.key.set_repeat()

running = True
while running:
    enemy_move_time -= 1
    check_death_enemy(enemy1,map)
    check_death_enemy(enemy2,map)
    check_death_enemy(enemy3,map)
    check_death_enemy(enemy4,map)
    if enemy_move_time == 0:
        enemy_move_time = 30
        if enemy1.alive:
            enemy1.move(map,player,player2)
        if enemy2.alive:
            enemy2.move(map,player,player2)
        if enemy3.alive:
            enemy3.move(map,player,player2)
        if enemy4.alive:
            enemy4.move(map,player,player2)

        check_death_player(player, map)
        check_death_player(player2, map)

        if (player.alive == False and player2.alive == False):
            game_over(2)
        elif (player.alive == False):
            game_over(0)
        elif (player2.alive == False):
            game_over(1)
    # Handle events
    for event in pygame.event.get():

        if player.alive:
            if event.type == pygame.KEYDOWN:
                if(event.key == pygame.K_s):
                    player.move(0 , 1 , map)
                elif(event.key == pygame.K_w):
                    player.move(0 , -1 , map)
                elif(event.key == pygame.K_a):
                    player.move(-1 , 0 , map)
                elif(event.key == pygame.K_d):
                    player.move(1 , 0 , map)
                elif(event.key == pygame.K_q):
                    if(player.bomb_limit > 0):
                        player.bomb_limit-= 1
                        bombs.append(player.plant_bomb())
        
        if player2.alive:
            if event.type == pygame.KEYDOWN:
                if(event.key == pygame.K_DOWN):
                    player2.move(0 , 1 , map)
                elif(event.key == pygame.K_UP):
                    player2.move(0 , -1 , map)
                elif(event.key == pygame.K_LEFT):
                    player2.move(-1 , 0 , map)
                elif(event.key == pygame.K_RIGHT):
                    player2.move(1 , 0 , map)
                elif(event.key == pygame.K_SPACE ):
                    if(player2.bomb_limit > 0):
                        player2.bomb_limit-= 1
                        bombs.append(player2.plant_bomb())
            
        if event.type == pygame.QUIT:
            running = False

    update_bombs(bombs)
    update_map()
    explosions.clear()
    pygame.display.update()


pygame.quit()
