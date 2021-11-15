
def subgen():
    while True:
        try:
            message = yield
            print(f'>>> {message=}')
        except ValueError:
            print('Done!')
            break
    return 'subgen execution result'


def delegator1(sg):
    next(sg)
    while True:
        try:
            data = yield
            sg.send(data)
        except ValueError as err:
            try:
                sg.throw(err)
            except StopIteration as err:
                sg_result = err.value
                break
    print(f'{sg_result =}')


def delegator2(sg):
   sg_result = yield from sg
   print(f'{sg_result=}')

