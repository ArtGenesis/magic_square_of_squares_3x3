from decimal import *
getcontext().prec = 200 #need increase with big argument 

'''
Some python functions to generate magic square of squares 3x3
with 6 perfect squares
'''

'''

Example: tri_duplet(5, 6)
Work with x = odd(x), y = even(y), and different x = even(x), y = odd(y)
6 * 3(18)
5 + 6(11), 5 - 6 (1)
5 + 18(23), 5 - 18(13)
5 * 11(55), 5 * 1(5)
23 * 6(138), 13 * 6(78)
(78**2 - 55**2) * 78 * 55 (13123110)
5**2 + 138**2(19069), 55**2 + 78**2(9109)
19069**2 - 13123110 * 4, 19069**2, 19069**2 + 13123110 * 4
9109**2 - 13123110 * 4, 9109**2, 9109**2 + 13123110 * 4

check func :
19069        5521      275792761
11639      223300321     17639
170807881    20399       9109

Smallest :
x = 2, y = 1:

37    41    265       47    1  1897
1    1105   47        1057 37   41
1945  23    29        29  2737  23

x = 1, y = 2:
197    151    14425   
31    25345   223          
36265  167    109     
'''

def tri_duplet(x, y):                         
    y1, y3 = y, y * 3                         
    xpy1, xmy1 = x + y1, abs(x - y1)          
    xpy3, xmy3 = x + y3, abs(x - y3)           
    a1, a2 = xpy1 * x, xmy1 * x               
    b1, b2 = xpy3 * y1,  xmy3 * y1            
    area = abs(b2 * a1 * (b2**2 - a1**2))
    area4 = area * 4
    n1, n2 = a2**2 + b1**2, a1**2 + b2**2     
    tripa = [n1**2 - area4, n1**2, n1**2 + area4]
    tripb = [n2**2 - area4, n2**2, n2**2 + area4]
    return tripa, tripb, area            
    


'''
Example: get_plus_double_square(5, 1)
Work with x = odd(x), y = odd(y), and different x = odd(x), y = odd(y)                             

5**2(25), 1**2 (1)
25 + (2 * 1**2) // 3 (9)
25 — 9 * 2 (7)
25 — 7 * 2 (11)
25 * 9 * 2 * 7 * 11 * 1**2 (34650)
((9*2)**2 + 7**2) * 1 (373)
(9**2 + (1 * 2)**2) * 5 (425)
425**2 - 34650 * 4, 425**2, 425**2 + 34650 * 4
373**2 - 34650 * 4, 373**2, 373**2 + 34650 * 4

Smallest : 
x = 5, y = 1
425        23    298477      565    23     222121   
527      159877   205        289    425    527
21277     565     373        373   360721  205


x = 1, y = 5





'''
#!!! Don't work if x % 3 == 0 or y % 3 == 0
def get_plus_double_square(x, y):                               
    xp, yp = x**2, y**2                                         
    a = (xp + 2 * yp) // 3                                     
    b =  xp - a * 2                                                                 
    c = abs(xp - b * 2)                                                          
    area = abs(xp * a * 2 * b * c * yp)                      
    area4 = area * 4                                            
    sqra = ((a * 2)**2 + b**2) * y                                        
    sqrb = (a**2 + (yp * 2)**2) * x                             
    tripa = [sqra**2 - area4, sqra**2, sqra**2 + area4]
    tripb = [sqrb**2 - area4, sqrb**2, sqrb**2 + area4]
    return tripa, tripb, area



'''
Example: get_square_minus_square(13, 7)
Work with x = odd(x), y = odd(y), and same x = odd(x), y = odd(y)                          

13**2(169), 7**2(49)
(169-49) // 3 (40)
169 - 40 (129)
169 - 40 * 2(89)
169 * 40 * 129 * 89 * 49(3802966440)
(129**2 + 40**2) * 7 (127687)
(89**2 + 40**2) * 13(123773)
123773**2-3802966440*4, 123773**2, 123773**2+3802966440*4
127687**2-3802966440*4, 127687**2, 127687**2+3802966440*4

'''
#!!! Don't work if x % 3 == 0 or y % 3 == 0
def get_square_minus_square(x, y):              
    xp, yp = x**2, y**2                         
    a = (xp - yp) // 3                          
    b = xp - a                                  
    c = xp - a * 2                              
    area = abs(xp * a * b * c * yp)          
    area4 = area * 4                             
    sqra = (a**2 + b**2) * y                    
    sqrb = (a**2 + c**2) * x                    
    tripa = [sqra**2 - area4, sqra**2, sqra**2 + area4]
    tripb = [sqrb**2 - area4, sqrb**2, sqrb**2 + area4]
    return tripa, tripb, area


'''
checkmagic(list1, list2)
Get two list with perfect squares from functions above
and check if exist at least one another perfect square
in different positions, if exists atleast one, print...
'''

def checkmagic(n1, n2): 
    
    a, b, c = n1 
    d, e, f = n2

    if b * 2 > f:
        g = b * 2 - d
        h = b * 2 - e
        j = b * 2 - f
        gs = Decimal(g).sqrt()
        hs = Decimal(h).sqrt()
        js = Decimal(j).sqrt()
        if gs % 1 == 0 or hs % 1 == 0 or js % 1 == 0:
            print(n1, n2, g, h, j)
        #print(n1, n2, g, h, j)
    
    if e * 2 > c:
        g = e * 2 - a
        h = e * 2 - b
        j = e * 2 - c
        gs = Decimal(g).sqrt()
        hs = Decimal(h).sqrt()
        js = Decimal(j).sqrt()
        if gs % 1 == 0 or hs % 1 == 0 or js % 1 == 0:
            print(n2, n1, g, h, j)
        #print(n1, n2, g, h, j)

    #check if one of result in diagonal is perfect square 
    ad = (a + d) // 2
    be = (b + e) // 2
    cf = (c + f) // 2
    ads = Decimal(ad).sqrt()
    bes = Decimal(be).sqrt()
    cfs = Decimal(cf).sqrt()
    #print(n1, n2, ad, be, cf)
    if ads % 1 == 0 or bes % 1 == 0 or cfs % 1 == 0:
        print(n1, n2, ad, be, cf)

      
      
