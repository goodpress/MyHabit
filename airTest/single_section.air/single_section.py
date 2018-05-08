# -*- encoding=utf8 -*-
__author__ = "wyk"

from airtest.core.api import *

auto_setup(__file__)

# -*- encoding=utf8 -*-
__author__ = "wyk"

from airtest.core.api import *

auto_setup(__file__)


def backToHomeTab():
    pluseIcon=exists(Template(r"tpl1525780162891.png", record_pos=(0.247, 0.692), resolution=(1080, 1920)))
    touchedNum=0;
    while pluseIcon == False:
        backIcon=exists(Template(r"tpl1525777345762.png", record_pos=(-0.431, -0.757), resolution=(1080, 1920)))
        if backIcon:
            touchedNum=touchedNum+1
            print "find back icon ,will touch ..." + str(touchedNum)
            touch(Template(r"tpl1525777345762.png", record_pos=(-0.431, -0.757), resolution=(1080, 1920)))
            sleep(1)
        cacelIcon=exists(Template(r"tpl1525777502214.png", record_pos=(-0.433, -0.753), resolution=(1080, 1920)))
        if cacelIcon:
            print "find cacelIcon ,will touch ..." + str(touchedNum)

            touch(Template(r"tpl1525777502214.png", record_pos=(-0.433, -0.753), resolution=(1080, 1920)))
            sleep(2)
            
            
        pluseIcon=exists(Template(r"tpl1525780162891.png", record_pos=(0.247, 0.692), resolution=(1080, 1920)))

            
    print " ok , had in home TAB "
    return;


def removeTmpAccountDialogue():
    backToHomeTab()
    received=exists(Template(r"tpl1525479334499.png", record_pos=(-0.38, -0.625), resolution=(1080.0, 1920.0)))


    if received:
        touch(Template(r"tpl1525479334499.png", record_pos=(-0.38, -0.625), resolution=(1080.0, 1920.0)),duration=1)
        touch(Template(r"tpl1525775694396.png", record_pos=(0.031, 0.532), resolution=(1080, 1920)))
        sleep(1)
        touch(Template(r"tpl1525775752939.png", record_pos=(0.255, 0.093), resolution=(1080, 1920)))
    else:
        print "WARN: not received ";
    return;

def openMainWX():
    keyevent("HOME")
    sleep(2)
    touch(Template(r"tpl1525452724649.png", record_pos=(0.422, 0.756), resolution=(1080.0, 1920.0)))
    sleep(4)
    return;
def cleanJunkAccount():
    touch(Template(r"tpl1525779377238.png", record_pos=(-0.126, 0.702), resolution=(1080, 1920)))
    sleep(2)
    
    touch(Template(r"tpl1525678744263.png", record_pos=(-0.328, -0.183), resolution=(1080, 1920)))
    sleep(2)

    cacellationBtn = exists(Template(r"tpl1525774549108.png", record_pos=(-0.154, -0.14), resolution=(1080, 1920)))
    while cacellationBtn:
        print "this account is cacellationBtn" + str(cacellationBtn[0]) + "," + str(cacellationBtn[1])
        touch(Template(r"tpl1525774549108.png", record_pos=(-0.154, -0.14), resolution=(1080, 1920)),duration=1)
    
        touch(Template(r"tpl1525773678520.png", record_pos=(0.216, -0.691), resolution=(1080, 1920)))
        sleep(1)

        touch(Template(r"tpl1525773711606.png", record_pos=(0.237, 0.093), resolution=(1080, 1920)))
        sleep(1)
        cacellationBtn = exists(Template(r"tpl1525774549108.png", record_pos=(-0.154, -0.14), resolution=(1080, 1920)))
    
    return;


 
