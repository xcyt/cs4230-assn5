from . import computetriangle

def main():
    result = ''
    while True:
        resp = input('Enter a filename: ')
        try:     
            f = open(resp, 'r')
        except (FileNotFoundError, IOError):
            print("Wrong file or file path")
        else:
            break

    for x in f:
        if '#' in x:
            x = x.rstrip('\n')
            print(x)
        else:
            ct = computetriangle.ComputeTriangle()
            s1,s2,s3 = sorted([int(x) for x in x.rstrip('\n').split(' ')])
            result = ct.compute_triangle(s1, s2, s3)
            print(f'{s1}, {s2}, {s3} - {result}')
    f.close()

if __name__ == "__main__":
    main()
