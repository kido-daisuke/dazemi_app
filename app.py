#import tkinter as tk
import streamlit as st
#from turtle import width
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

interest_now = st.text_input('以上の「興味探しの中で」今最も興味のある分野は何ですか？')

st.write('上に[ Tableau , Python , Modeler , Googleアナリティクス , Webデザイン , Webライティング , SNSマーケティング , コピーライティング ]のどれかを[]内の表記通りに記入しよう！')

if interest_now == 'Tableau':
    expander = st.expander("この先輩方に聞いて見ると良いかもです！")
    expander.write("""
        仁田原 良信(4年)、諸富 樹(3年)、外宮 拓実(3年)、樋口 瑠星(3年)、外宮 拓実(3年)、福永 匠(3年)、前崎 彩乃(3年)、金丸 智央(3年)、武石 瑛(3年)、上田 さくら(3年)
    """)
elif interest_now == 'Python':
    expander = st.expander("この先輩方に聞いて見ると良いかもです！")
    expander.write("""
        重松 隼輔(3年)、外宮 拓実(3年)、武石 瑛(3年)、木戸 大輔(3年)
    """)
elif interest_now == 'Modeler':
    expander = st.expander("この先輩方に聞いて見ると良いかもです！")
    expander.write("""
        太宰 潮(教授)、外宮 拓実(3年)、金丸 智央(3年)、武石 瑛(3年)、上田 さくら(3年)、木戸 大輔(3年)
    """)
elif interest_now == 'Googleアナリティクス':
    expander = st.expander("この先輩方に聞いて見ると良いかもです！")
    expander.write("""
        樋口 瑠星(3年)、原田 佳奈(3年)、宮崎 かほ(3年)、上田 さくら(3年)、光本 恵一郎(3年)、木戸 大輔(3年)
    """)
elif interest_now == 'Webデザイン':
    expander = st.expander("この先輩方に聞いて見ると良いかもです！")
    expander.write("""
        上田 さくら(3年)、木戸 大輔(3年)
    """)
elif interest_now == 'Webライティング':
    expander = st.expander("この先輩方に聞いて見ると良いかもです！")
    expander.write("""
        木戸 大輔(3年)
    """)
elif interest_now == 'SNSマーケティング':
    expander = st.expander("この先輩方に聞いて見ると良いかもです！")
    expander.write("""
        光本 恵一朗(3年)、木戸 大輔(3年)
    """)
elif interest_now == '七並べ':
    expander = st.expander("この先輩方に聞いて見ると良いかもです！")
    expander.write("""
        堀 薫(3年)
    """)
else :
    expander = st.expander("この先輩方に聞いて見ると良いかもです！")
    expander.write("""
        原田 佳奈(3年)、木戸 大輔(3年)
    """)

#先輩スキル図鑑
st.title('ゼミ生スキル丸分かり表')

col1, col2, = st.columns(2)

with col1:
    st.header('3年生[13期生]')
    st.image("ushio-img/higuti.png")
    st.image("ushio-img/hokamiya.png")
    st.image("ushio-img/hori.png")
    st.image("ushio-img/hukunaga.png")
    st.image("ushio-img/kana.png")
    st.image("ushio-img/kanamaru.png")
    st.image("ushio-img/kido.png")
    st.image("ushio-img/maesaki.png")
    st.image("ushio-img/mitumoto.png")
    st.image("ushio-img/miyazaki.png")
    st.image("ushio-img/morotomi.png")
    st.image("ushio-img/nakano.png")
    st.image("ushio-img/noguti.png")
    st.image("ushio-img/sigematu.png")
    st.image("ushio-img/takeisi.png")
    st.image("ushio-img/ueda.png")
    st.image("ushio-img/yusuke.png")


with col2:
    st.header('4年生[12期生]')
    st.image("ushio-img/zyunbi.png")



#就活体験記
#st.title('太宰ゼミ卒業生の就職先図鑑')
#interest_job = st.radio(
    #'Q. あなたは以下の業界で興味のあるものはありますか？',
    #('データサイエンティスト', 'Webマーケティング', 'SNSによる集客')
#)

