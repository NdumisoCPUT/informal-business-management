import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from creational_patterns.singleton import SystemSettingsManager

def test_singleton_consistency():
    s1 = SystemSettingsManager()
    s1.set("timezone", "SAST")

    s2 = SystemSettingsManager()
    assert s2.get("timezone") == "SAST"
    assert s1 is s2
