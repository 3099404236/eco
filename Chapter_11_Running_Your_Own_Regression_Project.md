# Chapter 11: Running Your Own Regression Project

**Pages:** 360-383

---

Running Your Own  
Regression Project
11.1  Choosing Your Topic
11.2  Collecting Your Data
11.3  Advanced Data Sources
11.4  Practical Advice for Your Project
11.5  Writing Your Research Report
11.6  A Regression User’s Checklist and Guide
11.7  Summary
11.8  Appendix: The Housing Price Interactive Exercise
Chapter 11
We believe that econometrics is best learned by doing, not by reading books, 
listening to lectures, or taking tests. To us, learning the art of econometrics 
has more in common with learning to fly a plane or learning to play golf 
than it does with learning about history or literature. In fact, we developed 
the interactive exercises of this chapter and Chapter 8 precisely because of 
our confidence in learning by doing.
Although interactive exercises are a good bridge between textbook exam-
ples and running your own regressions, they don’t go far enough. You still 
need to “get your hands dirty.” We think that you should run your own 
regression project before you finish reading this book even if you’re not 
required to do so. We’re not alone. Some professors substitute a research 
project for the final exam as their class’s comprehensive learning experience.
Running your own regression project has three major components:
1.	 Choosing a topic
2.	 Applying the six steps in regression analysis to that topic
3.	 Writing your research report
340


341
  Choosing Your Topic
The first and third of these components are the topics of Sections 11.1 and 
11.5, respectively. The rest of the chapter focuses on helping you carry out 
the six steps in regression analysis.
11.1   Choosing Your Topic
The purpose of an econometric research project is to use regression analysis 
to build the best explanatory equation for a particular dependent variable for 
a particular sample. Often, though, the hardest part is getting started. How 
can you choose a good topic?
There are at least three keys to choosing a topic. First, try to pick a field 
that you find interesting and that you know something about. If you enjoy 
working on your project, the hours involved will seem to fly by. In addition, 
if you know something about your subject, you’ll be more likely to make 
correct specification choices and to notice subtle indications of data errors or 
theoretical problems. A second key is to make sure that data are readily avail-
able with a reasonable sample (we suggest at least 25 observations). Nothing 
is more frustrating than searching through data source after data source in 
search of numbers for your dependent variable or one of your independent 
variables, so before you lock yourself into a topic, see if the data are there. 
The final key is to make sure that there is some substance to your topic. Try 
to avoid topics that are purely descriptive or virtually tautological in nature. 
Instead, look for topics that address an inherently interesting economic or 
behavioral question or choice.
Perhaps the best place to look for ideas for topics is to review your text-
books and notes from previous economics classes or to look over the exam-
ples and exercises of the first 10 chapters of this book. Often, you can take 
an idea from a previous study and update the data to see if the idea can be 
applied in a different context. Other times, reading an example will spark an 
idea about a similar or related study that you’d be interested in doing. Don’t 
feel that your topic has to contain an original hypothesis or equation. On 
your first or second project, it’s more important to get used to the economet-
rics than it is to create a publishable masterpiece.
Another way to find a topic is to read through issues of economics jour-
nals, looking for article topics that you find interesting and that might be 
possible to model. For example, Table 11.1 contains a list of the journals cited 
so far in this textbook (in order of the frequency of citation). These journals 
would be a great place to start if you want to try to replicate or update a pre-
vious research study. Although this is an excellent way to get ideas, it’s also 
frustrating, because most current articles use econometric techniques that go 
beyond those that we’ve covered so far in this text. As a result, it’s often dif-
ficult to compare your results to those in the article.


342
Chapter 11  Running Your Own Regression Project 
If you get stuck for a topic, go directly to the data sources themselves. That 
is, instead of thinking of a topic and then seeing if the data are available, look 
over what data are available and see if they help you generate ideas for topics. 
Quite often, a reference will have data not only for a dependent variable but 
also for most of the relevant independent variables all in one place, minimiz-
ing time spent collecting data.
Once you pick a topic, don’t rush out and run your first regression. 
Remember, the more time you spend reviewing the literature and analyzing 
your expectations on a topic, the better the econometric analysis and, ulti-
mately, your research report will be.
11.2   Collecting Your Data
Before any quantitative analysis can be done, the data must be collected, 
organized, and entered into a computer. Usually, this is a time-consuming 
and frustrating task because of the difficulty of finding data, the existence 
Table 11.1  Sources of Potential Topic Ideas
Econometrica
American Economic Review
Journal of Applied Econometrics
American Journal of Agricultural Economics
Journal of Economic Education
Journal of the American Statistical Association
World Development
Applied Economics
Assessment and Evaluation in Higher Education
Economic Inquiry
Economica
Journal of Agricultural and Applied Economics
Journal of Econometrics
Journal of Economic Literature
Journal of Money, Credit and Banking
Journal of the Royal Statistical Society
National Tax Review
NBER working papers
Review of Economics and Statistics
Scandinavian Journal of Economics
Southern Economic Journal
The Appraisal Journal


343
  Collecting Your Data
