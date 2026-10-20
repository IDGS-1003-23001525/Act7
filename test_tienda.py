import pytest
from tienda import calcular_precio, calcular_iva, validar_descuento

def test_calcular_iva():
    assert calcular_iva(100) == pytest.approx(999.0) #Valor intencionalmente incorrecto
    
def test_calcular_sin_descuento():
    assert calcular_precio(500, 0) == 500

def test_descuento_invalido():
    with pytest.raises(ValueError):
        validar_descuento(150)