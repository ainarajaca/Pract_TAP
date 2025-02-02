import mcpi.minecraft as mc
import mcpi.block as blocks
import time
import random

from bots.botBase import BlockAssistant

class TntBot(BlockAssistant):
    def __init__(self):
        super().__init__()
        # Conectar a Minecraft
        self.mc = mc.Minecraft.create()

    def place_tnt(self, x, y, z):
        """Coloca un bloque de TNT en las coordenadas especificadas."""
        self.mc.setBlock(x, y, z, blocks.TNT.id, 1)

    def explode_tnt(self, x, y, z):
        """Coloca fuego para activar el TNT y esperar la explosión."""
        self.mc.setBlock(x, y, z, blocks.FIRE.id)

    def random_tnt_placement(self, radius=5):
        """Coloca TNT aleatoriamente cerca del jugador y lo explota."""
        pos = self.mc.player.getTilePos()
        tnt_x = pos.x + random.randint(-radius, radius)
        tnt_y = pos.y
        tnt_z = pos.z + random.randint(-radius, radius)

        print(f"Colocando TNT en: ({tnt_x}, {tnt_y}, {tnt_z})")
        self.place_tnt(tnt_x, tnt_y, tnt_z)
        time.sleep(2)
        self.explode_tnt(tnt_x, tnt_y, tnt_z)

if __name__ == "__main__":
    tnt_bot = TntBot()
    try:
        while True:
            tnt_bot.random_tnt_placement(radius=10)
            time.sleep(5)
    except KeyboardInterrupt:
        print("Bot detenido manualmente.")
