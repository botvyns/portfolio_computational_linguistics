import re

def execute_query(cursor, query, params=None):
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    return cursor.fetchall()

def parse_text(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    patterns = [
        r"(.+)(?:\tprofesor\t+?subst:sg:nom)",
        r"(.+)(?:\tprofesor\t.+?subst:sg:gen)",
        r"(.+)(?:\tprofesor\t+?subst:sg:dat)",
        r"(.+)(?:\tprofesor\t+?subst:sg:acc)",
        r"(.+)(?:\tprofesor\t+?subst:sg:inst)",
        r"(.+)(?:\tprofesor\t+?subst:sg:loc)",
        r"(.+)(?:\tprofesor\t.+?subst:sg:voc)",
        r"(.+)(?:\tprofesor\t+?subst:pl:nom)",
        r"(.+)(?:\tprofesor\t.+?subst:pl:gen)",
        r"(.+)(?:\tprofesor\t+?subst:pl:dat)",
        r"(.+)(?:\tprofesor\t+?subst:pl:acc)",
        r"(.+)(?:\tprofesor\t+?subst:pl:inst)",
        r"(.+)(?:\tprofesor\t+?subst:pl:loc)",
        r"(.+)(?:\tprofesor\t.+?subst:pl:voc)"
    ]
    
    return [re.findall(pattern, content) for pattern in patterns]