import os
import shutil
import glob

# Ensure directories exist
dirs = ['docs', 'docs/reports', 'docs/presentations', 'scripts', 'assets', 'src', 'src/old_flask_app']
for d in dirs:
    os.makedirs(d, exist_ok=True)

def move_files(pattern, dest):
    for f in glob.glob(pattern):
        if os.path.isfile(f) and f != 'organize_project.py':
            try:
                shutil.move(f, os.path.join(dest, os.path.basename(f)))
            except Exception as e:
                pass

def move_dir(src, dest):
    if os.path.exists(src) and os.path.isdir(src):
        try:
            shutil.move(src, dest)
        except Exception as e:
            pass

# Move docs
move_files('*.docx', 'docs/reports')
move_files('*.pdf', 'docs/reports')
move_files('*.html', 'docs/reports')
move_files('*.md', 'docs')
move_files('*.txt', 'docs')
move_files('*.pptx', 'docs/presentations')

# Move scripts
move_files('*.py', 'scripts')

# Move assets
move_files('*.png', 'assets')
move_files('*.jpg', 'assets')

# Move old root flask app
move_files('app.py', 'src/old_flask_app')
move_dir('instance', 'src/old_flask_app/instance')
move_dir('templates', 'src/old_flask_app/templates')

# Consolidate src
if os.path.exists('jaymani-krishi-sewa'):
    for item in os.listdir('jaymani-krishi-sewa'):
        try:
            shutil.move(os.path.join('jaymani-krishi-sewa', item), os.path.join('src', item))
        except:
            pass
    try:
        os.rmdir('jaymani-krishi-sewa')
    except:
        pass

# Move other scattered dirs
move_dir('frontend', 'src/frontend_generated')
move_dir('backend', 'src/backend_generated')
move_dir('jaymani-krishi-sewa-vanilla', 'src/jaymani-krishi-sewa-vanilla')
move_dir('JMKS', 'docs/JMKS_history')
move_dir('scratch_pptx', 'scripts/scratch_pptx')

print("Workspace organized successfully!")
