import random
def attack_result():
    result_of_attack = random.choice([\
        'CH','FH','FH','DB','BM','M','GB','AH','AH','SH','SH','SH','SH','CH Hit','CH','CH','CH','DB',\
            'DB','DB','DB','FH','FH','FH','FH','SH','SH','KB'])

    if result_of_attack == 'BM':
        descriptor = 'Big Miss'
        damage_factor = -0.25
    elif result_of_attack == 'M':
        descriptor = 'Miss'
        damage_factor = 0
    elif result_of_attack == 'GB':
        descriptor = 'Glancing Blow'
        damage_factor = 0.2
    elif result_of_attack == 'AH':
        descriptor = 'Average Hit'
        damage_factor = 0.5
    elif result_of_attack == 'SH':
        descriptor = 'Solid Hit'
        damage_factor = 0.75
    elif result_of_attack == 'CH':
        descriptor = 'Critical Hit'
        damage_factor = 1.0
    elif result_of_attack == 'DB':
        descriptor = 'Devastating Blow'
        damage_factor = 1.5
    elif result_of_attack == 'FH':
        descriptor = 'Fatal Hit'
        damage_factor = 2.5
    else:
        descriptor = 'Death Shot'
        damage_factor = 4.0
    print('\a')
    print(f'\033[1;31;43m Result of attack is.....{descriptor} \033[0;0m')    
    return damage_factor