from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import tkinter as tk
from tkinter import messagebox

options = Options()
Options.chrome_executable_path = "D:\極品的檔案\北科\程式設計二\python\003\chromedriver.exe"


def ClickOK(ClassNunber, CheckInTime, U_ID, U_Password):
    status = 0
    U_ClassNunber = ClassNunber.get()
    timeString = CheckInTime.get()
    nowTime = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())
    if (nowTime > timeString):
        messagebox.showinfo('錯誤', '您輸入的時間錯誤，請重新輸入!')
    else:
        messagebox.showinfo('設定完成', '時間到將為您點名')
        XPATH_class = f'//*[@id="content"]/div[1]/div[1]/div[2]/div[{U_ClassNunber + 1}]/div[2]/div[1]'
        while (status == 0):
            nowTime = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())
            print("現在時間：" + nowTime)
            if (nowTime == timeString):
                print("啟動點名程序")
                status = 1
                driver = webdriver.Chrome(options=options)
                driver.get("https://irs.zuvio.com.tw/irs/login")

                zuvio_email = driver.find_element(By.NAME, "email")
                zuvio_email.send_keys(f'{U_ID}@mail.shu.edu.tw')
                zuvio_login = driver.find_element(
                    By.CLASS_NAME, "submit-button")
                zuvio_login.click()

                SHU_email = driver.find_element(By.NAME, "txtMyId")
                SHU_password = driver.find_element(By.NAME, "txtMyPd")
                SHU_email.send_keys(U_ID)
                SHU_password.send_keys(U_Password)
                SHU_login = driver.find_element(By.NAME, "btnLogin")
                SHU_login.click()

                time.sleep(5.5)

                zuvio_EnterClass = driver.find_element(
                    By.XPATH, f'{XPATH_class}')
                zuvio_EnterClass.click()

                # 點選下排列的「點名簽到」
                zuvio_ClassCheckIn = driver.find_element(
                    By.XPATH, '//*[@id="footer"]/div/div[2]/div[1]')
                zuvio_ClassCheckIn.click()
                time.sleep(1)

                # 檢查按鈕是否存在
                try:
                    # 點名
                    zuvio_CheckIn = driver.find_element(
                        By.XPATH, '//*[@id="submit-make-rollcall"]')
                    zuvio_CheckIn.click()

                    # 確認點名
                    zuvio_CheckInOk = driver.find_element(
                        By.XPATH, '//*[@id="answer-finish-fcbx"]/div[4]/div')
                    zuvio_CheckInOk.click()

                    messagebox.showinfo('提醒', '簽到完成')
                    print("已成功簽到")
                    driver.quit()
                    break
                except:
                    print("\n注意：" + nowTime + " 老師尚未開放點名，一分鐘後將為您再次查看\n")
                    status = 0
                    timeString_List = list(timeString)
                    if (timeString_List[15] == '0'):
                        timeString_List[15] = '1'
                    elif (timeString_List[15] == '1'):
                        timeString_List[15] = '2'
                    elif (timeString_List[15] == '2'):
                        timeString_List[15] = '3'
                    elif (timeString_List[15] == '3'):
                        timeString_List[15] = '4'
                    elif (timeString_List[15] == '4'):
                        timeString_List[15] = '5'
                    elif (timeString_List[15] == '5'):
                        timeString_List[15] = '6'
                    elif (timeString_List[15] == '6'):
                        timeString_List[15] = '7'
                    elif (timeString_List[15] == '7'):
                        timeString_List[15] = '8'
                    elif (timeString_List[15] == '8'):
                        timeString_List[15] = '9'
                    elif (timeString_List[15] == '9'):
                        timeString_List[15] = '0'
                        if (timeString_List[14] == '0'):
                            timeString_List[14] = '1'
                        elif (timeString_List[14] == '1'):
                            timeString_List[14] = '2'
                        elif (timeString_List[14] == '2'):
                            timeString_List[14] = '3'
                        elif (timeString_List[14] == '3'):
                            timeString_List[14] = '4'
                        elif (timeString_List[14] == '4'):
                            timeString_List[14] = '5'
                        elif (timeString_List[14] == '5'):
                            timeString_List[14] = '0'
                            if (timeString_List[12] == '0'):
                                timeString_List[12] = '1'
                            elif (timeString_List[12] == '1'):
                                timeString_List[12] = '2'
                            elif (timeString_List[12] == '2'):
                                timeString_List[12] = '3'
                            elif (timeString_List[12] == '3'):
                                timeString_List[12] = '4'
                            elif (timeString_List[12] == '4'):
                                timeString_List[12] = '5'
                            elif (timeString_List[12] == '5'):
                                timeString_List[12] = '6'
                            elif (timeString_List[12] == '6'):
                                timeString_List[12] = '7'
                            elif (timeString_List[12] == '7'):
                                timeString_List[12] = '8'
                            elif (timeString_List[12] == '8'):
                                timeString_List[12] = '9'
                            elif (timeString_List[12] == '9'):
                                timeString_List[12] = '0'
                                timeString_List[11] = '1'
                    timeString = ''.join(timeString_List)
                    driver.quit()
            time.sleep(1)


