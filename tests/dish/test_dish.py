from src.models.dish import Dish, Recipe  # noqa: F401, E261, E501
from src.models.ingredient import (
    Ingredient,
    Restriction,
)

import pytest


# Req 2
def test_dish():
    # passa com a implementação correta da classe Dish
    instance = Dish("macarrão", 35.00)
    assert instance.name == "macarrão"
    assert instance.price == 35.00
    instance.add_ingredient_dependency(Ingredient("farinha"), 1)
    assert instance.get_ingredients() == {Ingredient("farinha")}

    # falha caso o método get_ingredients retorne
    # um set de ingredientes diferente do esperado;
    instance = Dish("macarrão", 35.00)
    ingredients = instance.get_ingredients()
    assert ingredients != {"bacon"}
    # falha caso o método get_restrictions retorne
    # um set de restrições diferente do esperado
    instance = Dish("macarrão", 35.00)
    instance.add_ingredient_dependency(Ingredient("farinha"), 1)
    restrictions = instance.get_restrictions()
    assert restrictions == {Restriction.GLUTEN}
    # falha caso o acesso a um valor do atributo recipe,
    # ao ser indexado com um ingrediente válido retorne uma
    # quantidade inválida (dica: use o método get do dicionário,
    # por exemplo dish.recipe.get(ingredient));

    # teste falha caso um ValueError não seja
    # levantado ao criar um prato com um valor inválido;
    with pytest.raises(ValueError):
        Dish("macarrão", -35)
    #  falha caso um TypeError não seja levantado ao
    # criar um prato com um valor de tipo inválido;
    with pytest.raises(TypeError):
        Dish("macarrão", "35")
    # falha caso a implementação do método __repr__
    # retorne um valor inadequado;
    instance = Dish("macarrão", 35.00)
    assert repr(instance) == "Dish('macarrão', R$35.00)"
    # falha caso a comparação de igualdade de
    # dois pratos diferentes seja verdadeira;
    dish1 = Dish("macarrão", 35.00)
    dish2 = Dish("risoto", 45.00)
    assert dish1 != dish2
    # falha caso a comparação de igualdade
    # de dois pratos iguais (ou de um prato com ele mesmo) seja falsa;
    dish1 = Dish("macarrão", 35.00)
    dish2 = Dish("macarrão", 35.00)
    assert dish1 == dish2
    # teste falha caso os hashes de dois pratos diferentes sejam iguais
    dish1 = Dish("macarrão", 35.00)
    dish2 = Dish("risoto", 45.00)
    assert hash(dish1) != hash(dish2)
    # falha caso os hashes de dois pratos iguais sejam diferentes;
    dish1 = Dish("macarrão", 35.00)
    dish2 = Dish("macarrão", 35.00)
    assert hash(dish1) == hash(dish2)
    # falha caso o atributo name de um
    # prato seja diferente que o passado ao construtor.
    instance = Dish("macarrão", 35.00)
    assert instance.name != "risoto"
