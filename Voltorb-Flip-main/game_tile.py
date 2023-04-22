from pygame import sprite, image, time

clock = time.Clock()

class Tile(sprite.Sprite):

  # Constructor. Pass in the color of the block,
  # and its x and y position
  def __init__(self, name, value, xCoords, yCoords):
    __name__ = name
    self.value = value
    self.xCoords = xCoords
    self.yCoords = yCoords
  # Call the parent class (Sprite) constructor
    sprite.Sprite.__init__(self)

    self.flip_images = [
                    image.load(r"Voltorb-Flip-main\Asssets\Tile Flip Animation Frames\flip_0.png"), 
                    image.load(r"Voltorb-Flip-main\Asssets\Tile Flip Animation Frames\flip_1.png"), 
                    image.load(r"Voltorb-Flip-main\Asssets\Tile Flip Animation Frames\flip_2.png"),
                    image.load(r"Voltorb-Flip-main\Asssets\Tile Flip Animation Frames\1_flip.png")
                     ]

    tile_image = r"Voltorb-Flip-main\Asssets\voltorb_flip_tile.png"

    # Load generic tile image
    self.image = image.load(tile_image)


    # Fetch the rectangle object that has the dimensions of the image
    # Update the position of this object by setting the values of rect.x and rect.y
    self.rect = self.image.get_rect()
    self.rect.right = xCoords
    self.rect.top = yCoords          

  # plays animation for flipping tile
  def flip_tile(self, screen, display):
    for frames in self.flip_images:

      # gets next frame
      current_frame = frames.convert()
      self.image = current_frame
      screen.blit(current_frame, (self.xCoords - 78, self.yCoords))

      # updates display
      display.flip()
      clock.tick(10)
      screen.fill((82,162,111), rect=self.rect)
    screen.blit(self.flip_images[3], (self.xCoords - 78, self.yCoords))


