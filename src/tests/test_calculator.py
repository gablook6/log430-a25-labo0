"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

from calculator import Calculator

my_calculator = Calculator()

def test_app():
    assert my_calculator.get_hello_message() == "== Calculatrice v1.0 =="

# TODO: ajoutez les tests

# Test Fonction Addition
def test_addition():
    assert my_calculator.addition(2, 3) == 5

# Test Fonction Soustraction
def test_subtraction():
    assert my_calculator.subtraction(20, 10) == 10

# Test Fonction Multiplication
def test_multiplication():
    assert my_calculator.multiplication(6, 4) == 24

# Test Fonction Division    
def test_division():
    assert my_calculator.division(100, 4) == 25
    
def test_division_error():
    assert my_calculator.division(12,0) == "Erreur : division par zéro"


# Ce test est mit en commentaire pour eviter l'erreur provoquer.   
# def test_provoque_erreur():
#     assert my_calculator.division(12,0) == "Provoque Erreur"