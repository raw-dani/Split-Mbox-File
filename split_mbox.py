import os

def split_mbox(input_file, output_prefix, max_size_gb=2):
    max_size = max_size_gb * 1024 * 1024 * 1024  # Convert GB to bytes
    part_num = 1
    current_size = 0
    output_file = None
    buffer = []

    with open(input_file, 'r', encoding='utf-8', errors='ignore') as infile:
        for line in infile:
            # Jika baris dimulai dengan "From " (header MBOX baru)
            if line.startswith('From '):
                # Jika ukuran file melebihi max_size, buat file baru
                if output_file and current_size >= max_size:
                    output_file.close()
                    output_file = None
                    part_num += 1
                    current_size = 0
                
                # Jika belum ada file output, buka file baru
                if output_file is None:
                    output_filename = f"{output_prefix}_part{part_num}.mbox"
                    output_file = open(output_filename, 'w', encoding='utf-8')
            
            # Tulis baris ke file output
            if output_file:
                output_file.write(line)
                current_size += len(line.encode('utf-8'))

    # Tutup file terakhir
    if output_file:
        output_file.close()

if __name__ == "__main__":
    input_file = "file.mbox"       # Ganti dengan file Anda
    output_prefix = "file_output"   # Prefix untuk output
    split_mbox(input_file, output_prefix, 2)  # 2GB per file
