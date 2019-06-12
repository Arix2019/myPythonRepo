#   testa se o padrao de email esta correto
import re

def email(testMail):

    padrao = re.findall(r'\w+@\w+\.\w+', testMail)

    if padrao:
        return 0
    else:
        return 1


if email('teste@dominio.com') == 0:
    print('OK!')
else:
    print('E-mail incorreto!')








