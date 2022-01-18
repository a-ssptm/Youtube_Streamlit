import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image#画像を表示
import time

st.title('Streamlit 超入門') #タイトルの表示

st.write('DataFrame')#テキストの表示
'テキストの表示'

#データフレームの作成と表示
#df= pd.DataFrame({
#    '1列目':[ 1, 2, 3, 4],
#    '2列目':[ 10, 20, 30, 40],
#})
#st.write(df) #簡単だが引数は指定できない
#st.dataframe(df) #動的な表を表示させたいときに使う、画面上でソートと全体表示が可能
#st.dataframe(df, width=100, height=100) #表の縦横の長さをピクセル単位で指定可能

#st.dataframe(df.style.highlight_max(axis=0)) #列の中で最大なものをハイライトする
#st.dataframe(df.style.highlight_max(axis=1)) #行の中で最大なものをハイライトする
#st.table(df.style.highlight_max(axis=0)) #静的な表を表示させたいときに使う、画面上でのソートなどができない

#マジックコマンドでテキストを表示
"""
# 章
## 節
### 項

```python #pythonコードを表示できる
import streamlit as st
import numpy as np
import pandas as pd
```

"""

#チャートを描く　折れ線グラフ
df= pd.DataFrame(#EX縦に20横に3つの乱数を生成した
    np.random.rand(20,3),
    columns=['a','b','c']
)
#st.table(df)
#st.line_chart(df)#折れ線グラフでプロットする
#st.area_chart(df)#エリアチャートでプロットする
#st.bar_chart(df)#棒グラフでプロットする

#マップをプロットする
data=[[35.17,136.90],[35.15,136.87]]
df= pd.DataFrame(data,columns=['lat','lon'])#日本語の緯度経度だと作成できなかった
st.table(df)
st.map(df)

#画像を表示させる
img = Image.open('D:\移行フォルダ\python\YURI.png')#''内に格納場所、プログラムと同じ階層ならファイル名のみでおけ
st.image(img, caption = 'YURI', use_column_width = True)#use_column_width実際のレイアウトの横幅に合わせて表示

#####インタラクティブなウィジェットを表示させる####

#チェックボックス
if st.checkbox('画像を表示させたいならチェックして下さい'):#チェックが入っているとTRUEで画像表示
    img = Image.open('D:\移行フォルダ\python\YURI.png')
    st.image(img, caption = 'YURI', use_column_width = True)

#セレクトボックス
options = st.selectbox(
    '1～10で好きな数字は？',
    list(range(1,11))#リスト
)
'あなたの好きな数字は', options,'です。'

#テキストを入力させ表示する
text_1 = st.text_input('あなたの趣味は？')
'あなたの趣味:',text_1

#スライダー
condition = st.slider('今のコンディションは？',0,100,50) #最大値、最小値、デフォ 
'コンディション:',condition

######レイアウトを整える#####

#サイドバー
#text_2 = st.sidebar.text_input('好きな食べ物は？')
#condition_1 = st.sidebar.slider('今の気分は？',0,10,5)
#st.write('サイドバーで入力してね')
#'好きな食べ物:',text_2
#'コンディション:',condition_1


#2カラムレイアウト
left_column,right_column = st.columns(2)#2カラムレイアウトにした
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')
    
#エキスパンダーの追加(クリックすると詳しく表示させるQandAみたいなやつ)
expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1の回答はこちら')

expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答はこちら')

#プログレスバーの表示
'Start!!'

latest_iteration = st.empty()#空の要素を生成
bar = st.progress(0)#0から100か、0.0から1.0なのか

for i in range(100):
    latest_iteration.text(f'Iteration {i+1} ')
    bar.progress(i+1)
    time.sleep(0.1)
'Dooooone!'#100まで表示された後に表示される