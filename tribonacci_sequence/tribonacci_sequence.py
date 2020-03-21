def tribonacci(signature, n):
    numbers = []
    for i in range(n):
        if i < 3:
            numbers.append(signature[i])
        else:
            numbers.append(sum(numbers[-3:]))
    return numbers
