import sys
for x in range(1,11):
    for y in range(1,11):
        tymczasowa=x*y
        tymczasowa=str(tymczasowa)
        sys.stdout.write(tymczasowa+" ")
    sys.stdout.write('\n')