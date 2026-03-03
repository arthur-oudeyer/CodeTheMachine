# ------------- level -------------- #
LEVEL = 6
# ---------------------------------- #

# ------------ Objectif ------------ #
# Mettre en place un pilote suffisament efficace pour récuperer les points dans le temps imparti !.
# ---------------------------------- #

import CodeTheMachine_ao.controller as controller
from CodeTheMachine_ao.controller import Vector, config

machine = controller.LoadMachine(machine_type="drone")

# Défini la fonction de controle du drone :
def drone_control_function(m: controller.machine.Drone) -> None:
    keyboard_inputs = controller.get_keyboard_inputs()
    if keyboard_inputs["R"]:  # Reset simulation
        controller.reset()

    # ----- Complète le programme ----- #

    # 1.
    # Si aucune touche n'est appuyé -> on égalise les puissance moteurs (stop rotation)
    moyenne_moteurs = 0 # COMPLETE : calcul de la puissance moyenne des moteurs (m.getRightPower() ...)
    m.setRightPower(moyenne_moteurs)
    m.setLeftPower(moyenne_moteurs)

    # 2. Pilotage Vertical
    neutral_thrust = 0  # COMPLETE : Puissance qui permet au drone de se "maintenir' en l'air (proche de 20)
    # Flèche du haut
    if keyboard_inputs['UP']:
        pass # COMPLETE : Remplace par m.setRightPower(...) / m.setLeftPower(...) ...
    # Flèche du bas
    elif keyboard_inputs['DOWN']:
        pass  # COMPLETE : Remplace par m.setRightPower(...) / m.setLeftPower(...) ...
    else: # Sinon on mets les 2 moteurs à puissance neutre
        m.setLeftPower(neutral_thrust)
        m.setRightPower(neutral_thrust)

    # 3. Pilotage Horizontale
    turn_power = 5
    # Flèche de droite -> on augmente le moteur gauche et diminue le moteur droit
    if keyboard_inputs['RIGHT']:
        pass # COMPLETE : remplace et complète
    # Flèche de gauche -> pareil qu'à droite mais en inversé
    elif keyboard_inputs['LEFT']:
        pass  # COMPLETE : remplace et complète
    else: # On stabilise selon l'angle d'inclinaison
        # Si on penche de 5° à droite, on veut 'tourner' le drone vers la gauche, donc augmenter le moteur droit
        # et diminuer le moteur gauche. (par exemple de 5% chacun..)
        # utiles :
        # m.getAngleRelativeToVertical() -> angle en degrèes du drone par rapport à l'axe vertical
        # m.increaseRightPower(...), m.increaseLeftPower(...)
        pass # COMPLETE : remplace et complète

    # Stabilisation Globale
    # Si on penche trop (angle seuil à définir) -> on force une stabilisation
    angle_threshold = 90 # COMPLETE : angle seuil à régler (au delà on veut forcer une stabilisation)
    if m.getAngleRelativeToVertical() > angle_threshold:
        # Si on penche trop à droite, on va forcer une rotation vers la gauche (utilise m.increaseRightPower() et m.increaseLeftPower())
        pass  # COMPLETE : remplace et complète
    elif False : # COMPLETE : condition opposé
        pass # COMPLETE : remplace et complète

    return


machine.set_update_function(drone_control_function)
controller.StartSimulation(LEVEL)
