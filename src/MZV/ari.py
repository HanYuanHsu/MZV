# the alphabet = {1, 2, 3, 4, ..., ALPHABET_SIZE}
# the numbers in the alphabet represent the intermediates
# of a noncommutative ring
ALPHABET_SIZE = 13



class derivative:
    # instantiate the derivation operator made from flexions flexion_f, flexion_phi
    def __init__(self, flexion_f, flexion_phi):
        self.f = flexion_f # `__` in front of a variable means it is private
        self.phi = flexion_phi
    
    # u, v, w are all words/tuples
    def diff(self, u, v, w):
        if len(w) != len(u) + len(v):
            return 0

        # w will be dissected into abc, where c nonempty, so w is nonempty
        if len(w) == 0:
            return 0
        
        result = 0

        # dissect w into abc, where len(b) = len(v) and c is nonempty
        for i in range(0, len(w) - len(v)):
            a = w[:i]
            b = w[i : i + len(v)]
            c = w[i + len(v):] # c is shortest when i + len(v) = len(w) - 1, i.e. len(c) = 1
            
            u1 = a + (self.f(b, c[0]),) + c[1:]
            v1 = self.phi(c[0], b)
            
            if u1 == u and v1 == v:
                result += 1
            
        # dissect w into abc, where len(b) = len(v) and a is nonempty       
        for i in range(1, len(w) - len(v) + 1):
            a = w[:i]
            b = w[i : i + len(v)]
            c = w[i + len(v):]

            # used for testing
            #print("{0} {1} {2}".format(a, b, c))
            
            u1 = a[:-1] + (self.f(b, a[-1]),) + c
            v1 = self.phi(a[-1], b)

            if u1 == u and v1 == v:
                result -= 1
            
        return result


