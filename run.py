from funcs import conf
import sys

parametros = conf.param()

for param in sys.argv :

    try:
        var = str(param)
        p0 = var.split('=')[0]
        p1 = var.split('=')[1]
        parametros[p0] = p1

    except:
        continue

conexao = conf.cnx()