
def count_elves_calories(dir:str, elves_count:int):
    elves_calories = []
    with open( dir, "r") as file:
        elf_candies = []
        for line in file.readlines():
            if len(line) == 1:
                elves_calories.append(sum(elf_candies))
                elf_candies = []
            else:
                elf_candies.append(int(line))
    sorted_elves = sorted(elves_calories, reverse=True)
    print(sorted_elves[:elves_count])

if __name__ =="__main__":
    count_elves_calories("input", 1)
    count_elves_calories("input", 3)