def SearchClass():
    messagebox.showinfo('提醒', '將為您查詢課程!!')

    j = 0
    U_ID = ID.get()
    U_Password = Password.get()

    driver = webdriver.Chrome(options=options)
    driver.get("https://irs.zuvio.com.tw/irs/login")

    zuvio_email = driver.find_element(By.NAME, "email")
    zuvio_email.send_keys(f'{U_ID}@mail.shu.edu.tw')
    zuvio_login = driver.find_element(
        By.CLASS_NAME, "submit-button")
    zuvio_login.click()

    SHU_email = driver.find_element(By.NAME, "txtMyId")
    SHU_password = driver.find_element(By.NAME, "txtMyPd")
    SHU_email.send_keys(U_ID)
    SHU_password.send_keys(U_Password)
    SHU_login = driver.find_element(By.NAME, "btnLogin")
    SHU_login.click()

    time.sleep(5.5)

    if (driver.current_url != "https://irs.zuvio.com.tw/student5/irs/index"):
        driver.close()
        messagebox.showinfo('警告', '登入失敗，請再次登入')
    else:
        OUTPUT = ""
        ClassList = driver.find_elements(
            By.CLASS_NAME, "i-m-p-c-a-c-l-c-b-t-course-name")
        for i in ClassList:
            print(f"{j}. " + i.text + "\n")
            j += 1
        j = 0
        for i in ClassList:
            OUTPUT += f"{j}. " + i.text + "\n"
            j += 1
        label_ClassList.config(text=OUTPUT)

        # 選擇課程
        label_CheckInTime = tk.Label(win, text='請輸入需點名課程編號：', font='標楷體, 15')
        label_CheckInTime.place(x=320, y=180)
        txt_CheckInTime = tk.Entry(win, width=25, textvariable=ClassNunber)
        txt_CheckInTime.place(x=328, y=220)

        # 點名時間
        label_CheckInTime = tk.Label(win, text='請輸入點名時間：', font='標楷體, 15')
        label_CheckInTime.place(x=320, y=260)
        txt_CheckInTime = tk.Entry(win, width=25, textvariable=CheckInTime)
        txt_CheckInTime.place(x=328, y=300)
        label_CheckInTime = tk.Label(
            win, text='(ex.2022/12/03 15:42:00)', padx=10, pady=8, font='標楷體, 10')
        label_CheckInTime.place(x=330, y=320)

        # OK button
        button_Ok = tk.Button(win, text='確認', width=12,
                              command=lambda: ClickOK(ClassNunber, CheckInTime, U_ID, U_Password))
        button_Ok.place(x=240, y=370)
        win.geometry('560x420')


win = tk.Tk()
win.title('zuvio自動點名系統_世新大學')
win.geometry('560x180')

CheckInTime = tk.StringVar()
ID = tk.StringVar()
Password = tk.StringVar()
ClassNunber = tk.IntVar()

# 帳號
label_ID = tk.Label(win, text='請輸入帳號：', padx=10, pady=8, font='標楷體, 15')
label_ID.place(x=100, y=30)
txt_ID = tk.Entry(win, width=25, textvariable=ID)
txt_ID.place(x=240, y=40)

# 密碼
label_Password = tk.Label(win, text='請輸入密碼：', padx=10, pady=8, font='標楷體, 15')
label_Password.place(x=100, y=60)
txt_Password = tk.Entry(win, width=25, textvariable=Password)
txt_Password.place(x=240, y=70)

# Search Class button
button_SearchClass = tk.Button(
    win, text='查詢課程', width=12, command=SearchClass)
button_SearchClass.place(x=150, y=120)

# Exit button
button_Exit = tk.Button(win, text='離開', width=12, command=win.quit)
button_Exit.place(x=330, y=120)

# ClassListLabel
label_ClassList = tk.Label(win, text='', justify='left')
label_ClassList.place(x=10, y=180)

win.mainloop()
