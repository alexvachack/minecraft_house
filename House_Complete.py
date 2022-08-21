from mcpi.minecraft import Minecraft
from mcpi import block

# Conéctate a Minecraft
mc = Minecraft.create()

# Determinar la posición actual del jugador.
x,y,z = mc.player.getTilePos()

width = 5
height = 3
depth = 6

# Crea un caparazón hueco hecho de ladrillos.
mc.setBlocks(x, y, z+3, x+width, y+height, z+3+depth, block.BRICK_BLOCK.id)
mc.setBlocks(x+1, y, z+4, x+width-1, y+height-1, z+2+depth, block.AIR.id)

# Establecer el suelo.
mc.setBlocks(x-1, y-1, z+2, x+1+width, y-1, z+4+depth, block.COBBLESTONE.id)

# Agregar una puerta.
mc.setBlock(x+1, y, z+3, block.DOOR_WOOD.id, 0)
mc.setBlock(x+1, y+1, z+3, block.DOOR_WOOD.id, 8)

# Agregar ventanas.
mc.setBlocks(x+3, y+1, z+3, x+4, y+2, z+3, block.GLASS.id)
mc.setBlocks(x+2, y+1, z+3+depth, x+3, y+2, z+3+depth, block.GLASS.id)
mc.setBlocks(x, y+1, z+5, x, y+2, z+7, block.GLASS.id)
mc.setBlocks(x+width, y+1, z+5, x+width, y+2, z+7, block.GLASS.id)

# Agregue un techo.
for i in range(int(width/2) + 1):
    mc.setBlocks(x+i, y+height+i, z+3, x+i, y+height+i, z+3+depth, block.STAIRS_WOOD.id, 0)
    mc.setBlocks(x+width-i, y+height+i, z+3, x+width-i, y+height+i, z+3+depth, block.STAIRS_WOOD.id, 1)
    # Extremos del hastial.
    if (int(width/2) - i > 0):
        mc.setBlocks(x+1+i, y+height+i, z+3, x+width-i-1, y+height+i, z+3, block.BRICK_BLOCK.id, 0)
        mc.setBlocks(x+1+i, y+height+i, z+3+depth, x+width-i-1, y+height+i, z+3+depth, block.BRICK_BLOCK.id, 1)
        
