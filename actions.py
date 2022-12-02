"""
Contains functions related to the actions and dialog of each room on the game board.
"""
import itertools
import random
import time
import json

from helpers import print_in_color, print_user_options, get_user_choice


# Game Opening ---------------------------------------------------------------------------------------------------------
def opening_dialogue() -> None:
    """
    Print the opening story and ascii art to stdout.

    :postcondition: prints the opening story and ascii art to stdout
    """

    opening_one = "During the Reign of Gold, the continent of Alyndelle were prosperous. The Golden Capital of \n" \
                  "Astera were at the pinnacle of its reign, their prowess told to match the power of gods. \n"

    opening_two = "However, power such as these often corrupts and the God King of Alyndelle were no different. \n" \
                  "His arrogance lead him to enslaving an angel to extract their power to truly transcend the " \
                  "realm of humanhood.\n"

    opening_three = "His greed and transgression angered the Gods leading the world into the Age of Fire.\n" \
                    "God King Thompson finally slayed the Gods but to do so he took the flame of humanity, casting \n" \
                    "the rest humanity into darkness...\n"

    print_in_color("...\n", "cyan")
    time.sleep(1)
    print_in_color(opening_one, "cyan")
    time.sleep(1)
    print_in_color(opening_two, "cyan")
    time.sleep(1)
    print_in_color(opening_three, "cyan")
    time.sleep(3)
    print_in_color(r"""
                                                                                                    
                                                      %#&&%%#*                                      
                                                 #(#(&##&                                           
                                               @(((#%(%                                             
                                             #(&%((#(                                               
                                              ((#%(@&@                                              
                                     ,********,*/**//***&                                           
                                     &*/(*(**,*,*/*///**,                                           
                                     #/**********//////**/                                          
                                     @&&/*********////***,                                          
                                     *#&%&&%##***////////*#                                         
                                     *##%/*(*,*/((%##(//(/                                          
                                     (//********/////#&(//(,                                        
                                     %%*****,*,,*#/*(***%/((&//                                     
                                     %#/*******&**,***%**,/%#                                       
                                     /((****(#(**&**%,(@%&#(%(*@(&(                                 
                                     @%%**(*#//#***#@(#(##@#((/#(#%(#((%%& (                        
                                   ((@**%*//*///&(((/%/(#(((%#((((((((#((#&&(%                      
                               %(###@#%&&%%&%&((/(&#&@#%(/%%(##((#(###(%#&&#((&                     
                             *%%##%%%@(%@@/((((((@((((&#(((#%(%##%(&#&@%@(%((#&                     
                           ,(###%##%#&#((%((((%(&&@#%%##(&&@##%#&(@&%#%(##((&%((((                  
                        @@@@##%#%&((/#/%((%&&/,,(&(%##%#%#%%%#(((%(((####&##((%((&&(&               
                           ###@#%/,,,.&%#...#,....,,&@&%#%%#&&%@%%(####(#@&@%(%%#&&#                
                  &        @((%*,,...#......#.....,*(/*#%@&&#%%%&&(((%%&#@%#%%%#@%                  
               /***/%*#.     (.,...&#.......* #@#.,,/*%&&%@%#%%###%%##%#(((#(&%%(                   
              ,,,*,,##&      &..,.##.....,((#....,,,,*%%%&@@%&@(%#%###%(((((#(&(#(                  
              %,,,,,,%/&    &(#. ##(..&(##@.....,,,,*@%&&&&%%%%@&%####((#(((%#(%##(@                
              %#*#,,,(&     @.%%////&##(%......,,,,,/@&%%##%%&&%%&&##%###(((#((@,%%%&&@             
               @//%/(/%&    @,%#/%%//(...........,,,&%%(&&%%%&&&%&&@%%%(##&&&%%%@@*%@&&&            
               #(*,&%&/,**(&&%@/(////#((@........,,((/////(((/%((#(/@@&&&&@##%%##%#%/#&             
               .&%,*#%@(%&(##&&/////%%####(#####%*,&////////(((/((/%#  &%%(((((((((##((.            
               &...@/,(((#(#%%#&(/(@@,.......,,,,,,@#(///////(/(//*.   #%##((((##%%#(/#             
             %%,.../,,##&%(%&#,,#&&%%@,,,,/,,,,,,,,(////#(//(//(/(%& @##((((((((((##(&              
             &..,..*,,,..@%#(( ,%/*@%%************%/#((///*(***/(%# @%%%(((((((/&%((.               
            #(/%/@.,,*##  @@#%%(&&,(/&%&*#/****(/*@/////////**/*/&( %#%(((#(((((%#%                 
                #/,(#(       &####(*////&@(****/////(#((((/%##@&#  @##(((((##(/&(&                  
                 .(            ,/###(@//((%///(/#@&#%#%&@&&&&%#&% @(%%###(&&&(((                    
                                #%@%%(((&&@%&&&&&&&&&&(##(@&@%/(&#/*******#((//                     
                               %%%,(@%%###%&&@&&&@@@%#(#&@(//(//,/*/*****#(@#&                      
                               @%&%@&@*#%%##&@*,@&##@&((/*&(/*(@*(/**/**//@                         
                               (*@&@%%%@%@###((###%***,,,...(#//&&(*,/*%*(                          
                                ,,,#//&&%&(#&%##(@**%&(****.,,,,(*,*#&/,                            
                              @.,.,(,,,,*&#%%%%%%**@***&(,****,,,,,/*@&                             
                               .,,&&,,@@%%#.@&##&*@**#***,@****,/**@                                
                             ...,,, ####@...,(*@#@**,**%@**/@/////&#                                
                            @%...@#%%%&,..,../,,**&%*&&**@%&%@(/% @#,                               
                            (...,.@&@*,,...,....,*,,@#&@%%%(((((  @(%                               
                           /&.../ @  ..,...*,,..&*,...%%&%%###((#(%@&                               
                           &...,,.&    ,....,/,,.........@%%#####(#@#                               
                          &...(*..    @/,...*,,........... (#%#%#&%%@(%                             
                          , @#./,&     ..,./..,,...*,,.,..%  @&%&&@##((((                           
                        @      &        #.#   #@*  . ,.# (/     @(&%%##((((.                        
                                        (.      %                  (#%###(#((&                      
                                                                     @%%###/                        
                                                                        /                          
    """, "cyan")
    print_in_color(r"""
         _______  _______ _________ _______  _          _______  _______    _______ _________ _______  _______  
        (  ____ )(  ____ \\__   __/(  ____ \( (    /|  (  ___  )(  ____ \  (  ____ \\__   __/(  ____ )(  ____  \
        | (    )|| (    \/   ) (   | (    \/|  \  ( |  | (   ) || (    \/  | (    \/   ) (   | (    )|| (    \/ 
        | (____)|| (__       | |   | |      |   \ | |  | |   | || (__      | (__       | |   | (____)|| (__     
        |     __)|  __)      | |   | | ____ | (\ \) |  | |   | ||  __)     |  __)      | |   |     __)|  __)    
        | (\ (   | (         | |   | | \_  )| | \   |  | |   | || (        | (         | |   | (\ (   | (       
        | ) \ \__| (____/\___) (___| (___) || )  \  |  | (___) || )        | )      ___) (___| ) \ \__| (____/\ 
        |/   \__/(_______/\_______/(_______)|/    )_)  (_______)|/         |/       \_______/|/   \__/(_______/ 
        """, "cyan")
    time.sleep(3)


