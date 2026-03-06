# cloner.py
import shutil
import os
 
def clone_module(source, new_name, dest=False, verbose=False):
  if not os.path.exists(source):
    raise FileNotFoundError(f"Ruta fuente no encontrada: {source}")
  if not dest:
    dest = os.path.dirname(source)
    
  destination = shutil.copytree(source, os.path.join(dest, new_name))
  old_module_name = os.path.basename(source)
  
  for path,subdir,files in os.walk(destination):
    for name in files:
      if name.split('.')[-1] in ['php', 'yml', 'module', 'theme', 'install']:
        old_file = new_file = os.path.join(path,name)
        if old_module_name in name:
          new_file = os.path.join(path,name.replace(old_module_name,new_name))
          os.rename(old_file, new_file)
          if verbose:
            print(f"Renombrado: {old_file} -> {new_file}")
        new_content = ""
        with open(new_file, "r", encoding="utf8") as current_file:
          old_content = current_file.read()
          new_content = old_content.replace(old_module_name, new_name)
        with open(new_file, "w", encoding="utf8") as current_file:
          current_file.write(new_content)
          if verbose:
            print(f"Actualizado contenido en: {new_file}")
  