of definitional differences between theoretical variables and their empirical 
counterparts, and the high probability of data entry errors or data transmis-
sion errors. In general, though, time spent thinking about and collecting the 
data is well spent, since a researcher who knows the data sources and defini-
tions is much less likely to make mistakes using or interpreting regressions 
run on those data.
What Data to Look For
Before you settle on a research topic, make sure that data for your depen-
dent variable and all relevant independent variables are available. How-
ever, checking for data availability means deciding what specific variables 
you want to study. Half of the time that beginning researchers spend 
collecting data is wasted by looking for the wrong variables in the wrong 
places. A few minutes thinking about what data to look for will prevent 
hours of frustration later.
For example, if the dependent variable is the quantity of television sets 
demanded per year, then most independent variables should be measured 
annually as well. It would be inappropriate and possibly misleading to 
define the price of TVs as the price from a particular month. An average of 
prices over the year (usually weighted by the number of TVs sold per month) 
would be more meaningful. If the dependent variable includes all TV sets 
sold regardless of brand, then the price would appropriately be an aggregate 
based on prices of all brands. Calculating such aggregate variables, however, is 
not straightforward. Researchers typically make their best efforts to compute 
the respective aggregate variables and then acknowledge that problems still 
remain. For example, if the price data for all the various brands are not avail-
able, a researcher may be forced to compromise and use the price of one or a 
few of the major brands as a substitute for the proper aggregate price.
Another issue is suggested by the TV example. Over the years of the 
sample, it’s likely that the market shares of particular kinds of TV sets have 
changed. For example, flat-screen HD TV sets might have made up a majority 
of the market in one decade, but black-and-white sets might have been the 
favorite 40 years before. In cases where the composition of the market share, 
the size, or the quality of the various brands have changed over time, it would 
make little sense to measure the dependent variable as the number of TV sets 
because a “TV set” from one year has little in common with a “TV set” from 
another. The approach usually taken to deal with this problem is to measure 
the variable in dollar terms, under the assumption that value encompasses 
size and quality. Thus, we would work with the dollar sales of TVs rather than 
the number of sets sold.


344
Chapter 11  Running Your Own Regression Project 
A third issue, whether to use nominal or real variables, usually depends on 
the underlying theory of the research topic. Nominal (or money) variables 
are measured in current dollars and thus include increases caused by infla-
tion. If theory implies that inflation should be filtered out, then it’s best to 
state the variables in real (constant-dollar) terms by selecting an appropriate 
price deflator, such as the Consumer Price Index, and adjusting the money 
(or nominal) value by it.
As an example, the appropriate price index for Gross Domestic Product is 
called the GDP deflator. Real GDP is calculated by multiplying nominal GDP 
by the ratio of the GDP deflator from the base year to the GDP deflator from 
the current year:
Real GDP = nominal GDP * (base GDP deflator/current GDP deflator)
In 2007, U.S. nominal GDP was $13,807.5 billion and the GDP deflator was 
119.82 (for a base year of 2000 5 100), so real GDP was:1
Real GDP = $13,807.5 (100/119.82) = $11,523.9 billion
That is, the goods and services produced in 2007 were worth $13,807.5 bil-
lion if 2007 dollars were used but were worth only $11,523.9 billion if 2000 
dollars were used.
Fourth, recall that all economic data are either time series or cross sec-
tional in nature. Since time-series data are for the same economic entity from 
different time periods, whereas cross-sectional data are from the same time 
period but for different economic entities, the appropriate definitions of the 
variables depend on whether the sample is a time series or a cross section.
To understand this, consider the TV set example once again. A time-series 
model might study the sales of TV sets in the United States from 1967 to 2015, 
and a cross-sectional model might study the sales of TV sets by state for 2015. 
The time-series data set would have 49 observations, each of which would refer 
to a particular year. In contrast, the cross-sectional model data set would have 
50 observations, each of which would refer to a particular state. A variable that 
might be appropriate for the time-series model might be completely inappro-
priate for the cross-sectional model, and vice versa; at the very least, it would 
have to be measured differently. National advertising in a particular year would 
be appropriate for the time-series model, for example, while advertising in or 
near each particular state would make more sense for the cross-sectional one.
Finally, learn to be a critical reader of the descriptions of variables in 
econometric research. Are variables measured in nominal or real terms? 
1. 2009 Economic Report of the President, pp. 282–285.


345
  Collecting Your Data
Where did the data originate? A careful reader would want to know the 
answers to these questions before analyzing any results.
Where to Look for Economic Data
Although some researchers generate their own data through surveys or other 
techniques (and we’ll address this possibility in Section 11.3), the vast major-
ity of regressions are run on publicly available data. The best sources for such 
data are government publications and machine-readable data files. In fact, 
the U.S. government has been called the most thorough statistics-collecting 
agency in history.
Excellent government publications include the annual Economic Report 
of the President, the Handbook of U.S. Labor Statistics, and Historical Statistics 
of the U.S.  (published in 1975). One of the best places to start with U.S. 
data2 is the annual Census Catalog and Guide, which provides overviews and 
abstracts of data sources and various statistical products as well as details on 
how to obtain each item. Consistent international data are harder to come 
by, but the United Nations publishes a number of compilations of figures. 
The best of these are the U.N. Statistical Yearbook and the U.N. Yearbook of 
National Account Statistics.
However, most researchers use online computer databases to find data 
instead of plowing through stacks of printed volumes. These online databases, 
available through most college and university libraries, contain complete 
series on literally thousands of possible variables. Perhaps the best source of 
economic data on the Internet is FRED, the Federal Reserve Economic Data-
base, which contains more than 268,000 U.S. and international time series, 
all downloadable in Excel spreadsheets. It is hosted and maintained by the 
Federal Reserve Bank of St. Louis at https://research.stlouisfed.org/fred2/. The 
best guides to Internet data are “Resources for Economists on the Internet” 
and “Economagic.” Other good Internet resources are EconLit, which is an 
online summary of the Journal of Economic Literature, and “ProQuest, Dialog,” 
which provides online access to a large number of data sets.3
2. For older data, the Statistical Abstract of the United States is a great source. Sadly, this is no lon-
ger published by the government, but it is commercially available both in print and online as 
the ProQuest Statistical Abstract of the United States (Lanham, MD: Bernan, 2015).
3. The website addresses of these resources are:
Resources for Economists: https://www.aeaweb.org/RFE/showCat.php?cat_id=2
Economagic: http://www.economagic.com/ 
EconLit: https://www.aeaweb.org/econlit/ 
Proquest Dialog: http://www.proquest.com/products-services/ProQuest-Dialog.html


