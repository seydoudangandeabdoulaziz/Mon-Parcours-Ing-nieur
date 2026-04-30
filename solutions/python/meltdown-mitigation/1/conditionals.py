def is_criticality_balanced(temperature, neutrons_emitted):
    # On vérifie les 3 conditions simultanément
    # On utilise "return" pour renvoyer le résultat (booléen)
    return (temperature < 800 and 
            neutrons_emitted > 500 and 
            (temperature * neutrons_emitted) < 500000)


def reactor_efficiency(voltage, current, theoretical_max_power):
    # 1. Calcul de la puissance générée
    generated_power = voltage * current
    # 2. Calcul du pourcentage d'efficacité
    efficiency = (generated_power / theoretical_max_power) * 100

    # 3. Logique de décision (du plus haut vers le plus bas)
    if efficiency >= 80:
        return 'green'
    elif efficiency >= 60: # Signifie entre 60 et 79.99
        return 'orange'
    elif efficiency >= 30: # Signifie entre 30 et 59.99
        return 'red'
    else:
        return 'black'


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    # 1. Calcul de la valeur critique
    valeur_actuelle = temperature * neutrons_produced_per_second
    
    # 2. Définition des zones (90% et 110% pour le +/- 10%)
    if valeur_actuelle < (0.9 * threshold):
        return 'LOW'
    elif (0.9 * threshold) <= valeur_actuelle <= (1.1 * threshold):
        return 'NORMAL'
    else:
        return 'DANGER'