# Game Intro -----------------------------------------------------------------------------------------------------------
def cell_description() -> None:
    """
    Print the cell description to stdout.

    :postcondition: prints the cell description to stdout
    """
    part_one = "You wake to the sound of metal against stone.\n" \
               "You lift your head from the floor and as your eyes adjust to the darkness you start to scan your " \
               "surroundings..\n"

    part_two = "You are in a small cell, metal bars straight ahead; cobblestone lines the rest of the room\n" \
               "You can feel the damp air in your breath, and hear the slow drop of water against the stone floor\n" \
               "You sense a darkness weighing in your chest and a cold breeze stroke down your spine\n" \
               "From down the hall you see a shadow as it rounds the east corner, you catch a glimpse of a metal " \
               "foot..\n"

    part_three = "The last thing you can remember is the moment the King Thompson took the flame of humanity\n" \
                 "You and the rest of the royal knights were all there..\n" \
                 "There was lightning, darkness. It blanketed the sky; low and heavy causing a sense of confusion\n" \
                 "You turn to your left to see your comrades yelling and tearing at their heads..\n" \
                 "As they glance up you see a glow of deep red, shining from the slits of their helmets\n" \
                 "You tried to scream but fear restrained your voice,\n" \
                 "And then nothing..\n"

    part_four = "As you bring yourself back to the cell, to the present, you feel your heart beat speed up, " \
                "as the feeling of entrapment sets in.. " \
                "but not for long\n" \
                "The metal door of the cell creaks open, revealing a clear stone path to the hall where the shadow " \
                "walked\n" \
                "You lift yourself to your feet from the cobblestone floor and contemplate your options\n" \
                "The curiosity twists in your gut and pulls you north..\n" \
                "You are now following the shadowy figure north down the dungeon hall...\n"

    part_five = "As you approach the end of the hall, you feel a stronger wind against your skin\n" \
                "At the end of the hall, the room opens to a small room, arched doorways to your north and east\n" \
                "Another chill propagates along your spine, as you make your choice...\n\n\n"

    part_six = "Hints:\n" \
               "- To fight the final boss, you need to beat both the sub-bosses first.\n" \
               "- We recommend to be at least level 2 and equipped with items before attemping the sub-bosses.\n" \
               "- Dying sets you back so be mindful of your HP, there are ways to heal in this game.\n" \
               "- Even though some monsters are higher level than you, there is a chance to beat them!\n"\
               "- Have fun!\n\n"

    print_in_color("**CLANK**\n", "cyan")
    time.sleep(1)
    print_in_color(part_one, "cyan")
    time.sleep(1)
    print_in_color(part_two, "cyan")
    time.sleep(1)
    print_in_color(part_three, "cyan")
    time.sleep(1)
    print_in_color(part_four, "cyan")
    time.sleep(1)
    print_in_color(part_five, "cyan")
    time.sleep(1)
    print_in_color(part_six, "purple")
    time.sleep(1)


