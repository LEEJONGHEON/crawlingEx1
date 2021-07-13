from selenium import webdriver

driver = webdriver.Chrome() # 크롬 드라이버와 연결
driver.get("https://finance.naver.com/sise/sise_rise.nhn") # 크롤링할 주소

prices = []
rises = []
for i in range(2, 80):
    try:
        prices.append(driver.find_element_by_xpath('//*[@id="contentarea"]/div[3]/table[1]/tbody/tr['+str(i)+']/td[3]').text)
        rises.append(driver.find_element_by_xpath('//*[@id="contentarea"]/div[3]/table/tbody/tr['+str(i)+']/td[5]/span').text)
    except:
        continue
names = driver.find_elements_by_class_name("tltle") #이미지 태그를 이용하여 이미지 정보 가져오기
for price,name,rise in zip(prices,names,rises):
    print(f"종목 : {name.text} 가격 : {price} 상승률 : {rise}")


