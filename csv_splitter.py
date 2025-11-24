import os

def split_csv_by_size(source, output_dir, max_size_mb=100):
    max_size = max_size_mb * 1024 * 1024  # bytes
    part = 1

    output_path = os.path.join(output_dir, f"{os.path.basename(source)}_part_{part}.csv")
    writer = open(output_path, "wb")  # binary write
    current_size = 0

    with open(source, "rb") as reader:  # binary read
        for line in reader:
            line_size = len(line)

            if current_size + line_size > max_size:
                writer.close()
                part += 1
                output_path = os.path.join(
                    output_dir, f"{os.path.basename(source)}_part_{part}.csv"
                )
                writer = open(output_path, "wb")
                current_size = 0

            writer.write(line)
            current_size += line_size

    writer.close()
    print(f"完成！共分割成 {part} 個檔案。")


# -------------------------
# 修改這兩個參數即可使用
# -------------------------

source_file = r"C:\Users\stella.dai\Downloads\BGMOPEN1.csv"
output_folder = r"C:\Users\stella.dai\Downloads"

split_csv_by_size(source_file, output_folder, max_size_mb=80)
