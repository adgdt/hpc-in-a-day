import numpy

def main():
    data = numpy.loadtxt("output",delimiter=",")
    values = numpy.mean(data, axis=0)
    print(values)

if __name__ == '__main__':
   main()
