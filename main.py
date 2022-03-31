import os, tkinter, psd_tools

root = tkinter.Tk()
root.withdraw()

file_path = tkinter.filedialog.askdirectory()

for index, file_name in enumerate(os.listdir(file_path)):
	if '.psd' in file_name:
		print(f'converting {index} ',file_name)
		psd_tools.PSDImage
			.open(file_name)
			.composite()
			.save(f"{file_name.replace('.psd','')}.pdf")
