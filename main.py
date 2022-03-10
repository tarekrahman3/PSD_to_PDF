from psd_tools import PSDImage
import os

files = os.listdir('./')
for index, file_name in enumerate(files):
	if '.psd' in file_name:
		print(f'converting {index} ',file_name)
		psd = PSDImage.open(file_name)
		psd.composite().save(f"{file_name.replace('.psd','')}.pdf")
