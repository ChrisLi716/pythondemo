from faker import Faker

faker = Faker("en_GB")
print('name:', faker.name())
print('address:', faker.address())
print('text:', faker.text())

faker = Faker('zh_CN')
print(faker.providers)
