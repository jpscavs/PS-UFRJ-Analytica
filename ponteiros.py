while True:
    t_s = input()

    if t_s == "f":
        print("Fim...")
        break
    elif not len(t_s)==5:
        print("Input inválido")
    elif (t_s[2] ==":") and (t_s[:2].isnumeric()) and (t_s[3:].isnumeric()):
        h = int(t_s[:2])
        m = int(t_s[3:])

        if h>24 or m>60:
            print("Input inválido")

        h = (h % 12)/12 * 360
        m = m/60 * 360

        r1 = max(h,m) - min(h,m)

        r2 = min(m,h) - (max(m,h)-360)

        print("O menor ângulo é de", str(round(min(r1,r2)))+"°")


    else:
        print("Input inválido")