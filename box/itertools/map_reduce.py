class MapReduce:
    """MapReduce function-class"""
    
    BREAK_BEFORE = 1
    BREAK_AFTER = 2
    
    def __call__(self, iterable, 
                 breakers=[], filters=[], processors=[], reducers=[]):
        elements = self._map(iterable, breakers, filters, processors)
        reduced_elements = self._reduce(elements, reducers)
        return reduced_elements

    #Protected
    
    def _map(self, iterable, breakers, filters, processors):
        for element, *args in iterable:
            is_break = self._break(breakers, element, *args)
            if is_break == self.BREAK_BEFORE:
                break
            if not self._filter(filters, element, *args):
                continue
            processed_element = self._process(processors, element, *args)
            yield processed_element
            if is_break == self.BREAK_AFTER:
                break
    
    def _reduce(self, elements, reducers):
        result = elements
        for reducer in reducers:
            result = reducer(result)
        return result
    
    def _break(self, breakers, element, *args):
        for breaker in breakers:
            is_break = breaker(element, *args)
            if is_break:
                return is_break
        return False 
    
    def _filter(self, filters, element, *args):
        for fltr in filters:
            if not fltr(element, *args):
                return False
        return True
    
    def _process(self, processors, element, *args):
        result = element
        for processor in processors:
            result = processor(result, *args)
        return result
    

map_reduce = MapReduce()