def shareToSubAccount():
    cleanJunkAccount();
    
    touch(Template(r"tpl1525451310507.png", record_pos=(0.209, -0.613), resolution=(1080.0, 1920.0)))
    sleep(3)

    junkAccound=exists(Template(r"tpl1525773590239.png", record_pos=(-0.091, -0.749), resolution=(1080, 1920)))
    if junkAccound:
        touch(Template(r"tpl1525773638175.png", record_pos=(-0.427, -0.747), resolution=(1080, 1920)))
        touch(Template(r"tpl1525451310507.png", record_pos=(0.209, -0.613), resolution=(1080.0, 1920.0)),duration=1)
        sleep(1)
    
        touch(Template(r"tpl1525773678520.png", record_pos=(0.216, -0.691), resolution=(1080, 1920)))
        sleep(1)
    
        touch(Template(r"tpl1525773711606.png", record_pos=(0.237, 0.093), resolution=(1080, 1920)))
        sleep(1)
    
    

    



    touch(Template(r"tpl1525776327147.png", record_pos=(0.42, -0.742), resolution=(1080, 1920)))
    sleep(2)




    touch(Template(r"tpl1525451336035.png", record_pos=(0.425, -0.76), resolution=(1080.0, 1920.0)))
    sleep(2)



    touch(Template(r"tpl1525776362573.png", record_pos=(-0.323, 0.17), resolution=(1080, 1920)))
    sleep(2)




    touch(Template(r"tpl1525451347322.png", record_pos=(-0.414, -0.248), resolution=(1080.0, 1920.0)))
    sleep(2)
    
    touch(Template(r"tpl1525451353208.png", record_pos=(0.258, 0.295), resolution=(1080.0, 1920.0)))
    sleep(2)
    return;


        
def openSubAccount():
    keyevent("HOME")
    sleep(2)
    touch(Template(r"tpl1525776614728.png", record_pos=(0.163, -0.384), resolution=(1080, 1920)))
    sleep(6)
    return;

def fellow():
    received=exists(Template(r"tpl1525479334499.png", record_pos=(-0.38, -0.625), resolution=(1080.0, 1920.0)))
    if received:

        touch(Template(r"tpl1525479334499.png", record_pos=(-0.38, -0.625), resolution=(1080.0, 1920.0)))
        sleep(2)


        card=exists(Template(r"tpl1525775234003.png", record_pos=(-0.245, -0.37), resolution=(1080, 1920)))

        if card:
            touch(Template(r"tpl1525479652540.png", threshold=0.25, target_pos=5, rgb=False, record_pos=(-0.176, -0.354), resolution=(1080, 1920)))
            sleep(2)


            swipe(Template(r"tpl1525478687615.png", record_pos=(-0.388, -0.233), resolution=(1080.0, 1920.0)), vector=[-0.0374, -0.3572])
            sleep(2)

            fellow=exists(Template(r"tpl1525775342417.png", record_pos=(0.008, 0.608), resolution=(1080, 1920)))
            if fellow:
                touch(Template(r"tpl1525775342417.png", record_pos=(0.008, 0.608), resolution=(1080, 1920)))
                sleep(2)
        
        
                fellowOk = exists(Template(r"tpl1525775432609.png", record_pos=(0.415, -0.756), resolution=(1080, 1920)))
            
                if fellowOk :
                    # 返回子账号首页,删除消息.
                    backToHomeTab()
                    ########remove
            enterAccount=exists(Template(r"tpl1525776785000.png", record_pos=(-0.001, 0.688), resolution=(1080, 1920)))
            if enterAccount:
                # 返回子账号首页,删除消息.
                backToHomeTab()
            ########remove
    return;
def cancellationFellow():
    touch(Template(r"tpl1525451336035.png", record_pos=(0.425, -0.76), resolution=(1080.0, 1920.0)))
    sleep(2)

    
    touch(Template(r"tpl1525776476669.png", record_pos=(-0.341, 0.561), resolution=(1080, 1920)))
    sleep(1)


    touch(Template(r"tpl1525776497518.png", record_pos=(0.246, 0.102), resolution=(1080, 1920)))
    sleep(1)
    return;


        
#open main wx home tab
openMainWX()
backToHomeTab()
#share one account to sub count 
shareToSubAccount()
# open sub account 
openSubAccount()
# fellow 
fellow()
# remove sub account dialogue
removeTmpAccountDialogue();  
# open main account 
openMainWX()
# cancellation fellow
cancellationFellow()










