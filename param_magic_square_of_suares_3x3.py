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
19069**2 - 13123110 * 4, 19069**2, 19069**2 + 13123110 * 4 (17639**2, 19069**2, 20399**2)
9109**2 - 13123110 * 4, 9109**2, 9109**2 + 13123110 * 4    (5521**2, 9109**2, 11639**2)

check func :
19069        5521      275792761         20399       5521   644279641 
11639      223300321     17639           591787201  19069      11639
170807881    20399       9109            9109      696772081   17639

Smallest :
x = 2, y = 1:

37    41    265       47    1  1897
1    1105   47        1057 37   41
1945  23    29        29  2737  23

x = 1, y = 2:
197    151    14425      223    31   65737
31    25345   223        54817  197   151  
36265  167    109        109  76657   167

Some famed results from oeis.org/A283274  with  such arguments:
(5, 6) = [19069, 9109], 13123110
(58, 1) = [10933357, 11713109], 2203385574390
(46, 11) = [3347261, 6895333],  2570042985510
(22, 31) = [12748429, 6203957], 8943387723270
(94, 17) = [58464869, 109402717], 826290896699730
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
It is interesting that at tri_duplet_2(x = 5, y = 2) there is a crossover
with the  tri_duplet(x = 22, y = 31) with different pairs
tri_duplet(22, 31) = [12748429, 6203957], 8943387723270
tri_duplet_2(5, 2) = [12748429, 10085069], 8943387723270
maybe can be exist another intersection with such algorithms...or others algorithms..

Smallest :

x = 1, y = 2 and same y = 2, x = 1

4201969    991      2965            2887       991      17056825 
3041     4658425   263              17513281   2965     263
725       2887    5114881           725      16600369   3041

'''

def tri_duplet_2(x, y):            
    xpy, xmy = x + y, abs(x - y)   
    a, b = xpy * xmy, x * y * 2    
    even = ((a * b) // 3) * 2      
    db_even =  even * 2            
    ap_m_bp = abs(a**2 - b**2)     

    od1 = ap_m_bp + db_even         
    od2 = ap_m_bp - db_even         

    odx1 = abs(od1 * y - even * x)
    ody1 = abs(od1 * x + even * y)

    odx2 = abs(od2 * y - even * x)
    ody2 = abs(od2 * x + even * y)
    
    odx3 = abs(od1 * y + even * x)
    ody3 = abs(od1 * x - even * y)

    odx4 = abs(od2 * y + even * x)
    ody4 = abs(od2 * x - even * y)

    area1 = abs((odx1**2 - ody1**2) * odx1 * ody1)
    area2 = abs((odx2**2 - ody2**2) * odx2 * ody2)
    area3 = abs((odx3**2 - ody3**2) * odx3 * ody3)
    area4 = abs((odx4**2 - ody4**2) * odx4 * ody4)

    #area1 = area2 while (y / x) < (sqrt(2) + 1)
    if area1 == area2:
        sqra, sqrb = (odx1**2 + ody1**2)**2, (odx2**2 + ody2**2)**2
        tripa = [sqra - area1 * 4, sqra, sqra + area1 * 4]
        tripb = [sqrb - area1 * 4, sqrb, sqrb + area1 * 4]
        return tripa, tripb, area1

    #area3 = area4 while (y / x) > (sqrt(2) + 1)
    if area3 == area4:
        sqra, sqrb = (odx4**2 + ody4**2)**2, (odx3**2 + ody3**2)**2
        tripa = [sqra - area3 * 4, sqra, sqra + area3 * 4]
        tripb = [sqrb - area3 * 4, sqrb, sqrb + area3 * 4]
        return tripa, tripb, area3
    
    
    
'''
Example: get_plus_double_square(5, 1)
Work with x = odd(x), y = odd(y), and different x = odd(x), y = odd(y)                             

5**2(25), 1**2 (1)
(25 + (2 * 1**2)) // 3 (9)
25 — 9 * 2 (7)
25 — 7 * 2 (11)
25 * 9 * 2 * 7 * 11 * 1**2 (34650)
((9*2)**2 + 7**2) * 1 (373)
(9**2 + (1 * 2)**2) * 5 (425)
425**2 - 34650 * 4, 425**2, 425**2 + 34650 * 4 (205**2, 425**2, 565**2)
373**2 - 34650 * 4, 373**2, 373**2 + 34650 * 4 (23**2, 373**2, 527**2)

Smallest : 
x = 5, y = 1
425        23    298477      565    23     222121   
527      159877   205        289    425    527
21277     565     373        373   360721  205


x = 1, y = 5
11225      511     74406973      11555       511     244222729
3911     66889573   10885        236705329  11225    3911
59372173  11555     2789         2789     251740129  10885


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
123773**2-3802966440*4, 123773**2, 123773**2+3802966440*4 (10387**2, 123773**2, 174733**2)
127687**2-3802966440*4, 127687**2, 127687**2+3802966440*4 (33047**2, 127687**2, 177527**2)


127687   10387    31023728509           177527       10387    17288184409
174733  15811862749    33047            2076318649  127687     174733
599996989    177527   123773            123773    32500050169   33047


Smallest:
x = 1, y = 5 and x = 5, y = 1

725     47    447517      805     47     926641    
497   325117   635        804241  725     497
202717  805    353        353    1049041  635


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

        
        
'''
Another way to construct magic square 3x3 with 6 perfect squares
I Don't have time to write deepest realisation with some optimisation,
but with some trick need check only three numbers to know is number is
additional 7 perfect square, one of corner is always perfect square
(maybe prefer use arguments, such that sum of squares such arguments will be perfect square)

Work with x = odd(x), y = even(y), and different x = even(x), y = odd(y)

Smallest:
x = 1, y = 2

7081  23  5065 
47    65   79
3385  89   37

x = 2, y = 1

60169  49   40105
119    185  233
28345  257  91
'''

def corner_square(x, y):           
    if x > y:
        xpy =  x + y
        xmy = abs(x - y)
        a, a2 = xmy * y, xmy * x 
        b, b2 = xpy * x, xpy * y
        corner = ((a + b) * (a2**2 + b2**2))**2
    else:
        xpy =  y - x
        xmy =  x + y                
        a, a2 = xmy * x, xmy * y   
        b, b2 = xpy * y, xpy * x
        corner = (abs(a - b) * (a2**2 + b2**2))**2

    od1 = y * a + x * b             
    ev1 = abs(x * a - y * b)        
    od2 = abs(y * a - x * b)        
    ev2 = x * a + y * b             
   
    n = od1**2 + ev1**2             

    ar1 = abs((od1 - ev1) * od1 * ev1 * (od1 + ev1) * 4)
    ar2 = abs((od2 - ev2) * od2 * ev2 * (ev2 + od2) * 4)

    tripa = [n**2 - ar1, n**2, n**2 + ar1]
    tripb = [n**2 - ar2, n**2, n**2 + ar2]

    return tripa, tripb, corner      
      

def check_corner_square(n1, n2, corner):
    a, b, c = n1
    d, b, e = n2

    ad = (a + d) // 2
    ae = (a + e) // 2
    cd = (c + d) // 2
    ce = (c + e) // 2
    li = [ad, ae, cd, ce]
    #print(n1, n2, ad, ae, cd, ce)
    for i in li:
        if i != corner:
            sq = Decimal(i).sqrt()
            if sq % 1 == 0:
                print(n1, n2, corner, i)
