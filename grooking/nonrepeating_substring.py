def non_repeat_substring(str):
  window_start =0
  letter_frequency = {}
  max_substring =0

  for window_end in range(len(str)):
    right_letter = str[window_end]
    if right_letter not in letter_frequency:
      letter_frequency[right_letter] =0
    letter_frequency[right_letter] += 1

    while letter_frequency[right_letter] > 1:
      left_letter = str[window_start]
      letter_frequency[left_letter] -= 1
      window_start += 1
    
    max_substring = max(max_substring, window_end - window_start +1)

  return max_substring

  
def main():
  print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
  print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
  print("Length of the longest substring: " + str(non_repeat_substring("abccde")))


main()