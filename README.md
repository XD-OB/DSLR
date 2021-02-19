# Harry Potter and a Data Scientist

### Subject PDF:
[project_pdf!](https://github.com/XD-OB/DSLR/blob/master/ressources/subject.en.pdf)

### Cook Book:
[Cook_book!](https://github.com/XD-OB/DSLR/blob/master/ressources/nootboot.ipynb)

### DSLR (Datascience X Logistic Regression)

On no! Since its creation, the famous school of wizards, Hogwarts, had never known such an offense. The forces of evil have bewitched the Sorting Hat.
It no longer responds, and is unable to fulfill his role of sorting the students to the houses.

The new academic year is approaching. Gladly, the Professor McGonagall was able to take action in such a stressful situation, since it is impossible for Hogwarts not to welcome new students. . . She decided to call on you, a muggle "datascientist" who is able to create miracles with the tool which all muggles know how to use: a "computer".
Despite the intrinsic reluctance of many wizards, the director of the school welcomes you to his office to explain the situation. You are here because his informant discovered
that you are able to recreate a magic Sorting Hat using your muggle tools.

You explain to him that in order for your "muggle" tools to work, you need students data. Hesitantly, Professor McGonagall gives you a dusty spellbook. Fortunately for you, a simple "Digitalis!" and the book turned into a USB stick.

# Data Visualization
## Histogram
Which Hogwarts course has a homogeneous score distribution between all four houses ?

### python3 histogram.py -d
*   **-d**: Display all the histograms.
*   **-f**: Show histogram of the feature 'n'.

![Screen Shot 1](https://github.com/XD-OB/DSLR/blob/master/ressources/hist.JPG)

## Scatter plot
What are the two features that are similar ?

### python3 scatter_plot.py [-f1{n1}  -f2{n2}]
*   **-f1**: precise the first feature to use.
*   **-f2**: precise the second feature to use.
*   **n1** and **n2**: index of the features to use

![Screen Shot 2](https://github.com/XD-OB/DSLR/blob/master/ressources/scatter.JPG)


## Pair plot
### python3 pair_plot.py

![Screen Shot 3](https://github.com/XD-OB/DSLR/blob/master/ressources/pplot.JPG)


## Data Analysis:

Some features are homogenous or coherant with other ones, so there existance is not necessary for training the model and can give use= a complex hypothesis that will cause 'Overfitting' Our choice was to remove:
- **Arithmancy**: Homogenous
- **Astronomy**:  Similar to 'Defense Against the Dark Arts'
- **Transfiguration**:  Semi similar to 'History of Magic'
- **Potions**:  Semi homogenous
- **Care of Magical Creatures**:  Semi homogenous


# Training the model

### python3 logreg_train.py [-BGD | -SGD] <_train dataset_>
*   **-BGD**: Batch Gradient Descent Algorithm
*   **-SGD**: Stochastic Gradient Descent Algorithm

Output a file named: **./weights.csv** that contain the weights of the model.

In the end of the training the program output the: (using the training set)
- Accuracy of the model 98.06% 
- Confusion Matrix
- F1 Score
- Balanced Accuracy 98.71%


# Predict with the model

### python3 logreg_predict.py [-p] <_dataset_> <_weights_>
*   **-p**: Print the result with the students names in the stdout

Output a file named: **./houses.csv** that contain the Indexs and the predicted house affected to the students.


# Packages needed
### pip3 install pandas
### pip3 install matplotlib
### pip3 install seaborn

# Grade
- ✔️ 125   [ Accuracy: (training data: 98.06%) (evaluation data: 99%) ]
- Miss McGonagall is very happy for the results 🎉🥳

# Owners:
### Oussama Belouche 1337
### Anas Elouargui   1337
