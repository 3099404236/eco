# Chapter 3: Learning to Use Regression Analysis

**Pages:** 85-111

---

65
3.1  Steps in Applied Regression Analysis
3.2  Using Regression Analysis to Pick Restaurant Locations
3.3  Dummy Variables
3.4  Summary and Exercises
3.5  Appendix: Econometric Lab #2
Learning to Use 
­Regression Analysis
From a quick reading of Chapter 2, it’d be easy to conclude that regression 
analysis is little more than the mechanical application of a set of equations 
to a sample of data. Such a notion would be similar to deciding that all that 
matters in golf is hitting the ball well. Golfers will tell you that it does little 
good to hit the ball well if you have used the wrong club or have hit the ball 
toward a trap, tree, or pond. Similarly, experienced econometricians spend 
much less time thinking about the OLS estimation of an equation than they 
do about a number of other factors. Our goal in this chapter is to introduce 
some of these “real-world” concerns.
The first section, an overview of the six steps typically taken in applied 
regression analysis, is the most important in the chapter. We believe that 
the ability to learn and understand a specific topic, like OLS estimation, is 
enhanced if the reader has a clear vision of the role that the specific topic 
plays in the overall framework of regression analysis. In addition, the six 
steps make it hard to miss the crucial function of theory in the development 
of sound econometric research.
This is followed by a complete example of how to use the six steps in 
applied regression: a location analysis for the “Woody’s” restaurant chain 
that is based on actual company data and to which we will return in future 
chapters to apply new ideas and tests. The chapter concludes with a discus-
sion of dummy variables and econometric lab #2.
Chapter 3


66
Chapter 3  Learning to Use ­Regression Analysis
3.1   Steps in Applied Regression Analysis
Although there are no hard and fast rules for conducting econometric 
research, most investigators commonly follow a standard method for applied 
regression analysis. The relative emphasis and effort expended on each step 
will vary, but normally all the steps are necessary for successful research. Note 
that we don’t discuss the selection of the dependent variable; this choice is 
determined by the purpose of the research. We’ll cover choosing a dependent 
variable in Chapter 11. Once a dependent variable is chosen, however, it’s 
logical to follow these six steps in applied regression analysis.
	1.	 Review the literature and develop the theoretical model.
	2.	 Specify the model: Select the independent variables and the  
functional form.
	3.	 Hypothesize the expected signs of the coefficients.
	4.	 Collect the data. Inspect and clean the data.
	5.	 Estimate and evaluate the equation.
	6.	 Document the results.
The purpose of suggesting these steps is not to discourage the use of innova-
tive or unusual approaches but rather to develop in the reader a sense of how 
regression ordinarily is done by professional economists and business analysts.
Step 1: Review the Literature and Develop the Theoretical Model
The first step in any applied research is to get a good theoretical grasp of the 
topic to be studied. That’s right: the best data analysts don’t start with data, but 
with theory! This is because many econometric decisions, ranging from which 
variables to include to which functional form to employ, are determined by the 
underlying theoretical model. It’s virtually impossible to build a good econo-
metric model without a solid understanding of the topic you’re studying.
For most topics, this means that it’s smart to review the scholarly literature 
before doing anything else. If a professor has investigated the theory behind 
your topic, you want to know about it. If other researchers have estimated 
equations for your dependent variable, you might want to apply one of 
their models to your data set. On the other hand, if you disagree with the 
approach of previous authors, you might want to head off in a new direction. 
In either case, you shouldn’t have to “reinvent the wheel.” You should start 


67
  Steps in Applied Regression Analysis
your investigation where earlier researchers left off. Any academic paper on 
an empirical topic should begin with a summary of the extent and quality of 
previous research.
The most convenient approaches to reviewing the literature are to obtain 
several recent issues of the Journal of Economic Literature or a business-oriented 
publication of abstracts, or to run an Internet search or an EconLit search1 on 
your topic. Using these resources, find and read several recent articles on your 
topic. Pay attention to the bibliographies of these articles. If an older article is 
cited by a number of current authors, or if its title hits your topic on the head, 
trace back through the literature and find this article as well. We’ll have more 
advice on reviewing the literature in Chapter 11.
In some cases, a topic will be so new or so obscure that you won’t be able 
to find any articles on it. What then? We recommend two possible strategies. 
First, try to transfer theory from a similar topic to yours. For example, if you’re 
trying to build a model of the demand for a new product, read articles that 
analyze the demand for similar, existing products. Second, if all else fails, 
contact someone who works in the field you’re investigating. For example, 
if you’re building a model of housing in an unfamiliar city, call a real estate 
agent who works there.
Step 2: Specify the Model: Select the Independent Variables  
and the Functional Form
The most important step in applied regression analysis is the specification of 
the theoretical regression model. After selecting the dependent variable, the 
specification of a model involves choosing the following components:
1.	 the independent variables and how they should be measured,
2.	 the functional (mathematical) form of the variables, and
3.	 the properties of the stochastic error term.
A regression equation is specified when each of these elements has been 
treated appropriately. We’ll discuss the details of these specification decisions 
in Chapters 6, 7, and 4, respectively.
Each of the elements of specification is determined primarily on the 
basis of economic theory. A mistake in any of the three elements results in a 
1. EconLit is an electronic bibliography of economics literature. EconLit contains abstracts, 
reviews, indexing, and links to full-text articles in economics journals. In addition, it abstracts 
books and indexes articles in books, working papers series, and dissertations. EconLit is ­available 
at libraries and on university websites throughout the world. For more, go to www.­EconLit.org.


