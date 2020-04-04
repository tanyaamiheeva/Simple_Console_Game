from factory import DemigodsArmy, MonstersArmy


print('Choose which side are you on:')
print('Type 1 if you want to fight for Demigods')
print('Type 2 if you want to fight for Monsters')

n = int(input())

if n == 1:
    DemigodsArmy().recruit_human()
    DemigodsArmy().recruit_centaur()
    DemigodsArmy().recruit_cyclops()
    DemigodsArmy().recruit_dragon()
    DemigodsArmy().recruit_special_human()
else:
    MonstersArmy().recruit_human()
    MonstersArmy().recruit_special_human()
    MonstersArmy().recruit_dragon()
    MonstersArmy().recruit_cyclops()
    MonstersArmy().recruit_centaur()

