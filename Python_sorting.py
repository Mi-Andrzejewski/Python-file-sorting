import os
import shutil

#Path
FilePath = os.path.dirname(os.path.abspath(__file__))

#Extensions
FileExtension = {'zip':'Archives','rar':'Archives','sql':'Database','pdf':'Pdf','webm':'Video','mp4':'Video','mkv':'Video','mp3':'Music','exe':'Exe','odt':'Document','txt':'Document','doc':'Document','docx':'Document',
                 'xls':'Data','html':'Web','css':'Web','iso':'Iso','pkt':'Pkt','wav':'Music','gif':'Image','png':'Image','jpg':'Image','jfif':'Image','jpeg':'Image','csv':'Data','xlsx':'Data',
                 'avi':'Video','ogg':'Music','mov':'Video','pptx':'Document','bmp':'Image'}

#Creating folders and moving files
for FileName in os.listdir(FilePath):
    N_Path = os.path.join(FilePath, FileName)
    if os.path.isfile(N_Path):
        Extension = FileName.lower().split('.')[-1]
        if Extension in FileExtension:
            Folder_N = FileExtension[Extension]
            Folder_P = os.path.join(FilePath,Folder_N)

            
            os.makedirs(Folder_P , exist_ok = True)
            
            shutil.move(N_Path, os.path.join(Folder_P , FileName))
