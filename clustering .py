import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, davies_bouldin_score
from sklearn.decomposition import PCA
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

data = pd.read_csv("Seed_Data.csv")  # đọc dữ liệu
X = np.array(data.values) # lấy giá trị của các cột

max_ss = 0
max_dbs = 0
max_cluster = 0
for i in range (2,10):
    kmeans1 = KMeans(n_clusters=i,random_state=0).fit(X)
    ss_pca = silhouette_score(X,kmeans1.labels_)
    dbs_pca = davies_bouldin_score(X, kmeans1.labels_) # độ đo sự phù hợp
    if ss_pca > max_ss or dbs_pca > max_dbs:
        max_ss = ss_pca
        max_dbs = dbs_pca
        fitmodel = kmeans1
        max_cluster = i
print(fitmodel.n_clusters)

form = Tk()                                 # tạo form
form.title('Phân cụm hạt giống')            # tạo title
form.config(bg='#8DB1EB')                   # tạo màu background form
form.geometry('600x600')
grInfor = LabelFrame(form, text="Nhập thông tin hạt giống:", font=("Arial Bold", 10), fg="red", bg='#82E3EB')         # tạo group box Nhập thông tin hạt giống
grInfor.grid(row = 1, column = 0, padx= 70, pady= 50) # vị trí

lable_A = Label(grInfor, text = " A: ", bg='#82E3EB') #tạo lable A
lable_A.grid(row = 2, column = 1, padx = 20, pady = 10)# vị trí
textbox_A = Entry(grInfor)# tạo ô nhập thông tin
textbox_A.grid(row = 2, column = 2, padx= 20) # ví trí

lable_P = Label(grInfor, text = "P: ",bg='#82E3EB')
lable_P.grid(row = 3, column = 1, pady = 10)
textbox_P = Entry(grInfor)
textbox_P.grid(row = 3, column = 2)

lable_C = Label(grInfor, text = "C: ",bg='#82E3EB')
lable_C.grid(row = 4, column = 1,pady = 10)
textbox_C = Entry(grInfor)
textbox_C.grid(row = 4, column = 2)

lable_LK = Label(grInfor, text = "LK: ",bg='#82E3EB')
lable_LK.grid(row = 5, column = 1, pady = 10)
textbox_LK = Entry(grInfor)
textbox_LK.grid(row = 5, column = 2)

lable_WK = Label(grInfor, text = " WK: ", bg='#82E3EB')
lable_WK.grid(row = 2, column = 3, padx = 20, pady = 10)# vị trí
textbox_WK = Entry(grInfor)# tạo ô nhập thông tin
textbox_WK.grid(row = 2, column = 4, padx= 20) # ví trí

lable_A_Coef = Label(grInfor, text = "A_Coef: ",bg='#82E3EB')
lable_A_Coef.grid(row = 3, column = 3, pady = 10)
textbox_A_Coef = Entry(grInfor)
textbox_A_Coef.grid(row = 3, column = 4)

lable_LKG = Label(grInfor, text = "LKG: ",bg='#82E3EB')
lable_LKG.grid(row = 4, column = 3,pady = 10)
textbox_LKG = Entry(grInfor)
textbox_LKG.grid(row = 4, column = 4)

lblSoCum = Label(grInfor ,text= "Số cụm phù hợp nhất là: " + str(max_cluster), bg='#82E3EB')
lblSoCum.grid(row = 5, column = 4, pady = 10)

grPercentCluster = LabelFrame(form, text='Điểm độ đo của Cluster: ', bg='#EBA398') # tạo group box Mức độ phù hợp
grPercentCluster.grid(column=0, row=8, pady=5)   # vị trí
lbl1 = Label(grPercentCluster,text=""+'\n'
                           +"Điểm Silhouette: "+str(max_ss)+'\n'
                           +"Điểm Davies_bouldin: "+str(max_dbs)+'\n', bg='#EBC06A', padx=20) # tạo lable
lbl1.grid(column=0, row=0)
def dudoancluster():
    A = textbox_A.get()# lấy thông tin ở ô nhập
    P = textbox_P.get()
    C = textbox_C.get()
    Lk = textbox_LK.get()
    Wk = textbox_WK.get()
    A_Coef = textbox_A_Coef.get() 
    Lkg = textbox_LKG.get()
    if((A == '') or (P == '') or (C == '') or (Lk == '') or Wk == '' or A_Coef == '' or Lkg == ''): # nếu còn ô nào rỗng thì thông báo chưa nhập đủ thông tin
        messagebox.showinfo("Thông báo", "Bạn cần nhập đầy đủ thông tin!")
    else:
        X_dudoan = np.array([A, P, C, Lk, Wk, A_Coef, Lkg]).reshape(1, -1) # X_dudoan là mảng vừa nhập vào
        y_kqua = kmeans1.predict(X_dudoan) # dự đoán x_dudoan
        y1 = [] #tạo y1 rỗng
        if y_kqua == 0: #nếu y_kqua == 0   pca
            y1 = 'Kama' # y1 = Kama
        elif y_kqua == 1:
            y1 = 'Rosa'
        else:
            y1 = 'Canadian'
        lbl.configure(text= y1, bg='#75EBB3')# hiển thị dự đoán
groupCluster = LabelFrame(form, text = 'Dự đoán', bg='#75EBB3')#tạo group box Dự đoán theo clustering
groupCluster.grid(column=0, row=9, pady=10)
button_Cluster = Button(groupCluster, text = 'Hạt giống thuộc nước nào', command = dudoancluster, bg='#EBC06A')# tạo button dư đoán
button_Cluster.grid(row = 0, column = 1, pady = 20, padx=10)
lbl = Label(groupCluster, text="...", bg='#75EBB3')
lbl.grid(column=2, row=0, padx=50)

form.mainloop()
