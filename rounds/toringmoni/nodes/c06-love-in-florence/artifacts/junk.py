JUNK = {
 0: [(1,2),(28,34),(39,42),(57,60),(93,95)],                      # S1: U LINCHO TAL GUA NI
 1: [(4,8),(14,15),(39,42),(53,57),(57,65),(71,78)],              # S2: CKER P R/HA SANT NATACROI E/ROTLES
 2: [(5,6),(34,37),(38,41),(60,62),(70,71),(85,89),(91,94),(99,103)],  # S3
 3: [(7,12),(17,24),(69,71),(89,93)],                             # S4: MARFO SOVIETA DA GYPT
 4: [(8,13),(64,67),(87,89),(99,102),(102,105),(108,113)],        # S5: CERAN STF TY PAR TOA CINTH
 5: [(1,6),(11,13),(29,33),(82,84)],                              # S6: MINGB TI AMEN DY
}
import os
OVL = int(os.environ.get('OVL', '1'))
def isjunk(si, a, b):
    """does span [a,b) overlap a junk region by >=OVL letters?"""
    for (x, y) in JUNK[si]:
        if min(b, y) - max(a, x) >= OVL: return True
    return False
