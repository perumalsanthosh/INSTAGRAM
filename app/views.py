from django.shortcuts import render
from django.http import HttpResponse
import instaloader
ig=instaloader.Instaloader()

def index(request):
    if request.method=="POST":
        username=request.POST['email1']
        pass1=request.POST['pass']
        l1=[]
        a=ig.login(username,pass1)
        ig.download_profile(username,profile_pic_only=True)
        profile = instaloader.Profile.from_username(ig.context,username)
        followers=profile.get_followers()
        for i in followers:
            i=str(i)
            a=i.split(' ')
            l1.append(a[1])

        l2=[]
        myfollowing=profile.get_followees()
        for f in myfollowing:
            f=str(f)
            gf=f.split(' ')
            l2.append(gf[1])

        set0=set(l1)
        set1=set(l2)


        a=set1.difference(set0)
        c=list(a)
        b=set0.difference(set1)
        d=list(b)
        ad={"abc":l1,
        "a":username,
        "b":c,
        "h":d}
        return render(request,"main.html",ad)
    return render(request,"index.html")
