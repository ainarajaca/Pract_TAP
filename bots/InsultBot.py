import mcpi.minecraft as mc
import mcpi.block as blocks
import time
import random
from bots.botBase import BlockAssistant


class InsultBot(BlockAssistant):
    
    def command_insultbot(self):
        # Lista de frases provocadoras
        insults = [
            "¡Eres más lento que una tortuga en arena movediza!",
            "¿Eso es todo lo que puedes hacer? ¡Patético!",
            "¡Hasta las ovejas de Minecraft construyen mejor que tú!",
            "¿Te perdiste? Parece que sí...",
            "¡Tu estructura tiene más agujeros que un queso suizo!",
        ]
        # Seleccionar un insulto aleatorio
        insult = random.choice(insults)
        self.send_chat(insult)

    def interactive_chat(self):
        # Leer el chat y responder a comandos
        self.send_chat("Escribe 'insultbot' para recibir un insulto.")
        while True:
            try:
                chat_msgs = self.world.events.pollChatPosts()
                for msg in chat_msgs:
                    if msg.message.lower() == "insultbot":
                        self.command_insultbot()
            except StopIteration:
                break

if __name__ == "__main__":
    bot = InsultBot()
    bot.send_chat("Hola, soy InsultBot. Estoy listo.")
    time.sleep(2)
    bot.interactive_chat()