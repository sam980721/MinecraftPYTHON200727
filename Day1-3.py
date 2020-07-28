# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 14:11:07 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()

X=103
Y=102
Z=101
mc.player.setTilePos(X,Y,Z)