68
Chapter 3  Learning to Use ­Regression Analysis
specification error. Of all the kinds of mistakes that can be made in applied 
regression analysis, specification error is usually the most disastrous to the 
validity of the estimated equation. Thus, the more attention paid to eco-
nomic theory at the beginning of a project, the more satisfying the regression 
results are likely to be.
The emphasis in this text is on estimating behavioral equations, those 
that describe the behavior of economic entities. We focus on selecting inde-
pendent variables based on the economic theory concerning that behavior. 
An explanatory variable is chosen because it is a theoretical determinant of 
the dependent variable; it is expected to explain at least part of the varia-
tion in the dependent variable. Recall that regression gives evidence but does 
not prove economic causality. Just as an example does not prove the rule, a 
regression result does not prove the theory.
There are dangers in specifying the wrong independent variables. Our 
goal should be to specify only relevant explanatory variables, those expected 
theoretically to assert a substantive influence on the dependent variable. Vari-
ables suspected of having little effect should be excluded unless their possible 
impact on the dependent variable is of some particular (e.g., policy) interest.
For example, an equation that explains the quantity demanded of a con-
sumption good might use the price of the product and consumer income or 
wealth as likely variables. Theory also indicates that complementary and sub-
stitute goods are important. Therefore, you might decide to include the prices 
of complements and substitutes, but which complements and substitutes? 
Of course, selection of the closest complements and/or substitutes is appro-
priate, but how far should you go? The choice must be based on theoretical 
judgment, and such judgments are often quite subjective.
When researchers decide, for example, that the prices of only two other 
goods need to be included, they are said to impose their priors (i.e., previous 
theoretical belief) or their working hypotheses on the regression equation. 
Imposition of such priors is a common practice that determines the number 
and kind of hypotheses that the regression equation has to test. The danger 
is that a prior may be wrong and could diminish the usefulness of the esti-
mated regression equation. Each of the priors therefore should be explained 
and justified in detail.
Step 3:  Hypothesize the Expected Signs of the Coefficients
Once the variables have been selected, it’s important to hypothesize the 
expected signs of the slope coefficients before you collect any data. In many 
cases, the basic theory is general knowledge, so you don’t need to discuss the 
reasons for the expected sign. However, if any doubt surrounds the choice of 


69
  Steps in Applied Regression Analysis
an expected sign, then you should document the opposing theories and your 
reasons for hypothesizing a positive or a negative slope2 coefficient.
For example, suppose that you’re interested in the impact of class size on 
student learning at the elementary level in the United States. A reasonable 
dependent variable 1Y2 might be the student score on a test of grammar, 
math, and science. Likely independent variables would include the income 
level of the student’s family 1X12 and the size (in students per teacher) of the 
student’s class 1X22.
	
   +    
- 	
	
Y = β0 + β1X1 + β2X2 + e	
(3.1)
The signs above the coefficients in Equation 3.1 indicate the hypothesized 
sign of that particular coefficient. Take another look at the equation. Do you 
agree with the hypothesized signs? The expectation that higher income will 
improve test scores (holding constant class size) seems reasonable because of 
the extra learning opportunities that the money might allow, but the hypoth-
esized sign for β2 is a little trickier. Do you agree that it should be negative?
Step 4:  Collect the Data. Inspect and Clean the Data
Obtaining an original data set and properly preparing it for regression is a 
surprisingly difficult task. This step entails more than a mechanical recording 
of data, because the type and size of the sample also must be chosen.
A general rule regarding sample size is “the more observations the better,” 
as long as the observations are from the same general population. Ordinarily, 
researchers take all the roughly comparable observations that are readily 
available. In regression analysis, all the variables must have the same number 
of observations. They also should have the same frequency (monthly, quar-
terly, annual, etc.) and time period. Often, the frequency selected is deter-
mined by the availability of data.
The reason there should be as many observations as possible concerns 
the statistical concept of degrees of freedom first mentioned in Section 2.4. 
Consider fitting a straight line to two points on an X, Y coordinate system 
as in Figure 3.1. Such an exercise can be done mathematically without error. 
Both points lie on the line, so there is no estimation of the coefficients 
involved. The two points determine the two parameters, the intercept and the 
slope, precisely. Estimation takes place only when a straight line is fitted to 
2. Note that while we hypothesize signs for the slope coefficients, we don’t hypothesize an 
expected sign for the intercept. We’ll explain why in Section 7.1.


70
Chapter 3  Learning to Use ­Regression Analysis
three or more points that were generated by some process that is not exact. 
The excess of the number of observations (three) over the number of coeffi-
cients to be estimated (in this case two, the intercept and slope) is the degrees 
of freedom.3 All that is necessary for estimation is a single degree of freedom, 
as in Figure 3.2, but the more degrees of freedom there are, the better. This is 
because when the number of degrees of freedom is large, every positive error 
is likely to be balanced by a negative error. When degrees of freedom are low, 
the random element is likely to fail to provide such offsetting observations. 
For example, the more a coin is flipped, the more likely it is that the observed 
proportion of heads will reflect the true probability of 0.5.
Another area of concern has to do with the units of measurement of the 
variables. Does it matter if a variable is measured in dollars or thousands of 
dollars? Does it matter if the measured variable differs consistently from the 
true variable by 10 units? Interestingly, such changes don’t matter in terms 
of regression analysis except in interpreting the scale of the coefficients. All 
conclusions about signs, significance, and economic theory are independent 
of units of measurement. For example, it makes little difference whether an 
independent variable is measured in dollars or thousands of dollars. The 
3. Throughout the text, we will calculate the number of degrees of freedom (d.f.) in a regres-
sion equation as d.f. = (N - K - 1), where K is the number of independent variables in the 
equation. Equivalently, some authors will set K′ = K + 1 and define d.f. = (N - K′). Since 
K′ equals the number of independent variables plus 1 (for the constant), it equals the number 
of coefficients to be estimated in the regression.
Y
0
X
Figure 3.1  Mathematical Fit of a Line to Two Points
If there are only two points in a data set, as in Figure 3.1, a straight line can be fitted to 
those points mathematically without error, because two points completely determine a 
straight line.


71
  Steps in Applied Regression Analysis
constant term and measures of overall fit remain unchanged. Such a multipli-
cative factor does change the slope coefficient, but only by the exact amount 
necessary to compensate for the change in the units of measurement of the 
independent variable. Similarly, a constant factor added to a variable alters 
only the intercept term without changing the slope coefficient itself.
The final step before estimating your equation is to inspect and clean the 
data. You should make it a point always to look over your data set to see if 
you can find any errors. The reason is obvious: why bother using sophisti-
cated regression analysis if your data are incorrect?
To inspect the data, obtain a plot (graph) of the data and look for outliers. 
An outlier is an observation that lies outside the range of the rest of the observa-
tions, and looking for outliers is an easy way to find data entry errors. In addi-
tion, it’s a good habit to look at the mean, maximum, and minimum of each 
variable and then think about possible inconsistencies in the data. Are any 
observations impossible or unrealistic? Did GDP double in one year? Does a 
student have a 7.0 GPA on a 4.0 scale? Is consumption negative?
Typically, the data can be cleaned of these errors by replacing an incorrect 
number with the correct one. In extremely rare circumstances, an observation 
can be dropped from the sample, but only if the correct number can’t be found 
or if that particular observation clearly isn’t from the same population as the rest 
of the sample. Be careful! The mere existence of an outlier is not a justification 
for dropping that observation from the sample. A regression needs to be able 
to explain all the observations in a sample, not just the well-behaved ones. For 
more on the details of data collection, see Sections 11.2 and 11.3. For more on 
generating your own data through an economic experiment, see Section 16.1.
Y
0
X
Figure 3.2  Statistical Fit of a Line to Three Points
If there are three (or more) points in a data set, as in Figure 3.2, then the line must almost 
always be fitted to the points statistically, using the estimation procedures of ­Section 2.1.


