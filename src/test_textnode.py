import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        
        node3 = TextNode("This is a text node", TextType.ITALIC, "https://www.google.com/")
        node4 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node3, node4)
        
        node5 = TextNode("This is a text node", TextType.LINK,)
        node6 = TextNode("This is a text node", TextType.IMAGE)
        self.assertNotEqual(node5, node6)
        
        node7 = TextNode("This is a text node", TextType.BOLD)
        node8 = TextNode("This is not a text node", TextType.BOLD)
        self.assertNotEqual(node7, node8)


if __name__ == "__main__":
    unittest.main()