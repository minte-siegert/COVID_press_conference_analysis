==========================================================
 D A T A S E T / D A T A B A S E  D E S C R I P T I O N
==========================================================

(template based on https://arxiv.org/abs/1803.09010)


* Name of the dataset/database:
COVID-19 Press Conference Responses in the Netherlands



==========================================================
1. MOTIVATION
==========================================================

1.1  For what purpose was the dataset created?
    Was there a specific task in mind? Was there
        a specific gap that needed to be filled?
    Please provide a description.
‘COVID-19 Press Conference Responses NL’ was created with
the purpose of researching how individuals respond (sentiment)
to their national leaders’ crisis management capabilities.
This dataset in particular aimed to get a closer look at the
responses from individuals residing in the Netherlands to the
new COVID-19 prevention policies (announced on April 21st, 2020)
and the way the Prime Minister Mark Rutte communicated such
measures. In such a way, this data can be used to perform a
sentiment analysis in order to study citizens’ attitudes towards
the new COVID-19 preventive measurements, as well as the way
the situation has been handled by the country’s national leader.
This analysis could serve to perhaps examine if any improvements
can be made to the way COVID-19 preventive measures are
currently being communicated in order to more efficiently
incite citizens to comply with these policies accordingly.
Furthermore, the data could also be used for future research
aimed at comparing individual responses to their national
leaders’ crisis management capabilities for different pandemics
or other types of national crises across time.

1.2  Who created this dataset
    (e.g., which team, research group) and on behalf of
        which entity (e.g., company, institution, organization)?
The dataset was created by Jahna van den Burg, Nikki Jacobs,
Maria Rodriguez, Minte Siegert and Dionne Verkerk for the course
of Research in Social Media at Tilburg University.

1.3  Who funded the creation of the dataset?
    If there is an associated grant, please provide
        the name of the grantor and the grant name and number.
The dataset was generated from the Twitter API. This is an API
for which users can get free access, due to this no funding was
needed for the creation of the dataset.

1.4  Any other comments?

==========================================================
2. COMPOSITION
==========================================================

2.1  What do the instances that comprise the dataset represent
    (e.g., documents, photos, people, countries)?
    Are there multiple types of instances (e.g., movies,
        users, and ratings; people and interactions between them;
        nodes and edges)?
    Please provide a description.
The instances are tweets and retweets extracted from Twitter.
These tweets consist of text and possibly photos and videos.

2.2  How many instances are there in total
    (of each type, if appropriate)?
The original dataset consists of in total 10,932 tweets (instances).

2.3  Does the dataset contain all possible instances or is it a sample
    (not necessarily random) of instances from a larger set?
    If the dataset is a sample, then what is the larger set?
    Is the sample representative of the larger set
        (e.g., geographic coverage)? If so, please describe how this
        representativeness was validated/verified.
    If it is not representative of the larger set, please describe why not
    (e.g., to cover a more diverse range of instances, because
    instances were withheld or unavailable).
The Twitter API does not generate a full source of tweets,
because not all tweets get indexed or are made available.
The tweets were collected between 15 minutes before the press
conference until 10 minutes after, this way it only takes a part
of the overall reactions of the citizens. As well, it is
unknown whether tweets made under private accounts are
extracted by the API (examination of the data so far has only
shown publicly available tweets). Thus, the sample is not
representative of all the users because APIs have an in-built
bias toward types of users that are the most active content
contributors, and a possible inability to provide tweets under
private accounts.

2.4  What data does each instance consist of?
    "Raw" data (e.g., unprocessed text or images)
    or features? In either case, please provide a description.
Each instance consists of unprocessed tweets and retweets.
The main object is the Tweet object. All tweets also include a
user object and an entity’s object. The user object describes
who authored the tweet and the entity’s object shows hashtags,
user mentions, URLs, and native media. When the tweet has an
attached media object, the data will also show an
extended_entities object. A retweet also contains a
retweeted_status object, which shows the retweet itself and its
user object.

2.5  Is there a label or target associated with each instance?
    If so, please provide a description.
No, there are no labels provided.

2.6  Is any information missing from individual instances?
    If so, please provide a description, explaining why this information is
    missing (e.g., because it was unavailable). This does not include
        intentionally removed information, but might include, e.g., redacted text.
Yes, there are a few missings in most of the data.
    Especially in the user data, which contains a lot of ‘null’
    on the geo, coordinates, place and contributors. This is
    because of the privacy default settings of some users.
    But also the reply status and/or users id is missing in most
    of the data. This indicates that no other users interacted
    with a particular instance.


2.7  Are relationships between individual instances made
    explicit (e.g., users' movie ratings, social network links)?
    If so, please describe how these relationships are made explicit.
Technically no, there are no known relationships between the
instances except for the fact that all the tweets are in the
database because they used the same #. So they all relate to the
event but not to each other.

2.8  Are there recommended data splits (e.g., training, development/validation,
    testing)?
    If so, please provide a description of these splits, explaining the
    rationale behind them.
The 80/20 model will be used to split data. This entails that 80%
of the data set will be used to run the analysis, and the results
will be validated by running the same analysis on the remaining 20%.

2.9  Are there any errors, sources of noise, or redundancies in the dataset?
    If so, please provide a description.
No, there are no errors, sources of noise or redundancies in the dataset.

2.10 Is the dataset self-contained, or does it link to or otherwise rely on
    external resources (e.g., websites, tweets, other datasets)?
    If it links to or relies on external resources,
    a) are there guarantees that they will exist, and remain constant,
        over time;
    b) are there official archival versions of the complete dataset
    (i.e., including the external resources as they existed at the
    time the dataset was created);
    c) are there any restrictions (e.g., licenses, fees) associated with
    any of the external resources that might apply to a future user?
    Please provide descriptions of all external resources and any restrictions
    associated with them, as well as links or other access points, as
        appropriate.
