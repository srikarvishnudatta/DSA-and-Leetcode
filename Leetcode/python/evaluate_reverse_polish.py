def evalRPN(tokens: list[str]) -> int:
        st = []
        for token in tokens:
            if token=="+":
                pop1 = st.pop()
                pop2 = st.pop()
                result = pop2 + pop1
                st.append(result)
            elif token=="-":
                pop1 = st.pop()
                pop2 = st.pop()
                result = pop2 - pop1
                st.append(result)
            elif token=="*":
                pop1 = st.pop()
                pop2 = st.pop()
                result = pop2 * pop1
                st.append(result)
            elif token == "/":
                pop1 = st.pop()
                pop2 = st.pop()
                st.append(int(float(pop2) / pop1))
            else:
                st.append(int(token))
        return st.pop()