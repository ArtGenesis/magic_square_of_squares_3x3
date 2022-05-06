# magic_square_of_squares_3x3
Some python functions to generate magic square of squares 3x3 with 6 perfect squares

Example: tri_duplet(5, 6)
Work with x = odd(x), y = even(y), and different x = even(x), y = odd(y)

6 * 3(18)
5 + 6(11), 5 - 6 (1)
5 + 18(23), 5 - 18(13)
5 * 11(55), 5 * 1(5)
23 * 6(138), 13 * 6(78)
(78**2 - 55**2) * 78 * 55 (13123110)
5**2 + 138**2(19069), 55**2 + 78**2(9109)
19069**2 - 13123110 * 4, 19069**2, 19069**2 + 13123110 * 4  ([17639**2, 19069**2, 20399**2])
9109**2 - 13123110 * 4, 9109**2, 9109**2 + 13123110 * 4     ([5521**2 ,  9109**2, 11639**2])

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


Example: get_plus_double_square(5, 1)
Work with x = odd(x), y = odd(y), and different x = odd(x), y = odd(y)                             

5**2(25), 1**2 (1)
25 + (2 * 1**2) // 3 (9)
25 — 9 * 2 (7)
25 — 7 * 2 (11)
25 * 9 * 2 * 7 * 11 * 1**2 (34650)
((9*2)**2 + 7**2) * 1 (373)
(9**2 + (1 * 2)**2) * 5(425)
425**2 - 34650 * 4, 425**2, 425**2 + 34650 * 4 ([205**2, 425**2, 565**2])      
373**2 - 34650 * 4, 373**2, 373**2 + 34650 * 4 ([23**2, 373**2, 527**2])

Smallest : 

x = 5, y = 1

425        23    298477      565    23     222121   
527      159877   205        289    425    527
21277     565     373        373   360721  205

x = 1, y = 5

11225      511     74406973      11555       511     244222729
3911     66889573   10885        236705329  11225    3911
59372173  11555     2789         2789     251740129  10885



Example: get_square_minus_square(13, 7)
Work with x = odd(x), y = odd(y), and same x = odd(x), y = odd(y)                          
13**2(169), 7**2(49)
(169-49) // 3 (40)
169 - 40 (129)
169 - 40 * 2(89)
169 * 40 * 129 * 89 * 49(3802966440)
(129**2 + 40**2) * 7 (127687)
(89**2 + 40**2) * 13(123773)
123773**2-3802966440*4, 123773**2, 123773**2+3802966440*4   ([10387**2, 123773**2, 174733**2])
127687**2-3802966440*4, 127687**2, 127687**2+3802966440*4   ([33047**2, 127687**2, 177527**2])


127687   10387    31023728509           177527       10387    17288184409
174733  15811862749    33047            2076318649  127687     174733
599996989    177527   123773            123773    32500050169   33047

Smallest:

x = 1, y = 5 and same x = 5, y = 1

725     47    447517      805     47     926641    
497   325117   635        804241  725     497
202717  805    353        353    1049041  635

