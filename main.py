from psd_tools import PSDImage
import os

files = os.listdir('./')
files.remove('main.py')
print(files)
for file_name in files:
	print('converting ',file_name)
	psd = PSDImage.open(file_name)
	psd.composite().save(f'{file_name.replace('.psd','')}.pdf')
