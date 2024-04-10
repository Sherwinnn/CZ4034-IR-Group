# Solr Index Structure for Core: restaurantCore

## Fields

- **LatLong**
  - Type: location
  - Indexed: Yes
  - Stored: Yes
  - MultiValued: No

- **_root_**
  - Type: string
  - Indexed: Yes
  - Stored: No
  - MultiValued: No

- **_version_**
  - Type: plong
  - Indexed: No
  - Stored: No
  - MultiValued: No

- **address**
  - Type: text_general
  - Indexed: Yes
  - Stored: Yes
  - MultiValued: No

- **categoryName**
  - Type: text_general
  - Indexed: Yes
  - Stored: Yes
  - MultiValued: No

- **id**
  - Type: string
  - Indexed: Yes
  - Stored: Yes
  - MultiValued: No

- **isLocalGuide**
  - Type: boolean
  - Indexed: Yes
  - Stored: Yes
  - MultiValued: No

- **likesCount**
  - Type: pint
  - Indexed: Yes
  - Stored: Yes
  - MultiValued: No

- **neighborhood**
  - Type: text_general
  - Indexed: Yes
  - Stored: Yes
  - MultiValued: No

- **publishedAtDate**
  - Type: pdate
  - Indexed: Yes
  - Stored: Yes
  - MultiValued: No

- **qualityScore**
  - Type: pdouble
  - Indexed: Yes
  - Stored: Yes
  - MultiValued: No

- **restaurant**
  - Type: text_general
  - Indexed: Yes
  - Stored: Yes
  - MultiValued: No

- **review**
  - Type: text_general
  - Indexed: Yes
  - Stored: Yes
  - MultiValued: No

- **reviewContextMeal**
  - Type: text_general
  - Indexed: Yes
  - Stored: Yes
  - MultiValued: No

- **reviewContextParking**
  - Type: text_general
  - Indexed: Yes
  - Stored: Yes
  - MultiValued: No

- **reviewContextService**
  - Type: text_general
  - Indexed: Yes
  - Stored: Yes
  - MultiValued: No

- **reviewDetailedRatingAtmosphere**
  - Type: text_general
  - Indexed: Yes
  - Stored: Yes
  - MultiValued: No

- **reviewDetailedRatingFood**
  - Type: text_general
  - Indexed: Yes
  - Stored: Yes
  - MultiValued: No

- **reviewDetailedRatingService**
  - Type: text_general
  - Indexed: Yes
  - Stored: Yes
  - MultiValued: No

- **review_stars**
  - Type: pint
  - Indexed: Yes
  - Stored: Yes
  - MultiValued: No

- **reviewer**
  - Type: text_general
  - Indexed: Yes
  - Stored: Yes
  - MultiValued: No

- **reviewerNumberOfReviews**
  - Type: pfloat
  - Indexed: Yes
  - Stored: Yes
  - MultiValued: No

- **reviewsCount**
  - Type: pint
  - Indexed: Yes
  - Stored: Yes
  - MultiValued: No

- **street**
  - Type: text_general
  - Indexed: Yes
  - Stored: Yes
  - MultiValued: No

- **text**
  - Type: text_general
  - Indexed: Yes
  - Stored: No
  - MultiValued: Yes

- **text_rev**
  - Type: text_general_rev
  - Indexed: Yes
  - Stored: No
  - MultiValued: Yes

- **totalScore**
  - Type: pfloat
  - Indexed: Yes
  - Stored: Yes
  - MultiValued: No

## Index Information

- Number of Documents: 10677
- Max Document: 10677
- Deleted Documents: 0
- Segment Count: 1
