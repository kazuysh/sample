import glob
import pandas as pd

matchPath = glob.glob('../jpg_data/*.jpg', recursive=True)
df=pd.DataFrame(matchPath,columns=['Path'])
df=df['Path'].str.split('/',expand=True)

df['Name']=df[2].str.replace('.jpg','')
df=df.set_index("Name")
df.drop(0,axis=1)

df.to_csv('FileList.csv')
