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

def b_cir(t, T):
    result = 2*(math.exp(gamma*(T-t)) - 1)/((gamma + a)*(math.exp(gamma*(T-t)) - 1) + 2*gamma)
    return result

def a_cir(t, T):
    p = 2*a*a/sigma**2
    result = ((2*gamma*math.exp((a + gamma)*(T - t)*0.5))/((gamma + a)*(math.exp(gamma*(T-t)) - 1) + 2*gamma))**p
    return result

def b_vas(t, T):
    result = (1 - math.exp(-a*(T-t)))/a
#    print(result)
    return result

def a_vas(t, T):
    result = math.exp((b_vas(t, T) - T + t) * (b*a**2 - 0.5 * sigma**2)/a**2 - (sigma**2) * (b_vas(t, T)**2)/(4*a))
 #   print(result)
    return result

def calc_vasicek(t, T):
    return a_vas(t, T)*math.exp(-b_vas(t, T) * r)

def calc_cir(t, T):
    return a_cir(t, T)*math.exp(-b_cir(t, T) * r)

if __name__ == "__main__":
    while True:
        print("-----------------")
        print("Problem 31.6")
        print("_________________\n")

        print("Please enter parameters for Vasicek and CIR models (X or x to terminate program):")
        a = get_required_number("Enter parameter a: ")
        b = get_required_number("Enter parameter b: ")
        r = get_required_number("Enter initial short rate %: ")
        dT = get_required_number("Enter bond maturity period in years: ")

        #Vasicek model
        r = r * 0.01
        sigma = 0.02
        t = 1
        T = 1 + dT

        price_vasicek = calc_vasicek(t, T)
        print("\n\nVasicek model bond price estimate: " + str(price_vasicek))

        #CIR Model
        sigma = 0.02/math.sqrt(r)
        gamma = math.sqrt(a**2 + 2*sigma**2)

        price_cir = calc_cir(t, T)
        print("CIR model bond price estimate: " + str(price_cir) + "\n\n")

        more = input("Press Y or y to continue: ")
        if more.upper() != "Y":
            break


