import math as mt
my_city = (28.6553, -106.0889)

friend1 = (34.0522, -118.2437)  # Los Angeles
friend2 = (40.7128, -74.0060)   # New York
friend3 = (41.8781, -87.6298)   # Chicago   

#imprimir las ubicaciones 
print(f"My location: {my_city}")
print(f"Friend 1 Los Angeles: {friend1}")     
print(f"Friend 2 New York: {friend2}")
print(f"Friend 3 Chicago: {friend3}")

def calculate_distance(coord1, coord2): #formula de haversine
   lat1 , lon1 = mt.radians(coord1[0]), mt.radians(coord1[1])
   lat2, lon2 = mt.radians(coord2[0]), mt.radians(coord2[1])
   dlat = lat2 - lat1
   dlon = lon2 - lon1

   a = mt.sin(dlat / 2)**2 + mt.cos(lat1) * mt.cos(lat2) * mt.sin(dlon / 2)**2
   c = 2 * mt.asin(mt.sqrt(a))
   radio_tierra = 6371  # Radio de la Tierra en kilómetros
   distancia = radio_tierra * c
   return distancia

distancias = { #calcular distancias
   "Los Angeles": calculate_distance(my_city, friend1),
   "New York": calculate_distance(my_city, friend2),
    "Chicago": calculate_distance(my_city, friend3)
}
#encontrar la mas lejana
mas_lejano = max(distancias, key=distancias.get) #distancias.get obtiene el valor de cada ciudad
distancia_max = distancias[mas_lejano]

print("\n Distancias desde Chihuahua:")
for ciudad, distancia in distancias.items():#.item devuelve posicion 0 y 1
    print(f"{ciudad}: {distancia:.2f} km")

print(f"\n Mi amigo mas lejano esta en {mas_lejano}, a una distancia de {distancia_max:.2f} km.")

todas_ubicaciones = [my_city, friend1, friend2, friend3]
print("\n Todas las ubicaciones (latitud, longitud):")
print(todas_ubicaciones)