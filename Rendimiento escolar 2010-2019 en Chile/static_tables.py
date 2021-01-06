import pandas as pd

# Inicializamos la lista de dependencia establecimientos
data_depe = [[1, 'Corporación Municipal'], 
                 [2, 'Municipal DAEM'], 
                 [3, 'Particular Subvencionado'],
                 [4, 'Particular Pagado (o no subvencionado)'],
                 [5, 'Corporación de Administración Delegada (DL 3166)'],
                 [6, 'Servicio Local de Educación']]

# Inicializamos la lista de regiones
data_region = [[1, 'Región de Tarapacá', 'TPCA'], 
                [2, 'Región de Antofagasta', 'ANTOF'],
                [3, 'Región de Atacama', 'ATCMA'],
                [4, 'Región de Coquimbo', 'COQ'],
                [5, 'Región de Valparaíso', 'VALPO'],
                [6, 'Región del Libertador Gral. Bernardo O’Higgins', 'LGBO'],
                [7, 'Región del Maule', 'MAULE'],
                [8, 'Región del Biobío','BBIO'],
                [9, 'Región de la Araucanía', 'ARAUC'],
                [10, 'Región de Los Lagos', 'LAGOS'],
                [11, 'Región de Aysén del Gral. Carlos Ibáñez del Campo', 'AYSEN'],
                [12, 'Región de Magallanes y de la Antártica Chilena', 'MAG'],
                [13, 'Región Metropolitana de Santiago', 'RM'],
                [14, 'Región de Los Ríos', 'RIOS'],
                [15, 'Región de Arica y Parinacota', 'AYP'],
                [16, 'Región de Ñuble', 'NUBLE']]

# Inicializamos la lista de provincias
data_provincia = [
[1, 11, 'Provincia de Iquique'],
[1, 14, 'Provincia del Tamarugal'],
[2, 21, 'Provincia de Antofagasta'],
[2, 22, 'Provincia de El Loa'],
[2, 23, 'Provincia de Tocopilla'],
[3, 31, 'Provincia de Copiapó'],
[3, 32, 'Provincia de Chañaral'],
[3, 33, 'Provincia de Huasco'],
[4, 41, 'Provincia de Elqui'],
[4, 42, 'Provincia de Choapa'],
[4, 43, 'Provincia de Limarí'],
[5, 51, 'Provincia de Valparaíso'],
[5, 52, 'Provincia de Isla de Pascua'],
[5, 53, 'Provincia de Los Andes'],
[5, 54, 'Provincia de Petorca'],
[5, 55, 'Provincia de Quillota'],
[5, 56, 'Provincia de San Antonio'],
[5, 57, 'Provincia de San Felipe de Aconcagua'],
[5, 58, 'Provincia de Marga Marga'],
[6, 61, 'Provincia de Cachapoal'],
[6, 62, 'Provincia de Cardenal Caro'],
[6, 63, 'Provincia de Colchagua'],
[7, 71, 'Provincia de Talca'],
[7, 72, 'Provincia de Cauquenes'],
[7, 73, 'Provincia de Curicó'],
[7, 74, 'Provincia de Linares'],
[8, 81, 'Provincia de Concepción'],
[8, 82, 'Provincia de Arauco'],
[8, 83, 'Provincia de Biobío'],
[8, 84, 'Provincia de Ñuble'],
[9, 91, 'Provincia de Cautín'],
[9, 92, 'Provincia de Malleco'],
[10, 101, 'Provincia de Llanquihue'],
[10, 102, 'Provincia de Chiloé'],
[10, 103, 'Provincia de Osorno'],
[10, 104, 'Provincia de Palena'],
[11, 111, 'Provincia de Coyhaique'],
[11, 112, 'Provincia de Aysén'],
[11, 113, 'Provincia de Capitán Prat'],
[11, 114, 'Provincia de General Carrera Aconcagua'],
[12, 121, 'Provincia de Magallanes'],
[12, 122, 'Provincia de Antártica Chilena'],
[12, 123, 'Provincia de Tierra del Fuego'],
[12, 124, 'Provincia de Última Esperanza'],
[13, 131, 'Provincia de Santiago'],
[13, 132, 'Provincia de Cordillera'],
[13, 133, 'Provincia de Chacabuco'],
[13, 134, 'Provincia de Maipo'],
[13, 135, 'Provincia de Melipilla'],
[13, 136, 'Provincia de Talagante'],  
[14, 141, 'Provincia de Valdivia'],
[14, 142, 'Provincia de Ranco'],        
[15, 151, 'Provincia de Arica'],
[15, 152, 'Provincia de Parinacota'],        
[16, 161, 'Provincia de Diguillin'],
[16, 162, 'Provincia de Itata'],
[16, 163, 'Provincia de Punilla']]

