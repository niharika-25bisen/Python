def capitalizeFirst(arr):
    result = []
    if len(arr) == 0:
        return result

    result.append(arr[0][0].upper() + arr[0][1:])
    result += capitalizeFirst(arr[1:])
    return result

print(capitalizeFirst(['car', 'taco', 'banana']))  # ['Car', 'Taco', 'Banana']