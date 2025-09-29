import unittest
import sys

# Add path to find your Boggle solver module
sys.path.append("/home/codio/workspace/")
from boggle_solver import Boggle


# --- Category 1: Normal Input Cases ---
class TestSuite_Normal_Cases(unittest.TestCase):
    """Test normal operation with valid inputs"""
    
    def test_Normal_case_3x3(self):
        """Test basic 3x3 grid with simple words"""
        grid = [
            ["A", "B", "C"],
            ["D", "E", "F"],
            ["G", "H", "I"]
        ]
        dictionary = ["ABC", "ABDHI", "CFI"]
        mygame = Boggle(grid, dictionary)
        solution = [x.upper() for x in mygame.getSolution()]
        expected = [x.upper() for x in dictionary]
        self.assertEqual(sorted(solution), sorted(expected))

    def test_Normal_case_5x5(self):
        """Test medium 5x5 grid"""
        grid = [
            ["A","B","C","D","E"],
            ["F","G","H","I","J"],
            ["K","L","M","N","O"],
            ["P","Q","R","S","T"],
            ["U","V","W","X","Y"]
        ]
        dictionary = ["ABC", "FGH", "KLM", "PQR", "UVW"]
        mygame = Boggle(grid, dictionary)
        solution = [x.upper() for x in mygame.getSolution()]
        expected = [x.upper() for x in dictionary]
        self.assertEqual(sorted(solution), sorted(expected))


# --- Category 2: Edge Cases ---
class TestSuite_Edge_Cases(unittest.TestCase):
    """Test boundary conditions and edge cases"""
    
    def test_EmptyGrid_case_0x0(self):
        """Test with empty grid"""
        grid = [[]]
        dictionary = ["HELLO", "THERE"]
        mygame = Boggle(grid, dictionary)
        solution = [x.upper() for x in mygame.getSolution()]
        expected = []
        self.assertEqual(sorted(solution), sorted(expected))

    def test_SquareGrid_case_1x1(self):
        """Test minimum grid size (words must be 3+ chars)"""
        grid = [["A"]]
        dictionary = ["A", "B", "C"]
        mygame = Boggle(grid, dictionary)
        solution = [x.upper() for x in mygame.getSolution()]
        expected = []  # cannot form words >= 3 chars
        self.assertEqual(sorted(solution), sorted(expected))

    def test_No_Words_In_Grid(self):
        """Test when dictionary words don't exist in grid"""
        grid = [
            ["A", "B", "C"],
            ["D", "E", "F"],
            ["G", "H", "I"]
        ]
        dictionary = ["XYZ", "QQQ", "ZZZ"]
        mygame = Boggle(grid, dictionary)
        solution = [x.upper() for x in mygame.getSolution()]
        expected = []
        self.assertEqual(sorted(solution), sorted(expected))

    def test_Empty_Dictionary(self):
        """Test with empty dictionary"""
        grid = [
            ["A", "B", "C"],
            ["D", "E", "F"],
            ["G", "H", "I"]
        ]
        dictionary = []
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        expected = []
        self.assertEqual(solution, expected)


# --- Category 3: Problem Constraints ---
class TestSuite_Constraints(unittest.TestCase):
    """Test specific problem constraints"""
    
    def test_Words_That_Only_Are_3_or_More_Chars(self):
        """Test minimum word length constraint (3 characters)"""
        grid = [
            ["A", "B", "C"],
            ["D", "E", "F"],
            ["G", "H", "I"]
        ]
        dictionary = ["AB", "A", "ABC", "DEF"]  # Only ABC and DEF are valid
        mygame = Boggle(grid, dictionary)
        solution = [x.upper() for x in mygame.getSolution()]
        expected = ["ABC", "DEF"]
        self.assertEqual(sorted(solution), sorted(expected))

    def test_Words_Cant_Use_Cell_More_Than_Once(self):
        """Test that same cell cannot be reused in a word"""
        grid = [
            ["A", "B", "C"],
            ["D", "E", "F"],
            ["G", "H", "I"]
        ]
        dictionary = ["ABA", "AEA"]  # These would require reusing 'A'
        mygame = Boggle(grid, dictionary)
        solution = [x.upper() for x in mygame.getSolution()]
        expected = []  # Should not find words that reuse cells
        self.assertEqual(sorted(solution), sorted(expected))

    def test_Duplicate_Letters_Allowed_Different_Cells(self):
        """Test that different cells with same letter can both be used"""
        grid = [
            ["A", "B", "A"],
            ["D", "E", "F"],
            ["G", "H", "I"]
        ]
        dictionary = ["ABA"]  # Using both A cells
        mygame = Boggle(grid, dictionary)
        solution = [x.upper() for x in mygame.getSolution()]
        expected = ["ABA"]
        self.assertEqual(sorted(solution), sorted(expected))


# --- Category 4: Complex Patterns ---
class TestSuite_Complex_Patterns(unittest.TestCase):
    """Test complex word patterns and paths"""
    
    def test_All_Eight_Directions(self):
        """Test words can be formed in all 8 directions"""
        grid = [
            ["A", "B", "C"],
            ["H", "I", "D"],
            ["G", "F", "E"]
        ]
        # Can form: ABC (right), AHG (down), BID (diagonal), DEF (left), FED (right)
        dictionary = ["ABC", "AHG", "BID", "FED"]
        mygame = Boggle(grid, dictionary)
        solution = [x.upper() for x in mygame.getSolution()]
        expected = [x.upper() for x in dictionary]
        self.assertEqual(sorted(solution), sorted(expected))

    def test_Winding_Path(self):
        """Test words that wind through the grid"""
        grid = [
            ["A", "B", "C"],
            ["H", "G", "D"],
            ["I", "F", "E"]
        ]
        dictionary = ["ABCDEFGHI"]  # Winds around entire grid
        mygame = Boggle(grid, dictionary)
        solution = [x.upper() for x in mygame.getSolution()]
        expected = ["ABCDEFGHI"]
        self.assertEqual(sorted(solution), sorted(expected))


# --- Category 5: Special Cases (Qu, St, Ie) ---
class TestSuite_Special_Cells(unittest.TestCase):
    """Test handling of multi-character cells"""
    
    def test_Simple_Qu_Case(self):
        """Test basic Qu cell handling"""
        grid = [
            ["Qu","A","B"],
            ["C","D","E"],
            ["F","G","H"]
        ]
        dictionary = ["QUAD"]
        mygame = Boggle(grid, dictionary)
        solution = [x.upper() for x in mygame.getSolution()]
        expected = ["QUAD"]
        self.assertEqual(sorted(solution), sorted(expected))

    def test_Simple_St_Case(self):
        """Test basic St cell handling"""
        grid = [
            ["St","A","B"],
            ["C","D","E"],
            ["F","G","H"]
        ]
        dictionary = ["STAB"]
        mygame = Boggle(grid, dictionary)
        solution = [x.upper() for x in mygame.getSolution()]
        expected = ["STAB"]
        self.assertEqual(sorted(solution), sorted(expected))


if __name__ == '__main__':
    unittest.main()
