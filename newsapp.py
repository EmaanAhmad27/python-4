import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st
from datetime import datetime
def scrape_news(url, max_articles=10):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find_all('h2', class_='story__title')[:max_articles] 
    news_data = []
    for headline in headlines:
        title = headline.get_text().strip()  
        link = headline.find('a')['href']  
        article_url = f"https://www.dawn.com{link}" if link.startswith('/') else link
        article_response = requests.get(article_url)
        article_soup = BeautifulSoup(article_response.text, 'html.parser')
        date_tag = article_soup.find('span', class_='timestamp--time timeago')
        if date_tag:
            full_date = date_tag['title']  
            date = full_date.split('T')[0]  
        else:
            date = 'No Date'
        summary_tag = article_soup.find('p') 
        summary = summary_tag.get_text().strip() if summary_tag else 'No Summary'
        category = categorize_article(title)
        news_data.append([title, date, summary, category])
    return pd.DataFrame(news_data, columns=['Title', 'Publication Date', 'Summary', 'Category'])
def categorize_article(title):
    title = title.lower()  
    if any(keyword in title for keyword in ['amendment', 'political rights', 'governance', 'politics']):
        return 'Domestic Politics and Governance'
    elif any(keyword in title for keyword in ['government policies', 'initiative', 'power relief', 'exports']):
        return 'Government Policies and Initiatives'
    elif any(keyword in title for keyword in ['kashmir', 'occupied kashmir']):
        return 'Kashmir Updates'
    elif any(keyword in title for keyword in ['us elections', 'donald', 'global implications', 'trump']):
        return 'International Relations'
    elif any(keyword in title for keyword in ['climate change', 'environmental issues', 'pollution', 'air quality']):
        return 'Climate Change & Environmental Issues '
    elif any(keyword in title for keyword in ['cricket', 'trophy', 'runners', 'pakistan', 'odi', 'sports']):
        return 'Sports and Entertainment'
    elif any(keyword in title for keyword in ['international incidents', 'plane', 'flight', 'qantas']):
        return 'Global Events & International Incidents'
    else:
        return 'General' 
def display_news():
    news_url = 'https://www.dawn.com/latest-news' 
    news_df = scrape_news(news_url, max_articles=20)  
    categories = news_df['Category'].unique()
    selected_category = st.sidebar.selectbox("Select Category", ["All Categories"] + list(categories))
    start_date, end_date = st.sidebar.date_input("Select Date Range", [datetime(2024, 1, 1), datetime.today()])
    if selected_category != "All Categories":
        news_df = news_df[news_df['Category'] == selected_category]
    news_df['Publication Date'] = pd.to_datetime(news_df['Publication Date'], errors='coerce')
    news_df = news_df[(news_df['Publication Date'] >= pd.Timestamp(start_date)) & (news_df['Publication Date'] <= pd.Timestamp(end_date))]
    if news_df.empty:
        st.write("No news articles found with the selected filters.")
    else:
        st.markdown("""
        <style>
        .news-ribbon {
            background-color: #3776ab;  /* Blue color for ribbon */
            color: white;
            padding: 10px;
            font-size: 24px;
            font-weight: bold;
            text-align: center;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
        </style>
        <div class="news-ribbon">
            📰 Latest News Articles
        </div>
        """, unsafe_allow_html=True)
        for idx, row in news_df.iterrows():
            st.markdown(f"### {idx + 1}. **{row['Title']}**")  
            st.write(f"**Published on:** {row['Publication Date'].strftime('%Y-%m-%d')}")
            st.write(f"**Category:** {row['Category']}")
            st.write(f"**Summary:** {row['Summary']}")
            st.markdown("---")  
if __name__ == '__main__':
    display_news()