346
Chapter 11  Running Your Own Regression Project 
Missing Data
Suppose the data aren’t there? What happens if you choose the perfect vari-
able and look in all the right sources and can’t find the data?
The answer to this question depends on how much is missing. If a few obser-
vations have incomplete data in a cross-sectional study, you usually can afford to 
drop these observations from the sample. If the incomplete data are from a time 
series, you can sometimes estimate the missing value by interpolating (taking the 
mean of adjacent values). Similarly, if one variable is available only annually in 
an otherwise quarterly model, you may want to consider quarterly interpolations 
of that variable. In either case, interpolation can be justified only if the variable 
moves in a slow and smooth manner. Extreme caution should always be exer-
cised when “creating” data in such a way (and full documentation is required).
If no data at all exist for a theoretically relevant variable, then the problem 
worsens significantly. Omitting a relevant variable runs the risk of biased 
coefficient estimates, as you learned in Chapter 6. After all, how can you hold 
a variable constant if it’s not included in the equation? In such cases, most 
researchers resort to the use of proxy variables.
Proxy variables can sometimes substitute for theoretically desired vari-
ables for which data are missing. For example, the value of net investment is a 
variable that is not measured directly in a number of countries. As a result, a 
researcher might use the value of gross investment as a proxy, the assumption 
being that the value of gross investment is directly proportional to the value 
of net investment. This proportionality (which is similar to a change in units) 
is required because the regression analyzes the relationship between changes 
among variables, rather than the absolute levels of the variables.
In general, a proxy variable is a “good” proxy when its movements corre-
spond relatively well to movements in the theoretically correct variable. Since 
the latter is unobservable whenever a proxy must be used, there is usually 
no easy way to examine a proxy’s “goodness” directly. Instead, the researcher 
must document as well as possible why the proxy is likely to be a good or 
bad one. Poor proxies and variables with large measurement errors constitute 
“bad” data, but the degree to which the data are bad is a matter of judgment 
by the individual researcher.
11.3   Advanced Data Sources
So far, all the data sets in this text have been cross sectional or time series in 
nature, and we have collected our data by observing the world around us, 
instead of by creating the data ourselves. It turns out, however, that time-
series and cross-sectional data can be pooled to form panel data, and that data 


347
  Advanced Data Sources
can be generated through surveys. The purpose of this short section is to intro-
duce you to these more advanced data sources and to explain why it probably 
doesn’t make sense to use these data sources on your first regression project.
Surveys
Surveys are everywhere in our society. Marketing firms use surveys to learn 
more about products and competition, political candidates use surveys to 
fine-tune their campaign advertising or strategies, and governments use sur-
veys for all sorts of purposes, including keeping track of their citizens with 
instruments like the U.S. Census. As a result, many beginning researchers 
(particularly those who are having trouble obtaining data for their project) 
are tempted to run their own surveys in the hope that it’ll be an easy way to 
generate the data they need.
However, running a survey is not as easy as it might seem. For example, 
the topics to be covered in the survey need to be thought through carefully, 
because once a survey has been run, it’s virtually impossible to go back to 
the respondents and add another question. In addition, the questions them-
selves need to be worded precisely (and pretested) to avoid confusing the 
respondent or “leading” the respondent to a particular answer. Perhaps most 
importantly, it’s crucial for the sample to be random in order to avoid selec-
tion, survivor, and nonresponse biases. In fact, running a survey properly is 
so difficult that entire books and courses are devoted to the topic. To top it 
all off, most colleges and universities require a lengthy institutional review 
before allowing an on-campus survey.
As a result, we don’t encourage beginning researchers to run their own sur-
veys, and we’re cautious when we analyze the results of surveys run by others. 
As put by the American Statistical Association, “The quality of a survey is best 
judged not by its size, scope, or prominence, but by how much attention is 
given to preventing, measuring, and dealing with the many important prob-
lems that can arise.”4
Panel Data
As mentioned previously, panel data are formed when cross-sectional and 
time-series data sets are pooled to create a single data set. Why would you 
want to use panel data? In some cases, researchers use panel data to increase 
4. As quoted in “Best Practices for Research,” on the website of the American Association for 
Public Opinion Research: www.aapor.org. The best practices outlined on this website are a good 
place to start if you decide to create your own survey.


348
Chapter 11  Running Your Own Regression Project 
their sample size, but the main reason for using panel data is to provide an 
insight into an analytical question that can’t be obtained by using time-series 
or cross-sectional data alone.
What’s an example of panel data? Suppose that we’re interested in the rela-
tionship between budget deficits and interest rates but we have only 10 years’ 
worth of comparable annual data to study. Ten observations is too small a 
sample for a reasonable regression, so it might seem as if we’re out of luck. 
However, if we can find time-series data on the same economic variables—
interest rates and budget deficits—for the same ten years for six different coun-
tries, we’ll end up with a sample of 10*6 = 60 observations, which is more than 
enough to use. The result is a pooled cross-section time-series data set—a panel 
data set!
Unfortunately, panel data can’t be analyzed fully with the economet-
ric techniques you’ve learned to date in this text, so we don’t encourage 
beginning researchers to attempt to run regressions on panel data. Instead, 
we’ve devoted the majority of a chapter (Chapter 16) to panel data, and 
we urge you to read that chapter if you’re interested. Chapter 16 also covers 
experimental methods in economics, since such experiments often generate 
panel data.
11.4   Practical Advice for Your Project
The purpose of this section is to give you some practical advice about actu-
ally doing applied econometric work. Such advice often is missing from 
econometrics textbooks and courses, but the advice is crucial because many 
of the skills of an applied econometrician are judgmental and subjective in 
nature. No single text or course can teach these skills, and that’s not our goal. 
Instead, we want to alert you to some technical suggestions that a majority of 
experienced applied econometricians would be likely to support.
What to Check If You Get an Unexpected Sign
An all-too-familiar problem for a beginning econometrician is to run a 
regression and find that the sign of one or more of the estimated coefficients 
is the opposite of what was expected. While an unexpected sign certainly is 
frustrating, it’s not entirely bad news. Rather than considering this a disaster, 
a researcher should consider it a blessing—this result is a friendly message 
that some detective work needs to be done—there is undoubtedly some 
shortcoming in the theory, data, specification, or estimation procedure. If the 


