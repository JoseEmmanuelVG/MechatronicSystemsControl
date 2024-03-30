import os

# Ruta de la carpeta que contiene los archivos
folder_path = "/workspaces/MechatronicSystemsControl/docs"

# Agregar el pie de pagina a los archivos markdown
FOOTER = """
<details>
  <summary>🌟 Did you find any repository useful?</summary>
  If any project has been helpful to you, consider giving it a ⭐ star in the repository and follow my GitHub account to stay tuned for future updates! 🚀

  In addition, I am always open to suggestions, recommendations or collaborations. Feel free to [get in touch](https://www.linkedin.com/in/vazquez-galan-jose-emmanuel-664968221) if you have any questions or ideas for improving this project. I'm excited for your feedback and contributions.

  Thank you for your interest and support! 😊
</details>

<p align="center">
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
</p>
"""

# Función para verificar si el footer ya está en el archivo
def footer_already_added(file_path):
    with open(file_path, 'r') as file:
        if FOOTER.strip() in file.read():
            return True
    return False

# Función para agregar el footer a un archivo si aún no está
def add_footer_to_file(file_path):
    if not footer_already_added(file_path):
        with open(file_path, 'a') as file:  # Abre el archivo en modo append
            file.write(FOOTER)  # Agrega el footer
            print(f"Footer added to {file_path}")
    else:
        print(f"Footer already present in {file_path}")

# Lista de nombres de archivos para modificar
file_names = [f"e{i}.md" for i in range(1, 7)]

# Ejecutar la función add_footer_to_file en cada archivo
for name in file_names:
    full_path = os.path.join(folder_path, name)
    add_footer_to_file(full_path)
