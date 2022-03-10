from psd_tools import PSDImage
import os

for index, file_name in enumerate(os.listdir('./')):
	if '.psd' in file_name:
		print(f'converting {index} ',file_name)
		PSDImage.open(file_name).composite().save(f"{file_name.replace('.psd','')}.pdf")
