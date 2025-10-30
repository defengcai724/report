import os
import re
import time
from tkinter import Tk, Button, Label, filedialog, LEFT
from docx import Document
from PyPDF2 import PdfReader
from PIL import Image
import piexif
from geopy.geocoders import Nominatim

# ---------------- 通用函數 ----------------
def sanitize_filename(name):
    return re.sub(r'[\\/*?:"<>|]', '_', name)

# ---------------- Word/PDF 改名 ----------------
def extract_word_first_line(file_path):
    try:
        doc = Document(file_path)
        for para in doc.paragraphs:
            text = para.text.strip()
            if text:
                return text
    except:
        return None

def extract_pdf_first_line(file_path):
    try:
        reader = PdfReader(file_path)
        if len(reader.pages) > 0:
            text = reader.pages[0].extract_text()
            if text:
                for line in text.splitlines():
                    line = line.strip()
                    if line:
                        return line
    except:
        return None

def rename_file_by_first_line(file_path):
    if not os.path.isfile(file_path):
        return

    filename = os.path.basename(file_path)
    folder = os.path.dirname(file_path)
    ext = filename.lower().split('.')[-1]

    new_name = None
    if ext == "docx":
        new_name = extract_word_first_line(file_path)
        new_ext = ".docx"
    elif ext == "pdf":
        new_name = extract_pdf_first_line(file_path)
        new_ext = ".pdf"
    else:
        return

    if new_name:
        new_name = sanitize_filename(new_name[:50]) + new_ext
        new_path = os.path.join(folder, new_name)
        if not os.path.exists(new_path):
            os.rename(file_path, new_path)
            print(f"✅ {filename} → {new_name}")
        else:
            print(f"⚠️ 目標檔名已存在: {new_name}")
    else:
        print(f"❌ 無法提取第一行文字: {filename}")

def rename_files_in_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for item in files:
            file_path = os.path.join(root, item)
            rename_file_by_first_line(file_path)

# ---------------- 清理重複文件 ----------------
def sanitize_base_name(filename):
    base, ext = os.path.splitext(filename)
    base = re.sub(r'\(\d+\)$', '', base)
    return base, ext

def collect_all_files(folder_path):
    all_files = []
    for root, dirs, files in os.walk(folder_path):
        for f in files:
            full_path = os.path.join(root, f)
            all_files.append(full_path)
    return all_files

def clean_duplicates_in_folder_tree(folder_path):
    all_files = collect_all_files(folder_path)
    file_groups = {}

    for f in all_files:
        if os.path.isfile(f):
            base, ext = sanitize_base_name(os.path.basename(f))
            key = (base.lower(), ext.lower())
            if key not in file_groups:
                file_groups[key] = []
            file_groups[key].append(f)

    for key, paths in file_groups.items():
        if len(paths) > 1:
            paths.sort(key=lambda x: os.path.getmtime(x))
            for old_file in paths[:-1]:
                os.remove(old_file)
                print(f"刪除舊檔: {old_file}")
            latest_file = paths[-1]
            base, ext = key
            new_path = os.path.join(folder_path, base + ext)
            if latest_file != new_path:
                if os.path.exists(new_path):
                    os.remove(new_path)
                os.rename(latest_file, new_path)
                print(f"重命名: {latest_file} → {new_path}")

# ---------------- 圖片改名 ----------------
geolocator = Nominatim(user_agent="photo_renamer")

def convert_to_degrees(value, ref):
    d = value[0][0] / value[0][1]
    m = value[1][0] / value[1][1]
    s = value[2][0] / value[2][1]
    deg = d + m/60 + s/3600
    if ref in ['S', 'W']:
        deg = -deg
    return deg

def get_exif_data(image_path):
    try:
        img = Image.open(image_path)
        exif_bytes = img.info.get('exif')
        if exif_bytes:
            return piexif.load(exif_bytes)
        else:
            return None
    except:
        return None

