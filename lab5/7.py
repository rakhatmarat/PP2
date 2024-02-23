def snake_to_camel(snake_case):
    words = snake_case.split('_')
    return ''.join(word.title() for word in words)

snake_case_string = "this_is_snake_case"
camel_case_string = snake_to_camel(snake_case_string)
print("Task 7 Result:", camel_case_string)
