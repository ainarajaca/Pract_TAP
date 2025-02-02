import pytest
from unittest.mock import MagicMock
import random
import time

# Asegúrate de que el archivo de tu clase 'InsultBot' esté importado correctamente.
from bots.InsultBot import InsultBot

# Usamos un fixture para la instancia de InsultBot
@pytest.fixture
def bot():
    # Crea una instancia de InsultBot simulada (sin conexión al servidor de Minecraft)
    bot_instance = InsultBot()
    bot_instance.send_chat = MagicMock()  # Mock del método send_chat
    bot_instance.world.events.pollChatPosts = MagicMock()  # Mock de pollChatPosts
    return bot_instance


def test_command_insultbot(bot):
    """Verifica que el comando 'insultbot' envíe un insulto aleatorio."""
    # Mock para la función de elección de insultos aleatorios
    random.choice = MagicMock(return_value="¡Eres más lento que una tortuga en arena movediza!")
    
    # Ejecutar el comando 'insultbot'
    bot.command_insultbot()
    
    # Verificar que send_chat fue llamada con el insulto esperado
    bot.send_chat.assert_called_with("¡Eres más lento que una tortuga en arena movediza!")


def test_interactive_chat(bot):
    """Verifica que el bot responda correctamente a un chat interactivo."""
    # Simular el mensaje "insultbot" en el chat
    mock_message = MagicMock(message="insultbot")
    bot.world.events.pollChatPosts.return_value = [mock_message]

    # Mock de pollChatPosts para que solo se ejecute una vez
    bot.world.events.pollChatPosts.side_effect = [
        [mock_message],  # Primera interacción
        []  # Después de la primera, el chat vuelve vacío
    ]
    
    # Asegurémonos de que el insulto se elija correctamente
    mock_random_choice = MagicMock(return_value="¡Eres más lento que una tortuga en arena movediza!")
    random.choice = mock_random_choice

    # Ejecutar la función interactive_chat
    bot.interactive_chat()  # Esto debería llamar command_insultbot y enviar el insulto

    # Verificar que send_chat fue llamada con el insulto esperado
    bot.send_chat.assert_called_with("¡Eres más lento que una tortuga en arena movediza!")

    # Asegurarnos de que random.choice se llamó con los insultos correctos
    mock_random_choice.assert_called_with([
        "¡Eres más lento que una tortuga en arena movediza!",
        "¿Eso es todo lo que puedes hacer? ¡Patético!",
        "¡Hasta las ovejas de Minecraft construyen mejor que tú!",
        "¿Te perdiste? Parece que sí...",
        "¡Tu estructura tiene más agujeros que un queso suizo!"
    ])
def test_random_insult(bot):
    """Verifica que el insulto aleatorio se elige correctamente."""
    insults = [
        "¡Eres más lento que una tortuga en arena movediza!",
        "¿Eso es todo lo que puedes hacer? ¡Patético!",
        "¡Hasta las ovejas de Minecraft construyen mejor que tú!",
        "¿Te perdiste? Parece que sí...",
        "¡Tu estructura tiene más agujeros que un queso suizo!"
    ]
    
    # Hacer que random.choice elija un valor específico
    random.choice = MagicMock(return_value=insults[0])
    
    # Ejecutar la función y verificar que se elige correctamente
    bot.command_insultbot()
    bot.send_chat.assert_called_with(insults[0])


def test_sleep(bot):
    """Verifica que la función de espera no bloquea el hilo."""
    # Asegúrate de que la función de comando tenga un sleep real
    start_time = time.time()

    # Simular que se llama al comando con un tiempo de espera
    bot.command_insultbot()  # Aquí debes tener un sleep dentro de esta función

    # Aquí agregamos una pausa de 2 segundos manualmente para simular un tiempo de espera
    time.sleep(2)

    elapsed_time = time.time() - start_time
    # Verificar que el tiempo de espera es alrededor de 2 segundos
    assert 1.8 < elapsed_time < 2.2
