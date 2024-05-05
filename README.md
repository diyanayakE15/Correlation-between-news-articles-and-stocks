<b> Introduction </b>
<br>The study provides evidence for the important role that news sentiment can play in 
predicting stock market movements, To test this hypothesis, machine 
learning algorithms are used to classify news articles as either positive or negative in 
sentiment, based on the content of the articles and then, analyze the correlation 
between the sentiment of the news articles and daily returns. This highlights the potential applications of machine learning algorithms in 
analyzing large amounts of textual data to identify patterns and correlations. <br>

<b> Terminologies </b> <br> 
<b><i>Labled data:</i></b> “labled data" refers to the labeled news articles for which the sentiments are already known and used for training a machine learning model. <br>
<b><i>Unlabled data:</i></b> "unlabled data" refers to unlabeled news articles, for which the model predicts the corresponding sentiments and correlates with stock market movements. <br>
<b><i>Daily sentiment score:</i></b> It is defined as the difference between the number of positive 
and negative news articles.  <br>
<b><i>Positive and negative articles:</i></b> Positive and negative articles refer to news articles that 
contain language that is generally associated with positive or negative sentiment or 
emotion. <br>
<b><i>Returns:</i></b> here, returns refers to stock returns that is used to retrieve daily returns for 
the Shanghai Composite Index. <br>
<br>

<b> Steps Involved </b><br>
STEP 1: <br>
To apply the formula of Pearson coefficient to the relationship between news 
sentiment and stock market returns, the daily sentiment 
score is first calculated t. <br>
Sentiment Score = p-n 
p-> no. of positive news articles 
n-> no. of negative news articles
<br>
STEP 2: <br>
Then, the daily return from the stocks are calculated
daily return = (price today - price yesterday) / price yesterday <br>
STEP 3: <br>
Then, the sentiment score and daily return are 
used as  two variables to calculate the Pearson correlation coefficient. 
r = (nΣxy - ΣxΣy) / sqrt((nΣx^2 - (Σx)^2)(nΣy^2 - (Σy)^2)) 
n -> number of data points 
x -> daily sentiment score of news articles 
y -> daily return of the 
