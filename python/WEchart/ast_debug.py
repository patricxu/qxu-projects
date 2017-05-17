import ast
import codegen
import pdb
#pdb.set_trace()

expr="""
pdb.set_trace()
a = 1
b = 2
def foo():
   print("hello world")

foo()
"""
p=ast.parse(expr)
print(ast.dump(p))

exec(compile(p, filename="<ast>", mode="exec"))

#p.body[0].body = [ ast.parse("return 42").body[0] ] # Replace function body with "return 42"

#exec(compile(expr, filename="<ast>", mode="exec"))

