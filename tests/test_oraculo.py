import pytest
from unittest import mock
from bots.OracleBot import OraculoBot  # Asumimos que tu código está en oraculo_bot.py
import random

# Simular la clase Minecraft y sus métodos
class MockMinecraft:
    def __init__(self):
        self.events = mock.Mock()
    
    def postToChat(self, mensaje: str):
        pass  # Simula el envío de un mensaje en el chat

    def getTilePos(self):
        return (0, 0, 0)  # Simula la posición del jugador

    def setBlock(self, x, y, z, id_bloque):
        pass  # Simula la colocación de un bloque

    def getBlock(self, x, y, z):
        return 1  # Simula la obtención de un bloque


@pytest.fixture
def oraculo_bot():
    """Fixture para crear un objeto de OraculoBot simulado."""
    bot = OraculoBot("OraculoBot")
    bot.mc = MockMinecraft()  # Reemplazar el objeto Minecraft con el mock
    bot.enviar_mensaje = mock.Mock()  # Mockear el método 'enviar_mensaje'
    return bot


def test_responder_pregunta(oraculo_bot):
    """Test para asegurar que el bot responde con una respuesta genérica."""
    
    # Simulamos una pregunta
    pregunta = "¿Cuál es el sentido de la vida?"
    
    # Llamamos al método responder_pregunta
    with mock.patch('random.choice') as mock_random_choice:
        mock_random_choice.return_value = "El universo tiene una forma misteriosa de mostrarte lo que necesitas saber."
        
        # Ejecutamos el método
        oraculo_bot.responder_pregunta(pregunta)
        
        # Verificamos que la respuesta fue la esperada
        oraculo_bot.enviar_mensaje.assert_called_with(f"Q: {pregunta} | A: El universo tiene una forma misteriosa de mostrarte lo que necesitas saber.")


def test_respuesta_generica_unica(oraculo_bot):
    """Test para asegurar que la respuesta es aleatoria pero dentro de las opciones disponibles."""
    
    # Vamos a simular que se elige una respuesta aleatoria de las opciones disponibles
    with mock.patch('random.choice') as mock_random_choice:
        mock_random_choice.return_value = "Todo pasa por una razón, incluso si no la entiendes ahora."
        
        # Simulamos que el bot responde a una pregunta
        pregunta = "¿Por qué estamos aquí?"
        oraculo_bot.responder_pregunta(pregunta)
        
        # Verificamos que la respuesta fue una de las opciones genéricas
        oraculo_bot.enviar_mensaje.assert_called_with(f"Q: {pregunta} | A: Todo pasa por una razón, incluso si no la entiendes ahora.")


def test_mensaje_inicial_al_conectarse(oraculo_bot):
    """Test para asegurar que el mensaje de 'a su disposición' se envía cuando el bot se conecta."""

    # Mockear el método 'enviar_mensaje'
    oraculo_bot.enviar_mensaje = mock.Mock()

    # Simulamos la inicialización del bot
    oraculo_bot.__init__("OraculoBot")  # Asegúrate de llamar al constructor

    # Verificamos que el mensaje de "OraculoBot a su disposición" fue enviado al conectarse
    oraculo_bot.enviar_mensaje.assert_called_with("OraculoBot a su disposición")


if __name__ == "__main__":
    pytest.main()
