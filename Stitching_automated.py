def stitchImgList(imgList, dir, outName):
    from PIL import Image
    import os
    # sorting the names 
    imgList.sort()

    print(imgList)
    maxx = -1
    minx = int(imgList[0][0])
    maxy = -1
    miny = int(imgList[0][2])

    #serching for the minimum & maximum index
    for i in imgList:
        if not os.path.isfile(f"{dir}/{i}"):
            imgList.remove(i)
            continue

        if(int(i[0])>maxx):
            maxx = int(i[0])
        if(int(i[0])<minx):
            minx = int(i[0])
        if(int(i[2])>maxy):
            maxy = int(i[2])
        if(int(i[2])<miny):
            miny = int(i[2])
    
    print(f"x  : {minx} - {maxx} || y : {miny} - {maxy}")


    # calculating vertical & horizonatal size
    tosearchx = minx
    tosearchy = miny

    xlen = 0
    ylen = 0


    imtemp = Image.open(f"{dir}/{imgList[0]}")
    w, h = imtemp.size
        
    xlen = (maxx-minx+1)*w
    ylen = (maxy-miny+1)*h
    

    final = Image.new("RGB", (ylen, xlen))

    for i in imgList:
        try:
            im = Image.open(f"{dir}/{i}")
            w, h = im.size
            posy = (int(i[0])-minx)*w
            posx = (int(i[2])-miny)*h
            print(f"{i} ==> x : {posx}\t| y : {posy}")
            final.paste(im, box=(posx, posy))
        except:
            print(f"{i} : Image Not Found")

        

    final.save(f"{outName}.jpg", "JPEG")


    print(f"Image Size : x size : {xlen}| y size : {ylen}")


# para1 : List of file names of images
# para2 : directory folder
# para3 : outputfileName

stitchImgList(["2x1.jpg", "2x2.jpg", "2x3.jpg", "2x20.jpg", "3x1.jpg", "3x2.jpg", "3x3.jpg" ,"3x4.jpg"], "OUT", "MYIMAGE")