# Spider Web -----------------------------------------------------------------------------------------------------------
def spider_web_blockade(character: dict) -> None:
    """
    Print the spider web blockade room dialog and interactions.

    :param character: a character in dictionary form
    :precondition: character must be a dictionary in the form of our game character with all proper keys
    :postcondition: prints the spider web blockage room description dialog and interactions
    """
    print_in_color("You pause once in the room. You see that all of the archways are blocked off with layers upon \n"
                   "layers of spider webs. You need some way to clear the archways before you can proceed.", "cyan")
    print_in_color("You might be able to use one of your abilities to clear the webs!\n", "cyan")

    ability_options = list(enumerate(character["abilities"], start=1))
    print_user_options(ability_options, "Ability")

    ability_used = get_user_choice(ability_options)
    while ability_used != "Fireball":
        print_in_color(f"\nI don't think {ability_used} will work here, try a different one.", "red")
        ability_used = get_user_choice(ability_options)

    print_in_color("\n\nNice work! You were able to clear out all of those webs with your Fireball!", "cyan")

    if character["level"] < 3:
        character["xp"] += 12
        print_in_color(f"\n[{character['name']} | xp: +12]", "yellow")


def empty_room(character: dict) -> bool:
    """
    Print the empty room dialog with the character name.

    :param character: a character in dictionary form
    :precondition: character must be a dictionary in the form of our game character with at least the "name" key
    :postcondition: prints the empty room dialog with the character name
    """
    print_in_color("You stop in the center of the room. It appears empty, but you hear a voice whispering..", "cyan")
    print_in_color(f"{character['name']}, keep walking if you know what's good for you!", "cyan")
    print_in_color("You hastily make your decision..", "cyan")

    return True


