# poly class extends dict, python's dictionary class
# a polynomial is represented by a dictionary
# e.g. p = {(3, 1): -1, (1, 3): 1}, instantiate p by writing
# p = poly({(3, 1): -1, (1, 3): 1}) or poly([((3, 1), -1), ((1, 3), 1)])
# or any iterable structure with key-value pairing
class poly(dict):
    # word is a monomial, i.e. a tuple
    # returns the coefficient of the monomial `word`
    # e.g. p = poly({(3, 1): -1, (1, 3): 1}); p.coeff_of((3, 1)) = -1; p.coeff_of((1, 1)) = 0;
    def coeff_of(self, word):
        if word in self:
            return self[word]
        return 0

    # adds polynomial q to this polynomial, mutates this polynomial
    # q is a poly object
    def add(self, q):
        for word in q:
            if word in self:
                self[word] += q[word]
            else:
                self[word] = q[word]

    # multiplies this polynomial with scalar c
    # mutates this polynomial
    def scal(self, c):
        for word in self:
            self[word] *= c

    # overloads + operator
    # self and q are both polys
    # returns self + q but self, q stay the same
    def __add__(self, q):
        result = poly(self.copy())
        result.add(q)
        return result

    # o: scalar
    # 3 * poly({(3, 1): -1}) doesn't work
    def __mul__(self, o):
        result = poly(self.copy())
        result.scal(o)
        return result
    

# f is a function whose arguments can only be monomials/tuples
# output_type is the type of what f outputs. 
# The output of f supports poly objects or scalar (int, float, ...) for now
# extends f by linearity
# returns the extended f whose every argument can now be a polynomial
def lin_extend(f, output_type):
    zero = __zero(output_type)

    # each argument in *polys is a poly object or a dict
    def extended_f(*polys):
        result = zero
        d = __lin_extend_helper(polys)
        for words, coeff in d.items():
            result = result + f(*words) * coeff
        return result
    
    return extended_f

# object_type: poly or scalar (int, float, ...) for now
# returns the zero of that object type
def __zero(object_type):
    if object_type == poly:
        return poly({})
    else: # scalar
        return 0

# polys is a tuple of polynomials p1, p2, ..., pn
# returns a dictionary consisting of all possible (key: value) pairs
# of the form (w1, w2, ..., wn): <p1|w1><p2|w2>...<pn|wn>
# (w1, w2, ..., wn) is a tuple of monomials, where w_i comes from polynomial p_i
# <p1|w1><p2|w2>...<pn|wn> is the product of coefficients
# kind of like tensor product
def __lin_extend_helper(polys):
    if len(polys) == 1:
        result = {}
        for w, c in polys[0].items():
            result[ (w,) ] = c
        return result
    
    recursive = __lin_extend_helper(polys[:-1])
    result = {}
    for w, c in polys[-1].items():
        for key, value in recursive.items():
            new_key = (*key, w) # *key uses the unpacking operator
            new_value = value * c
            result[new_key] = new_value
    
    return result

def test_lin_extend_helper(polys):
    return __lin_extend_helper(polys)


#def lincom(<list of dictionaries>, <list of coeff>) e.g. lincom([u,v,w], [3,4,-1]) => return dictionary: 3u + 4v - w
def lincom(l, c):
    r = {}
    n = len(c) #len(l) should equal to len(c)
    for i in range(n):
        r = plus(r, scal(c[i], l[i]))
    return r        

def show(d):
    for k in d:
        print(k, '------', d[k]) 

def plus(u, v): 
    result = v.copy()
    for k in u:
        if k in result:
            result[k] += u[k]
        else:
            result[k] = u[k]
    return result

def plus1(u, v): #v will CHANGE to u+v; u won't change
    for k in u:
        if k in v:
            v[k] += u[k]
        else:
            v[k] = u[k]
            
def scal(n, d): #d is a dictionary; return scalar product of d by n
    r = d.copy()
    for k in r:
        r[k] *= n
    return r

def scal1(n, d): #d will CHANGE
    for k in d:
        d[k] *= n
        
def concat(u, v): #u,v are dicts with xy-string/z-value-tuple keys; return uv
                    #watch out when u, v are empty dicts
    r = {}
    for k in u:
        for l in v:           
            r[k + l] = u[k] * v[l] #k + l joins two strings or tuples
    return r




