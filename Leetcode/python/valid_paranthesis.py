def isValid(s: str) -> bool:
        st = []
        for char in s:
            if(char == "(" or char == "{" or char=="["):
                st.append(char)
            else:
                if len(st)==0: return False
                if char == ")":
                    if st[-1] != "(": return False
                elif char == "]":
                    if st[-1] != "[": return False
                else: 
                    if st[-1] != "{": return False
                st.pop()
        return len(st)==0