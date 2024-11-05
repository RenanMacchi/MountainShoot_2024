#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT
from code.EnemyShot import EnemyShot
from code.Entity import Entity




class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.vertical_speed = 1  # Velocidade vertical inicial para o Enemy3


    def move(self):
        if self.name == 'Enemy3':
            # Movimento horizontal (direita para esquerda)
            self.rect.centerx -= ENTITY_SPEED[self.name]
           
            # Movimento vertical oscilante
            self.rect.centery += self.vertical_speed
           
            # Muda a direção ao atingir a borda superior ou inferior
            if self.rect.top <= 0:
                self.vertical_speed = abs(self.vertical_speed) * 2  # Desce com o dobro da velocidade
            elif self.rect.bottom >= WIN_HEIGHT:
                self.vertical_speed = -abs(self.vertical_speed)  # Sobe com velocidade normal
        else:
            # Movimento padrão para Enemy1 e Enemy2
            self.rect.centerx -= ENTITY_SPEED[self.name]


    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
