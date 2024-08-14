# Breaking Records

This Python script solves the "Breaking the Records" problem, which involves determining the number of times a player's season records for most and least points were broken during a series of games.

## Problem Description

Given a list of scores representing the points scored in each game of a season, this script calculates how many times the player breaks their record for the most points scored in a game and the number of times they break their record for the least points scored in a game.

## Input

- A list of integers representing the scores in each game.

## Output

- Two integers:
  - The first integer represents the number of times the maximum score record was broken.
  - The second integer represents the number of times the minimum score record was broken.

## Implementation

The `breakingRecords` function takes a list of scores as input and returns a tuple containing the number of times the maximum and minimum records were broken.

## Iterations

 #  [10, 5, 20, 20, 4, 5, 2, 25, 1]


    # Iteration Table:
    # | Iteration | Current Score | max_score | min_score | max_count | min_count | Action                           
    # |-----------|---------------|-----------|-----------|-----------|-----------|----------------------------------
    # | 1         | 5             | 10        | 5         | 0         | 1         | New min record set               
    # | 2         | 20            | 20        | 5         | 1         | 1         | New max record set               
    # | 3         | 20            | 20        | 5         | 1         | 1         | No change                        
    # | 4         | 4             | 20        | 4         | 1         | 2         | New min record set               
    # | 5         | 5             | 20        | 4         | 1         | 2         | No change                        
    # | 6         | 2             | 20        | 2         | 1         | 3         | New min record set               
    # | 7         | 25            | 25        | 2         | 2         | 3         | New max record set               
    # | 8         | 1             | 25        | 1         | 2         | 4         | New min record set  