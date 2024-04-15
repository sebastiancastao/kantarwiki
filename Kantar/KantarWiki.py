

from dataclasses import dataclass
import os
from flask import Flask, render_template,request, redirect, url_for
import os
import openai







app= Flask(__name__, template_folder='templates')

picFolder= os.path.join('static','pics')
app.config['UPLOAD_FOLDER']=picFolder

@app.route('/', methods=['POST','GET'])

def home():
    
    
    

    pic1=os.path.join(app.config['UPLOAD_FOLDER'], 'kantar.PNG')
    if request.method== "POST":
        user=request.form["bq"].lower()
        if user=="football"or user=="college" or user=="espn" or user=="nfl"or user=="nfln" or user=="game"or user=="games"or user=="classics" or user=="classic"or user=="pre kick"or user=="gm"or user=="post gun":
         return render_template("football.html")
        
        elif user=="flag" or user=="flagged"or user=="flagging"or user=="flaged"or user=="flaging":
            return render_template("flagging.html")
        elif user=="time zones" or user=="time"or user=="times"or user=="zone"or user=="zones"or user=="region"or user=="regions"or user=="state" or user=="states":
            return render_template("timezones.html")
        elif user=="email" or user=="emailed" or user=="e-mail" or user=="e-mail" or user=="valid sports title" or user=="rate issues" or user=="quality reviews" or user=="announcement" or user=="announcements" or user=="anouncements"or user=="anouncement":
            return render_template("emailinfo.html")
        elif user=="spanish" or user=="hispanic" or user=="latino"or user=="azteca"or user=="azta"or user=="telemundo"or user=="tel"or user=="unimas"or user=="uma"or user=="univision"or user=="uni":
            return render_template("spanish.html")
        elif user=="car ads" or user=="car ad" or user=="car" or user=="ford escape" or user=="ford" or user=="ford dealer assn escape"or user=="dealer assn"or user=="denver ford dealer assn escape + northwest ford dealer assn espcape" or user=="denver ford dealer assn escape "or user=="northwest ford Dealer assn espcape" or user=="colorado ford dealer assn escape"or user=="local dealer"or user=="local dealer"or user=="ford local dealer"or user=="mccafferty ford local dealer"or user=="ford of dayton"or user=="bills auto enterprises":
            return render_template("carads.html")
        elif user=="promo"or user=="promos"or user=="call letters"or user=="call letter":
            return render_template("promos.html")
        elif user=="promo"or user=="news specials"or user=="news special"or user=="saturday morning"or user=="saturday morning network"or user=="children programming"or user=="children program"or user=="children programs"or user=="syndicated movies"or user=="specials list"or user=="special list"or user=="specials"or user=="special"or user=="plog"or user=="pacific log"or user=="pacific"or user=="lucky dog"or user=="henry ford’s innova"or user=="mission unstoppable"or user=="pet vet dream team"or user=="hope in the wild"or user=="best friends furever"or user=="all in with laila"or user=="champion within"or user=="earth odyssey/dylan"or user=="consumer 101"or user=="roots less traveled"or user=="vets saving pets"or user=="one team: power/spor"or user=="wild child":
            return render_template("snf.html")
        elif user=="missing time"or user=="mising time"or user=="missing"or user=="daily alert"or user=="gap"or user=="banner":
            return render_template("missingtime.html")
        elif user=="diapositivas"or user=="slides"or user=="introduction"or user=="editing"or user=="types of tv"or user=="ews"or user=="summary":
            return render_template("summary.html")
        
        elif user=="questionable apot airing in a religious show"or user=="questionable short show length"or user=="religious"or user=="religion" or user=="account deactivated"or user=="brand in program buy"or user=="commercial starts day"or user=="comment beyond end of day comment"or user=="comment breaks spot"or user=="comment must start day"or user=="different origins in same show"or user=="last record not end of day comment"or user=="origin invalid for show origin is unusual for show invalid origins"or user=="paid promo airing on same owner network"or user=="alerts editor that a promo is airing in the edit that does not agree with the network affiliate it is airing on"or user=="previous record not show"or user=="product invalid for market"or user=="product invalid for service specified by origin"or user=="questionable hispanic activity"or user=="questionable tv show name"or user=="review local newscast"or user=="review local newscast"or user=="recurring flip to unknown advertiser"or user=="show breaks pod"or user=="show length differs from network log"or user=="spot overlap"or user=="tv show invalid for service"or user=="missing a missing time comment"or user=="daily alert":
            return render_template("guidelines.html")  
        elif user=="market" or user=="station"or user=="broadcast date"or user=="local edit "or user=="network edit"or user=="pacific edit"or user=="cable network edit"or user=="cable network log"or user=="syndication edit"or user=="syndication log"or user=="hispanic edit"or user=="spot"or user=="brand spots"or user=="brand spot"or user=="non-paid promo"or user=="nonpaid promo"or user=="non paid promo"or user=="paid promo"or user=="psa"or user=="pod"or user=="recover log"or user=="total errors"or user=="error"or user=="spli screen editing"or user=="validate":
            return render_template("spotvocab.html")  
        else:
            return render_template('homespot.html',user_image= pic1)
    else:

     return render_template('homespot.html',user_image= pic1)

    


   

