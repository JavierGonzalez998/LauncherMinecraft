import customtkinter as ctk
import minecraft_launcher_lib
import psutil
import subprocess
from tkinter import messagebox
import os

user = os.environ["USERNAME"]
dir = f"C:/USERS/{user}/AppData/Roaming/.minecraft"
memtotal = round(psutil.virtual_memory().total / (1024 ** 3))
mem = round(memtotal * 0.15)
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

#Ventana
window = ctk.CTk()
window_width = 500
window_height = 500
# Obtener el tamaño de la pantalla
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calcular la posición en el centro de la pantalla
position_x = int((screen_width / 2) - (window_width / 2))
position_y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

window.title("Launcher - Made By Javo")
window.resizable(False, False)

#Widgets
btn_exec_minecraft = ctk.CTkButton(window, text="Iniciar Minecraft", text_color="white", fg_color="#3b82f6")
btn_install_versions = ctk.CTkButton(window, text="Instalar Versiones de Minecraft", text_color="white", fg_color="#10b981")
btn_install_forge = ctk.CTkButton(window, text="Instalar Forge", text_color="white", fg_color="#ef4444")

label_name = ctk.CTkLabel(window, text="User:", text_color="white", font=("Arial", 12))
label_ram = ctk.CTkLabel(window, text=f"Ingrese la memoria RAM a usar en gb. Recomendado: {mem}gb", text_color="white", font=("Arial", 12))

entry_name = ctk.CTkEntry(window, placeholder_text="User")
entry_ram = ctk.CTkEntry(window, placeholder_text="RAM")

def Load_versions() -> list:
    return [version["id"] for version in minecraft_launcher_lib.utils.get_installed_versions(dir)]

installedVersions = Load_versions()

if len(installedVersions) != 0:
    vers = ctk.StringVar(value=installedVersions[0])
else:
    vers = ctk.StringVar(value="No Versions")

installed_versions_label = ctk.CTkLabel(window, text="Versiones instaladas:", font=("Arial",12))
installedVersionsMenu = ctk.CTkOptionMenu(window, variable=vers, values=installedVersions)
installedVersionsMenu.configure()



def Install():
    version = entry_version.get()
    if version:
        messagebox.showinfo("Instalando",f"Instalando versión {version}. Por favor, espere")
        minecraft_launcher_lib.install.install_minecraft_version(version, dir)
        global installedVersions
        installedVersions = Load_versions()
        messagebox.showinfo("Exito", f"Se ha instalado la versión {version}")
    else:
        messagebox.showerror("Error", "Por favor, ingrese una versión válida")

def Install_forge() -> bool:
    version = entry_version.get()
    forge = minecraft_launcher_lib.forge.find_forge_version(version)
    if forge:
        messagebox.showinfo("Instalando",f"Instalando forge {version}. Por favor, espere")
        minecraft_launcher_lib.forge.install_forge_version(forge, dir)
        global installedVersions
        installedVersions = Load_versions()
        messagebox.showinfo("Éxito",f"Forge instalado, version: {version}")
    else:
        messagebox.showerror("Error", "No se encontró una versión de Forge para esta versión de Minecraft")

def Exec():
    user = entry_name.get()
    ram = entry_ram.get()
    
    if not user:
        messagebox.showerror("Error", "Por favor, ingrese un nombre de usuario")
        return
    if not ram:
        messagebox.showerror("Error", "Por favor, ingrese la cantidad de memoria RAM a ejecutar")
        return
    version = vers.get()
    options = {
        "username": user,
        "uuid": "",
        "token": "",
        "jvmArguments": [f"-Xmx{ram}G", f"-Xms{ram}G"],
        "launcherVersion": "0.0.2",
    }
    window.destroy()
    comm = minecraft_launcher_lib.command.get_minecraft_command(version, dir, options)
    subprocess.run(comm)

def install_ver():
    verWindow = ctk.CTkToplevel(window)
    verWindow.geometry(f"300x150+{position_x}+{position_y}")
    verWindow.title(f"Instalar version")
    verWindow.grab_set()
    
    global entry_version
    
    entry_version = ctk.CTkEntry(verWindow, placeholder_text="Ingrese la versión")
    entry_version.pack(pady=10)
    
    btn_install = ctk.CTkButton(verWindow, command=Install, text="Instalar")
    btn_install.pack(pady=10)
    
def install_forge_ver():
    verWindow = ctk.CTkToplevel(window)
    verWindow.geometry(f"300x150+{position_x}+{position_y}")
    verWindow.title(f"Instalar forge")
    verWindow.grab_set()
    
    global entry_version
    
    entry_version = ctk.CTkEntry(verWindow, placeholder_text="Ingrese la versión")
    entry_version.pack(pady=10)
    
    btn_install = ctk.CTkButton(verWindow, command=Install_forge, text="Instalar")
    btn_install.pack(pady=10)



def Menu():
    btn_install_versions.configure(command=install_ver)
    btn_install_versions.place(x=20, y=400)
    
    btn_install_forge.configure(command=install_forge_ver)
    btn_install_forge.place(x=280, y=400)
    
    label_name.place(x=20,y=30)
    entry_name.place(x=20, y=70)
    
    label_ram.place(x=20, y=110)
    entry_ram.place(x=20, y=150)
    
    installed_versions_label.place(x=20, y=210)
    installedVersionsMenu.place(x=20, y=240)
    
    btn_exec_minecraft.configure(command=Exec)
    btn_exec_minecraft.place(x=250, y=240)
    
    window.mainloop()
    