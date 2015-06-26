

# 1
def findit(doop):
    the_list = []
    for i in range(0, doop):
        three = (i % 3) == 0
        five = (i % 5) == 0
        if three or five:
            the_list.append(i)
    return sum(the_list)


#2
def fib(i):
    first = 1
    sec = 2
    new = 0
    the_list = [1, 2]
    evens = [2]
    while new <= i:
        new = first + sec
        the_list.append(new)
        if new % 2 == 0:
            evens.append(new)
        first = sec
        sec = new
    return sum(evens)


#3
def factors(x):
    """
    Returns list of factors of a number not including 1,
    and including the number.
    """
    # first find list of factors
    factors = []
    for n in range(2, x + 1):
        if x % n == 0:
            factors.append(n)
    return factors


def is_prime(num):
    "Is num prime?"
    if num == 1:
        return False
    for r in range(2, num):
        if (num % r) is 0:
            return False
    return True


def prime_factors(num):
    facts = factors(num)
    primes = []
    for n in facts:
        if is_prime(n):
            primes.append(n)
    return primes


def factors2(x):
    """
    Returns list of factors of a number not including 1,
    and including the number.
    """
    # first find list of factors
    factors = []
    for n in range(2, x + 1):
        if x % n == 0:
            print(n)


def factors(x):
    factors = []
    divisor = 2
    while finished is False:
        if (x % divisor) == 0:
            factors.append(divisor)
            x = x / divisor
        divisor += 1
"""
Factoring:

Simplest method:
n is number to factor.
Go through every number from 2 to n checking for remainder.
However for large n, this is a problem.

Second method:
Start by making target = n
Check every number m from 2 to target.
Each time you find a match, target = target / m
This is much better.

But what about huge numbers? Is there any way to reduce the time?

Here is a thought:
    Only explore the space from 2 to the square root.
"""


#4
# Check every number multiplying
# 100-999 * 100-999 = 808201 possibilites.


def pal(num):
    new = ""
    snum = str(num)
    for n in snum:
        new = n + new
    reverse = int(new)
    if num == reverse:
        return True
    else:
        return False


def generate():
    pal_list = []
    for x in range(100, 1000):
        for y in range(100, 1000):
            thing = x * y
            if pal(thing):
                pal_list.append(thing)
    return pal_list

generate()


#5
def smallestmult(f):
    n = 1
    test = True
    while True:
        for z in range(1, f + 1):
            if n % z != 0:
                test = False
                break
        if test is True:
            return n
        test = True
        n += 1

#6:


def one(n):
    result = 0
    for p in range(1, n + 1):
        result = result + (p * p)
    return result


def two(n):
    result = 0
    for p in range(1, n + 1):
        result = result + p
    result = result * result
    return result


def answer(num):
    return (two(num) - one(num))


#7
def is_prime(num):
    "Is num prime?"
    if num == 1:
        return False
    for r in range(2, num):
        if (num % r) == 0:
            return False
    return True


def findit(num):
    total = 0
    n = 2
    while True:
        if is_prime(n):
            total += 1
        if total == num:
            return n
        n += 1

#8
mystring = (
"73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450")


def search(thing=mystring):
    ans = 1
    biggest = 0
    for n in range(0, len(thing) - 5):
        for m in range(0, 5):
            ans = ans * int(thing[n + m])
        if ans > biggest:
            biggest = ans
        ans = 1
    return biggest


#9
def findit(num=1000):
    for c in range(1, num - 1):
        for a in range(1, num - c):
            b = num - c - a
            if a ** 2 + b ** 2 == c ** 2:
                print(a, b, c, a + b + c)

# 200 375 425
# a * b * c = 31875000


#10
def is_prime1(num):
    "Is num prime?"
    if num == 1:
        return False
    for r in range(2, num):
        if (num % r) == 0:
            return False
    return True