# Default Battles ------------------------------------------------------------------------------------------------------
def fight(character: dict, enemy: dict) -> bool:
    """
    Print dialog and receive decisions for battle mechanics.

    The character and enemy dictionaries do get modified during execution.

    :param character: a character in dictionary form
    :param enemy: an enemy in dictionary form
    :precondition: character must be a dictionary in the form of our game character with all proper keys
    :precondition: enemy must be a dictionary in the form of our game enemies with all proper keys
    :postcondition: prints dialog and receives decisions for battle mechanics
    :postcondition: returns True if character wins the fight, otherwise False
    :return: True if character wins the fight, otherwise False
    """
    print_in_color(f"\nBoth you and the {enemy['name']} step forward, and prepare for a battle..\n", "cyan")

    while (character["current_hp"] > 0) and (enemy["current_hp"] > 0):
        ability_options = list(enumerate(character["abilities"], start=1))
        print_user_options(ability_options, "Ability")

        chosen_ability = get_user_choice(ability_options)

        print_in_color(f"\nYour {chosen_ability} hits the {enemy['name']}", "cyan")
        # enemy health will decrease by character damage * character level * (1 + (0.1 * staff rarity))
        try:
            damage_given = character["damage"] * character["level"] * (1 + (0.2 * character["staff"]["rarity"]))
        except TypeError:
            damage_given = character["damage"] * character["level"]
        enemy["current_hp"] -= round(damage_given)

        print_in_color(f"But the {enemy['name']}'s attack lands successfully as well", "cyan")
        # character health with decrease by 10 * (1 + (0.2 * enemy level))
        damage_taken = 10 * (1 + (0.2 * enemy["level"]))
        character["current_hp"] -= round(damage_taken)

        print_in_color(f"\n[{character['name']} | hp: {character['current_hp']}/{character['max_hp']}]", "yellow")
        print(f"[{enemy['name']} | hp: {enemy['current_hp']}/{enemy['max_hp']}]")

    if (enemy["current_hp"] <= 0) and (character["current_hp"] > 0):
        print_in_color(f"\n\nCongratulations! You have defeated the {enemy['name']}", "cyan")

        if enemy["level"] > character["level"]:
            earned_xp = 15 * ((enemy["level"] - character["level"]) + 1)
        else:
            earned_xp = 15

        if character["level"] < 3:
            character["xp"] += earned_xp
            print_in_color(f"\n[{character['name']} | xp: +{earned_xp}]", "yellow")

        enemy_item = enemy["item"]
        try:
            character_item_rarity = character[enemy_item["type"]]["rarity"]
        except TypeError:
            character_item_rarity = 0

        # gain enemy item if they have one, and it's rarity is more than the one you have
        if enemy_item and (enemy_item["rarity"] > character_item_rarity):
            character[enemy["item"]["type"]] = {
                key: value for key, value in enemy['item'].items() if key != 'type'
            }
            print_in_color(f"[{character['name']} | {enemy['item']['type']}: +{enemy['item']['name']}]\n", "yellow")

        enemy["current_hp"] = enemy["max_hp"]
        return True

    enemy["current_hp"] = enemy["max_hp"]
    return False


def fight_decision() -> str:
    """
    Display battle choices for user and return decision received from stdin.

    :postcondition: displays battle choices for user and returns decision received from stdin as a string
    :return: user decision received from stdin as a string
    """
    options = list(enumerate(["Fight", "Flee"], start=1))

    print_user_options(options, "Choice")

    return get_user_choice(options, True)


def generate_enemy_battle(enemy: dict):
    """
    Generate an enemy battle function with the enemy data.

    :param enemy: an enemy in dictionary form
    :precondition: enemy must be a dictionary in the form of our game enemies with all proper keys
    :postcondition: generates a function with the specific enemy data
    :return: an enemy battle function with the specific enemy data
    """
    def enemy_battle(character: dict) -> bool:
        """
        Print dialog and receive decisions for choosing whether to start an enemy battle.

        The character dictionary is modified during execution.

        :param character: a character in dictionary form
        :precondition: character must be a dictionary in the form of our game character with all proper keys
        :postcondition: prints dialog and receive decisions for choosing whether to start an enemy battle
        :postcondition: returns True if character wins the enemy battle, otherwise False
        :return: True if character wins the enemy battle, otherwise False
        """
        print_in_color(f"Out of the corner of your eye you see a {enemy['name']} appear!\n", "cyan")

        if character["level"] < enemy["level"]:
            print_in_color(f"This enemies level is greater than yours, you might want to weigh your options before "
                           f"you make your decision\n", "red")

        decision = fight_decision()

        if int(decision) == 1:
            return fight(character, enemy)
        else:
            print_in_color(f"\nAs you turn to flee the {enemy['name']} says:", "cyan")
            print("I should have guessed. You do seem like a cowardly creature. I will be here if you wish "
                  "to return with a bit more courage..")
            return False

    return enemy_battle


