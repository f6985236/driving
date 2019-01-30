#先去github建立專案上傳（網頁重新整理），再存PY檔案到資料夾！
country = input('請問你是哪國人？')
age = input('請輸入年齡')
age = int(age)

if country == '台灣':#記得是雙等於／台灣要加引號
	 if  age >= 18 :  #這邊是雙重if (第二個框框)
	 	print('你可以考駕照')
	 else:
	 	print('你還不能考駕照')

	 #在終端機加入台灣的版本 git add driving.py/ git commit -m'add taiwan'/
	 # git push oringin master  完成上傳重新整理網頁
#接著加入美國，年齡大於16就可以開車
#用elif
elif country =='美國':
	if age >= 16:
		print('你可以開車')
	else :
		print('不能開')
#那要如何告訴使用者，只能輸入台灣或美國？
#分第三路
else :
	print('你只能輸入 台灣／美國')