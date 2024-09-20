Original Code source: https://github.com/BitPatty/FFXRandomizer

Changed some stuff from the original randomizer:

You now cannot choose to opt out for stat randomization, but you can now choose between shufflizing (like the original randomizer did) or randomizing stats.

Choosing to Randomize will result in every possbile stat being scattered across the sphere grid with the same weight.

This will drastically lower the amount of overall HP nodes, since they have by far the highest weight on the original grid. 

Therefore, HP+300 nodes, which aren´t usually present, have been added to the pool with the same weight as all other nodes.

To get a feeling for how the grid will change (Standard):

Usually there are 507 stat nodes at the start of the game. 97!!! of those are HP+200 nodes.

Before adding HP+300, there were 35 different stat nodes on the standard grid. This means, every stat has an estimated count of ~14!

Thats the amount of Magic+3 nodes that are usually present!

Now with HP+300 included, there are 36 different stats on the standard grid, which still equates to an estimate of pretty exactly 14 of each stat, but now with 14 HP+200 and 14 HP+300 nodes, which is still not a lot, but its a randomizer after all.

You have the following options for ability-randomization:

-None (Abilites aren´t randomized)

-Shuffle (Abilities are in the same spots, but shufflized)

-Scatter (Abilities are in random positions on the grid)

To use, open _includes/generator.html in your browser  
