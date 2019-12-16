# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 18:05:35 2019

@author: RickP
"""
import cx_Freeze

executables = [cx_Freeze.Executable('Santa1.py')]

cx_Freeze.setup(
        name="Santa's Dungeon Escape",
        options={"build_exe": {"packages":["pygame", "PIL"],"include_files":["Media\\","readme.txt","leveldata.py"]}},
        
        executables = executables
        
        
        )