72
Chapter 3  Learning to Use ­Regression Analysis
Step 5:  Estimate and Evaluate the Equation
Believe it or not, it can take months to complete steps 1–4 for a regression 
equation, but a computer program like Stata or EViews can estimate that equa-
tion in less than a second! Typically, estimation is done using OLS, as discussed 
in Section 2.1, but if another estimation technique is used, the reasons for that 
alternative technique should be carefully explained and evaluated.
You might think that once your equation has been estimated, your work is 
finished, but that’s hardly the case. Instead, you need to evaluate your results 
in a variety of ways. How well did the equation fit the data? Were the signs 
and magnitudes of the estimated coefficients what you expected? Most of the 
rest of this book is concerned with the evaluation of estimated econometric 
equations, and beginning researchers should be prepared to spend a consid-
erable amount of time doing this evaluation.
Once this evaluation is complete, don’t automatically go to step 6. Regres-
sion results are rarely what one expects, and additional model development 
often is required. For example, an evaluation of your results might indicate 
that your equation is missing an important variable. In such a case, you’d 
go back to step 1 to review the literature and add the appropriate variable 
to your equation. You’d then go through each of the steps in order until you 
had estimated your new specification in step 5. You’d move on to step 6 only 
if you were satisfied with your estimated equation. Don’t be too quick to 
make such adjustments, however, because we don’t want to adjust the theory 
merely to fit the data. A researcher has to walk a fine line between making 
appropriate changes and avoiding inappropriate ones, and making these 
choices is one of the artistic elements of applied econometrics.
Finally, it’s often worthwhile to estimate additional specifications of an 
equation in order to see how stable your observed results are. This approach, 
called sensitivity analysis, will be discussed in Section 6.4.
Step 6:  Document the Results
A standard format usually is used to present estimated regression results:
	
Yni = 103.40 + 6.38Xi	
	
 (0.88)	
(3.2)
	
 t = 7.22	
	
       N = 20 R  2 = .73	
The number in parentheses is the estimated standard error of the estimated 
coefficient, and the t-value is the one used to test the hypothesis that the 
true value of the coefficient is different from zero. These and other measures 


73
  Using Regression Analysis to Pick Restaurant ­Locations
of the quality of the regression will be discussed in later chapters.4 What is 
important to note is that the documentation of regression results using an 
easily understood format is considered part of the analysis itself. For time-
series data sets, the documentation also includes the frequency (e.g., quarterly 
or annual) and the time period of the data.
One of the important parts of the documentation is the explanation of the 
model, the assumptions, and the procedures and data used. The written doc-
umentation must contain enough information so that the entire study could 
be replicated by others.5 Unless the variables have been defined in a glossary 
or table, short definitions should be presented along with the equations. If 
there is a series of estimated regression equations, then tables should provide 
the relevant information for each equation. All data manipulations as well 
as data sources should be documented fully. When there is much to explain, 
this documentation usually is relegated to a data appendix. If the data are not 
available generally or are available only after computation, the data set itself 
might be included in this appendix.
3.2   Using Regression Analysis to Pick 
Restaurant ­Locations
To solidify your understanding of the six basic steps of applied regression 
analysis, let’s work through a complete regression example. Suppose that 
you’ve been hired to determine the best location for the next Woody’s res-
taurant, where Woody’s is a moderately priced, 24-hour, family restaurant 
chain.6 You decide to build a regression model to explain the gross sales vol-
ume at each of the restaurants in the chain as a function of various descrip-
tors of the location of that branch. If you can come up with a sound equation 
to explain gross sales as a function of location, then you can use this equa-
tion to help Woody’s decide where to build their newest eatery. Given data on 
4. The standard error of the coefficient is discussed in more detail in Section 4.2; the t-value 
is developed in Section 5.2. 
5. For example, the Journal of Money, Credit, and Banking and the American Economic Review have 
requested authors to submit their actual data sets so that regression results can be verified. See 
W. G. Dewald et al., “Replication in Empirical Economics,” American Economic Review, Vol. 76, 
No. 4, pp. 587–603 and Daniel S. Hamermesh, “Replication in Economics,” NBER Working 
Paper 13026, April 2007.
6. The data in this example are real (they’re from a sample of 33 Denny’s restaurants in Southern 
California), but the number of independent variables considered is much smaller than was 
used in the actual research. Datafile = WOODY3.


74
Chapter 3  Learning to Use ­Regression Analysis
land costs, building costs, and local building and restaurant municipal codes, 
the owners of Woody’s will be able to make an informed decision.
1.	 Review the literature and develop the theoretical model. You do some reading 
about the restaurant industry, but your review of the literature consists 
mainly of talking to various experts within the firm. They give you some 
good ideas about the attributes of a successful Woody’s location. The ex-
perts tell you that all of the chain’s restaurants are identical (indeed, this 
is sometimes a criticism of the chain) and that all the locations are in 
what might be called “suburban, retail, or residential” environments (as 
distinguished from central cities or rural areas, for example). Because of 
this, you realize that many of the reasons that might help explain differ-
ences in sales volume in other chains do not apply in this case because 
all the Woody’s locations are similar. (If you were comparing Woody’s to 
another chain, such variables might be appropriate.)
In addition, discussions with the people in the Woody’s strategic plan-
ning department convince you that price differentials and consumption 
differences between locations are not as important as the number of cus-
tomers a particular location attracts. This causes you concern for a while 
because the variable you had planned to study originally, gross sales vol-
ume, would vary as prices changed between locations. Since your com-
pany controls these prices, you feel that you would rather have an esti-
mate of the “potential” for such sales. As a result, you decide to specify 
your dependent variable as the number of customers served (measured 
by the number of checks or bills that the servers handed out) in a given 
location in the most recent year for which complete data are available.
2.	 Specify the model: Select the independent variables and the functional form. 
Your discussions lead to a number of suggested variables. After a while, 
you realize that there are three major determinants of sales (customers) 
on which virtually everyone agrees. These are the number of people 
who live near the location, the general income level of the location, 
and the number of direct competitors close to the location. In addi-
tion, there are two other good suggestions for potential explanatory 
variables. These are the number of cars passing the location per day and 
the number of months that the particular restaurant has been open. 
After some serious consideration of your alternatives, you decide not 
to include the last possibilities. All the locations have been open long 
enough to have achieved a stable clientele. In addition, it would be very 
expensive to collect data on the number of passing cars for all the loca-
tions. Should population prove to be a poor measure of the available 
customers in a location, you’ll have to decide whether to ask your boss 
for the money to collect complete traffic data.


