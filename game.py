#!/usr/bin/env python3
# Created By: Atri Sarker
# Date: April 29, 2025
# King of the Ants

# Import library for handling randomness
import random
# Import util.py, used for input+output
import util

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
        if (gold < self.min_population):
            return False
        if (gold < self.min_gold):
            return False
        if (gold < self.min_power):
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
# Creates all the events
def make_events() -> list[Event]:
    # Template event [With Comments]
    def template_event_with_comments():
        # Instantiate new event
        event = Event()
        # Define Synopsis
        def event_synopsis(self):
            pass
        # Set event's synopsis to defined function
        event.synopsis = event_synopsis
        # Set and Define Effect
        def event_effect(self, decision):
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
        def event_synopsis(self):
            pass
        event.synopsis = event_synopsis
        def event_effect(self, decision):
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
            util.blue("The colony awaits your command, and your wisdom is needed now more than ever.\n")
        event.synopsis = event_synopsis
        event.question = "Do you understand your role, my liege? (yes,no): "
        event.decisions = ["YES", "NO"]
        def event_effect(decision):
            util.blue("[ROYAL ADVISOR] Vexel\n")
            if decision == "YES":
                util.blue("Excellent, Your Majesty.\n")
                util.blue("Let's continue.\n")
            elif decision == "NO":
                util.blue("Ah, a jest, perhaps?\n")
                util.blue("No matter—your instincts shall guide you, as they always have.\n")
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
            util.blue("This is the most important pillar and must be upheld at all times\n")
            util.blue("Without it, our goal, is nothing but a lofty dream.\n")
            util.blue("\n")
            util.blue("Second: *")
            util.yellow("GOLD")
            util.blue("*. The foundation of our economy. ")
            util.blue("It funds our expansion, our armies, and the future of the colony.\n")
            util.blue("\n")
            util.blue("Third: *")
            util.red("POWER")
            util.blue("*. The measure of your might. When battle comes, it is this that determines victory or defeat.\n")

            util.blue("Every decision you make shall shape these forces. ")
            util.blue("Balance them wisely, for the fate of the empire lies in your hands.\n")



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
            util.grey("you notice a fellow ant that is trapped under a slump of mashed banana.\n")
            util.blue("He begs for a helping hand.\n")
        event.synopsis = event_synopsis
        event.question = "What do you decide to do? (help,kill,ignore): "
        event.decisions = ["HELP", "KILL", "IGNORE"]
        def event_effect(decision):
            global population
            global gold
            global power
            if decision == "HELP":
                util.blue("Thank you, Your Majesty.\n")
                util.blue("He gifts you a pleasant alm.")
                util.green("[+20 GOLD]\n")
                gold += 20
            elif decision == "KILL":
                util.red("WEAKNESS IS NOT TOLERATED IN THIS KINGDOM! ")
                util.red("[-1 POPULATION] ")
                population -= 1
                util.green("[+10 POWER]\n")
                power += 10
                util.grey("Bystanders watch in schock as you ransack the remaining parts of his dead body. ")
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
        if (min_bound <= rand_num <= max_bound):
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
    decision = util.get_decision(current_event.question, 
                                 current_event.decisions)
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


if __name__ == "__main__":
    main()
