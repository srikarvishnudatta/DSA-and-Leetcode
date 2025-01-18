def evaluatePolishExpression(tokens:  list[int]):
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

def dailytemperatures(temps: list[int]) -> list[int]:
    res = [0] * len(temps)
    st = []
    for index, temp in enumerate(temps):
        while st and temp > st[-1][0]:
            stT, stI = st.pop()
            res[stI] = temp-stT
        st.append([temp, index])