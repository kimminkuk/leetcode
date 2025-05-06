class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        st, ed = 0, 1        
        n = len(dominoes)
        if n <= 1:
            return dominoes      
            
        pre_set, next_set = "", ""
        ans = ""
        while ed < n:
            #if dominoes[st] == "L" or "R":
            #    pre_set = dominoes[st]
            pre_set = dominoes[st]
            next_set = dominoes[ed]
            
            if next_set == "L":
                if pre_set == "L":
                    ans += (ed-st)*"L"
                    st = ed
                    pre_set = next_set
                elif pre_set == "R":
                    l = (ed-st-1)
                    extra = l // 2
                    if l % 2 == 0:
                        ans += "R" + "R"*extra + "L"*extra
                    else:
                        ans += "R" + "R"*extra + "." + "L"*extra
                    st = ed
                    pre_set = next_set
                else: # pre_set is "."
                    ans += (ed-st)*"L"
                    st = ed
                    pre_set = next_set
                    
                    
            if next_set == "R":
                if pre_set == "R":
                    ans += (ed-st)*"R"
                    st = ed
                    pre_set = next_set
                elif pre_set == "L":
                    ans += "L" + (ed-st-1)*"."
                    st = ed
                    pre_set = next_set
                else:
                    ans += "." * (ed-st)
                    st = ed
                    pre_set = next_set                    
            ed += 1
        
        if st == ed - 1:
            ans += next_set
        else:
            #print(f"pre_set:{pre_set} st:{st} ed:{ed} ans:{ans}")
            if pre_set == "." or pre_set == "R":
                #print(f"11")
                ans += (ed - st) * pre_set
            elif pre_set == "L":
                #print(f"22")
                ans += "L" + (ed - st - 1) * "."
        return ans        