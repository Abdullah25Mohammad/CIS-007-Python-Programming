#6.9
#Conversions between feet and meters
#Abdullah Mohammad
#1/13/23


def footToMeter(foot):
    meter = 0.305 * foot
    return format(meter, '.3f')

def meterToFoot(meter):
    foot = meter / 0.305
    return format(foot, '.3f')

def main():
    feet = 1.0
    meters = 20.0
    print("Feet \t Meters  |  Meters \t Feet \n")
    for i in range(1,11):        
        print(feet, '\t', footToMeter(feet), "\t | ", meters, '\t', meterToFoot(meters))
        feet += 1
        meters += 5


main()
