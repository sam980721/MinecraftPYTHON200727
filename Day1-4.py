# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 14:33:06 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time

x,y,z=mc.player.getTilePos()

mc.player.setTilePos(x,y,z)
time.sleep(5)
y=y+50
mc.player.setTilePos(x,y,z)
time.sleep(5)
y=y+50
