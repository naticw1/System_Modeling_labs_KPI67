import generators

intervals = 15
AMOUNT = 10_000

# for first
LAMBDA = 15

# for second
A_2 = 5
SIGMA = 8

# for third
A_3 = pow(5, 10)
C = pow(2, 10)




GENERATOR = 3

def main():
    match GENERATOR:
        case 1: gen_result = generators.gen_first.GeneratorFirst(AMOUNT, intervals, LAMBDA)
        case 2: gen_result = generators.gen_second.GeneratorSecond(AMOUNT, intervals, A_2, SIGMA)
        case 3: gen_result = generators.gen_third.GeneratorThird(AMOUNT, intervals, A_3, C)
        case _: return
    gen_result.validate()

if __name__ == "__main__":
    main()