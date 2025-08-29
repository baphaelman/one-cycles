# One-Cycles
My attempt to answer the question "how often do you only need to memorize a single cycle when solving the edges of a Rubik's Cube blindfolded using [Old Pochmann's algorithm](https://www.speedcubereview.com/blind-solving-algorithms.html)?"

See [this article](https://www.raphaelbajet.com/single-cycles) motivating the equations I use to solve the problem.

The first functions compute a simpler case, without considering edge orientation, both through brute force (testing every permutation) and calculation.
The last section is the more complicated case for a real cube, and hard_prob(12) gives the final answer of ~14.4%
