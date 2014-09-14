__author__ = 'Kalyan'

from placeholders import *

# instead of returning a list of tuples like zip, generate it incrementally (refer to the generators and iterators lessons)
# a tuple at a time. Use exception control flow to write elegant code.
def generator_zip(seq1, seq2, *more_seqs):
    x=tuple(seq1)
    y=tuple(seq2)
    iterables=[x, y]
    count=min(len(x),len(y))
    if(more_seqs):
        z=more_seqs
        for i in range(len(z)):
            a=z[i]
            iterables.append(a)
            count=min(count,len(a))
    iterables=tuple(iterables)

    for k in range(count):
        b=[];
        it=iter(iterables)
        for j in range(len(iterables)):
            try:
                c=it.next()[k]
                b.append(c)
            except StopIteration:
                continue
        yield tuple(b)

def check_generator(gen, max_count, tuple_length):
    for x in range(max_count):
        result = next(gen)
        assert len(result) == tuple_length, "invalid length"
        for element in result:
            assert x == element, "unexpected value"

    try:
        next(gen)
        assert False, "generator did not finish as expected"
    except StopIteration as se:
        pass

def test_generator_zip():
    gen = generator_zip(range(5), range(3), range(4), range(5))
    assert type(gen).__name__ == 'generator'
    check_generator(gen, 3, 4)

    gen = generator_zip(range(5), range(3), range(2))
    assert type(gen).__name__ == 'generator'
    check_generator(gen, 2, 3)

    gen = generator_zip((1,2), "abcd")
    assert [(1,'a'), (2, 'b')] == list(gen)

    gen = generator_zip(range(1,5), "abc", [1,2])
    assert [(1,'a', 1), (2, 'b', 2)] == list(gen)



three_things_i_learnt = """
-The actual working of the zip function.
-Writing a code to implement the copy of the zip function using iterator.
-Exception flow control can work if we have no more data to fetch.. Just put in the try catch block
your code is done. :)
"""

time_taken_minutes = 180