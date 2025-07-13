
import os
import glob
import pandas as pd



#=============================================
# currentパス
#=============================================
current_dpath = os.getcwd()
#=============================================
# parentパス
#=============================================
parent_dpath =os.path.sep.join(current_dpath.split(os.path.sep)[:-1])

#=============================================
# Inputデータフォルダパス
#=============================================

INPUT_DNAME = "2_data"
input_dpath =os.path.sep.join([parent_dpath,INPUT_DNAME])

#=============================================
# 出力先のフォルダパス
#=============================================
OUTPUT_DNAME = "3_output"
output_dpath =os.path.sep.join([parent_dpath,OUTPUT_DNAME])

#=============================================
# 出力先のフォルダ　なければ作成
#=============================================
os.makedirs(output_dpath,exist_ok = True)

#=============================================
# 出力先のフォルダ内の　前回処理ファイルを削除
#=============================================
dir = output_dpath
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))




#=============================================
# ファイルリスト
#=============================================
csv_files = glob.glob(input_dpath + "/*.csv")

#=============================================
# 保存名
#=============================================
save_name = "結合.csv"

data_list=[]
for file in csv_files:
    data_list.append(pd.read_csv(file))

data_df = pd.concat(data_list,axis=0)
data_df.to_csv(output_dpath + "/" + save_name, encoding='cp932',index =False)




#=============================================
# 保存フォルダ開く
#=============================================
os.startfile(os.path.realpath(output_dpath) + "\\")


#=============================================
# 保存したファイル開く 
#=============================================
#os.startfile(os.path.realpath(output_dpath) + "\\" + save_name)






