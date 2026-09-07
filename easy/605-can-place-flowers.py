class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:

      #No need to continue if we do not need to plant any flowers
      if n == 0:
        return True

      #Establish a counter variable to keep track of flowers that will be planted
      counter = 0

      for i in range(len(flowerbed)):

        if flowerbed[i] == 0:

          #Check the first position
          if i == 0:
            if len(flowerbed) == 1 or flowerbed[i + 1] == 0:
              counter += 1
              flowerbed[i] = 1

          #Check the last position
          elif i == len(flowerbed) - 1:
            if flowerbed[i - 1] == 0:
              counter += 1
              flowerbed[i] = 1

          #Check middle positions
          else:
            if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
              counter += 1
              flowerbed[i] = 1

          if counter == n:
            return True

      return counter >= n