@app.route('/spotvocab')


def spotvocab():
    v1=os.path.join(app.config['UPLOAD_FOLDER'], 'vocab1.PNG')
    v2=os.path.join(app.config['UPLOAD_FOLDER'], 'vocab2.PNG')
    v3=os.path.join(app.config['UPLOAD_FOLDER'], 'vocab3.PNG')
    vews=os.path.join(app.config['UPLOAD_FOLDER'], 'vocabews.PNG')
    vf1=os.path.join(app.config['UPLOAD_FOLDER'], 'vocabflagging1.PNG')
    vf2=os.path.join(app.config['UPLOAD_FOLDER'], 'vocabflagging2.PNG')
    vh1=os.path.join(app.config['UPLOAD_FOLDER'], 'vocabhisp1.PNG')
    vh2=os.path.join(app.config['UPLOAD_FOLDER'], 'vocabhisp2.PNG')
    vn1=os.path.join(app.config['UPLOAD_FOLDER'], 'vocabnetwork1.PNG')
    vn2=os.path.join(app.config['UPLOAD_FOLDER'], 'vocabnetwork2.PNG')
    vs1=os.path.join(app.config['UPLOAD_FOLDER'], 'vocabsynd1.PNG')
    vs2=os.path.join(app.config['UPLOAD_FOLDER'], 'vocabsynd2.PNG')
    vq=os.path.join(app.config['UPLOAD_FOLDER'], 'vocabque.PNG')

    

    
    

    
    
    return render_template("spotvocab.html",vocab1=v1,vocab2=v2,vocab3=v3,vocabews=vews,vocabflagging1=vf1,vocabflagging=vf2, vocahisp1=vh1 ,vocabhisp2=vh2, vocabnetwork1=vn1 , vocabnetwork2=vn2, vocabsynd1=vs1 , vocabsynd2=vs2, vocabque=vq )#+


 
@app.route('/flagging')
    
