def len_longest_chain(chain_pairs):
    s = sorted(chain_pairs)
    last_chain = []
    first_chain = []
    count = 0
    for i in s:
        last_chain.append(i[1])
        first_chain.append(i[0])
    first_chain.pop(0)
    for j in last_chain:
        for i in first_chain:
            if j >= i:
                count += 1 
        return len(chain_pairs) - count
        