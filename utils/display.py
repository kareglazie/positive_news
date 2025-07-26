import streamlit as st

def display_news(news):
    if not news:
        st.info("No news found matching your criteria")
        return
        
    for i, article in enumerate(news, 1):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.subheader(f"{i}. {article['title']}")
            st.caption(f"Source: {article.get('source', {}).get('name', 'Unknown')} • {article.get('publishedAt', '')[:20]}")
            st.write(article.get('description', article.get('content', '')))
            st.markdown(f"[Read full article]({article['url']})", unsafe_allow_html=True)
        with col2:
            if article.get('urlToImage'):
                st.image(article['urlToImage'], width=150)
        st.write("---")
