#!/usr/bin/env python3
"""Finite exact-success frontier; rational coefficients, numeric LP and checks.

No unitary-Choi theorem or approximate-fidelity law enters this evaluator.
"""
import argparse
import json
from fractions import Fraction as F
from math import comb, factorial, sqrt
from functools import lru_cache

import numpy as np
from scipy.optimize import linprog


def dim_h(d, r, j):
    h = comb(d+r+j-1, r+j) * comb(d+j-1, j)
    if j:
        h -= comb(d+r+j-2, r+j-1) * comb(d+j-2, j-1)
    return h


def orbit_weights(d, n, m):
    n, m = max(n, m), min(n, m)
    r = n-m
    return [F(dim_h(d, r, j)*factorial(d-1)*factorial(n)*factorial(m),
              factorial(m-j)*factorial(d+n+j-1)) for j in range(m+1)]


def recurrence(d, r, j):
    a = F((j+d-1)*(j+d+r-1), (2*j+d+r-1)*(2*j+d+r))
    c = F(j*(j+r), (2*j+d+r-2)*(2*j+d+r-1)) if j else F(0)
    return a, 1-a-c, c


def frontier(d, n, m):
    if d < 2 or n < 0 or m < 0:
        raise ValueError('Need d>=2 and nonnegative integer budgets')
    n, m = max(n, m), min(n, m)
    if not m:
        return {'success': 0.0, 'u': [], 'p': orbit_weights(d,n,m), 'M': []}
    r = n-m
    p = orbit_weights(d,n,m)
    mat = [[F(0) for _ in range(m)] for _ in range(m+1)]
    for j in range(m):
        a,b,c = recurrence(d,r,j)
        mat[j][j] = (1+b)/2
        mat[j+1][j] = a/2
        if j:
            mat[j-1][j] = c/2
    arr = np.array(mat, dtype=float)
    sol = linprog(-np.ones(m), A_ub=arr, b_ub=np.array(p,dtype=float),
                  bounds=(0,None), method='highs')
    if not sol.success:
        raise RuntimeError(sol.message)
    return {'success': float(-sol.fun), 'u': sol.x.tolist(), 'p': p, 'M': mat}


def occupations(d,n):
    if d == 1:
        return [(n,)]
    return [(j,)+tail for j in range(n+1) for tail in occupations(d-1,n-j)]


def contraction(d,n,m):
    """Unnormalized bosonic C on normalized symmetric occupation bases."""
    left = [(a,b) for a in occupations(d,n) for b in occupations(d,m)]
    if not n or not m:
        return np.zeros((0,len(left))), left, []
    right = [(a,b) for a in occupations(d,n-1) for b in occupations(d,m-1)]
    index = {ab:i for i,ab in enumerate(right)}
    c = np.zeros((len(right),len(left)))
    for col,(a,b) in enumerate(left):
        for i in range(d):
            if a[i] and b[i]:
                aa,bb = list(a),list(b)
                aa[i]-=1; bb[i]-=1
                c[index[tuple(aa),tuple(bb)],col] += sqrt(a[i]*b[i])
    return c,left,right


def physical_check(d,n,m):
    """Build actual W and residual X from the LP; verify V^dagger V<=I."""
    n,m=max(n,m),min(n,m)
    sol=frontier(d,n,m)
    c,left,right=contraction(d,n,m)
    rr=len(right); ii={ab:i for i,ab in enumerate(right)}
    w=np.zeros(((1+d*d)*rr,len(left)))
    w[:rr,:]=c/sqrt(2*n*m)
    for col,(a,b) in enumerate(left):
        for i in range(d):
            for j in range(d):
                if a[i] and b[j]:
                    aa,bb=list(a),list(b);aa[i]-=1;bb[j]-=1
                    row=(1+i*d+j)*rr+ii[tuple(aa),tuple(bb)]
                    w[row,col]=sqrt(a[i]*b[j]/(2*n*m))
    cr,_,_=contraction(d,n-1,m-1)
    vals,vecs=np.linalg.eigh(cr.T@cr)
    x=np.zeros((rr,rr))
    pres=orbit_weights(d,n-1,m-1)
    r=n-m; b=m-1
    for j,u in enumerate(sol['u']):
        ev=(b-j)*(d+r+b+j-1)
        sel=np.abs(vals-ev)<1e-7
        assert sel.sum()==dim_h(d,r,j), (d,n,m,j,sel.sum())
        proj=vecs[:,sel]@vecs[:,sel].T
        x += (u/float(pres[j]))*proj
    effect=w.T@np.kron(np.eye(1+d*d),x)@w
    eig=np.linalg.eigvalsh(effect)
    assert eig.min()>-1e-7 and eig.max()<1+1e-7
    aa=(n,)+(0,)*(d-1);bb=(m,)+(0,)*(d-1)
    pos=left.index((aa,bb))
    assert abs(effect[pos,pos]-sol['success'])<1e-7
    return {'d':d,'n':n,'m':m,'success':sol['success'],
            'input_dimension':len(left),'residual_dimension':rr,
            'largest_success_effect_eigenvalue':float(eig.max())}


def mixed_one_conjugate(d, ordinary_cap):
    """Exact rational M3, including the probability of no conjugate signal."""
    return sum((F(comb(ordinary_cap,k)*k,
                  2**ordinary_cap*(d+2*k-1))
                for k in range(ordinary_cap+1)), F(0))


