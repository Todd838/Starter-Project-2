class Boggle:
    def __init__(self, grid, dictionary):
        # Keep original grid to preserve case of multi-char cells
        self.grid_original = grid
        # Normalize grid to uppercase for comparison
        self.grid = [[cell.upper() if cell else "" for cell in row] for row in grid]
        # Store dictionary mappings (uppercase -> original case)
        self.dictionary_original = {word.upper(): word for word in dictionary}
        # Create uppercase set for searching
        self.dictionary = set(word.upper() for word in dictionary)
        self.solutions = []

    def setGrid(self, grid):
        self.grid_original = grid
        self.grid = [[cell.upper() if cell else "" for cell in row] for row in grid]

    def setDictionary(self, dictionary):
        self.dictionary_original = {word.upper(): word for word in dictionary}
        self.dictionary = set(word.upper() for word in dictionary)

    def getSolution(self):
        self.solutions = []

        if not self.grid:  # empty grid guard
            return []
        
        # Handle empty first row
        if not self.grid[0]:
            return []

        rows = len(self.grid)
        cols = len(self.grid[0])
        
        found = set()
        
        # Build prefixes for early pruning
        prefixes = set()
        for word in self.dictionary:
            for i in range(1, len(word)+1):
                prefixes.add(word[:i])

        def dfs(r, c, visited, current_word, current_word_upper):
            # Check boundaries FIRST before accessing grid
            if r < 0 or r >= rows:
                return
            if c < 0 or c >= len(self.grid[r]):  # Check column bounds per row
                return
            if (r, c) in visited:
                return

            cell = self.grid[r][c]
            cell_original = self.grid_original[r][c] if r < len(self.grid_original) and c < len(self.grid_original[r]) else cell
            
            # Skip empty cells
            if not cell:
                return
            
            # Handle multi-letter cells (Qu, St, Ie) - use original case
            if cell == "QU":
                new_word = current_word + cell_original
                new_word_upper = current_word_upper + "QU"
            elif cell == "ST":
                new_word = current_word + cell_original
                new_word_upper = current_word_upper + "ST"
            elif cell == "IE":
                new_word = current_word + cell_original
                new_word_upper = current_word_upper + "IE"
            else:
                new_word = current_word + cell_original
                new_word_upper = current_word_upper + cell

            # Early pruning: if current word is not a prefix of any dictionary word, stop
            if new_word_upper not in prefixes:
                return

            # Check if we found a valid word (>= 3 characters)
            if len(new_word_upper) >= 3 and new_word_upper in self.dictionary:
                found.add(new_word)

            # Mark cell as visited
            visited.add((r, c))
            
            # Explore all 8 neighbors
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    dfs(r + dr, c + dc, visited, new_word, new_word_upper)
            
            # Backtrack: unmark cell
            visited.remove((r, c))

        # Start DFS from each cell
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, set(), "", "")

        # Return words in their found case, sorted
        self.solutions = sorted(list(found), key=str.upper)
        return self.solutions
