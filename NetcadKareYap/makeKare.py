import math

def calculate_side_length(point1, point2, point3, point4,length):
    # İlk iki nokta arası uzaklık
    distance1 = math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
    # İkinci ve üçüncü nokta arası uzaklık
    distance2 = math.sqrt((point2[0] - point3[0])**2 + (point2[1] - point3[1])**2)
    # üçüncü ve dördüncü nokta arası uzaklık
    distance3 = math.sqrt((point3[0] - point4[0])**2 + (point3[1] - point4[1])**2)
    # dördüncü ve birinci nokta arası uzaklık
    distance4 = math.sqrt((point4[0] - point1[0])**2 + (point4[1] - point1[1])**2)

    # Kenar boyu, karenin dik kenarları olduğu için iki uzaklık da aynı olmalı
    print(distance1, distance2,distance3, distance4)


    first_side_length = distance1 - length
    if first_side_length < 0:
        first_side_length = first_side_length * -1
    first_side_length = first_side_length / 2

    b = (point2[1] * (distance1-1) + point2[1])/ distance1
    print('EskiY2')
    print(b)

    b = point2[1] - ((length*(point2[1]-1))/(2*distance1))
    print('YeniY2')
    print(b)

    a = (point2[0] * (distance1-1) + point2[0])/ distance1
    print(a)


    second_side_length = distance2 - length
    if second_side_length < 0:
        second_side_length = second_side_length * -1
    second_side_length = second_side_length / 2



    third_side_length = distance3 - length
    if third_side_length < 0:
        third_side_length = third_side_length * -1
    third_side_length = third_side_length / 2



    fourt_side_length = distance4 - length
    if fourt_side_length < 0:
        fourt_side_length = fourt_side_length * -1
    fourt_side_length = fourt_side_length / 2


    print(first_side_length , second_side_length, third_side_length, fourt_side_length)

    return first_side_length , second_side_length, third_side_length, fourt_side_length


length = 0.63
x1=4510773.1244
y1=513798.8189
x2=4510773.7524
y2=513798.7847
x3=4510773.7886
y3=513799.4077
x4=4510773.1878
y4=513799.4560


x1=4
y1=15
x2=10
y2=7
length = 12



# Girilen 4 nokta koordinatları
point1 = (x1, y1) #point1[0] x point1[1] y
point2 = (x2, y2) #point2[0] x point2[1] y
point3 = (x3, y3) #point3[0] x point3[1] y
point4 = (x4, y4) #point4[0] x point4[1] y


# Kenar boyunu düzeltmek için kullanılan faktör
#correction_factor = 63 / calculate_side_length(point1, point2, point3, point4,length)
calculate_side_length(point1, point2, point3, point4,length)
correction_factor = length

# Düzeltilmiş noktalar
point1 = (x1 * correction_factor, y1 * correction_factor)
point2 = (x2 * correction_factor, y2 * correction_factor)
point3 = (x3 * correction_factor, y3 * correction_factor)
point4 = (x4 * correction_factor, y4 * correction_factor)

# Dosya adı
file_name = "corrected_points.ncn"

# Dosyayı yazma modunda aç
with open(file_name, "w") as file:
    # Her noktayı dosyaya yaz
    for point in [point1, point2, point3, point4]:
        file.write("{} {}\n".format(point[1], point[0]))


