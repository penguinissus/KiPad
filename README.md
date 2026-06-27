# KiPad
A macropad built for the most common KiCAD shortcuts. 
![Zine](assets/KiPad-Zine-V2.png)

# User Instructions
Assembly: 
1. Print out and buy all the parts found in `BOM.csv`
2. Solder everything together
3. Put in the keycaps accordingly (refer to `3d-models/full-assembly.step` or pictures below)
4. Sandwich PCB between the top and the bottom case

Firmware: 
1. go to circuitpython.org/downloads
2. download circuitpython for XIAO RP2040
3. plug in keyboard to laptop and make sure to use a data transmitting cable
4. open up the pico folder in your computer's directory
5. replace the contents of `code.py` in the XIAO RP2040 folder with the one in this repo

# Why did I make it
I wanted to make the process of designing on KiCAD easier, so I made this macropad for this problem. 

# Diagrams
Schematic:  
![schematic](assets/schematic.png)  
PCB Editor:  
![pcb-editor](assets/pcb-editor.png)  
PCB Assembly:  
![pcb-assembly](assets/pcb.png)  
Full Assembly:  
![full-assembly](assets/full-assembly.png)

# BOM