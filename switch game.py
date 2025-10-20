A,B,C,D=map(int,input().split())
o=0
if A<=C:
    if B<=D and B>C:
        o+=B-C
    elif D<=B:
        o+=(D-C)
elif C<A:
    if B<=D:
        o+=B-A
    elif D<=B and D>=A:
        o+=D-A
else:
    o==0
print(o)
