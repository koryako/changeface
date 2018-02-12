#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import numpy
import os
 
    
def get_image_paths( directory ):
    return [ x.path for x in os.scandir( directory ) if x.name.endswith(".jpg") or x.name.endswith(".png") ]

def load_images( image_paths, convert=None ):
    iter_all_images = ( cv2.imread(fn) for fn in image_paths )
    if convert:
        iter_all_images = ( convert(img) for img in iter_all_images )
    for i,image in enumerate( iter_all_images ):
        if i == 0:
            all_images = numpy.empty( ( len(image_paths), ) + image.shape, dtype=image.dtype )
        all_images[i] = image
    return all_images

def get_transpose_axes( n ):
    if n % 2 == 0:
        y_axes = list( range( 1, n-1, 2 ) )
        x_axes = list( range( 0, n-1, 2 ) )
    else:
        y_axes = list( range( 0, n-1, 2 ) )
        x_axes = list( range( 1, n-1, 2 ) )
    return y_axes, x_axes, [n-1]

def stack_images( images ):
    images_shape = numpy.array( images.shape )
    new_axes = get_transpose_axes( len( images_shape ) )
    new_shape = [ numpy.prod( images_shape[x] ) for x in new_axes ]
    return numpy.transpose(
        images,
        axes = numpy.concatenate( new_axes )
        ).reshape( new_shape )


def video2img(videoname,imgroot):
    #获得视频的格式    
    vc=cv2.VideoCapture(videoname)
    #cap = cv2.VideoCapture(0)
    #videoCapture = cv2.VideoCapture('oto.avi')  
    c=1
    
    #magnet:?xt=urn:btih:598F5888522C860D48629EB8EC267496B4322E70
  
    #获得码率及尺寸  
    fps = vc.get(cv2.cv.CV_CAP_PROP_FPS)  
    size = (int(vc.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),   
            int(vc.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))  
    print("fps:",fps)
    print("size:",size)
    """
    #w = cap.get(cv2.CAP_PROP_FRAME_WIDTH);
    #h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT); 
    if vc.isOpened():  
        rval,frame=vc.read()
    else:  
        rval=False 
    timeF = 1 #视频帧计数间隔频率 
    while rval:  
        rval,frame=vc.read()
        if(c%timeF == 0): #每隔timeF帧进行存储操作
            cv2.imwrite(imgroot+str(videoname).split('.')[0]+str(c)+'.jpg',frame)  
        c=c+1
        cv2.waitKey(1) 
    """ 
    vc.release()  
    
def img2video(img_root,name):
    
    #from cv2 import VideoWriter,VideoWriter_fourcc,imread,resize 
    
    #Edit each frame's appearing time!  
    fps=20
    #fourcc = cv2.cv.CV_FOURCC(*'XVID')
    fourcc = cv2.cv.CV_FOURCC(*'mp4v')
    #fourcc = cv2.cv.CV_FOURCC(*"MJPG")  
    #fourcc=VideoWriter_fourcc(*"MJPG")
    # fourcc = cv2.cv.CV_FOURCC('M', 'J', 'P', 'G')  
    videoWriter=cv2.VideoWriter(str(name)+".mp4",fourcc,fps,(368,640))  
  
    im_names=os.listdir(img_root)  
    for im_name in range(1,len(im_names)):
        frame=cv2.imread(img_root+str(im_name)+'.jpg')  
        print(im_name)
        #frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)  
        
        videoWriter.write(frame)  
      
    videoWriter.release()  


"""

    # -*- coding: utf-8 -*-  
  
#=================  
#File: PyOpenCV.py  
#Author: Wendy  
#Date: 2013-12-03  
#=================  
  
#eclipse, python2.7, opencv 2.4.6  
  
import cv2  
  

  
#指定写视频的格式, I420-avi, MJPG-mp4  
videoWriter = cv2.VideoWriter('oto_other.mp4', cv2.cv.CV_FOURCC('M', 'J', 'P', 'G'), fps, size)  
  
#读帧  
success, frame = videoCapture.read()  
  
while success :  
    cv2.imshow("Oto Video", frame) #显示  
    cv2.waitKey(1000/int(fps)) #延迟  
    videoWriter.write(frame) #写视频帧  
    success, frame = videoCapture.read() #获取下一帧  

    """

