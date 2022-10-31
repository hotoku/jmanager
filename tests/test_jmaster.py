#!/usr/bin/env python

"""Tests for `jmanager` package."""


import unittest
from click.testing import CliRunner
import tempfile

from jmanager import jmanager


class TestJmaster(unittest.TestCase):
    """Tests for `jmanager` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        help_result = runner.invoke(jmanager.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output

    def test_find_pid_file(self):
        """Test find_pid_file."""
        with tempfile.TemporaryDirectory() as td:
            print(td)
        
