from turtle import width
import streamlit as st
from PIL import Image


st.header('太宰ゼミ　興味探しアプリ')
st.title('うしおくん13号')

#興味探索
interest = st.radio(
    'Q. あなたは以下の分野で興味のあるものはありますか？',
    ('データ分析によるマーケティング', 'Webページ分析によるECの売上UP', 'SNSによる集客')
)

#データ分析
if interest == 'データ分析によるマーケティング':
    interest_data = st.radio(
    'Q. どれを使って分析したいですか？',
    ('手軽に可視化できるツール', '最初のハードルが高いが可能性が無限大のツール', 'マウスで分析できるツール')
    )

    #Tableau
    if interest_data == '手軽に可視化できるツール':
        if st.checkbox('← 判定結果を見る'):
            img = Image.open('ushio-img/1.png')
            st.image(img, caption='Tableau', use_column_width=True)

            #興味の度合いを調査
            level = st.slider('Q. Tableauにどのくらい興味がある？',  min_value=0, max_value=100, step=1, value=50)
            if level >= 50:
                img = Image.open('ushio-img/Tableau.png')
                st.image(img, caption='Tableau', use_column_width=True)
                link = '[Tableau インストール画面](https://www.tableau.com/ja-jp)'
                st.markdown(link, unsafe_allow_html=True)
                st.write('上記のリンクからTableauのインストールが可能です。')
                st.write('遊び感覚で触ってみてください！')
            else:
                st.write('他の分野もチェックしてみてはどうですか？')
    #Python
    elif interest_data == '最初のハードルが高いが可能性が無限大のツール':
        if st.checkbox('← 判定結果を見る'):
            img = Image.open('ushio-img/2.png')
            st.image(img, caption='Python', use_column_width=True)

            #興味の度合いを調査
            level = st.slider('Q. Pythonにどのくらい興味がある？',  min_value=0, max_value=100, step=1, value=50)
            if level >= 50:
                img = Image.open('ushio-img/progate.png')
                st.image(img, caption='Python', use_column_width=True)
                link = '[Progate Python入門](https://prog-8.com/courses/python)'
                st.markdown(link, unsafe_allow_html=True)
                st.write('上記のリンクからPythonのお試しが可能です。')
                st.write('遊び感覚で触ってみてください！')
            else:
                st.write('他の分野もチェックしてみてはどうですか？')
    #Modeler
    else:
        if st.checkbox('← 判定結果を見る'):
            img = Image.open('ushio-img/3.png')
            st.image(img, caption='Modeler', use_column_width=True)

            #興味の度合いを調査
            level = st.slider('Q. Modelerにどのくらい興味がある？',  min_value=0, max_value=100, step=1, value=50)
            if level >= 50:
                img = Image.open('ushio-img/Modeler.jpeg')
                st.image(img, caption='Modeler', use_column_width=True)
                link = '[Modeler インストール画面](https://www.ibm.com/jp-ja/products/spss-modeler)'
                st.markdown(link, unsafe_allow_html=True)
                st.write('上記のリンクからModelerのインストールが可能です。')
                st.write('遊び感覚で触ってみてください！')
            else:
                st.write('他の分野もチェックしてみてはどうですか？')

#Webサイト
elif interest == 'Webページ分析によるECの売上UP':
    interest_web = st.radio(
    'Q. どの分野で活躍したいですか？',
    ('ツールによるサイトの分析', 'ユーザーを誘導するスキル', '文字で目的を達成する')
    )
    
    #GA
    if interest_web == 'ツールによるサイトの分析':
        if st.checkbox('← 判定結果を見る'):
            img = Image.open('ushio-img/4.png')
            st.image(img, caption=' Google Analytics', use_column_width=True)

            #興味の度合いを調査
            level = st.slider('Q. Googleアナリティクスにどのくらい興味がある？',  min_value=0, max_value=100, step=1, value=50)
            if level >= 50:
                img = Image.open('ushio-img/ga.png')
                st.image(img, caption='Googleアナリティクス', use_column_width=True)
                link = '[Googleアナリティクス ログイン画面](https://analytics.google.com/analytics/web/?hl=ja#/)'
                st.markdown(link, unsafe_allow_html=True)
                st.write('上記のリンクからGoogleアナリティクスのログインが可能です。')
                st.write('遊び感覚で触ってみてください！')
            else:
                st.write('他の分野もチェックしてみてはどうですか？')

    #Webデザイン
    elif interest_web == 'ユーザーを誘導するスキル':
        if st.checkbox('← 判定結果を見る'):
            img = Image.open('ushio-img/5.png')
            st.image(img, caption='Webデザイン', use_column_width=True)

            #興味の度合いを調査
            level = st.slider('Q. Webデザインにどのくらい興味がある？',  min_value=0, max_value=100, step=1, value=50)
            if level >= 50:
                img = Image.open('ushio-img/webデザイン.png')
                st.image(img, caption='Webデザイン', use_column_width=True)
                link = '[「WEBデザインとは」を学べるサイトへ](https://www.sejuku.net/blog/96085)'
                st.markdown(link, unsafe_allow_html=True)
                st.write('上記のリンクから無料で「WEBデザインとは」を学ぶことが可能です。')
                st.write('遊び感覚で触ってみてください！')
            else:
                st.write('他の分野もチェックしてみてはどうですか？')

    #Webライティング
    else:
        if st.checkbox('← 判定結果を見る'):
            img = Image.open('ushio-img/6.png')
            st.image(img, caption='Webライティング', use_column_width=True)

            #興味の度合いを調査
            level = st.slider('Q. WEBライティングにどのくらい興味がある？',  min_value=0, max_value=100, step=1, value=50)
            if level >= 50:
                img = Image.open('ushio-img/webライティング.png')
                st.image(img, caption='WEBライティング', use_column_width=True)
                link = '[「WEBライティングとは」を学べるサイトへ](https://cakutama.com/blog/writingtechnique/writerschool.html)'
                st.markdown(link, unsafe_allow_html=True)
                st.write('上記のリンクから無料で「WEBライティングとは」を学ぶことが可能です。')
                st.write('遊び感覚で触ってみてください！')
            else:
                st.write('他の分野もチェックしてみてはどうですか？')