The dataset creation relied on external resources, the Twitter API.
The database has been downloaded and will remain on the laptop of each
of the researchers. So the database will stay constant and the same,
it will not change in the future.

2.11 Does the dataset contain data that might be considered confidential
    (e.g., data that is protected by legal privilege or by doctor-patient
    confidentiality, data that includes the content of individuals'
    non-public communications)?
    If so, please provide a description.
No. All data were derived from publicly available news sources.

2.12 Does the dataset contain data that, if viewed directly, might be offensive,
    insulting, threatening, or might otherwise cause anxiety?
    If so, please describe why.
Generally not. Some tweets might contain moderately inappropriate or
offensive language, but it is not expected that this will be the
norm.

2.13 Does the dataset relate to people?
    If not, you may skip the remaining questions in this section.
The data relates to people’s responses (sentiments) to the Dutch press
conference on April 21st, 2020 on the new measures taken to battle
the COVID-19 crisis.

2.14 Does the dataset identify any subpopulations (e.g., by age, gender)?
    If so, please describe how these subpopulations are identified and
    provide a description of their respective distributions within the dataset.
The whole Twitter population was able to use the hashtags #coronavirus
#MarkRutte and #persconferentie, so no subpopulations are identified.

2.15 Is it possible to identify individuals (i.e., one or more natural persons),
    either directly or indirectly (i.e., in combination with other data)
    from the dataset?
    If so, please describe how.
It would be possible to directly identify individuals by looking up their
“screen_name”, which is included in the dataset. Indirectly, the users
could be found by searching for the text in the tweets.

2.16 Does the dataset contain data that might be considered sensitive in
    any way (e.g., data that reveals racial or ethnic origins, sexual
    orientations, religious beliefs, political opinions or union memberships,
    or locations; financial or health data; biometric or genetic data;
    forms of government identification, such as social security numbers;
    criminal history)?
    If so, please provide a description.
It is possible that there might be political views/opinions reflected in
some of the instances due to the fact that the event was a press
conference carried out by the Prime Minister of the Netherlands.

2.17 Any other comments?

==========================================================
3. COLLECTION PROCESS
==========================================================

3.1  How was the data associated with each instance acquired?
    Was the data directly observable (e.g., raw text, movie ratings),
    reported by subjects (e.g., survey responses), or indirectly
        inferred/derived from other data (e.g., part-of-speech tags, model-based
       guesses for age or language)? If data was reported by subjects or indirectly
    inferred/derived from other data, was the data validated/verified?
    If so, please describe how.
The data was directly observable by means of using a Twitter API to collect
tweets that were tweeted between 18:45 PM and 19:50 PM
(Central European Summer Time) by people using the hashtags #MarkRutte
#coronacrisisnederland or #persconferentie.

3.2  What mechanisms or procedures were used to collect the data
    (e.g., hardware apparatus or sensor, manual human curation,
        software program, software API)?
    How were these mechanisms or procedures validated?
Twitter API was used to collect the data. The validation of this mechanism
on Twitter’s behalf is unknown.

3.3  If the dataset is a sample from a larger set, what was the sampling strategy
    (e.g., deterministic, probabilistic with specific sampling probabilities)?
The dataset was a sample. The sampling strategy is unclear, as this is
integrated within the API’s settings. For more details see question 2.3.

3.4  Who was involved in the data collection process (e.g., students,
      crowdworkers, contractors) and how were they compensated (e.g., how
        much were crowdworkers paid)?
