from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    # passa com a implementação correta da classe Ingredient
    instance = Ingredient("farinha")
    assert instance.name == "farinha"
    assert instance.restrictions == {Restriction.GLUTEN}
    # falha caso o atributo restrictions de um ingrediente
    # não contenha os valores corretos para o alimento passado.
    instance = Ingredient("farinha")
    assert instance.name == "farinha"
    assert instance.restrictions != {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }
    # falha caso o atributo name de um ingrediente
    # seja diferente que o passado ao construtor.
    instance = Ingredient("bacon")
    assert instance.name != "farinha"
    assert instance.restrictions == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
    }
    # falha caso a implementação do método __repr__
    # retorne um valor inadequado.
    instance = Ingredient("farinha")
    assert repr(instance) == "Ingredient('farinha')"
    # falha caso a comparação de igualdade de dois
    # ingredientes diferentes seja verdadeira
    ingredient1 = Ingredient("farinha")
    ingredient2 = Ingredient("bacon")
    assert ingredient1 != ingredient2
    # falha caso a comparação de igualdade de dois
    # ingredientes iguais (ou de um ingrediente com ele mesmo) seja falsa
    ingredient1 = Ingredient("farinha")
    ingredient2 = Ingredient("farinha")
    assert ingredient1 == ingredient2
    # falha caso a classe retorne hashes iguais
    # para dois ingredientes diferentes
    ingredient1 = Ingredient("farinha")
    ingredient2 = Ingredient("bacon")
    assert hash(ingredient1) != hash(ingredient2)
    # falha caso a classe retorne hashes diferentes
    # para dois ingredientes iguais
    ingredient1 = Ingredient("farinha")
    ingredient2 = Ingredient("farinha")
    assert hash(ingredient1) == hash(ingredient2)
