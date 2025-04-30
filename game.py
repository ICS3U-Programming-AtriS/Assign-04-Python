#!/usr/bin/env python3
# Created By: Atri Sarker
# Date: April 29, 2025
# King of the Ants

# Import library for handling randomness
import random

population = 100
gold = 100
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
        if (gold <= self.min_population):
            return False
        if (gold <= self.min_gold):
            return False
        if (gold <= self.min_power):
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
        pass

    question: str = ""
    decisions: list[str] = []
    
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
    
    # Template event [Without Comments]
    def template_event():
        event = Event()
        def event_synopsis(self):
            pass
        event.synopsis = event_synopsis
        def event_effect(self, decision):
            pass
        event.effect = event_effect

current_event: Event = Event()
event_list: list[Event] = []

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
    # Generate a random number between 0 and sum of weights
    rand_num = random.randint(0, sum_of_weights)
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



def game_loop():
    # Get random unlocked event
    current_event = random_event()
    print(gold)


def main():
    game_loop()
    pass


if __name__ == "__main__":
    main()
