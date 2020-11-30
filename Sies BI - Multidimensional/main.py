import pandas as pd
import sqlalchemy
import psycopg2
import numpy as np
import re
import time

start_time = time.time()

df = pd.read_excel("sies.xlsx")
df_len = df['CODIGO UNICO DE CARRERA'].count()

no_data =  '-'

def cleanDigit(input):
    input = str(input)
    if not input:
        return 0
    if '-' in input:
        return 0
    if 'nan' in input:
        return 0
    if 's/i' in input:
        return 0
    if input:
        return 0
    return int(float(input))

def cleanText(input):
    input = str(input)
    if ',' in input:
        input = input.replace(',','.')
    if 'nan' in input:
        return no_data
    if 's/i' in input:
        return no_data
    return input

def cleanPercentages(input):
    input = str(input)
    if not input:
        return 0.0
    if 'nan' in input:
        return 0.0
    if 'N/A' in input:
        return 0.0
    if 'NULL' in input:
        return 0.0
    return float(input)

def cleanDecimal(input):
    input = str(input)
    if not input:
        return 0.0
    if 'nan' in input:
        return 0.0
    if '-' in input:
        return 0.0
    if 's/i' in input:
        return 0.0
    if input == ' ':
        return 0.0
    return float(input)

def cleanPCobertura(input):
    input = str(input)
    if '-' in input:
        return 0.0, 0.0
    input = input.replace("% <= X <",",")
    input = input.replace("=","")
    input = input.rstrip('%')
    values = input.split(',')
    return int(values[0]), int(values[1])

def cleanDuracionRealSemestres(input):
    input = str(input)
    if 'nan' in input:
        return 0.0
    if '-' in input:
        return 0.0
    if 's/i' in input:
        return 0.0
    if not input:
        return 0.0
    return float(input)



# Eliminar las columnas que no se van a utilizar
df = df.drop(columns=['TIPO DE INSTITUCION', 'AÑO_DURAC', 'TOTAL MATRICULA','TOTAL MATRICULA 1ER AÑO','TOTAL TITULADOS'])

# Eliminar filas para hacer pruebas
#df = df[:-20920]
#a = df.iloc[:,5].tolist()

# Generar una instanciacion de las columnas a modificar
aa = df["ARANCEL ANUAL"].tolist()
ct = df["COSTO TITULACION"].tolist()
nc = df["NIVEL CARRERA O TIPO DE CARRERA"].tolist()
nca = df["NOMBRE CARRERA"].tolist()

am = df["AÑO MATRÍCULA"].tolist()
tmf = df["TOTAL MATRICULA FEMENINO"].tolist()
tmm = df["TOTAL MATRICULA MASCULINO"].tolist()
m1f = df["MATRICULA DE 1ER AÑO FEMENINO"].tolist()
m1m = df["MATRICULA 1ER AÑO MASCULINO"].tolist()

pmm = df["MATRÍCULA - % DE MUNICIPAL"].tolist()
pmps = df["MATRÍCULA - % DE PARTICULAR SUBVENCIONADO"].tolist()
pmpp = df["MATRÍCULA - % DE PARTICULAR PAGADO"].tolist()
cad = df["C. Administración Delegada"].tolist()

tf = df["TITULADOS FEMENINO"].tolist()
tm = df["TITULADOS MASCULINO"].tolist()

pcpsum1 = df["% DE COBERTURA PSU EN MATRICULA 1ER AÑO "].tolist()
pcpsum1min = []
pcpsum1max = []

ppsum1 = df["PROMEDIO PSU EN MATRICULA 1ER AÑO"].tolist()
pnemm = df["PROMEDIO NEM EN MATRICULA"].tolist()

v1s = df["VACANTES 1ER SEMESTRE"].tolist()

r1a = df["Retención de 1er año"].tolist()
drs = df["Duración real (semestres)"].tolist()
e1a = df["Empleabilidad al 1er año"].tolist()
ip4t = df["Ingreso promedio al 4° año de titulación"].tolist()

