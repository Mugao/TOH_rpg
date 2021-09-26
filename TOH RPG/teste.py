
#cada heroi tera um base stats.
# Cada base stats está dividido em:
    # Ataque
    # Defesa
    # Ataque especial
    # Defesa Especial
    # Velocidade
    # hp
# O personagem Azura vai ter 100 em todos - balanceado - personagem teste 
# para definir os stats atuais, aplicar a formula: 2 * base * level // 100 + lvl + 10
# Dano = ((2*self_lvl//5+2) * move_power * self_atk//inimigo_defe)//50 + 2
# cada personagem possui 4 movimentos que variam de classe a classe 
# Movimentos Azura:
#   -Now eat this, sucker!
#       power=100 Acurancy=90% Type=special
#       Sem efeito secundario
#   -Thorn Vault.
#       power=120 acurancy=80% Type=phsical
#       Se errar o ataque, Azura perda 25% da vida
#   -Be friend!
#       power=0 acurancy=100% type=status
#       diminui ambos ataques de todos os adversarios por 50%
#   - 


from ataques import Ataque
from dataclasses import dataclass
import json
from settings import *
import random

class Charcter:
    
    def __init__(self, nome, base_atk, base_defe, base_sp_atk, base_sp_defe, base_spe, base_hp, lvl):
        self.nome = nome
        self.base_atk = base_atk
        self.base_defe = base_defe
        self.base_sp_atk = base_sp_atk
        self.base_sp_defe = base_sp_defe
        self.base_spe = base_spe
        self.base_hp = base_hp
        self.lvl = lvl
        self.definir_ataques()
        self.set_stats()
    
    def set_stats(self):
        self.atk = 2 * self.base_atk * self.lvl // 100 + self.lvl + 10
        self.defe = 2 * self.base_defe * self.lvl // 100 + self.lvl + 10
        self.sp_atk = 2 * self.base_sp_atk * self.lvl // 100 + self.lvl + 10
        self.sp_defe = 2 * self.base_sp_defe * self.lvl // 100 + self.lvl + 10
        self.spe = 2 * self.base_spe * self.lvl // 100 + self.lvl + 10
        self.hp = 2 * self.base_hp * self.lvl // 100 + self.lvl + 10
         
        
    def level_up(self):
        self.lvl += 1
        self.set_stats()
        
    def calc_dmg(self, nome_ataque, inimigo):
        ataque: Ataque = self.ataques.get(nome_ataque)
        chance = random.randint(1, 100) 
        if chance > ataque.accuracy:
            return 'errou'    
        elif ataque.type == 'phsical': 
            damage = ((2*self.lvl//5+2) * ataque.power * self.atk//inimigo.defe)//50 + 2
            return damage
        else: 
            damage = ((2*self.lvl//5+2) * ataque.power * self.sp_atk//inimigo.sp_defe)//50 + 2
            return damage

        
        
    def definir_ataques(self):
        self.ataques = {}
        for ataque in ATAQUES.get(self.nome):
            self.ataques[ataque] = Ataque(**ATAQUES[self.nome][ataque])


    


if __name__ == "__main__":
    azura = Charcter('azura',100,100,100,100,100,100,100)
    print(azura.ataques['atk_1'].power)
    print(azura.atk)
    azura.level_up()
    print(azura.atk)
    gilder_snake = Charcter('gilder_snake',70,70,70,70,70,70,70)
    print(gilder_snake.atk)
    print(azura.atk)
    print(gilder_snake.hp)
    print(azura.calc_dmg('atk_1', gilder_snake))
