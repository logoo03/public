# from bisect import *
# from math import *
# from collections import Counter, defaultdict
from io import BytesIO, IOBase
import os, sys
try:
    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
    # noinspection PyUnresolvedReferences
    from debug.debug import Debug
    dbg = Debug().dbg
except ModuleNotFoundError:
    pass
# ----------------------------------------------------------------------------------------------------------------------


def main():
    case = int(input())

    def solve():
        la = int(input())
        a = list(map(int, input().split()))

        res = []
        if la % 2 != 0:
            a.insert(0, 0)
            la += 1
        for i in range(0, la, 2):
            x, y = a[i], a[i+1]
            res.extend([x, y] if x <= y else [y, x])

        for i in range(1, la):
            if res[i] < res[i-1]:
                print("NO")
                break
        else:  # usage of for(break)-else; keyword: for-else
            print("YES")

    while case:
        solve()
        case += -1


# ----------------------------------------------------------------------------------------------------------------------
def gcd(gcd_x, gcd_y):
    while gcd_y:
        gcd_x, gcd_y = gcd_y, gcd_x % gcd_y
    return gcd_x


def lcm(lcm_x, lcm_y):
    return lcm_x * lcm_y // gcd(lcm_x, lcm_y)


def isprime(integer_x):
    if integer_x <= 1:
        return False
    for i in range(2, int(integer_x ** 0.5) + 1):
        if integer_x % i == 0:
            return False
    return True


BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = 'x' in file.mode or 'r' not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self, **kwargs):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b'\n') + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode('ascii'))
        self.read = lambda: self.buffer.read().decode('ascii')
        self.readline = lambda: self.buffer.readline().decode('ascii')


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)


def input(): return sys.stdin.readline().rstrip('\r\n')


if __name__ == '__main__':
    main()
