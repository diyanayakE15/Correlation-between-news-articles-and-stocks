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
y -> daily return of the <br>


<b> Implementation</b> <br>
<b><i>Data Preparation:</i></b> 
Labeled and unlabeled data are prepared and saved as CSV files.
Stock data is generated and saved as a CSV file.<br>
<b><i>Model Training:</i></b>
Labeled data is loaded, and TF-IDF features are extracted from the text using a vectorizer.
An SVM model with a linear kernel is trained on the labeled data.<br>
<b><i>Sentiment Analysis:</i></b>
Unlabeled news articles are loaded.
The trained SVM model is used to classify the sentiment of the unlabeled articles, providing sentiment scores.
Sentiment scores are calculated based on predicted probabilities.<br>
<b><i>Stock Returns:</i></b>
Daily stock open and close prices are loaded.
Returns are calculated as the percentage change between open and close prices.<br>
<b><i>Correlation Analysis:</i></b>
Pearson correlation coefficient is calculated between stock returns and sentiment scores.
The correlation coefficient indicates the strength and direction of the linear relationship between the two variables.<br>

<b> Prerequisites</b><br>
Python 3.x<br>
Required Python libraries: pandas, sklearn, numpy<br>
Installation and Setup<br>

<b> Clone the repository:</b><br>
git clone https://github.com/diyanayakE15/Correlation-between-news-articles-and-stocks<br>

<b>Install the required dependencies:</b><br>
pip install pandas scikit-learn numpy<br>

<b> Run the Python script:</b><br>
python Correlation.py<br>

<b> Usage</b><br>
Ensure the labeled and unlabeled data files are in the correct format (CSV).<br>
Run the script to perform sentiment analysis on the unlabeled news articles and calculate stock returns.<br>
View the Pearson correlation coefficient to understand the relationship between sentiment scores and stock returns.
