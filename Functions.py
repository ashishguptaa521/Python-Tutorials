def greet_user(first_name, last_name):#first_name and last_name are positional arguments.
    print(f"""Hi {first_name}  {last_name}!
Welcome aboard!""")


greet_user(last_name='Smith',first_name='John') #Here we've passed John as first name, so position doesn't matter, hence it's Keyword argument.