349
  Practical Advice for Your Project
“correct” signs had been obtained, odds are that the analysis would not be 
double-checked. What should be checked?
1.	 Recheck the expected sign. Every once in a while, a variable that is 
defined “upside down” will cause a researcher to expect the wrong 
sign. For example, in an equation for student SATs, the variable “high 
school rank in class” (where a rank of 1 means that the student was 
first in his or her class) can sometimes lure a beginning researcher into 
expecting a positive coefficient for rank.
2.	 Check your data for input errors and/or outliers. If you have data errors or 
oddball observations, the chances of getting an unexpected sign—even 
a significant unexpected sign—increase dramatically.
3.	 Check for an omitted variable. The most frequent source of a significant 
unexpected sign for the coefficient of a relevant independent variable 
is an omitted variable. Think hard about what might have been omit-
ted, and remember to use our equation for expected bias.
4.	 Check for an irrelevant variable. A frequent source of insignificant unex-
pected signs is that the variable doesn’t actually belong in the equation 
in the first place. If the true coefficient for an irrelevant variable is zero, 
then you’re likely to get an unexpected sign half the time.
5.	 Check for multicollinearity. Multicollinearity increases the variances and 
standard errors of the estimated coefficients, increasing the chance that 
a coefficient could have an unexpected sign. The sampling distribu-
tions will be widely spread and may straddle zero, implying that it is 
quite possible that a draw from this distribution will produce an unex-
pected sign. Indeed, one of the casual indicators of multicollinearity is 
the presence of unexpected signs.
6.	 Check for sample selection bias. An unexpected sign sometimes can be 
due to the fact that the observations included in the data were not ob-
tained randomly.
7.	 Check your sample size. Multicollinearity isn’t the only source of high 
variances; they also could result from a small sample size or minimal 
variation in the explanatory variables. In some cases, all it takes to fix 
an unexpected sign is to increase the sample.
8.	 Check your theory. If you’ve exhausted every logical econometric 
­explanation for your unexpected sign, there are only two likely re-
maining explanations. Either your theory is wrong, or you’ve got a bad 
data set. If your theory is wrong, then you of course have to change 
your expected sign, but remember to test this new expectation on a 
different data set. However, be careful! It’s amazing how economists 


350
Chapter 11  Running Your Own Regression Project 
can conjure up rationales for unexpected signs after the regression has 
been run! One theoretical source of bias, and therefore unexpected 
signs, is if the underlying model is simultaneous in nature (we’ll cover 
simultaneous equations in Chapter 14).
A Dozen Practical Tips Worth Reiterating
Here are a number of practical tips for applied econometrics5 that we’ve 
made in previous chapters that are worth emphasizing. They work!
  1.	Don’t attempt to maximize R  2. (Chapter 2)
  2.	Always review the literature and hypothesize the signs of your coeffi-
cients before estimating a model. (Chapter 3)
  3.	Remember to inspect and clean your data before estimating a model. 
Know that outliers should not be automatically omitted; instead, they 
should be investigated to make sure that they belong in the sample. 
(Chapter 3)
  4.	Know the Classical Assumptions cold! (Chapter 4)
  5.	In general, use a one-sided t-test unless the expected sign of the coef-
ficient actually is in doubt. (Chapter 5)
  6.	Don’t automatically discard a variable with an insignificant t-score. 
In general, be willing to live with a variable with a t-score lower than 
the critical value in order to decrease the chance of omitting a relevant 
variable. (Chapter 6)
  7.	Know how to analyze the size and direction of the bias caused by an 
omitted variable. (Chapter 6)
  8.	Understand all the different functional form options and their com-
mon uses, and remember to choose your functional form primarily 
on the basis of theory, not fit. (Chapter 7)
  9.	Remember that multicollinearity doesn’t create bias; the estimated 
variances are large, but the estimated coefficients themselves are unbi-
ased. As a result, the most-used remedy for multicollinearity is to do 
nothing. (Chapter 8)
10.	 If you get a significant Durbin–Watson, Breusch–Pagan, or White test, 
remember to consider the possibility that a specification error might be  
5. For more practical tips of a similar nature, see Peter Kennedy, “Sinning in the Basement: 
What are the Rules? The Ten Commandments of Applied Econometrics,” Journal of Economic 
Surveys, Vol. 16, No. 4, pp. 569–589.


351
  Practical Advice for Your Project
causing impure serial correlation or heteroskedasticity. Don’t change 
your estimation technique from OLS to GLS or use adjusted standard 
errors until you have the best possible specification. (Chapters 9 and 10)
11.	 Remember that adjusted standard errors like Newey–West standard 
errors or HC standard errors use the OLS coefficient estimates. It’s the 
standard errors of the estimated coefficients that change, not the esti-
mated coefficients themselves. (Chapters 9 and 10)
12.	Finally, and perhaps most importantly, if in doubt, rely on common 
sense and economic theory, not on statistical tests.
The Ethical Econometrician
One conclusion that a casual reader of this book might draw from the large 
number of specifications we include is that we encourage the estimation of 
numerous regression results as a way of ensuring the discovery of these best 
possible estimates.
Nothing could be further from the truth!
As every reader of this book should know by now, our opinion is that the 
best models are those on which much care has been spent to develop the 
theoretical underpinnings and only a short time is spent pursuing alterna-
tive estimations of that equation. Many econometricians, ourselves included, 
would hope to be able to estimate only one specification of an equation 
for each data set. Econometricians are fallible and our data are sometimes 
imperfect, however, so it is unusual for a first attempt at estimation to be 
totally problem free. As a result, two or even more regressions are often neces-
sary to rid an estimation of fairly simple difficulties that perhaps could have 
been avoided in a world of perfect foresight.
Unfortunately, a beginning researcher usually has little motivation to stop 
running regressions until he or she likes the way the result looks. If running 
another regression provides a result with a better fit, why shouldn’t one more 
specification be tested?
The reason is a compelling one. Every time an extra regression is run and a 
specification choice is made on the basis of fit or statistical significance, the 
chances of making a mistake of inference increase dramatically. This can hap-
pen in at least two ways:
1.	 If you consistently drop a variable when its coefficient is insignificant but 
keep it when it is significant, it can be shown, as discussed in Section 6.4, 
that you bias your estimates of the coefficients of the equation and of the 
t-scores.


