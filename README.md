# DSO_Challenge3_Robotic_Autonomy-2023
This repo is my answer to the 2023 DSO Challege 3 - Robotic Autonomy. 

# The Challenge
A robot has to move from an initial position of [0,0] to a goal at [90, 50]. The map contains obstacles and terrain. The objective is to reach the goal with as little energy expended as possible. 

# TLDR
The robot takes the lowest cost action at each step without backtracking. The cost is a weighted sum of the control action and the distance to goal. The lowest recorded cost is 203.5685 [4dp] where the gains used are 4.5 and 1.0 for the distance to goal cost and control action cost respectively. An improvement that can be made is to allow the search to backtrack to the previous taken step when no optimal solution is found. 

# Resources
https://www.dtcareers.gov.sg/challenge/?utm_source=email&utm_medium=EDM&utm_campaign=ChallengeOfWits2023&utm_content=Challenge3-University