75
  Using Regression Analysis to Pick Restaurant ­Locations
The exact definitions of the independent variables you decide to 
include are:
N = Competition:	the number of direct market competitors within a 
two-mile radius of the Woody’s location
P = Population:	
the number of people living within a three-mile 
radius of the Woody’s location
I  = Income:	
the average household income of the population 
measured in variable P
Since we have yet to develop any functional forms other than a linear 
functional form and a typical stochastic error term, that’s what you 
decide to use.
3.	 Hypothesize the expected signs of the coefficients. After thinking about 
which variables to include, you expect hypothesizing signs will be easy. 
For two of the variables, you’re right. Everyone expects that the more 
competition there is, the fewer customers (holding constant the popu-
lation and income of an area) there will be, and also that the more 
people there are who live near a particular restaurant, the more cus-
tomers (holding constant the competition and income) the restaurant 
will have. You expect that the greater the income is in a particular area, 
the more people will choose to eat in a family restaurant. However, 
people in especially high-income areas might want to eat in a restau-
rant that has more “atmosphere” than a family restaurant like Woody’s. 
As a result, you worry that the income variable might be only weakly 
positive in its impact. To sum, you expect:
	
       -         +        +?
	
Yi = β0 + βNNi + βPPi + βIIi + ei	
(3.3)
where the signs above the coefficients indicate the expected impact of 
that particular independent variable on the dependent variable, hold-
ing constant the other two explanatory variables, and ei is a typical sto-
chastic error term.
4.	 Collect the data. Inspect and clean the data. You want to include every 
local restaurant in the Woody’s chain in your study, and, after some 
effort, you come up with data for your dependent variable and your 
independent variables for all 33 locations. You inspect the data, and 
you’re confident that the quality of your data is excellent for three rea-
sons: each manager measured each variable identically, you’ve included 
each restaurant in the sample, and all the information is from the same 
year. [The data set is included in this section, along with a sample com-
puter output for the regression estimated by Stata (Tables 3.1 and 3.2).]


76
Chapter 3  Learning to Use ­Regression Analysis
Table 3.1  Data for the Woody’s Restaurant Example (Using the Stata Program)
Y
N
P
I
1.
107919
3
65044
13240
2.
118866
5
101376
22554
3.
98579
7
124989
16916
4.
122015
2
55249
20967
5.
152827
3
73775
19576
6.
91259
5
48484
15039
7.
123550
8
138809
21857
8.
160931
2
50244
26435
9.
98496
6
104300
24024
10.
108052
2
37852
14987
11.
144788
3
66921
30902
12.
164571
4
166332
31573
13.
105564
3
61951
19001
14.
102568
5
100441
20058
15.
103342
2
39462
16194
16.
127030
5
139900
21384
17.
166755
6
171740
18800
18.
125343
6
149894
15289
19.
121886
3
57386
16702
20.
134594
6
185105
19093
21.
152937
3
114520
26502
22.
109622
3
52933
18760
23.
149884
5
203500
33242
24.
98388
4
39334
14988
25.
140791
3
95120
18505
26.
101260
3
49200
16839
27.
139517
4
113566
28915
28.
115236
9
194125
19033
29.
136749
7
233844
19200
30.
105067
7
83416
22833
31.
136872
6
183953
14409
32.
117146
3
60457
20307
33.
163538
2
65065
20111
(obs=33)
Y
N
P
I
Y
1.0000
N
-0.1442
1.0000
P
0.3926
0.7263
1.0000
I
0.5370
-0.0315
0.2452
1.0000


77
  Using Regression Analysis to Pick Restaurant ­Locations
Table 3.2  Actual Computer Output (Using the Stata Program)
Number of obs
=
33
F(     3,     29)
=
15.65
Prob 7 F
= 0.0000
R–squared
= 0.6182
Adj R–squared
= 0.5787
Root MSE
=
14543
Y
Coef.
Std. Err.
t
p 7  t
[95% Conf.
Interval]
N
-9074.674
2052.674
-4.42
0.000
-13272.86
-4876.485
P
.3546684
.0726808
4.88
0.000
.2060195
.5033172
I
1.287923
.5432938
2.37
0.025
.1767628
2.399084
_cons
102192.4
12799.83
7.98
0.000
76013.84
128371
Source
SS
df
MS
Model
9.9289e + 09
3
3.3096e + 09
Residual
6.1333e + 09
29
211492485
Total
1.6062e + 10
32
501943246
Y
Yhat
residuals
1.
107919
115089.6
-7170.56
2.
118866
121821.7
-2955.74
3.
98579
104785.9
-6206.864
4.
122015
130642
-8627.041
5.
152827
126346.5
26480.55
6.
91259
93383.88
-2124.877
7.
123550
106976.3
16573.66
8.
160931
135909.3
25021.71
9.
98496
115677.4
-17181.36
10.
108052
116770.1
-8718.094
11.
144788
138502.6
6285.425
12.
164571
165550
-979.0342
13.
105564
121412.3
-15848.3
14.
102568
118275.5
-15707.47
15.
103342
118895.6
-15553.63
16.
127030
133978.1
-6948.114
17.
166755
132868.1
33886.91
18.
125343
120598.1
4744.898
19.
121886
116832.3
5053.7
20.
134594
137985.6
-3391.591
21.
152937
149717.6
3219.428
22.
109622
117903.5
-8281.508
23.
149884
171807.2
-21923.22
24.
98388
99147.65
-759.6514
25.
140791
132537.5
8253.518
26.
101260
114105.4
-12845.43
27.
139517
143412.3
-3895.303
28.
115236
113883.4
1352.599
29.
136749
146334.9
-9585.905
30.
105067
97661.88
7405.122
31.
136872
131544.4
5327.621
32.
117146
122564.5
-5418.45
33.
163538
133021
30517


