import pygame
import sys
import random
pygame.init()

#game window proportions
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400

#colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

#coin proportions
COIN_RADIUS = 20

#player proportions
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 30

#creating a game window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Coin Collector")

#clock rate
clock = pygame.time.Clock()

#coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((COIN_RADIUS * 2, COIN_RADIUS * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, YELLOW, (COIN_RADIUS, COIN_RADIUS), COIN_RADIUS)
        self.rect = self.image.get_rect(center=(random.randint(0, WINDOW_WIDTH), 0))

    def update(self):
        #moving coin down to 5 pixels
        self.rect.y += 5

        #colliding with down wall of window
        if self.rect.y > WINDOW_HEIGHT:
            self.kill()  #deleting the coin if it collides

#player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT), pygame.SRCALPHA)
        pygame.draw.rect(self.image, (0, 128, 255), (0, 0, PLAYER_WIDTH, PLAYER_HEIGHT))
        self.rect = self.image.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT - 50))

    def update(self):
        #moving the player rectangle
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.right < WINDOW_WIDTH:
            self.rect.x += 5

#groups
all_sprites = pygame.sprite.Group()
coins = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

#coin counter
collected_coins = 0

#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #creating random coins
    if random.randint(0, 100) < 5:
        coin = Coin()
        all_sprites.add(coin)
        coins.add(coin)

    all_sprites.update()

    #check the colliding between player and coin
    collisions = pygame.sprite.spritecollide(player, coins, True)
    for coin in collisions:
        collected_coins += 1

    #draw everything
    window.fill(WHITE)
    all_sprites.draw(window)

    #showing coin counter
    font = pygame.font.Font(None, 36)
    text = font.render(f"Coins: {collected_coins}", True, (0, 0, 0))
    window.blit(text, (WINDOW_WIDTH - 150, 10))

    pygame.display.flip()
    clock.tick(60)
