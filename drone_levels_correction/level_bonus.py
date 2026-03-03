# ------------- level -------------- #
LEVEL = 6
# ---------------------------------- #

# ------------ Objectif ------------ #
# Mettre en place un asservissement suffisament efficace pour suivre correctement le point et attraper tout les points.
# ---------------------------------- #

import CodeTheMachine_ao.controller as controller
from CodeTheMachine_ao.controller import Vector, config
machine = controller.LoadMachine(machine_type="drone")

# Défini la fonction de controle du drone :
def drone_control_function(m: controller.machine.Drone) -> None:

    keyboard_inputs = controller.get_keyboard_inputs()

    if keyboard_inputs["R"]: # Reset simulation
        controller.reset()

    # Si aucune touche n'est appuyé -> on égalise les puissance moteurs (stop rotation)
    moyenne_moteurs = (m.getLeftPower() + m.getRightPower()) / 2
    m.setRightPower(moyenne_moteurs)
    m.setLeftPower(moyenne_moteurs)

    neutral_thrust = 19.7 # Puissance qui permet au drone de se "maintenir' en l'air
    # Flèche du haut
    if keyboard_inputs['UP']:
        m.setLeftPower(neutral_thrust * 1.5)
        m.setRightPower(neutral_thrust * 1.5)
    # Flèche du bas
    elif keyboard_inputs['DOWN']:
        m.setLeftPower(neutral_thrust * 0.5)
        m.setRightPower(neutral_thrust * 0.5)
    else:
        m.setLeftPower(neutral_thrust)
        m.setRightPower(neutral_thrust)

    turn_power = 5
    # Flèche de droite -> on augmente le moteur gauche et diminue le moteur droit
    if keyboard_inputs['RIGHT']:
        m.increaseRightPower(-turn_power)
        m.increaseLeftPower(turn_power)
    # Flèche de gauche -> pareil qu'à droite mais en inversé
    elif keyboard_inputs['LEFT']:
        m.increaseRightPower(turn_power)
        m.increaseLeftPower(-turn_power)
    else: # On stabilise selon l'angle d'inclinaison
        m.increaseRightPower(m.getAngleRelativeToVertical())
        m.increaseLeftPower(-1 * m.getAngleRelativeToVertical())

    # Si on penche trop -> on force une stabilisation
    angle_threshold = 15
    if m.getAngleRelativeToVertical() > angle_threshold:
        m.increaseRightPower(2 * turn_power)
        m.increaseLeftPower(-2 * turn_power)
    elif m.getAngleRelativeToVertical() < -angle_threshold:
        m.increaseRightPower(-2 * turn_power)
        m.increaseLeftPower(2 * turn_power)

    return

machine.set_update_function(drone_control_function)
controller.StartSimulation(LEVEL)