# Inicializamos la lista de indice de ruralidad
data_rural_rbd = [[0, 'Urbano'], 
                  [1, 'Rural']] 

# Inicializamos la lista de tipo de enseñanza
data_ense = [
[110, 'Enseñanza Básica'],
[160, 'Educación Básica Común Adultos (Decreto 584/2007)'],
[161, 'Educación Básica Especial Adultos'],
[163, 'Escuelas Cárceles (Básica Adultos)'],
[165, 'Educación Básica Adultos Sin Oficios (Decreto 584/2007)'],
[167, 'Educación Básica Adultos Con Oficios (Decreto 584/2007 y 999/2009)'],
[310, 'Enseñanza Media H-C niños y jóvenes'],
[360, 'Educación Media H-C adultos vespertino y nocturno (Decreto N°190/1975)'],
[361, 'Educación Media H-C adultos (Decreto N° 12/1987)'],
[362, 'Escuelas Cárceles (Media Adultos)'],
[363, 'Educación Media H-C Adultos (Decreto N°1000/2009)'],
[410, 'Enseñanza Media T-P Comercial Niños y Jóvenes'],
[460, 'Educación Media T-P Comercial Adultos (Decreto N° 152/1989)'],
[461, 'Educación Media T-P Comercial Adultos (Decreto N° 152/1989)'],
[463, 'Educación Media T-P Comercial Adultos (Decreto N° 1000/2009)'],
[510, 'Enseñanza Media T-P Industrial Niños y Jóvenes'],
[560, 'Educación Media T-P Industrial Adultos (Decreto N° 152/1989)'],
[561, 'Educación Media T-P Industrial Adultos (Decreto N° 152/1989)'],
[563, 'Educación Media T-P Industrial Adultos (Decreto N° 1000/2009)'],
[610, 'Enseñanza Media T-P Técnica Niños y Jóvenes'],
[660, 'Educación Media T-P Técnica Adultos (Decreto N° 152/1989)'],
[661, 'Educación Media T-P Técnica Adultos (Decreto N° 152/1989)'],
[663, 'Educación Media T-P Técnica Adultos (Decreto N° 1000/2009)'],
[710, 'Enseñanza Media T-P Agrícola Niños y Jóvenes'],
[760, 'Educación Media T-P Agrícola Adultos (Decreto N° 152/1989)'],
[761, 'Educación Media T-P Agrícola Adultos (Decreto N° 152/1989)'],
[763, 'Educación Media T-P Agrícola Adultos (Decreto N° 1000/2009)'],
[810, 'Enseñanza Media T-P Marítima Niños y Jóvenes'],
[860, 'Enseñanza Media T-P Marítima Adultos (Decreto N° 152/1989)'],
[863, 'Enseñanza Media T-P Marítima Adultos (Decreto N° 1000/2009)'],
[910, 'Enseñanza Media Artística Niños y Jóvenes'],
[963, 'Enseñanza Media Artística Adultos']]

