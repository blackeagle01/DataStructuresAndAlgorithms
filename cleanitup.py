'''
import os
for file in os.listdir():
	if file=='red.py':
		continue
	print('rename',file,'to')
	os.rename(file,input())

'''
'''
import os,shutil
for files in os.listdir():
      if files.endswith('.txt'):
            shutil.move(files,os.path.join(os.getcwd(),'text'))
'''
import os,shutil
text=['.oc','.odt','.pdf','.rtf','.tex','.txt','.wks','.pptx']
programs=['.py','.cpp','.c','.java']
vids=['.mp4','.webm','.flv','.mkv','.avi','.wmv','.3gp']
audios=['.aa','.mp3','.m3p','.mmp']
images=['.jpeg','.bmp','.jpg','.tif']
os.mkdir('Docs')
os.mkdir('Programs')
os.mkdir('Audio')
os.mkdir('Vids')
os.mkdir('Misc')
os.mkdir('Images')
for files in os.listdir():
	if os.path.isfile(files):
		a,b=os.path.splitext(files)
		if b in text:
			shutil.move(files,os.path.join(os.getcwd(),'Docs'))
		elif b in programs:
			shutil.move(files,os.path.join(os.getcwd(),'Programs'))
		elif b in audios:
			shutil.move(files,os.path.join(os.getcwd(),'Audio'))
		elif b in images:
			shutil.move(files,os.path.join(os.getcwd(),'Images'))
		elif b in vids:
			shutil.move(files,os.path.join(os.getcwd(),'Vids'))
		
		else:
			shutil.move(files,os.path.join(os.getcwd(),'Misc'))