acg = df["Área Carrera Genérica"].tolist()

for i in range(len(aa)):
    aa[i] = cleanDigit(aa[i])
    ct[i] = cleanDigit(ct[i])
    nc[i] = cleanText(nc[i])
    nca[i] = cleanText(nca[i])
    
    am[i] = cleanDigit(am[i])
    tmf[i] = cleanDigit(tmf[i])
    tmm[i] = cleanDigit(tmm[i])
    m1f[i] = cleanDigit(m1f[i])
    m1m[i] = cleanDigit(m1m[i])
    
    pmm[i] = cleanPercentages(pmm[i])
    pmps[i] = cleanDecimal(pmps[i])
    pmpp[i] = cleanDecimal(pmpp[i])
    cad[i] = cleanDecimal(cad[i])
    
    tf[i] = cleanDigit(tf[i])
    tm[i] = cleanDigit(tm[i])
    
    mini, maxi = cleanPCobertura(pcpsum1[i])
    pcpsum1min.append(mini)
    pcpsum1max.append(maxi)
    
    ppsum1[i] = cleanDecimal(ppsum1[i])
    pnemm[i] = cleanDecimal(pnemm[i])
    
    v1s[i] = cleanDigit(v1s[i])
    
    r1a[i] = cleanDecimal(r1a[i])
    drs[i] = cleanDuracionRealSemestres(drs[i])
    e1a[i] = cleanDecimal(e1a[i])
    ip4t[i] = cleanText(ip4t[i])
    
    acg[i] = cleanText(acg[i])
    
    
# Asignar las columnas filtradas al dataframe

df["ARANCEL ANUAL"] = aa
df["COSTO TITULACION"] = ct
df["NIVEL CARRERA O TIPO DE CARRERA"] = nc
df["NOMBRE CARRERA"] = nca

df["AÑO MATRÍCULA"] = am
df["TOTAL MATRICULA FEMENINO"] = tmf
df["TOTAL MATRICULA MASCULINO"] = tmm
df["MATRICULA DE 1ER AÑO FEMENINO"] = m1f
df["MATRICULA 1ER AÑO MASCULINO"] = m1m

df["MATRÍCULA - % DE MUNICIPAL"] = pmm
df["MATRÍCULA - % DE PARTICULAR SUBVENCIONADO"] = pmps
df["MATRÍCULA - % DE PARTICULAR PAGADO"] = pmpp
df["C. Administración Delegada"] = cad

df["TITULADOS FEMENINO"] = tf
df["TITULADOS MASCULINO"] = tm

df["% DE COBERTURA PSU EN MATRICULA 1ER AÑO "] = pcpsum1
df["% COBERTURA MIN"] = pcpsum1min
df["% COBERTURA MAX"] = pcpsum1max

df["PROMEDIO PSU EN MATRICULA 1ER AÑO"] = ppsum1
df["PROMEDIO NEM EN MATRICULA"] = pnemm

df["VACANTES 1ER SEMESTRE"] = v1s

df["Retención de 1er año"] = r1a
df["Duración real (semestres)"] = drs
df["Empleabilidad al 1er año"] = e1a
df["Ingreso promedio al 4° año de titulación"] = ip4t

df["Área Carrera Genérica"] = acg

# Crear nuevos frames

df_titulados = df[['AÑO TITULADOS', 
                   'TITULADOS MASCULINO',
                   'TITULADOS FEMENINO',
                   'CODIGO UNICO DE CARRERA']].copy()

df_carrera = df[['CODIGO UNICO DE CARRERA', 
                 'NOMBRE CARRERA', 
                 'ARANCEL ANUAL', 
                 'COSTO TITULACION', 
                 'AREA DE CONOCIMIENTO', 
                 'DURACION CARRERA FORMAL',
                 'NIVEL CARRERA O TIPO DE CARRERA',
                 'Retención de 1er año',
                 #"Duración real (semestres)",
                 'Empleabilidad al 1er año',
                 'Ingreso promedio al 4° año de titulación',
                 'CODIGO DE INSTITUCIÓN']].copy()

