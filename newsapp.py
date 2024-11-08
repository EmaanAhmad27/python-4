import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st
from datetime import datetime

# Function to scrape the news listing page
def scrape_news(url, max_articles=10):
    # Send a request to the website
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extracting titles from the homepage (limit to max_articles)
    headlines = soup.find_all('h2', class_='story__title')[:max_articles]  # Limit number of articles
    news_data = []

    # Iterate through all headlines and scrape each article
    for headline in headlines:
        title = headline.get_text().strip()  # Get the title of the article
        link = headline.find('a')['href']   # Get the link to the article

        # Construct the full URL for the article page
        article_url = f"https://www.dawn.com{link}" if link.startswith('/') else link

        # Scrape the article page for publication date, summary, and category
        article_response = requests.get(article_url)
        article_soup = BeautifulSoup(article_response.text, 'html.parser')

        # Extract the publication date from the timestamp span (using the 'title' attribute)
        date_tag = article_soup.find('span', class_='timestamp--time timeago')
        
        # Check if the date exists and format it properly
        if date_tag:
            full_date = date_tag['title']  # Full date-time string (e.g., "2024-11-08T18:45:22+05:00")
            date = full_date.split('T')[0]  # Extract the date part (before 'T')
        else:
            date = 'No Date'

        # Extracting the summary (using a generic method to find the first paragraph or relevant content)
        summary_tag = article_soup.find('p')  # Find the first <p> tag as the summary (adjust as needed)
        summary = summary_tag.get_text().strip() if summary_tag else 'No Summary'
        
        # Categorize the article based on keywords in the title
        category = categorize_article(title)

        # Append the scraped data to the list
        news_data.append([title, date, summary, category])

    # Return the data as a pandas DataFrame
    return pd.DataFrame(news_data, columns=['Title', 'Publication Date', 'Summary', 'Category'])

# Function to categorize articles based on keywords in the title
def categorize_article(title):
    title = title.lower()  # Convert title to lowercase for easier matching
    
    # Define categories based on provided topics
    if any(keyword in title for keyword in ['amendment', 'political rights', 'governance', 'politics']):
        return 'Domestic Politics and Governance'
    elif any(keyword in title for keyword in ['government policies', 'initiative', 'power relief', 'exports']):
        return 'Government Policies and Initiatives'
    elif any(keyword in title for keyword in ['modi', 'kashmir', 'occupied kashmir']):
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
        return 'General'  # Default category if no match is found

# Streamlit app function
def display_news():
    # Define the URL of the news page
    news_url = 'https://www.dawn.com/latest-news'  # Dawn's latest news page

    # Scrape the news articles
    news_df = scrape_news(news_url, max_articles=20)  # Set the number of articles to 20 or more

    # Category filter (unique categories in the dataset)
    categories = news_df['Category'].unique()
    selected_category = st.sidebar.selectbox("Select Category", ["All Categories"] + list(categories))

    # Date filter (using a date range picker)
    start_date, end_date = st.sidebar.date_input("Select Date Range", [datetime(2024, 1, 1), datetime.today()])

    # Filter data based on the selected category
    if selected_category != "All Categories":
        news_df = news_df[news_df['Category'] == selected_category]

    # Filter data based on the selected date range
    news_df['Publication Date'] = pd.to_datetime(news_df['Publication Date'], errors='coerce')
    news_df = news_df[(news_df['Publication Date'] >= pd.Timestamp(start_date)) & (news_df['Publication Date'] <= pd.Timestamp(end_date))]

    # Display the data using Streamlit
    if news_df.empty:
        st.write("No news articles found with the selected filters.")
    else:
        # Add News Ribbon on Title
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

        # Iterate through each article in the DataFrame and display it
        for idx, row in news_df.iterrows():
            # Display numbered article sections
            st.markdown(f"### {idx + 1}. **{row['Title']}**")  # Numbered title
            st.write(f"**Published on:** {row['Publication Date'].strftime('%Y-%m-%d')}")
            st.write(f"**Category:** {row['Category']}")
            st.write(f"**Summary:** {row['Summary']}")
            st.markdown("---")  # Add a line to separate articles visually

# Run the Streamlit app
if __name__ == '__main__':
    display_news()
