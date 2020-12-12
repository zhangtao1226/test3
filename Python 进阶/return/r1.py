def profile():
    name = 'tao'
    age = 20
    return (name, age)

print(profile())


def profile_2():
    name = 'tao'
    age = 30
    return name, age
name, age = profile_2()
print(name, age)