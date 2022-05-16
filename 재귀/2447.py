def star(n):
    if n == 1:
        return ['*']
    stars = star(n//3)
    result = []

    for i in stars:
        result.append(i*3)
    for i in stars:
        result.append(i+(n//3)*' '+i)
    for i in stars:
        result.append(i*3)

    return result

n = int(input())
print('\n'.join(star(n)))