#if interest_job == 'データサイエンティスト':

    #電通
    #agree = st.checkbox('電通')
    #if agree:
        #st.write('お疲れ様です、11期の横溝です。自分は大学入学時に一つ大きな目標を掲げました。それは”自分が楽しいと思うことを仕事にすること”です。自分は誇りを持って仕事をする人に強く憧れていて、正直、自分は事務作業でも力仕事でも公務員でも、自分がそれをやりたい!と思っていたらどんな仕事でもいいなと思っている人間です。その為、自分は最初教員を目指していましたが、大学在学中に様々な出会いと体験から電通デジタルという企業で働くことを決めました。そんな1人の人間の就活体験記です。流し読み程度にコーヒーでも飲みながら読んでみてください。 ')
        #st.header('2. 自分の性格と価値観')
        #st.write('自分の性格と価値観を言っておきます。性格と価値観って意外と重要で、就活体験記を読んでいて性格と価値観が似ていると共感する点が多かったりする為、一応書いておきます。自分は多面性のある人間です。(みんなそうかも)自分はロマンチストでありリアリストでもあります(ロマンチスト強め)。素直で人懐っこい人間です。子供みたいにはしゃぎますし、大人みたいに冷静で論理的な一面もあります。あと、自分の意見や考えは必ず持ちます。価値観は「1.初めに」で書いたような感じです。')
        #st.header('3. 大学での行動 ')
        #st.write('入学当初は目標を立て、一番身近な職業の教員を目指し、教職課程を取りました。「自分が楽しいことを見つけるためにまずは業界を知らないと」と感じ、業界研究セミナーに参加しました。1年次は全く楽しいことを見つけられませんでした。2年次からはゼミに入り、9期の松本さんと出会い「とりあえずやってみよう」の精神でプログラミングを始めました。ここから俺の世界観が一変していたみたいです。2年次はプログラミング、勉強会の参加、ゼミ活動、遊び、全てが充実していました。3年次からは、自分のしたいことがデータサイエンティストと呼ばれる職種の業務内容だと気づき、猛勉強、猛遊び、猛悩み、猛不安。といった感じです。')
        #st.header('4. 後輩に伝えたいこと')
        #st.write('他の就活体験記で書いていそうなことは書きません。 ')
        #st.write('・目標や夢のためなら迷わず努力しろ ')
        #st.write('太宰ゼミの中には、福岡大学では就活が難しいと思われる仕事に就きたいと思っている人がいると思います。もし自分と同じで「楽しいことを仕事にしたい」と思う人がいたら、俺はその人達を応援します！ただ、人一倍努力をする必要はあります。どのくらい努力が必要かと言われたらわかりません笑。俺は二年次基本毎日プログラミングしていました。(ただこんなことをみんなには言ったりしていません。これはあくまで夢のためにやっていたことなのでひけらかすことでもないです笑。)')
        #st.header('5. インターン経験')
        #image_yokomizo1 = Image.open('ushio-img/yokomizo_1.png')
        #st.image(image_yokomizo1, caption='')
        #st.header('6. 就活フロー')
        #image_yokomizo2 = Image.open('ushio-img/yokomizo_2.png')
        #st.image(image_yokomizo2, caption='')
        #st.header('7. 選考状況')
        #image_yokomizo3 = Image.open('ushio-img/yokomizo_3.png')
        #st.image(image_yokomizo3, caption='')
        #st.header('8. 最後に')
        #st.write('自分は周りから「横溝なら就活余裕だろ」と言われていました。でも、自分の目指す方向は文系ではなく理系や院生が多かったです。その為、毎日不安と戦いました。性格や就活の軸、将来の夢は人それぞれです。自信がなくなる時もあります。それでも大事なのは自分自身が自分の味方でいることかなと思います。強がったりせずに自分の良いところ悪いところを全て認めて、ありのままを受け入れることが大事かなと。')
        #st.write('２年生はこれから様々な人に出会い、多くの体験をするかなと思います。３年生は将来を考え始める人もいると思います。正直働くことが全てではないし、人生なんて人それぞれなので、自分のペースで楽しく生きましょう!')
        #st.write('俺は頑張る人を応援するし力になりたいです！　就活頑張ってください！！')

    #カホエンタープライズ
    #agree = #st.checkbox('カホエンタープライズ')
    #if agree:
        #st.write('これから書くことは全て僕の持論です。僕以外の人の話もですが、鵜呑みにしないよう気をつけてください。皆さんの考えで、取り入れるか取り入れないか判断してください。少しでも気づきがあれば幸いです。')
        #st.write('僕はカホエンタープライズに内定をいただきました。（正確には嘉穂無線ホールディングス） Tableauというデータ可視化ツールを取り扱う会社です。グループ会社にホームセンターのグッデイがあります。')
        #st.header('【使っていたサイト】')
        #st.write('マイナビ、リクナビ、ワンキャリア、就活会議、OfferBox、エンカレッジ 『勉強会系』 テックプレイ、connpass ')
        #st.header('【就活のためにやったこと】')
        #st.write('大学の就活セミナーや会社説明会に参加する')
        #st.write('SPIの勉強')
        #st.write('やってきたことをまとめる。')
        #st.write('・やったこと ')
        #st.write('・きっかけ ')
        #st.write('・目的 ')
        #st.write('・苦労')
        #st.write('・学び/“自分“の考え')
        #st.write('・評価(あれば)')
        #st.write('この項目を書き出してみると整理できる。')
        #st.write('Formsで自分についてのアンケート（他己分析）を作った。')
        #st.header('【就活終えての感想】')
        #st.write('就活ここから頑張るぞ！ではなく、なんとなく緩やかにやって、佳境だけ力を入れました。正直、明確な軸は『一緒に働く人』を重視するくらいで後は何も決めていません。業界を絞るだの大手と中小を決めるだのはやっていません。だからなのか、今も“この会社で良かったのかな”と思うことはあります。でも、その答えは誰もわからないし、これからの自分次第で正解にも不正解にもなると思っています。別に世界にこの会社しかないわけではないので、違うと思ったら違う道を探すつもりでもあります。')
        #st.header('【みんなへ】')
        #st.write('嘘だけは絶対につかないように。人事の方を甘く見ない方がいいです。ほんの少しの誇張くらいにしてください。逆に言えば、内容はそこまででも熱意が伝われば良い評価を得られる可能性があります。')
        #st.write('就活の軸や進め方は人それぞれです。同じように、着地点も人それぞれです。僕は結局、マイナビとかではなく、直談判でお願いしたところに入社しました。そういう進め方もある、と知っておいて欲しいです。就活のやり方はいくらでもあります。みんな自身の発想や工夫を実行してみてください。失礼でない限り、嫌がる人はあまりいないと思います。むしろ積極的だと評価される可能性が高いです。')
        #st.write('社会人と学生は対等であるべきです。敬意を持つのは当たり前ですが、明らかにへり下る必要はありません。')
        #st.write('人と話すことはめちゃくちゃオススメです。先輩、後輩、友達、先生、親などなど。同じ人だけでなく、いろんな立場の人と話した方がいいです。話すと、頭の中のことを口に出す難しさを知れるし、整理できるし、フィードバックももらえます。頭の中だけで考えることには限界があります。是非人と話して、考えを頭の中から出してあげてください。')
        #st.write('最後に、これは僕もこれから身につけたいことなのですが、『質問力』と『読取力』を磨くと良いと思います。')
        #st.write('質問力というのは、相手に対する質問の量もですが、特に質のことを言いたいです。「はい/いいえ」で答えられる内容か？相手も気付いていない領域か？聞き方は本当に適切か？を考えてください。例えば、入社後にどんな働き方ができるのか、という疑問を持っているとします。そこで「どんな働き方ができますか？」と聞くのは簡単です。そうではなく、「入社後に、私にどのようなポジション、キャリア、働き方を期待していますか？」と聞くことで、相手の中にある理想像を引き出すことができると思います。')
        #st.write('読取力は、そのままです。相手の発言や行動には、一つ一つ隠された意図があるはずです。それを少しでも汲み取るセンサーを磨いておくと、共感力が上がって相手が何を求めているかわかるようになると思います。')
        #st.write('皆さん一人一人に合う会社と出会えることを願っています。')
        #st.write('就活に使ったノートとか、自己PRやガクチカをまだWordで残しています。 見たい方がいれば声かけてください。 ')


#if interest_job == 'Webマーケティング':
    
    

        




#サイドバー
st.sidebar.title('現在のあなた')
st.sidebar.write('常に自分のことを理解しておくと、今すべき行動がわかるので成長が速くなります。')
your_number = st.sidebar.text_input('あなたの学籍番号')
your_name = st.sidebar.text_input('あなたの名前')
st.sidebar.write('現在あなたの興味のある分野：')
st.sidebar.write(interest_now)




