import pandas as pd
import numpy as np
import math

class goal_finder():
    # coord = [x, y, z, g(n), h(n), f(n)]
    def __init__(s, gain): 
        s.map = pd.read_csv("Elevation.csv", index_col=0)
        s.goal = [90, 50, s.find_elevation(90, 50)]
        s.dist2goal_gain = gain
        s.control_cost_gain = 1.0
        s.start = [0, 0, s.find_elevation(0, 0), 
                   0, s.calc_dist2goal([0, 0, s.find_elevation(0,0)]), 
                   s.calc_total_cost([0, 0, s.find_elevation(0,0)],[0, 0, s.find_elevation(0,0)])]
        s.state_space = [s.start] # ordered

    def find_elevation(s, x, y):
        coulmn_key = str(int(x))
        row_index = y
        return s.map[coulmn_key][row_index]
    
    def calc_dist2goal(s, coord):
        # coord = [x, y, z, g(n), h(n), f(n)]
        dx = s.goal[0] - coord[0]
        dy = s.goal[1] - coord[1]
        dz = s.goal[2] - coord[2]
        norm = math.sqrt(dx**2+ dy**2+ dz**2)
        return norm

    def calc_step_cost(s, current_coord, next_coord):
        dx = next_coord[0] - current_coord[0]
        dy = next_coord[1] - current_coord[1]
        if next_coord[2] > current_coord[2]:
            dz = next_coord[2] - current_coord[2]
        else:
            dz = 0
        horizontal_cost = np.hypot(dx, dy)
        climbing_cost = 10 * dz
        return horizontal_cost + climbing_cost
    
    def calc_total_cost(s, current_coord, next_coord):
        control_cost = s.calc_step_cost(current_coord, next_coord)
        distance_cost = s.calc_dist2goal(next_coord)
        total_cost = s.control_cost_gain * control_cost + s.dist2goal_gain * distance_cost
        return total_cost
    
    def search(s, coord):
        # Returns a search space around coord
        # (x+1, y+1)
        # (x+1, y)
        # (x+1, y-1)
        # (x, y-1)
        # (x-1, y-1)
        # (x-1, y)
        # (x-1, y+1)
        # (x, y+1)
        search_space = []
        for i in range(-1, 2, 1):
            for j in range(-1, 2, 1):
                test_coord = np.array(coord)
                test_coord = list(test_coord + np.array([i, j, 0, 0, 0, 0]))
                test_coord[2] = s.find_elevation(test_coord[0],test_coord[1])
                step_cost = s.calc_step_cost(coord, test_coord)
                dist2goal = s.calc_dist2goal(test_coord)
                test_coord[3] = coord[3] + step_cost
                test_coord[4] = dist2goal
                test_coord[5] = s.calc_total_cost(coord, test_coord)
                search_space = s.insert_into_sorted_list(search_space, test_coord)
        return search_space


    def insert_into_sorted_list(s, a_list, variable):
        index_to_insert = 0
        sorted_list = a_list.copy()

        # Find the correct index to insert the variable while maintaining the sorted order
        while index_to_insert < len(sorted_list) and sorted_list[index_to_insert][5] < variable[5]:
            index_to_insert += 1

        # Insert the variable at the determined index
        sorted_list.insert(index_to_insert, variable)
        return sorted_list

    def run(s):
        count = 0
        stop = False
        while True:
            best_state = s.state_space[0]
            search_space = s.search(best_state)
            for search_count, state in enumerate(search_space):
                if state[5] < best_state[5]:
                    s.state_space = s.insert_into_sorted_list(s.state_space, state)
                    count = 0
                    # print(state)
                    break
            count += 1
            if count > 2:
                print(s.state_space)
                break
            if best_state[:2] == s.goal[:2]:
                print("SUCCESS")
                print(best_state)
                break