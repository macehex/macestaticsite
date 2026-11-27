import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_noteq(self):
        node = TextNode("this is a text node", TextType.TEXT)
        node2 = TextNode("this is another text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_url(self):
        node = TextNode("this is a text node with no url", TextType.TEXT)
        node2 = TextNode("this is a text node with  url", TextType.TEXT, "bootdev.com")
        self.assertNotEqual(node, node2)

    def test_propertyeq(self):
        node = TextNode("this is a text node with no url", TextType.BOLD)
        node2 = TextNode("this is a text node with  url", TextType.LINK, "bootdev.com")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