def is_prime2(num):
    "Is num prime? Much faster than is_prime1()."
    if num == 1:
        return False
    rt = int(num ** .5)
    for r in range(2, rt + 1):
        if (num % r) == 0:
            return False
    return True


def test(num=10000):
    count = 0
    for x in range(1, num + 1):
        if is_prime2(x):
            count = count + x
    return count

#12
numstring = (
"08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 \
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 \
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 \
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 \
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 \
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 \
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 \
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 \
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 \
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 \
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 \
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 \
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 \
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 \
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 \
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 \
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 \
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 \
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 \
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48")

def doit(numstring=numstring):
    arr = np.zeros((20, 20))
    width = 20
    numsplit = numstring.split(" ")
    row = 0
    col = 0
    for x in numsplit:
        arr[row, col] = int(x)
        col += 1
        if col == 20:
            row += 1
            col = 0
    return arr

# put the string into an array
thing = doit()

# First find highest going across.

def horz(arr=thing, trans=False):
    "Select trans=True to find trasposed values."
    num = 4
    result = []
    if trans is True:
        arr = np.swapaxes(arr, 0 ,1)
    arrwidth = np.shape(arr)[0]
    arrheight = np.shape(arr)[1]
    for y in range(0, arrheight):
        for x in range(0, arrwidth - num + 1):
            # print(arr[y,x],arr[y,x+1],arr[y,x+2],arr[y,x+3])
            result.append(arr[y,x]*arr[y,x+1]*arr[y,x+2]*arr[y,x+3])
    return result

largest vert: 51267216
largest hor: 48477312


for diagonals, scan in the same way. The simplest way to keep things
in bounds is to make a try except check.

def diag1(arr=thing, trans=False):
    "Select trans=True to find trasposed values."
    num = 4
    result = []
    if trans is True:
        arr = np.swapaxes(arr, 0 ,1)
    arrwidth = np.shape(arr)[0]
    arrheight = np.shape(arr)[1]
    for y in range(0, arrheight):
        for x in range(0, arrwidth):
            try:
                value = arr[y,x]*arr[y+1,x+1]*arr[y+2,x+2]*arr[y+3,x+3]
                result.append(value)
            except:
                pass
    return result

def diag2(arr=thing, trans=False):
    "Select trans=True to find trasposed values."
    num = 4
    result = []
    if trans is True:
        arr = np.swapaxes(arr, 0 ,1)
    arrwidth = np.shape(arr)[0]
    arrheight = np.shape(arr)[1]
    for y in range(0, arrheight):
        for x in range(0, arrwidth):
            try:
                value = arr[y,x]*arr[y+1,x-1]*arr[y+2,x-2]*arr[y+3,x-3]
                result.append(value)
            except:
                pass
    return result

diagonal 1: 40304286
diagonal 2: 70600674

# 12

For this I needed to rewrite my factoring algorithm.
It is much faster now.

def best_factor(x):
    """
    Counts factors of a number. Includes 1 and the number.
    Way better than previous version
    """
    if x == 1:
        return 1  # [1]
    factors = 1
    n = 2
    limit = x
    # factors_list = [1]
    while n <= limit:
        if x % n == 0:  # Is it a factor?
            if n != limit:
                factors += 2
                # factors_list.append(n)
                # factors_list.append(limit)
                limit = x / n
            else:
                factors += 1
                # factors_list.append(n)
        n += 1
    # factors_list.sort()
    return factors  # factors_list


def again():
    n = 1
    tri = 1
    while True:
        if best_factor(tri) > 500:
            return tri
        # print(tri, factor_count(tri))
        n += 1
        tri = tri + n

In [530]: again()
Out[530]: 76576500

