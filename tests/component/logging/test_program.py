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
        
    @patch('logging.getLogger')
    def test___call___with_error(self, get_logger):
        self.program._execute = Mock(side_effect=Exception('exception'))
        self.assertRaises(SystemExit, self.program)
        get_logger.assert_called_with('box.logging.program')
        get_logger.return_value.error.assert_called_with(
            'exception', exc_info='debug')   
    
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