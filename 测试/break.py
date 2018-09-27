def foo():
    print('I am foo')


def bar():
    print('I am bar')


# 函数都是对象，所以既可以有属性，又可以作为属性
# 下面bar被定义为foo的属性
foo.bar = bar
foo.bar()
print(type(foo))


def deco(func):
    string = 'I am deco'

    def wrapper():
        print(string)
        func()

    return wrapper


def foo():
    print('I am foo')


# 第一句话赋值，但没有输出。把函数foo作为参数传递给deco函数得到返回值wrapper
# wrapper是一个定义在函数里的函数，打印一个string 并且执行传递进来的foo。
foo = deco(foo)
foo()
"""
输出:
I am deco
Iam foo
"""
print(foo.__closure__)


def print_msg(msg):
    """This is the outer enclosing function"""
    def printer():
        """This is the nested function"""
        print(msg)
    return printer

# Now let's try calling this function.
# Output: Hello
another = print_msg("Hello")
another()


def a():

    return max(r for r in range(5))

