"""
Blue Ocean Keyword Analyzer - Minimal Demo

Identifies recurring pain points in Reddit communities to discover startup ideas.
"""

import os
from dotenv import load_dotenv
import praw
from collections import defaultdict

load_dotenv()

# Keywords that indicate unmet market needs
PAIN_KEYWORDS = [
    "no tool", "wish there was", "need something", "manual process",
    "no solution", "waste hours", "too expensive", "overpriced",
    "not built for", "why doesn't"
]

def analyze_community(subreddit_name, limit=50):
    """Analyze a subreddit for recurring pain point keywords"""

    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT", "BlueOceanAnalyzer/1.0"),
        username=os.getenv("REDDIT_USERNAME"),
        password=os.getenv("REDDIT_PASSWORD")
    )

    sub = reddit.subreddit(subreddit_name)
    results = []
    keyword_counts = defaultdict(int)

    # Analyze hot posts (current discussions)
    for post in sub.hot(limit=limit):
        title_lower = post.title.lower()
        engagement = post.score + (post.num_comments * 2)

        # Check for pain point keywords
        matched_keywords = [kw for kw in PAIN_KEYWORDS if kw in title_lower]

        if matched_keywords:
            results.append({
                "title": post.title,
                "engagement_score": engagement,
                "upvotes": post.score,
                "comments": post.num_comments,
                "keywords_matched": matched_keywords,
                "url": post.url
            })

            for kw in matched_keywords:
                keyword_counts[kw] += 1

    return {
        "community": subreddit_name,
        "top_discussions": sorted(results, key=lambda x: x["engagement_score"], reverse=True)[:5],
        "common_themes": sorted(keyword_counts.items(), key=lambda x: x[1], reverse=True)[:3]
    }


if __name__ == "__main__":
    # Example: Analyze a niche community
    communities = ["Etsy", "gamedev", "freelance"]

    for community in communities:
        try:
            print(f"\n📊 Analyzing r/{community}...")
            analysis = analyze_community(community, limit=30)

            print(f"   Top themes: {[t[0] for t in analysis['common_themes']]}")
            if analysis['top_discussions']:
                print(f"   Example: {analysis['top_discussions'][0]['title'][:60]}...")
                print(f"   Engagement: {analysis['top_discussions'][0]['engagement_score']}")
        except Exception as e:
            print(f"   ⚠️  Could not analyze: {e}")
