#!/usr/bin/env python3
# Created By: Atri Sarker
# Date: April 29, 2025
# King of the Ants

# Import library for handling randomness
import random

# Import util.py, used for input+output
import util

# Import math, used for rounding
import math

# Initial stats
population = 100
gold = 0
power = 100

# Initialize a list to hold the flags for the user
user_flags = []


# EVENT CLASS
class Event:
    # Function that checks whether an event is available or not
    def available(self) -> bool:
        # Check if the user has the prerequisite flags
        for flag in self.inclusion_flags:
            if flag not in user_flags:
                return False

        # Check if the user does not have the blacklisted flags
        for flag in self.exclusion_flags:
            if flag in user_flags:
                return False

        # Check if the user meets the minimum stat criteria
        if population < self.min_population:
            return False
        if gold < self.min_gold:
            return False
        if power < self.min_power:
            return False
        # Check if the user meets the maximum stat criteria
        if (self.max_population != -1) and (population > self.max_population):
            return False
        if (self.max_gold != -1) and (gold > self.max_gold):
            return False
        if (self.max_power != -1) and (power > self.max_power):
            return False

        # Once all checks are passed, return True
        return True

    # Function that displays the synopsis of the event
    def synopsis(self):
        print("This is an event!")

    # The event question that is asked to the user after the synopsis
    question: str = "Do you understand? (yes/no): "
    # LIST OF POSSIBLE DECISIONS FOR THE PLAYER TO MAKE
    # ALL DECISIONS MUST BE UPPERCASE
    decisions: list[str] = ["YES", "NO"]

    # Function that displays the aftermath
    def effect(self, decision):
        print(f"You picked {decision}")

    # Flag Lists
    # List of prerequisite flags
    inclusion_flags: list[str] = []
    # List of blacklisted flags
    exclusion_flags: list[str] = []

    # Minimums and Maximums
    # -1 will represent infinity
    # These values are used to check the availability of the event
    min_population = 0
    max_population = -1
    min_gold = 0
    max_gold = -1
    min_power = 0
    max_power = -1

    # Event Name
    name = "Event Name"

    # Weight determines the likelihood of an event
    # I decided to keep it as a number [different from design]
    weight = 0


# Function for adding a flag
def add_flag(flag_name: str):
    # Check if flag is not inside user_flags [Not really needed]
    if flag_name not in user_flags:
        # Append it to the flag list
        user_flags.append(flag_name)


# Initialize list to hold all the events
event_list: list[Event] = []


# Function for adding event to event_list
def add_event(event: Event):
    # Append event to the event list
    event_list.append(event)


