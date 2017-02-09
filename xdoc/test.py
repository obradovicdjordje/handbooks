

class Box():
    """
        demo class
    """
    def testB(a, b):
        """api
            endpoint:/api/test
            method:GET
            args:[
                username,
                password]
            returns: 
                token
        """
        return a+b

    def testA(a, b):
        """api
            endpoint:/api/users
            method:GET
            returns: list of all users
        """
        return a*b

if __name__ == '__main__':
    print test(3, 5)
    print test2(3, 5)