#13
numstring = (
"37107287533902102798797998220837590246510135740250 \
46376937677490009712648124896970078050417018260538 \
74324986199524741059474233309513058123726617309629 \
91942213363574161572522430563301811072406154908250 \
23067588207539346171171980310421047513778063246676 \
89261670696623633820136378418383684178734361726757 \
28112879812849979408065481931592621691275889832738 \
44274228917432520321923589422876796487670272189318 \
47451445736001306439091167216856844588711603153276 \
70386486105843025439939619828917593665686757934951 \
62176457141856560629502157223196586755079324193331 \
64906352462741904929101432445813822663347944758178 \
92575867718337217661963751590579239728245598838407 \
58203565325359399008402633568948830189458628227828 \
80181199384826282014278194139940567587151170094390 \
35398664372827112653829987240784473053190104293586 \
86515506006295864861532075273371959191420517255829 \
71693888707715466499115593487603532921714970056938 \
54370070576826684624621495650076471787294438377604 \
53282654108756828443191190634694037855217779295145 \
36123272525000296071075082563815656710885258350721 \
45876576172410976447339110607218265236877223636045 \
17423706905851860660448207621209813287860733969412 \
81142660418086830619328460811191061556940512689692 \
51934325451728388641918047049293215058642563049483 \
62467221648435076201727918039944693004732956340691 \
15732444386908125794514089057706229429197107928209 \
55037687525678773091862540744969844508330393682126 \
18336384825330154686196124348767681297534375946515 \
80386287592878490201521685554828717201219257766954 \
78182833757993103614740356856449095527097864797581 \
16726320100436897842553539920931837441497806860984 \
48403098129077791799088218795327364475675590848030 \
87086987551392711854517078544161852424320693150332 \
59959406895756536782107074926966537676326235447210 \
69793950679652694742597709739166693763042633987085 \
41052684708299085211399427365734116182760315001271 \
65378607361501080857009149939512557028198746004375 \
35829035317434717326932123578154982629742552737307 \
94953759765105305946966067683156574377167401875275 \
88902802571733229619176668713819931811048770190271 \
25267680276078003013678680992525463401061632866526 \
36270218540497705585629946580636237993140746255962 \
24074486908231174977792365466257246923322810917141 \
91430288197103288597806669760892938638285025333403 \
34413065578016127815921815005561868836468420090470 \
23053081172816430487623791969842487255036638784583 \
11487696932154902810424020138335124462181441773470 \
63783299490636259666498587618221225225512486764533 \
67720186971698544312419572409913959008952310058822 \
95548255300263520781532296796249481641953868218774 \
76085327132285723110424803456124867697064507995236 \
37774242535411291684276865538926205024910326572967 \
23701913275725675285653248258265463092207058596522 \
29798860272258331913126375147341994889534765745501 \
18495701454879288984856827726077713721403798879715 \
38298203783031473527721580348144513491373226651381 \
34829543829199918180278916522431027392251122869539 \
40957953066405232632538044100059654939159879593635 \
29746152185502371307642255121183693803580388584903 \
41698116222072977186158236678424689157993532961922 \
62467957194401269043877107275048102390895523597457 \
23189706772547915061505504953922979530901129967519 \
86188088225875314529584099251203829009407770775672 \
11306739708304724483816533873502340845647058077308 \
82959174767140363198008187129011875491310547126581 \
97623331044818386269515456334926366572897563400500 \
42846280183517070527831839425882145521227251250327 \
55121603546981200581762165212827652751691296897789 \
32238195734329339946437501907836945765883352399886 \
75506164965184775180738168837861091527357929701337 \
62177842752192623401942399639168044983993173312731 \
32924185707147349566916674687634660915035914677504 \
99518671430235219628894890102423325116913619626622 \
73267460800591547471830798392868535206946944540724 \
76841822524674417161514036427982273348055556214818 \
97142617910342598647204516893989422179826088076852 \
87783646182799346313767754307809363333018982642090 \
10848802521674670883215120185883543223812876952786 \
71329612474782464538636993009049310363619763878039 \
62184073572399794223406235393808339651327408011116 \
66627891981488087797941876876144230030984490851411 \
60661826293682836764744779239180335110989069790714 \
85786944089552990653640447425576083659976645795096 \
66024396409905389607120198219976047599490197230297 \
64913982680032973156037120041377903785566085089252 \
16730939319872750275468906903707539413042652315011 \
94809377245048795150954100921645863754710598436791 \
78639167021187492431995700641917969777599028300699 \
15368713711936614952811305876380278410754449733078 \
40789923115535562561142322423255033685442488917353 \
44889911501440648020369068063960672322193204149535 \
41503128880339536053299340368006977710650566631954 \
81234880673210146739058568557934581403627822703280 \
82616570773948327592232845941706525094512325230608 \
22918802058777319719839450180888072429661980811197 \
77158542502016545090413245809786882778948721859617 \
72107838435069186155435662884062257473692284509516 \
20849603980134001723930671666823555245252804609722 \
53503534226472524250874054075591789781264330331690\
")

