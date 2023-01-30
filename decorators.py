import os
import datetime


def logger(old_function):
    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)

        start = datetime.datetime.now()
        name = new_function.__name__()
        info = f' В {start} была вызвана функция {name} с аргументами {args} и {kwargs}, возвращающая {result}.'

        with open("main.log", 'w+') as file:
            file.write(info)

    return new_function


def test_1():
    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    def hello_world():
        return 'Hello World'

    @logger
    def summator(a, b=0):
        return a + b

    @logger
    def div(a, b):
        return a / b

    assert 'Hello World' == hello_world()
    result = summator(2, 2)
    assert isinstance(result, int)
    assert result == 4
    result = div(6, 2)
    assert result == 3

    assert os.path.exists(path)

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path) as log_file:
        log_file_content = log_file.read()

    assert 'summator' in log_file_content
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content


if __name__ == '__main__':
    test_1()

#########################################################################################################################

import os
import datetime

def logger(path):
    name_file = path

    def __logger(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            start = datetime.datetime.now()
            name = new_function.__name__()
            info = f' В {start} была вызвана функция {name} с аргументами {args} и {kwargs}, возвращающая {result}.'

            with open(name_file, 'w+') as file:
                file.write(info)

        return new_function

    return __logger


def test_2():
    paths = ('log_1.log', 'log_2.log', 'log_3.log')

    for path in paths:
        if os.path.exists(path):
            os.remove(path)

        @logger(path)
        def hello_world():
            return 'Hello World'

        @logger(path)
        def summator(a, b=0):
            return a + b

        @logger(path)
        def div(a, b):
            return a / b

        assert 'Hello World' == hello_world()
        result = summator(2, 2)
        assert isinstance(result, int)
        assert result == 4
        result = div(6, 2)
        assert result == 3
        summator(4.3, b=2.2)

    for path in paths:

        assert os.path.exists(path)

        with open(path) as log_file:
            log_file_content = log_file.read()

        assert 'summator' in log_file_content

        for item in (4.3, 2.2, 6.5):
            assert str(item) in log_file_content


if __name__ == '__main__':
    test_2()


#########################################################################################################################
import os
import datetime

def logger(old_function):
    def new_function(*args):
        result = old_function(*args)

        start = datetime.datetime.now()
        name = new_function.__name__()
        info = f' В {start} была вызвана функция {name} с аргументами {args} , возвращающая {result}.'

        with open("flat.log", 'w+') as file:
            file.write(info)

    return new_function

@logger
def flat_generator(list_of_lists):
    current = 0
    circle_1 = 0
    circle_2 = 0
    result = []
    while circle_1 < len(list_of_lists):
        if current == 0:
            object_list = list_of_lists[circle_1]
            circle_1 +=1
            current +=1
            if circle_2 < len (object_list):
                while circle_2 <len(object_list):
                    result.append(object_list[circle_2])
                    circle_2 +=1
        else:
            circle_2 = 0
            current = 0
    yield result

def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


