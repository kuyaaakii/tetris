moving_tetrominos = []
        for tetromino in self.tetrominos:
            for y,arrays in enumerate(tetromino.shape[tetromino.rotation]):
                if tetromino.point_y + y in self.full_lines:
                    for x in range(len(arrays)):
                        tetromino.shape[tetromino.rotation][y][x] = 0
        print(self.matrix[19])                
        for tetromino in self.tetrominos:
            print("jabol")
            tetromino.moving = 1
            moving_tetrominos.append(tetromino)
        self.tetrominos.clear()

        for tetromino in moving_tetrominos:    
            while tetromino.moving:
                tetromino.update_y()
            self.tetrominos.append(tetromino)