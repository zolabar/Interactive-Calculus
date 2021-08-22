import sympy as sym
import numpy as np

x, y, z = sym.symbols('x y z', real=True)


class statPoint:
    def __init__(self, point, eigenvalues):
        self.point=point
        self.eigenvalues=eigenvalues
        if (np.array(list(eigenvalues))>0).all():
            self.eType='min'
        elif  (np.array(list(eigenvalues))<0).all():
            self.eType='max'
        elif  np.array(list(eigenvalues)).prod()==0:
            self.eType='not classifiable'        
        else:
            self.eType='saddle'
  
def H(f):
    """
    

    Parameters
    ----------
    f : symbolic function

    Returns
    -------
    Hf : Hessian matrix

    """
    Hf=sym.Matrix(([sym.diff(f,x,x),sym.diff(f,x,y)],[sym.diff(f,x,y),sym.diff(f,y,y)]))
    return Hf

def exFinder(f):
    """
    

    Parameters
    ----------
    f : symbolic function from R^2 to R

    Returns
    -------
    statPoints : stationary points
    H : Hessian at those points

    """
    print('function:')
    print(f)
    print(' ')
    system=[sym.diff(f,x),
            sym.diff(f,y),
           ]
  

    solSet=sym.nonlinsolve(system,[x,y])

    solSetReal=[]
    for i in list(solSet):
        if i[0].is_real and i[1].is_real:
            solSetReal.append(i)

    statPoints=[]
    for i in solSetReal:
        H=sym.Matrix(([sym.diff(f,x,x),sym.diff(f,x,y)],
                      [sym.diff(f,x,y),sym.diff(f,y,y)]))
        H=H.subs(x,i[0])
        H=H.subs(y,i[1])
        statPoints.append(statPoint(i,H.eigenvals()))

    for i in statPoints:
        print(i.point, i.eigenvalues, i.eType)  
        
    return statPoints, H
