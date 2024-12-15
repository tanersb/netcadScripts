import math


x1=4
y1=15
x2=10
y2=7
x3=4
y3=15
x4=10
y4=7
length = 8

length = 0.63
x1=4510773.1244
y1=513798.8189
x2=4510773.7524
y2=513798.7847
x3=4510773.7886
y3=513799.4077
x4=4510773.1878
y4=513799.4560


x1=4510773.124106082
y1=513798.8186437038
x2=4510773.770751577
y2=513799.09592062054
x3=4510773.788870792
y3=513799.40794430824
x4=4510773.187571548
y4=513799.4562913674




# Girilen 4 nokta koordinatları
point1 = (x1, y1) #point1[0] x point1[1] y
point2 = (x2, y2) #point2[0] x point2[1] y
point3 = (x3, y3) #point3[0] x point3[1] y
point4 = (x4, y4) #point4[0] x point4[1] y

# İlk iki nokta arası uzaklık
distance1 = math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
# İkinci ve üçüncü nokta arası uzaklık
distance2 = math.sqrt((point2[0] - point3[0]) ** 2 + (point2[1] - point3[1]) ** 2)
# üçüncü ve dördüncü nokta arası uzaklık
distance3 = math.sqrt((point3[0] - point4[0]) ** 2 + (point3[1] - point4[1]) ** 2)
# dördüncü ve birinci nokta arası uzaklık
distance4 = math.sqrt((point4[0] - point1[0]) ** 2 + (point4[1] - point1[1]) ** 2)

# Kenar boyu, karenin dik kenarları olduğu için iki uzaklık da aynı olmalı
print('Aralarındaki Mesafeler')
print(distance1, distance2, distance3, distance4)
print('Olması gereken:',length)



first_side_length = distance1 - length
second_side_length = distance2 - length
third_side_length = distance3 - length
fourt_side_length = distance4 - length


#print('EskiY ve X')
#b = (point2[1] * (distance1 - 1) + point2[1]) / distance1
#a = (point2[0] * (distance1 - 1) + point2[0]) / distance1
#print(a)
#print(b)

print('---------------------------')
print('ilk ve İkinci Koordinat için')
print('YeniKoordinatlar')
new_y21 = point2[1] + ((first_side_length * (point1[1] - point2[1])) / (2 * distance1))
new_x21 = point2[0] + ((first_side_length * (point1[0] - point2[0])) / (2 * distance1))

print('X2',new_x21)
print('Y2',new_y21)

new_y11 = point1[1] - ((first_side_length * (point1[1] - point2[1])) / (2 * distance1))
new_x11 = point1[0] - ((first_side_length * (point1[0] - point2[0])) / (2 * distance1))

print('X1',new_x11)
print('Y1',new_y11)


print('------------------------------')
print('İki ve Üç Koordinat için')
print('YeniKoordinatlar')
new_y31 = point3[1] + ((first_side_length * (point2[1] - point3[1])) / (2 * distance1))
new_x31 = point3[0] + ((first_side_length * (point2[0] - point3[0])) / (2 * distance1))

print('X3',new_x31)
print('Y3',new_y31)

new_y22 = point3[1] - ((first_side_length * (point2[1] - point3[1])) / (2 * distance1))
new_x22 = point3[0] - ((first_side_length * (point2[0] - point3[0])) / (2 * distance1))

print('X2',new_x22)
print('Y2',new_y22)

print('------------------------------')
print('Üç ve Dört Koordinat için')
print('YeniKoordinatlar')
new_y41 = point4[1] + ((first_side_length * (point3[1] - point4[1])) / (2 * distance1))
new_x41 = point4[0] + ((first_side_length * (point3[0] - point4[0])) / (2 * distance1))

print('X4',new_x41)
print('Y4',new_y41)

new_y32 = point3[1] - ((first_side_length * (point3[1] - point4[1])) / (2 * distance1))
new_x32 = point3[0] - ((first_side_length * (point3[0] - point4[0])) / (2 * distance1))

print('X3',new_x32)
print('Y3',new_y32)
print('------------------------------')
print('Dört ve Bir Koordinat için')
print('YeniKoordinatlar')
new_y12 = point1[1] + ((first_side_length * (point4[1] - point1[1])) / (2 * distance1))
new_x12 = point1[0] + ((first_side_length * (point4[0] - point1[0])) / (2 * distance1))

print('X1',new_x12)
print('Y1',new_y12)

new_y42 = point4[1] - ((first_side_length * (point4[1] - point1[1])) / (2 * distance1))
new_x42 = point4[0] - ((first_side_length * (point4[0] - point1[0])) / (2 * distance1))

print('X4',new_x42)
print('Y4',new_y42)
print('------------------------------')


print('Olması Gerekenden Farkları')
print(first_side_length, second_side_length, third_side_length, fourt_side_length)


print('X1ler',new_x11, new_x12)
print('X2ler',new_x21, new_x22)
print('X3ler',new_x31, new_x32)
print('X4ler',new_x41, new_x42)
print()
print('Y1ler',new_y11, new_y12)
print('Y2ler',new_y21, new_y22)
print('Y3ler',new_y31, new_y32)
print('Y4ler',new_y41, new_y42)



correction_factor = length

# Düzeltilmiş noktalar
point1 = ((new_x11+new_x12)/2, (new_y11+new_y12)/2)
point2 = ((new_x21+new_x22)/2, (new_y21+new_y22)/2)
point3 = ((new_x31+new_x32)/2, (new_y31+new_y32)/2)
point4 = ((new_x41+new_x42)/2, (new_y41+new_y42)/2)

# Dosya adı
file_name = "corrected_points.ncn"

# Dosyayı yazma modunda aç
with open(file_name, "w") as file:
    # Her noktayı dosyaya yaz
    for point in [point1, point2, point3, point4]:
        file.write("{} {}\n".format(point[1], point[0]))