352
Chapter 11  Running Your Own Regression Project 
2.	 If you choose to use a lag structure, or a functional form or an estima-
tion procedure other than OLS, on the basis of fit rather than on the 
basis of previously theorized hypotheses, you run the risk that your 
equation will work poorly when it’s applied to data outside your 
sample. If you restructure your equation to work well on one data set, 
you might decrease the chance of it working well on ­another.
What might be thought of as ethical econometrics is also in reality good 
econometrics. That is, the real reason to avoid running too many different speci-
fications is that the fewer regressions you run, the more reliable and more con-
sistently trustworthy are your results. The instance in which professional ethics 
come into play is when a number of changes are made (different variables, lag 
structures, functional forms, estimation procedures, data sets, dropped outliers, 
and so on), but the regression results are presented to colleagues, clients, editors, 
or journals as if the final and best equation had been the first and only one esti-
mated. Our recommendation is that all estimated equations be reported even if 
footnotes or an appendix have to be added to the documentation.
We think that there are two reasonable goals for econometricians when 
estimating models:
1.	 Run as few different specifications as possible while still attempting 
to avoid the major econometric problems. The only exception to our 
recommendation to run as few specifications as possible is sensitivity 
analysis, described in Section 6.4.
2.	 Report honestly the number and type of different specifications esti-
mated so that readers of the research can evaluate how much weight to 
give to your results.
Therefore, the art of econometrics boils down to attempting to find the 
best possible equation in the fewest possible number of regression runs. Only 
careful thinking and reading before estimating the first regression can bring 
this about. An ethical econometrician is honest and complete in reporting 
the different specifications and/or data sets used.
11.5   Writing Your Research Report
Once you’ve finished your research, it’s important to write a report on your 
results so that others can benefit from what you found out (or didn’t find out) 
or so that you can get feedback on your econometric techniques from some-
one else. Most good research reports have a number of elements in common:
•	 A brief introduction that defines the dependent variable and states the 
goals of the research.


353
  A Regression User’s Checklist and Guide
•	 A short review of relevant previous literature and research.
•	 An explanation of the specification of the equation (model). This 
should include explaining why particular independent variables and 
functional forms were chosen as well as stating the expected signs of 
(or other hypotheses about) the slope coefficients.
•	 A description of the data (including generated variables), data sources, 
and any irregularities with the data.
•	 A presentation of each estimated specification, using our standard 
documentation format. If you estimate more than one specification, 
be sure to explain which one is best (and why).
•	 A careful analysis of the regression results that includes a discussion of 
any econometric problems encountered and complete documentation 
of all equations estimated and all tests run. (Beginning researchers are 
well advised to test for every possible econometric problem; with expe-
rience, you’ll learn to focus on the most likely difficulties.)
•	 A short summary/conclusion that includes any policy recommenda-
tions or suggestions for further research.
•	 A bibliography.
•	 An appendix that includes all data, all regression runs, and all relevant 
computer output. Do this carefully; readers appreciate a well-organized 
and labeled appendix.
We think that the easiest way to write such a research report is to keep 
a research journal as you go along. In this journal, you can keep track of a 
priori hypotheses, regression results, statistical tests, different specifications 
you considered, and theoretical analyses of what you thought was going on 
in your equation. You’ll find that when it comes time to write your research 
report, this journal will almost write your paper for you! The alternative to 
keeping a journal is to wait until you’ve finished all your econometric work 
before starting to write your research report, but by doing this, you run the 
risk of forgetting the thought process that led you to make a particular deci-
sion (or some other important item).
11.6   A Regression User’s Checklist and Guide
Table 11.2 contains a list of the items that a researcher checks when reviewing 
the output from a computer regression package. Not every item in the check-
list will be produced by your computer package, and not every item in your 
computer output will be in the checklist, but the checklist can be a very useful 
reference. In most cases, a quick glance at the checklist will remind you of the 


354
Chapter 11  Running Your Own Regression Project 
Table 11.2  Regression User’s Checklist
Symbol
Checkpoint
Reference
Decision
X, Y
Data observations
Check for errors. Check  
  means, ­maximums, 
and minimums.
Correct any errors.
df
Degrees of freedom
n - k - 1 7 0
n = number of  
observations
k = number of 
­explanatory 
­variables
If n - k - 1 … 0, equation  
  cannot be estimated, 
and if the degrees of 
freedom are low, pre-
cision is low. In such 
a case, try to include 
more observations.
βn
Estimated coefficient
Compare signs and  
  magnitudes to 
­expected values.
If they are unexpected,  
  respecify model if 
­appropriate.
t
t-statistic
tk =
βn k - βh0
se(βn k)
    or
tk =
βn k
se(βn k)
for computer- 
supplied t-scores 
or whenever 
βh0 = 0
Two-sided test:
h0: βk = βh0
ha: βk ≠βh0
One-sided test:
h0: βk … βh0
ha: βk 7 βh0
βh0, the hypothesized  
  β, is supplied by the 
researcher, and is 
often zero.
Reject h0 if 0 tk0 7 tc  
  and if the estimate is of 
the expected sign.
tc is the critical value of  
  α level of significance 
and n - k - 1 degrees  
of freedom.
R2
Coefficient of  
  ­determination
The percentage of the  
  variation of Y around 
its mean explained by 
the regression  
equation.
Measures the degree of  
  overall fit of the model  
to the data.
r  2
R2 adjusted for  
  degrees of 
­freedom
The percentage of the  
  variation of Y around 
its mean explained 
by the regression 
equation, adjusted for 
­degrees of freedom.
One indication that an  
  explanatory variable is 