# Function that will only be called once
# ################################################
# Creates all the events
# ################################################
def make_events():
    # Template event [With Comments]
    def template_event_with_comments():
        # Instantiate new event
        event = Event()
        # Set event name
        event.name = "template"

        # Define Synopsis
        def event_synopsis():
            pass

        # Set event's synopsis to defined function
        event.synopsis = event_synopsis
        # Set question and decisions
        event.question = ""
        event.decisions = []

        # Set and Define Effect
        def event_effect(decision):
            pass

        # Set event's effect to defined function
        event.effect = event_effect
        # Set flags
        event.inclusion_flags = []
        event.exclusion_flags = []
        # Set weight
        event.weight = 0
        # Set Other Stuff If Needed
        # Return event
        return event

    # Template event [Without Comments]
    def template_event():
        event = Event()
        event.name = "Template"

        def event_synopsis():
            pass

        event.question = ""
        event.decisions = []
        event.synopsis = event_synopsis

        def event_effect(decision):
            pass

        event.effect = event_effect

        event.inclusion_flags = []
        event.exclusion_flags = []
        event.weight = 0
        return event

    # Introduction
    def intro():
        event = Event()
        event.name = "Introduction"

        def event_synopsis():
            util.blue("[ROYAL ADVISOR] Vexel\n")
            util.blue("Your Majesty, you have awakened at last.\n")
            util.blue("Forgive my intrusion, but time is of the essence.\n")
            util.blue(
                "The colony awaits your command, and your wisdom is needed now more than ever.\n"
            )

        event.synopsis = event_synopsis
        event.question = "Do you understand your role, my liege? (yes/no): "
        event.decisions = ["YES", "NO"]

        def event_effect(decision):
            util.blue("[ROYAL ADVISOR] Vexel\n")
            if decision == "YES":
                util.blue("Excellent, Your Majesty.\n")
                util.blue("Let's continue.\n")
            elif decision == "NO":
                util.blue("Ah, a jest, perhaps?\n")
                util.blue(
                    "No matter--your instincts shall guide you, as they always have.\n"
                )
            add_flag("INTRO_COMPLETE")

        event.effect = event_effect
        event.inclusion_flags = []
        event.exclusion_flags = ["INTRO_COMPLETE"]
        event.weight = -1
        return event

    add_event(intro())

    # Tutorial
    def tutorial():
        event = Event()
        event.name = "The Three Pillars [Tutorial]"

        def event_synopsis():
            util.blue("[ROYAL ADVISOR] Vexel\n")
            util.blue("Before you proceed, Your Majesty, ")
            util.blue("allow me to speak of the three pillars that uphold your rule.\n")
            util.blue("\n")
            util.blue("First: *")
            util.purple("POPULATION")
            util.blue("*. Our strength in numbers. It is our greatest strength.\n")
            util.blue(
                "This is the most important pillar and must be upheld at all times\n"
            )
            util.blue("Without it, our goal, is nothing but a lofty dream.\n")
            util.blue("\n")
            util.blue("Second: *")
            util.yellow("GOLD")
            util.blue("*. The foundation of our economy. ")
            util.blue(
                "It funds our expansion, our armies, and the future of the colony.\n"
            )
            util.blue("\n")
            util.blue("Third: *")
            util.red("POWER")
            util.blue(
                "*. The measure of your might. When battle comes, it is this that determines victory or defeat.\n"
            )
            util.blue("\n")
            util.blue("Every decision you make shall shape these forces. ")
            util.blue(
                "Balance them wisely, for the fate of the empire lies in your hands.\n"
            )

        event.synopsis = event_synopsis
        event.question = "Shall we proceed, Your Majesty? (yes): "
        event.decisions = ["YES"]

        def event_effect(decision):
            util.blue("[ROYAL ADVISOR] Vexel\n")
            util.blue("Very well. The colony awaits your wisdom.\n")
            util.blue("Here's a sum of gold to get you started. ")
            util.green("[+500 GOLD]\n")
            global gold
            gold += 500
            add_flag("TUTORIAL_COMPLETE")

        event.effect = event_effect
        event.inclusion_flags = ["INTRO_COMPLETE"]
        event.exclusion_flags = ["TUTORIAL_COMPLETE"]
        event.weight = -1
        return event

    add_event(tutorial())

    def incident1():
        event = Event()
        event.name = "A stroll in the kingdom"

        def event_synopsis():
            util.grey("As you are taking a stroll outside the palace, \n")
            util.grey(
                "you notice a fellow ant that is trapped under a slump of mashed banana.\n"
            )
            util.blue("He begs for a helping hand.\n")

        event.synopsis = event_synopsis
        event.question = "What do you decide to do? (help/kill/ignore): "
        event.decisions = ["HELP", "KILL", "IGNORE"]

        def event_effect(decision):
            global population
            global gold
            global power
            if decision == "HELP":
                util.blue("Thank you, Your Majesty.\n")
                util.blue("He gifts you a pleasant alm. ")
                util.green("[+20 GOLD]\n")
                gold += 20
            elif decision == "KILL":
                util.red("WEAKNESS IS NOT TOLERATED IN THIS KINGDOM! ")
                util.red("[-1 POPULATION] ")
                population -= 1
                util.green("[+10 POWER]\n")
                power += 10
                util.grey(
                    "Bystanders watch in shock as you ransack the remaining parts of his dead body. "
                )
                util.green("[+10 GOLD]\n")
                gold += 10
            elif decision == "IGNORE":
                util.grey("Nothing ever happens... ")
                util.red("[-1 POPULATION]\n")
                population -= 1

            add_flag("INCIDENT1")

        event.effect = event_effect
        event.inclusion_flags = ["TUTORIAL_COMPLETE"]
        event.exclusion_flags = ["INCIDENT1"]
        event.weight = 1
        return event

    add_event(incident1())

    def incident2():
        event = Event()
        event.name = "Echoes of Power"

        def event_synopsis():
            util.purple("[Bandit Leader] Duarf, Goblin Slayer\n")
            util.purple("You are a Fraud.\n")
            util.purple("Give me 300 gold. Otherwise, I will burn down your colony.\n")

        event.synopsis = event_synopsis
        event.question = "What do you decide to do? (give/kill/ignore): "
        event.decisions = ["GIVE", "KILL", "IGNORE"]

        def event_effect(decision):
            global population
            global gold
            global power
            if decision == "GIVE":
                util.purple("[Bandit Leader] Duarf, Goblin Slayer\n")
                util.purple("You truly are a Fraud. ")
                util.red("[-300 GOLD]\n")
                gold -= 300
            elif decision == "KILL":
                util.grey(f"Bandit Army Power: 300\n")
                util.grey(f"Your Power: {power}\n")
                if power >= 300:
                    util.red(f"Your army slays the bandits and loots their corpses. ")
                    util.green("[+1000 GOLD]\n")
                    gold += 1000
                    add_flag("BANDITS_VANQUISHED")
                else:
                    util.red(f"Your army fails to prevent the carnage. ")
                    util.red("[-50 POPULATION] ")
                    population -= 50
                    util.red("[-25 POWER]\n")
                    power -= 20
            elif decision == "IGNORE":
                util.grey("Nothing ever happens... ")
                util.red("[-95 POPULATION]\n")
                population -= 95

        event.effect = event_effect
        event.inclusion_flags = ["TUTORIAL_COMPLETE"]
        event.exclusion_flags = ["BANDITS_VANQUISHED"]
        event.weight = 1
        event.min_gold = 300
        return event

    add_event(incident2())

    def reinforcements1():
        event = Event()
        event.name = "Reinforcement"

        def event_synopsis():
            util.blue("[ROYAL ADVISOR] Vexel\n")
            util.blue("Our army is requesting new equipment.\n")

        event.synopsis = event_synopsis
        event.question = "What do you decide to do? (accept/refuse): "
        event.decisions = ["ACCEPT", "REFUSE"]

        def event_effect(decision):
            global population
            global gold
            global power
            if decision == "ACCEPT":
                util.grey(
                    "Equipment is reforged, strengthening the ranks--at the cost of your treasury. "
                )
                util.red("[-100 GOLD] ")
                gold -= 100
                if "FIRE_NATION_CONFLICT_END" in user_flags:
                    util.green(f"[+{300 + power} POWER]\n")
                    power += 300 + power
                else:
                    util.green("[+100 POWER]\n")
                    power += 100
            elif decision == "REFUSE":
                util.blue("[ROYAL ADVISOR] Vexel\n")
                util.blue("Your wish is my command.\n")
                util.blue("Afterall, we can't just keep spoiling the soldiers.\n")
                util.blue("They shall continue using their rusty sticks.\n")

        event.effect = event_effect
        event.inclusion_flags = ["TUTORIAL_COMPLETE"]
        event.exclusion_flags = []
        event.weight = 1
        event.min_gold = 100
        return event

    add_event(reinforcements1())

    def reinforcements2():
        event = Event()
        event.name = "Awakened Mercenary"

        def event_synopsis():
            util.orange("[Homeless Assassin] Tojiro, Heavenly Demon\n")
            util.orange("I was blessed with strength. \n")
            util.orange("With my blade, kingdoms were erased. \n")
            util.orange("I will offer you my service in exchange for your riches. \n")
            util.orange("1000 gold will suffice. \n")

        event.synopsis = event_synopsis
        event.question = "What do you decide to do? (accept/refuse): "
        event.decisions = ["ACCEPT", "REFUSE"]

        def event_effect(decision):
            global population
            global gold
            global power
            if decision == "ACCEPT":
                util.grey("The heavenly demon is added to your ranks.")
                util.red("[-1000 GOLD] ")
                util.green("[+1000 power]\n")
                gold -= 1000
                power += 1000
                add_flag("MERCENARY_OBTAINED")
            elif decision == "REFUSE":
                util.grey("The mercenary promptly leaves.\n")
                util.grey("He leaves behind a child in his stead. ")
                util.green("[+1 population]\n")
                population += 1
                add_flag("CHILD_OBTAINED")
                util.grey(
                    "In the distance, you can see a relieved smirk on the mercenary's face. \n"
                )
                util.grey("Perhaps this was his plan all along. \n")
                util.grey("You will never see him again. \n")

        event.effect = event_effect
        event.inclusion_flags = ["TUTORIAL_COMPLETE"]
        event.exclusion_flags = ["CHILD_OBTAINED", "MERCENARY_OBTAINED"]
        event.weight = 1
        event.min_gold = 1000
        return event

    add_event(reinforcements2())

    def fire_nation_extortion():
        event = Event()
        event.name = "Extortment"

        def event_synopsis():
            util.red("[Fire Nation Scout] Zeko, fire ant\n")
            util.red("I represent the Fire Nation. \n")
            util.red("I am here to collect our tribute. \n")
            util.red("We deserve it because we are awesome and cool. \n")
            util.red("Anyways, 100 gold, pay up right now. \n")

        event.question = "What do you decide to do? (pay/refuse): "
        event.decisions = ["PAY", "REFUSE"]
        event.synopsis = event_synopsis

        def event_effect(decision):
            global gold
            if decision == "PAY":
                util.red("[Fire Nation Scout] Zeko, fire ant\n")
                util.red("Thanks for being smart! ")
                util.red("[-100 GOLD] \n")
                gold -= 100
            elif decision == "REFUSE":
                util.red("[Fire Nation Scout] Zeko, fire ant\n")
                util.red("The Fire Nation shall remember this! \n")
                util.red("You have just guaranteed your demise. \n")
                add_flag("FIRE_NATION_CONFLICT")

        event.effect = event_effect
        event.inclusion_flags = ["TUTORIAL_COMPLETE"]
        event.exclusion_flags = ["FIRE_NATION_CONFLICT"]
        event.weight = 1
        event.min_gold = 100
        return event

    add_event(fire_nation_extortion())

    def fire_nation_revenge():
        event = Event()
        event.name = "The Fire Nation Attacks"

        def event_synopsis():
            util.red("[Fire Nation Scout] Zeko, fire ant\n")
            util.red("The Fire Nation never forgets... \n")

        event.question = "... (continue): "
        event.decisions = ["CONTINUE"]
        event.synopsis = event_synopsis

        def event_effect(decision):
            global population
            global power
            util.grey(f"Fire Nation Power: 2000\n")
            util.grey(f"Your Power: {power}\n")
            if power >= 2000:
                util.red(f"A fierce battle takes place... \n")
                util.green("Ultimately, your colony is the victor. \n")
                util.grey("The Fire Nation Army has been wiped out. \n")
                util.grey("The land of the Fire Nation is now under your rule. ")
                util.green("[+50000 POPULATION]\n")
                population += 50000
                add_flag("FIRE_NATION_CONFLICT_END")
            else:
                util.red(f"Your colony is brutally wiped out. ")
                util.red(f"[-{population} POPULATION] \n")
                population -= population

        event.effect = event_effect
        event.inclusion_flags = ["FIRE_NATION_CONFLICT"]
        event.exclusion_flags = ["FIRE_NATION_CONFLICT_END"]
        event.weight = 2
        return event

    add_event(fire_nation_revenge())

    def tax_collection():
        event = Event()
        event.name = "Tax Collection"

        def event_synopsis():
            util.blue("[ROYAL ADVISOR] Vexel\n")
            util.blue("It's time to collect taxes, my liege.\n")

        event.synopsis = event_synopsis
        event.question = "Do you tax the colony? (yes/no): "
        event.decisions = ["YES", "NO"]

        def event_effect(decision):
            global population
            global gold
            global power
            if decision == "YES":
                util.grey("Very well. Our treasuries shall prosper.")
                util.green(f"[+{population} GOLD]\n")
                gold += population
                power += 100
            elif decision == "NO":
                util.blue("[ROYAL ADVISOR] Vexel\n")
                util.blue(
                    "A weird decision. Nevertheless, I shall trust your judgement.\n"
                )
                util.grey("The people are happy, and the colony grows. ")
                if "FIRE_NATION_CONFLICT_END" in user_flags:
                    util.green(f"[+{3000 + population//2} POPULATION]\n")
                    population += 3000 + population // 2
                else:
                    util.green("[+100 POPULATION]\n")
                    population += 100

        event.effect = event_effect
        event.inclusion_flags = ["TUTORIAL_COMPLETE"]
        event.exclusion_flags = []
        event.weight = 1
        event.max_population = 1_000_000_00
        return event

    add_event(tax_collection())

    def deja_vu():
        event = Event()
        event.name = "A Fateful Encounter"

        def event_synopsis():
            util.red("[Gambling Addict] Barbable from Liechtenstein\n")
            util.red("I challenge thee to a game of rock, paper, scissors! \n")

        event.synopsis = event_synopsis
        event.question = "What do you pick? (rock/paper/scissors): "
        event.decisions = ["ROCK", "PAPER", "SCISSORS"]

        def event_effect(decision):
            global population
            global gold
            global power
            if decision == "ROCK":
                util.grey("Barbable picked Paper. \n")
                util.grey("Paper beats Rock. You lost the round. \n")
                util.grey(
                    "Barbable spits on your colony, inflicting a terrible disease. \n"
                )
                util.grey("Society crumbles... ")
                util.red(f"[-{math.floor(population*0.5 + 1)} POPULATION]\n")
                population -= math.floor(population * 0.5 + 1)
            elif decision == "PAPER":
                util.grey("Barbable picked Scissors. \n")
                util.grey("Scissors beats Paper. You lost the round. \n")
                util.grey("Barable steals from your treasury. \n")
                util.grey("It is her prize for winning. ")
                util.red(f"[-{math.floor(gold*0.5 + 1)} GOLD]\n")
                gold -= math.floor(gold * 0.5 + 1)
            elif decision == "SCISSORS":
                util.grey("Barbable picked Rock. \n")
                util.grey("Rock beats Scissors. You lost the round. \n")
                util.grey("Your pair of scissors broke in the process. \n")
                util.grey("It was a valuable weapon... ")
                util.red(f"[-100 POWER] \n")
                power -= 100

        event.effect = event_effect
        event.inclusion_flags = ["TUTORIAL_COMPLETE"]
        event.exclusion_flags = []
        event.weight = 1
        event.min_gold = 20
        event.min_power = 110
        return event

    add_event(deja_vu())

    def reinforcements3():
        event = Event()
        event.name = "Mutation"

        def event_synopsis():
            util.purple("[Mad Scientist] Sinko\n")
            util.purple("I have a proposition >> \n")
            util.purple(
                "I've invented a potion that can grant ants special abilities.\n"
            )
            util.purple(
                "With enough funds, I can grant every member of your army a potion.\n"
            )

        event.synopsis = event_synopsis
        event.question = "What do you decide to do? (accept/refuse): "
        event.decisions = ["ACCEPT", "REFUSE"]

        def event_effect(decision):
            global population
            global gold
            global power
            if decision == "ACCEPT":
                util.grey("Drinks are readily provided to all members of your army. ")
                util.red("[-100000 GOLD] \n")
                gold -= 100000
                util.grey("All soldiers of your army gain an extra pair of limbs. \n")
                util.grey("Some even gain wings. \n")
                util.grey("Your army is much more mighty. ")
                util.green(f"[+{power*5} POWER] \n")
                power += power * 5

            elif decision == "REFUSE":
                util.purple("[Mad Scientist] Sinko\n")
                util.purple("... >> \n")

        event.effect = event_effect
        event.inclusion_flags = ["FIRE_NATION_CONFLICT_END"]
        event.exclusion_flags = []
        event.weight = 3
        event.min_gold = 100000
        event.max_power = 1_000_000_000_000
        return event

    add_event(reinforcements3())

    def dragon1():
        event = Event()
        event.name = "Slaying the Dragon [1/3]"

        def event_synopsis():
            util.blue("[ROYAL ADVISOR] Vexel\n")
            util.blue("A suspicious cave has been spotted in the distance.\n")
            util.blue("Shall we send some soldiers to go investigate it? \n")

        event.question = "Do you send soldiers? (yes/no): "
        event.decisions = ["YES", "NO"]
        event.synopsis = event_synopsis

        def event_effect(decision):
            global population
            global power
            if decision == "YES":
                util.grey("The soldiers never came back... ")
                util.red("[-100 POPULATION] ")
                population -= 100
                util.red(f"[-{power//3} POWER] \n")
                power -= power // 3
                add_flag("CAVE_INVESTIGATED")
            elif decision == "NO":
                util.blue("[ROYAL ADVISOR] Vexel\n")
                util.blue("I will trust your decision, my liege.\n")
                util.blue("It is better to not cross uncharted territories. \n")
                util.grey("A sudden fire breaks out in the colony... \n")
                util.grey("All the witnesses are dead. ")
                util.red(f"[-{1000 + population//4} POPULATION] \n")
                population -= 1000 + population // 4

        event.effect = event_effect
        event.inclusion_flags = ["FIRE_NATION_CONFLICT_END"]
        event.exclusion_flags = ["CAVE_INVESTIGATED"]
        event.weight = 3
        return event

    add_event(dragon1())

    def dragon2():
        event = Event()
        event.name = "Slaying the Dragon [2/3]"

        def event_synopsis():
            util.blue("[ROYAL ADVISOR] Vexel\n")
            util.blue("Rumours about a dragon are circulating around our colony. \n")
            util.blue("I suspect that this dragon truly exists. \n")
            util.blue("I saw it with my two own very eyes. \n")
            util.blue("This must've been the dragon that killed our men. \n")
            util.blue("It's lurking around the very cave we sent our men to. \n")
            util.blue("Do you think the kingdom is ready to defeat it? \n")

        event.question = "Should we take down the dragon? (yes/no): "
        event.decisions = ["YES", "NO"]
        event.synopsis = event_synopsis

        def event_effect(decision):
            global population
            global power
            if decision == "YES":
                util.blue("[ROYAL ADVISOR] Vexel\n")
                util.blue("Very well, my majesty. \n")
                util.blue("I shall gather the entirety of our forces. \n")
                util.blue("The dragon stands no chance against our mighty army. \n")
                util.blue("Our battle shall commence the very next dawn. \n")
                add_flag("ENGAGE_DRAGON")
            elif decision == "NO":
                util.blue("[ROYAL ADVISOR] Vexel\n")
                util.blue("I shall heed your command. \n")
                util.blue("The dragon shall live on for a couple more days. \n")
                util.grey("A sudden fire breaks out in the colony... \n")
                util.grey("All the witnesses are dead. ")
                util.red(f"[-{600 + population//5} POPULATION] \n")
                population -= 600 + population // 5

        event.effect = event_effect
        event.inclusion_flags = ["CAVE_INVESTIGATED"]
        event.exclusion_flags = ["ENGAGE_DRAGON"]
        event.weight = 1
        return event

    add_event(dragon2())

    def dragon3():
        event = Event()
        event.name = "Slaying the Dragon [3/3] [FINAL]"

        def event_synopsis():
            util.grey("It is time to face the dragon ... \n")

        event.question = "... (continue): "
        event.decisions = ["CONTINUE"]
        event.synopsis = event_synopsis

        def event_effect(decision):
            global population
            global power
            global gold
            util.grey(f"Dragon power: 500000000\n")
            util.grey(f"Your Power: {power}\n")
            if power >= 500000000:
                util.red(f"The showdown finally takes place... \n")
                util.red(f"The battle is intense and losses were made. \n")
                util.red(f"[-{population//2} POPULATION] ")
                population -= population // 2
                util.red(f"[-{power//2} POWER] \n")
                population -= power // 2
                util.green("But, in the end, your colony won. \n")
                util.grey("The mighty dragon has been defeated. \n")
                util.grey("The dragon's treasure is now yours. ")
                util.green("[+1000000000 GOLD] \n")
                gold += 1000000000
                util.grey("News of your deed spreads... ")
                util.green("[+1000000000 POWER] \n")
                power += 1000000000
                util.grey("Peace has been restored to the lands... \n")
                util.grey("You are now acknowledged as the king of the world. \n")
                util.yellow("Earth is now under your rule. \n")
                util.yellow("[+100000000000 POPULATION] \n")
                population += 100000000000
            else:
                util.red(f"The dragon tears through your army. ")
                util.red(f"[-{power} POWER] \n")
                population -= power
                util.red(f"The dragon steals all your gold. ")
                util.red(f"[-{gold} GOLD] \n")
                gold -= gold
                util.red(f"The dragon eradicates your colony. ")
                util.red(f"[-{population} POPULATION] \n")
                population -= population

        event.effect = event_effect
        event.inclusion_flags = ["ENGAGE_DRAGON"]
        event.exclusion_flags = []
        event.weight = -1
        return event

    add_event(dragon3())

    # NULL [INACCESSIBLE]
    def null():
        event = Event()
        event.name = "VOID"

        def event_synopsis():
            util.black("[FORGOTTEN ONE] NULL\n")
            util.black("You aren't supposed to be here!\n")

        event.synopsis = event_synopsis
        event.question = "What? (what): "
        event.decisions = ["WHAT"]

        def event_effect(decision):
            util.black("[FORGOTTEN ONE] NULL\n")
            util.black("...\n")
            add_flag("INTRO_COMPLETE")

        event.effect = event_effect
        event.inclusion_flags = []
        event.exclusion_flags = []
        event.weight = 0
        return event

    add_event(null())


