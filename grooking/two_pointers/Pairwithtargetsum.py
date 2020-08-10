def pair_with_targetsum(arr, target_sum):
  front_pointer, back_pointer, sum = 0, len(arr) - 1, 0
  res = []
  while front_pointer < len(arr) or back_pointer > 0:
    sum = arr[front_pointer] + arr[back_pointer]
    if sum == target_sum:
      res.append(front_pointer)
      res.append(back_pointer)
      return res
    elif sum > target_sum:
      back_pointer -= 1
    else:
      front_pointer += 1
  return [-1, -1]
