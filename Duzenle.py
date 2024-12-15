import os
import shutil

def organize_files():
    source_dir = os.getcwd()  # Programın çalıştığı dizin

    if not os.path.exists("CKS"):
        os.makedirs("CKS")

    if not os.path.exists("NCZ"):
        os.makedirs("NCZ")
        
    if not os.path.exists("NCY"):
        os.makedirs("NCY")
        
    if not os.path.exists("TXT"):
        os.makedirs("TXT")
    
    if not os.path.exists("DWG"):
        os.makedirs("DWG")
        
    if not os.path.exists("NCN"):
        os.makedirs("NCN")

    if not os.path.exists("NCP"):
        os.makedirs("NCP")

    if not os.path.exists("DXF"):
        os.makedirs("DXF")

    if not os.path.exists("PDF"):
        os.makedirs("PDF")

    if not os.path.exists("PNG"):
        os.makedirs("PNG")

    if not os.path.exists("WORLD"):
        os.makedirs("WORLD")

     
        
    for filename in os.listdir(source_dir):
        print(filename)
        source_path = os.path.join(source_dir, filename)

        # Convert both filename and extension to lowercase for case-insensitive comparison
        lower_filename = filename.lower()

        if lower_filename.endswith(".cks"):
            target_subdir = os.path.join(source_dir, "CKS")
        elif lower_filename.endswith(".txt"):
            target_subdir = os.path.join(source_dir, "TXT")
        elif lower_filename.endswith(".ncy"):
            target_subdir = os.path.join(source_dir, "NCY")
        elif lower_filename.endswith(".ncz"):
            target_subdir = os.path.join(source_dir, "NCZ")
        elif lower_filename.endswith(".dwg"):
            target_subdir = os.path.join(source_dir, "DWG")
        elif lower_filename.endswith(".ncn") and lower_filename != "nokta.ncn":
            target_subdir = os.path.join(source_dir, "NCN")
        elif lower_filename.endswith(".ncp"):
            target_subdir = os.path.join(source_dir, "NCP")
        elif lower_filename.endswith(".dxf"):
            target_subdir = os.path.join(source_dir, "DXF")
        elif lower_filename.endswith(".pdf"):
            target_subdir = os.path.join(source_dir, "PDF")
        elif lower_filename.endswith(".png"):
            target_subdir = os.path.join(source_dir, "PNG")
        elif lower_filename.endswith(".xls") or lower_filename.endswith(".xlsx") or lower_filename.endswith(".doc") or lower_filename.endswith(".docx"):
            target_subdir = os.path.join(source_dir, "WORLD")        
        else:
            continue

        if not os.path.exists(target_subdir):
            os.makedirs(target_subdir)

        target_path = os.path.join(target_subdir, filename)

        shutil.move(source_path, target_path)
        print(f"{filename} dosyası {target_subdir} klasörüne kopyalandı.")

# Kullanım örneği
organize_files()
