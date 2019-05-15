import os
import random
import time

try:
    start = time.time()
    #Variables for dice numbers
    N1 = 0
    N2 = 0
    N3 = 0
    N4 = 0
    N5 = 0
    N6 = 0
    N7 = 0
    N8 = 0
    N9 = 0
    N10 = 0
    N11 = 0
    N12 = 0
    PN1 = 0
    PN2 = 0
    PN3 = 0
    PN4 = 0
    PN5 = 0
    PN6 = 0
    PN7 = 0
    PN8 = 0
    PN9 = 0
    PN10 = 0
    PN11 = 0
    PN12 = 0
    TH = 0 #Number of dice threw
    Time = 0 #Time to wait between turns

    while True:

        #Other variables
        D1 = random.randrange(1,7) #Generate a number between 1 and 6
        D2 = random.randrange(1,7) #Generate a number between 1 and 6
        D1D2 = D1 + D2 #Add D1 and D2
        TH = TH + 1

        if D1D2 == 1:
            N1 = N1 + 1
            PN1 = (N1 / TH)*100
            print(f'Turn Nº: {TH} || Numbers: {D1D2} || Dice 1: {D1} || Dice 2: {D2} || Times: {N1} || Probability: {int(PN1)}%')
        if D1D2 == 2:
            N2 = N2 + 1
            PN2 = (N2 / TH)*100
            print(f'Turn Nº: {TH} || Numbers: {D1D2} || Dice 1: {D1} || Dice 2: {D2} || Times: {N2} || Probability: {int(PN2)}%')
        if D1D2 == 3:
            N3 = N3 + 1
            PN3 = (N3 / TH)*100
            print(f'Turn Nº: {TH} || Numbers: {D1D2} || Dice 1: {D1} || Dice 2: {D2} || Times: {N3} || Probability: {int(PN3)}%')
        if D1D2 == 4:
            N4 = N4 + 1
            PN4 = (N4 / TH)*100
            print(f'Turn Nº: {TH} || Numbers: {D1D2} || Dice 1: {D1} || Dice 2: {D2} || Times: {N4} || Probability: {int(PN4)}%')
        if D1D2 == 5:
            N5 = N5 + 1
            PN5 = (N5 / TH)*100
            print(f'Turn Nº: {TH} || Numbers: {D1D2} || Dice 1: {D1} || Dice 2: {D2} || Times: {N5} || Probability: {int(PN5)}%')
        if D1D2 == 6:
            N6 = N6 + 1
            PN6 = (N6 / TH)*100
            print(f'Turn Nº: {TH} || Numbers: {D1D2} || Dice 1: {D1} || Dice 2: {D2} || Times: {N6} || Probability: {int(PN6)}%')
        if D1D2 == 7:
            N7 = N7 + 1
            PN7 = (N7 / TH)*100
            print(f'Turn Nº: {TH} || Numbers: {D1D2} || Dice 1: {D1} || Dice 2: {D2} || Times: {N7} || Probability: {int(PN7)}%')
        if D1D2 == 8:
            N8 = N8 + 1
            PN8 = (N8 / TH)*100
            print(f'Turn Nº: {TH} || Numbers: {D1D2} || Dice 1: {D1} || Dice 2: {D2} || Times: {N8} || Probability: {int(PN8)}%')
        if D1D2 == 9:
            N9 = N9 + 1
            PN9 = (N9 / TH)*100
            print(f'Turn Nº: {TH} || Numbers: {D1D2} || Dice 1: {D1} || Dice 2: {D2} || Times: {N9} || Probability: {int(PN9)}%')
        if D1D2 == 10:
            N10 = N10 + 1
            PN10 = (N10 / TH)*100
            print(f'Turn Nº: {TH} || Numbers: {D1D2} || Dice 1: {D1} || Dice 2: {D2} || Times: {N10} || Probability: {int(PN10)}%')
        if D1D2 == 11:
            N11 = N11 + 1
            PN11 = (N11 / TH)*100
            print(f'Turn Nº: {TH} || Numbers: {D1D2} || Dice 1: {D1} || Dice 2: {D2} || Times: {N11} || Probability: {int(PN11)}%')
        if D1D2 == 12:
            N12 = N12 + 1
            PN12 = (N12 / TH)*100
            print(f'Turn8 Nº: {TH} || Numbers: {D1D2} || Dice 1: {D1} || Dice 2: {D2} || Times: {N12} || Probability: {int(PN12)}%')
        time.sleep(Time)

except KeyboardInterrupt:
    end = time.time()
    TT = end - start
    print()
    print('-------------------------------------------------------------------------------')
    print(f'Turn Nº: {TH} || Numbers: 1 || Times: {N1} || Probability: {int(PN1)}%')
    print(f'Turn Nº: {TH} || Numbers: 2 || Times: {N2} || Probability: {int(PN2)}%')
    print(f'Turn Nº: {TH} || Numbers: 3 || Times: {N3} || Probability: {int(PN3)}%')
    print(f'Turn Nº: {TH} || Numbers: 4 || Times: {N4} || Probability: {int(PN4)}%')
    print(f'Turn Nº: {TH} || Numbers: 5 || Times: {N5} || Probability: {int(PN5)}%')
    print(f'Turn Nº: {TH} || Numbers: 6 || Times: {N6} || Probability: {int(PN6)}%')
    print(f'Turn Nº: {TH} || Numbers: 7 || Times: {N7} || Probability: {int(PN7)}%')
    print(f'Turn Nº: {TH} || Numbers: 8 || Times: {N8} || Probability: {int(PN8)}%')
    print(f'Turn Nº: {TH} || Numbers: 9 || Times: {N9} || Probability: {int(PN9)}%')
    print(f'Turn Nº: {TH} || Numbers: 10 || Times: {N10} || Probability: {int(PN10)}%')
    print(f'Turn Nº: {TH} || Numbers: 11 || Times: {N11} || Probability: {int(PN11)}%')
    print(f'Turn8 Nº: {TH} || Numbers: 12 || Times: {N12} || Probability: {int(PN12)}%')
    print(f'Time elapsed: {int(TT)}s')
    print('-------------------------------------------------------------------------------')
