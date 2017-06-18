#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
"""
    Implémentation des outils de normalization de l'image.
 
    Usage:
 
    >>> import MetaLex as dico
    >>> import ImageFilter
    >>> project = dico.newProject(project_name)
    >>> images = project.MetaLex.getImages(imagelist)
    >>> images.enhanceImages().filter(f.DETAIL)
    >>> images.enhanceImages().bright(1, save=True)
    
    ImageFilter.filters :
    
    'BLUR', 'BuiltinFilter', 'CONTOUR', 'DETAIL', 'EDGE_ENHANCE', 
    'EDGE_ENHANCE_MORE', 'EMBOSS', 'FIND_EDGES', 'Filter', 
    'GaussianBlur', 'Kernel', 'MaxFilter', 'MedianFilter', 
    'MinFilter', 'ModeFilter', 'RankFilter', 
    'SHARPEN', 'SMOOTH', 'SMOOTH_MORE', 'UnsharpMask'
          
"""

# ----Internal Modules------------------------------------------------------

import MetaLex
from MetaLex import dicProject

# ----External Modules------------------------------------------------------

import Image, os
import ImageEnhance
from shutil import copyfile
import warnings

# ----Exported Functions-----------------------------------------------------

__all__ = ['getImages', 'enhanceImages']

# ----------------------------------------------------------


def getImages(images):
    """Take input image list and save it in the scope"""
    
    if len(images) >= 1 :
        num = 1
        for image in images : 
            exts = ('.png', '.jpg', '.JPG', '.jpeg', '.PNG', '.JPEG', '.tif', '.gif')
            imageroot, ext = dicProject.get_part_file(image)
            if os.path.isfile(image) and ext in exts:
                imagedir = os.path.dirname(image)
                
                imagedirNew = ""
                for tep in imagedir.split('/')[:-1] :
                    imagedirNew += tep +"/"
                imagedirNew = imagedirNew+"dicImages/"
                
                if not os.path.exists(imagedirNew) :
                    os.mkdir(imagedirNew)
                    
                imagefileNew = "dic_image_"+str(num)+ext
                imageLocationNew =  imagedirNew+'/'+imagefileNew
                copyfile(image, imageLocationNew)
                MetaLex.fileImages.append(imageLocationNew)
                num += 1
            else :
                print " Error : getImages(images) >> The input image '"+imageroot+ext+"' is not a file image"
                
        imagestr = str(images)
        message = imagestr + ' > are append for the current treatment' 
        MetaLex.dicLog.manageLog.writelog(message)
    else: 
        message = ' Error : getImages(images) >> They are not images for the current treatment : input images !!' 
        print message+"\n"
        MetaLex.dicLog.manageLog.writelog(message)
        
    return MetaLex
    
        
   
