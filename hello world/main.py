#!/usr/bin/ython
# -*- coding:utf-8 -*-
class SyntaxTest(object):
    '''
    This is a class used for learning Python
    
    >>> s = SyntaxTest()
    class SyntaxTest initialized.
    >>> s.test_doc_demo()
    this is a test
    
    '''
    selfIntroStr = 'This is a class used for learning Python syntax'

    def __init__(self):
        print 'class SyntaxTest initialized.'

    def closeureTest(self):
        f1, f2, f3 = self.__closeureTest()
        print f1(), f2(), f3()

    def __closeureTest(self):
        # a closeure demo
        fs = []
        def f(a):
            def f2():
                # generated 3 times
                return a
            return f2
        for i in range(1,4):
            fs.append(f(i))
        return fs

    def mapReduceTest(self):
        # a map reduce demo
        def f(x):
            return x*x
        list = [x for x in range(1,4)]
        print list
        print "map:", map(f,list)

        def g(x, y):
            return x*y
        print "reduce:", reduce(g, list)

    def lambdaTest(self):
        # a lambda function demo
        f = lambda x : x+1
        print f(1)

    def decoratorTest(self):
        # a decorator demo
        def decorator(f):

            def wrapper(*args, **kw):
                return "In wrapper." + " " + f(*args, **kw)
            return wrapper

        @decorator
        def f():
            return "In f."
        print f()

    def decoratorTestBis(self):
        # a decorator demo again
        def log(func) :
            # log can run in two methods
            if isinstance(func, str):
                def outer(f):
                    def wrapper(*args, **kw):
                        print func
                        return "In wrapper." + " " + f(*args, **kw)
                    return wrapper
                return outer
            else :
                def wrapper(*args, **kw):
                    return "In wrapper." + " " + func(*args, **kw)
                return wrapper
        @log("execute")
        def f():
            return "In f"
        print f()

    def partialTest(self):
        import functools
        max5 = functools.partial(max, 5)
        print max5(1, 2, 3)

    def bindingTest(self):
        class C(object):
            pass
        c = C()
        from types import MethodType

        def test(self):
            print "This is a test"
        # the function can only bind a instance
        C.test = MethodType(test, None, C)
        # also:
        # C.test = test
        # How about realization
        c.test()

    def propertySetterDemo(self):
        class C(object):
            @property
            def score(self):
                return self.__score
            @score.setter
            def score(self, val):
                self.__score = val
        c = C()
        c.score = 90
        print c.score

    def mixinDemo(self):
        # a class mix-in demo
        class B1(object):
            def __init__(self):
                print "In B1 __init__."

            def B1(self):
                print "In B1 B1"

        class B2(object):
            def __init__(self):
                print "In B2 __init__."

            def B2(self):
                print "In B2 B2"

        class C(B1, B2):
            def __init__(self):
                B1.__init__(self)
                B2.__init__(self)
                # only B1 is initialized:
                # super(C, self).__init__()
                print "In C __init__"
        c = C()
        c.B1()

    def custom_class(self):
        # customize the class by __xx__ like functions
        class C(object):
            def __getitem__(self, item):
                if isinstance(item, int):
                    return item + 1
                if isinstance(item, slice):
                    return [x+1 for x in range(item.start, item.stop) ]

            def __call__(self, n):
                return n+1
        c = C()
        print c[1:5]
        print c(1)

    def dynamic_compiling(self):
        # class is constructed while running
        def f(self):
            print "In f."
        C = type('C', (object,), dict(debug=f))
        c = C()
        print type(C)
        print type(c)
        c.debug()

    def try_catch(self):
        # a python try... catch demo
        def f():
            raise StandardError("My customized error.")
        try:
            f()
            print "try"
        except StandardError, e:
            print e
        finally:
            print "finally"

    def set_trace(self):
        import pdb
        d = dict(a=1,b=2,c=3)
        pdb.set_trace()
        print d

    def test_case_demo(self):
        def Abs(x):
            if x >= 0:
                return x
            else:
                return -x
        return Abs

    def test_doc_demo(self):
        print 'this is a test'

    def pickling_demo(self):
        import json
        d = dict(name='Tom', id=1)
        str = json.dumps(d)
        d2 = json.loads(str)
        print type(d2),d2
        j = json.dumps(str, default=lambda obj: obj.__dict__)
        str2 = json.loads(j, object_hook=lambda s: str(s))
        print type(str2), str2

    @classmethod
    def selfIntroduction(cls):
        print cls.selfIntroStr
if __name__ == '__main__':
    print 'Syntax Test'
    import sys
    args = sys.argv
    s = SyntaxTest()
    # s.closeureTest()
    # s.mapReduceTest()
    # s.lambdaTest()
    # s.decoratorTest()
    # s.decoratorTestBis()
    # s.partialTest()
    # SyntaxTest.selfIntroduction()
    # s.bindingTest()
    # s.propertySetterDemo()
    # s.mixinDemo()
    # s.custom_class()
    # s.dynamic_compiling()
    # s.try_catch()
    # s.set_trace()
    s.pickling_demo()
    # __name__ = '__doctest__'
if __name__ == '__unittest__':
    import unittest

    class TestFunAbs(unittest.TestCase):
        def setUp(self):
            print 'test set up'
            o = SyntaxTest()
            self.f = o.test_case_demo()

        def test_pos(self):
            self.assertEquals(self.f(3), 3)

        def test_neg(self):
            self.assertEquals(self.f(-3), 3)

        def test_zero(self):
            o = SyntaxTest()
            self.assertEquals(self.f(0), 0)
    unittest.main()
if __name__ == '__doctest__':
    import doctest
    doctest.testmod()
