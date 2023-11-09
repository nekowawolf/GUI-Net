import tkinter as tk
import socket

def nslookup(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        print(f"Nama domain: {domain}")
        print(f"Alamat IP: {ip_address}")
    except socket.gaierror:
        print(f"Tidak dapat menemukan alamat IP untuk domain: {domain}")

if __name__ == "__main__":
    domain = input("Masukan domain yang ingin Anda cek: ")
    nslookup(domain)

# Membuat jendela utama
root = tk.Tk()
root.title("Nslookup App")

root.geometry("400x200")

domain_label = tk.Label(root, text="Masukan Domain:")
domain_label.pack(pady=10)
domain_entry = tk.Entry(root)
domain_entry.pack()

lookup_button = tk.Button(root, text="Nslookup," command=nslookup)
lookup_button.pack(pady=10)

result_label = tk.Label(root, text="", wraplegth=300)
result_label.pack()

root.mainloop()
_