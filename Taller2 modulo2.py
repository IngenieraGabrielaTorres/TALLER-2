# Taller 2
# Los datos y yo 
# Gariela Torres
# ID:1001970935
# ID:502193
# correo:gabriela.torresr@correo.upb.edu.co
# Cel:3234708201
# Diplomado de PYTHON APLICADO A LA INGENIERIA 
# Docente:Roberto Paez Salgado
# Modulo 2


import pandas as pd

# 1 Lea la base de datos netflix_titles usando la libreria "pandas"
my_data = pd.read_csv("netflix_titles.csv")
print(my_data)

#2 Imprima por consola las primeras y ultimas 5 filas del arreglo

print(my_data.head(5))
print(my_data.tail (5))

#3 Imprima cada uno de los tipos de datos asociados a las etiquetas
print(my_data.info())

#4 Guarde un archivo .xlxs, en el cual nombre el arhivo sea "Netflix_lis" y el nombre de la hoja de titulos 
my_data.to_excel("Netflix_list.xlsx", sheet_name="titulos", index=False)

#5 Cree una nueva data frame en el cual segmente : unicamente el tipo, la duracion la descripcion y el pais
nueva_my_data = my_data[["type", "duration", "description", "country"]]



#6 Haga un filtro para las peliculas que tienen duracion superior a 100min
movies = my_data[my_data["type"] == "Movie"]
DivDurationMovies = movies["duration"].str.split(expand=True).dropna()
movies.insert(4,"durationIntMovies", DivDurationMovies[0].astype(int))
filtered_by_more_than_100 = movies[movies["durationIntMovies"] > 100]
print(filtered_by_more_than_100)

#7 Haga un filtro para los "Tv shows" que tienen mas de 3 temporadas 
series = my_data[my_data["type"] == "TV Show"]
DivDurationseries = series["duration"].str.split(expand=True).dropna()
series.insert(5, "durationIntSeries", DivDurationseries[0].astype(int))
FiltBy3 = series[series["durationIntSeries"] > 3]
print(FiltBy3)

#8 Haga un filtro en el cual solo tenga en cuenta 2 categorias/etiquetas(libre eleccion)
nueva_filtro = (my_data[["type", "title"]])

#9 Recuerde usar casos con indexacion numerica y con texto (loc/ iloc)
my_data.loc[:1, "director"] = 'non'
my_data.iloc[:2, 4] = 'none'

#10 Modifique los valores del ID de las 5 primeras y 5 ultimas "shows"
my_data["show_id"] = my_data["show_id"].replace({"s1":"1","s2":"2","s3":"3","s4":"4","s5":"5"})
my_data["show_id"] = my_data["show_id"].replace({"s8803":"8803","s8804":"8804","s8805":"8805","s8806":"8806","s8807":"8807"})
print (my_data)

# 

