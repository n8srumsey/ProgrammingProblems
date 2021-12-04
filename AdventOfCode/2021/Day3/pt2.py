data_input = "./input.txt"

with open(data_input) as f:
    data = [l.rstrip("\n") for l in f.readlines()]


def get_gamma_epsilon(data_in):
    cols = [[] for _ in range(len(data_in[0]))]
    for l in data_in:
        for i, c in enumerate(l):
            cols[i].append(c)
    columns = ["".join(cols[i]) for i in range(len(cols))]
    gamma = ""
    epsilon = ""
    for c in columns:
        freq_0 = 0
        freq_1 = 0
        
        for s in c:
            if s == "1":
                freq_1 += 1
            else: 
                freq_0 += 1
        
        if freq_0 > freq_1:
            gamma += "0"
            epsilon += "1"
        elif freq_0 < freq_1:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "1"
            epsilon += "0"
    return gamma, epsilon

def oxy_rating(col: int, inpt):
    gamma, _ = get_gamma_epsilon(inpt)
    good = []
    for b in inpt:
        if b[col] == gamma[col]:
            good.append(b)        
    if len(good) != 1 and col + 1 != len(gamma) :
        return oxy_rating(col + 1, good)
    return good[0]        
    
def co2_rating(col: int, inpt):
    _, epsilon = get_gamma_epsilon(inpt)
    good = []
    for b in inpt:
        if b[col] == epsilon[col]:
            good.append(b)        
    if len(good) != 1 and col + 1 != len(epsilon):
        return co2_rating(col + 1, good)
    return good[0]

if __name__ == '__main__':
    oxy = int(oxy_rating(0, data), 2)
    co2 = int(co2_rating(0, data), 2)
    print(oxy, co2, co2*oxy)