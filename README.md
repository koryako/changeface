
**环境:**

    Python 3
    Opencv 3
    Tensorflow 1.3+(?)
    Keras 2
* GIF Animator (GIFAnimator-Setup)

https://www.deepfakes.club/tutorial/


**训练数据和已经训练好的模型 (~300MB):**  
anonfile.com/p7w3m0d5be/face-swap.zip or [click here to download](anonfile.com/p7w3m0d5be/face-swap.zip)


conda install pip
pip install tensorflow-gpu dlib opencv-python keras scipy numpy h5py matplotlib tqdm scikit-image
conda install -c peterjc123 pytorch cuda80

# 以下是详细的配置要求

## 在 RussellCloud 平台上实现快速复现
在[RussellCloud](http://russellcloud.com)上新建名为`faceswap`的项目，选择默认容器环境`tensorflow-1.4`

```
git clone git@github.com:RussellCloud/deepfakes_faceswap.git
cd deepfakes_faceswap
russell init --name faceswap
russell run --data f3fadfadf6ac417e9f20813603187344:data "python run.py"
```	

约一分钟左右,就可以在该项目的网页端检查输出. 
(if the pip doenst work, download the wheel, pick based on your system and python, then run `pip install whatever_the-name-is.whl` in the directory of the wheel downloaded)

----------------------------------

**intro**

* get ready
* open code.txt in \face-swap
* run cmd, `cd [FACE-SWAP DIRECTORY HERE]`
* run in cmd, `activate tensorflow` and `python train.py`
* wait for several hours, stop the training by clicking on the faces window (not X), and then press Q.
* exit the cmd

----------------------------------

**get the data!**

* collect tons of images of target (200+)
* gather the images in a new folder, and rename as *target*, and copy to `\face-alignment-master`

* find the video that satisfies your imagination (POV view recommended)
* convert the video to jpg by using FFMPEG or any video software
* to convert, read the code.txt in bin directory in FFMPEG folder
* run cmd, 

    `cd [BIN DIRECTORY INSIDE OF FFMPEG HERE]`
        `ffmpeg -i file.mp4 -r 1/1 $filename%d.jpg` 
(change *file.mp4* to your video name with its extensions, and *$filename%d.jpg* to any name eg *riley%d.jpg*)

* copy the jpgs to a new folder, rename to *source*, and copy to `\face-alignment-master`

----------------------------------

**i'm ready!**

before do anything:

     pip install -r requirements.txt
     python setup.py install

* align both *target* and *source* images, to get aligned, cropped faces:

    `python align_images.py target`
    `python align_images.py source`
    
* open *target* and *source* folder, take a look at the *aligned* folder in both folder
* remove unwanted images. rename folder to *targetA* and *sourceA*. copy **aligned** folder in both *target* and *source* to `\face-swap\data`
* rename *cage* and *trump* to *cageA* and *trumpA*, and rename *targetA* and *sourceA* to *cage* and *trump*

* after done, copy *align_images.py*, *merge_faces.py*, *umeyama.py*, *source* folder to `\face-swap`

----------------------------------

**lets train!**

* run the same code for training, `activate tensorflow` and `python train.py`
* after it done, new *output* folder can be access
* have a look of the training data. if satisfied, proceed
* run cmd `python merge_faces_masked.py source`
* a new *aligned* folder can be access in *source* folder
* take a look at the merged faces

----------------------------------

**but, no gif?**

from the *merged* folder,
* go to GIFMaker , to convert jpg to gif. (it easier!)
* you can also use the install GIF Animator to make GIF
* DONE

----------------------------------

**kinda bored. need some audio!**

use FFMPEG, to convert gif to video

    ffmpeg -i try.gif -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" try.mp4

use any video software

* add the source video (video + audio)
* add the final deepfake video
* align it correctly to the time/frames of the source video
* delete the source video
* render and voilà, now you have a new fake video with sound!




