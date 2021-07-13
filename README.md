# crawlingEx1
사용 기술 : Python Selenium
필요 파일 : chromedriver.exe
driver.get("크롤링하고싶은 url주소")

# 크롤링한 데이터 저장할 변수
prices = [] # 가격
rises = [] # 상승률

# 크롤링 방법에는 여러가지가있는데 prices와 rises 태그같은경우 중복되는 
rises = driver.find_elements_by_class_name("tah p11 red01") # 상승률 같은경우 해당태그로 크롤링하게되면 크롤링 되지않음

그래서 가격와 증가율은 xpath를 이용하여 매번 새롭게 태그를 할당해서 데이터를 추출함
for i in range(2, 80):
    try:
        prices.append(driver.find_element_by_xpath('//*[@id="contentarea"]/div[3]/table[1]/tbody/tr['+str(i)+']/td[3]').text)
        rises.append(driver.find_element_by_xpath('//*[@id="contentarea"]/div[3]/table/tbody/tr['+str(i)+']/td[5]/span').text)
    except:
        continue
