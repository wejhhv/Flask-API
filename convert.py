#漢数字、数字の桁、特定の桁（桁がつかない部分は空白としている）
Num=["零","壱","弐","参","四","五","六","七","八","九"]

Digit1_kanji =["","拾","百","千"]
Digit1_number =[1,10,100,1000]

Digit2_kanji =["","万","億","兆"]
Digit2_number=[1,10000,100000000,1000000000000]

#アラビア数字を漢数字に変換
def NumberToKanji(Number):
        
    #逆順で処理
    lis=Number[::-1]

    #変換できない値の処理　
    if Number.isdigit()==False or int(Number)<0 or len(Number)>16:
        return False,Number
    
    else:
        
        #順番に文字列を格納
        Str=""
        for i in range(len(lis)) :
            
            #特定の桁の処理
            if i%4==0:
                Str=Digit2_kanji[int(i/4)]+Str
            
            #0以外の桁と数字の処理
            if lis[i]!="0":
                
                Str=Digit1_kanji[i%4%4]+Str
                Str=Num[int(lis[i])]+Str
            
            #0のみであるときの処理
            if lis[i]=="0" and len(lis)==1:
                Str=Num[int(lis[i])]+Str

    #0が特定の桁をまたいで連続する時の処理　
    if "兆億万" in Str: 
        Str=Str.replace('億万', '')
    
    elif "兆万" in Str: 
        Str=Str.replace('万', '')
    
    elif "兆億" in Str: 
        Str=Str.replace('億', '')
        
    elif "億万" in Str: 
        Str=Str.replace("万", "")
    
    return True,Str


#漢数字をアラビア数字に変換
def KanjiToNumber(Kanji):
    
    Kanji=str(Kanji)
    
    #最終結果
    cal=0
    
    #前回の処理を記憶する
    mel=0
    
    #各種一時変数
    tmp=0
    tmp1=0
    tmp2=0
    tmp3=0
    
    for i in Kanji:
        
        #数字の処理
        if i in Num:
            tmp1=Num.index(i)
            mel=0

        #桁の処理
        elif i in Digit1_kanji:
            tmp2=Digit1_number[Digit1_kanji.index(i)]
            tmp+=tmp1*tmp2
            tmp1=0
            mel=1

        #特定の桁の処理    
        elif i in Digit2_kanji:
            tmp3=Digit2_number[Digit2_kanji.index(i)]
            
            #桁の処理を行わず、特定の桁の処理
            if tmp==0:
                cal+=tmp1*tmp3
                
            #通常の特定の桁の処理
            elif mel==0:
                tmp+=tmp1
                cal+=tmp*tmp3
                tmp=0
            
            else:
                cal+=tmp*tmp3
                tmp=0
        
        #特定の漢字以外の漢字が来た時の処理
        else:
            return False,Kanji
    

    #千以下は足されていないので、ここで処理
    if len(Kanji)<=3 and Kanji[-1]!="兆" and  Kanji[-1]!="億" and Kanji[-1]!="万":
        if tmp1!=0:
            cal+=tmp+tmp1
        
        else:
            cal+=tmp
    
    elif Kanji[-1]=="兆" or  Kanji[-1]=="億" or Kanji[-1]=="万":
        cal+=tmp
    
    else :
        
        cal+=tmp+tmp1
    
    return True,cal


