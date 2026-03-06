# tests/test_cloner.py
import pytest
from custom_cloner.cloner import clone_module
from pathlib import Path

@pytest.fixture
def setup_test_module(tmp_path):
  """creamos un modulo falso para testear"""
  module_path = tmp_path / "test_module"
  module_path.mkdir()
  """creamos archivos de ejemplo dentro del módulo"""
  (module_path / "test_module.info.yml").write_text("name: Test Module\ntype: module\n")
  (module_path / "test_module.module").write_text("<?php\n// Test module\n")
  """creamos subcarpeta con archivos dentro del módulo"""
  subfolder = module_path / "src"
  subfolder.mkdir()
  (subfolder / "example.php").write_text("<?php\n// Example file\n")
  return module_path

# pruebas
def test_directory_is_created(setup_test_module, tmp_path):
    dest = tmp_path / "new_module"
    clone_module(setup_test_module, "my_module", dest, "new_module")
    assert dest.exists()


def test_files_are_copied(setup_test_module, tmp_path):
    dest = tmp_path / "new_module"
    clone_module(setup_test_module, "my_module", dest, "new_module")
    archivos = list(dest.rglob("*"))
    assert len(archivos) > 0


def test_files_are_renamed(setup_test_module, tmp_path):
    dest = tmp_path / "new_module"
    clone_module(setup_test_module, "my_module", dest, "new_module")
    assert (dest / "new_module.info.yml").exists()
    assert (dest / "new_module.module").exists()


def test_old_name_not_in_destination(setup_test_module, tmp_path):
    dest = tmp_path / "new_module"
    clone_module(setup_test_module, "my_module", dest, "new_module")
    archivos = [f.name for f in dest.rglob("*")]
    assert not any("my_module" in nombre for nombre in archivos)


def test_internal_content_is_replaced(setup_test_module, tmp_path):
    dest = tmp_path / "new_module"
    clone_module(setup_test_module, "my_module", dest, "new_module")
    contenido = (dest / "new_module.info.yml").read_text()
    assert "new_module" in contenido
    assert "my_module" not in contenido


def test_subdir_are_copied(setup_test_module, tmp_path):
    dest = tmp_path / "new_module"
    clone_module(setup_test_module, "my_module", dest, "new_module")
    assert (dest / "templates").exists()


def test_error_if_path_does_not_exist(tmp_path):
    with pytest.raises(FileNotFoundError):
        clone_module(tmp_path / "no_existe", "x", tmp_path / "dest", "y")