# Sub-Boss 1: Lord-Commander Ymir --------------------------------------------------------------------------------------
def lord_commander_ymir():
    """
    Generate and return the ymir mini boss battle function.

    :postcondition: generates and returns the ymir mini boss battle function
    :return: the ymir mini boss battle function
    """
    ymir = {
                "name": "Lord-Commander Ymir",
                "max_hp": 400,
                "current_hp": 400,
                "level": 5,
                "item": {
                    "type": "armour",
                    "name": "Ymir's Royal Armour",
                    "rarity": 5
                    }
                }

    def ymir_battle(character: dict) -> bool:
        """
        Print dialog and receive decisions for choosing whether to start the mini boss battle.

        The character dictionary is modified during execution.

        :param character: a character in dictionary form
        :precondition: character must be a dictionary in the form of our game character with all proper keys
        :postcondition: prints dialog and receive decisions for choosing whether to start the mini boss battle
        :postcondition: returns True if character wins the mini boss battle, otherwise False
        :return: True if character wins the mini boss battle, otherwise False
        """
        print_in_color("You reach closer to the throne room, and arrive at a grand hall supported by marble pillars \n"
                       "and the statues depict the past heroes and kings of Alyndelle.\n",
                       "cyan")
        print_in_color("***CRASH***.\n"
                       "There's dust and smoke everywhere!\n"
                       "*cough cough*\n"
                       "You see a huge figure appear as the dust settles.", "cyan")
        print_in_color("He is clad in ornate armor; those scratches and gouges on his armor proving the warrior's "
                       "skill.\n", "cyan")

        if character["level"] <= 3:
            print_in_color(f"\nThis enemies level is greater than yours, you might want to weigh your options before "
                           f"you make your decision\n", "red")

        decision = fight_decision()

        if int(decision) == 1:
            print_in_color(f"The giant knight notices you, and he readies his greatsword: \n", "cyan")
            print("I commend you for making this far, but, your luck ends here, mortal.\n"
                  "On my honour as the Right wing of Alyndelle, the guardian of this empire,\n"
                  "and as the Lord-Commander, I must stop you.\n")

            return fight(character, ymir)
        else:
            print_in_color(f"\nYou fled. You should probably get stronger first.", "cyan")
            return False

    return ymir_battle


# Sub-Boss 2: Royal Knight ---------------------------------------------------------------------------------------------
def royal_mage_angelozzi():
    """
    Generate and return the angelozzi mini boss battle function.

    :postcondition: generates and returns the angelozzi mini boss battle function
    :return: the angelozzi mini boss battle function
    """
    angelozzi = {
                "name": "Royal Battle-Mage Angelozzi",
                "max_hp": 250,
                "current_hp": 250,
                "level": 7,
                "item": {
                    "type": "staff",
                    "name": "Angelozzi's Ill-Omen",
                    "rarity": 5
                    }
                }

    def angelozzi_battle(character: dict) -> bool:
        """
        Print dialog and receive decisions for choosing whether to start the mini boss battle.

        The character dictionary is modified during execution.

        :param character: a character in dictionary form
        :precondition: character must be a dictionary in the form of our game character with all proper keys
        :postcondition: prints dialog and receive decisions for choosing whether to start the mini boss battle
        :postcondition: returns True if character wins the mini boss battle, otherwise False
        :return: True if character wins the mini boss battle, otherwise False
        """
        print_in_color("As you exit the narrow collider, you arrive at a grand opening to what seems like a giant "
                       "underground cave...You notice a cathedral in the distance.\n\n"
                       "'How can someone build something so magnificent underground,' you thought.\n", "cyan")
        print_in_color("As you stand there in awe, you notice a huge knight clad in royal armour towering over the "
                       "cathedral entrance.\n", "cyan")
        print_in_color(f"You approach the giant knight to observe them better.\n", "cyan")

        if character["level"] <= 3:
            print_in_color(f"\nThis enemies level is greater than yours, you might want to weigh your options before "
                           f"you make your decision\n", "red")

        decision = fight_decision()

        if int(decision) == 1:
            print_in_color(f"The battle mage notices you, he readies his staff: \n", "cyan")
            print("You wretched createre, how dare you stain this sacred haven with your miserable existence.\n"
                  "Instead of fulfilling your duty as one of the royal knights, you chose to betray our King.\n"
                  "I do not know how you escaped your cell, but on my honour as the Left wing of Alyndelle, "
                  "the guardian of this empire, I must stop you.\n")

            return fight(character, angelozzi)
        else:
            print_in_color(f"\nYou fled. You should probably get stronger first.", "cyan")
            return False

    return angelozzi_battle