from decimal import Decimal, getcontext
getcontext().prec = 100
# or use mpmath. Might be better.
nums = numstring.split(" ")
new = []
for x in nums:
    new.append(Decimal(x))
sum(new)

In [576]: sum(new)
Out[576]: Decimal('5537376230390876637302048746832985971773659831892672')


# 14
def findit():
    max = 0
    n = 1
    longest = [1, 1]  # number and sequence length.
    for n in range(1, 1000000):
        test = collatz(n)
        if test > max:
            max = test
            print (n, max)


def collatz(seq):
    terms = 1
    while seq != 1:
        is_odd = bool(seq % 2)
        if is_odd is True:
            seq = 3 * seq + 1
            terms += 1
        elif is_odd is False:
            seq = seq / 2
            terms += 1
    return terms

#15
import random


def transit():
    path_list = []
    coords = (0, 0)
    while coords != (19, -19):
        flip = random.randint(0, 1)
        if flip == 0:

Plan:
start with 2 x 2 and move up.
Do not use random paths.
Do not make a list to be counted later.
Use a binary number to specify the path with zero signifying down
and 1 signifying right.
Prune the path and all the possible subpaths when a wall is hit.

the number will look like this:
initial paths.............final paths.
0101001011010010101101001111001111010

So the number will be counted forward but 'read' backwards.

Now determine what the maximum path length is.

To make iteration easy, use decimal and convert to binary

To prune a path, add 2^n to the search decimal.

Other than traversing step by step, is there any other way of
determining if a wall has been hit?

I could use vectors but that would not tell me where to prune the
tree.


 max path:
1: 01
2: 0011
3: 000111
4: 00001111

min path:
1: 10
2: 1100
3: 111000
4: 11110000

what is 0b1100-0b0011?
Out[7]: 9
so, for a 2x2 grid I am assuming that means that there will
be 9+1=10 paths to check. (because you include the edges.)
6 of them will reach the other corner.

First make a loop that tests every possibility and test it on small
lattices. Then make it better by pruning. Make sure the loop goes
up in value instead of down.

max_path = for 2 by 2: 0011 (3) (2**1 + 2**2)
min_path = for 2 by 2: 1100 (12)

def pathstring(path_decimal, side_length):
    "Converts decimal path to 0 padded pathstring."
    half_path = str(bin(path_decimal))
    half_path = half_path.split("b")
    half_path = half_path[1]
    pad = 2 * side_length - len(half_path)
    full_path = "0" * pad + half_path
    return full_path


