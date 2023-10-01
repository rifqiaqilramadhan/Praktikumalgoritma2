import math

def calculate_distance(lat1, lon1, lat2, lon2):
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)
    
    radius_bumi = 6371.0

    delta_lat = lat2 - lat1
    delta_lon = lon2 - lon1

    a = math.sin(delta_lat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(delta_lon / 2)**2
    b = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    distance = radius_bumi * b
    return distance

lat1 = float(input("Masukkan lattitude kota asal : "))
lon1 = float(input("Masukkan longitude kota tujuan : "))
lat2 = float(input("Masukkan lattitude kota asal : "))
lon2 = float(input("Masukkan longitude kota tujuan : "))

jarak = calculate_distance(lat1, lon1, lat2, lon2)

print(f"Jarak antara kota asal dan kota tujuan adalah {jarak:.2f} KM")