78
Chapter 3  Learning to Use ­Regression Analysis
5.	 Estimate and evaluate the equation. You take the data set and enter it into 
the computer. You then run an OLS regression on the data, but you do 
so only after thinking through your model once again to see if there are 
hints that you’ve made theoretical mistakes. You end up admitting that 
although you cannot be sure you are right, you’ve done the best you 
can, so you estimate the equation, obtaining:
	
Yni = 102,192 - 9075Ni +  0.355Pi +  1.288Ii	
(3.4)
	
                          (2053)      (0.073)     (0.543)
	
                   t = -4.42        4.88          2.37
	
           N = 33 R  2 = .579
This equation satisfies your needs in the short run. In particular, the 
estimated coefficients in the equation have the signs you expected. The 
overall fit, although not outstanding, seems reasonable for such a di-
verse group of locations. To predict Y, you obtain the values of N, P, and 
I for each potential new location and then plug them into Equation 3.4. 
Other things being equal, the higher the predicted Y, the better the loca-
tion from Woody’s point of view.
6.	 Document the results. The results summarized in Equation 3.4 meet our 
documentation requirements. (Note that we include the standard er-
rors of the estimated coefficients and t-values7 for completeness, even 
though we won’t make use of them until Chapter 5.) However, it’s not 
easy for a beginning researcher to wade through a computer’s regres-
sion output to find all the numbers required for documentation. You’ll 
probably have an easier time reading your own computer system’s 
printout if you take the time to “walk through” the sample computer 
output for the Woody’s model in Tables 3.1–3.2. This sample output 
was produced by the Stata computer program, but it’s similar to those 
produced by EViews, SAS, SHAZAM, TSP, and others.
7. Throughout the text, the number in parentheses below a coefficient estimate typically will 
be the standard error of that estimated coefficient. Some authors put the t-value in parentheses, 
though, so be alert when reading journal articles or other books.
The first items listed are the actual data. These are followed by the 
simple correlation coefficients between all pairs of variables in the data 
set. Next comes a listing of the estimated coefficients, their estimated 
standard errors, and the associated t-values, and follows with R2, R2, 
RSS, the F-ratio, and other items that we will explain in later chap-
ters. Finally, we have a listing of the observed Ys, the predicted Ys, and 


79
  Dummy Variables
the ­residuals for each observation. Numbers followed by “e + 06” or 
“e - 01” are expressed in a scientific notation indicating that the printed 
decimal point should be moved six places to the right or one place to 
the left, respectively.
In future sections, we’ll return to this example in order to apply vari-
ous tests and ideas as we learn them.
3.3   Dummy Variables
Some concepts (for example, gender) might seem impossible to include in 
an equation because they’re inherently qualitative in nature and can’t be 
expressed as a number. Luckily, such concepts can be quantified by using 
dummy (or binary) variables. A dummy variable takes on the value of one 
or zero (and only those values) depending on whether a specified condition 
is met.
As an illustration of a dummy variable, suppose that Yi represents the 
salary of the ith high school teacher and that salaries depend primarily on 
the experience of the teacher and the type of degree that the teacher has 
earned. All teachers have a B.A., but some also have a graduate degree like an 
M.A. An equation representing the relationship between earnings and these 
variables would be:
+        +
	
Yi = β0 + β1Xi + β2Di + ei	
(3.5)
where:	
Yi = the income of the ith teacher in dollars
	
 Xi = the number of years of teaching experience of the ith 
teacher
	
Di = e 1 if the ith teacher has a graduate degree
0 otherwise
The variable Di takes on values of only zero or one, so Di is called a 
dummy variable, or just a “dummy.” Needless to say, the term has generated 
many a pun. In this case, the dummy variable represents the condition of 
having a graduate degree. The coefficient β2 indicates the additional salary 
that can be attributed to having a graduate degree, holding teaching experi-
ence constant.
Since more experience and a graduate degree can be expected to increase 
the earnings of teachers, we expect positive coefficients for both variables, 
as indicated by the signs above the coefficients in Equation 3.5. Think 
for a second about what those expected signs would be if we had instead 


80
Chapter 3  Learning to Use ­Regression Analysis
defined Di to be equal to one if the ith teacher has no graduate degree and 
equal to zero otherwise. This change shouldn’t impact the expected sign of 
β1, but do you see that the expected sign of β2 now would be negative?8
As can be seen in Figure 3.3, the dummy changes the intercept depending 
on the value of D, but the slopes remain constant no matter what value D 
takes. This is true even if we define the dummy variable “reversed” and have 
D = 0 if the particular condition is met and D = 1 otherwise. The slopes 
still remain constant.
Note that in this example only one dummy variable is used even though 
there were two conditions. This is because one fewer dummy variable is con-
structed than conditions. The event not explicitly represented by a dummy 
variable, the omitted condition, forms the basis against which the included 
conditions are compared. Thus, for dual situations only one dummy variable 
is entered as an independent variable; the coefficient is interpreted as the 
effect of the included condition relative to the omitted condition. Be careful 
Y
0
X
Di = 0
d2
d0
d0 + d2
(d2 7 0)
Di = 1
Both Slopes = d1
Yi = d0 + d1Xi + d2Di
Figure 3.3  A Dummy Variable
If a dummy (β2Di) is added to an equation, a graph of the equation will have differ-
ent intercepts for the two qualitative conditions specified by the dummy variable. The 
difference between the two intercepts is β2. The slopes are constant with respect to the 
qualitative condition.
8. The constant term will change as well. 


81
  Dummy Variables
never to use two dummy variables to describe the two conditions. If you were 
to make this mistake, sometimes called a dummy variable trap, you’d have per-
fect multicollinearity (to be described in Section 8.1).
For another example of the meaning of the coefficient of a dummy vari-
able, let’s look at a study of the relationship between fraternity/sorority mem-
bership and grade point average (GPA). Most noneconometricians would 
approach this research problem by calculating the mean grades of fraternity/
sorority (so-called Greek) members and comparing them to the mean grades 
of nonmembers. However, such a technique would ignore the relationship 
that grades have to characteristics other than Greek membership.
Instead, we’d want to build a regression model that explains college GPA. 
Independent variables would include not only Greek membership but also 
other predictors of academic performance such as SAT scores and high school 
grades. Being a member of a social organization is a qualitative variable, 
however, so we’d have to create a dummy variable to represent fraternity or 
sorority membership quantitatively in a regression equation:
	
Di = •
 1 if the ith student is an active member
   of a fraternity or sorority
 0 otherwise
