#Unit tests for Wikipedia Visualiser
import unittest
import requests
from Wikipedia_Visualiser import WebScraper, IDGenerator, Node, GraphNodes

class TestWebScraper(unittest.TestCase):

    def test_request_response(self):
        '''Test for response status code'''
        self.assertEqual(str(requests.get("https://simple.wikipedia.org/")), "<Response [200]>")

    def test_valid_article_1(self):
        '''Test for valid article (Planet)'''
        scrapeTest1 = WebScraper("https://simple.wikipedia.org/wiki/Planet")
        scrapeTest1._soup()
        self.assertTrue(scrapeTest1._validArticle())

    def test_valid_article_2(self):
        '''Test for valid article (Solar_System)'''
        scrapeTest2 = WebScraper("https://simple.wikipedia.org/wiki/Solar_System")
        scrapeTest2._soup()
        self.assertTrue(scrapeTest2._validArticle())

    def test_invalid_article_1(self):
        '''Test for invalid article (PLANET)'''
        scrapeTest3 = WebScraper("https://simple.wikipedia.org/wiki/PLANET")
        scrapeTest3._soup()
        self.assertFalse(scrapeTest3._validArticle())

    def test_invalid_article_2(self):
        '''Test for invalid article (Solarsystem)'''
        scrapeTest4 = WebScraper("https://simple.wikipedia.org/wiki/Solarsystem")
        scrapeTest4._soup()
        self.assertFalse(scrapeTest4._validArticle())

class TestIDGen(unittest.TestCase):

    def test_count(self):
        '''Test for ID count'''
        gen = IDGenerator()
        self.assertNotEqual(gen._count, gen._nextID())

class TestNodes(unittest.TestCase):

    # set up Node objects (normal data)
    cookie = Node(0, "Cookie", None) 
    applePie = Node(1, "Apple_pie", "wiki/Apple_pie") 

    def test_get_title(self):
        '''Test for replacing underscore with space'''
        self.assertEqual(self.applePie.getTitle(), "Apple pie")

    def test_get_url(self):
        '''Test for generating URLs'''
        self.assertEqual(self.cookie.getURL(), "https://simple.wikipedia.org/wiki/Cookie")
        self.assertEqual(self.applePie.getURL(), "https://simple.wikipedia.org/wiki/Apple_pie")

    def test_depth_1(self):
        '''Test for node expansion with a depth of 1'''
        self.applePie.expandNode(1)
        for lvl1 in self.cookie._childNodes:
            # leaf nodes should have no child nodes, so it should be an empty set
            self.assertEqual(lvl1._childNodes, set()) 

    def test_depth_2(self):
        '''Test for node expansion with a depth of 2'''
        self.cookie.expandNode(2)
        for lvl1 in self.cookie._childNodes:
            for lvl2 in lvl1._childNodes:
                # leaf nodes should have no child nodes, so it should be an empty set
                self.assertEqual(lvl2._childNodes, set())

class TestGraphNodes(unittest.TestCase):

    def createGraphNodes(self):
        # set up Node objects and GraphNodes attributes (normal data)
        graphNodes = GraphNodes
        cookie = Node(0, "Cookie", None)
        applePie = Node(1, "Apple_pie", "wiki/Apple_pie")
        graphNodes._nodeObjByID = {0:cookie, 1:applePie}
        graphNodes._nodeObjByTitle = {"Cookie":cookie, "Apple_pie":applePie}
        return graphNodes

    def test_find_by_valid_id(self):
        '''Test for finding a Node object with a valid ID'''
        findIDTest = self.createGraphNodes()
        node = findIDTest.findByID(1)
        self.assertIsNotNone(node)
        self.assertEqual(node.getTitle(), "Apple pie")

    def test_find_by_invalid_id(self):
        '''Test for finding a Node object with an invalid ID'''
        findIDTest = self.createGraphNodes()
        node = findIDTest.findByID(9)
        # ID does not exist in dictionary, should return None
        self.assertIsNone(node)

    def test_find_by_valid_title(self):
        '''Test for finding a Node object with a valid title'''
        findTitleTest = self.createGraphNodes()
        node = findTitleTest.findByTitle("Cookie")
        self.assertIsNotNone(node)
        self.assertEqual(node.getID(), 0)

    def test_find_by_invalid_title(self):
        '''Test for finding a Node object with an invalid title'''
        findTitleTest = self.createGraphNodes()
        node = findTitleTest.findByTitle("Orange")
        # title does not exist in dictionary, should return None
        self.assertIsNone(node)

    def test_clear_dictionary(self):
        '''Test for clearing dictionaries'''
        clearTest = self.createGraphNodes()
        clearTest.clearDict()
        self.assertEqual(clearTest._nodeObjByID, {})
        self.assertEqual(clearTest._nodeObjByTitle, {})

if __name__ == '__main__':      # boilerplate
    unittest.main(verbosity=2)




