### Crawling results

The csv files with the name convention `apify_xxx.csv` were obtained from the original crawl using the Apify API. 

`apify_all_restaurants.csv`: information of all restaurants crawled  
`apify_all_reviews.csv`: reviews of all restaurants crawled  
`apify_restaurants_contact_info.csv`: additional information of the restaurants  

The reviews were initially cleaned. 
This includes removing all reviews which do not have any text in the reviews, did not leave any star ratings, or had reviews which were predominantly in a non-English language.

`cleaned_reviews.csv` should be used as the cleaned version of `apify_all_reviews.csv` hereafter. 
`initial_clean_reviews.ipynb` contains the code for the initial cleaning of reviews and splitting of 10% of reviews for annotation.