If we collect data from all the students in our class and estimate the equa-
tion implied in this example, we obtain:
	
CGi = 0.37 + 0.81HGi + 0.00001Si - 0.38Di	
(3.6)
	
R  2 = .45 N = 25
where:	
CGi = the cumulative college GPA (4-point scale) of the ith 
­student
	
HGi = the cumulative high school GPA (4-point scale) of the ith 
student
	
Si
 = the sum of the highest verbal and mathematics SAT scores 
earned by the ith student
The meaning of the estimated coefficient of Di in Equation 3.6 is very spe-
cific. Stop for a second and figure it out for yourself. What is it? The estimate 
that βn D = -0.38 means that, for this sample, the GPA of fraternity/sorority 
members is 0.38 lower than for nonmembers, holding SATs and high school 
GPA constant. Thus, Greek members are doing about a third of a grade worse 
than otherwise might be expected. To understand this example better, try 
using Equation 3.6 to predict your own GPA; how close does it come?
h


82
Chapter 3  Learning to Use ­Regression Analysis
Before you rush out and quit whatever social organization you’re in, how-
ever, note that this sample is quite small and that we’ve surely omitted some 
important determinants of academic success from the equation. As a result, 
we shouldn’t be too quick to conclude that Greeks are dummies.
Up to this point, we’ve used dummy variables to represent only those 
qualitative variables that have exactly two possibilities (such as gender). What 
about situations where a qualitative variable has three or more alternatives? For 
example, in our study of the salaries of high school teachers in Equation 3.5, 
what if we learn that some of the teachers have Ph.D.s? We now need to be 
able to distinguish teachers whose highest degree is a Ph.D. from teachers 
whose highest degree is an M.A. from teachers whose highest degree is a B.A. 
What can we do?
Well, the answer certainly isn’t to define a variable such that Ph.D. = 2, 
M.A. = 1, and B.A. = 0, because we have no reason to think that the impact 
of having a Ph.D. is exactly twice that of having an M.A. If not that, then 
what?
The answer is to create one fewer dummy variable than there are pos-
sibilities (conditions) and to use each dummy to represent only one of the 
possible conditions. In the high school salary case, you’d create two dummy 
variables to represent the three conditions, for example:
PHDi = e 1 if the ith teacher’s highest degree is a Ph.D.
0 otherwise
and
MAi
 = e 1 if the ith teacher’s highest degree is an M.A.
0 otherwise
The omitted condition (when a B.A. is the highest degree) is represented by 
having both dummies equal to 0. This way you can measure the impact of 
each degree independently without having to link the impacts of having an 
M.A. and a Ph.D.
Thus Equation 3.5 now would look like this:
	
+	
+	
?
	
Yi = β0 + β1Xi + β2PHDi + β3MAi + ei	
(3.7)
However, be careful! The interpretation of the coefficients when there 
are two or more related dummy variables is tricky. The coefficient tells you 
the increase in the dependent variable caused by the condition being met 


83
  Summary
compared to the omitted condition. Thus β3 measures the impact of having the 
highest degree be an M.A. (holding X and PHD constant) compared to the 
omitted condition, which is when the highest degree is a B.A. To make sure that 
you understand this, go back to Equation 3.7 and determine the expected 
sign of β3. Did you decide it should be positive? That’s right! We’d expect a 
high school teacher whose highest degree is an M.A. to have a higher salary 
than one whose highest degree is a B.A. (holding X and PHD constant).
A dummy variable that has only a single observation with a value of 
1 while the rest of the observations are 0 (or vice versa) is to be avoided 
unless the variable is required by theory. Such a one-time dummy acts merely 
to eliminate that observation from the data set, improving the fit artificially 
by setting the dummy’s coefficient equal to the residual for that observation. 
One would obtain exactly the same estimates of the other coefficients if that 
observation were deleted, but the deletion of an observation is rarely, if ever, 
appropriate.
While this is the end of the section, it’s not the end of our coverage of 
dummy variables. In Section 7.4, we’ll discuss slope dummy variables, and 
in Chapter 13 we’ll analyze what happens when the dependent variable is a 
dummy.
3.4   Summary
1.	
Six steps typically taken in applied regression analysis for a given 
dependent variable are:
a.	Review the literature and develop the theoretical model.
b.	Specify the model: Select the independent variables and the func-
tional form.
c.	 Hypothesize the expected signs of the coefficients.
d.	Collect the data. Inspect and clean the data.
e.	 Estimate and evaluate the equation.
f.	 Document the results.
2.	
A dummy variable takes on only the values of 1 or 0, depending on 
whether some condition is met. An example of a dummy variable 
would be X equals 1 if a particular individual is female and 0 if the 
person is male.


84
Chapter 3  Learning to Use ­Regression Analysis
Exercises
(The answers to the even-numberd exercises are in Appendix A.)
	 1.	 Write the meaning of each of the following terms without referring 
to the book (or your notes), and compare your definition with the 
version in the text for each:
a.	dummy variable (p. 79)
b.	omitted condition (p. 80)
c.	 six steps in applied regression analysis (p. 66)
d.	specification (p. 67)
e.	 specification error (p. 68)
	 2.	 Contrary to their name, dummy variables are not easy to understand 
without a little bit of practice:
a.	Specify a dummy variable that would allow you to distinguish 
between undergraduate students and graduate students in your 
econometrics class.
b.	Specify a regression equation to explain the grade (measured on 
a scale of 4.0) each student in your class received on his or her 
first econometrics test (Y) as a function of the student’s grade in a 
previous course in statistics (G), the number of hours the student 
studied for the test (H), and the dummy variable you created above 
(D). Are there other variables you would want to add? Explain.
c.	 What is the hypothesized sign of the coefficient of D? Does the sign 
depend on the exact way in which you defined D? (Hint: In par-
ticular, suppose that you had reversed the definitions of 1 and 0 in 
your answer to part a.) How?
d.	Suppose that you collected the data and ran the regression and 
found an estimated coefficient for D that had the expected sign 
and an absolute value of 0.5. What would this mean in real-world 
terms?
e.	 Suppose three of the students in your class are high school seniors 
who are taking econometrics as part of an accelerated study pro-
gram for especially talented youngsters. What’s the best way to use 
dummy variables to distinguish between the three types of stu-
dents in your class? Be specific as to the definition of the dummy 
variable(s) you’d use.


85
EXERCISES
	 3.	 Do liberal arts colleges pay economists more than they pay other 
