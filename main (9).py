import numpy

def print_floor(my_array):
    print(numpy.floor(my_array))

def print_ceil(my_array):
    print(numpy.ceil(my_array))

#The rint tool rounds to the nearest integer of input element-wise.
def print_rint(my_array):
    print(numpy.rint(my_array))

if __name__ == '__main__':
    
    #numpy.set_printoptions(precision=None, threshold=None, edgeitems=None, linewidth=None, suppress=None, nanstr=None, infstr=None, formatter=None, sign=None, floatmode=None, *, legacy=None) Set printing options.
    #These options determine the way floating point numbers, arrays and other NumPy objects are displayed.
#signstring, either ‘-‘, ‘+’, or ‘ ‘, optional
#Controls printing of the sign of floating-point types. If ‘+’, always print the sign of positive values. If ‘ ‘, always prints a space (whitespace character) in the sign position of positive values. If ‘-‘, omit the sign character of positive values. (default ‘-‘)

    numpy.set_printoptions(sign = ' ')
    my_list = list(map(float,input().split()))
    my_array = numpy.array(my_list)
    print_floor(my_array)
    print_ceil(my_array)
    print_rint(my_array)
