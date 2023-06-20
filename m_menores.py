def m_menores(V, m):
    if m < 0 or m > len(V):
        return []

    # preenche todos os elementos do vetor com infinito
    m_menores = [float('inf')] * m
    # [-3, -1, -1, 0]

    for num in V:  # num = -1
        for i in range(m):  # i = 0
            if num < m_menores[i]:
                m_menores.insert(i, num)
                m_menores.pop()
                break

    return m_menores


print(m_menores([-3, -1, 0, 0, 10, -1, 6, 5, 6], 4))
