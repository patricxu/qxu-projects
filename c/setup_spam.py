from distutils.core import setup, Extension
modulel = Extension('spam', sources=['pyex_spam.c'])
setup(name = 'PackageName', version = '1.0', description = "This is a spam extension", ext_modules = [modulel])