def flagging():
    f1=os.path.join(app.config['UPLOAD_FOLDER'], 'flaging.PNG')
    f2=os.path.join(app.config['UPLOAD_FOLDER'], 'flaging2.PNG')
    idf=os.path.join(app.config['UPLOAD_FOLDER'], 'identflag.PNG')
    fn1=os.path.join(app.config['UPLOAD_FOLDER'], 'flagnet1.PNG')
    fn2=os.path.join(app.config['UPLOAD_FOLDER'], 'flagnet2.PNG')
    fne1=os.path.join(app.config['UPLOAD_FOLDER'], 'flagnetex1.PNG')
    fne2=os.path.join(app.config['UPLOAD_FOLDER'], 'flagnetex2.PNG')
    fnep1=os.path.join(app.config['UPLOAD_FOLDER'], 'flagnetex1p1.PNG')
    fnep2=os.path.join(app.config['UPLOAD_FOLDER'], 'flagnetex1p2.PNG')
    fs1=os.path.join(app.config['UPLOAD_FOLDER'], 'flagsynd1.PNG')
    fs2=os.path.join(app.config['UPLOAD_FOLDER'], 'flagsynd2.PNG')
    fse1=os.path.join(app.config['UPLOAD_FOLDER'], 'flagsyndex1.PNG')
    fse2=os.path.join(app.config['UPLOAD_FOLDER'], 'flagsyndex2.PNG')

    fsep1=os.path.join(app.config['UPLOAD_FOLDER'], 'flagsyndex1p1.PNG')
    fsep2=os.path.join(app.config['UPLOAD_FOLDER'], 'flagsyndex1p2.PNG')

    fh1=os.path.join(app.config['UPLOAD_FOLDER'], 'flaghisp1.PNG')
    fh2=os.path.join(app.config['UPLOAD_FOLDER'], 'flaghisp2.PNG')



    return render_template('flagging.html',flaging=f1,flaging2=f2,identflag=idf,flagnet1=fn1,flagnet2=fn2,flagnetex1=fne1, vflagnetex2=fne2 ,flagnetex1p1=fnep1, flagnetex1p2=fnep2 , flagsynd1=fs1, flagsynd2=fs2 , flagsyndex1=fse1, flagsyndex2=fse2,flagsyndex1p1=fsep1,flagsynd1ex1p2=fsep2,flaghisp1=fh1, flaghisp2=fh2)#+


@app.route('/timezones')
    
def timezones():
    t1=os.path.join(app.config['UPLOAD_FOLDER'], 'timezones1.PNG')
    t2=os.path.join(app.config['UPLOAD_FOLDER'], 'timezones2.PNG')
    t3=os.path.join(app.config['UPLOAD_FOLDER'], 'timezones3.PNG')
    t4=os.path.join(app.config['UPLOAD_FOLDER'], 'timezones4.PNG')

    return render_template('timezones.html',timezones1=t1,timezones2=t2,timezones3=t3,timezones4=t4)#+

@app.route('/emailinfo')
    
def emailinfo():
    e1=os.path.join(app.config['UPLOAD_FOLDER'], 'emailinfo1.PNG')
    e2=os.path.join(app.config['UPLOAD_FOLDER'], 'emailinfo2.PNG')
    e3=os.path.join(app.config['UPLOAD_FOLDER'], 'emailinfo3.PNG')
    e4=os.path.join(app.config['UPLOAD_FOLDER'], 'emailinfo4.PNG')
    es1=os.path.join(app.config['UPLOAD_FOLDER'], 'emailspecial1.PNG')
    es2=os.path.join(app.config['UPLOAD_FOLDER'], 'emailspecial2.PNG')
    esy1=os.path.join(app.config['UPLOAD_FOLDER'], 'emailinfosynd1.PNG')
    esy2=os.path.join(app.config['UPLOAD_FOLDER'], 'emailsynd2.PNG')
    esy3=os.path.join(app.config['UPLOAD_FOLDER'], 'emailinfosynd2.PNG')
    esy4=os.path.join(app.config['UPLOAD_FOLDER'], 'emailinfosynd3.PNG')
    esy5=os.path.join(app.config['UPLOAD_FOLDER'], 'emailinfosynd4.PNG')
    er=os.path.join(app.config['UPLOAD_FOLDER'], 'emailinforates.PNG')
    eqa=os.path.join(app.config['UPLOAD_FOLDER'], 'emailinfoqa.PNG')
    ese1=os.path.join(app.config['UPLOAD_FOLDER'], 'emailinfosear1.PNG')
    ese2=os.path.join(app.config['UPLOAD_FOLDER'], 'emailinfosear2.PNG')
    ese3=os.path.join(app.config['UPLOAD_FOLDER'], 'emailinfosear3.PNG')
    ese4=os.path.join(app.config['UPLOAD_FOLDER'], 'emailinfosear4.PNG')

    
    

    return render_template('emailinfo.html', emailinfo1=e1,emailinfo2=e2,emailinfo3=e3,emailinfo4=e4,emailspecial1=es1,emailspecial2=es2, emailinfosynd1=esy1 ,emailsynd2=esy2, emailinfosynd2=esy3,emailinfosynd3=esy4 , emailinfosynd4=esy5, emailinforates=er , emailinfoqa=eqa, emailinfosear1=ese1,emailinfosear2=ese2,emailinfosear3=ese3,emailinfosear4=ese4)#+

