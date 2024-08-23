import sys
import os
import unittest

sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'../src')))
                                  
from outfit_recommender import recommend_outfit

class TestOutfitRecommender(unittest.TestCase):
    def test_recommend_outfit(self):
        self.assertEqual(recommend_outfit(30,'cold')," Heavy coat, woolen scarf,gloves, and boots.")
        self.assertEqual(recommend_outfit(20,'cool'),"Jacket, jeans, and a beanie.")
        self.assertEqual(recommend_outfit(10,'warm'),"T-shirt,jeans, and sneakers.")
        self.assertEqual(recommend_outfit(20,'hot'),"shorts,tank top, and flip-flops.")

if __name__ == '__main__':
    unittest.main()