# Final Boss: God-King Thompson ----------------------------------------------------------------------------------------
def god_king_thompson():
    """
    Generate and return the god king thompson final boss battle function.

    :postcondition: generates and returns the god king thompson final boss battle function
    :return: the god king thompson final boss battle function
    """
    thompson = {
                "name": "God-King Thompson",
                "max_hp": 450,
                "current_hp": 450,
                "level": 6,
                "item": {
                    "type": "staff",
                    "name": "Demonic Python Staff",
                    "rarity": 7
                    }
                }

    def thompson_battle(character: dict) -> bool:
        """
        Print dialog and receive decisions for choosing whether to start the final boss battle.

        The character dictionary is modified during execution.

        :param character: a character in dictionary form
        :precondition: character must be a dictionary in the form of our game character with all proper keys
        :postcondition: prints dialog and receive decisions for choosing whether to start the final boss battle
        :postcondition: returns True if character wins the final boss battle, otherwise False
        :return: True if character wins the final boss battle, otherwise False
        """
        print_in_color("As you enter into throne room, you see a colossal of a man sitting on the Golden throne.\n"
                       "He must be the king, the man who stole the light and betrayed the very gods itself.\n",
                       "cyan")
        print_in_color("You approach the golden throne\n", "cyan")

        if character["level"] <= 3:  # max level is three?
            print_in_color(f"\nThis enemies level is greater than yours, you might want to weigh your options before "
                           f"you make your decision\n", "red")

        decision = fight_decision()

        if int(decision) == 1:
            print_in_color("The King acknowledge you, and readies his Warhammer: \n", "cyan")
            print("You have done well, mortal. It is commendable. However, as the God King of Alyndelle,"
                  "I cannot allow your transgression no longer.\nYour treachery will end here, I will not "
                  "allow the Flame of Humanity to be restored. This is the sacrifice your kind must make "
                  "for my victory.")

            return fight(character, thompson)
        else:
            print_in_color(f"\nYou fled. You should probably get stronger first.", "cyan")
            return False

    return thompson_battle


# Generate Riddles -----------------------------------------------------------------------------------------------------
def generate_riddle(riddle_data: dict):
    """
    Generate and return a riddle function with the specific riddle_data.

    :postcondition: generates and returns a riddle function with the specific riddle_data
    :return: a riddle function with the specific riddle_data
    """
    def riddle_success(character: dict) -> None:
        """
        Print dialog and accept input for decisions after correctly answering a riddle.

        The character dictionary is modified during execution.

        :param character: a character in dictionary form
        :precondition: character must be a dictionary in the form of our game character with all proper keys
        :postcondition: prints dialog and accepts input for decisions after correctly answering a riddle
        """
        print_in_color(f"\n\nCongratulations {character['name']}, you are not as dumb as I thought for a creature such "
                       f"as yourself.", "green")

        if character["level"] < 3:
            character["xp"] += 15
            print_in_color(f"\n[{character['name']} | xp: +15]", "yellow")

        print_in_color(f"\n\nTo reward your success, I give you two options: try your luck at possibly earning a "
                       f"new ability, or accept the gift of maximum health", "green")

        success_options = list(enumerate(["Try my luck at a new ability", "Refill HP to max"], start=1))

        print_user_options(success_options, "Choice")

        user_choice = get_user_choice(success_options, True)

        if int(user_choice) == 1:
            new_ability = riddle_data["ability"]
            if (
                    new_ability is not None and
                    new_ability not in character["abilities"]
            ):
                character["abilities"].append(new_ability)
                print(f"\nYou got lucky! I am feeling generous and will grant you a new ability. You can now use "
                      f"{new_ability}")
                print_in_color(f"\n[{character['name']} | abilities: +'{new_ability}']", "yellow")
            else:
                print("\nOh no, looks like you lost the coin flip, you will not be getting a new ability.")
        else:
            difference = character["max_hp"] - character["current_hp"]
            character["current_hp"] = character["max_hp"]
            print_in_color(f"\n[{character['name']} | hp: +{difference}]", "yellow")

    def riddle(character: dict) -> bool:
        """
        Print dialog and accept input for answering a riddle.

        The character dictionary is modified during execution.

        :param character: a character in dictionary form
        :precondition: character must be a dictionary in the form of our game character with all proper keys
        :postcondition: prints dialog and accepts input for answering a riddle
        """
        print_in_color("As you enter a dark, candle-lit room; you notice a mysterious potion placed by your feet.\n"
                       "You picked it up out of curiosity, but it started to shake violently.", "cyan")
        print_in_color("***POOF***", "cyan")
        print_in_color("Through the thick purple smoke, a Phantom Imp appears, with unnaturally wide smile, \n"
                       "and in a high-pitch crackle, speaks:", "cyan")
        time.sleep(3)

        print_in_color(r"""
                        _.----._     _.---.
                     .-'        `-.-'      `.
                   .'                 .:''':.`.
                 .'        .:'''':. .' .----.  `.
             .-./        .' .----.    /  .-. \   `.
            /.-.           /  .-. \   \ ' O ' |    \
            ||        `.   | ' O '/    \ `-' /     |
            || (        \   \ `-'/      `-.__     / `.
             \`-'        )   .-'  --         )        `.
              `-'     _.'   (            _.-'    _/\    \
                 `.       /\_ `-.____..-'     .-' _/    /
                   `.     \_ `-._         _.-'_.-'   .' 
                     `--.._ `-._ `-.__..-'_.-'     .' 
                   .-'     `-._ `--.__..-'  _.----'`. 
                  /            `---.......-' _     \ \ 
                 /                          ( `-._.-` )
                /  /     _                  .-    _.-' 
               (  `-._.-' )                (_   .'    \ 
                `-._      -.               (_.-'       |
                    `.     _)                   __..---'
                   |  `-._) ''...__ .-. __...'''__..---'
                    \      '''...__((=))__...'''      /
                     |              `-'             .'
                     \                             /
                      |                           |
                      \     \    \      /    /   /
                       `. \               /     /
                         `.    \   \   /   /   /
                           `--.._   ` '  _.--'
                                  [====]
                                   )  (
                                .-'    '-.
                               |          |
                               | .------. |
                               | | LGBT | |
                               | '------' |
                               |          |
                               '----------'
                               """, "green")

        print(f"Oh {character['name']}, you foolish creature, how dare you interrupt my slumber. For your transgression"
              f" you must prove your intellect to me with a riddle if you want me to spare your life..\n")
        time.sleep(1)
        print_in_color(riddle_data["question"], "purple")

        options = list(enumerate(riddle_data["options"], start=1))

        print_user_options(options, "Response")

        print_in_color("\nYou have one chance to guess the answer or you will be punished.\nPlease choose the correct "
                       "answer to this riddle..", "purple")

        user_answer = get_user_choice(options)

        if user_answer == riddle_data["answer"]:
            riddle_success(character)
            return True
        else:
            print_in_color(f"\n{character['name']}, I knew a creature such as yourself was not intellectually gifted. "
                           f"That answer is far from correct and for that you must be punished!", "red")
            lost_hp = character["current_hp"] * 0.25
            character["current_hp"] -= round(lost_hp)
            print_in_color(f"\n[{character['name']} | hp: -{lost_hp}]", "yellow")
            return False

    return riddle


