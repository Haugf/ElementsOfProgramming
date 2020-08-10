def fruits_into_baskets(fruits):
  window_start = 0
  max_length = 0
  fruit_freq = {}

  for window_end in range(len(fruits)):

    # Add the fruit into the map
    end_fruit = fruits[window_end]
    if end_fruit not in fruit_freq:
      fruit_freq[end_fruit] = 0
    fruit_freq[end_fruit] += 1

    # check for maximum len, shrink start of window until we have an empty fruit basket
    while len(fruit_freq) > 2:
      left_fruit = fruits[window_start]
      fruit_freq[left_fruit] -= 1
      if fruit_freq[left_fruit] == 0:
        del fruit_freq[left_fruit]
      window_start += 1  # shrink the window
      
    max_length = max(max_length, window_end-window_start+1)

  return max_length



def main():
  print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
  print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))


main()