def get_datetime_and_gps(exif_dict, file_path):
    datetime_str = None
    gps_coords = None

    if exif_dict and '0th' in exif_dict:
        dt_bytes = exif_dict['0th'].get(piexif.ImageIFD.DateTime)
        if dt_bytes:
            datetime_str = dt_bytes.decode().replace(":", "-").replace(" ", "_")

    if exif_dict and 'GPS' in exif_dict and exif_dict['GPS']:
        gps_info = exif_dict['GPS']
        lat = gps_info.get(piexif.GPSIFD.GPSLatitude)
        lat_ref = gps_info.get(piexif.GPSIFD.GPSLatitudeRef)
        lon = gps_info.get(piexif.GPSIFD.GPSLongitude)
        lon_ref = gps_info.get(piexif.GPSIFD.GPSLongitudeRef)
        if lat and lat_ref and lon and lon_ref:
            gps_coords = (convert_to_degrees(lat, lat_ref.decode()),
                          convert_to_degrees(lon, lon_ref.decode()))

    if not datetime_str:
        t = os.path.getctime(file_path)
        datetime_str = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime(t))

    return datetime_str, gps_coords

def get_county_city_from_gps(coords):
    try:
        location = geolocator.reverse(coords, language='zh')
        if location and 'address' in location.raw:
            address = location.raw['address']
            county = address.get('county')
            city = address.get('city') or address.get('town') or address.get('village')
            if county:
                return county
            elif city:
                return city
    except:
        pass
    return None

def rename_photo(file_path):
    exif = get_exif_data(file_path)
    datetime_str, gps_coords = get_datetime_and_gps(exif, file_path)

    location_name = None
    if gps_coords:
        location_name = get_county_city_from_gps(gps_coords)

    parts = []
    if location_name:
        parts.append(location_name)
    if datetime_str:
        parts.append(datetime_str)

    if parts:
        folder = os.path.dirname(file_path)
        ext = os.path.splitext(file_path)[1].lower()
        new_name = sanitize_filename("_".join(parts)) + ext
        new_path = os.path.join(folder, new_name)
        if not os.path.exists(new_path):
            os.rename(file_path, new_path)
            print(f"✅ {os.path.basename(file_path)} → {new_name}")
        else:
            print(f"⚠️ 目標檔名已存在: {new_name}")
    else:
        print(f"❌ 無法提取資料: {file_path}")

def rename_photos_in_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for f in files:
            if f.lower().endswith(('.jpg', '.jpeg')):
                file_path = os.path.join(root, f)
                rename_photo(file_path)

# ---------------- GUI ----------------
def center_window(root, width, height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = int((screen_width - width) / 2)
    y = int((screen_height - height) / 2)
    root.geometry(f"{width}x{height}+{x}+{y}")

def select_folder_and_clean():
    folder_path = filedialog.askdirectory(title="選擇資料夾進行清理重複文件")
    if folder_path:
        status_label.config(text=f"清理中: {folder_path}")
        root.update()
        clean_duplicates_in_folder_tree(folder_path)
        status_label.config(text=f"完成! 已清理: {folder_path}")

def select_folder_and_rename():
    folder_path = filedialog.askdirectory(title="選擇資料夾進行重命名 Word/PDF")
    if folder_path:
        status_label.config(text=f"重命名中: {folder_path}")
        root.update()
        rename_files_in_folder(folder_path)
        status_label.config(text=f"完成! 已重命名 Word/PDF: {folder_path}")

def select_folder_and_rename_photos():
    folder_path = filedialog.askdirectory(title="選擇資料夾進行重命名圖片")
    if folder_path:
        status_label.config(text=f"重命名圖片中: {folder_path}")
        root.update()
        rename_photos_in_folder(folder_path)
        status_label.config(text=f"完成! 已重命名圖片: {folder_path}")

# ---------------- 主程式 ----------------
root = Tk()
root.title("清理文件工具")
center_window(root, 800, 200)

button_clean = Button(root, text="清理重複文件", command=select_folder_and_clean, width=25, height=4)
button_clean.pack(side=LEFT, padx=20, pady=30)

button_rename = Button(root, text="重命名 Word/PDF", command=select_folder_and_rename, width=25, height=4)
button_rename.pack(side=LEFT, padx=20, pady=30)

button_photo = Button(root, text="重命名圖片", command=select_folder_and_rename_photos, width=25, height=4)
button_photo.pack(side=LEFT, padx=20, pady=30)

status_label = Label(root, text="等待操作...", wraplength=780)
status_label.pack(pady=10)

root.mainloop()
