class InvalidInputError(Exception):
    pass

while True:
    m_s = input()

    if m_s == "f":
        print("Fim...")
        break
    elif not len(m_s)==5:
        raise InvalidInputError("Input Inválido")
    elif (m_s[2] ==" ") and (m_s[0].isalpha())and (m_s[3].isalpha()) and (m_s[1].isnumeric()) and (m_s[4].isnumeric()):
        sx,sy = (ord(m_s[0])-96, int(m_s[1]))
        fx,fy = (ord(m_s[3])-96, int(m_s[4]))

        if sx<0 or fx<0 or sx>8 or fx>8:
            raise InvalidInputError("Input Inválido")

        move = (fx-sx, fy-sy)

        if move in [( 2, 1), ( 2,-1), (-2, 1), (-2,-1), ( 1, 2), ( 1,-2), (-1, 2), (-1,-2)]:
            print("VÁLIDO")
        else:
            print("INVÁLIDO")
    else:
        raise InvalidInputError("Input Inválido")