import camelcase

c = camelcase.CamelCase()
txt = "hello world"

print(c.hump(txt))

'''
pip --version
pip install camelcase
在 https://pypi.org/，您可以找到更多的包
pip uninstall  pip install camelcase
pip list  --列出系统上安装的所有软件包

升级pip
python -m pip install --upgrade pi
'''
