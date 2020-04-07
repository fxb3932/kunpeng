txt = 'test\n\n\n'\
    'test\n\n' \
    'test\n'
# txt = txt.replace("\n\n", '\n')
txt2 = []
for line in txt.split('\n') :
    if line != '':
        txt2.append(line)

print('\n'.join(txt2))