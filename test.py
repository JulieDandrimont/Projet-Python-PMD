

#EXEMPLE COMMENT STOCKER LES DONNES
#reflexion sur le dic des objets

Player = {
    "name" :"input",
    "life" : 10,
    #"strength": ne pas encore defini,
    #defense : ne pas encore defini,
    "Inventory" : { "objects" : [],
                   "potion" : []},
    "Attacks" : {
        "push": ["dommage","hit"],
        "love_dance": ["dommage","hit"],
    }
    }
Drunk_crowd = {
    "name" : ["Corto","Geoffrey","Fadil","Lysianna","Florine"],
    "life" : 8,
    #"strength": ne pas encore defini,
    #defense : ne pas encore defini,
    "Attacks" : {
        "sweaty_contact": ["dommage","hit"],
        "step_on_the_feet": ["dommage","hit"]
    },
    "dropped_object" : ["cashless_bracelet","beer"],
    }
Security = {
    "name" : "Breit from security",
    "life" : 20,
    #"strength": ne pas encore defini,
    #defense : ne pas encore defini,
    "Attacks" : {
        "death_stare": ["dommage","hit"],
        "body_search": ["dommage","hit"],
        "teargas": ["dommage","hit"],
    },
    }


Map = {
      "B1" : {
          "room_name" :"entrance",
          "coordinates":(2,1),
          "object" : True, #objet eventail et consignes
          "possible_box_directions":["A1","C1","quit"],
          "print_possible_answers" :["right","crowd","quit"],
          "direction_print" : "",
          "fight" : False,
      },
      "A1" : {
          "room_name" :"secret_room_1",
          "coordinates":(1,1),
          "object" : True, #objet biere
          "possible_box_directions":["B1","quit"],
          "print_possible_answers" : ["right","quit"],
          "direction_print" : "",
          "fight" : False,
          },
      "C1" : {
          "room_name" :"crowd_1",
          "coordinates":(3,1),
          "object" : False,
          "possible_box_directions":["C2","quit"],
          "print_possible_answers" :["go further in the crowd","quit"],
          "direction_print" : "",
          "fight" : True, #objet a recuperer cashless et biere
          },
      "C2" : {
          "room_name" :"hallway_1",
          "coordinates":(3,2),
          "object" : True, #objet consignes
          "possible_box_directions":["D2","C3","quit"],
          "print_possible_answers" :["yes","no","quit"],#input == no -> C3 else D2
          "direction_print" : "Do you need a break?",
          "fight" : False,
          },
      "D2" : {
          "room_name" :"safer_zone",
          "coordinates":(4,2),
          "object" : True, #eau
          "possible_box_directions":["C2","quit"],
          "print_possible_answers" :["return to crowd","quit"],
          "direction_print" : "",
          "fight" : False,
          },
      "C3" : {
          "room_name" :"crowd_2",
          "coordinates":(3,3),
          "object" : True, #chaise decathlon
          "possible_box_directions":["B3","C4","quit"],
          "print_possible_answers" :["direction to the bar","go further in the crowd","quit"],
          "direction_print" : "",#qqn a attirer ton attention a gauche et tu vois la buvette un peu plus loin a gauche
          "fight" : False, # if randint(0,100)<30: True ,
          },
      "B3" : {
          "room_name" :"hallway_2",
          "coordinates":(2,3),
          "object" : True, #if yes to the candy
          "possible_box_directions":["A3","C3","quit"],
          "print_possible_answers" :["bar","return to the crowd","quit"],
          "direction_print" : "",
          "fight" : False,
          },
       "A3" : {
          "room_name" :"bar",
          "coordinates" : (1,3),
          "object" : True, #if casheless == ou > beer price : 15
          "possible_box_directions":["B3","quit"],
          "print_possible_answers" :["return to the crowd","quit"],
          "direction_print" : "",
          "fight" : False,
          },
      "C4" : {
          "room_name" :"hallway3",
          "coordinates" : (3,4),
          "object" : False,
          "possible_box_directions":["C5","quit"],
          "print_possible_answers" :["go further into the music","quit"],
          "direction_print" : "",#Tu entends la musique de plus en plus tu the rapproches de la mainstage
          "fight" : False,
          },
         "C5" : {
          "room_name" :"hallway4",
          "coordinates" : (3,5),
          "object" : False,
          "possible_box_directions":["B5","D5","quit"],
          "print_possible_answers" :["go to security","right","quit"],
          "direction_print" : "",#a droit secret room en allemand et a gauche les lumieres de la secu
          #rassure toi que tu as le plus d objet possible avant d avancer vers la secu
          "fight" : False,
          },
       "D5" : {
          "room_name" :"secret_room_2",
          "coordinates" : (4,5),
          "object" : True, #bonbon magique
          "possible_box_directions":["C5","quit"],
          "print_possible_answers" :["Go back to the music","quit"],
          "direction_print" : "Nur Deutsche hier. Du verstehst nichts aber du sprichst mit jemanden der nett aussieht. Nach der Unterhaltung verabschieddet er sich und gibt dir ein Geschenk",
          "fight" : False,
          },
       "B5" : {
          "room_name" :"security",
          "coordinates" : (2,5),
          "object" : False,
          "possible_box_directions":["B6","quit"],
          "print_possible_answers" :["Go main","quit"],
          "direction_print" : "Le mec de la secu t as vu et tu a l air trop suspect. Il t interroge",
          "fight" : True,
          },
      "B6" : {
          "room_name" :"main_stage",
          "coordinates" : (2,6),
          "object" : False,
          "possible_box_directions":["quit"],
          "print_possible_answers" :["quit"],
          "direction_print" : "Enfin tu es arrive a la mainstage Profite bien de ton festival",
          "fight" : True,
          },
  }


    

