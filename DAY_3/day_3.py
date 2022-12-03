import string

def task_1(priorities:dict):
    with open("input", "r") as file: 
        rucksacks = [ line.rstrip('\n') for line in file.readlines() ]
    sum_s = 0
    for rucksack in rucksacks:
        commons = {}
        compartment_len = int(len(rucksack)//2)
        compartment_1 = rucksack[0:compartment_len]
        compartment_2 = rucksack[compartment_len:]
        for item in compartment_1:
            if compartment_2.find(item) != -1 :
                commons[item] = priorities.get(item)
        sum_s += sum(commons.values())
    print(sum_s)
        

def task_2(priorities:dict):
    with open("input", "r") as file: 
        rucksacks = [ line.rstrip('\n') for line in file.readlines() ]
    groups = [ rucksacks[i:i+3] for i in range(0, len(rucksacks), 3 )]
    sum_s =0
    for group in groups: 
        commons = {}
        for item in group[0]:
                if group[1].find(item) != -1 and group[2].find(item) !=-1 :
                    commons[item] = priorities.get(item)
        sum_s += sum(commons.values())
    print(sum_s)


if __name__ == "__main__":
    priorities = dict(zip(string.ascii_letters, range(1, 53)))
    task_1(priorities)
    task_2(priorities)