import unittest
from unittest.mock import Mock
from box.argparse.program import Program

class ProgramTest(unittest.TestCase):

    #Public

    def setUp(self):
        MockProgram = self._make_program_mock_class()
        self.argv = ['prog', 'argument']
        self.program = MockProgram(self.argv)
        
    def test__command(self):
        self.assertEqual(self.program._command, 'command')
        self.program._command_class.assert_called_with(
            ['prog', 'argument'], 
            config={'prog': 'programmock', 'kwarg': 'kwarg'})
        
    #Protected
    
    def _make_program_mock_class(self):
        class ProgramMock(Program):
            #Public
            __call__ = Mock()
            #Protected
            _command_class = Mock(
                config={'kwarg': 'kwarg'},
                return_value='command')
        return ProgramMock