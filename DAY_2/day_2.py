

def count_strategy( strategy: dict):

    with open("input", "r") as file: 
        fights = [ fight.split() for fight in file.readlines() ]
        outcomes = []
        for fight in fights:
            elf_1 = fight[0]
            me = fight[1]
            # print(outcomes)
            if elf_1 == "A":
                if me == "X": 
                    outcomes.append(strategy.get(me) + 3)
                elif me == "Y":
                    outcomes.append(strategy.get(me) + 6)
                else:
                    outcomes.append(strategy.get(me))
            elif elf_1 == "B":
                if me == "X": 
                    outcomes.append(strategy.get(me))
                elif me == "Y":
                    outcomes.append(strategy.get(me) + 3)
                else:
                    outcomes.append(strategy.get(me) + 6)
            elif elf_1 == "C":
                if me == "X": 
                    outcomes.append(strategy.get(me) + 6)
                elif me == "Y":
                    outcomes.append(strategy.get(me))
                else:
                    outcomes.append(strategy.get(me)+3)
        print(sum(outcomes))

def part_2():
    with open("input", "r") as file: 
        fights = [ fight.split() for fight in file.readlines() ]
        outcomes = []
        for fight in fights:
            elf_1 = fight[0]
            me = fight[1]
            # print(outcomes)
            if me == "X":
                if elf_1 == "A":
                    outcomes.append(3)
                elif elf_1 == "B":
                    outcomes.append(1)
                else:
                    outcomes.append(2)

            elif me == "Y":
                if elf_1 == "A":
                    outcomes.append(1+3)
                elif elf_1 == "B":
                    outcomes.append(2+3)
                else:
                    outcomes.append(3+3)

            elif me == "Z":
                if elf_1 == "A":
                    outcomes.append(2 + 6)
                elif elf_1 == "B":
                    outcomes.append(3 + 6)
                else:
                    outcomes.append(1 + 6)
        print(sum(outcomes))    
            
        # print(fits)
    # sum(fights)
if __name__ == "__main__":
    strategy = {
        "A": 1,
        "B": 2,
        "C": 3,
        "X": 1,
        "Y": 2,
        "Z": 3,   
    }
    # wygrywajace
    # C X 
    # B Z
    # A Y
    # remisy 
    # A X
    # B Y
    # C Z
    # przegrywajace reszta
    count_strategy(strategy)
    part_2()