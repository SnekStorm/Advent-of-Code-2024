def run():
    matches = []
    found = 0
    foundXmas = 0
    directions = [ [1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1] ]
    xmas = ["MS", "SM"]

    with open("input.txt") as f:
        for line in f:
            matches.append(list(line.strip('\n')))

    for row in range(len(matches)):
        for column in range(len(matches)):
            if(matches[row][column]) != 'X':
                continue

            for direction in directions:
                # Check if indexes exists
                if row+direction[0]*3 > len(matches)-1 or row+direction[0]*3 < 0:
                    continue
                if column+direction[1]*3 > len(matches)-1 or column+direction[1]*3 < 0:
                    continue

                if "XMAS" == matches[row][column] + matches[row + 1 * direction[0]][column + 1 * direction[1]] + matches[row + 2 * direction[0]][column + 2 * direction[1]] + matches[row + 3 * direction[0]][column + 3 * direction[1]]:
                    found += 1


    for row in range(1,len(matches)-1):
        for column in range(1,len(matches)-1):
            if(matches[row][column]) != 'A':
                continue

            if matches[row+1][column+1]+matches[row-1][column-1] in xmas:
                if matches[row-1][column+1]+matches[row+1][column-1] in xmas:
                    foundXmas +=1


    print(f'Nr of XMAS found: {found}')
    print(f'Nr of X-MAS found: {foundXmas}')

if __name__ == '__main__':
    run()