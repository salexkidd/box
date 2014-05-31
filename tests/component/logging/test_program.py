import logging
import unittest
from unittest.mock import Mock, call, patch
from box.logging.program import LoggingProgram

class LoggingProgramTest(unittest.TestCase):

    #Public

    def setUp(self):
        self.MockProgram = self._make_mock_program_class()
        self.program = self.MockProgram('argv')
    
    @patch('logging.config')
    @patch('logging.getLogger')
    def test___call__(self, get_logger, logging_config):
        self.program()
        logging_config.dictConfig.assert_called_with(
            self.program._settings.logging)
        get_logger.assert_called_with()
        get_logger.return_value.setLevel.assert_has_calls([
            call(logging.DEBUG),
            call(logging.INFO),
            call(logging.ERROR)])
        self.program._execute.assert_called_with()   
    
    #Protected
    
    def _make_mock_program_class(self):
        class MockProgram(LoggingProgram):
            #Protected
            _execute = Mock()
            _command_class = Mock(return_value=Mock(
                debug='debug',
                verbose='verbose',
                quiet='quiet'))
        return MockProgram