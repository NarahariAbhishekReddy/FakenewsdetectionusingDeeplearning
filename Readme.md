

<html>
<head>
  <h1> Fraudulent news detection using deep learning</h1>
 </head>
 <body>
 <p>
Name: Abhishek Reddy Narahari</br> 

Email: anvcy@umsystem.edu</br>
<p> 
<b> Introduction</b></br>
With the increase in usage of social media all around the world, It has become simple for anyone to publish news/articles through their own pages or a specified social media channel. Therefore, with the true news, fraudulent news has also become more popular</br>
</p>
<p>
  <b> our approach to the problem</b></br>
  In this project, our major focus is to discriminate the fake news among a set of news articles and determine the articles that contain misleading information. In order to achieve our goal, we would make use of machine learning and deep learning techniques  that provide an possible approach to discriminate between true and fake news</br>
  </p>
  <p> <b>Dataset preprocessing</b></br>
We are using fake,true and news dataset in our model. We are splitting the different types of news articles present in our dataset to true and fake . There are different categories like click and other</br>
we are even balancing the dataset and we are using Word2Vec model for performing word embedding so that it maps the textual data to vectors of numeric values</br>
</p>
  
  <p> <b>CNN MODEL</b></br>
  We are using a functional CNN model since we want to share the output of one layer as an input to the other layer</br>
We are using input layers, hidden layers, embedding layer , pooling layers, flattening layer and dense layers in our model</br>
In the final classification layer we are using 1 as number of neurons. Since we want to specify whether the given text is true or fake</p>
<p> <b>Logistic Model</b></br>
 We are using logistic regression to find whether the given news is fake or legit since logistic regression can be used for classification. We found out that our machine learning model's accuracy is better than that of deep learning</br>
 </p>
 <p><b> UI Design</b>
  We have created a simple web  application using flask. Flask lets us to connect our fornt-end html with our model so that we can create an application</br>
  We designed a simple webpage that accepts the content/news/article and return with the classified result which could be True or False.</br>

We created the webpage using HTML5 and CSS and Flask. Flask is a framework that helps us to build web applications and gives us the necessary tools and libraries.</br>

By using the saved model (CNN), we predict the class of the text/news/articles and send the results back to the webpage.</br>

Conv1d is used for classification in our case.</br>
</p>
</body> 
</html>
