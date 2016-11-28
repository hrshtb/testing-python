#! /usr/bin/env python2

"""
Checking working and order of the super parameters in Python 2.x
"""

# Conclusion from the code is that in Python 2.x where we have to pass
# parameters in the super function the first parameter describes what next
# part of mro should the super call, eg., if mro is [E,D,C,B,A,object]
# passing D as the first argument in a super function in an E function it would
# call C's function instead of D's function which is next in mro for E.
# The second argument describes which object's mro are we calculating the
# call's in. function's signature : super(type->class, object->a class object)

import operator

class TestingMetaClass(type):
    def __init__(cls, base_classes=[], attr_dict={}):
        self.base_classes = base_classes

    def __new__(cls, name, bases, attrs):
	super.__new__(cls, name, bases, attrs)

    def __call__(self, *args, **kwargs):


class Parent1(object, metaclass=TestingMetaClass):
    def __init__(self, print_val_test=None):
        print("The value of the string : ", print_val_test)

    def sum(self, first_num=None, second_num=None):
        print("The sum is : ", str(first_num + second_num))


class Parent2(object):
    def __init__(self, print_val_test=None):
        print("The value which should for sure be of the string : ",
              print_val_test)

    def sum(self, first_num=None, second_num=None):
        print("The sum is now mul : ", operator.mul(first_num, second_num))


class Child2(Parent2):
    def __init__(self, string_to_pass=None):
        if not string_to_pass:
            pass
        else:
            super(Child2, self).__init__('Call from child1')
            print('Is coming here')
            super(Child2, self).sum(12, 34)


class Child1(Parent1):
    def __init__(self, string_to_pass=None):
        if not string_to_pass:
            pass
        else:
            super(Child1, self).__init__('Call from child1')
            print('Is coming here')
            super(Child1, self).sum(12, 34)


class GrandChild(Child2, Child1):
    def __init__(self, class_object_to_call=None):
        super(Child2, Child2()).__init__('Call from GrandChild')
        # super(self, class_object_to_call).sum(12,34)


if __name__ == "__main__":
    # p1 = Parent1('Initiating 1')
    # p2 = Parent2('Initiating 2')
    # c1 = Child1(p1)
    gc1 = GrandChild(Child2())
    # gc2 = GrandChild()
