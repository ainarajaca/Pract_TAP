import mcpi.minecraft as minecraft
import time
import random

class OracleBot:
    def __init__(self):
        self.mc = minecraft.Minecraft.create()
        self.respuestas = [
            "Sí, sin duda alguna.",
            "No cuentes con ello.",
            "Tal vez, inténtalo de nuevo más tarde.",
            "Definitivamente sí.",
            "Parece poco probable.",
            "Las señales apuntan a que sí.",
            "No puedo predecirlo ahora.",
            "Pregunta de nuevo y veré qué puedo hacer.",
            "La respuesta está en tu corazón.",
            "No estoy seguro, pero suena interesante."
        ]
        self.mc.postToChat("OracleBot activado. Escribe 'oráculo' seguido de tu pregunta para recibir una respuesta.")
    
    def responder_pregunta(self):
        respuesta = random.choice(self.respuestas)
        self.mc.postToChat(respuesta)
    
    def escuchar_chat(self):
        while True:
            events = self.mc.events.pollChatPosts()
            for event in events:
                if event.message.lower().startswith("oráculo"):
                    self.responder_pregunta()
                elif event.message.lower() == "salir":
                    self.mc.postToChat("El oráculo descansa por ahora...")
                    return

if __name__ == "__main__":
    bot = OracleBot()
    bot.escuchar_chat()
