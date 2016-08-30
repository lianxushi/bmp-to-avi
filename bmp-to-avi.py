#!\usr\bin\env python
# -*- coding: utf-8 -*-
# Author: PZX
# FileName: batchrename.py
# Function: 批量命名某一文件夹下的文件名
import sys
import os
DIR=' '
def UsePrompt():
    #如果省略path，则path为当前路径
    print 'Useage: batchrename.py [path] newfilenames'
    sys.exit()

def compare(x, y):
    global DIR
    print DIR
    stat_x = os.stat(DIR + "/" + x)  
    stat_y = os.stat(DIR + "/" + y)  
    if stat_x.st_ctime > stat_y.st_ctime:  
        return -1  
    elif stat_x.st_ctime < stat_y.st_ctime:  
        return 1  
    else:  
        return 0

def BatchRename(path, pattern):
    #设置路径
    os.chdir(path)
    fileList = os.listdir(path)
    #fileList.sort(compare) 
    dotIndex = pattern.rfind('.')
    fileName = pattern[ : dotIndex]
    fileExt = pattern[dotIndex : ]
    genNum = 0
    for fileItem in fileList:
        fileFullName = fileName + str(genNum) + fileExt
        try:
            os.rename(fileItem, fileFullName)
        except OSError,e:
            print e
        print (fileItem + ' => ' + fileFullName) 
        genNum += 1
        
def BatchRemove(path, pattern):
    #设置路径
    os.chdir(path)
    fileList = os.listdir(path)
    dotIndex = pattern.rfind('.')
    fileName = pattern[ : dotIndex]
    fileExt = pattern[dotIndex : ]
    lenth=len(fileExt)
    for fileItem in fileList:
        if fileItem[-lenth:]==fileExt:
            os.remove(fileItem)
            print fileItem


    
def convertbmp2mp4(rootDir,re_pattern):
    sys_cmd = 'd:/software/ffmpeg-20160718-450cf40-win64-shared/bin/ffmpeg.exe '
    sys_cmd_pre_args = ' -f image2 -i '
    #sys_cmd_pre_args = ' -f rawvideo -i '
    #sys_cmd_post_args = ' -vcodec libx264 -r 25 '
    sys_cmd_post_args = ' -vcodec rawvideo -r 25 -pix_fmt rgb24 '
    list_dirs = os.walk(rootDir)
    global DIR
    for root, dirs, files in list_dirs:
        for sub_dir in dirs:
            absolute_path_sudir = os.path.join(root, sub_dir)
            absolute_path_sudir_file = absolute_path_sudir + '/' + '%01d.bmp'
	    #absolute_path_mp4 = absolute_path_sudir + '/'+ sub_dir +'.mp4'
            absolute_path_mp4 = absolute_path_sudir + '/'+ sub_dir +'.avi'
            print absolute_path_sudir
            print absolute_path_sudir_file
            print absolute_path_mp4
            DIR = absolute_path_sudir
            BatchRename(absolute_path_sudir, re_pattern)
            sys_cmd_combines = sys_cmd + sys_cmd_pre_args + absolute_path_sudir_file + sys_cmd_post_args + absolute_path_mp4
            print sys_cmd_combines
            os.system(sys_cmd_combines)
            #BatchRemove(absolute_path_sudir, re_pattern) 

def main():
    if len(sys.argv) == 3:
        path = sys.argv[1]
        pattern = sys.argv[2]
    elif len(sys.argv) == 2:
        path = os.getcwd()
        pattern = sys.argv[1]
    else:
        UsePrompt()
    confirm = raw_input('Confirm(y|n): ')
    if confirm == 'n':
        sys.exit()
    #BatchRename(path, pattern)
    #print path
    #print pattern
    convertbmp2mp4(path,pattern)
    
if __name__ == '__main__':
    main()
          