@app.route('/guidelines')
    
def guidelines():
    ga1=os.path.join(app.config['UPLOAD_FOLDER'], 'guide.PNG')
   


    return render_template('guidelines.html',guidelinesal1=ga1)


@app.route('/football')
    
def football():
    ft1=os.path.join(app.config['UPLOAD_FOLDER'], 'nfl1.png')
    ft2=os.path.join(app.config['UPLOAD_FOLDER'], 'nfl2.PNG')
    ft3=os.path.join(app.config['UPLOAD_FOLDER'], 'nfl3.PNG')
    ft4=os.path.join(app.config['UPLOAD_FOLDER'], 'nfl4.PNG')
    ft5=os.path.join(app.config['UPLOAD_FOLDER'], 'nfl5.PNG')
    
    return render_template('football.html',football1=ft1,football2=ft2,football3=ft3,football4=ft4,football5=ft5)#+


@app.route('/spanish')
    
def spanish():
   
    sp=os.path.join(app.config['UPLOAD_FOLDER'], 'spanish.PNG')
    
    
    return render_template('spanish.html',spanish=sp)


@app.route('/carads')
    
def carads():
    c1=os.path.join(app.config['UPLOAD_FOLDER'], 'carads1.PNG')
    c2=os.path.join(app.config['UPLOAD_FOLDER'], 'carads2.PNG')

    return render_template('carads.html',carads1=c1, carads2=c2)#+


@app.route('/promos')
    
def promos():
    p1=os.path.join(app.config['UPLOAD_FOLDER'], 'pguidelines1.PNG')
    p2=os.path.join(app.config['UPLOAD_FOLDER'], 'pguidelines2.PNG')
    p3=os.path.join(app.config['UPLOAD_FOLDER'], 'pguidelines3.PNG')


    return render_template('promos.html',pguidelines1=p1,pguidelines2=p2,pguidelines3=p3)#+


@app.route('/missingtime')
    
def missingtime():
   
    m1=os.path.join(app.config['UPLOAD_FOLDER'], 'MIT1.PNG')
    m2=os.path.join(app.config['UPLOAD_FOLDER'], 'MIT2.PNG')
    
    
    return render_template('missingtime.html',missingtime1=m1,missingtime2=m2)

@app.route('/snf')
    
def snf():
   
    snfe=os.path.join(app.config['UPLOAD_FOLDER'], 'snf.PNG')
    
    
    
    return render_template('snf.html',spec=snfe)

@app.route('/summary')
    
