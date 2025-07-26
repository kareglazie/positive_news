import streamlit as st
from news_api.client import fetch_news
from utils.sentiment import filter_good_news
from utils.display import display_news
from utils.topics import generate_random_topic

st.title("🌞 Positive News Generator")
st.markdown("Discover uplifting stories from around the world")

if 'topic' not in st.session_state:
    st.session_state.topic = "positive news"
col1, col2 = st.columns([4, 1])
with col1:
    topic = st.text_input(
        "What positive news would you like to see?", 
        placeholder="e.g., technology, science, health...",
        value=st.session_state.topic
    )
with col2:
    if st.button("🎲 Random Topic"):
        st.session_state.topic = generate_random_topic()
        st.rerun() 

with st.expander("Advanced Filters"):
    col1, col2 = st.columns(2)
    with col1:
        language = st.selectbox("Language", ["en", "es", "fr", "de", "it"])
    with col2:
        num_articles = st.slider("Number of articles", 5, 20, 10)

if st.button("Get Positive News!", type="primary"):
    if not topic.strip():
        st.warning("Please enter a search topic or generate a random one")
    else:
        with st.spinner(f"🔍 Searching for positive news about '{topic}'..."):
            raw_news = fetch_news(query=topic, language=language, page_size=num_articles)
            good_news = filter_good_news(raw_news)
            
            if good_news:
                st.success(f"✨ Found {len(good_news)} positive news stories about '{topic}'")
                display_news(good_news)
            else:
                st.warning(f"No positive news found about '{topic}'. Try another topic or adjust your filters")