<b> Introduction <b>
The study provides evidence for the important role that news sentiment can play in 
predicting stock market movements, To test this hypothesis, the authors use machine 
learning algorithms to classify news articles as either positive or negative in 
sentiment, based on the content of the articles. They then analyze the correlation 
between the sentiment of the news articles and daily returns of the Shanghai 
Composite Index, which is a widely recognized benchmark of the Chinese stock 
market. This highlights the potential applications of machine learning algorithms in 
analyzing large amounts of textual data to identify patterns and correlations. 

<b> Terminologies <b>
<i>Labled data:<i> “labled data" refers to the labeled news articles for which the stock 
market movements are already known and used for training a machine learning model. 
<i>Unlabled data:<i> "unlabled data" refers to unlabeled news articles, for which the model 
predicts the corresponding stock market movements. 
<i>Daily sentiment score:<i> It is defined as the difference between the number of positive 
and negative news articles.  
<i>Positive and negative articles:<i> Positive and negative articles refer to news articles that 
contain language that is generally associated with positive or negative sentiment or 
emotion. 
<i>Returns:<i> here, returns refers to stock returns that is used to retrieve daily returns for 
the Shanghai Composite Index. 

<b> Steps Involved <b>
STEP 1: 
To apply the formula of Pearson coefficient to the relationship between news 
sentiment and stock market returns, Zhang et al. first calculated the daily sentiment 
score. 
Sentiment Score = p-n 
p-> no. of positive news articles 
n-> no. of negative news articles 
STEP 2: 
They then calculated the daily return from the Shanghai composite index 
daily return = (price today - price yesterday) / price yesterday 
STEP 3: 
Then, they calculate the daily returns of the Shanghai Composite Index, and 
use these two variables to calculate the Pearson correlation coefficient. 
r = (nΣxy - ΣxΣy) / sqrt((nΣx^2 - (Σx)^2)(nΣy^2 - (Σy)^2)) 
n -> number of data points 
x -> daily sentiment score of news articles 
y -> daily return of the 
