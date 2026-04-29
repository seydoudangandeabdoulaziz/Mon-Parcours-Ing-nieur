"""Functions for calculating steps in exchanging currency.

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""

def exchange_money(budget, exchange_rate):
    """
    :param budget: float - montant que vous prévoyez d'échanger.
    :param exchange_rate: float - valeur unitaire de la devise étrangère.
    :return: float - valeur échangée dans la devise étrangère.
    """
    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """
    :param budget: float - montant total possédé.
    :param exchanging_value: float - montant que vous voulez échanger.
    :return: float - montant restant dans votre devise locale.
    """
    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """
    :param denomination: int - la valeur d'un billet (ex: billet de 20).
    :param number_of_bills: int - nombre total de billets.
    :return: int - valeur totale des billets.
    """
    return denomination * number_of_bills


def get_number_of_bills(amount, denomination):
    """
    :param amount: float - la valeur totale à convertir en billets.
    :param denomination: int - la valeur d'un seul billet.
    :return: int - nombre de billets complets que l'on peut obtenir.
    """
    return int(amount // denomination)


def get_leftover_of_bills(amount, denomination):
    """
    :param amount: float - la valeur totale.
    :param denomination: int - la valeur d'un seul billet.
    :return: float - le reste (monnaie) après avoir fait le maximum de billets.
    """
    return amount % denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    :param budget: float - montant à échanger.
    :param exchange_rate: float - taux de change standard.
    :param spread: int - pourcentage de frais (ex: 10 pour 10%).
    :param denomination: int - la valeur d'un seul billet.
    :return: int - valeur maximale échangeable en billets entiers.
    """
    # 1. Calculer le taux de change réel (taux + frais)
    actual_rate = exchange_rate * (1 + (spread / 100))
    
    # 2. Calculer le montant total en devise étrangère
    total_foreign_currency = budget / actual_rate
    
    # 3. Calculer combien de billets entiers on peut avoir
    number_of_bills = total_foreign_currency // denomination
    
    # 4. Retourner la valeur totale de ces billets (en entier)
    return int(number_of_bills * denomination)