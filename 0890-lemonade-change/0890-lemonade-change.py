class Solution(object):
    def lemonadeChange(self, bills):
        if bills[0] != 5:
            return False
        fiveDoller=0
        tenDoller=0

        for x in bills:
            if x==5:
                fiveDoller+=1
            elif x== 10:
                if fiveDoller > 0:
                    fiveDoller-=1
                else:
                    return False
                tenDoller +=1
            else:
                if fiveDoller > 0 and tenDoller> 0:
                    fiveDoller-=1
                    tenDoller-=1
                elif fiveDoller >= 3:
                    fiveDoller -= 3
                else:
                    return False
            # print(fiveDoller, tenDoller)
        return True
        