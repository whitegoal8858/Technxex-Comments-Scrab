
# Comment Scraping and Sentiment Detection & Analyzer

## Overview
This project is a web-based sentiment analysis tool that allows users to analyze YouTube video comments and Instagram post comments. It extracts engagement data (likes, views, and comments) and performs sentiment analysis, categorizing comments as positive, negative, or neutral.

## Features
- **YouTube Analysis**: Extracts video details, views, likes, and comment sentiment.
- **Instagram Analysis**: Scrapes Instagram post comments and performs sentiment analysis.
- **Graphical Representation**: Displays sentiment data in bar and line charts.
- **Neomorphic UI**: A modern and visually appealing design with a smooth UI.
- **Loading Page**: Displays a loading screen before showing results.

## Tech Stack
- **Frontend**: HTML, CSS (Neomorphism), JavaScript
- **Backend**: Python (Flask)
- **APIs Used**: YouTube Data API, Instagram Scraper (Apify/Other APIs)
- **Charts**: Chart.js for sentiment visualization

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/whitegoal8858/Technxex-Comments-Scrab/
   ```
2. Navigate to the project directory:
   ```sh
   cd index
   ```
3. Install required Python dependencies:
   ```sh
   pip install flask requests beautifulsoup4
   ```
4. Set up API keys for YouTube and Instagram (if needed).
5. Run the application:
   ```sh
   python app.py
   ```
6. Open the web app in your browser:
   ```
   http://127.0.0.1:5000
   ```

## Usage
1. Enter a YouTube video or Instagram post URL.
2. Click the **Search** button.
3. Wait for the loading page to finish processing.
4. View video details and sentiment breakdown in graphical form.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss your proposed changes.

