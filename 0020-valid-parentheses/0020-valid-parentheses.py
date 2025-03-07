class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        s_len = len(s)
        for i in range(s_len):
            if not st:
                st.append(s[i])
            else:
                if s[i] == ')' and st[-1] == '(':
                    st.pop()
                elif s[i] == ']' and st[-1] == '[':
                    st.pop()
                elif s[i] == '}' and st[-1] == '{':
                    st.pop()
                else:
                    st.append(s[i])

        return st == []