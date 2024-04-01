
def ask(var, value, evidence, bn):
    variables = bn.variable_names.copy()
    H = evidence.copy()
    H[var] = value
    notH = evidence.copy()
    notH[var] = not value
    check = list(set(bn.variable_names) - set(H.keys()))
    probHE = ask1(H, bn, check, variables)
    variables = bn.variable_names.copy()
    alpha = probHE + ask1(notH, bn, check, variables)
    pFinal = probHE/alpha
    return pFinal

def ask1(e, bn, check, variables):
    current = variables.pop(0)
    if current in check:
        if len(variables) > 0:
            eTrue = e.copy()
            eTrue[current] = True
            eFalse = e.copy()
            eFalse[current] = False
            v = bn.get_var(current)
            pTrue = v.probability(True, eTrue)
            pFalse = v.probability(False, eFalse)
            res = (pTrue * ask1(eTrue, bn, check, variables.copy())) + (pFalse * ask1(eFalse, bn, check, variables.copy()))
            return res
        else:
            return 1
    else:
        v = bn.get_var(current)
        p1 = v.probability(e[current], e)
    if len(variables) > 0:
        return p1 * ask1(e, bn, check, variables.copy())
    else:
        return p1
