#!/usr/bin/python3
"""This module defines tests for the console"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """The unittests for the class HBNBCommand"""

    def tearDown(self):
        """Cleans the test environment"""

        self.console = None

    def test_quit_command(self):
        """Test the quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd('quit'))
            self.assertEqual(f.getvalue(), 'Good Bye!\n')

    def test_EOF_command(self):
        """Tests the end of file command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd('EOF'))
            self.assertEqual(f.getvalue(), '\n')

    def test_emptyline_command(self):
        """This tests the empty line command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertIsNone(HBNBCommand().onecmd(''))
            self.assertEqual(f.getvalue(), '')

    def test_create_command(self):
        """This tests for create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create BaseModel')
            output = f.getvalue().strip()
            self.assertTrue(len(output) > 0)

    def test_show_command(self):
        """This tests for the show command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show BaseModel 0789-5647-5487')
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_destroy_command(self):
        """This tests for the destroy command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show BaseModel 0789-5647-5487')
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_all_command(self):
        """This tests for all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all')
            output = f.getvalue().strip()
            self.assertTrue(len(output) > 0)

    def test_update_command(self):
        """This tests for the update command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                  'update BaseModel 0789-5647-5487 name "Betty Smith"')
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_help(self):
        """This tests the help command"""
        hp = "Quit command to exit the program"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(hp, output.getvalue().strip())

    def test_create_missing_class_name(self):
        """This tests create command with missing class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create')
            output = f.getvalue().strip()
            self.assertEqual(output, '** class name missing **')

    def test_show_missing_class_name(self):
        """This tests for the show command missing class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show')
            output = f.getvalue().strip()
            self.assertEqual(output, '** class name missing **')

    def test_destroy_missing_class_name(self):
        """This tests for destroy command missing class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('destroy')
            output = f.getvalue().strip()
            self.assertEqual(output, '** class name missing **')

    def test_update_missing_class_name(self):
        """This tests for update command with missing class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('update')
            output = f.getvalue().strip()
            self.assertEqual(output, '** class name missing **')

    def test_show_missing_instance_id(self):
        """Tests the show command with missing instance id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show BaseModel')
            output = f.getvalue().strip()
            self.assertEqual(output, '** instance id missing **')

    def test_destroy_missing_instance_id(self):
        """This tests the destroy command with missing instance id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('destroy BaseModel')
            output = f.getvalue().strip()
            self.assertEqual(output, '** instance id missing **')

    def test_update_missing_instance_id(self):
        """This tests update command with missing instance id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('update BaseModel')
            output = f.getvalue().strip()
            self.assertEqual(output, '** instance id missing **')

    def test_user_show_command(self):
        """This tests for show command for user class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show User 0789-5647-5487')
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_user_destroy_command(self):
        """This tests the destroy command for class User"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('destroy User 0789-5647-5487')
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_base_model_show_command(self):
        """This tests for show command for class BaseMosel"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show BaseModel 0789-5647-5487')
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_base_model_destroy_command(self):
        """This tests for destroy command for class BaseModel"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('destroy BaseModel 0789-5647-5487')
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")


if __name__ == '__main__':
    unittest.main()