def path(side_length):
    '0 is down. 1 is right.'
    solutions = 0
    max_path = 0
    min_path = 0
    for n in range(0, side_length):
        max_path = max_path + 2**n
    min_path_string = "0b" + pathstring(max_path, side_length)[::-1]
    # print(pathstring(max_path, side_length), min_path_string)
    min_path = int(min_path_string, 2)
    # return pathstring(max_path,side_length), pathstring(min_path,side_length)
    path = max_path
    while path <= min_path / 2:
        coord = [0, 0]  # x,y
        # print(coord)
        check = pathstring(path, side_length)
        # print(check)
        path_pos = 0
        for step in check:
            path_pos += 1
            if step == "0":
                coord[1] = coord[1] - 1
            if step == "1":
                coord[0] = coord[0] + 1
            # print(coord)
            if coord == [side_length, - side_length]:
                solutions += 1
                # print("yes")
                # print(path) # There is no need to prune here.
                path += 1
            if coord[0] > side_length or coord[1] < - side_length:
                rev_pos = 2 * side_length - path_pos
                # print("prune at pos ", rev_pos)
                path = path + 2 ** rev_pos
                break  # Prune only here.
    return solutions * 2


from time import time


def test(num):
    for x in range(1, num + 1):
        start = time()
        sol = path(x)
        total = time()-start
        print(x, sol, int(total*100)/100)


In [178]: test(10)
1 2 0.0
2 6 0.0
3 20 0.0
4 70 0.0
5 252 0.0
6 924 0.02
7 3432 0.1
8 12870 0.42
9 48620 1.54
10 184756 6.95


Also, this is symmetrical.
You only need to do half and multiply by 2.
Not that that helps much.
start: 15:23:20

Too long.

Next thought: I am repeating work by traversing the same paths.
I need to make this a linear problem instead of an exponetial one.

1: Midline method.
divide the midline into a list of points.
Number the paths going into each point.
Because of symmetry, paths going in should equal paths going out.
For each midline point, the total number of paths leading from
corner to corner will be paths^2.
Simply sum to get the total.
The total time will be the square root of what it would be if all paths
were explored.
mid_points[]

No pruning will be needed.

import numpy as np

def pathstring2(path_decimal, side_length):
    "Converts decimal path to 0 padded pathstring."
    half_path = str(bin(path_decimal))
    half_path = half_path.split("b")
    half_path = half_path[1]
    pad = side_length - len(half_path)
    full_path = "0" * pad + half_path
    return full_path


def path2(side_length):
    '0 is down. 1 is right.'
    solutions = np.zeros(side_length + 1)
    min_path_string = "0b" + side_length * "0"
    max_path_string = "0b" + side_length * "1"
    # print(pathstring(max_path, side_length), min_path_string)
    min_path = int(min_path_string, 2)
    max_path = int(max_path_string, 2)
    path = min_path
    while path <= max_path:
        coord = [0,0]  # x,y
        # print(coord)
        check = pathstring2(path, side_length)
        #print(check)
        for step in check:
            if step == "0":
                coord[1] = coord[1] - 1
            if step == "1":
                coord[0] = coord[0] + 1
            #print(coord)
        path += 1
        solutions[coord[0]] += 1
    total = 0
    for x in solutions:
        total = total + x**2
    return total

def test2(num):
    for x in range(1, num + 1):
        start = time()
        sol = path2(x)
        total = time()-start
        print(x, sol, int(total*100)/100)

In [216]: test2(10)
1 2.0 0.0
2 6.0 0.0
3 20.0 0.0
4 70.0 0.0
5 252.0 0.0
6 924.0 0.0
7 3432.0 0.0
8 12870.0 0.0
9 48620.0 0.0
10 184756.0 0.0

In [217]: path2(20)
Out[217]: 137846528820.0

#16
In [231]: thing = "10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376"

total = 0

for x in thing:
    total = total + int(x)


#17

num_dict = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five",
            6:"six", 7:"seven", 8:"eight",9:"nine"}





#20
getcontext().prec = 5000
total = Decimal(0)
big = Decimal(100)

def fact(num):
    total = Decimal(1)
    for x in range(int(num), 0, -1):
        total = total * Decimal(x)
    return total

real_big = fact(big)

real_string = str(real_big)

total_again = 0
for n in real_string:
    total_again += int(n)








#23
Start with the best factoring algo:


