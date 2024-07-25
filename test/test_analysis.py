import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


import unittest
import pandas as pd
from src.analysis import perform_analysis

class TestAnalysis(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create a sample DataFrame
        cls.data = pd.DataFrame({
            'X': [1, 2, 3, 4, 5],
            'Y': [2, 4, 6, 8, 10]
        })
    
    def test_perform_analysis(self):
        results = perform_analysis(self.data)
        
        # Check if results contain expected keys
        self.assertIn('intercept', results)
        self.assertIn('slope', results)
        self.assertIn('mean_squared_error', results)
        self.assertIn('r_squared', results)
        self.assertIn('plot', results)
        
        # Check that numerical results are floats
        self.assertIsInstance(results['intercept'], float)
        self.assertIsInstance(results['slope'], float)
        self.assertIsInstance(results['mean_squared_error'], float)
        self.assertIsInstance(results['r_squared'], float)
        
        # Check if plot is a valid base64 string
        self.assertIsInstance(results['plot'], str)
        # self.assertTrue(results['plot'].startswith('iVBORw0KGgo='))  # Simple base64 check
        
        # Additional checks to ensure the base64 string decodes to a valid PNG image
        import base64
        from PIL import Image
        import io
        
        try:
            img_data = base64.b64decode(results['plot'])
            img = Image.open(io.BytesIO(img_data))
            img.verify()  # Verifies the image data
        except Exception as e:
            self.fail(f"Plot image could not be verified: {e}")

if __name__ == '__main__':
    unittest.main()
