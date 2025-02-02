import mcpi.minecraft as mc
import mcpi.block as blocks
import time

class BlockAssistant:
    def __init__(self):
        # Establecer conexión con Minecraft
        self.world = mc.Minecraft.create()
        print("Conectado a Minecraft con éxito.")

    def send_chat(self, msg):
        # Enviar un mensaje al chat del juego
        self.world.postToChat(msg)

    def place_structure(self, x, y, z, material):
        # Poner un bloque en la ubicación especificada
        self.world.setBlock(x, y, z, material)

    def remove_block(self, x, y, z):
        # Eliminar un bloque colocando aire en su lugar
        self.world.setBlock(x, y, z, blocks.AIR.id)

    def fetch_position(self):
        # Obtener la posición del jugador
        return self.world.player.getTilePos()

    def teleport(self, x_offset, y_offset, z_offset):
        # Mover al jugador con valores relativos
        current_pos = self.fetch_position()
        self.world.player.setTilePos(current_pos.x + x_offset, current_pos.y + y_offset, current_pos.z + z_offset)

    def build_corridor(self, start_point, length=5, height=3):
        # Construir un pasillo de bloques
        x, y, z = start_point.x, start_point.y, start_point.z
        for step in range(length):
            for level in range(height):
                self.place_structure(x + step, y + level, z - 1, blocks.STONE.id)
                self.place_structure(x + step, y + level, z + 1, blocks.STONE.id)
            self.place_structure(x + step, y + height, z, blocks.STONE.id)
            self.place_structure(x + step, y - 1, z, blocks.STONE.id)
        self.send_chat(f"Pasillo de {length} bloques construido.")

    def process_command(self, cmd, *params):
        # Manejar comandos dinámicamente
        try:
            action = getattr(self, f"cmd_{cmd}")
            action(*params)
        except AttributeError:
            self.send_chat(f"Comando desconocido: '{cmd}'")
        except Exception as err:
            self.send_chat(f"Error ejecutando '{cmd}': {err}")

    def cmd_construir(self):
        pos = self.fetch_position()
        self.build_corridor(pos)

    def cmd_mover(self, dx, dy, dz):
        self.teleport(int(dx), int(dy), int(dz))
        self.send_chat(f"Desplazado a {dx}, {dy}, {dz}.")

    def cmd_eliminar(self):
        pos = self.fetch_position()
        self.remove_block(pos.x + 1, pos.y, pos.z)
        self.send_chat("Bloque eliminado enfrente de ti.")

    def cmd_salir(self):
        self.send_chat("Saliendo, hasta la próxima!")
        raise StopIteration

    def chat_listener(self):
        # Leer el chat y responder a comandos
        self.send_chat("Usa 'construir', 'mover dx dy dz' o 'eliminar'.")
        while True:
            try:
                chat_msgs = self.world.events.pollChatPosts()
                for msg in chat_msgs:
                    parts = msg.message.lower().split()
                    command = parts[0]
                    args = parts[1:]
                    self.process_command(command, *args)
            except StopIteration:
                break

if __name__ == "__main__":
    assistant = BlockAssistant()
    assistant.send_chat("Hola, listo para ayudar en Minecraft!")
    time.sleep(2)
    assistant.chat_listener()
