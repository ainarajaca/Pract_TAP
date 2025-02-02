import mcpi.minecraft as minecraft
import mcpi.block as block
import random
import time
import threading
from typing import Callable, Any

# Clase base para todos los asistentes
class Asistente:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.mc = minecraft.Minecraft.create()

    def enviar_mensaje(self, mensaje: str):
        self.mc.postToChat(f"[{self.nombre}] {mensaje}")

    def obtener_posicion(self):
        return self.mc.player.getTilePos()

    def colocar_bloque(self, x: int, y: int, z: int, id_bloque: int):
        self.mc.setBlock(x, y, z, id_bloque)

    def obtener_bloque(self, x: int, y: int, z: int):
        return self.mc.getBlock(x, y, z)

# OráculoBot: Responde con respuestas aún más genéricas y filosóficas
class OraculoBot(Asistente):
    def __init__(self, nombre: str):
        super().__init__(nombre)
        # Respuestas más genéricas y filosóficas
        self.respuestas_genericas = [
            "A veces, las respuestas están dentro de ti.",
            "El universo tiene una forma misteriosa de mostrarte lo que necesitas saber.",
            "Todo pasa por una razón, incluso si no la entiendes ahora.",
            "Al final, todo es solo un momento en el tiempo.",
            "¿Quién necesita respuestas cuando tienes curiosidad?",
            "Lo que buscas podría estar más cerca de lo que piensas.",
            "El silencio es tan poderoso como las palabras.",
            "A veces, el camino no tiene una respuesta clara, solo sigue caminando.",
            "¿Quién sabe qué traerá mañana?",
            "La vida no tiene manual de instrucciones, solo experiencias."
        ]
        # Imprimir mensaje cuando el bot se conecta
        self.enviar_mensaje("OraculoBot a su disposición")

    def responder_pregunta(self, pregunta: str):
        """Responder con una frase aleatoria de la lista de respuestas genéricas."""
        respuesta = random.choice(self.respuestas_genericas)
        self.enviar_mensaje(f"Q: {pregunta} | A: {respuesta}")

    def escuchar_preguntas(self):
        ultimo_chat = ""
        while True:
            eventos_chat = self.mc.events.pollChatPosts()
            for evento in eventos_chat:
                if evento.message != ultimo_chat:  # Evitar respuestas repetidas
                    ultimo_chat = evento.message
                    self.responder_pregunta(ultimo_chat)

# Función principal demostrando los bots, se ejecuta de manera continua
def principal():
    oraculo_bot = OraculoBot("OraculoBot")
    # Ejecutar OraculoBot en un hilo separado para escuchar preguntas
    threading.Thread(target=oraculo_bot.escuchar_preguntas, daemon=True).start()

    while True:
        # Demostrar cada bot periódicamente
        time.sleep(2)  # Esperar antes de detonar

if __name__ == "__main__":
    principal()
