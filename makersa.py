import execjs
import execjs.runtime_names
import os
import codecs
from Naked.toolshed.shell import execute_js, muterun_js
f = codecs.open('rsa4.js','r','utf-8').read()
myjs = execjs.get()
compjs = myjs.compile(f)
#print(compjs.call("RSASetPublic"))
print(compjs.call("a","1"))
#a.call("rsa")
#ctx.("rsa")
