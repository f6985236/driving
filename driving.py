#先去github建立專案上傳（網頁重新整理），再存PY檔案到資料夾！
country = input('請問你是哪國人？')
age = input('請輸入年齡')
age = int(age)

if country == '台灣':#記得是雙等於／台灣要加引號
	 if  age >= 18 :  #這邊是雙重if (第二個框框)
	 	print('你可以考駕照')
	 else:
	 	print('你還不能考駕照')
