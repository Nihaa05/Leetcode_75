class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        #initialize two deques for radiant and dire senators
        radiant, dire = deque(),deque()
        for i in range(n):
            #append index of senate to corresponding deque
            if senate[i] == 'R':
                radiant.append(i)
            else:
                dire.append(i)
        while radiant and dire:
            # if the radiant senator comes before the dire senator, radiant gets to act
            if radiant[0] <dire[0]:
                radiant.append(radiant[0] + n)
            else:
                # else, dire gets to act
                dire.append(dire[0] + n)
            # the senator who acted bans the opposing senator who comes first
            radiant.popleft()
            dire.popleft()
        #when one of the parties is empty, the other party wins
        return "Radiant" if radiant else "Dire"