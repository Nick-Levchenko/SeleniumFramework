def give_format_url(url: str, login, password):
    auth_string = f'{login}:{password}@'
    strings = url.split('//')
    formatted_url = f'{strings[0]}//{auth_string}{strings[1]}'
    return formatted_url
