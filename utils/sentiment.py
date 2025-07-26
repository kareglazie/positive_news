from textblob import TextBlob
from transformers import pipeline

SENTIMENT_ANALYZER = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def analyze_sentiment(text):
    if not text:
        return "neutral"
    
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0.3: 
        return "positive"
    
    if len(text.split()) < 100:
        try:
            result = SENTIMENT_ANALYZER(text[:512])[0]
            if result["label"] == "POSITIVE" and result["score"] > 0.8:
                return "positive"
        except:
            pass
    
    return "neutral"

def filter_good_news(articles):
    good_news = []
    for article in articles:
        title = article.get("title", "")
        content = article.get("content", "") or article.get("description", "") or title
        content_lead = content[:500]
        negative_indicators = ["death", "war", "attack", "crisis", "murder", "destroy", "attacks", "condemn", "murdered",
                               "wars", "accuse", "accused", "investigation", "court", "destroyed", "condemned", "investigated",
                               "prosecutor", "humiliation", "humiliate", "demolish", "destroys", "criticize", "criticized",
                               "die", "dies", "died", "attacked", "humility", "burden", "homeless", "refugee", "refugees"]
        if any(word in title for word in negative_indicators) or \
           any(word in content_lead for word in negative_indicators):
            continue
            
        if analyze_sentiment(content) == "positive":
            good_news.append(article)
    return good_news

