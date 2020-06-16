from faker import Faker

faker = Faker()

color_name = faker.color_name()
hex_color = faker.hex_color()
rgb_color = faker.rgb_color()
rgb_css_color = faker.rgb_css_color()
safe_color_name = faker.safe_color_name()
safe_hex_color = faker.safe_hex_color()

print("color_name :", color_name)
print("hex_color :", hex_color)
print("rgb_color :", rgb_color)
print("rgb_css_color :", rgb_css_color)
print("safe_color_name :", safe_color_name)
print("safe_hex_color :", safe_hex_color)
