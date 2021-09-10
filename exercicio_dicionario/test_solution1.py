import pytest
from solution import primeiras_ocorrencias

# Escreva seus testes neste arquivo. Para ajudar já importamos a função.


#  Teste com parametrize misturando letras maísculas com minusculas, testando entrada de número,
#  testando entrada de listas

@pytest.mark.parametrize("palavra , dicionario",
[("palavra",{"p":0,"a":1,"l":2,"v":4,"r":5}),
 ("PaLAVra",{"P":0,"a":1,"L":2,"A":3,"V":4,"r":5}),
 ("compartimentalização",{'c': 0, 'o': 1, 'm': 2, 'p': 3, 'a': 4, 'r': 5, 't': 6, 'i': 7, 'e': 9, 'n': 10, 'l': 13, 'z': 15, 'ç': 17, 'ã': 18} ), 
 ("AaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaABBBBBBBBBBBBBbbbb122222222222222222222333000000000000000000pP",{'A': 0, 'a': 1, 'B': 56, 'b': 69, '1': 73, '2': 74, '3': 94, '0': 97, 'p': 115, 'P': 116})

 ])

def test_func(palavra,dicionario):
    if type(palavra) == str:
        assert primeiras_ocorrencias(palavra) == dicionario

#Teste com palavras Maiores
def test_palavras_maiores():
    palavra = "compartimentalização"
    assert primeiras_ocorrencias(palavra) == {'c': 0, 'o': 1, 'm': 2, 'p': 3, 'a': 4, 'r': 5, 't': 6, 'i': 7, 'e': 9, 'n': 10, 'l': 13, 'z': 15, 'ç': 17, 'ã': 
18}

def test_vazio():
    palavra = ""
    assert primeiras_ocorrencias(palavra) == {}


