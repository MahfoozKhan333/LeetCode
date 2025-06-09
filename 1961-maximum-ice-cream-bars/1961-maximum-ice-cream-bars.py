# from typing import List

class Solution:
    def maxIceCream(self, costs,coins):
        max_num = max(costs)
        count = [0] * (max_num + 1)
        
        for cost in costs:
            count[cost] += 1
        
        bars = 0
        for cost in range(len(count)):
            if count[cost] == 0:
                continue
            max_can_buy = min(count[cost], coins  // cost)
            bars += max_can_buy
            coins -= max_can_buy * cost
            if coins < cost:
                break
        
        return bars
