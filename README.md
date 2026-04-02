# Blue Ocean Keyword Analyzer

A student research project to identify recurring pain points and market gaps by analyzing discussion trends on Reddit communities.

## Purpose

This tool helps student entrepreneurs discover underserved market opportunities by analyzing discussions in niche communities. It identifies which problems are frequently discussed and which solutions are missing—inspired by the "Jobs to be Done" framework taught in startup workshops.

**Use case:** Finding startup ideas based on real user frustrations in specific communities.

## Features

- **Keyword trend analysis**: Identify recurring pain points in community discussions
- **Market signal scoring**: Rank discussions by engagement (upvotes + comments)
- **Community-focused**: Search multiple niche subreddits at once
- **Demo output**: JSON results showing top opportunities

## Requirements

- Python 3.8+
- `praw` (Python Reddit API Wrapper)
- `python-dotenv` (for credentials)

## Installation

```bash
pip install praw python-dotenv
```

## Setup

1. Apply for Reddit API access (student/research project)
2. Create a `.env` file with your credentials:
```
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USER_AGENT=BlueOceanAnalyzer/1.0
REDDIT_USERNAME=your_username
REDDIT_PASSWORD=your_password
```

3. Run the analyzer:
```bash
python analyze_keywords.py
```

## Example Output

Shows top discussions matching pain-point keywords, ranked by community engagement:

- Post title and engagement score
- Common themes (manual work, missing tools, pricing issues, etc.)
- Links to original discussions for deeper research

## About This Project

This is a student project for exploring the "Blue Ocean Strategy" approach to finding startup ideas. It's used for personal market research and learning about user-centered product development.
