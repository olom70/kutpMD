class IterRegistry(type):
    '''
        To :
        - identify instances at creation
        - be able to iterate all instances (to save them)
    '''
    def __iter__(cls):
        return iter(cls._registry)