The data collection was carried out by the students of “team 17” from the
Research in Social Media course at Tilburg University. There was no
compensation awarded to those involved in this data collection process.

3.5  Over what timeframe was the data collected? Does this timeframe
    match the creation timeframe of the data associated with the
    instances (e.g., recent crawl of old news articles)?
    If not, please describe the timeframe in which the data associated with the
    instances was created.
Data was collected between 18:45 PM to 19:50 PM (Central European Summer Time)
on April 21st, 2020. The time-frame shown in the dataset does not seem to
directly match the creation time-frame associated with the instances, but not
because older tweets crawled into the data collection but rather because there
seems to be a mismatch between timezones (CEST vs. GMT). The first instance
listed in the data shows a timestamp of “16:45 PM” (exactly two hours prior
to the start of data collection), but when following the link
(in the CEST time zone) to examine the tweet further, the timestamp found
reads “18:45 PM”.

3.6  Were any ethical review processes conducted (e.g., by an institutional
    review board)?
    If so, please provide a description of these review processes, including
    the outcomes, as well as a link or other access point to any
    supporting documentation.
No ethical review processes were conducted during the data collection process.

3.7  Does the dataset relate to people?
    If not, you may skip the remainder of the questions in this section.
Yes, the dataset relates to people. Each instance is a tweet from a
particular Twitter user.

3.8  Did you collect the data from the individuals in question directly,
    or obtain it via third parties or other sources (e.g., websites)?
The data was not obtained from the individuals directly, but rather through
the use of Twitter’s API. So the data was crawled from Twitter.

3.9  Were the individuals in question notified about the data collection?
    If so, please describe(or show with screenshots or other information) how
    notice was provided, and provide a link or other access point to,
    or otherwise reproduce, the exact language of the notification itself.
No, the individuals in question were not notified about the data collection.

3.10 Did the individuals in question consent to the collection and use of their
    data?
    If so, please describe (or show with screenshots or other information)
    how consent was requested and provided, and provide a link or other access
    point to, or otherwise reproduce, the exact language to which the
    individuals consented.
Technically, yes. By accepting the terms and conditions from the site when
signing up for a Twitter account, individuals allow the service provider
(Twitter) to use the information they make publicly available. Twitter
specifically highlights this in the “Privacy” section of their terms of
service: https://twitter.com/en/tos, as well under the “Public Information”
section on their privacy conditions: https://twitter.com/en/privacy

3.11 If consent was obtained, were the consenting individuals provided with a
    mechanism to revoke their consent in the future or for certain uses?
    If so, please provide a description, as well as a link or other access
    point to the mechanism (if appropriate).
No, individuals are not provided with a mechanism to revoke their consent
in the future. The only thing they can do in the future, besides deleting
their account, is to share as little information as possible of themselves
that they do not want others to use or to keep their accounts private. But
other than that, there is no way individuals can stop Twitter from sharing the
information they make publicly available.

3.12 Has an analysis of the potential impact of the dataset and its use on data
    subjects (e.g., a data protection impact analysis)been conducted?
    If so, please provide a description of this analysis, including the
        outcomes, as well as a link or other access point to any supporting
        documentation.
No, there was no data protection impact analysis conducted.

3.13 Any other comments?

==========================================================
4. PREPROCESSING/CLEANING/LABELING
==========================================================

4.1  Was any preprocessing/cleaning/labeling of the data done (e.g.,
      discretization or bucketing, tokenization, part-of-speech tagging,
        SIFT feature extraction, removal of instances, processing of
        missing values)? If so, please provide a description. If not, you may
        skip the remainder of the questions in this section.
Yes, the dataset was labelled. Parts of the dataset are labelled, such as the 
sentiment, if the sentiment was lower than -0.2 it was labelled as negative, 
higher than 0.2 it is positive otherwise it is labelled as neutral.  
And tweets that has been retweeted are labelled as retweeted. 

4.2  Was the "raw" data saved in addition to the
    preprocessed/cleaned/labeled data (e.g., to support unanticipated
        future uses)? If so, please provide a link or other access point to
        the "raw" data.
Yes, we separated the data by using a Make file. All team members have the raw
data and the cleaned database saved separate on their computers. 

4.3  Is the software used to preprocess/clean/label the instances available?
    If so, please provide a link or other access point.
Yes, the instances are being labelled with their sentiment and if the tweet
was a retweet or not. 

4.4  Any other comments?


==========================================================
5. USES
==========================================================

5.1  Has the dataset been used for any tasks already?
    If so, please provide a description.
No further analysis or tasks have yet been executed on the dataset. No other
parties have used this dataset before to perform any tasks.

5.2  Is there a repository that links to any or all papers or systems
    that use the dataset?
    If so, please provide a link or other access point.
