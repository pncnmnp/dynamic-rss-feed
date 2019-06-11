# The Orient Chronicles
<p align="center">
<img src="https://github.com/pncnmnp/dynamic-rss-feed/blob/master/screenshots/news_1.png">
</p>

### Description
The Orient Chronicles is a news aggregator written in Django. It fetches news from various RSS feeds, prioritizes them according to the category's trend and displays the filtered news. <br/>
The features of this news aggregator are:
* Syndication support for each news category
* Support for custom search across all news categories
* Stores all news chronologically in a compressed format
* Automatically filters database periodically
* Clean and minimalistic UI

### Instructions
To increase the diversity of news, insert your RSS links in `./news/headlines/datasets/news_urls.json`. If you want a new news-category, you will have to update `categories.json` as well. To see the changes just add another category to the template - `./news/headlines/templates/index.html`.<br/>
If an update to the news is required, go to `https://base_url/headlines/update`. This will update the current headlines page. All the news previously fetched are stored in `./news/headlines/datasets/past_news/`.

### License
This project is under MIT License. Some of the logos used are under [Creative Commons License 3.0](https://creativecommons.org/licenses/by/3.0/). See the `imgs` repository in `headlines/static/` for more details.