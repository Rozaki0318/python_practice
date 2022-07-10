class Cal(object):
    def add_num_and_double(self, x, y):
        """
        >>> c = Cal()
        >>> c.add_num_and_double(1, 1)
        5
        """
        result = x + y
        result *= 2
        return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()