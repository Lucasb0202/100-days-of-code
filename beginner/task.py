def is_prime(num):
  count = 0
  for i in range(1, num + 1):
    if num % i == 0:
      count += 1
  return count == 2

print(is_prime(2))