def stage_display(nb):
    stages= [
        
    """
    |||||||||||||||||||||||||||||||||||||||||||||||||
    |name : Paul                             objet: |
    |                                        T.verre|
    |---------------------------------    éventaille|
    |Texte:                          /              |
    |                                /       Potion:|
    |                                /      S.Bonbon|
    |                                /              |
    |                                /              |
    |                                /              |
    |                                /              |
    |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _| 
    """,
    """
    |||||||||||||||||||||||||||||||||||||||||||||||||
    |name : Paul                             objet: |
    |                                        T.verre|
    |---------------------------------    éventaille|
    |Texte:                          /              |
    |                                /       Potion:|
    |                                /      S.Bonbon|
    |                                /              |
    |                                /              |
    |                                /              |
    |                                /              |
    |---------------------------------              |
    |  Maps:                         /              |
    |                                /              |
    |    +---+---+---+---+---+       /              |
    |    | E | C | @ | ? | ? |       /              |
    |    |---|---|---|---|---|       /              |
    |    | ? | ? | ? | ? | ? |       /              |
    |    |---|---|---|---|---|       /              |
    |    | ? | ? | ? | ? | ? |       /              |
    |    |---|---|---|---|---|       /              |
    |    | ? | ? | ? | ? | ? |       /              |
    |    |---|---|---|---|---|       /              |
    |    | ? | ? | ? | ? | ? |       /              |
    |    +---+---+---+---+---+       /              |
    |                                /              |
    |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _| 
    """,
    """
    |||||||||||||||||||||||||||||||||||||||||
    |                 Fight                 |
    |                                       |
    |     Name               Name           |
    |                                       |
    |    Stat                Stat           |
    |    pv:                 pv:            |
    |    def:                def:           |
    |    att:                att:           |
    |    obj:                obj:           |
    |    pt:                 pt:            |
    |---------------------------------------|
    |Texte:                                 |
    |                                       |
    |                                       |
    |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _| 
    """,
    """
    Maps:
    r: room
    sr:  secret room
    c: corridor
    sc: secret corridor
    fr: finish room
    +---+---+---+---+---+
    | - | - | @ | - | sr|
    |---|---|---|---|---|
    | r | c | r | c | r |
    |---|---|---|---|---|
    | c | - | - | - | - |
    |---|---|---|---|---|
    | c | - | - | - | sr|
    |---|---|---|---|---|
    | c | c | c | sc| sc|
    |---|---|---|---|---|
    | sr| - | r | - | - |
    |---|---|---|---|---|
    | - | - | fr| - | - |
    +---+---+---+---+---+ 
    """
    ]
    print(stages[4 - nb])
    
stage_display(1)

