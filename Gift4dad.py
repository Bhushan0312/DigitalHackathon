from src.testproject.sdk.drivers import webdriver
import time

def launch_Amazon():
    app_activity='com.amazon.mShop.home.HomeActivity'
    app_package='in.amazon.mShop.android.shopping'
    android_dev={
        "appPackage":app_package,
        "appActivity": app_activity,
        "udid":"a793956c",
        "platformName":"Android",
    }
    driver=webdriver.Remote(desired_capabilities=android_dev, project_name='Amazon Best Deal', job_name='Finding best Deal')
    driver.report().disable_auto_test_reports(disabled=True)
    #driver.start_activity(app_package=app_package,app_activity=app_activity)
    time.sleep(4)
    driver.find_element_by_xpath("//android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout").click()
    time.sleep(1)
    in2 = input("send inputs to amazon:")
    in1=in2.split()
    driver.find_element_by_xpath("//android.widget.EditText").send_keys(in2)
    driver.report().test(name="Taken imputs from user",message="related to the text will select suggetions",passed=True)
    time.sleep(2)
    driver.find_element_by_xpath("//android.view.View/android.view.View[1]/android.view.View[1]/android.view.View[1]").click()
    driver.report().test(name="Select suggetion",passed=True)

    count=2
    el=True
    input1=[]
    time.sleep(3)
    while True:
        try:
            print("//android.view.View["+str(count)+"]/android.view.View[2]/android.view.View[1]")
            input1.append(driver.find_element_by_xpath("//android.view.View["+str(count)+"]/android.view.View[2]/android.view.View[1]").text)
            count+=1
            print(count)
            if el == True:
                start=count
                el=False
        except:
            if count <5:
                print('move')
                count+=1
            else:
                print("breaking script")
                break
    if count >2:
        driver.report().test(name="Detected the result list", message="found list to fine best deal",passed=True)
    else:
       pass
    numbers=[]
    for n,i in enumerate(input1):
        i=str(i)
        valid=i.split()
        print(valid)
        print(input1)
        for j in valid:
            for i in in1:
                if i ==j:
                    numbers.append(n+start)
                    break
    print(numbers)
    if len(numbers)>0:
        driver.report().test(name="check price of specific result", passed=True)
    price=[]
    time.sleep(1)
    for i in numbers:
        #try:
            price.append(driver.find_element_by_xpath("//android.view.View["+str(i)+"]/android.view.View[2]/android.widget.TextView[1]").text)
        #except:
            #driver.swipe(100, 900, 100, 150)
            #price.append(driver.find_element_by_xpath("//android.view.View["+str(i)+"]/android.view.View[2]/android.widget.TextView[1]").text)
    print(price)
    price.sort()
    for i in numbers:
        if str(price[0])==driver.find_element_by_xpath("//android.view.View["+str(i)+"]/android.view.View[2]/android.widget.TextView[1]").text :
            driver.find_element_by_xpath("//android.view.View["+str(i)+"]/android.view.View[2]/android.widget.TextView[1]").click()
            time.sleep(3)
            driver.swipe(100, 700, 100, 150)
            driver.swipe(100, 700, 100, 150)
            driver.swipe(100, 700, 100, 150)
            driver.swipe(100, 700, 100, 150)
            driver.find_element_by_xpath("//android.widget.Button").click()
            time.sleep(2)
            driver.find_element_by_xpath("//android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ImageView").click()
            driver.find_element_by_xpath("//android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ImageView").click()
            driver.report().test(name="add to cart best deal", passed=True)
            time.sleep(3)
            driver.report().test(name="title: "+driver.find_element_by_xpath("//android.view.View[2]/android.view.View[1]/android.view.View//android.widget.TextView").text,passed=True)
            driver.report().test(name=driver.find_element_by_xpath("//android.view.View[2]/android.widget.ListView/android.view.View[1]").text,passed=True)
            driver.report().test(name=driver.find_element_by_xpath("//android.view.View[2]//android.view.View[4]").text, passed=True)
            driver.report().test(name=driver.find_element_by_xpath("//android.view.View[2]//android.view.View[5]").text, passed=True)
            driver.report().test(name=driver.find_element_by_xpath("//android.widget.ListView/android.view.View[6]").text, passed=True)

        else:
            pass


    time.sleep(1)
    #driver.back()
    time.sleep(1)
    time.sleep(3)

launch_Amazon()