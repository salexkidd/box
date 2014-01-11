class MapReduce:
    
    BREAK_BEFORE = 1
    BREAK_AFTER = 2
    
    def __init__(self, breakers=[], filters=[], processors=[], reducers=[]):
        self._breakers = breakers  
        self._filters = filters
        self._processors = processors        
        self._reducers = reducers
    
    def __call__(self, iterable):
        elements = self._map(iterable)
        reduced_elements = self._reduce(elements)
        return reduced_elements

    #Protected
    
    def _map(self, iterable):
        for element, *args in iterable:
            is_break = self._break(element, *args)
            if is_break == self.BREAK_BEFORE:
                break
            if not self._filter(element, *args):
                continue
            processed_element = self._process(element, *args)
            yield processed_element
            if is_break == self.BREAK_AFTER:
                break   
    
    def _break(self, element, *args):
        for breaker in self._breakers:
            is_break = breaker(element, *args)
            if is_break:
                return is_break
        return False 
    
    def _filter(self, element, *args):
        for fltr in self._filters:
            if not fltr(element, *args):
                return False
        return True
    
    def _process(self, element, *args):
        result = element
        for processor in self._processors:
            result = processor(result, *args)
        return result
    
    def _reduce(self, elements):
        result = elements
        for reducer in self._reducers:
            result = reducer(result)
        return result  