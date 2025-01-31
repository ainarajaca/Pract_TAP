import mcpi.minecraft as minecraft
import mcpi.block as block
import time

class TNTBot:
    def __init__(self):
        self.mc = minecraft.Minecraft.create()
        self.mc.postToChat("TNTBot activado. Escribe 'boom' en el chat para explotar TNT.")
    
    def colocar_tnt(self, x, y, z):
        self.mc.setBlock(x, y, z, block.TNT.id, 1)  # 1 para que se active
    
    def escuchar_chat(self):
        while True:
            events = self.mc.events.pollChatPosts()
            for event in events:
                if event.message.lower() == "boom":
                    pos = self.mc.player.getTilePos()
                    self.colocar_tnt(pos.x + 1, pos.y, pos.z)
                    self.mc.postToChat("¡TNT colocada y lista para explotar!")
                elif event.message.lower() == "salir":
                    self.mc.postToChat("¡Nos vemos, explosivo aventurero!")
                    return

if __name__ == "__main__":
    bot = TNTBot()
    bot.escuchar_chat()
