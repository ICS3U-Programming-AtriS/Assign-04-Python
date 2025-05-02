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
user_flags = []


class Event:
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

    # I decided to keep it as a number
    weight = 0

    def synopsis(self):
        print("This is an event!")

    question: str = "Do you understand? (yes/no): "
    # ALL DECISIONS MUST BE UPPERCASE
    decisions: list[str] = ["YES", "NO"]

    def effect(self, decision):
        print(f"You picked {decision}")

    # Flags
    inclusion_flags: list[str] = []
    exclusion_flags: list[str] = []

    # Minimums and Maximums
    # -1 will represent infinity
    min_population = 0
    max_population = -1
    min_gold = 0
    max_gold = -1
    min_power = 0
    max_power = -1

    # Event Name
    name = "Event Name"


# Function for adding a flag
def add_flag(flag_name: str):
    if flag_name not in user_flags:
        user_flags.append(flag_name)


event_list: list[Event] = []


# Function for adding event to event_list
def add_event(event: Event):
    event_list.append(event)


# Function that will only be called once
# ################################################
# Creates all the events
# ################################################
def make_events() -> list[Event]:
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

    # A Helping Hand
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

    # A fateful encounter
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
                    "Equipment is reforged, strengthing the ranks--at the cost of your treasury. "
                )
                util.red("[-100 GOLD] ")
                util.green("[+100 power]\n")
                gold -= 100
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
            util.orange("[Homeless Assasin] Tojiro, Heavenly Demon\n")
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
            util.red("I represent the First Nation. \n")
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
                util.red(f"[-{population} POPULATION] ")
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
                    "A weird decision. But Nevertheless, I shall trust your judgement.\n"
                )
                util.grey("The people are happy, and the colony grows. ")
                util.green("[+100 POPULATION]\n")
                population += 100

        event.effect = event_effect
        event.inclusion_flags = ["TUTORIAL_COMPLETE"]
        event.exclusion_flags = []
        event.weight = 1
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
                util.grey("Barbable picked Scissors \n")
                util.grey("Scissors beats Paper. You lost the round. \n")
                util.grey("Barable steals from your treasury. \n")
                util.grey("It is her prize for winning. ")
                util.red(f"[-{math.floor(gold*0.5 + 1)} GOLD]\n")
                gold -= math.floor(gold * 0.5 + 1)
            elif decision == "SCISSORS":
                util.grey("Barbable picked Rock \n")
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


# Call make_events()
make_events()

current_event: Event = Event()


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


def random_event():
    # Get list of available events
    unlocked_events = get_unlocked_events()
    # Initialize variable to hold sum of weights
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
            # Increment weight heap by the event's weight
            weight_heap += event.weight


def display_stats():
    util.purple(f"POPULATION: {population}, ")
    util.yellow(f"GOLD: {gold}, ")
    util.red(f"POWER: {power}\n")


def process_event():
    # Clear Terminal
    util.clear_terminal()
    # Display title at top
    util.display_title()
    # Display Stats
    display_stats()
    # Display name of event
    util.orange(f"~~~ < {current_event.name} > ~~~\n")
    # Display event synopsis
    current_event.synopsis()
    # Get players decision
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
    current_event.effect(decision)
    util.pause()


def game_loop():
    # Get random unlocked event
    global current_event
    current_event = random_event()
    # Process event + decision
    process_event()


def main():
    while True:
        game_loop()
        # Check if population is less than or equal to 0
        if population <= 0:
            # LOSS
            util.red("Your population has been eradicated.\n")
            util.red("Your kingdom has fallen. The colony is no more.\n")
            util.red("This is all your fault.\n")
            util.red("You lost. \n")
            # BREAK
            break
        # [ END ]


if __name__ == "__main__":
    main()
