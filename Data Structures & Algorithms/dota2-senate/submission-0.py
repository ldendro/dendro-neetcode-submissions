class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = dire = 0
        for ltr in senate:
            if ltr == 'R':
                radiant += 1
            else:
                dire += 1

        idx = 0
        rbanned = dbanned = 0
        while radiant != 0 and dire != 0:
            if idx == len(senate):
                idx = 0
            if senate[idx] == 'R':
                if rbanned > 0:
                    rbanned -= 1
                else:
                    dbanned += 1
                    dire -= 1
            elif senate[idx] == 'D':
                if dbanned > 0:
                    dbanned -= 1
                else:
                    rbanned += 1
                    radiant -= 1
            idx += 1
        return 'Radiant' if dire == 0 else 'Dire'
                    