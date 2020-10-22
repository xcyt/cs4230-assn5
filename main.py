def computetriagle(s1,s2,s3):
    if s1 + s2 > s3:
        if s1 == s2 and s2 == s3:
            return 'Equallateral Triangle'
        if s1 == s2 or s2 == s3 or s1 == s3:
            return 'Isosolese Triangle'     
        return 'Scalene Triagle'    
    return 'Not a Triangle'

def main():
    result = ''
    #resp = input('Enter a filename: ')
    #f = open(resp, 'r')
    f = open('a5.txt', 'r')
    for x in f:
        if '#' in x:
            x = x.rstrip('\n')
            print(x)
        else:
            s1,s2,s3 = sorted([int(x) for x in x.rstrip('\n').split(' ')])
            result = computetriagle(s1, s2, s3)
            print(f'{s1}, {s2}, {s3} - {result}')

if __name__ == "__main__":
    main()
