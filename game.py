#!/usr/bin/env python3
# Created By: Atri Sarker
# Date: April 29, 2025
# King of the Ants

# Class for Game
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
    weight = 1

    def synopsis(self):
        pass

    question: str = ""
    decisions: list[str] = []
    
    def effect(self, decision):
        print(f"You Picked {decision}")
    
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




def game_loop():
    print(gold)


def main():
    game_loop()
    pass


if __name__ == "__main__":
    main()
