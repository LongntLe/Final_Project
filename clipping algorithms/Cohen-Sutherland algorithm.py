# Cohen-Sutherland algorithm

'''
Source: scivision/morecvutils

This algorithm is a line clipping algorithm, often seen in computer graphic. The algorithm will employ multiple 
data structures for fast clipping.

Algorithm summary:
The algorithm includes, excludes or partially includes the line based on whether:

- Both endpoints are in the viewport region (bitwise OR of endpoints = 00): trivial accept.
- Both endpoints share at least one non-visible region, which implies that the line does not cross the visible region. (bitwise AND of endpoints ≠ 0): trivial reject.
- Both endpoints are in different regions: in case of this nontrivial situation the algorithm finds one of the two points that is outside the viewport region (there will be at least one point outside).
The intersection of the outpoint and extended viewport border is then calculated (i.e. with the parametric equation for the line), and this new point replaces the outpoint. The algorithm repeats until a trivial accept or reject occurs.

'''

import numpy as np

def cohensutherland(xmin, ymax, xmax, ymin, x1, y1, x2, y2):
    """Clips a line to a rectangular area.
    This implements the Cohen-Sutherland line clipping algorithm.  xmin,
    ymax, xmax and ymin denote the clipping area, into which the line
    defined by x1, y1 (start point) and x2, y2 (end point) will be
    clipped.
    If the line does not intersect with the rectangular clipping area,
    four None values will be returned as tuple. Otherwise a tuple of the
    clipped line points will be returned in the form (cx1, cy1, cx2, cy2).
    """
    INSIDE,LEFT, RIGHT, LOWER, UPPER = 0,1, 2, 4, 8

    def _getclip(xa, ya):
        p = INSIDE  #default is inside

        # consider x
        if xa < xmin:
            p |= LEFT
        elif xa > xmax:
            p |= RIGHT

        # consider y
        if ya < ymin:
            p |= LOWER
        elif ya > ymax:
            p |= UPPER
        return p

# check for trivially outside lines
    k1 = _getclip(x1, y1)
    k2 = _getclip(x2, y2)

#%% examine non-trivially outside points
    while (k1 | k2) != 0: # if both points are inside box (0000) , ACCEPT trivial whole line in box

        # if line trivially outside window, REJECT
        if (k1 & k2) != 0: #bitwise AND &
            #if dbglvl>1: print('  REJECT trivially outside box')
            #return nan, nan, nan, nan
            return None, None, None, None

        #non-trivial case, at least one point outside window
        # this is not a bitwise or, it's the word "or"
        opt = k1 or k2 # take first non-zero point, short circuit logic
        if opt & UPPER: #these are bitwise ANDS
            x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
            y = ymax
        elif opt & LOWER:
            x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
            y = ymin
        elif opt & RIGHT:
            y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
            x = xmax
        elif opt & LEFT:
            y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
            x = xmin
        else:
            raise RuntimeError('Undefined clipping state')

        if opt == k1:
            x1, y1 = x, y
            k1 = _getclip(x1, y1)
        elif opt == k2:
            x2, y2 = x, y
            k2 = _getclip(x2, y2)
    return x1, y1, x2, y2
