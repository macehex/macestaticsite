import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_prop_to_html_method(self):
        node = HTMLNode(
            "h1",
            "Very big header",
        )


if __name__ == "__main__":
    unittest.main()
