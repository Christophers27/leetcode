class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        switch1, switch2 = "", ""
        switched = False

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if switch1 == switch2 == "":
                    switch1 = s2[i]
                    switch2 = s1[i]
                elif not switched and s1[i] == switch1 and s2[i] == switch2:
                    switched = True
                else:
                    return False

        if switch1 != "" and not switched:
            return False

        return True
