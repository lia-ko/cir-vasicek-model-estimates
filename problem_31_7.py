import sys
import math


def get_required_number(msg):
    value = 0
    while True:
        result = input_number(msg)
        if not result[0]:
            print("This is not a numeric value")
        else:
            value = result[1]
            break

    return value

# normal CDF approximation
def normсdf(x):
    c1 = 49867347 * 10**-9
    c2 = 21141006 * 10**-9
    c3 = 3277626 * 10**-9
    c4 = 38004 * 10**-9
    c5 = 48891 * 10**-9
    c6 = 5383 * 10**-9
    z = abs(x)
    y = 1 - ((1 + c1 * z + c2 * z * z + c3 * z ** 3 + c4 * z ** 4 + c5 * z ** 5 + c6 * z ** 6) ** -16) / 2

    if x < 0:
        y = 1 - y
    return y


def input_number(msg):
    value = 0
    done = True

    try:
        raw_value = input(msg)
        if raw_value.upper() == "X":
            sys.exit()

        value = float(raw_value)
    except ValueError:
        done = False

    return done, value


def get_sigmap():
    result = (sigma/a)*(1-math.exp(-a*(S-T)))*math.sqrt((1-math.exp(-2*a*T))/(2*a))
    return result


def calc_option_vas():
    p_0_T = calc_vasicek(0, T)
    # print("p0T " + str(p_0_T))
    p_0_S = calc_vasicek(0, S)
    # print("p0S " + str(p_0_S))
    sp = get_sigmap()
    # print("sp " + str(sp))
    h = (1/sp)*math.log((L*p_0_S)/(p_0_T*K)) + sp/2
    # print("h " + str(h))
    # print("cdf " + str(normсdf(h)))
    result = L*p_0_S*normсdf(h)-K*p_0_T*normсdf(h-sp)

    return result


def b_vas(t, T):
    result = (1 - math.exp(-a*(T-t)))/a
    # print(result)
    return result


def a_vas(t, T):
    result = math.exp((b_vas(t, T) - T + t) * (b*a**2 - 0.5 * sigma**2)/a**2 - (sigma**2) * (b_vas(t, T)**2)/(4*a))
    # print(result)
    return result


def calc_vasicek(t, T):
    return a_vas(t, T)*math.exp(-b_vas(t, T) * r)


def calc_cir(t, T):
    return a_cir(t, T)*math.exp(-b_cir(t, T) * r)


if __name__ == "__main__":
    while True:
        print("-----------------")
        print("Problem 31.7")
        print("_________________\n")

        print("Please enter parameters for Vasicek model (X or x to terminate program):")
        a = get_required_number("Enter parameter a: ")
        b = get_required_number("Enter parameter b: ")
        sigma = get_required_number("Enter sigma: ")
        r = get_required_number("Enter initial short rate %: ")
        S = get_required_number("Enter bond maturity period in years: ")
        L = get_required_number("Enter principal bond value: ")
        T = get_required_number("Enter European call option term in years: ")
        K = get_required_number("Enter a strike price for European call option: ")

        r = r * 0.01

        price_vasicek = calc_option_vas()
        print("\n\nVasicek model bond option price estimate: " + str(price_vasicek) + "\n\n")

        more = input("Press Y or y to continue: ")
        if more.upper() != "Y":
            break