# Inicializamos la lista de grado por tipo de enseñanza
data_grado = [
# Primera hoja
[110, 1, '1o Básico'],
[110, 2, '2o Básico'],
[110, 3, '3o Básico'],
[110, 4, '4o Básico'],
[110, 5, '5o Básico'],
[110, 6, '6o Básico'],
[110, 7, '7o Básico'],
[110, 8, '8o Básico'],
[160, 1, 'Alfabetización'],
[160, 2, 'Nivel Básico 1 (1o a 4o básico)'],
[160, 3, 'Nivel Básico 2 (5o a 6o básico)'],
[160, 4, 'Nivel Básico 3 (7o a 8o básico)'],
[160, 5, 'Nivel Técnico'],
[161, 1, 'Alfabetización'],
[161, 2, 'Nivel Básico 1 (1o a 4o básico)'],
[161, 3, 'Nivel Básico 2 (5o a 6o básico)'],
[161, 4, 'Nivel Básico 3 (7o a 8o básico)'],
[161, 5, 'Nivel Técnico'],
[163, 1, 'Alfabetización'],
[163, 2, 'Nivel Básico 1 (1o a 4o básico)'],
[163, 3, 'Nivel Básico 2 (5o a 6o básico)'],
[163, 4, 'Nivel Básico 3 (7o a 8o básico)'],
[163, 5, 'Nivel Técnico'],
[165, 1, 'Nivel Básico 1 (1o a 4o básico)'],
[165, 2, 'Nivel Básico 2 (5o a 6o básico)'],
[165, 3, 'Nivel Básico 3 (7o a 8o básico)'],
[167, 2, 'Nivel Básico 2 (5o a 6o básico)'],
[167, 3, 'Nivel Básico 3 (7o a 8o básico)'],
[310, 1, '1o medio'],
[310, 2, '2o medio'],
[310, 3, '3o medio'],
[310, 4, '4o medio'],
[360, 1, '1o medio'],
[360, 2, '2o medio'],
[360, 3, '3o medio'],
[360, 4, '4o medio'],
[361, 1, 'Primer ciclo (1o y 2o medio)'],
[361, 3, 'Segundo ciclo (3o y 4o medio)'],
[363, 1, 'Primer nivel (1o y 2o medio)'],
[363, 3, 'Segundo nivel (3o y 4o medio)'],
[410, 1, '1o medio'],
[410, 2, '2o medio'],
# Segunda hoja
[410, 3, '3o medio'],
[410, 4, '4o medio'],
[460, 1, 'Primer ciclo (1o y 2o medio)'],
[460, 3, '3o medio'],
[460, 4, '4o medio'],
[461, 1, 'Primer ciclo (1o y 2o medio)'],
[461, 3, '3o medio'],
[461, 4, '4o medio'],
[463, 1, 'Primer nivel (1o y 2o medio)'],
[463, 3, 'Segundo nivel (3o medio)'],
[463, 4, 'Tercero nivel (4o medio)'],
[510, 1, '1o medio'],
[510, 2, '2o medio'],
[510, 3, '3o medio'],
[510, 4, '4o medio'],
[560, 1, 'Primer ciclo (1o y 2o medio)'],
[560, 3, '3o medio'],
[560, 4, '4o medio'],
[561, 1, 'Primer ciclo (1o y 2o medio)'],
[561, 3, '3o medio'],
[561, 4, '4o medio'],
[563, 1, 'Primer nivel (1o y 2o medio)'],
[563, 3, 'Segundo nivel (3o medio)'],
[563, 4, 'Tercero nivel (4o medio)'],
[610, 1, '1o medio'],
[610, 2, '2o medio'],
[610, 3, '3o medio'],
[610, 4, '4o medio'],
[660, 1, 'Primer ciclo (1o y 2o medio)'],
[660, 3, '3o medio'],
[660, 4, '4o medio'],
[661, 1, 'Primer ciclo (1o y 2o medio)'],
[661, 3, '3o medio'],
[661, 4, '4o medio'],
[663, 1, 'Primer nivel (1o y 2o medio)'],
[663, 3, 'Segundo nivel (3o medio)'],
[663, 4, 'Tercero nivel (4o medio)'],
[710, 1, '1o medio'],
[710, 2, '2o medio'],
[710, 3, '3o medio'],
[710, 4, '4o medio'],
[760, 1, 'Primer ciclo (1o y 2o medio)'],
[760, 3, '3o medio'],
[760, 4, '4o medio'],
# Tercera hoja
[761, 1, 'Primer ciclo (1o y 2o medio)'],
[761, 3, '3o medio'],
[761, 4, '4o medio'],
[763, 1, 'Primer nivel (1o y 2o medio)'],
[763, 3, 'Segundo nivel (3o medio)'],
[763, 4, 'Tercero nivel (4o medio)'],
[810, 1, '1o medio'],
[810, 2, '2o medio'],
[810, 3, '3o medio'],
[810, 4, '4o medio'],
[860, 1, 'Primer ciclo (1o y 2o medio)'],
[860, 3, '3o medio'],
[860, 4, '4o medio'],
[861, 1, 'Primer ciclo (1o y 2o medio)'],
[861, 3, '3o medio'],
[861, 4, '4o medio'],
[863, 1, 'Primer nivel (1o y 2o medio)'],
[863, 3, 'Segundo nivel (3o medio)'],
[863, 4, 'Tercero nivel (4o medio)'],
[910, 1, '1o medio'],
[910, 2, '2o medio'],
[910, 3, '3o medio'],
[910, 4, '4o medio'],
[963, 3, 'Segundo nivel (3o medio)'],
[963, 4, 'Tercero nivel (4o medio)']]

