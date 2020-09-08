def main():
    cost_m2 = float(input('Enter cost of 1^2 meter:', ))
    height = float(input('Enter height:', ))
    width = float(input('Enter width:', ))
    print(find_floor_cost(cost_m2, height, width))


def find_floor_cost(cost_m2=0, height=0.0, width=0.0):
    area = height * width
    cost_of_all = area * cost_m2
    return cost_of_all


if __name__ == "__main__":
    main()
