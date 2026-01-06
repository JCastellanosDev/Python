from random import choice as ch
import os
import math 

def clear_screen():   
    os.system("clear" if os.name == "posix" else "cls")

planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]
random_planet = ch(planets, k=1)[0]

if random_planet == 'Mercury':
    radio = 2440
elif random_planet == 'Venus':
    radio = 6052
elif random_planet == 'Earth':
    radio = 6371        
elif random_planet == 'Mars':
    radio = 3390
elif random_planet == 'Saturn':
    radio = 58232  
else:
    print("Error: Planet not found")

print(f"The selected planet is: {random_planet}")
area = 4 * math.pi * (radio ** 2)
print(f"The surface area of {random_planet} is: {area:.2f} square meters")