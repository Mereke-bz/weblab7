#string_times
def string_times(str, n):
  return str * n


#front_times
def front_times(str, n):
  front_len = 3
  if(len(str) < front_len):
    front_len = len(str)
  front = str[:front_len]
  
  result = ""
  for i in range(n):
    result = result + front
  return result

#string_bits
def string_bits(str):
  result = ""
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result

#string_splosion
def string_splosion(str):
  result = ""
  for i in range(len(str)):
    result = result+ str[:i + 1]
  return result


#last2
def array_count9(nums):
  count = 0
  for i in range(len(nums)):
    if nums[i] == 9:
      count += 1
  
  return count


#array123
def array123(nums):
  for i in range(len(nums) - 2):
    if nums[i] == 1 and nums[i + 1] == 2 and nums[i + 2] == 3:
      return True
  return False


#string match
def string_match(a, b):
  shorter = min(len(a), len(b))
  count = 0
  
  for i in range(shorter - 1):
    a_sub = a[i : i + 2]
    b_sub = b[i: i + 2]
    if a_sub == b_sub:
      count = count + 1
      
  return count