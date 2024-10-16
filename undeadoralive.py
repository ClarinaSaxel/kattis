i=input()
print('double agent' if ':(' in i and ':)' in i else 'undead' if ':(' in i else 'alive' if ':)' in i else 'machine')