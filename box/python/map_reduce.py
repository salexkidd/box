class MapReduce:
    
    def __init__(self, filters=[], iterators=[], processors=[], reducers=[]):
        self._fiters = filters
        self._iterators = iterators
        self._processors = processors
        self._reducers = reducers
    
    def __call__(self, iterable):
        elements = self._map(iterable)
        reduced_elements = self._reduce(elements)
        return reduced_elements

    #Protected
    
    def _map(self, iterable):
        for element, *args in iterable:
            if not self._filter(element, *args):
                continue
            if not self._iterate(element, *args):
                continue
            processed_element = self._process(element, *args)
            yield processed_element
    
    def _filter(self, element, *args):
        for fltr in self._filters:
            if not fltr(element, *args):
                return False
        return True
    
    def _iterate(self, element, *args):
        for iterator in self._iterators:
            if not iterator(element, *args):
                return False
        return True    
    
    def _process(self, element, *args):
        processed_element = element
        for processor in self._processors:
            processed_element = processor(processed_element, *args)
        return processed_element
    
    def _reduce(self, elements):
        reduced_elements = elements
        for reducer in self.reducers:
            reduced_elements = reducer(reduced_elements)
        return reduced_elements  