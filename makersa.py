import execjs
import execjs.runtime_names
from Naked.toolshed.shell import execute_js, muterun_js
f = open('rsa2.js', 'r',encoding = "utf-8" )
js = f.read()
f.close()
ctx = execjs.compile(js)

jscript = execjs.get()
jscript.compile(js)
jscript.compile("rsa = RSAKey();")
#a.call("rsa")
#ctx.("rsa")
