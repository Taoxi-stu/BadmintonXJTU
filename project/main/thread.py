
import copy
import threading
from time import sleep
from PlayBadminton import *
import schedule
def MainBook():
    # def test():
    #     print('rtest')
    userInfo = userInfoRead()
    mode = 0
    start_time = "08:40:00" #08:40:00
    # start_time = (datetime.datetime.now() + datetime.timedelta(seconds=10)).strftime('%H:%M:%S') 
    if mode:
        sub_thread = []
        ydjd = YiDongJiaoDa(userInfo['username'],userInfo['pwd'],'41');
        ydjd.login()
        ydjd2 = copy.deepcopy(ydjd)
        ydjd2.platid = '42'
        for i in range(0,2):
            print("正在注册线程",2*i+1,'--------------')
            sub_thread.append( threading.Thread(target = bmt_for_thread,args=(ydjd,userInfo,mode,str(i)+'-1')) )
            # sub_thread.append( threading.Thread(target = bmt_for_thread,args=(ydjd2,userInfo,mode,str(i)+'-2')) )
            # sub_thread.append( threading.Thread(target = test) )
        schedule_break_flag = False
        def schedule_thread():
            global schedule_break_flag 
            schedule_break_flag= True
            for i in range(0,2):
                sub_thread[i].start()
                sleep(30)   
        schedule.every().day.at(start_time).do(schedule_thread)
        while not schedule_break_flag:
            schedule.run_pending()
            sleep(1)
    else:
        ydjd = YiDongJiaoDa(userInfo['username'],userInfo['pwd'],'41');
        ydjd.login()
        ydjd2 = copy.deepcopy(ydjd)
        ydjd2.platid = '42'
        schedule.every(30).seconds.do(bmt_for_thread,ydjd=ydjd,userInfo=userInfo,mode=mode,thread_id = '1-1')
        # schedule.every(120).seconds.do(bmt_for_thread,ydjd=ydjd2,userInfo=userInfo,mode=mode,thread_id = '1-2' )
        while 1:
            schedule.run_pending()
            sleep(1)
if __name__ == "__main__":
    MainBook()