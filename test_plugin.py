# tests/test_plugin.py

from meu_plugin import hello

def test_hello():
    assert hello() == "Hello from meu_plugin!"