irrelevant is if the r  2 
falls when it is included.
F
F-statistic
f =
1rssM - rss2>M
rss>1n - k - 12
Can be used to test joint  
  hypotheses about 
two or more coeffi-
cients. A ­special case 
is the F-test of overall 
­significance.


355
  A Regression User’s Checklist and Guide
Symbol
Checkpoint
Reference
Decision
DW
Durbin–Watson  
  ­statistic
Tests: h0: ρ … 0 
ha: ρ 7 0
For positive serial  
  ­correlation.
Reject h0 if Dw 6 dl.
Inconclusive if  
  dl … Dw … du.  
(dL and dU are critical 
DW ­values.)
ei
Residual
Check for heteroske- 
  dasticity by examin-
ing the pattern of the 
residuals.
May take appropriate  
  corrective action, but 
test first.
SE
Standard error of the  
  regression
An estimate of the  
  standard error of the 
error term.
A guide to the overall fit.
TSS
Total sum of squares
Tss = a
i
1Yi - Y22
Used to compute F, R2, 
and r  2.
RSS
Residual sum of  
  squares
rss = a
i
1Yi - Yni22
Same as above.
se(βn k)
Standard error of βn k
Used in t-statistics and  
  confidence intervals.
A measure of the  
  imprecision of the  
estimated coefficient.
ρn
Estimated first-order  
  autocorrelation  
coefficient
Usually provided by an  
  autoregressive 
­routine.
If negative, implies a  
  specification error or 
that the data were  
differenced.
r12
Simple correlation  
  coefficient ­between 
X1 and X2
Used to detect  
  multicollinearity.
Suspect severe multicol- 
  linearity if r12 7 .8.
VIF
Variance inflation  
  factor
Used to detect  
  multicollinearity.
Suspect severe multicol- 
  linearity if vif 7 5.
text sections that deal with the item, but if this is not the case, the fairly mini-
mal explanation in the checklist should not be relied on to cover everything 
needed for complete analysis and judgment. Instead, you should look up the 
item in the index. In addition, note that the actions in the right-hand column 
are merely suggestions. The circumstances of each individual research project 
are much more reliable guides than any dogmatic list of actions.
There are two ways to use the checklist. First, you can refer to it as a “glos-
sary of packaged computer output terms” when you encounter something 
in your regression result that you don’t understand. Second, you can work 
your way through the checklist in order, finding the items in your computer 
output and marking them. As with the Regression User’s Guide (Table 11.3), 


356
Chapter 11  Running Your Own Regression Project 
Table 11.3  Regression User’s Guide
What Can Go  
Wrong?
What Are the  
Consequences?
How Can It Be  
Detected?
How Can It Be  
Corrected?
Omitted Variable
The omission of a  
  relevant indepen-
dent variable
Bias in the coeffi- 
  cient estimates (the 
βns) of the included 
Xs.
Theory, significant  
  unexpected signs, 
or surprisingly poor 
fits.
Include the  
  omitted variable 
or a proxy.
Irrelevant Variable
The inclusion of a  
  variable that 
does not belong 
in the equation
Decreased precision 
  in the form of higher 
standard ­errors, 
lower t-scores and 
wider confidence 
intervals.
 1.  Theory
 2.  t-test on βn
3.  r  2
 4.  Impact on other 
coefficients if X is 
dropped.
Delete the  
  variable if its 
inclusion is not 
required by the 
underlying theory.
Incorrect Functional Form
The functional form  
  is inappropriate
Biased estimates,  
  poor fit, and ­difficult 
interpretation.
Examine the theory  
  carefully; think 
about the relation-
ship between X 
and Y.
Transform the  
  variable or the 
equation to a dif-
ferent functional 
form.
Multicollinearity
Some of the inde- 
  pendent variables 
are (imperfectly) 
correlated
No biased βns, but  
  estimates of the 
separate effects 
of the Xs are not 
reliable, i.e., high 
se(βn)s and low t-
scores.
No universally  
  accepted rule or 
test is available. 
Use high r12s or 
the VIF test.
Drop redundant  
  variables, but to 
drop others might 
introduce bias. 
Often doing noth-
ing is best.
Serial Correlation
Observations of 
the error term are 
correlated, as in: 
et = ρet-1 + ut
No biased βns, but  
  OLS no longer is 
minimum variance, 
and hypothesis 
testing and confi-
dence intervals are 
unreliable.
Use Durbin–Watson  
  test; if significantly 
less than 2, posi-
tive serial correla-
tion exists.
If impure, fix  
  the specification. 
Otherwise, con-
sider Generalized 
Least Squares 
or Newey–West 
standard errors.
Heteroskedasticity
The variance of  
  the error term 
is not constant 
for all observa-
tions, as in: 
var(ei) = σ2Zi
Same as for serial  
  correlation.
Use residual plots  
  and the Breusch–
Pagan or White 
tests.
If impure, fix the  
  specification. 
Otherwise, use 
HC standard er-
rors or reformu-
late the variables.


357
  Summary
the use of the Regression User’s Checklist will be most helpful for beginning 
researchers, but we also find ourselves referring back to it once in a while 
even after years of experience.
Be careful. All simplified tables, like the two in this chapter, must trade 
completeness for ease of use. As a result, strict adherence to a set of rules is 
not recommended even if the rules come from one of our tables. Someone 
who understands the purpose of the research, the exact definitions of the 
variables, and the problems in the data is much more likely to make a correct 
judgment than is someone equipped with a set of rules created to apply to a 
wide variety of possible applications.
Table 11.3, the Regression User’s Guide, contains a brief summary of the 
major econometric maladies discussed so far in this text. For each economet-
ric problem, we list:
1.	 Its nature.
2.	 Its consequences for OLS estimation.
3.	 How to detect it.
4.	 How to attempt to get rid of it.
How might you use the guide? If an estimated equation has a particular 
problem, such as an insignificant coefficient estimate, a quick glance at the 
guide can give some idea of the econometric problems that might be causing 
the symptom. Both multicollinearity and irrelevant variables can cause regres-
sion coefficients to have insignificant t-scores, for example, and someone 
who remembered only one of these potential causes might take the wrong 
corrective action. After some practice, the use of this guide will decrease until 
it eventually will seem fairly limiting and simplistic. Until then, however, our 
experience is that those about to undertake their first econometric research 
can benefit by referring to this guide.
11.7   Summary
1.	
Running your own regression project involves choosing your dependent 
variable, applying the six steps in applied regression (of Chapter 3) to 
that dependent variable, and then writing a research report that sum-
marizes your work.
2.	
A great research topic is one that you know something about, one 
that addresses an inherently interesting economic or behavioral ques-
tion or choice, and one for which data are available not only for the 
dependent variable but also for the obvious independent variables.


