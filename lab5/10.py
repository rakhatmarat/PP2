import re
def camel_to_snake(camel_case):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', camel_case)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

camel_case_string = "helloWorld"
snake_case_string = camel_to_snake(camel_case_string)
print(snake_case_string)
