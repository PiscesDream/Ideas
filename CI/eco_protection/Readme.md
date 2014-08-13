#Eco_system project#

=====================

#version1#

eco_pro.py_bck

#version2#

eco_pro.py

biont:
    gene:       1. Does not change in one group
                2. [0,1]*100 #the age can eat
                3. can repoduct in [20, 40]

    fitness:    When the group died out.

    health:     effect health and repoduct ability
    age:        unchangable

    repoduct:   able when 1. health >= rep_req #repoduct requirement
                          2. age is in range
                          3. health -= rep_req
                          4. propobility depends on health and alive num
                num. of scions depends on health

plant:
    grow:       in sigmoid function    
    maximum:    500

#version2.1#
    gene:       [int] * 100, how health to get in age **

