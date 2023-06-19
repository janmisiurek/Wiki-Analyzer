from urllib.parse import urlparse
import nltk
from nltk.probability import FreqDist
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')

def analyze_links_data(links, base_url):
    domain = urlparse(base_url).netloc
    internal_links = 0
    external_links = 0

    for link in links:
        if urlparse(link).netloc == domain:
            internal_links += 1
        else:
            external_links += 1

    return {
        "internal_links": internal_links,
        "external_links": external_links,
    }


def analyze_content_data(content):
    words = nltk.word_tokenize(content)
    words = [word.lower() for word in words if word.isalpha()]
    words = [word for word in words if word not in stopwords.words('english')]

    fdist = FreqDist(words)

    return dict(fdist.most_common(10))