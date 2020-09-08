def main():
    file = open("file.txt", encoding="utf-8")
    cost_finder(file)


def cost_finder(file):
    w_h = file.readline()
    cost = float(file.readline())
    m_2 = float(w_h.split(",")[0]) + float(w_h.split(",")[1])
    total_cost = m_2 * cost
    print("Square metre: " + str(m_2))
    print("Total cost: " + str(total_cost))


if __name__ == "__main__":
    main()
