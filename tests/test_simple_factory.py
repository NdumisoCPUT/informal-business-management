import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from creational_patterns.simple_factory import PromotionalMessageFactory

def test_factory_creates_whatsapp_message():
    msg = PromotionalMessageFactory.create_message("whatsapp")
    assert msg.channel == "WhatsApp"
    assert "delivery" in msg.content.lower()

def test_factory_raises_for_invalid_type():
    try:
        PromotionalMessageFactory.create_message("telegram")
    except ValueError as e:
        assert str(e) == "Unknown message type"