No other papers or systems have made usage of this dataset.

5.3  What (other) tasks could the dataset be used for?
The ‘COVID-19 Press Conference Responses NL’ can be used for analysis around
individuals' responses (sentiments) to a national leader's crisis management
capabilities. For instance, the insights can be used to show differences
between countries' crisis management responses, or compare multiple pandemic
crisis management responses over time.

5.4  Is there anything about the composition of the dataset or the way it was
        collected and preprocessed/cleaned/labeled that might impact future uses?
        For example, is there anything that a future user might need to know to
        avoid uses that could result in unfair treatment of individuals or groups
        (e.g., stereotyping, quality of service issues) or other undesirable harms
        (e.g., financial harms, legal risks) If so, please provide a description.
        Is there anything a future user could do to mitigate these undesirable
        harms?
Due to the fact that the data was already publicly available, on Twitter,
there is a minimum risk for harm.

5.5  Are there tasks for which the dataset should not be used?
    If so, please provide a description.
The dataset is collected for a specific setting, that of a crucial press
conference during the COVID-19 period. The specific context in which the
dataset is a part of makes it not suitable for a generalized conclusion or
decision regarding the people's responses (sentiments) to overall governments’
crisis management capabilities. In addition, the fact that the sample is part
of a bigger population, there are missing values in the dataset, and the
in-built bias of Twitter's API to active users, creates for certain limitations
regarding the sample's representativeness. Thus, this dataset should not be
used for tasks at high stakes.

5.6  Any other comments?

==========================================================
6. DISTRIBUTION
==========================================================

6.1  Will the dataset be distributed to third parties outside of the entity
    (e.g., company, institution, organization) on behalf of which the
    dataset was created?
    If so, please provide a description.
No, the data will be used by the students self, but there is a possibility the 
same dataset will be used by other students of the course Research in 
Social Media. 

6.2  How will the dataset be distributed(e.g.,tarball on website, API,
      GitHub)? Does the dataset have a digital object identifier (DOI)?
No, it will only be available for other students who follow the course Research
in Social Media.

6.3  When will the dataset be distributed?
It is distributed on April 21st 2020.

6.4  Will the dataset be distributed under a copyright or other intellectual
    property(IP) license, and/or under applicable terms of use (ToU)?
    If so, please describe this license and/or ToU, and provide a link or other
    access point to, or otherwise reproduce, any relevant licensing terms or
        ToU (Terms of Use), as well as any fees associated with these
        restrictions.
No, the dataset will be available for the students of the course Research in
Social Media

6.5  Have any third parties imposed IP-based or other restrictions on the
    data associated with the instances?
    If so, please describe these restrictions, and provide a link or other
    access point to, or otherwise reproduce, any relevant licensing terms,
    as well as any fees associated with these restrictions.
No, there are no restricties on the data, it is a dataset obtained from 
Twitter, which is open and free to use. 

6.6  Do any export controls or other regulatory restrictions apply to the
    dataset or to individual instances?
    If so, please describe these restrictions, and provide a link or other
    access point to, or otherwise reproduce, any supporting documentation.


6.7  Any other comments?

==========================================================
7. MAINTENANCE
==========================================================

7.1  Who is supporting/hosting/maintaining the dataset?
It is not necessary to maintain the dataset. The data conducted was for only
one specific moment on April 21st. After the production of the datasset all 
five of the students saved the database on their laptop. But the analysis 
of the dataset afterwards is mostly done by one student, Minte, specific 
information and conclusion are saved at here laptop. 

7.2  How can the owner/curator/manager of the dataset be contacted
    (e.g., email address)?
All the students can be contacted by their University mail. 

7.3  Is there an erratum?
    If so, please provide a link or other access point.


7.4  Will the dataset be updated (e.g., to correct labeling errors, add
    new instances, delete instances)?
    If so, please describe how often, by whom, and how updates will
    be communicated to users (e.g., mailing list, GitHub)?

7.5  If the dataset relates to people, are there applicable limits on the
    retention of the data associated with the instances
    (e.g., were individuals in question told that their data would be retained
      for a fixed period of time and then deleted)?
    If so, please describe these limits and explain how they will be enforced.

7.6  Will older versions of the dataset continue to be
    supported/hosted/maintained?
    If so, please describe how. If not, please describe how its obsolescence
    will be communicated to users.

7.7  If others want to extend/augment/build on/contribute to the dataset,
    is there a mechanism for them to do so?
    If so, please provide a description. Will these contributions be
    validated/verified?
    If so, please describe how. If not, why not? Is there a process for
    communicating/distributing these contributions to other users?
    If so, please provide a description.

7.8  Any other comments?