def create_batch_of_enemy_battles(amount: int) -> list:
    """
    Read a list of json data and generate a list of length amount, containing battle functions generated from json data.

    :param amount: an integer greater than 0
    :precondition: amount must be an integer greater than 0
    :postcondition: generates a list of length amount, containing battle functions generated from json data
    :return: a list of length amount, containing battle functions generated from json data
    """
    battles = []

    with open("json/enemies.json") as file_object:
        enemy_data = json.load(file_object)

        for enemy in enemy_data:
            battles.append(generate_enemy_battle(enemy))

    return battles[:amount + 1]


def create_batch_of_riddles(amount: int) -> list:
    """
    Read a list of json data and generate a list of length amount, containing riddle functions generated from json data.

    :param amount: an integer greater than 0
    :precondition: amount must be an integer greater than 0
    :postcondition: generates a list of length amount, containing riddle functions generated from json data
    :return: a list of length amount, containing riddle functions generated from json data
    """
    riddles = []

    with open("json/riddles.json") as file_object:
        riddles_data = json.load(file_object)

        for riddle in riddles_data:
            riddles.append(generate_riddle(riddle))

    return riddles[:amount + 1]


def get_generic_room_description() -> str:
    """
    Return a random room description selected from a list.

    :postcondition: selects and returns a random room description as a string
    :return: a random room description as a string
    """
    descriptions = [
        "\nAs your foot passes the threshold into the next room, you feel something slither across your toes..",
        "\nYou are approaching the next room, and you see a dark mist fly past the archway..",
        "\nThe room feels cold and appears empty, but you sense a presence lingering..",
        "\nYou can taste the dampness in the air as you enter through the arched cobblestone..",
        "\nThe cold stone walls seem to radiate brisk air as you enter the room..",
        "\nYou step forward into the next room, you examine the walls and notice the hand of a skeleton jammed between "
        "two stones..",
        "\nYou hear the soft tapping of spider legs across the cobblestone archway..",
        "\nBeyond the cobblestone archway is a crumbling room, covered in crawling insects, broken pottery and bat "
        "droppings..",
        "\nTo the west you see a small statue of the queen's crown, crumbling onto the stone floor. It is covered in "
        "small bones, rat droppings and dead insects..",
        "\nA warn banner hangs from archway, displaying the crest of our dear queen. It is battered and torn, "
        "covered in condensation and insects..",
        "\nA fallen statue blocks the archway. You are able to slip through under arm, and enter into a room too "
        "clean for comfort..",
        "\nYou hear the drip of water to your east. There is a small fountain streaming out of the mouth of a stone "
        "gargoyle, mounted to the wall..",
        "\nA dim torch highlights the features of a pillaged statue, that has been eaten by time itself..",
        "\nThe deep purple banners flood the walls, with bats gripping to the bottom. You enter silently as to not "
        "disrupt them..",
        "\nA small puddle makes contact with the sole of your foot. You look up to see a crack in the cobblestone "
        "dripping at an unsettling-ly slow pace..",
        "\nIvy cracks the cobblestone and lines the ceiling. It's vines seem to plague the room, having propagated "
        "from north wall..",
        "\nA gloomy torch sits on the wall to the south. It's light fading with each grain of the hourglass..",
        "\nUnder your foot you hear the crack of bone. The room is a wasteland of bone and insects..",
        "\nA minor hum echoes off of the cobblestone walls. It is not random, but in an unsettling rhythm..",
        "\nA grand statue of the kingdom stands 10 feet tall in the far corner of the room, silently inspiring you to "
        "escape..",
        "\nOvergrown vines plague the stone floor, making you conscious of your feet. You fear that getting your foot "
        "stuck could render you a target for attack..",
        "\nBroken pottery carpets the floor. As you step you hear the cracking and fear that there may be creatures "
        "lurking beneath..",
        "\nYou advance carefully deeper through the castle dungeon, and enter a dark room, lit only by a dim torch..",
        "\nThe archway to the next room is crumbling under the damp runoff, pebbles fall like rain as you cover your "
        "head to enter..",
        "\nThere is a suspicious hole on the west wall, you fear something may be watching.."
    ]

    return random.choice(descriptions)


