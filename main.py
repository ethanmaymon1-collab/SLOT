import pygame
import random
import sys
import os

# --- SETTINGS ---
WIDTH, HEIGHT = 800, 600
FPS = 60
GLITCH_GREEN = (0, 255, 65)
BLACK = (10, 10, 10)
WHITE = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SOAKEDVERSE: THE HOUSE NEVER WINS")
clock = pygame.time.Clock()
font = pygame.font.SysFont("monospace", 24, bold=True)

# --- LOAD ASSETS FROM FOLDER ---
def load_symbol(name, color):
    path = os.path.join("assets", f"{name.lower()}.jpg")
    if os.path.exists(path):
        img = pygame.image.load(path)
        return pygame.transform.scale(img, (150, 150))
    else:
        # Fallback if image is missing
        surf = pygame.Surface((150, 150))
        surf.fill(color)
        return surf

SYM_DATA = {
    "SOAKED": (0, 0, 255),
    "WESPURYY": (50, 50, 50),
    "TRYSTONS": (255, 0, 0),
    "PAMELI": (200, 200, 200),
    "CHEATMAXXER": (255, 100, 0)
}

SYMBOLS = {name: load_symbol(name, color) for name, color in SYM_DATA.items()}
SYM_LIST = list(SYMBOLS.keys())

class SlotMachine:
    def __init__(self):
        self.reels = [random.choice(SYM_LIST) for _ in range(3)]
        self.spinning = False
        self.spin_timer = 0
        self.balance = 1000
        self.last_win = 0

    def spin(self):
        if not self.spinning and self.balance >= 10:
            self.spinning = True
            self.spin_timer = 30
            self.balance -= 10
            self.last_win = 0

    def update(self):
        if self.spinning:
            self.spin_timer -= 1
            self.reels = [random.choice(SYM_LIST) for _ in range(3)]
            if self.spin_timer <= 0:
                self.spinning = False
                if self.reels[0] == self.reels[1] == self.reels[2]:
                    self.last_win = 100
                    self.balance += self.last_win

    def draw(self):
        screen.fill(BLACK)
        # Glitch background
        for _ in range(15):
            x, y = random.randint(0, WIDTH), random.randint(0, HEIGHT)
            g_text = font.render(random.choice(["0","1","ERR"]), True, (0, 80, 0))
            screen.blit(g_text, (x, y))

        # Reel Frame
        pygame.draw.rect(screen, GLITCH_GREEN, (100, 150, 600, 220), 4)
        
        for i, name in enumerate(self.reels):
            screen.blit(SYMBOLS[name], (130 + i*200, 185))
            
        # HUD
        screen.blit(font.render(f"CREDITS: ${self.balance}", True, GLITCH_GREEN), (20, 20))
        screen.blit(font.render("SPACE TO SPIN", True, WHITE), (WIDTH//2 - 100, 500))
        if self.last_win > 0:
            screen.blit(font.render("SYSTEM BREACH! WIN!", True, (255,255,0)), (WIDTH//2 - 150, 100))

# --- MAIN LOOP ---
game = SlotMachine()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game.spin()
    
    game.update()
    game.draw()
    pygame.display.flip()
    clock.tick(FPS)