professors? To find out, we looked at a sample of 2,929 small-college 
faculty members and built a model of their salaries that included a 
number of variables, four of which were:
Sni = 36,721 + 817Mi + 426Ai + 406Ri + 3539Ti + g	
(3.8)
           
12592    14562      1242      14582
             R2 = .77  N = 2929
	
	 where:	
Si = the salary of the ith college professor
	
	 	
Mi = a dummy variable equal to 1 if the ith professor is a 
male and 0 otherwise
	
	 	
Ai = a dummy variable equal to 1 if the ith professor is 
African American and 0 otherwise
	
	 	
Ri = the years in rank of the ith professor
	
	 	
Ti  = a dummy variable equal to 1 if the ith professor 
teaches economics and 0 otherwise
a.	Carefully explain the meaning of the estimated coefficient of M.
b.	The equation indicates that African Americans earn $426 more 
than members of other ethnic groups, holding constant the other 
variables in the equation. Does this coefficient have the sign you 
expected? Why or why not?
c.	 Is R a dummy variable? If not, what is it? Carefully explain the 
meaning of the coefficient of R. (Hint: A professor’s salary typically 
increases each year based on rank.)
d.	What’s your conclusion? Do economists earn more than other pro-
fessors at liberal arts colleges? Explain.
e.	 The fact that the equation ends with the notation “+ g” indicates 
that there were more than four independent variables in the equa-
tion. If you could add a variable to the equation, what would it be? 
Explain.
	 4.	 Use Stata or your own computer regression software to estimate Equa-
tion 3.4 using the data in Table 3.1. Can you get the same results?
	 5.	 The Graduate Record Examination (GRE) subject test in economics 
was a multiple-choice measure of knowledge and analytical ability in 
economics that was used mainly as an entrance criterion for students 
applying to Ph.D. programs in the “dismal science.” For years, critics 
claimed that the GRE, like the Scholastic Aptitude Test (SAT), was 
biased against women and some ethnic groups. To test the possibil-
ity that the GRE subject test in economics was biased against women, 


86
Chapter 3  Learning to Use ­Regression Analysis
Mary Hirschfeld, Robert Moore, and Eleanor Brown estimated the fol-
lowing equation (standard errors in parentheses):9
GREi = 172.4 + 39.7Gi + 78.9GPAi + 0.203SATMi + 0.110SAT  Vi
110.92    110.42     10.0712       10.0582
N = 149 R  2 = .46	
(3.9)
where:	
GREi  = the score of the ith student in the Graduate 
Record Examination subject test in economics
	
Gi     = a dummy variable equal to 1 if the ith student 
was a male, 0 otherwise
	
GPAi  = the GPA in economics classes of the ith student 
(4 = A, 3 = B, etc.)
	
SATMi = the score of the ith student on the mathematics 
portion of the Scholastic Aptitude Test
	
SAT  Vi = the score of the ith student on the verbal portion 
of the Scholastic Aptitude Test
a.	Carefully explain the meaning of the coefficient of G in this equa-
tion. (Hint: Be sure to specify what 39.7 stands for.)
b.	Does this result prove that the GRE is biased against women? Why 
or why not?
c.	 If you were going to add one variable to Equation 3.9, what would 
it be? Explain your reasoning.
d.	Suppose that the authors had defined their gender variables as 
Gi = a dummy variable equal to 1 if the ith student was a female, 
0 otherwise. What would the estimated Equation 3.9 have been 
in that case? (Hint: Only the intercept and the coefficient of the 
dummy variable change.)
	 6.	 Your boss is about to start production of her newest box-office smash-
to-be, Invasion of the Economists, Part II, when she calls you in and asks 
you to build a model of the gross receipts of all the movies produced in 
the last five years. Your regression is (standard errors in parentheses):10
Gn i = 781 + 15.4Ti - 992Fi + 1770Ji + 3027Si - 3160Bi + g
15.92   16742     18002  110062   123812
R2 = .485 N = 254
h
9. Mary Hirschfeld, Robert L. Moore, and Eleanor Brown, “Exploring the Gender Gap on the 
GRE Subject Test in Economics,” Journal of Economic Education, Vol. 26, No. 1, pp. 3–15.
10. This estimated equation (but not the question) comes from a final exam in managerial eco-
nomics given at the Harvard Business School.


87
EXERCISES
where:	
Gi = the final gross receipts of the ith motion picture 
(in thousands of dollars)
	
Ti = the number of screens (theaters) on which the ith 
film was shown in its first week
	
Fi = a dummy variable equal to 1 if the star of the ith 
film is a female and 0 otherwise
	
Ji  = a dummy variable equal to 1 if the ith movie was 
released in June or July and 0 otherwise
	
Si = a dummy variable equal to 1 if the star of the ith 
film is a superstar (like Tom Cruise or Milton) and 0 
otherwise
	
Bi = a dummy variable equal to 1 if at least one member 
of the supporting cast of the ith film is a superstar 
and 0 otherwise
a.	Hypothesize signs for each of the slope coefficients in the equa-
tion. Which, if any, of the signs of the estimated coefficients are 
different from your expectations?
b.	Milton, the star of the original Invasion of the Economists, is demand-
ing $4 million from your boss to appear in the sequel. If your esti-
mates are trustworthy, should she say “yes” or hire Fred (a nobody) 
for $500,000?
c.	 Your boss wants to keep costs low, and it would cost $1.2 million 
to release the movie on an additional 200 screens. Assuming your 
estimates are trustworthy, should she spring for the extra screens?
d.	The movie is scheduled for release in September, and it would cost 
$1 million to speed up production enough to allow a July release 
without hurting quality. Assuming your estimates are trustworthy, 
is it worth the rush?
e.	 You’ve been assuming that your estimates are trustworthy. Do you 
have any evidence that this is not the case? Explain your answer.
	 7.	 Let’s get some more experience with the six steps in applied regres-
sion. Suppose that you’re interested in buying an Apple iPod (either 
new or used) on eBay (the auction website) but you want to avoid 
overbidding. One way to get an insight into how much to bid would 
be to run a regression on the prices11 for which iPods have sold in 
previous auctions.
11. This is an example of a hedonic model, in which the price of an item is the dependent 
variable and the independent variables are the attributes of that item rather than the quantity 
demanded/supplied of that item. For more on hedonic models, see Section 11.8.


