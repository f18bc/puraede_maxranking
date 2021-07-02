from tkinter import *
from tkinter import messagebox
from tkinter import ttk

window = Tk()

#タイトルの名前

window.title("Calculator for Puraede")

#Windowのサイズ

window.geometry('800x600')

#表示するコンテンツ

titlep = Label(window, text="プラエデ競技場ランキングを計算しましょう", font=("Arial Bold", 25))

titlep.grid(column=0, row=0)

result = Label(window, text="ここでランキングごとに理想値を表示する", font=("Arial Bold", 20))

result.grid(column=0, row=1)

input_rank = Entry(window,width=10)

input_rank .grid(column=0, row=2)

#計算のプロセスはここ
def clicked():

	if input_rank .get():
		x = int(input_rank .get())

		if x >= 20000:
			highest = 0.8 * 20000
		elif x >= 10000 and x < 20000:
			highest = 0.8 * x
		elif x >= 5000 and x < 10000:
			highest = 0.79 * x
		elif x >= 2000 and x < 5000:
			highest = 0.78 * x
		elif x >= 1000 and x < 2000:
			highest = 0.77 * x
		elif x >= 500 and x < 1000:
			highest = 0.76 * x
		elif x >= 200 and x < 500:
			highest = 0.75 * x
		elif x >= 50 and x < 200:
			highest = 0.74 * x
		elif x >= 20 and x < 50:
			highest = 0.73 * x
		elif x >= 15 and x < 20:
			highest = 0.72 * x
		elif x >= 10 and x < 15:
			highest = 0.6 * x
		elif x >= 5 and x < 10:
			highest = x - 4
		elif x>= 1 and x < 5:
			highest = 1
		else:
			lbl.configure(text="入力エラー")
			return 0

		if highest != int(highest):
			highest = int(highest) + 1

		if highest * 0.0005 == int(highest * 0.0005):
			goal = int(highest) + int(highest * 0.0005)
		else:
			goal = int(highest) + int(highest * 0.0005) + 1

		result.configure(text="可能な順位は" +str(int(highest)) + "位, " + str(goal) + "位以上を目指せ")


#入力なしの場合、メッセージボックスを表示

	else:
		messagebox.showinfo('警告','入力なし')

	input_rank.delete(0, 'end')

#表示するボタン 

btn = Button(window, text="計算", bg="orange", fg="red", command=clicked)

btn.grid(column=0, row=3)

#可能なアップデートに備え、FRAMEを構築する

StartWarnFrame=Frame(window, width=100, height =50)
StartWarnFrame.place(x=300,y=140)


#最初の時、デフォルト値及び理論値を提示する

StartWarnLabel1=Label(StartWarnFrame, text="注意事項：ランキングなしの場合では20000以上の任意数値を入れましょう").pack()
StartWarnLabel2=Label(StartWarnFrame, text="理想値は以下である\n（★は15回目終了を意味する）").pack()


bestversion = Scrollbar(StartWarnFrame)
bestversion.pack( side = LEFT, fill=Y)

desired_ranking_list = Listbox(StartWarnFrame, yscrollcommand = bestversion.set, height=15, width=30)

x = 20000
count = 1


while x > 2:
	if x >= 20000:
		desired_highest = 0.8 * 20000
	elif x >= 10000 and x < 20000:
		desired_highest = 0.8 * x
	elif x >= 5000 and x < 10000:
		desired_highest = 0.79 * x
	elif x >= 2000 and x < 5000:
		desired_highest = 0.78 * x
	elif x >= 1000 and x < 2000:
		desired_highest = 0.77 * x
	elif x >= 500 and x < 1000:
		desired_highest = 0.76 * x
	elif x >= 200 and x < 500:
		desired_highest = 0.75 * x
	elif x >= 50 and x < 200:
		desired_highest = 0.74 * x
	elif x >= 20 and x < 50:
		desired_highest = 0.73 * x
	elif x >= 15 and x < 20:
		desired_highest = 0.72 * x
	elif x >= 10 and x < 15:
		desired_highest = 0.6 * x
	elif x >= 5 and x < 10:
		desired_highest = x - 4
	elif x>= 1 and x < 5:
		desired_highest = 1

	if desired_highest == int(desired_highest):
		x = int(desired_highest)
	else:
		x = int(desired_highest) + 1

	if desired_highest * 0.0005 == int(desired_highest * 0.0005):
		desired_goal = int(desired_highest) + int(desired_highest * 0.0005)
	else:
		desired_goal = int(desired_highest) + int(desired_highest * 0.0005) + 1

	if count == 15:
		desired_ranking_list.insert(END, str(int(x)) + "位から" + str(desired_goal) + "位を目指せ ★")
		count = 0
	else:
		desired_ranking_list.insert(END, str(int(x)) + "位から" + str(desired_goal) + "位を目指せ")

	count += 1

desired_ranking_list.pack( side = LEFT, fill = BOTH )
bestversion.config( command = desired_ranking_list.yview )

StartWarnLabel3=Label(StartWarnFrame, text="最悪の状況は\n（52位以下は左に参照せよ）\n16815 13452\n10762 8610\n6802 5374\n4246 3312\n2584 2016\n1553 1196\n921 700\n532  ★\n405 304\n228 171\n127 94\n70 52").pack()


window.mainloop()

