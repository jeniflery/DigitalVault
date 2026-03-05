# test_digitalvault.py
"""
Tests for DigitalVault module.
"""

import unittest
from digitalvault import DigitalVault

class TestDigitalVault(unittest.TestCase):
    """Test cases for DigitalVault class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DigitalVault()
        self.assertIsInstance(instance, DigitalVault)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DigitalVault()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
