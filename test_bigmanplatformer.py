import unittest
import pygame
from bigmanplatformer import *

if __name__ == '__main__':
    class testLoad_Files(unittest.TestCase):
        def test_detected(self):
            #checks if the files are seen
            self.assertIsNotNone(load_assets(assets_path))
    