def mixed_frontier(d, ordinary_cap, conjugate_cap):
    """Numerical binomial transform of the proved exact finite pure LP."""
    if d < 2 or ordinary_cap < 0 or conjugate_cap < 0:
        raise ValueError('Need d>=2 and nonnegative integer hard caps')

    @lru_cache(maxsize=None)
    def pure(k,l):
        return frontier(d,k,l)['success']

    value = sum(comb(ordinary_cap,k)*comb(conjugate_cap,l)*pure(k,l)
                for k in range(ordinary_cap+1)
                for l in range(conjugate_cap+1))
    return value / 2**(ordinary_cap+conjugate_cap)


def exact_two_by_two_certificate():
    """Exact rational primal/dual equality for q_2^*(2,2)=12/13."""
    mat = [[F(3,4),F(1,12)],[F(1,4),F(3,4)],[F(0),F(1,6)]]
    p = [F(1,3),F(1,2),F(1,6)]
    u = [F(5,13),F(7,13)]
    y = [F(12,13),F(16,13),F(0)]
    assert all(sum(mat[i][j]*u[j] for j in range(2)) <= p[i]
               for i in range(3))
    assert all(sum(mat[i][j]*y[i] for i in range(3)) == 1
               for j in range(2))
    assert sum(u) == sum(p[i]*y[i] for i in range(3)) == F(12,13)
    return {'success':str(sum(u)),'primal':[str(x) for x in u],
            'dual':[str(x) for x in y],'status':'exact rational certificate passed'}


def mixed_checks():
    """Check rare-source edge and independently certified small sectors."""
    count=0
    for d in [2,3,10]:
        for ordinary_cap in [0,1,2,4,8]:
            value=mixed_frontier(d,ordinary_cap,1)
            exact=mixed_one_conjugate(d,ordinary_cap)
            assert abs(value-float(exact))<1e-10
            assert 0<=exact<=F(1,2)*(1-F(1,2**ordinary_cap))
            count+=1
    # Occupancy-sector enumeration from independently certified pure values.
    certified=(F(4,16)*F(2,3)+F(4,16)*F(4,5)+F(1,16)*F(12,13))
    assert certified==F(331,780)
    assert abs(mixed_frontier(2,2,2)-float(certified))<1e-10
    for d,a,b in [(2,0,3),(2,2,3),(3,1,4),(3,3,2)]:
        value=mixed_frontier(d,a,b)
        assert abs(value-mixed_frontier(d,b,a))<1e-10
        assert value <= (1-2**(-a))*(1-2**(-b))+1e-10
        count+=1
    return {'edge_and_boundary_cases':count,
            'certified_mixed_2_by_2':str(certified),'status':'passed'}


def self_test():
    import sympy as sp
    t=sp.symbols('t')
    count=0
    for d in [2,3,5,20]:
        for n in range(0,7):
            for m in range(0,n+1):
                z=frontier(d,n,m)
                assert sum(z['p'])==1 and all(v>0 for v in z['p'])
                assert 0<=z['success']<=1+1e-8
                assert abs(z['success']-frontier(d,m,n)['success'])<1e-9
                if m==0:
                    assert z['success']==0
                elif m==1:
                    assert abs(z['success']-2*n/(d+2*n-1))<1e-8
                if m:
                    top=F(factorial(d+n-2)*factorial(d+m-2),
                          factorial(d-2)*factorial(d+n+m-2))
                    assert top==z['p'][-1]
                    assert z['success']<=min(1,2*float(1-top))+1e-7
                count+=1
        for r in [0,1,3]:
            for j in range(0,5):
                q=lambda l:sp.jacobi(l,d-2,r,2*t-1)/sp.binomial(l+d-2,l)
                a,b,c=recurrence(d,r,j)
                assert min(a,b,c)>=0
                rhs=sp.Rational(a.numerator,a.denominator)*q(j+1)
                rhs+=sp.Rational(b.numerator,b.denominator)*q(j)
                if j: rhs+=sp.Rational(c.numerator,c.denominator)*q(j-1)
                assert sp.expand(t*q(j)-rhs)==0
    phys=[physical_check(d,n,m) for d,n,m in
          [(2,1,1),(2,2,1),(2,2,2),(2,3,2),(2,3,3),(3,2,2),(3,3,2)]]
    return {'allocation_cases':count,'rational_recurrence_checks':60,
            'physical_matrix_checks':phys,
            'two_by_two_certificate':exact_two_by_two_certificate(),
            'mixed_source_checks':mixed_checks(),'status':'passed'}


def main():
    a=argparse.ArgumentParser()
    a.add_argument('--d',type=int,default=3)
    a.add_argument('--n',type=int,default=2)
    a.add_argument('--m',type=int,default=2)
    a.add_argument('--self-test',action='store_true')
    a.add_argument('--mixed',action='store_true',help='Treat --n/--m as hard mixed-source caps')
    a.add_argument('--output')
    args=a.parse_args()
    if args.self_test:
        obj=self_test()
    elif args.mixed:
        obj={'d':args.d,'ordinary_cap':args.n,'conjugate_cap':args.m,
             'success':mixed_frontier(args.d,args.n,args.m)}
        if args.m==1:
            obj['exact_rational']=str(mixed_one_conjugate(args.d,args.n))
    else:
        obj=frontier(args.d,args.n,args.m)
    raw=json.dumps(obj,default=str,indent=2)
    if args.output:
        with open(args.output,'w') as f:f.write(raw+'\n')
    print(raw)


if __name__=='__main__':main()
