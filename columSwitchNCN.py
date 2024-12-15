import os

def switch_columns(data, col1, col2):
    """İki sütunun yerlerini değiştirir"""
    for row in data:
        row[col1], row[col2] = row[col2], row[col1]
    return data

def read_data(filepath):
    """Dosyadan verileri okur"""
    data = []
    with open(filepath, 'r') as file:
        for line in file:
            parts = line.split()
            row = [parts[0]] + list(map(float, parts[1:4])) + parts[4:]
            data.append(row)
    return data

def write_data(filepath, data):
    """Verileri dosyaya yazar"""
    with open(filepath, 'w') as file:
        for row in data:
            file.write(" ".join(map(str, row)) + '\n')

def print_data(data):
    """Verileri ekrana yazdırır"""
    for row in data:
        print(" ".join(map(str, row)))

def main():
    # Masaüstü yolu
    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    input_filepath = os.path.join(desktop, 'nokta.ncn')
    output_filepath = os.path.join(desktop, 'noktaswitchedkolon.ncn')
    
    # Dosyayı okuma
    data = read_data(input_filepath)
    
    print("\nOriginal Data:")
    print_data(data)
    
    col1 = int(input("\nEnter the first column index to switch (1-based): ")) - 1
    col2 = int(input("Enter the second column index to switch (1-based): ")) - 1
    
    data = switch_columns(data, col1, col2)
    
    print("\nData After Switching Columns:")
    print_data(data)
    
    # Dosyayı yazma
    write_data(output_filepath, data)
    print(f"\nData has been written to {output_filepath}")

if __name__ == "__main__":
    main()
