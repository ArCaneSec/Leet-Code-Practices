class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if children > money:
            return -1

        eights = 0
        for child in range(1, children + 1):
            amount_left = money - 8
            if amount_left < children - child:
                return eights

            if amount_left == 4 and child + 1 == children:
                return eights
            eights += 1
            money = amount_left
        
        return eights if money == 0 else eights - 1 
    
print(Solution().distMoney(120, 3))