# Inicializamos la lista de géneros
data_genero = [[0, 'Sin Información'], 
               [1, 'Masculino'],
               [2, 'Femenino']] 

# Aqui va COD_COM_ALU

# Inicializamos la lista de situacion final
data_sit_fin = [['P', 'Promovido'], 
                ['R', 'Reprobado'],
                ['Y', 'Retirado'],
                ['-', 'Sin información']] 

# Inicializamos la lista de situacion final con traslado
data_sit_fin_t = [['P', 'Promovido'], 
                ['R', 'Reprobado'],
                ['Y', 'Retirado'],
                ['T', 'Trasladado'],
                ['en blanco', 'Sin información']] 

data_jornada = [[1, 'Mañana'],
                [2, 'Tarde'],
                [3, 'Mañana y tarde'],
                [4, 'Vespertina / Nocturna']]

"""
# Creamos los dataframes
df_depe = pd.DataFrame(data_depe, columns = ['COD_DEPE', 'DEPENDENCIA_ESTABLECIMIENTO'])
df_region = pd.DataFrame(data_region, columns = ['COD_REG_RBD', 'REGION', 'REGION_ABREVIADO'])
df_provincia = pd.DataFrame(data_provincia, columns = ['COD_REG_RBD', 'COD_PRO_RBD', 'PROVINCIA'])
df_rural_rbd = pd.DataFrame(data_rural_rbd, columns = ['RURAL_RBD', 'INDICE_RURALIDAD'])
df_data_ense = pd.DataFrame(data_ense, columns = ['COD_ENSE', 'DESCRIPCION'])
df_grado = pd.DataFrame(data_grado, columns = ['COD_ENSE', 'COD_GRADO', 'NOMBRE_GRADO'])
df_genero = pd.DataFrame(data_genero, columns = ['GEN_ALU', 'GENERO'])
# Aqui va COD_COM_ALU
df_sit_fin = pd.DataFrame(data_sit_fin, columns = ['SIT_FIN', 'SITUACION_CIERRE'])
df_sit_fin_t = pd.DataFrame(data_sit_fin_t, columns = ['SIT_FIN_R', 'SITUACION_CIERRE_TRASLADADO'])
df_jornada = pd.DataFrame(data_jornada, columns=['COD_JOR', 'JORNADA'])
"""


# La tabla de comuna hay que autogenerarla 
# Con los datos que tenemos en el dataset

#print(df_jornada)