def summary():
    adint=os.path.join(app.config['UPLOAD_FOLDER'], 'adint.PNG')
    dorad=os.path.join(app.config['UPLOAD_FOLDER'], 'dorado.PNG')
    net=os.path.join(app.config['UPLOAD_FOLDER'], 'net.PNG')
    synd=os.path.join(app.config['UPLOAD_FOLDER'], 'synd.PNG')
    local=os.path.join(app.config['UPLOAD_FOLDER'], 'local.PNG')

    cable=os.path.join(app.config['UPLOAD_FOLDER'], 'cable.PNG')
    canadian=os.path.join(app.config['UPLOAD_FOLDER'], 'canada.PNG')
    hispanic=os.path.join(app.config['UPLOAD_FOLDER'], 'hispanic.PNG')
    usmap=os.path.join(app.config['UPLOAD_FOLDER'], 'usmap.PNG')
    edpro=os.path.join(app.config['UPLOAD_FOLDER'], 'edpro.PNG')
    marvel=os.path.join(app.config['UPLOAD_FOLDER'], 'marvel.PNG')
    marvel2=os.path.join(app.config['UPLOAD_FOLDER'], 'marvel2.PNG')
    marvel3=os.path.join(app.config['UPLOAD_FOLDER'], 'marvel3.PNG')
    env1=os.path.join(app.config['UPLOAD_FOLDER'], 'env1.PNG')
    env2=os.path.join(app.config['UPLOAD_FOLDER'], 'env2.PNG')
    env3=os.path.join(app.config['UPLOAD_FOLDER'], 'env3.PNG')
    env4=os.path.join(app.config['UPLOAD_FOLDER'], 'env4.PNG')
    env5=os.path.join(app.config['UPLOAD_FOLDER'], 'env5.PNG')
    env6=os.path.join(app.config['UPLOAD_FOLDER'], 'env6.PNG')
    f1=os.path.join(app.config['UPLOAD_FOLDER'], 'f1.PNG')
    f2=os.path.join(app.config['UPLOAD_FOLDER'], 'f2.PNG')
    f3=os.path.join(app.config['UPLOAD_FOLDER'], 'f3.PNG')
    f4=os.path.join(app.config['UPLOAD_FOLDER'], 'f4.PNG')
    f5=os.path.join(app.config['UPLOAD_FOLDER'], 'f5.PNG')
    f6=os.path.join(app.config['UPLOAD_FOLDER'], 'f6.PNG')
    f7=os.path.join(app.config['UPLOAD_FOLDER'], 'f7.PNG')
    f8=os.path.join(app.config['UPLOAD_FOLDER'], 'f8.PNG')
    f9=os.path.join(app.config['UPLOAD_FOLDER'], 'f9.PNG')
    e1=os.path.join(app.config['UPLOAD_FOLDER'], 'e1.PNG')
    e2=os.path.join(app.config['UPLOAD_FOLDER'], 'e2.PNG')
    e3=os.path.join(app.config['UPLOAD_FOLDER'], 'e3.PNG')
    e4=os.path.join(app.config['UPLOAD_FOLDER'], 'e4.PNG')
    e5=os.path.join(app.config['UPLOAD_FOLDER'], 'e5.PNG')
    e6=os.path.join(app.config['UPLOAD_FOLDER'], 'e6.PNG')
    e7=os.path.join(app.config['UPLOAD_FOLDER'], 'e7.PNG')
    e8=os.path.join(app.config['UPLOAD_FOLDER'], 'e8.PNG')
    e9=os.path.join(app.config['UPLOAD_FOLDER'], 'e9.PNG')
    e10=os.path.join(app.config['UPLOAD_FOLDER'], 'e10.PNG')
    e11=os.path.join(app.config['UPLOAD_FOLDER'], 'e11.PNG')
    e12=os.path.join(app.config['UPLOAD_FOLDER'], 'e12.PNG')
    pt=os.path.join(app.config['UPLOAD_FOLDER'], 'pt.PNG')
 

    
   
    
    
    
    
    return render_template('summary.html',adi=adint, dorado=dorad, net=net, synd=synd, local=local, cable=cable, canadian=canadian, hispanic=hispanic, usmap=usmap, edpro=edpro, marvel=marvel, marvel2=marvel2, marvel3=marvel3, env1=env1,env2=env2,env3=env3,env4=env4,env5=env5,env6=env6, f1=f1,f2=f2,f3=f3,f4=f4,f5=f5,f6=f6,f7=f7,f8=f8,f9=f9,e1=e1,e2=e2,e3=e3,e4=e4,e5=e5,e6=e6,e7=e7,e8=e8,e9=e9,e10=e10,e11=e11,e12=e12, pt=pt)


if __name__=='__main__':
    app.run(host='0.0.0.0')