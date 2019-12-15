# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 18:05:35 2019

@author: RickP
"""
import cx_Freeze

executables = [cx_Freeze.Executable('Santa1.py')]

cx_Freeze.setup(
        name="Santa's Dungeon Escape",
        options={"build_exe": {"packages":["pygame", "PIL"],"include_files":["leveldata.py","imageConversionTool.py","Media\\Graphics\\background.png","Media\\Graphics\\background2.jpg","Media\\Graphics\\background3.png","Media\\Graphics\\background4.jpg","Media\\Graphics\\brick.jpg","Media\\Graphics\\brickz.png","Media\\Graphics\\ground.png","Media\\Graphics\\ground2.png","Media\\Graphics\\mario.jpg","Media\\Graphics\\SANTA.jpg","Media\\Graphics\\SANTA.png","Media\\Graphics\\SANTA2.png","Media//Graphics//SANTAFLIP.jpg","Media\\Graphics\\SANTAFLIP.png","Media\\Graphics\\SANTAFLIP2.png","Media\\Graphics\\SnowPlat.jpg","Media\\Graphics\\SnowPlat2.jpg","Media\\Graphics\\spikes.png","Media\\Graphics\\spikez.png","Media\\Graphics\\walls.png","Media\\Graphics\\walls2.png","Media\\Music\\Buffalo.mp3","Media\\Music\\DownUnder.mp3","Media\\Music\\Dreaming.mp3","Media\\Music\\HorseNoName.mp3","Media\\Sounds\\effect_collide.wav","Media\\Sounds\\effect_death.wav","Media\\Sounds\\effect_jump.wav","Media\\Sounds\\effect_level.wav","Media\\Sounds\\effect_run.wav","Media\\Sounds\\effect_start_reverse.wav","Media\\Sounds\\effect_start.wav","Media\\Sounds\\effect_walk.wav"]}},
        
        executables = executables
        
        
        )


