import math

def triplet_sum_close_to_target(arr, target_sum):
  arr.sort()
  smallest_difference = math.inf

  for i in range(len(arr)-2):

    left = i +1
    right = len(arr) -1
    while left < right: 

      current_difference = target_sum - arr[i] - arr[left] - arr[right]

      if current_difference == 0:
        return target_sum - current_difference
    
      if abs(current_difference) < abs(smallest_difference) or (abs(current_difference) == abs(smallest_difference) and current_difference > smallest_difference):
        smallest_difference = current_difference
    
      if current_difference > 0:
        left += 1
      else: 
        right -= 1

  return target_sum - smallest_difference


def main():
  print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
  print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
  print(triplet_sum_close_to_target([1, 0, 1, 1], 100))


main()