88
Chapter 3  Learning to Use ­Regression Analysis
	
	 	
The first step would be to review the literature, and luckily you 
find some good material—particularly a 2008 article by Leonardo 
Rezende12 that analyzes eBay Internet auctions and even estimates a 
model of the price of iPods.
	
	 	
The second step would be to specify the independent variables and 
functional form for your equation, but you run into a problem. The 
problem is that you want to include a variable that measures the con-
dition of the iPod in your equation, but some iPods are new, some 
are used and unblemished, and some are used and have a scratch or 
other defect.
a.	Carefully specify a variable (or variables) that will allow you to 
quantify the three different conditions of the iPods. Please answer 
this question before moving on.
b.	The third step is to hypothesize the signs of the coefficients of your 
equation. Assume that you choose the following specification. 
What signs do you expect for the coefficients of NEW, SCRATCH, 
and BIDRS? Explain.
PRICEi = β0 + β1NEWi + β2SCRATCHi + β3BIDRSi + ei
where:	
PRICEi       = the price at which the ith iPod sold on 
eBay
	
NEWi     = a dummy variable equal to 1 if the ith iPod 
was new, 0 otherwise
	
SCRATCHi = a dummy variable equal to 1 if the ith iPod 
had a minor cosmetic defect, 0 otherwise
	
BIDRSi    = the number of bidders on the ith iPod
c.	 The fourth step is to collect your data. Luckily, Rezende has data for 
215 silver-colored, 4 GB Apple iPod minis available on a website, 
so you download the data and are eager to run your first regres-
sion. Before you do, however, one of your friends points out that 
the iPod auctions were spread over a three-week period and wor-
ries that there’s a chance that the observations are not comparable 
because they come from different time periods. Is this a valid 
concern? Why or why not?
12. Leonardo Rezende, “Econometrics of Auctions by Least Squares,” Journal of Applied Econo-
metrics, November/December 2008, pp. 925–948.


89
  Appendix: Econometric Lab #2
d.	The fifth step is to estimate your specification using Rezende’s data, 
producing:
PRICEi = 109.24 + 54.99NEWi - 20.44SCRATCHi + 0.73BIDRSi
15.342            15.112           10.592
t =          10.28       -4.00             1.23
N = 215
	
Do the estimated coefficients correspond to your expectations? 
Explain.
e.	 The sixth step is to document your results. Look over the regres-
sion results in part d. What, if anything, is missing that should be 
included in our normal documentation format?
f.	 (optional) Estimate the equation yourself (Datafile = IPOD3), 
and determine the value of the item that you reported missing in 
your answer to part e.
h
3.5   Appendix: Econometric Lab #2
This lab contains a section for each of the six steps in applied regression 
analysis. Your project is to estimate an aggregate consumption function for 
the U.S. economy for the period 1945–2014.
Step 1: Review the Literature and Develop the Theoretical Model
John Maynard Keynes, one of the most influential economists since Adam 
Smith, developed the notion of a consumption function, which explains 
total consumption as a function of disposable personal income. You prob-
ably learned about the Keynesian consumption function in your principles 
of macroeconomics class, your intermediate macroeconomics class, or both. 
Other variables, including interest rates, also affect aggregate consumption.
a.	 One key analytical concept in the consumption function is the mar-
ginal propensity to consume. If you already know the definition of the 
marginal propensity to consume, write down that definition. If you 
don’t know the definition, read through your macroeconomics text-
book or find an appropriate website and write down the definition, 
being sure to specify your source with a full bibliographical reference.


90
Chapter 3  Learning to Use ­Regression Analysis
b.	 Use the EconLit database or another source to find two articles from 
academic journals (not newspapers, blogs, or magazines) about the 
consumption function. You don’t need to read the articles, but you 
must include the full bibliographic references for both articles.
Step 2: Specify the Model: Select the Independent Variables and 
the Functional Form
At this point, you would normally choose your independent variables and 
your functional form. Since we’d like everyone to estimate the same equa-
tion, we’ll make those decisions for you. Please estimate a linear consump-
tion function that includes disposable personal income and interest rates as 
your independent variables. The specific variables will be:
CONt
real personal consumption expenditures in year t, in billions 
of 2009 dollars
PYDt
real disposable personal income in year t, in billions of 2009 
dollars
AAAt
the real interest rate in year t
Write out your equation for consumption as a function of disposable 
personal income and the interest rate, using the form of Equation 3.1 in the 
text but substituting the appropriate variable names for Y and X.
Step 3: Hypothesize the Expected Signs of the Coefficients
Hypothesize the expected signs of the slope coefficients of your model. 
Explain your reasoning—if you don’t know, read about it. That’s what litera-
ture reviews are for!
Step 4: Collect the Data. Inspect and Clean the Data
A handy source of macroeconomic data is the Federal Reserve Economic Data 
(FRED) website: https://research.stlouisfed.org/fred2/. It contains hundreds 
of thousands of downloadable time series from the U.S. and around the 
world. This lab assignment uses data from FRED and other sources. You can 
download this dataset from http://www.pearson.com/studenmund in Stata 
or other formats. The dataset name is LAB3.
Optional: Spot check the dataset yourself by using FRED to find real per-
sonal consumption expenditures in billions of 2009 dollars (annual, not 
seasonally adjusted) for 1946.


91
  Appendix: Econometric Lab #2
Finally, clean and inspect the data. To do this, print out the summary 
statistics (mean, standard deviation, minimum, maximum) for all three vari-
ables and look for unusual numbers. Do you see any maximum or minimum 
values that are impossible (like negative consumption) or unreasonably high 
(like interest rates over 100%)? If so, that’s a clear indication that there is a 
mistake in the data.
Step 5: Estimate and Evaluate the Equation
Estimate your equation using Stata and print out the results. Then evaluate 
your results by answering the following questions:
a.	 Do the signs of the coefficients meet the expectations you developed 
in Step 3? If not, explain what differences there are.
b.	 What is R2? What is R2? Why are they different?
c.	 According to your results, what is the value of the marginal propensity 
to consume (rounded to three decimal places)? By how much will 
consumption change if disposable personal income falls by $1 billion 
(holding constant the corporate bond Aaa interest rate)?
d.	 According to your results, by how much will consumption change if 
the corporate bond Aaa interest rate rises by three percentage points 
(holding constant disposable personal income)?
e.	 Based on your answers to parts a–d above, does your regression result 
seem reasonable, or do you think that you’ve made an error of some sort?
Step 6: Document the Results
Now reorganize your Stata regression results and put them into the standard 
format presented in Equation 3.4.
