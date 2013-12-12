from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.

company_name = "Epitech"
product_name = "Blih"

bdist_msi_options = {
    'add_to_path': True,
    'initial_target_dir': r'[ProgramFilesFolder]\%s\%s' % (company_name, product_name),
    }

build_exe_options = {
	
}

base = 'Console'

executables = [
    Executable('blih.py', base=base)
]

setup(name='blih2exe',
      version = '0.2',
      description = 'Portage de blih sur windows',
      options={
          'bdist_msi': bdist_msi_options,
          'build_exe': build_exe_options},
      executables = executables)
