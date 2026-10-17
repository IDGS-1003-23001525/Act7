import pytest
from tienda import calcular_precio, calcular_iva
def calcular_precio(precio,descuento):
    total= precio - (precio*descuento/100)
    return total

def calcular_iva(precio):
    return calcular_iva(100,10) == 90

def test_calcular_iva():
    assert calcular_iva(100) == pytest.approx(116.0)
    
def test_calcular_sin_descuento():
    assert calcular_precio(500,0)

def test_descuento_invalido():
    with pytest.raises(ValueError):
        calcular_precio(100,150)