df_carrera_sede = df[['CODIGO UNICO DE CARRERA',
                      'SEDE', # Este lo usare como codigo sede
                      'PSU PONDERACION NOTAS EM',
                      'PSU PONDERACION RANKING',
                      'PSU PONDERACION LENGUAJE',
                      'PSU PONDERACION MATEMATICAS',
                      'PSU PONDERACION HISTORIA',
                      'PSU PONDERACION CIENCIAS',
                      'PSU PONDERACION OTROS',
                      'VACANTES 1ER SEMESTRE',
                      'TOTAL MATRICULA FEMENINO',
                      'TOTAL MATRICULA MASCULINO',
                      'AÑO_INFORM']].copy()

df_sede = df[['SEDE', 
              'CODIGO DE INSTITUCIÓN',
              'JORNADA',
              'REGION']].copy()

df_institucion = df[['CODIGO DE INSTITUCIÓN',
                     'INSTITUCION']].copy()

df_matricula = df[['PROMEDIO NEM EN MATRICULA',
                   'CODIGO DE INSTITUCIÓN',
                   'PROMEDIO PSU EN MATRICULA 1ER AÑO',
                   'AÑO MATRÍCULA',
                   #'MATRÍCULA - % DE MUNICIPAL',
                   #'MATRÍCULA - % DE PARTICULAR SUBVENCIONADO',
                   #'MATRÍCULA - % DE PARTICULAR PAGADO',
                   'C. Administración Delegada',
                   #'% COBERTURA MIN',
                   #'% COBERTURA MAX'
                   ]].copy()

df_titulados.drop_duplicates(subset="CODIGO UNICO DE CARRERA", inplace=True)
df_titulados.reset_index(drop=True, inplace=True)

df_carrera.drop_duplicates(subset="CODIGO UNICO DE CARRERA", inplace=True)
df_carrera.reset_index(drop=True, inplace=True)

df_sede.drop_duplicates(subset="SEDE", inplace=True)
df_sede.reset_index(drop=True, inplace=True)

df_carrera_sede.drop_duplicates(['CODIGO UNICO DE CARRERA','SEDE'], keep='last')
df_carrera_sede.reset_index(drop=True, inplace=True)

df_institucion.drop_duplicates(subset="CODIGO DE INSTITUCIÓN", inplace=True)
df_institucion.reset_index(drop=True, inplace=True)

"""
df_matricula.drop_duplicates(['CODIGO DE INSTITUCIÓN',
                              'PROMEDIO NEM EN MATRICULA',
                              'AÑO MATRÍCULA',
                              'MATRÍCULA - % DE MUNICIPAL',
                              'MATRÍCULA - % DE PARTICULAR SUBVENCIONADO',
                              'MATRÍCULA - % DE PARTICULAR PAGADO',
                              'C. Administración Delegada'], keep='last')
"""
df_matricula.reset_index(drop=True, inplace=True)

# Medimos el tiempo que se demoró en ejecutar el código
print("El código se compiló en %s segundos" % (time.time() - start_time))


html_sede = df_sede.to_html("df_SEDE.html")
html_institucion = df_institucion.to_html("df_INSTITUCION.html")
html_titulados = df_titulados.to_html("df_TITULADOS.html")
html_matricula = df_matricula.to_html("df_MATRICULA.html")
html_carrera = df_carrera.to_html("df_CARRERA.html")

engine = sqlalchemy.create_engine('postgresql://postgres:postgres@localhost:5432/SIES_MULTI')
#df_sede.to_sql('sedes',engine)
#df_sede.set_index('SEDE', inplace=False)
#df_sede.to_sql('sedes',engine,if_exists='replace',index=False)

#df_institucion.to_sql('institucion',engine,if_exists='replace',index=False)
#df_titulados.to_sql('titulados',engine,if_exists='replace',index=False)
df_matricula.to_sql('matricula',engine,if_exists='replace',index=False)

#df_carrera.to_sql('carrera',engine,if_exists='replace',index=False)
