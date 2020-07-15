'''
    Rumtime:
        time: O(1) since only arithmatic logics are used and no loops
        space: O(1) since no extra space needed
    Analysis:
        Given: hour in [1, 12] and minute in [0, 59]
        Ask: return the angle difference between hour hand and minute hand, e.g.
        Input: hour = 12, minutes = 30
        Output: 165
        To accomplish this: simulate how these hands move in response to given time. for the 
        hour hand, for each hour increase, it rotate clockwise by 30 degree because it move 360 degree
        in a 12 hour period, so divide by 12 to get 30. for minute hand, samiliar caculations to find it
        moves 6 degree for each minute increases. The catch is the hour hand moves as the minute hand moves,
        to find how much the hour hand moves, we can think this way: when the minute hand move 360 degree, 
        it means 1 hour passes, and the hour hand will need to move 30 degree, so for 1 minute, the hour
        hand moves 30 * (minutes/60). the difference between two hands are the smaller number from 
        the difference of hour and minute hands, and 360 minus this difference
'''
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        h = 30. * (hour % 12) + (minutes % 60 ) / 2.
        m = (minutes % 60 ) * 6.
        
        diff = abs(h-m)
        
        return min(diff, 360 - diff)
