import streamlit as st
import plotly.graph_objects as go

# ========== 怪獸資料庫 ==========
monsters = {
    "雷焰獸": {
        "屬性": "🔥 火系",
        "攻擊": 92, "防禦": 65, "速度": 78, "魔力": 40,
        "稀有度": 4,
        "圖片": "https://i.imgur.com/jO1B4pM.png"
    },
    "冰魄狐": {
        "屬性": "❄ 冰系",
        "攻擊": 75, "防禦": 72, "速度": 92, "魔力": 95,
        "稀有度": 5,
        "圖片": "https://i.imgur.com/8cV8xVd.png"
    },
    "影鱗龍": {
        "屬性": "🌑 暗系",
        "攻擊": 88, "防禦": 70, "速度": 85, "魔力": 88,
        "稀有度": 5,
        "圖片": "https://i.imgur.com/96E6zWI.png"
    }
}

# ========== UI 樣式 ==========
st.set_page_config(page_title="Monster Lab", layout="centered")
st.title("🧪 Monster Lab｜怪獸研究室")

# 選擇怪獸
selected = st.selectbox("🔍 選擇研究對象：", list(monsters.keys()))
monster = monsters[selected]

# 左右版面
col1, col2 = st.columns([1, 2])

with col1:
    st.image(monster["圖片"], width=180)
    st.write(f"屬性：{monster['屬性']}")
    stars = "⭐" * monster["稀有度"]
    st.write(f"稀有度：{stars}")

with col2:
    st.subheader(f"{selected} 能力資料")
    st.write(f"攻擊：{monster['攻擊']}")
    st.write(f"防禦：{monster['防禦']}")
    st.write(f"速度：{monster['速度']}")
    st.write(f"魔力：{monster['魔力']}")

# ========== 雷達圖 ==========
labels = ["攻擊", "防禦", "速度", "魔力", "攻擊"]
values = [monster["攻擊"], monster["防禦"], monster["速度"], monster["魔力"], monster["攻擊"]]

fig = go.Figure(data=go.Scatterpolar(
    r=values,
    theta=labels,
    fill="toself",
    name=selected
))

fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])))
st.plotly_chart(fig)
