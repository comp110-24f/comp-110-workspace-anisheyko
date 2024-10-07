"""Practice with for loops and range"""

pets: list[str] = ["Louie", "Bo", "Bear"]
for names in pets:
    print(f"Good boy,{names}!")

names: list[str] = ["Alyssa", "Janet", "Vrinda"]
for idx in range(0, len(names)):
    print(f"{idx}: {names[idx]} ")
