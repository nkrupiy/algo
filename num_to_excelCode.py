_dbg_=True
_dbg_=False

def prt(*s): print(s)
def dbg(*s):
    if _dbg_: prt(s)
def dbg_var(**vars): dbg(vars)
def _dbg(var, val): prt(f'{var} =', val)
def err(n: int): raise ValueError(f"Bad value for n = {n}")

def int2char(n: int) -> str:
    if n < -1: err(n)
    if n < 0: return ""
    return chr(ord('A') + n)

def num_to_excelCode(n: int) -> str:
    x = 26; s = 0
    r1 = n // x - 1
    if r1 >= x:
        l1 = num_to_excelCode(r1)
        s = 1
    r2 = n % x
    dbg_var(n=n, r1=r1, r2=r2)
    if not s:
        l1 = int2char(r1)
    l2 = int2char(r2)
    r = l1 + l2
    dbg(r)
    return r

def print_res(n):
    print(str(f'num_to_excelCode({n})=' + num_to_excelCode(n)))

def demo(FROM, NR):
    TO = FROM + NR
    for i in range(FROM, TO):
        print_res(i)

demo(0, 3)
demo(-2 + 26, 3)
demo(-2 + 26*26, 3)
demo(-2 + 26*26*26, 3)
