#Daniel Ben Harush
#ID: 316152792

def my_func(x1, x2, x3):
    try:
        if(x1 + x2 + x3 == 0):
            return "Not a number – denominator equals zero"
        else:
            return (((x1 + x2 + x3) * (x2 + x3) * x3) / (x1 + x2 +x3))
    except:
        print("Error: parameters should be float")


def convert(hours, minutes):
    if(hours < 0 or minutes < 0):
        print("Input error!")
    else:
        return (hours * 60 * 60 + minutes * 60)

