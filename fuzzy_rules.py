import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define fuzzy inputs and outputs
calories = ctrl.Antecedent(np.arange(0, 1001, 1), 'calories')
protein = ctrl.Antecedent(np.arange(0, 51, 1), 'protein')
fat = ctrl.Antecedent(np.arange(0, 51, 1), 'fat')
suitability = ctrl.Consequent(np.arange(0, 101, 1), 'suitability')

# Membership functions
calories['low'] = fuzz.trimf(calories.universe, [0, 0, 400])
calories['medium'] = fuzz.trimf(calories.universe, [300, 500, 700])
calories['high'] = fuzz.trimf(calories.universe, [600, 1000, 1000])

protein['low'] = fuzz.trimf(protein.universe, [0, 0, 10])
protein['medium'] = fuzz.trimf(protein.universe, [8, 20, 30])
protein['high'] = fuzz.trimf(protein.universe, [25, 50, 50])

fat['low'] = fuzz.trimf(fat.universe, [0, 0, 10])
fat['medium'] = fuzz.trimf(fat.universe, [8, 20, 30])
fat['high'] = fuzz.trimf(fat.universe, [25, 50, 50])

suitability['low'] = fuzz.trimf(suitability.universe, [0, 0, 40])
suitability['medium'] = fuzz.trimf(suitability.universe, [30, 50, 70])
suitability['high'] = fuzz.trimf(suitability.universe, [60, 100, 100])

# Fuzzy rules
rule1 = ctrl.Rule(calories['low'] & protein['high'] & fat['low'], suitability['high'])
rule2 = ctrl.Rule(calories['medium'] & protein['medium'] & fat['medium'], suitability['medium'])
rule3 = ctrl.Rule(calories['high'] & fat['high'], suitability['low'])
rule4 = ctrl.Rule(protein['low'] & fat['high'], suitability['low'])
rule5 = ctrl.Rule(protein['high'] & fat['medium'], suitability['high'])

# Control system
suitability_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
suitability_simulator = ctrl.ControlSystemSimulation(suitability_ctrl)

# Function to calculate suitability
def fuzzy_suitability(calories_value, protein_value, fat_value, goal):
    suitability_simulator.input['calories'] = calories_value
    suitability_simulator.input['protein'] = protein_value
    suitability_simulator.input['fat'] = fat_value
    suitability_simulator.compute()
    return suitability_simulator.output['suitability']