def best_factor(x):
    """
    Counts factors of a number. Includes 1 and the number.
    Way better than previous version
    """
    if x == 1:
        return 1, [1]
    factors = 1
    n = 2
    limit = x
    factors_list = [1]
    while n <= limit:
        if x % n == 0:  # is it a factor?
            if n != limit:
                factors += 2
                factors_list.append(n)
                factors_list.append(limit)
                limit = x / n
            else:
                factors += 1
                factors_list.append(n)
        n += 1
    factors_list.sort()
    return factors , factors_list


def list_perfect(num):
    for n in range(1, num):
        if n == sum(best_factor(n)[1]) - n:
            print(n)

In [57]: list_perfect(100000)
1
6
28
496
8128


def list_abundant(num):
    'lists abundant #s under num'
    num_list = []
    for n in range(1, num + 1):
        fact_sum = (sum(best_factor(n)[1]) - n)
        if n < fact_sum:
            num_list.append(n)
    num_list.sort()
    return num_list

poop = list_abundant(28123)

def canitbe(x, nums=nums):
    """
    checks if x can be expressed as a sum of any two numbers in
    nums.
    """
    n = 0
    while nums[n] < int(x/2) + 1:
        left_over = x - nums[n]
        if left_over in poop:
                # print("works: ", nums[n])
                return True
        n += 1
    return False

In [236]: canitbe(24,nums=poop)
Out[236]: True

def allthatdont(poop=poop):
    total = 0
    for x in range(1, 28123 + 1):
        if canitbe(x, nums=poop) is False:
            total += x
        print(x, total)
    return total

Hmm. Too slow but it works.


i got to 4179871 and it seemed stuck so I tried it...

#24

In [254]: from math import factorial

In [255]: factorial(10)
Out[255]: 3628800

method 1:
Iterate through from 0123456789 - 9876543210.
Count when any number doen not appear twice.

first make a function that lists them all.
Then alter it to skip...

def iter():
    count = 1
    rotate = 0
    x = 123456789
    old = x
    while x <= 9876543210:
        numstring = str(x)
        if len(numstring) == 9:
            numstring = "0" + numstring
        if "0" in numstring:
            if "1" in numstring:
                if "2" in numstring:
                    if "3" in numstring:
                        if "4" in numstring:
                            if "5" in numstring:
                                if "6" in numstring:
                                    if "7" in numstring:
                                        if "8" in numstring:
                                            if "9" in numstring:
                                                # print(x, count, x - old)
                                                if count == 999999:
                                                    print(x)
                                                if count == 1000000:
                                                    return x
                                                if count == 1000001:
                                                    print(x)
                                                rotate += 1
                                                if rotate > 10000: # this is jump
                                                    print(x, count, x - old)
                                                    rotate = 0
                                                old = x
                                                count += 1
        x += 1

highest known:
659874312 226799

This numerical approach is going nowhere.
I am not even sure my algorith is right.
How about something stringy?

123456789
123456798
123456879
123456897
123456978
123456987
123457689
123457698
123457869
123457896
123457968
123457986
123458679
123458697
123458769
123458796
123458967
123458976
123459678
123459687
123459768


answer is
Out[49]: 2783915460
I had to iterate the entire million to find it



#25
def fib_iter(n):
    'fast but not fastest, i think.'
    assert n >= 0
    i, fib_i, fib_i_minus_one = 0, 0, 1
    while i < n:
        i = i + 1
        fib_i, fib_i_minus_one = fib_i_minus_one + fib_i, fib_i
    return fib_i


def findit(num):
    result = 0
    start = 1
    while len(str(result)) < num:
        result = fib_iter(start)
        start += 1
    return start - 1, len(str(result))

In [298]: findit()
Out[298]: (4783, 1000)

More fibonacci algos:
http://bosker.wordpress.com/2011/04/29/the-worst-algorithm-in-the-world/






#48
getcontext().prec = 5000
total = Decimal(0)

for n in range(1, 1001):
    poop = Decimal(n)
    total = total + poop ** poop







