def average_gen():
    count, sum, average = 0, 0, None
    while True:
        try:
            x = yield average
        except StopIteration:
            print('Done')
            break
        else:
            count += 1
            sum += x
            average = round(sum / count, 2)
    return average


g = average_gen()
next(g)
g.send(5)
