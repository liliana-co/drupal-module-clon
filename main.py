'''
    script para renombrar archivos y modificar contenido interno en la clonacion de modulos drupal
'''
import shutil
import os

if __name__ == "__main__":
    ruta_origen = input('entre la ruta origen del modulo a clonar: ')
    new_module_name = input('escriba el nuevo nombre del modulo: ')
    ruta_destino = os.path.dirname(ruta_origen)
    destination = shutil.copytree(ruta_origen, ruta_destino+'\\'+new_module_name)
    old_module_name = os.path.basename(ruta_origen)
    #let's rename the files wich has the old module name with the new module name    
    for path,subdir,files in os.walk(destination):
        for name in files:
            if name.split('.')[-1] in ['php', 'yml', 'module', 'theme', 'install']:                
                old_file = new_file = os.path.join(path,name)
                if old_module_name in name:
                    new_file = os.path.join(path,name.replace(old_module_name,new_module_name))
                    os.rename(old_file, new_file)
                new_content = ""
                with open(new_file, "r", encoding="utf8") as current_file:
                    old_content = current_file.read()
                    new_content = old_content.replace(old_module_name, new_module_name)
                with open(new_file, "w", encoding="utf8") as current_file:
                    current_file.write(new_content)    