358
Chapter 11  Running Your Own Regression Project 
3.	
Don’t underestimate the difficulty and importance of collecting a 
complete and accurate data set. It’s a lot of work, but it’s worth it!
4.	
The art of econometrics boils down to finding the best possible equa-
tion in the fewest possible number of regression runs. The only way to 
do this is to spend quite a bit of time thinking through the underlying 
principles of your research project before you run your first regression.
5.	
Before you complete your research project, be sure to review the prac-
tical hints and regression user’s guide and checklist in Sections 11.4 
and 11.6.
11.8   Appendix: The Housing Price Interactive Exercise
This interactive regression learning exercise is somewhat different from the pre-
vious one in Section 8.7. Our goal is still to bridge the gap between textbook 
and computer, but we feel that if you completed the previous interactive exer-
cise, you should be ready to do the computer work on your own. As a result, 
this interactive exercise will provide you with a short literature review and the 
data, but you’ll be asked to calculate your own estimates. Feedback on your 
specification choices will once again be found in the hints in Appendix A.
Since the only difference between this interactive exercise and the first one 
is that this one requires you to estimate your chosen specification(s) with the 
computer, our guidelines for interactive exercises still apply:
1.	 Take the time to look over a portion of the reading list before choosing 
a specification.
2.	 Try to estimate as few regression runs as possible.
3.	 Avoid looking at the hints until after you’ve reached what you think is 
your best specification.
We believe that the benefits you get from an interactive exercise are 
directly proportional to the effort you put into it. If you have to delay this 
exercise until you have the time and energy to do your best, that’s probably 
a good idea.
Building a Hedonic Model of Housing Prices
In the next section, we’re going to ask you to specify the independent vari-
ables and functional form for an equation whose dependent variable is the 
price of a house in Southern California. Before making these choices, it’s vital 


359
  Appendix: The Housing Price Interactive Exercise
to review the housing price literature and to think through the theory behind 
such models. Such a review is especially important in this case because the 
model we’ll be building will be hedonic in nature.
What is a hedonic model? Recall that in Section 1.5 we estimated an equa-
tion for the price of a house as a function of the size of that house. Such a 
model is called hedonic because it uses measures of the quality of a product 
as independent variables instead of measures of the market for that product 
(like quantity demanded, income, etc.). Hedonic models are most useful 
when the product being analyzed is heterogeneous in nature because we 
need to analyze what causes products to be different and therefore to have 
different prices. With a homogeneous product, hedonic models are virtually 
useless.
Perhaps the most-cited early hedonic housing price study is that of G. 
Grether and P. Mieszkowski,6 who collected a seven-year data set and built 
a number of linear models of housing price using different combinations of 
variables. They included square feet of space, the number of bathrooms, and 
the number of rooms, although the number of rooms turned out to be insig-
nificant. They also included lot size and the age of the house as variables, 
specifying a quadratic function for the age variable. Most innovatively, they 
used several slope dummies in order to capture the interaction effects of vari-
ous combinations of variables (like a hardwood-floors dummy times the size 
of the house).
Peter Linneman7 estimated a housing price model on data from Los Angeles, 
Chicago, and the entire United States. His goal was to create a model that 
worked for the two individual cities and then to apply it to the nation to test 
the hypothesis of a national housing market. Linneman did not include any 
lot characteristics, nor did he use any interaction variables. His only measures 
of the size of the living space were the number of bathrooms and the num-
ber of nonbathrooms. Except for an age variable, the rest of the independent 
variables were dummies describing quality characteristics of the house and 
neighborhood. Although many of the dummy variables were quite fickle, the 
coefficients of age, number of bathrooms, and the number of nonbathrooms 
were relatively stable and significant. Central air conditioning had a negative, 
insignificant coefficient for the Los Angeles regression.
6. G. M. Grether and Peter Mieszkowski, “Determinants of Real Estate Values,” Journal of Urban 
Economics, Vol. 1, pp. 127–146. Another classic article of the same era is J. Kain and J. Quigley, 
“Measuring the Value of Housing Quality,” Journal of the American Statistical Association, Vol. 45, 
pp. 532–548.
7. Peter Linneman, “Some Empirical Results on the Nature of the Hedonic Price Functions for 
the Urban Housing Market,” Journal of Urban Economics, Vol. 8, No. 1, pp. 47–68.


360
Chapter 11  Running Your Own Regression Project 
K. Ihlanfeldt and J. Martinez-Vasquez8 investigated sample bias in vari-
ous methods of obtaining house price data and concluded that a house’s 
sales price is the least biased of all measures. Unfortunately, they went on to 
estimate an equation by starting with a large number of variables and then 
dropping all those that had t-scores below 1, almost surely introducing bias 
into their equation.
Finally, Allen Goodman9 added some innovative variables to an estimate 
on a national data set. He included measures of specific problems like rats, 
cracks in the plaster, holes in the floors, plumbing breakdowns, and the level 
of property taxes. Although the property tax variable showed the capitaliza-
tion of low property taxes, as would be expected, the rats coefficient was 
insignificant, and the cracks variable’s coefficient asserted that cracks signifi-
cantly increase the value of a house.
The Housing Price Interactive Exercise
Now that we’ve reviewed at least a portion of the literature, it’s time to build 
your own model. Recall that in Section 1.5, we built a simple model of the 
price of a house as a function of the size of that house, Equation 1.21:
	