# Initialize variable for the current event
current_event: Event = Event()


# Function that returns a list of all available events
def get_unlocked_events() -> list[Event]:
    # Initialize a list to hold the unlocked events
    unlocked_events = []
    # Go through every event in event list
    for event in event_list:
        # Check if it is available
        if event.available():
            # If it is, append it to the list
            unlocked_events.append(event)
    # Return the completed list
    return unlocked_events


# Function that gets a random unlocked event
def random_event() -> Event:
    # Get list of available events
    unlocked_events = get_unlocked_events()
    # Initialize variable to hold the total sum of weights
    sum_of_weights = 0
    # Loop through every unlocked event
    # And add up all the weights
    for event in unlocked_events:
        # A weight of -1 is a priority event
        if event.weight == -1:
            # Return it immediately
            return event
        else:
            # Increment sum of weights by event's weight
            sum_of_weights += event.weight
    # Generate a random float between 0 and sum of weights
    rand_num = random.random() * sum_of_weights
    # Initialize a variable that accounts for the weight of previous events
    weight_heap = 0
    # Loop through every unlocked event
    for event in unlocked_events:
        # minimum boundary
        min_bound = weight_heap
        # maximum boundary
        max_bound = weight_heap + event.weight
        # Check if the random number falls within the boundary
        if min_bound <= rand_num <= max_bound:
            # If it does, return the event
            return event
        else:
            # Otherwise, increment weight heap by the event's weight
            weight_heap += event.weight


