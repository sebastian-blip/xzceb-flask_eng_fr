"""Modulo que traduce texto"""

from deep_translator import MyMemoryTranslator


def english_french(english_text: str) -> str:
    """Función que traduce de ingles a frances

    Args:
        english_test: Texto en ingles
    
    Retunrs:
        Texto traducido a frances

    """
    instance = MyMemoryTranslator(source='en-GB', target='fr-FR')
    french_text = instance.translate(english_text)
    return french_text


def french_english(french_text: str) -> str:
    """Función que traduce de frances a ingles

    Args:
        french_text: Texto en frances
    
    Retunrs:
        Texto traducido a ingles

    """
    instance = MyMemoryTranslator(source='fr-FR', target='en-GB')
    english_text = instance.translate(french_text)
    return english_text