#SNS
else:
    interest_cm = st.radio(
    'Q. どの分野で活躍したいですか？',
    ('SNSによる認知の獲得', 'ユーザーを誘導するスキル', '文字で目的を達成する')
    )

    #SNSマーケ
    if interest_cm == 'SNSによる認知の獲得':
        if st.checkbox('← 判定結果を見る'):
            img = Image.open('ushio-img/7.png')
            st.image(img, caption='SNSマーケティング', use_column_width=True)

            #興味の度合いを調査
            level = st.slider('Q. SNSマーケティングにどのくらい興味がある？',  min_value=0, max_value=100, step=1, value=50)
            if level >= 50:
                img = Image.open('ushio-img/sns.png')
                st.image(img, caption='SNSマーケティング', use_column_width=True)
                link = '[「SNSマーケティングとは」を学べるサイトへ](https://liskul.com/sns-marketig-68530)'
                st.markdown(link, unsafe_allow_html=True)
                st.write('上記のリンクから無料で「SNSマーケティングとは」を学ぶことが可能です。')
                st.write('遊び感覚で触ってみてください！')
            else:
                st.write('他の分野もチェックしてみてはどうですか？')
    
    
    #Webデザイン
    elif interest_cm == 'ユーザーを誘導するスキル':
        if st.checkbox('← 判定結果を見る'):
            img = Image.open('ushio-img/5.png')
            st.image(img, caption='Webデザイン', use_column_width=True)

            #興味の度合いを調査
            level = st.slider('Q. Webデザインにどのくらい興味がある？',  min_value=0, max_value=100, step=1, value=50)
            if level >= 50:
                img = Image.open('ushio-img/webデザイン.png')
                st.image(img, caption='Webデザイン', use_column_width=True)
                link = '[「WEBデザインとは」を学べるサイトへ](https://www.sejuku.net/blog/96085)'
                st.markdown(link, unsafe_allow_html=True)
                st.write('上記のリンクから無料で「WEBデザインとは」を学ぶことが可能です。')
                st.write('遊び感覚で触ってみてください！')
            else:
                st.write('他の分野もチェックしてみてはどうですか？')
    
    #コピーライティング
    else:
        if st.checkbox('← 判定結果を見る'):
            img = Image.open('ushio-img/8.png')
            st.image(img, caption='コピーライティング', use_column_width=True)

            #興味の度合いを調査
            level = st.slider('Q. コピーライティングにどのくらい興味がある？',  min_value=0, max_value=100, step=1, value=50)
            if level >= 50:
                img = Image.open('ushio-img/copy.png')
                st.image(img, caption='コピーライティング', use_column_width=True)
                link = '[「コピーライティングとは」を学べるサイトへ](https://www.gentosha-mc.com/terms/copywriting/#:~:text=%E3%82%B3%E3%83%94%E3%83%BC%E3%83%A9%E3%82%A4%E3%83%86%E3%82%A3%E3%83%B3%E3%82%B0%E3%81%A8%E3%81%AF%E3%80%81%E4%B8%BB,%E5%BA%83%E5%91%8A%E6%96%87%E3%80%8D%E3%81%AE%E6%84%8F%E5%91%B3%E3%81%A7%E3%81%99%E3%80%82)'
                st.markdown(link, unsafe_allow_html=True)
                st.write('上記のリンクから無料で「コピーライティングとは」を学ぶことが可能です。')
                st.write('遊び感覚で触ってみてください！')
            else:
                st.write('他の分野もチェックしてみてはどうですか？')



#先輩表
#st.title('太宰ゼミ 先輩表(得意分野記載)')

#col1, col2, = st.columns(2)

#with col1:
    #st.write('3年生[13期生]')
    #st.header("樋口 瑠星")
    #st.image("https://static.streamlit.io/examples/dog.jpg")
    #st.header("光本 恵一郎")
    #st.image("https://static.streamlit.io/examples/dog.jpg")
    #st.header("重松 隼輔")
    #st.image("https://static.streamlit.io/examples/dog.jpg")
    #st.header("金丸 智央")
    #st.image("https://static.streamlit.io/examples/dog.jpg")

#with col2:
    #st.write('4年生[12期生]')
    #st.header("仁田原 良信")
    #st.image("https://static.streamlit.io/examples/dog.jpg")
    #st.header("藤岡 美咲")
    #st.image("https://static.streamlit.io/examples/dog.jpg")
    #st.header("口元 創太")
    #st.image("https://static.streamlit.io/examples/dog.jpg")
    #st.header("平原 萌々佳")
    #st.image("https://static.streamlit.io/examples/dog.jpg")