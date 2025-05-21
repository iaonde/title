import streamlit as st
import random

# 关键词池
prefixes = [
    "Wholesale Custom", "Private Custom Designs", "Plastic Custom", "Personalized Custom", "Ordinary Custom",
    "New Design Custom", "Make Your Own Design Custom", "Low Moq Custom", "Hot Sell Custom",
    "Hot Sale Plastic Custom", "High Transparent Custom", "High Quality Factory Custom",
    "High Quality Custom Printed", "High Quality Clear Custom", "Factory Custom", "Factory Cheap Custom",
    "Eco-Friendly Custom", "Customized Wholesale", "Customized Hot Sale", "Customized High Quality",
    "Oem Custom Printing", "Custom Your Own", "Custom Wholesale", "Custom Various Shape", "Custom Trending",
    "Custom Printing", "Custom Printed", "Custom Print", "Custom Ordinary", "Custom Make Your Own",
    "Custom Image Printed", "Custom Hot Selling", "Custom Hot Sale", "Custom Eco-Friendly", "Custom Design",
    "Custom Cute Anime", "Custom Creative", "Custom Catoon Anime", "Eco-Friendly Keychain Custom",
    "Eco-Friendly Acrylic Custom", "Acrylic Charm Custom", "2025 Hot Sale Custom", "Promotional Custom",
    "Promotional Wholesale Custom", "Custom Promotional", "Wholesale Promotional Custom",
    "Promotional Gift Custom", "Souvenir Gifts Custom", "Decoration Gift Custom", "Decoration Keychain Custom",
    "Doc Creatives Custom", "Anime Peripheral Custom", "Star Peripheral Custom", "Personalised Custom",
]

adjectives = [
    "Keychain", "Charms", "Key Chains", "Key Rings", "Acrylic Keychain", "Acrylic Charm", "Acrylic Pendant",
    "Acrylic Key Rings", "Acrylic Key Chains", "Plastic Keychain", "Plastic Key Chain", "Charm", "Keychains", "Charms"
]

objects = [
    "Cute", "Cartoon", "Anime", "Mini", "Logo", "Photo", "Animal", "Kawaii", "Heart", "Character", "Fashionable",
    "DIY", "Eco-Friendly", "Spotify"
]

techniques = [
    "UV Printing", "CMYK UV Printing", "CNC Cut", "Diamond Cut", "Laser Cut", "Double Sided Printing",
    "Two Sided Print", "Both Side Print", "Digital Printing", "Single Side Print", "Front Side Print"
]

finishes = [
    "Double Side Clear", "Transparent", "Translucent", "Gradient", "Epoxy Epoxy", "Epoxy Glitter",
    "Double Sided Epoxy", "Single Sided Epoxy", "Double Sided Epoxy Resin", "Single Sided Epoxy Resin",
    "Double Sided Glitter Epoxy", "Double Sided Glitter Resin", "Single Sided Epoxy Epoxy",
    "Single Sided Epoxy Resin", "Two Side Epoxy Epoxy", "Front Side Epoxy Resin", "Hologram", "Holographic",
    "Holography", "Holo Star", "Rainbow", "Iridescent", "Cracked Holographic", "Glass Broken Holographic"
]

keyword_main = ["Custom Acrylic Keychain", "Acrylic Keychain"]
keyword_others = [
    "Custom Acrylic Charm", "Acrylic Charm", "Acrylic Key Rings", "Acrylic Key Chains",
    "Plastic Keychain", "Plastic Key Chain"
]

extras = [
    "with Glitter", "with Epoxy Glitter", "with Star Clasp", "with Color Edge", "Thick Acrylic",
    "as Gift", "as Phone Accessory", "for Souvenir Gifts"
]
keywords_pool = ["Custom Acrylic Keychain", "Custom Acrylic Charm", "Acrylic Keychain",
                 "Acrylic Charm", "Acrylic Key Rings", "Acrylic Key Chains",
                 "Plastic Keychain", "Plastic Key Chain"]

# Streamlit 界面
st.title("定制标题生成器")
st.markdown("生成包含关键词的产品标题 + 副标题")

# 控制项
count = st.slider("生成标题数量", 1, 5, 10)
use_extras = st.checkbox("是否包含副词（如 with/for+场景）", value=True)

col1, col2 = st.columns(2)
with col1:
    keyword_focus = st.selectbox("优先关键词", ["Acrylic Keychain","Acrylic Charm","Acrylic Key Chain","Plastic Keychain",
                                                "Key Rings", "Plastic Key Chain"])
with col2:
    keyword_prob = st.slider(f"关键词“{keyword_focus}”出现概率（%）", 0, 100, 60)

# 生成标题函数
def generate_title():
    is_priority = random.randint(1, 100) <= keyword_prob
    keyword_choice = keyword_focus if is_priority else random.choice(keywords_pool)
    extra = random.choice(extras) if use_extras else ""

    parts = [
        random.choice(prefixes),
        random.choice(adjectives),
        random.choice(objects),
        random.choice(techniques),
        random.choice(finishes),
        keyword_choice,
        extra
    ]
    return " ".join(p for p in parts if p.strip())

# 避免重复标题
def generate_unique_subtitle(main_title, used_titles):
    for _ in range(10):
        sub = generate_title()
        if sub != main_title and sub not in used_titles:
            return sub
    return ""

# 展示标题
st.divider()
used_titles = set()
for i in range(count):
    main = generate_title()
    used_titles.add(main)
    sub = generate_unique_subtitle(main, used_titles)

    st.markdown(f"""
        <div style='text-align: left; padding: 10px;'>
            <strong>{i+1}.</strong><br>
            <span style='color: #0072C6;'>{main}</span><br>
            <span style='color: #5C5C5C;'>{sub}</span>
        </div>
        <hr>
    """, unsafe_allow_html=True)