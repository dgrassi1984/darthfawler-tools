import unittest

from search_on_amazon import SearchOnAmazonTool, SearchOnAmazonInput


class SearchOnAmazonTestCase(unittest.TestCase):
    def setUp(self):
        self.tool = SearchOnAmazonTool()

    def test_tool_args_schema(self):
        self.assertEqual(self.tool.args_schema, SearchOnAmazonInput)

    def test_execute_method(self):
        input = SearchOnAmazonInput(query="macbook pro m2")
        output = self.tool._execute(query=input.query)
        self.assertIsInstance(output, list)
        self.assertGreater(len(output), 0)
