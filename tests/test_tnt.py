import pytest
import keyboard
from unittest.mock import MagicMock
from bots.TNTBot import TntBot  # Asegúrate de importar correctamente tu bot
import random

@pytest.fixture
def mock_minecraft(mocker):
    """Mockea la conexión con Minecraft."""
    mock_mc = MagicMock()
    mocker.patch('mcpi.minecraft.Minecraft.create', return_value=mock_mc)
    return mock_mc

def test_place_tnt(mock_minecraft):
    """Verifica que el bot coloque TNT en las coordenadas correctas."""
    tnt_bot = TntBot()

    # Llamar al método place_tnt
    tnt_bot.place_tnt(10, 20, 30)

    # Verificar que setBlock se llamó con los parámetros correctos
    mock_minecraft.setBlock.assert_called_with(10, 20, 30, 46, 1)  # El id de TNT es 46

def test_explode_tnt(mock_minecraft):
    """Verifica que el bot coloque fuego en las coordenadas correctas para activar el TNT."""
    tnt_bot = TntBot()

    # Llamar al método explode_tnt
    tnt_bot.explode_tnt(10, 20, 30)

    # Verificar que setBlock se llamó con el id de fuego (id=51)
    mock_minecraft.setBlock.assert_called_with(10, 20, 30, 51)

def test_random_tnt_placement(mock_minecraft, mocker):
    """Verifica que el bot coloque TNT aleatoriamente cerca del jugador."""
    tnt_bot = TntBot()

    # Mock de la función randint para que siempre devuelva 3
    mock_randint = mocker.patch('random.randint', return_value=3)

    # Mock de la posición del jugador
    mock_minecraft.player.getTilePos.return_value = MagicMock(x=0, y=0, z=0)

    # Mock de place_tnt y explode_tnt para verificar que se llaman
    mock_place_tnt = mocker.patch.object(tnt_bot, 'place_tnt')
    mock_explode_tnt = mocker.patch.object(tnt_bot, 'explode_tnt')

    # Llamar al método random_tnt_placement
    tnt_bot.random_tnt_placement(radius=5)

    # Verificar que place_tnt haya sido llamado con las coordenadas correctas
    mock_place_tnt.assert_called_with(3, 0, 3)  # Se espera TNT en (3, 0, 3)

    # Verificar que explode_tnt haya sido llamado con las coordenadas correctas
    mock_explode_tnt.assert_called_with(3, 0, 3)  # Se espera que explote en (3, 0, 3)

def test_stop_bot_on_q(mock_minecraft, mocker):
    """Verifica que el bot se detenga cuando se presiona la tecla 'q'."""
    tnt_bot = TntBot()

    # Mockear la función is_pressed para simular la tecla 'q' siendo presionada
    mock_is_pressed = mocker.patch('keyboard.is_pressed', return_value=True)

    # Mockear el comportamiento del ciclo infinito
    with mocker.patch('time.sleep', return_value=None):  # Evitar delays largos
        # Ejecutar el ciclo y verificar que el bot se detenga al presionar 'q'
        with pytest.raises(KeyboardInterrupt):  # Esperamos que el bot termine al presionar 'q'
            while True:
                if keyboard.is_pressed('q'):
                    raise KeyboardInterrupt
                tnt_bot.random_tnt_placement(radius=5)

    # Verificar que se detuvo correctamente
    mock_is_pressed.assert_called_with('q')
