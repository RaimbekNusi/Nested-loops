# Nested loops

## Description 

Loops can be nested in Python, as they can with other programming languages. A nested loop is a loop that occurs within another loop, structurally similar to nested if statements.

## Problem description

Pikachu is surrounded by pesky Gengars! Will Pikachu be able to defeat all the ghosts, or will their numbers prove too great for our hero? You must write a program to answer this question.

When your program starts, allow the user to input the number of Gengars that are attacking Pikachu (you may assume the user enters a positive number). 

Then, you must simulate a series of battles between Pikachu and a Gengar. Initially, Pikachu has 35 health, but he may lose health during the battles, and if he ever runs out of health, he faints!

The Gengars will attack one at a time, and the rules for the battle simulation are as follows. Note that you will definitely need to import Python’s random module, as there is luck in the simulation.
- The Gengar attacks first. It has a 50% chance to hit Pikachu (Hint: Use the random() function to generate a random float between 0 and 1, then check if that float is less than 0.5). If the Gengar hits, it will randomly deal either 1, 2, or 3 damage to Pikachu.
- Then Pikachu attacks. Pikachu has a 60% chance to hit the Gengar. If he does, he will defeat the ghost.

The ghosts will attack in turn until either they are all defeated, or Pikachu faints. When that happens, print out a message that describes the outcome.

- If Pikachu defeated all the Gengars, print out that he triumped and how much health he has left
- If Pikachu fainted, print out how many of the Gengars he managed to defeat.
