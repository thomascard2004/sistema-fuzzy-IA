'''
Pergunta: O que implica na boa montação de uma Drag Queen"
 "Qualidade da Peruca: "
 "Qualidade da Maquiagem: "
 "Qualidade da Roupa: "
 "Qualidade da Performance: "
 "Nível de Carisma: "

 '''
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

#criando as variáveis do problema
qualiperuca = ctrl.Antecedent(np.arange(0, 101, 1), 'Peruca')
qualimake = ctrl.Antecedent(np.arange(0, 101, 1), 'Maquiagem')
qualiroupa = ctrl.Antecedent(np.arange(0, 101, 1), 'Roupa')
qualiperform = ctrl.Antecedent(np.arange(0, 101, 1), 'Performance')
qualicharisma = ctrl.Antecedent(np.arange(0, 101, 1), 'Carisma')

ganhaconcurso = ctrl.Consequent(np.arange(0, 101, 1), 'Chance de ganhar o concurso:')

#criando as funções de pertinência para a peruca:
qualiperuca['sintética'] = fuzz.trapmf(qualiperuca.universe, [0, 0, 30, 40])
qualiperuca['orgânica'] = fuzz.gaussmf(qualiperuca.universe, 55, 15)
qualiperuca['lace'] = fuzz.trapmf(qualiperuca.universe, [65, 70, 100, 100])

#criando as funções de pertinência para a maquiagem:
qualimake['virginia'] = fuzz.trapmf(qualimake.universe, [0, 0, 30, 40])
qualimake['karenbachinni'] = fuzz.gaussmf(qualimake.universe, 55, 15)
qualimake['bocarosa'] = fuzz.trapmf(qualimake.universe, [65, 70, 100, 100])

#criando as funções de pertinência para a roupa:
qualiroupa['renner'] = fuzz.trapmf(qualiroupa.universe, [0, 0, 30, 40])
qualiroupa['riachuelo'] = fuzz.gaussmf(qualiroupa.universe, 55, 15)
qualiroupa['gucci'] = fuzz.trapmf(qualiroupa.universe, [65, 70, 100, 100])

#criando as funções de pertinência para a performance:
qualiperform['kimchi'] = fuzz.trapmf(qualiperform.universe, [0, 0, 10, 15])
qualiperform['valentina'] = fuzz.gaussmf(qualiperform.universe, 65, 15)
qualiperform['anetra'] = fuzz.trapmf(qualiperform.universe, [80, 95, 100, 100])

#criando as funções de pertinência para carisma:
qualicharisma['insuportável'] = fuzz.trapmf(qualicharisma.universe, [0, 0, 30, 40])
qualicharisma['legal'] = fuzz.gaussmf(qualicharisma.universe, 55, 15)
qualicharisma['carismática'] = fuzz.trapmf(qualicharisma.universe, [65, 70, 100, 100])


#criando as funções de pertinência para "chande de vencer o concurso":
ganhaconcurso['baixíssima'] = fuzz.trapmf(ganhaconcurso.universe, [0, 0, 5, 30])
ganhaconcurso['média'] = fuzz.trimf(ganhaconcurso.universe, [10, 30, 85])
ganhaconcurso['alta'] = fuzz.trapmf(ganhaconcurso.universe, [60, 90, 100, 100])



# Visualizando as funções de pertinência para cada variável
qualiperuca.view()
qualimake.view()
qualiroupa.view()
qualiperform.view()
qualicharisma.view()

ganhaconcurso.view()




# Base de Conhecimento/Regras
rule1 = ctrl.Rule(qualiperuca['lace'] & qualimake['bocarosa'] & qualiroupa['gucci'] & qualiperform['anetra'] & qualicharisma['carismática'], ganhaconcurso['alta'])
rule2 = ctrl.Rule(qualiperuca['orgânica'] & qualimake['karenbachinni'] & qualiroupa['riachuelo'] & qualiperform['valentina'] & qualicharisma['legal'], ganhaconcurso['média'])
rule3 = ctrl.Rule(qualiperuca['sintética'] & qualimake['virginia'] & qualiroupa['renner'] & qualiperform['kimchi'] & qualicharisma['insuportável'], ganhaconcurso['baixíssima'])

# Sistema Fuzzy e Simulação
ganhaconcurso_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
ganhaconcurso_simulador = ctrl.ControlSystemSimulation(ganhaconcurso_ctrl)


while True:
    make = int(input('Digite a qualidade da make [de 0 à 100]: '))
    if(make < 0 or make > 100):
        print('A qualidade da maquiagem deve estar no intervalo [0, 100]')
        continue
    
    ganhaconcurso_simulador.input['Maquiagem'] = make
    break

while True:
    peruca = int(input('Digite a qualidade da peruca [de 0 à 100]: '))
    if(peruca < 0 or peruca > 100):
        print('A qualidade da peruca deve estar no intervalo [0, 100]')
        continue
    
    ganhaconcurso_simulador.input['Peruca'] = peruca
    break

while True:
    roupa = int(input('Digite a qualidade da roupa [de 0 à 100]: '))
    if(roupa < 0 or roupa > 100):
        print('A qualidade da roupa deve estar no intervalo [0, 100]')
        continue

    ganhaconcurso_simulador.input['Roupa'] = roupa
    break

while True:
    perform = int(input('Digite a qualidade da perfomance [de 0 à 100]: '))
    if(perform < 0 or perform > 100):
        print('A qualidade da performance deve estar no intervalo [0, 100]')
        continue
    
    ganhaconcurso_simulador.input['Performance'] = perform
    break

while True:
    carisma = int(input('Digite a quantidade de carisma [de 0 à 100]: '))
    if(carisma < 0 or carisma > 100):
        print('A quantidade de carisma deve estar no intervalo [0, 100]')
        continue

    ganhaconcurso_simulador.input['Carisma'] = carisma
    break


ganhaconcurso_simulador.compute()
print('A chance dessa queen ganhar é de: ', (round(ganhaconcurso_simulador.output['Chance de ganhar o concurso:'])))


qualiperuca.view(sim=ganhaconcurso_simulador)
qualimake.view(sim=ganhaconcurso_simulador)
qualiroupa.view(sim=ganhaconcurso_simulador)
qualiperform.view(sim=ganhaconcurso_simulador)
qualicharisma.view(sim=ganhaconcurso_simulador)

ganhaconcurso.view(sim=ganhaconcurso_simulador)

input()