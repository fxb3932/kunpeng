# from glob import glob
# from keyword import iskeyword
# from os.path import dirname, join, split, splitext
#
# print('start __init__.py')

# basedir = dirname(__file__)
#
# for name in glob(join(basedir, '*.py')):
#     module = splitext(split(name)[-1])[0]
#     if not module.startswith('_') and \
#             module.isidentifier() and \
#             not iskeyword(module):
#         print(__name__ + '.' + module)
#         __import__(__name__ + '.' + module)


