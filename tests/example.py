# -*- coding: utf-8 -*-

import datetime

from openfisca_core import model
import openfisca_france
openfisca_france.init_country()
from openfisca_core.simulations import ScenarioSimulation


def case_study (year = 2013) :
#simulation est une classe , Scenariosimulation  est une instance, on a instancier "simulation"
#on a mainteant fait simulation.set_congif pour modifier les attributs. on lui a dit de prendre l'année 2013
#avec year=year. reforme = true. Nmen est le nombre de ménage. Maxrev est le salaire imposable de la première personne déclaré.
# Ici tu prends que deux menage et on fait varier les salaires. Simulation.set.param est la legislation par défaut.

    simulation = ScenarioSimulation()
    simulation.set_config(year = year,
                          nmen = 2,
                          maxrev = 10000,
                          x_axis= 'sali')

    simulation.set_param()
    df = simulation.get_results_dataframe()
    print df.to_string()
  
#Projet ménange enfant : Arbitrage entre garder l'enfant pour avoir le quotient familial ou perdre la demi part
# en donnant une pension. 2 fonctions à tester : un ménage avec un enfant et un sans enfants.
#pour rajouter des personnes simulation.scenario.add
#Dans openfisca-france data.py variables de d'entré et model.py variables de sortie

def menage_avec_enfant(year = 2013):
    simulation = ScenarioSimulation()
    simulation.set_config(year = year,
                          nmen = 1)    
    simulation.scenario.addIndiv(1, datetime.date(1975,1,1), 'conj','part')
    simulation.scenario.addIndiv(2, datetime.date(1990,1,1), 'pac', 'enf')
    
    print simulation.scenario
    print simulation.scenario.indiv[0]
    
    simulation.scenario.indiv[0]['sali'] = 30000
    
    
    simulation.set_param()
    df = simulation.get_results_dataframe()
    print df.to_string()
    
def menage_sans_enfant(year = 2013):
    simulation = ScenarioSimulation()
    simulation.set_config(year = year,
                          nmen = 10,
                          maxrev = 100000,
                          x_axis= 'sali')
    print simulation.scenario
    
    
    simulation.scenario.addIndiv(1, datetime.date(1975,1,1), 'conj','part')
    
def menage_enfant_seulement(year = 2013):
    simulation = ScenarioSimulation()
    simulation.set_config(year = year,
                          nmen = 10,
                          maxrev = 0,
                          x_axis= 'sali')
    print simulation.scenario
    
    
    

if __name__ == '__main__' :
    menage_avec_enfant()
    
    