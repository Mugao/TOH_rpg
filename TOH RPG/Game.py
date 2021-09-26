import pygame


WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

#Azura

class stats:
    def set_stats(self, base_atk, base_defe, base_sp_atk, base_sp_defe, base_spe, base_hp, lvl):
        atk = 2 * base_atk * lvl // 100 + lvl + 10
        defe = 2 * base_defe * lvl // 100 + lvl + 10
        sp_atk = 2 * base_sp_atk * lvl // 100 + lvl + 10
        sp_defe = 2 * base_sp_defe * lvl // 100 + lvl + 10
        spe = 2 * base_spe * lvl // 100 + lvl + 10
        hp = 2 * base_hp * lvl // 100 + lvl + 10




def main_battle(): 
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
    
    
    
if __name__ == "__main__":
    main_battle()  
