import math

def check(img,xx,yy,h,step,y0,y1,y2,y3,y4,w):
    a = [0, 0, 0, 0, 0]
    y=0
    k=0
    while (yy<h):
        # print(yy,xx)
        if xx==w-1:
            if img[yy][xx-1]==0:
                xx=xx-1
                if yy==y:
                    a[k]=xx
                    y+=step
                    k+=1
                    if k==4:
                        y-=1
            else:
                xx=xx
                if yy==y:
                    a[k]=xx
                    y+=step
                    k+=1
                    if k==4:
                        y-=1
        elif xx==0:
            if img[yy][xx]==0:
                xx=xx
                if yy==y:
                    a[k]=xx
                    y+=step
                    k+=1
                    if k==4:
                        y-=1
            else:
                xx=xx+1
                if yy==y:
                    a[k]=xx
                    y+=step
                    k+=1
                    if k==4:
                        y-=1
        else:
            if img[yy][xx-1]==0:
                xx=xx-1
                if yy==y:
                    a[k]=xx
                    y+=step
                    k+=1
                    if k==4:
                        y-=1
            elif img[yy][xx]==0:
                xx=xx
                if yy==y:
                    a[k]=xx
                    y+=step
                    k+=1
                    if k==4:
                        y-=1
            else:
                xx=xx+1
                if yy==y:
                    a[k]=xx
                    y+=step
                    k+=1
                    if k==4:
                        y-=1
        yy += 1
    aa=1
    cc=0
    return aa,a


def angle(img,y0,y1,y2,y3,y4,xdef,ydef,w,h,step):
    i=0
    for j in range(w-1):
        if img[i][j]==0:
            x1=w
            xx=j
            yy=i
            aa,bb=check(img,xx,yy,h,step,y0,y1,y2,y3,y4,w)
            if aa==1:
                res=an(bb,y0,y1,y2,y3,y4,xdef,ydef,step)
                # print (res)
                return res
    return res

def an(bb,y0,y1,y2,y3,y4,xdef,ydef,step):
    # print("success")
    aa = [0, 0, 0, 0]
    vecdef=(y4,y0)
    vec1=(bb[3]-bb[4],y4-y3)
    # print(vec1)
    aa[0]=vec(vecdef,vec1)
    vec2=(bb[2]-bb[3],y3-y2)
    aa[1] =vec(vecdef,vec2)
    vec3=(bb[1]-bb[2],y2-y1)
    aa[2] =vec(vecdef,vec3)
    vec4=(bb[0]-bb[1],y1-y0)
    aa[3] =vec(vecdef,vec4)
    # print(vecdef)


    print(aa)
    return aa

def vec(vec1,vec2):
    a=vec1[0]*vec2[0]+vec1[1]*vec2[1]
    v1=math.sqrt(pow(vec1[0],2)+pow(vec1[1],2))
    v2=math.sqrt(pow(vec2[0],2)+pow(vec2[1],2))
    ans=a/(v1*v2)
    # print(int(math.degrees(ans)))
    a=int(math.degrees(ans))
    return a