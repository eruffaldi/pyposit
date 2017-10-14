#
# Properties of summation table
#
# Given only points on lattice (a,b) >= 1
#
# lattice size n --> unum 3+n tbis
#
# (a,-a,1/a,-1/a) + (b,-b,1/b,-1/b) 
#
# [   a + b,     a - b,   a + 1/b,     a - 1/b]
# [   b - a,   - a - b,   1/b - a,   - a - 1/b]
# [ b + 1/a,   1/a - b, 1/a + 1/b,   1/a - 1/b]
# [ b - 1/a, - b - 1/a, 1/b - 1/a, - 1/a - 1/b]
#
# [ 1, 2, 3, 4; -2, -1, -4, -3; 5, 6, 7, 8; -6, -5, -8, -7]
#
# a+b
# a-b
# a+1/b = (ab+1)/b
# a-1/b = (ab-1)/b
# b+1/a = (ab+1)/a
# b-1/a = (ab-1)/a
# 1/a+1/b = (a+b)/ab deived
# 1/a-1/b = (b-a)/ab derived
#
# But then we can consider our magic properties so tat
#
# 
#
# Taking all pairs (a,b) with a <= b we have n(n+1)/2 pairs each of 8 cases => 8n (n+1)/2
#
# e.g. 16bit as n=13 we have 13*8 (13+1)/2 instead of 


import punum
import argparse
import fractions
import operator
import tabulate


def main():
    parser = argparse.ArgumentParser(description='Table generator')
    parser.add_argument('--points',nargs="+",type=int,help="lattice points")
    parser.add_argument('--op',choices=["times","plus"],default="plus")
    parser.add_argument('--p3',action="store_true")
    parser.add_argument('--p4',action="store_true")
    parser.add_argument('--p5',action="store_true")
    parser.add_argument('--p8',action="store_true")
    parser.add_argument('--p8b',action="store_true")
    parser.add_argument('--p16',action="store_true")
    parser.add_argument('--verbose',action="store_true")
    parser.add_argument('--sparsetab')
    args = parser.parse_args()
    if args.points is not None:
        if args.points[0] != 1:
            args.points = [1] + args.points
        args.points.sort()
        alpha = punum.Alphabet(args.points)
    else:
        if args.p3:
            alpha = punum.Alphabet.p3()
        elif args.p4:
            alpha = punum.Alphabet.p4()
        elif args.p5:
            alpha = punum.Alphabet.p5()
        elif args.p8:
            alpha = punum.Alphabet.p8()
        elif args.p8b:
            alpha = punum.Alphabet.p8b()
        elif args.p16:
            alpha = punum.Alphabet.p16()


    print ("with",len(alpha.eexacts),"obtain",alpha.n," and ",alpha.n2)
    print (alpha.eexacts)
    if args.op == "plus":
        op = operator.add
    elif args.op == "times":
        op = operator.mul

    rr = []
    for i,ae in enumerate(alpha.eexacts):
        a = alpha.fromexactsindex(i) # fraction
        for j,be in enumerate(alpha.eexacts):
            if j < i:
                continue
            b = alpha.fromexactsindex(j)
            # 8 cases 
            ia = ~a
            ib = ~b
            if i == 0:
                if j == 0:
                    # exactly 1+1 or 1-1 
                    whats = [(a,b),(a,-b)]
                else:
                    # a is 1, j > 1
                    whats = [(a,b),(a,-b),(a,ib),(a,-ib)]
            elif i == j:
                whats = [(a,a),(a,-a),(a,ia),(ia,ia),(a,-ia)]
            else:
                # both > 1
                whats = [(a,b),(a,-b),(b,ia),(a,ib),(ia,ib),(ia,-ib),(b,-ia),(a,-ib)]
            for k,(xa,xb) in enumerate(whats):
                print (xa.v,xb.v,ae,be,k,len(whats))
                x1 = xa.exactvalue()
                x2 = xb.exactvalue()
                y = op(x1,x2)
                uy = alpha.convert(y)
                iy = uy.v
                rr.append(dict(ai=xa.v,bi=xb.v,a=x1,b=x2,y=y,yi=iy))

    if args.sparsetab:
        o = open(args.sparsetab,"w",encoding="utf8")
        for x in rr:
            o.write("%d %d %d\n" % (x["ai"],x["bi"],x["yi"]))
    else:
        print (tabulate.tabulate(rr))




if __name__ == '__main__':
    main()