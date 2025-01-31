import random
from mcpi.minecraft import Minecraft

def generar_insulto():
    adjetivos = ["patético", "ridículo", "lamentable", "desastroso", "torpe", "insufrible", "inepto", "desagradable", "absurdo", "mediocre"]
    sustantivos = ["inútil", "bocachancla", "zoquete", "cenutrio", "mendrugo", "pelmazo", "zopenco", "berzotas", "mastuerzo", "tarado"]
    return f"Eres un {random.choice(adjetivos)} {random.choice(sustantivos)}."

def insultbot():
    mc = Minecraft.create()
    print("InsultBot 3000 activado en Minecraft. Escribe 'insulta' en el chat para recibir un insulto.")
    while True:
        events = mc.events.pollChatPosts()
        for event in events:
            if event.message.lower() == "insulta":
                insulto = generar_insulto()
                mc.postToChat(insulto)
            elif event.message.lower() == "salir":
                mc.postToChat("¡Vuelve pronto, zoquete!")
                return

if __name__ == "__main__":
    insultbot()
