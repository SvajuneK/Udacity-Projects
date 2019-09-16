# We Rate Dogs
## by Svajune Klimasauskaite


## Goal

The dataset that is used in this work is the tweet archive of Twitter user @dog_rates, also known as WeRateDogs. WeRateDogs is a Twitter account that rates people's dogs with a humorous comment about the dog. These ratings almost always have a denominator of 10. The numerators, though? Almost always greater than 10. 11/10, 12/10, 13/10, etc. Why? Because "they're good dogs Brent." WeRateDogs has over 4 million followers and has received international media coverage.
The goal is to create interesting and trustworthy analysis and visualizations and find explanations for the following questions:
* **What are the outcomes of image prediction algorithm?**
* **How did the follower count change over the years?**
* **How did twitting and retweeting likes change over the years?**
* **Which tweet characteristics predict likes and retweeting?**

## Dataset

* Enhanced Twitter Archive - The WeRateDogs Twitter archive contains basic tweet data for all 5000+ of their tweets, but not everything.
* Additional Data via the Twitter API - Back to the basic-ness of Twitter archives: retweet count and favorite count are two of the notable column omissions. Fortunately, this additional data can be gathered by anyone from Twitter's API.
* Image Predictions File - A table full of image predictions (the top three only) alongside each tweet ID, image URL, and the image number that corresponded to the most confident prediction 

## Summary

What are the outcomes of image prediction algorithm?
> * Dog breed success rate is 73.64%
> * Success rate distribution per each algoithms is very similar.
> * However the confidence interval for dog breed predictions has a very different distribution.

How did the follower count change over the years?
> * The followers number over the time has decreasing tendencies.

How did twitting and retweeting likes change over the years?
> * Despite the reducing of the followers' number, the tweet likes are increasing with the time.
> * However the user behaviour for liking and retweeting is changing slightly. 

Which tweet characteristics predict likes and retweeting?
> * Only 17.0% of the records had a Dogtionary category. 
> * However form those 17& cases you can see a clear correlation within the dogtionary and tweet likes or retweets. "doggo together with puppo are the favourite ones.  
----------
