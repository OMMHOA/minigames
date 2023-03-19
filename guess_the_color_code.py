#!/usr/bin/env python3
import random

colors = ['r', 'g', 'b']
slots = 5
tries = 10

solution = []
for _ in range(slots):
  randindex = random.randrange(len(colors))
  solution.append(colors[randindex])

# print(solution)
resolved = False
tri = 0
print(f"Guess the color code. You've got {slots} slots, {tries} tries and the following possible colors: {colors}")
print("Enter your solution with coma separated values.")
while not resolved and tri < tries:
  tri += 1
  response = input(f"#{tri} Your guess: ").split(',')
  correct_in_good_place = 0
  correct_in_bad_place = 0
  found = list(solution)
  rest = []
  for i, e in enumerate(response):
    if solution[i] == e:
      correct_in_good_place += 1
      found.remove(e)
    else:
      rest.append(e)
  for e in found:
    if e in rest:
      rest.remove(e)
      correct_in_bad_place += 1
  print(f"Correct: {correct_in_good_place}; Good color: {correct_in_bad_place}; Miss: {slots - correct_in_good_place - correct_in_bad_place}")
  if correct_in_good_place == slots:
    resolved = True

if resolved:
  print(f"Congratulations!! You guessed it in {tri} tries!")
else:
  print("Game over")
print(f"Solution was: {solution}")