# Function that displays every stat
def display_stats():
    util.purple(f"POPULATION: {population}, ")
    util.yellow(f"GOLD: {gold}, ")
    util.red(f"POWER: {power} \n")


# Function that manages the event
def process_event():
    # Clear Terminal
    util.clear_terminal()
    # Display title at top
    util.display_title()
    # Display Stats
    display_stats()
    # Display event name
    util.orange(f"~~~ < {current_event.name} > ~~~\n")
    # Display event synopsis
    current_event.synopsis()
    # Get player's decision
    decision = util.get_decision(current_event.question, current_event.decisions)
    # Clear Terminal
    util.clear_terminal()
    # Aftermath
    # Display title at top
    util.display_title()
    # Display Stats
    display_stats()
    # Display name of event
    util.orange(f"~~~ < {current_event.name} > ~~~\n")
    # Display effect
    current_event.effect(decision)
    # Pause
    util.pause()


# GAME LOOP
def game_loop():
    # Set current event to a random unlocked event
    global current_event
    current_event = random_event()
    # Process event + decision
    process_event()


def main():
    # Make all events
    make_events()
    # Keep on looping indefinitely
    # Until user wins or loses
    while True:
        # GAME LOOP
        game_loop()
        # At the end of every game loop,
        # Check if population is less than or equal to 0
        if population <= 0:
            # population <= 0 results in a loss
            # LOSS
            util.red("Your population has been eradicated.\n")
            util.red("Your kingdom has fallen. The colony is no more.\n")
            util.red("This is all your fault.\n")
            util.red("You lost. \n")
            # BREAK
            break
        # Check if population is more than 1 billion
        elif population >= 1_000_000_000:
            # population >= 1_000_000_000 results in a win
            # WIN
            util.green("The kindom is thriving.\n")
            util.green("No one dares to challenge you anymore.\n")
            util.green("The colony shall never fall as long as you rule.\n")
            util.green("You win. \n")
            break
        # [ END ]
        util.white("Thanks for Playing!\n")


if __name__ == "__main__":
    main()
