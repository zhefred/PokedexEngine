from desmume.emulator import DeSmuME
#from desmume.controls import DeSmuME

emu = DeSmuME()
emu.open("C:/Users/frede/Downloads/desmume-win-x64/Roms/Pokemon Platinum Version (US)(XenoPhobia)/3541 - Pokemon Platinum Version (US)(XenoPhobia).nds")

# Create the window for the emulator
window = emu.create_sdl_window()

# Run the emulation as fast as possible until quit
while not window.has_quit():
    window.process_input()   # Controls are the default DeSmuME controls, see below.
    emu.cycle()
    window.draw()

