#!/usr/bin/env python

"""Tests for `jmanager` package."""


import unittest
import tempfile
import os

from click.testing import CliRunner

from jmanager import jmanager


class TestJmanager(unittest.TestCase):
    """Tests for `jmanager` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_command_line_interface(self):
        """Test the CLI.

        A sample of testing cli by click.
        """
        runner = CliRunner()
        help_result = runner.invoke(jmanager.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output

    def test_find_pid_file(self):
        """Test find_pid_file."""
        with tempfile.TemporaryDirectory() as td:
            ret = jmanager.find_pid_file(td)
            assert ret is None
            open(os.path.join(td, jmanager._PID_FILE), "w").close()
            ret2 = jmanager.find_pid_file(td)
            assert ret2 == td
            path = os.path.join(td, "a/b/c/d/e/f")
            os.makedirs(path)
            ret3 = jmanager.find_pid_file(path)
            assert ret3 is not None
            assert ret3 == td