class enhanceImages ():
    """
    This Class enhance image file and save them to 'dicTemp'
    """
    
    def __init__(self): 
        self.images = MetaLex.fileImages
        
    def contrast(self, value, show=False, save=False):
        """Enhance image file with the contrast value"""
        
        if self.images >= 1 : 
            num = 1
            for image in  self.images :
                img = Image.open(image)
                imagename, ext = dicProject.get_part_file(image)
                tempname = 'img_contrast_'+str(num)+ext
                enh = ImageEnhance.Contrast(img)
                
                if show :
                    enh.enhance(value).show()
                elif save :
                    dicProject.createtemp()
                    enh.enhance(value).save(tempname)
                    dicProject.treat_image_append(tempname)
                    message = imagename + 'is modified with contrast (' +str(value)+ ') > '+tempname+' > Saved in dicTemp folder'  
                    MetaLex.dicLog.manageLog.writelog(message) 
                    num += 1 
                else :
                    print ' Warning : contrast(value, show=False, save=False) --> You must define one action for the current treatment : show=true or save=true '
                    
        else:
            message = ' Error : getImages(images) >> They are not images for the current treatment : please input images !! ' 
            print "--> "+message+"\n"
            MetaLex.dicLog.manageLog.writelog(message)
            
            
    def sharp(self, value, show=False, save=False):
        """Enhance image file with the sharp value"""
        
        if len(self.images) >= 1 :
            num = 1
            for image in  self.images :
                img_conv = self.convert(image, save=True)
                img = Image.open(img_conv)
                imagename, ext = dicProject.get_part_file(image)
                tempname = 'img_sharp_'+str(num)+ext
                enh = ImageEnhance.Sharpness(img)

                if show :
                    enh.enhance(value).show()
                elif save :
                    dicProject.createtemp()
                    enh.enhance(value).save(tempname)
                    dicProject.treat_image_append(tempname)
                    message = imagename + 'is modified with sharp ( ' +str(value)+ ') > '+tempname+' > Saved in dicTemp folder'  
                    MetaLex.dicLog.manageLog.writelog(message) 
                    num += 1 
                else :
                    print 'Warning : sharp(value, show=False, save=False) --> You must define one action for the current treatment : show=true or save=true '
        
        else:
            message = ' Error : getImages(images) >> They are not images for the current treatment : please input images !! ' 
            print "--> "+message+"\n"
            MetaLex.dicLog.manageLog.writelog(message)
            
            
    def bright(self, value, show=False, save=False):
        """Enhance image file with the bright value"""
        
        if len(self.images) >= 1 :
            num = 1
            for image in  self.images :
                img_conv = self.convert(image, save=True)
                img = Image.open(img_conv)
                imagename, ext = dicProject.get_part_file(image)
                tempname = 'img_bright_'+str(num)+ext
                enh = ImageEnhance.Brightness(img)

                if show :
                    enh.enhance(value).show()
                elif save :
                    dicProject.createtemp()
                    enh.enhance(value).save(tempname)
                    dicProject.treat_image_append(tempname)
                    message = imagename + 'is modified with bright (' +str(value)+ ') > '+tempname+' > Saved in dicTemp folder'  
                    MetaLex.dicLog.manageLog.writelog(message) 
                    num += 1 
                else :
                    print 'Warning : bright(value, show=False, save=False) --> You must define one action for the current treatment : show=true or save=true '
        else:
            message = ' Error : getImages(images) >> They are not images for the current treatment : input images!!' 
            print "--> "+message+"\n"
            MetaLex.dicLog.manageLog.writelog(message)
            
            
    def contrastBright(self, contrast, bright, show=False, save=False):
        """Enhance image file with the contrastBright value"""
        
        if len(self.images) >= 1 :
            num = 1
            for image in  self.images :
                img_conv = self.removeColor(image, save=True)
                img = Image.open(img_conv)
                imagename, ext = dicProject.get_part_file(image)
                tempname = 'img_bright_'+str(num)+ext
                enhbright = ImageEnhance.Brightness(img)
                dicProject.createtemp()
                enhbright.enhance(bright).save(tempname)
                img2 = Image.open(tempname)
                enhconst = ImageEnhance.Contrast(img2)
                if show :
                    enhconst.enhance(contrast).show()
                    dicProject.createtemp()
                    os.remove(tempname)
                if save :
                    tempname2 = 'img_contrast_bright_'+str(num)+ext
                    dicProject.createtemp()
                    enhconst.enhance(contrast).save(tempname2)
                    os.remove(tempname)
                    os.remove(img_conv)
                    dicProject.treat_image_append(tempname2)
                    
                message = imagename + ' is modified with  contrast (' +str(contrast)+ ') and  bright ('+str(bright)+') > '+tempname2+' > Saved in dicTemp folder'  
                MetaLex.dicLog.manageLog.writelog(message) 
                img.close()
                num += 1
        else:
            message = '  > They are not images for the current treatment : input images!!' 
            print "--> "+message+"\n"
            MetaLex.dicLog.manageLog.writelog(message)  
            
           
    def convert (self, img, show=False, save=False):
        """Convert image file to white/black image"""
        num = 1
        if len(self.images) >= 1 :
            for image in  self.images :
                img = Image.open(image)
                imagepart = dicProject.get_part_file(image)
                tempname = 'img_convert_'+str(num)+imagepart[1]
                if show : 
                    img.convert("L").show()
                if save :
                    dicProject.createtemp()
                    img.convert("L").save(tempname)
                    return tempname
                    
        else:
            message = '  > They are not images for the current treatment : input images!!' 
            print "--> "+message+"\n"
            MetaLex.dicLog.manageLog.writelog(message)
            
                  
                
    def filter (self, imgfilter, show=False):
        """Filter image file with specific filter value"""
        
        if len(self.images) >= 1 :
            num = 1
            for image in  self.images :
                img_conv = self.convert(image, save=True)
                img = Image.open(img_conv)
                imagename, ext = dicProject.get_part_file(image)
                tempname = 'img_filter_'+str(num)+ext
                dicProject.createtemp()
                if show :
                    img.filter(imgfilter).show()
                else :
                    img.filter(imgfilter).save(tempname)
                dicProject.treat_image_append(tempname)
                message = imagename + ' is modified with  filter (' +str(imgfilter)+ ')  > '+tempname+' > Saved in dicTemp folder'  
                MetaLex.dicLog.manageLog.writelog(message)
                img.close()
                num += 1
        else:
            message = '  > They are not images for the current treatment : input images!!' 
            print "--> "+message+"\n"
            MetaLex.dicLog.manageLog.writelog(message)
            
                    
                
    def removeColor(self, img, show=False, save=False):
        """Remove color in image file to enhance its quality"""
        
        if len(self.images) >= 1 :
            num = 1
            for image in  self.images :
                img = Image.open(image)
                imagepart = dicProject.get_part_file(image)
                tempname = 'img_color_remove_'+str(num)+imagepart[1]
                
                replace_color = (255, 255, 255)
                find_color = (0, 0, 0)
                new_image_data = []
                for color in list(img.getdata()) :
                    #print color
                    if color == find_color or color == replace_color :
                        #print color
                        new_image_data += [color]
                    else:
                        #print color
                        pass
                        
                img.putdata(new_image_data)
                if show :
                    img.show()
                if save :
                    dicProject.createtemp() 
                    img.save(tempname)   
                    return tempname
        else:
            message = '  > They are not images for the current treatment : input images!!' 
            print "--> "+message+"\n"
            MetaLex.dicLog.manageLog.writelog(message)
            
                    