Pni = 40.0 + 0.138Si	
(1.21)
where:  Pi = the price (in thousands of dollars) of the ith house
	
Si = the size (in square feet) of the ith house
Equation 1.21 was estimated on a sample of 43 houses that were purchased 
in the same Southern California town (Monrovia) within a few weeks of each 
other. It turns out that we have a number of additional independent variables 
for the data set we used to estimate Equation 1.21. Also available are:
Ni  = the quality of the neighborhood of the ith house (1 5 
best, 4 5 worst) as rated by two local real estate agents
Ai   = the age of the ith house in years
BEi = the number of bedrooms in the ith house
BAi = the number of bathrooms in the ith house
8. Keith Ihlanfeldt and Jorge Martinez-Vasquez, “Alternate Value Estimates of Owner-Occupied 
Housing: Evidence on Sample Selection Bias and Systematic Errors,” Journal of Urban Econom-
ics, Vol. 20, No. 3, pp. 356–369. Also see Eric Cassel and Robert Mendelsohn, “The Choice of 
Functional Forms for Hedonic Price Equations: Comment,” Journal of Urban Economics, Vol. 18, 
No. 2, pp. 135–142.
9. Allen C. Goodman, “An Econometric Model of Housing Price, Permanent Income, Tenure 
Choice, and Housing Demand,” Journal of Urban Economics, Vol. 23, pp. 327–353.


361
  Appendix: The Housing Price Interactive Exercise
CAi = a dummy variable equal to 1 if the ith house has central 
air conditioning, 0 otherwise
SPi = a dummy variable equal to 1 if the ith house has a pool, 0 
otherwise
Yi   = the size of the yard around the ith house (in square feet)
Read through the list of variables again, developing your own analyses of the 
theory behind each variable. What are the expected signs of the coefficients? 
Which variables seem potentially redundant? Which variables must you 
include?
In addition, there are a number of functional form modifications that can 
be made. For example, you might consider a quadratic polynomial for age, 
as Grether and Mieszkowski did, or you might consider creating slope dum-
mies such as SP # S or CA # S. Finally, you might consider interactive variables 
that involve the neighborhood proxy variable such as N # S or N # BA. What 
hypotheses would each of these imply?
Develop your specification carefully. Think through each variable and/or 
functional form decision, and take the time to write out your expectations for 
the sign and size of each coefficient. Don’t take the attitude that you should 
include every possible variable and functional form modification and then 
drop the insignificant ones. Instead, try to design the best possible hedonic 
model of housing prices you can the first time around.
Once you’ve chosen a specification, estimate your equation, using the data 
in Table 11.4 and analyze the result.
Table 11.4  Data for the Housing Price Interactive Exercise
P
S
N
A
BE
BA
CA
SP
Y
107
736
4
39
2
1
0
0
3364
133
720
3
63
2
1
0
0
1780
141
768
2
66
2
1
0
0
6532
165
929
3
41
3
1
0
0
2747
170
1080
2
44
3
1
0
0
5520
173
942
2
65
2
1
0
0
6808
182
1000
2
40
3
1
0
0
6100
200
1472
1
66
3
2
0
0
5328
220
1200
1.5
69
3
1
0
0
5850
226
1302
2
49
3
2
0
0
5298
260
2109
2
37
3
2
1
0
3691
275
1528
1
41
2
2
0
0
5860
(continued)


362
Chapter 11  Running Your Own Regression Project 
P
S
N
A
BE
BA
CA
SP
Y
280
1421
1
41
3
2
0
1
6679
289
1753
1
  1
3
2
1
0
2304
295
1528
1
32
3
2
0
0
6292
300
1643
1
29
3
2
0
1
7127
310
1675
1
63
3
2
0
0
9025
315
1714
1
38
3
2
1
0
6466
350
2150
2
75
4
2
0
0
14825
365
2206
1
28
4
2.5
1
0
8147
503
3269
1
5
4
2.5
1
0
10045
135
936
4
75
2
1
0
0
5054
147
728
3
40
2
1
0
0
1922
165
1014
3
26
2
1
0
0
6416
175
1661
3
27
3
2
1
0
4939
190
1248
2
42
3
1
0
0
7952
191
1834
3.5
40
3
2
0
1
6710
195
989
2
41
3
1
0
0
5911
205
1232
1
43
2
2
0
0
4618
210
1017
1
38
2
1
0
0
5083
215
1216
2
77
2
1
0
0
6834
228
1447
2
44
2
2
0
0
4143
242
1974
1.5
65
4
2
0
1
5499
250
1600
1.5
63
3
2
1
0
4050
250
1168
1.5
63
3
1
0
1
5182
255
1478
1
50
3
2
0
0
4122
255
1756
2
36
3
2
0
1
6420
265
1542
2
38
3
2
0
0
6833
265
1633
1
32
4
2
0
1
7117
275
1500
1
42
2
2
1
0
7406
285
1734
1
62
3
2
0
1
8583
365
1900
1
42
3
2
1
0
19580
397
2468
1
10
4
2.5
1
0
6086
Datafile 5 HOUSE11
Table 11.4  (continued)


363
  Appendix: The Housing Price Interactive Exercise
1.	 Test your hypotheses for each coefficient with the t-test. Pay special at-
tention to any functional form modifications.
2.	 Decide what econometric problems exist in the equation, testing, if ap-
propriate, for multicollinearity, serial correlation, or heteroskedasticity.
3.	 Decide whether to accept your first specification as the best one or to 
make a modification in your equation and estimate again. Make sure 
you avoid the temptation to estimate an additional specification “just 
to see what it looks like.”
Once you’ve decided to make no further changes, you’re finished— 
congratulations! Now turn to the hints in Appendix A for feedback on your 
choices.
