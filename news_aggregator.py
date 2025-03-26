import requests
from bs4 import BeautifulSoup
import json
from typing import List
import os

# Add near the top of the file
API_KEY = os.environ.get('NEWS_API_KEY')

# Modify API call to include your key
response = requests.get(source, params={
    'apiKey': API_KEY,
    'q': topic,
    'language': 'en',
    'sortBy': 'publishedAt'
})

class NewsAggregator:
    def __init__(self, topics: List[str]):
        self.topics = topics
        self.news_sources = [
            # Free News API Sources
            'https://newsapi.org/v2/everything',
            'https://api.currentsapi.services/v1/search',
            # Add more free news API endpoints
        ]
    
    def fetch_news(self) -> List[str]:
        all_headlines = []
        for topic in self.topics:
            for source in self.news_sources:
                try:
                    # Implement API calls with free API keys
                    response = requests.get(source, params={
                        'q': topic,
                        'language': 'en',
                        'sortBy': 'publishedAt'
                    })
                    headlines = self._extract_headlines(response.json())
                    all_headlines.extend(headlines)
                except Exception as e:
                    print(f"Error fetching news for {topic}: {e}")
        
        return all_headlines

    def _extract_headlines(self, api_response: dict) -> List[str]:
        # Implement parsing logic based on API response structure
        headlines = []
        # Example extraction (adjust based on actual API response)
        if 'articles' in api_response:
            headlines = [article['title'] for article in api_response['articles']]
        return headlines

    def generate_word_cloud(self, headlines: List[str]):
        from wordcloud import WordCloud
        import matplotlib.pyplot as plt
        
        # Combine headlines into a single text
        text = ' '.join(headlines)
        
        # Create and generate a word cloud image
        wordcloud = WordCloud(
            width=800, 
            height=400, 
            background_color='white',
            stopwords={'the', 'a', 'an', 'in', 'to', 'for'}
        ).generate(text)
        
        # Display the generated image
        plt.figure(figsize=(10,5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        
        # Save the image
        plt.savefig('daily_news_trends.png')
        plt.close()

def main():
    topics = ['Ukraine', 'Russia', 'Putin', 'Trump', 'Zelenskyy']
    aggregator = NewsAggregator(topics)
    headlines = aggregator.fetch_news()
    aggregator.generate_word_cloud(headlines)

if __name__ == '__main__':
    main()
