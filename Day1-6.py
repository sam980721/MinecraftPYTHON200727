# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 15:50:17 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time

while True:
    x,y,z=mc.player.getTilePos()
     mc.postToChat("你的位置-x:"+str(x)+"y:"str(y)+"z:"+str(z))