# Import Libraries
import pandas as pd

class Source:

    def show(caste,rank,branch,minority='none'):
            
        df1=pd.read_csv("C:\\Users\\ROSHAN YADAV\\Contacts\\Desktop\\WORK\\Dataset\\cutoff\\pred_open.csv")
        df2=pd.read_csv("C:\\Users\\ROSHAN YADAV\\Contacts\\Desktop\\WORK\\Dataset\\cutoff\\pred_tfws.csv")
        df3=pd.read_csv("C:\\Users\\ROSHAN YADAV\\Contacts\\Desktop\\WORK\\Dataset\\cutoff\\pred_obc.csv")
        df4=pd.read_csv("C:\\Users\\ROSHAN YADAV\\Contacts\\Desktop\\WORK\\Dataset\\cutoff\\pred_sc_st.csv")
        df5=pd.read_csv("C:\\Users\\ROSHAN YADAV\\Contacts\\Desktop\\WORK\\Dataset\\cutoff\\pred_minor.csv")
        dr=pd.read_csv("C:\\Users\\ROSHAN YADAV\\Contacts\\Desktop\\WORK\\Dataset\\cutoff\\rating.csv")

        g=[3209,3181,3199]
        h=[3176,3196]
        s=[3182,3185]
        m=[3183,3201]
        c=[3208,3204,3207,3197,3214]
            #OPEN
        if(caste=='General'):
                if(branch=='cs'):
                    l1=[int(df1.iloc[i]['College Code']) for i in range(0,31) if df1['CS'][i]>=rank]
                    l2=[i for i in dr['College Code'] for j in l1 if i==j]
                    return l2
                        
                elif(branch=='it'):
                    l1=[int(df1.iloc[i]['College Code']) for i in range(0,31) if df1['IT'][i]>=rank]
                    l2=[i for i in dr['College Code'] for j in l1 if i==j]
                    return l2
                    

                elif(branch=='me'):
                    l1=[int(df1.iloc[i]['College Code']) for i in range(0,31) if df1['ME'][i]>=rank]
                    l2=[i for i in dr['College Code'] for j in l1 if i==j]
                    return l2

                
                elif(branch=='ce'):
                    l1=[int(df1.iloc[i]['College Code']) for i in range(0,31) if df1['CE'][i]>=rank]
                    l2=[i for i in dr['College Code'] for j in l1 if i==j]
                    return l2
                
                elif(branch=='ch'):
                    l1=[int(df1.iloc[i]['College Code']) for i in range(0,31) if df1['CH'][i]>=rank]
                    l2=[i for i in dr['College Code'] for j in l1 if i==j]
                    return l2
                 
                elif(branch=='ee'):
                    l1=[int(df1.iloc[i]['College Code']) for i in range(0,31) if df1['EE'][i]>=rank]
                    l2=[i for i in dr['College Code'] for j in l1 if i==j]
                    return l2

        #TFWS

        elif(caste=='Tfws'):
                if(branch=='cs'):
                    l1=[int(df2.iloc[i]['College Code']) for i in range(0,31) if df2['CS'][i]>=rank]
                    l2=[i for i in dr['College Code'] for j in l1 if i==j]
                    return l2
                        
                elif(branch=='it'):
                    l1=[int(df2.iloc[i]['College Code']) for i in range(0,31) if df2['IT'][i]>=rank]
                    l2=[i for i in dr['College Code'] for j in l1 if i==j]
                    return l2
                
                elif(branch=='me'):
                    l1=[int(df2.iloc[i]['College Code']) for i in range(0,31) if df2['ME'][i]>=rank]
                    l2=[i for i in dr['College Code'] for j in l1 if i==j]
                    return l2
                
                elif(branch=='ce'):
                    l1=[int(df2.iloc[i]['College Code']) for i in range(0,31) if df2['CE'][i]>=rank]
                    l2=[i for i in dr['College Code'] for j in l1 if i==j]
                    return l2

                elif(branch=='ch'):
                    l1=[int(df2.iloc[i]['College Code']) for i in range(0,31) if df2['CH'][i]>=rank]
                    l2=[i for i in dr['College Code'] for j in l1 if i==j]
                    return l2
                
                elif(branch=='ee'):
                    l1=[int(df2.iloc[i]['College Code']) for i in range(0,31) if df2['EE'][i]>=rank]
                    l2=[i for i in dr['College Code'] for j in l1 if i==j]
                    return l2

        #OBC               

        elif(caste=='Obc'):
                if(branch=='cs'):
                    l1=[int(df3.iloc[i]['College Code']) for i in range(0,13) if df3['CS'][i]>=rank]
                    l2=[i for i in dr['College Code'] for j in l1 if i==j]
                    return l2
                        
                elif(branch=='it'):
                    l1=[int(df3.iloc[i]['College Code']) for i in range(0,13) if df3['IT'][i]>=rank]
                    l2=[i for i in dr['College Code'] for j in l1 if i==j]
                    return l2
                
                elif(branch=='me'):
                    l1=[int(df3.iloc[i]['College Code']) for i in range(0,13) if df3['ME'][i]>=rank]
                    l2=[i for i in dr['College Code'] for j in l1 if i==j]
                    return l2
                
                elif(branch=='ce'):
                    l1=[int(df3.iloc[i]['College Code']) for i in range(0,13) if df3['CE'][i]>=rank]
                    l2=[i for i in dr['College Code'] for j in l1 if i==j]
                    return l2

                elif(branch=='ch'):
                    l1=[int(df3.iloc[i]['College Code']) for i in range(0,13) if df3['CH'][i]>=rank]
                    l2=[i for i in dr['College Code'] for j in l1 if i==j]
                    return l2
                    
                elif(branch=='ee'):
                    l1=[int(df3.iloc[i]['College Code']) for i in range(0,13) if df3['EE'][i]>=rank]
                    l2=[i for i in dr['College Code'] for j in l1 if i==j]
                    return l2

        #SC-ST

        elif(caste=='Sc-St'):
                if(branch=='cs'):
                    l1=[int(df4.iloc[i]['College Code']) for i in range(0,13) if df4['CS'][i]>=rank]
                    l2=[i for i in dr['College Code'] for j in l1 if i==j]
                    return l2

                elif(branch=='it'):
                    l1=[int(df4.iloc[i]['College Code']) for i in range(0,13) if df4['IT'][i]>=rank]
                    l2=[i for i in dr['College Code'] for j in l1 if i==j]
                    return l2

                elif(branch=='me'):
                    l1=[int(df4.iloc[i]['College Code']) for i in range(0,13) if df4['ME'][i]>=rank]
                    l2=[i for i in dr['College Code'] for j in l1 if i==j]
                    return l2
                    
                elif(branch=='ce'):
                    l1=[int(df4.iloc[i]['College Code']) for i in range(0,13) if df4['CE'][i]>=rank]
                    l2=[i for i in dr['College Code'] for j in l1 if i==j]
                    return l2
                    
                elif(branch=='ch'):
                    l1=[int(df4.iloc[i]['College Code']) for i in range(0,13) if df4['CH'][i]>=rank]
                    l2=[i for i in dr['College Code'] for j in l1 if i==j]
                    return l2

                elif(branch=='ee'):
                    l1=[int(df4.iloc[i]['College Code']) for i in range(0,13) if df4['EE'][i]>=rank]
                    l2=[i for i in dr['College Code'] for j in l1 if i==j]
                    return l2

        #MINORITY
            
        elif(caste=='minor'):
                if(branch=='cs'):
                    l1=[int(df5.iloc[i]['College Code']) for i in range(0,17) if df5['CS'][i]>=rank]

                    if minority=='Hindi':
                        l1=[i for i in l1 if i in h]
                    elif minority=='Gujarati':
                        l1=[i for i in l1 if i in g]
                    elif minority=='Sindhi':
                        l1=[i for i in l1 if i in s]
                    elif minority=='Christian':
                        l1=[i for i in l1 if i in c]
                    elif minority=='Muslim':
                        l1=[i for i in l1 if i in m]
                        
                    l2=[i for i in dr['College Code'] for j in l1 if i==j]
                    return l2

                elif(branch=='it'):
                    l1=[int(df5.iloc[i]['College Code']) for i in range(0,17) if df5['IT'][i]>=rank]

                    
                    if minority=='Hindi':
                        l1=[i for i in l1 if i in h]
                    elif minority=='Gujarati':
                        l1=[i for i in l1 if i in g]
                    elif minority=='Sindhi':
                        l1=[i for i in l1 if i in s]
                    elif minority=='Christian':
                        l1=[i for i in l1 if i in c]
                    elif minority=='Muslim':
                        l1=[i for i in l1 if i in m]

                    l2=[i for i in dr['College Code'] for j in l1 if i==j]
                    return l2
                
                elif(branch=='me'):
                    l1=[int(df5.iloc[i]['College Code']) for i in range(0,17) if df5['ME'][i]>=rank]
                    
                    if minority=='Hindi':
                        l1=[i for i in l1 if i in h]
                    elif minority=='Gujarati':
                        l1=[i for i in l1 if i in g]
                    elif minority=='Sindhi':
                        l1=[i for i in l1 if i in s]
                    elif minority=='Christian':
                        l1=[i for i in l1 if i in c]
                    elif minority=='Muslim':
                        l1=[i for i in l1 if i in m]

                    l2=[i for i in dr['College Code'] for j in l1 if i==j]
                    return l2
                    
                elif(branch=='ce'):
                    l1=[int(df5.iloc[i]['College Code']) for i in range(0,17) if df5['CE'][i]>=rank]

                    
                    if minority=='Hindi':
                        l1=[i for i in l1 if i in h]
                    elif minority=='Gujarati':
                        l1=[i for i in l1 if i in g]
                    elif minority=='Sindhi':
                        l1=[i for i in l1 if i in s]
                    elif minority=='Christian':
                        l1=[i for i in l1 if i in c]
                    elif minority=='Muslim':
                        l1=[i for i in l1 if i in m]

                    l2=[i for i in dr['College Code'] for j in l1 if i==j]
                    return l2

                elif(branch=='ch'):
                    l1=[int(df5.iloc[i]['College Code']) for i in range(0,17) if df5['CH'][i]>=rank]

                    
                    if minority=='Hindi':
                        l1=[i for i in l1 if i in h]
                    elif minority=='Gujarati':
                        l1=[i for i in l1 if i in g]
                    elif minority=='Sindhi':
                        l1=[i for i in l1 if i in s]
                    elif minority=='Christian':
                        l1=[i for i in l1 if i in c]
                    elif minority=='Muslim':
                        l1=[i for i in l1 if i in m]

                    l2=[i for i in dr['College Code'] for j in l1 if i==j]
                    return l2

                elif(branch=='ee'):
                    l1=[int(df5.iloc[i]['College Code']) for i in range(0,17) if df5['EE'][i]>=rank]

                    
                    if minority=='Hindi':
                        l1=[i for i in l1 if i in h]
                    elif minority=='Gujarati':
                        l1=[i for i in l1 if i in g]
                    elif minority=='Sindhi':
                        l1=[i for i in l1 if i in s]
                    elif minority=='Christian':
                        l1=[i for i in l1 if i in c]
                    elif minority=='Muslim':
                        l1=[i for i in l1 if i in m]

                    l2=[i for i in dr['College Code'] for j in l1 if i==j]
                    return l2