def get_generic_actions() -> list:
    """
    Return a list of 97 shuffled action functions.

    :postcondition: returns a list of 97 shuffled action functions
    :return: a list of 97 shuffled action functions
    """
    actions = []

    # 36 battles
    enemy_battles = create_batch_of_enemy_battles(12)
    enemy_battles *= 3
    actions += enemy_battles

    # 36 riddles
    riddles = create_batch_of_riddles(26)
    actions += (riddles + riddles[:11])

    # 13 spider web rooms
    actions += list(itertools.repeat(spider_web_blockade, 13))

    # 12 empty rooms
    actions += list(itertools.repeat(empty_room, 12))

    random.shuffle(actions)

    return actions


def game_completed() -> None:
    """
    Print final dialogs and ascii art indicating the game is completed.

    :postcondition: prints final dialogs and ascii art indicating the game is completed
    """

    print_in_color("...\n", "cyan")
    time.sleep(1)
    print("H-How is this possible...how can a mortal like you defeat me,")
    print_in_color("\nThe King collapsed to the ground. You did it, You finally defeated him!\n"
                   "His body turns into a golden dust as the flame of humanity returned to the golden alter "
                   "sitting behind the throne.\n", "cyan")
    time.sleep(1)
    print_in_color("It's finally over, the flame is finally back to where it should be...\n"
                   "You collapsed to the ground in exhaustion...this is the start of a new era...\n", "cyan")
    time.sleep(3)
    print_in_color("""

                                      _A_
                                     / | \ 
                                    |.-=-.|
                                    )\_|_/(
                                 .=='\   /`==.
                               .'\   (`:')   /`.
                             _/_ |_.-' : `-._|__\_
                            <___>'\    :   / `<___>
                            /  /   >=======<  /  /
                          _/ .'   /  ,-:-.  \/=,'
                         / _/    |__/v^v^v\__) \ 
                         \(\)     |V^V^V^V^V|\_/
                          (\ \    \`---|---'/
                            \ \    \-._|_,-/
                             \ \    |__|__|
                              \ \  <___X___>
                               \ \  \..|../
                                \ \  \ | /
                                 \ \ /V|V\ 
                                  \|/  |  \ 
                                   '--' `--`   by hjw
                          ______               _   _                                                             
                         |  ____|             | | | |                                                            
                         | |__     _ __     __| | | |                                                            
                         |  __|   | '_ \   / _` | | |                                                            
                         | |____  | | | | | (_| | |_|                                                            
                         |______| |_| |_|  \__,_| (_)                                                            
                            \U0001F389 You won the game! \U0001F389 	                                                    
                           \U0001F970 Thanks for playing! \U0001F970 	 	                                                    
    """, "cyan")


def main():
    """
    Drive the program.
    """
    print("You are attempting to execute the actions.py module.")
    print("Executing this module does not do anything.")


if __name__ == '__main__':
    main()
