# Chapter 13: Dummy Dependent Variable Techniques

**Pages:** 410-430

---

13.1  The Linear Probability Model
13.2  The Binomial Logit Model
13.3  Other Dummy Dependent Variable Techniques
13.4  Summary and Exercises
Dummy Dependent  
Variable Techniques
Chapter 13
Until now, our discussion of dummy variables has been restricted to dummy 
independent variables. However, there are many important research topics 
for which the dependent variable is appropriately treated as a dummy, equal 
only to 0 or 1.
In particular, researchers analyzing consumer choice often must cope with 
dummy dependent variables (also called qualitative dependent variables). 
For example, how do high school students decide whether to go to college? 
What distinguishes Pepsi drinkers from Coke drinkers? How can we convince 
people to use public transportation instead of driving? For an econometric 
study of these topics, or of any topic that involves a discrete choice of some 
sort, the dependent variable is typically a dummy variable.
In the first two sections of this chapter, we’ll present two frequently used 
ways to estimate equations that have dummy dependent variables: the linear 
probability model and the binomial logit model. In the last section, we’ll 
briefly discuss the binomial probit model and multinomial models.
13.1   The Linear Probability Model
What Is a Linear Probability Model?
The most obvious way to estimate a model with a dummy dependent variable 
is to run OLS on a typical linear econometric equation. A linear probability 
390


391
  The Linear Probability Model
model is just that, a linear-in-the-coefficients equation used to explain a 
dummy dependent variable:
	
Di = β0 + β1X1i + β2X2i + ei	
(13.1)
where Di is a dummy variable and the Xs, βs, and e are typical independent 
variables, regression coefficients, and an error term, respectively.
For instance, suppose you’re interested in understanding why some states 
have female governors and others don’t. In such a model, the appropriate 
dependent variable would be a dummy, for example Di equal to 1 if the ith 
state has a female governor and equal to 0 otherwise. If we hypothesize that 
states with a high percentage of females and a low percentage of social con-
servatives would be likely to have a female governor, then a linear probability 
model would be:
	
+	
-
	
Di = β0 + β1Fi + β2Ri + ei	
(13.2)
where:	
Di = 1 if the ith state has a female governor, 0 otherwise
	
Fi  = females as a percent of the ith state’s population
	
Ri  = conservatives as a percent of the ith state’s registered  
voters
The term linear probability model comes from the fact that the right side 
of the equation is linear while the expected value of the left side measures 
the probability that Di = 1. To understand this second statement, let’s 
assume that we estimate Equation 13.2 and get a DN i of 0.10 for a particular 
state. What does that mean? Well, since D = 1 if the governor is female and 
D = 0 if the governor is male, a state with a DN i of 0.10 can perhaps best be 
thought of as a state in which there is a 10 percent chance that the governor 
will be female, based on the state’s values for the independent variables. 
Thus DN i is an estimate of the probability that Di = 1 for the ith observa-
tion, and:
	
DN i = Pr1Di = 12 = βN 0 + βN 1Fi + βN 2Ri	
(13.3)
where Pr1Di = 12 indicates the probability that Di = 1 for the ith observation.
How should we interpret the coefficients of Equation 13.3? Since DN i mea-
sures the probability that Di = 1, then a coefficient in a linear probability 
model is an estimate of the change in the probability that Di = 1 caused by 
a one-unit increase in the independent variable in question, holding constant 
the other independent variables in the equation.
∏


392
Chapter 13  Dummy Dependent Variable Techniques 
Let’s define Pi to be the true probability that Di = 1. We can never observe 
Pi, just as we can never observe true βs, because it reflects the underlying 
situation before a discrete choice is made. After the choice is made, we can 
observe only the outcome of that choice, and so the dependent variable Di 
can take on the values of only 0 or 1. Thus, even though Pi can be any value 
between 0 and 1, we can observe only the two extremes (0 and 1) in Di.
Problems with the Linear Probability Model
Unfortunately, using OLS to estimate the coefficients of an equation with a 
dummy dependent variable faces at least three problems:
1.	 R2 is not an accurate measure of overall fit. For models with a dummy 
dependent variable, R2 tells us very little about how well the model 
explains the choices of the decision makers. To see why, take a look at 
Figure 13.1. Di can equal only 1 or 0, but DN i must move in a continuous 
fashion from one extreme to the other. This means that DN i is likely to 
be quite different from Di for some range of Xi. Thus, R2 is likely to be 
much lower than 1 even if the model actually does an exceptional job 
of explaining the choices involved. As a result, R2 (or R2) should not 
be relied on as a measure of the overall fit of a model with a dummy 
dependent variable.
2.	 DN i is not bounded by 0 and 1. Since Di is a dummy variable, we’d expect 
DN i to be limited to a range of from 0 to 1. After all, the prediction that a 
probability equals 2.6 (or -2.6, for that matter) is almost meaningless. 
However, take another look at Equation 13.3. Depending on the values 
of the independent variables and the βN s, the right-hand side might well 
be outside the meaningful range. For instance, if F, R, and all the βN s 
in Equation 13.3 equal 1.0, then DN i equals 3.0, which is substantially 
greater than 1.0.
3.	 The error term is neither homoskedastic nor normally distributed. In addition, 
the error term in a linear probability model is heteroskedastic and is 
not distributed normally, mainly because Di takes on only two values 
(0 and 1). In practice, however, the impact of these problems on OLS 
estimation is minor, so many researchers ignore potential heteroskedas-
ticity and nonnormality and apply OLS directly to the linear probability 
model.1
1. See R. G. McGilvray, “Estimating the Linear Probability Function,” Econometrica, Vol. 38, 
pp. 775–776.


393
  The Linear Probability Model
The first of these problems isn’t impossible to deal with, because there are a 
variety of alternatives to R2 for equations with dummy dependent variables.2 
Our preference is to create a measure based on the percentage of the observa-
tions in the sample that a particular estimated equation explains correctly. 
Di
Di 7 1
Di = 1
1 7 Di 7 0
Di = 0
Di = b0 + b1X1i + b2X2i
X1i
(Holding X2i Constant)
Di 6 0
N
N
N
N
N
N
N
N
N
N
Figure 13.1  A Linear Probability Model
In a linear probability model, all the observed Dis equal either 0 or 1, but DN i moves 
linearly from one extreme to the other. As a result, R2 is often quite low even if the 
model does an excellent job of explaining the decision maker’s choice. In addition,  
exceptionally large or small values of X1i (holding X2i constant) can produce values  
of DN i outside the meaningful range of 0 to 1.
2. See M. R. Veal and K. F. Zimmerman, “Pseudo-R2 Measures for Some Common Limited 
Dependent Variables Models,” Journal of Economic Surveys, Vol. 10, No. 3, pp. 241–259 and 
C. S. McIntosh and J. J. Dorfman, “Qualitative Forecast Evaluation: A Comparison of Two 
Performance Measures,” American Journal of Agricultural Economics, Vol. 74, pp. 209–214.


394
Chapter 13  Dummy Dependent Variable Techniques 
To use this approach, consider a DN i 7 0.5 to predict that Di = 1 and a DN i 6 0.5 
to predict that Di = 0. If we then compare these predictions3 with the actual 
Di, we can calculate the percentage of observations explained correctly.
Unfortunately, using the percentage explained correctly as a substitute 
for R2 for the entire sample has a flaw. Suppose that 85 percent of your 
observations are 1s and 15 percent are 0s. Explaining 85 percent of the 
sample correctly sounds good, but your results are no better than naively 
guessing that every observation is a 1! A better way might be to calculate 
the percentage of 1s explained correctly, calculate the percentage of zeroes 
explained correctly, and then report the average of these two percentages. As 
a shorthand, we’ll call this average R2
p. That is, we’ll define R2
p to be the aver-
age of the percentage of 1s explained correctly and the percentage of zeroes 
explained correctly. Since R2
p is a new statistic, we’ll calculate and discuss both 
R2
p and R2 throughout this chapter.
For most researchers, therefore, the major difficulty with the linear prob-
ability model is the unboundedness of the predicted Dis. Take another look 
at Figure 13.1 for a graphical interpretation of the situation. Because of the 
linear relationship between the Xis and DN i, DN i can fall well outside the relevant 
range of 0 to 1.
One simplistic way to get around the unboundedness problem is to assign 
DN i = 1.0 to all values of DN i above 1 and DN i = 0.0 to all negative values. This 
approach copes with the problem by ignoring it, since an observation for 
which the linear probability model predicts a probability of 2.0 has been 
judged to be more likely to be equal to 1.0 than an observation for which 
the model predicts a 1.0, and yet they are lumped together. Even DN i = 1 isn’t 
very useful, because it implies that events will happen with certainty, which 
is surely a foolish prediction to make. What is needed is a systematic method 
of forcing the DN is to range from 0 to 1 in a smooth and meaningful fashion. 
We’ll present such a method, the binomial logit, in Section 13.2.
Using the linear probability model, despite this unboundedness problem, 
may not cause insurmountable difficulties. In particular, the signs and gen-
eral significance levels of the estimated coefficients of the linear probability 
model are often similar to those of the alternatives we will discuss later in 
this chapter.
3. Although it’s standard to use DN i = 0.5 as the value that distinguishes a prediction of Di = 1 
from a prediction of Di = 0, there’s no rule that requires that 0.5 be used. This is because it’s 
possible to imagine circumstances in which 0.5 is too high or too low. For example, if the pay-
off when you’re right if you classify Di = 1 is much lower than the payoff when you’re right if 
you classify Di = 0, then a value other than 0.5 might make sense.


395
  The Linear Probability Model
An Example of a Linear Probability Model
Let’s take a look at an example of a linear probability model: a disaggregate 
study of the labor force participation of women.
A person is defined as being in the labor force if she either has a job or is 
actively looking for a job. Thus, a disaggregate (cross-sectional by person) 
study of women’s labor force participation is appropriately modeled with a 
dummy dependent variable:
Di = 1 if the ith woman has or is looking for a job,  
0 otherwise (not in the labor force)
A review of the literature reveals that there are many potentially relevant 
independent variables. Two of the most important are the marital status and 
the number of years of schooling of the woman. The expected signs for the 
coefficients of these variables are fairly straightforward, since a woman who 
is unmarried and well educated is much more likely to be in the labor force 
than her opposite. If we choose a linear functional form, we’ve got a linear 
probability model:
	
-	
+
	
Di = β0 + β1Mi + β2Si + ei	
(13.4)
where:	
Mi = 1 if the ith woman is married and 0 otherwise
	
Si  = the number of years of schooling of the ith woman
The data are presented in Table 13.1. The sample size is limited to 30 in 
order to make it easier for readers to enter the dataset on their own. Unfor-
tunately, such a small sample will make hypothesis testing fairly unreliable. 
Table 13.1 also includes the age of the ith woman, Ai. Another typically used 
variable, Oi = other income available to the ith woman, is not available for 
this sample, introducing possible omitted variable bias.
If we now estimate Equation 13.4 with the data on the labor force partici-
pation of women from Table 13.1, we obtain (standard errors in parentheses):
	
DN i = -  0.28 - 0.38Mi + 0.09Si	
(13.5)
10.152     10.032
N = 30        R2 = .32         R2
p = .81
How do these results look? Despite the small sample and the possible bias 
due to omitting Oi, both independent variables have estimated coefficients 
that are significant in the expected direction. In addition, the R2 of .32 is 
fairly high for a linear probability model. (Since Di equals only 0 or 1, it’s 


396
Chapter 13  Dummy Dependent Variable Techniques 
Table 13.1  Data on the Labor Force Participation of Women
Observation #
Di
Mi
ai
Si
Dn i
  1
1.0
0.0
31.0
16.0
1.20
  2
1.0
1.0
34.0
14.0
0.63
  3
1.0
1.0
41.0
16.0
0.82
  4
0.0
0.0
67.0
  9.0
0.55
  5
1.0
0.0
25.0
12.0
0.83
  6
0.0
1.0
58.0
12.0
0.45
  7
1.0
0.0
45.0
14.0
1.01
  8
1.0
0.0
55.0
10.0
0.64
  9
0.0
0.0
43.0
12.0
0.83
10
1.0
0.0
55.0
  8.0
0.45
11
1.0
0.0
25.0
11.0
0.73
12
1.0
0.0
41.0
14.0
1.01
13
0.0
1.0
62.0
12.0
0.45
14
1.0
1.0
51.0
13.0
0.54
15
0.0
1.0
39.0
  9.0
0.17
16
1.0
0.0
35.0
10.0
0.64
17
1.0
1.0
40.0
14.0
0.63
18
0.0
1.0
43.0
10.0
0.26
19
0.0
1.0
37.0
12.0
0.45
20
1.0
0.0
27.0
13.0
0.92
21
1.0
0.0
28.0
14.0
1.01
22
1.0
1.0
48.0
12.0
0.45
23
0.0
1.0
66.0
  7.0
-0.01
24
0.0
1.0
44.0
11.0
0.35
25
0.0
1.0
21.0
12.0
0.45
26
1.0
1.0
40.0
10.0
0.26
27
1.0
0.0
41.0
15.0
1.11
28
0.0
1.0
23.0
10.0
0.26
29
0.0
1.0
31.0
11.0
0.35
30
1.0
1.0
44.0
12.0
0.45
Datafile = WOMEN13


397
  The Binomial Logit Model
almost impossible to get an R2 much higher than .70.) Further evidence of 
good fit is the fairly high R2
p of .81, meaning that an average of 81 percent of 
the choices were explained “correctly” by Equation 13.5.
We need to be careful when we interpret the estimated coefficients in 
Equation 13.5, however. Remember that the slope coefficient in a linear 
probability model represents the change in the probability that Di equals 1 
caused by a one-unit increase in the independent variable (holding the other 
independent variables constant). Viewed in this context, do the estimated 
coefficients make economic sense? The answer is yes: The probability of a 
woman participating in the labor force falls by 38 percentage points if she 
is married (holding constant schooling). Each year of schooling increases 
the probability of labor force participation by 9 percentage points (holding 
constant marital status).
The values for DN i have been included in Table 13.1. Note that DN i is indeed 
often outside the meaningful range of 0 and 1, causing most of the problems 
cited earlier. To attack this problem of the unboundedness of DN i, however, we 
need a new estimation technique, so let’s take a look at one.
13.2   The Binomial Logit Model
What Is the Binomial Logit?
The binomial logit is an estimation technique for equations with dummy 
dependent variables that avoids the unboundedness problem of the linear 
probability model by using a variant of the cumulative logistic function:
	
Pi =
1
1 + e-3β0+β1X1i+β2X2i4	
(13.6)
where Pi is the true probability that Di = 1. We can’t observe Pi, so we need 
to use observed Dis to estimate a logit equation like Equation 13.6. That 
estimation will produce DN is that we can compare to the DN is produced by an 
estimated linear probability model like Equation 13.3.
Are the DN is produced by a logit now limited by 0 and 1? The answer is yes, 
but to see why we need to take a close look at Equation 13.6. What is the 
largest that DN i can be? Well, if βN 0 + βN 1X1i + βN 2X2i equals infinity, then:
	
DN i =
1
1 + e-∞= 1
1 = 1	
(13.7)


398
Chapter 13  Dummy Dependent Variable Techniques 
because e to the minus infinity equals 0. What’s the smallest that DN i can be? 
If βN 0 + βN 1X1i + βN 2X2i equals minus infinity, then:
	
DN i =
1
1 + e∞=
1
∞= 0	
(13.8)
Thus, DN i is bounded by 1 and 0. As can be seen in Figure 13.2, DN i approaches 
1 and 0 very slowly (asymptotically). The binomial logit model therefore 
avoids the major problem that the linear probability model encounters in 
dealing with dummy dependent variables. In addition, the logit is quite sat-
isfying to most researchers because it turns out that real-world data often are 
described well by S-shape patterns like that in Figure 13.2.
Di
Di = 1
1 7 Di 7 0
Di = 0
X1
(Holding X2 Constant)
Logit
Linear Probability Model
(for comparison purposes)
N
N
N
N
Figure 13.2  dN i Is Bounded by 0 and 1 in a Binomial Logit Model
In a binomial logit model, DN i is nonlinearly related to X1, so even exceptionally large 
or small values of X1i, holding X2i constant, will not produce values of DN i outside the 
meaningful range of 0 to 1.


399
  The Binomial Logit Model
Logits cannot be estimated using OLS. Instead, we use maximum likeli-
hood (ML), an iterative estimation technique that is especially useful for 
equations that are nonlinear in the coefficients. ML estimation is inherently 
different from least squares in that it chooses coefficient estimates that 
maximize the likelihood of the sample data set being observed.4 Interestingly, 
OLS and ML estimates are not necessarily different; for a linear equation 
that meets the Classical Assumptions (including the normality assumption), 
ML estimates are identical to the OLS ones.
One of the reasons that maximum likelihood is used is that ML has a number 
of desirable large sample properties; ML is consistent (homes in on true param-
eter values) and asymptotically efficient (minimum variance for large samples). 
With very large samples, ML often has the added advantage of converging to a 
normal distribution, allowing the use of typical hypothesis testing techniques. 
As a result, sample sizes for logits should be substantially larger than they are 
for linear regressions. Some researchers aim for samples of 500 or more.
It’s also important to make sure that a logit sample contains a reasonable 
representation of both alternative choices. For instance, if 98 percent of a 
sample chooses alternative A and 2 percent chooses B, a random sample of 
500 might have only 10 observations that choose B. In such a situation, our 
estimated coefficients would be overly reliant on the characteristics of those 
10 observations. A better technique would be to disproportionately sample 
from those who choose B. It turns out that using different sampling rates for 
subgroups within the sample does not cause bias in the slope coefficients of a 
logit model,5 even though it might do so in a linear regression.
When we estimate a logit, we apply the ML technique to Equation 13.6, 
but that equation’s functional form is complex, so let’s try to simplify it a bit. 
First, a few mathematical steps can allow us to rewrite Equation 13.6 so that 
the right side of the equation looks like the linear probability model:
	
lna
Pi
31 - Pi4 b = β0 + β1X1i + β2X2i	
(13.9)
where Pi is the true probability that Di = 1.
4. Actually, the ML program chooses coefficient estimates that maximize the probability 
(or likelihood) of observing the particular set of values of the dependent variable in the sample 
1Y1, Y2, c, YN2 for a given set of Xs. For more on maximum likelihood, see Robert S. Pindyck 
and Daniel L. Rubinfeld, Economic Models and Economic Forecasts (New York: McGraw-Hill, 1998), 
pp. 51–53 and 329–330.
5. The constant term, however, needs to be adjusted. Multiply βN 0 by 3ln1p12 - ln1p224, where 
p1 is the proportion of the observations chosen if Di = 1 and p2 is the proportion of the 
observations chosen if Di = 0. See G. S. Maddala, Limited-Dependent and Qualitative Variables 
in Econometrics (Cambridge: Cambridge University Press, 1983), pp. 90–91.


400
Chapter 13  Dummy Dependent Variable Techniques 
Even Equation 13.9 is a bit cumbersome, however, since the left side of 
the equation contains the log of the ratio of Pi to 11 - Pi2, sometimes called 
the “log of the odds.” To make things simpler still, let’s adopt a shorthand 
for the logit functional form on the left side of Equation 13.9. Let’s define:
	
L:Pr1Di = 12 = lna
Pi
31 - Pi4 b	
(13.10)
The L indicates that the equation is a logit of the functional form in Equation 
13.9 (derived from Equation 13.6), and the ”Pr1Di = 12” is a reminder that 
the dependent variable is a dummy and that a DN i produced by an esti-
mated logit equation is an estimate of the probability that Di = 1. If we now 
substitute Equation 13.10 into Equation 13.9, we get:
	
L:Pr1Di = 12 = β0 + β1X1i + β2X2i	
(13.11)
Equation 13.11 will be our standard documentation format for estimated 
logit equations.
Interpreting Estimated Logit Coefficients
Once you’ve estimated a binomial logit, then hypothesis testing and the anal-
ysis of potential econometric problems can be undertaken using techniques 
similar to those discussed in previous chapters. The signs of the coefficients 
have the same meaning as they do in a linear probability model, and tests of 
hypotheses about logit coefficients can be run.6
When it comes to the economic interpretation of the estimated logit 
coefficients, however, all this changes. In particular, the absolute sizes of 
estimated logit coefficients tend to be quite different from the absolute sizes 
of estimated linear probability model coefficients for the same specification 
and the same data. What’s going on?
There are two powerful reasons for these differences. First, as you can see 
by comparing Equations 13.1 and 13.9, the dependent variable in a logit 
equation isn’t the same as the dependent variable in a linear probability 
6. Different econometric software programs provide a variety of information in support of this 
hypothesis testing, at least in part because the t-test isn’t appropriate for hypothesis testing for 
logits with small samples. Stata produces z-statistics, which require the Normal Distribution 
table in Appendix B-5. SAS, on the other hand, produces chi-square statistics, which use Table B-6. 
Our suggestion is to use p-values because they’re produced by virtually all the econometric pack-
ages and because their use doesn’t require the researcher to decide whether the t-distribution, 
normal distribution, or chi-square distribution is appropriate in any given case.


401
  The Binomial Logit Model
model. Since the dependent variable is different, it makes complete sense 
that the coefficients are different. The second reason that logit coefficients 
are different is even more dynamic. Take a look at Figure 13.2. The slope of 
the graph of the logit changes as DN i moves from 0 to 1! Thus the change in 
the probability that DN i = 1 caused by a one-unit increase in an independent 
variable (holding the other independent variables constant) will vary as we 
move from DN i = 0 to DN i = 1.
Given all this, how can we interpret estimated logit coefficients? How 
can we use them to measure the impact of an independent variable on the 
probability that Di = 1? It turns out that there are three reasonable ways of 
answering this question:
1.	 Change an average observation. Create an “average” observation by plug-
ging the means of all the independent variables into the estimated logit 
equation and then calculating an “average” DN i. Then increase the inde-
pendent variable of interest by one unit and recalculate the DN i. The dif-
ference between the two DN is tells you the impact of a one-unit increase 
in that independent variable on the probability that DN i = 1 (holding 
constant the other independent variables) for an average observation. 
This approach has the weakness of not being very meaningful when 
one or more of the independent variables is a dummy variable (after all, 
what is an average gender?), but it’s possible to work around this weak-
ness if you estimate the impact for an “average female” and an “average 
male” by setting the dummy independent variable equal first to 0 and 
then to 1.
2.	 Use a partial derivative. It turns out that if you take a derivative of the 
logit, you’ll find that the change in the expected value of DN i caused by a 
one-unit increase in X1i, holding constant the other independent vari-
ables in the equation, equals β1Pi 11 - Pi2. To use this formula, plug in 
your estimates of β1 and Pi 1βN 1 and DN i2. As you can see, the marginal 
impact of X does indeed depend on the value of DN i.
3.	 Use a rough estimate of 0.25. The previous two methods are reasonably 
accurate, but they’re hardly very handy. However, if you plug DN i = 0.5 
into β1Pi 11 - Pi2, you get the much more useful result that if you multi-
ply a logit coefficient by 0.25, you’ll get an equivalent linear probability 
model coefficient.7
7. See, for example, Jeff Wooldridge, Introductory Econometrics (Mason, OH: Southwestern, 
2009), p. 584. Wooldridge also suggests a multiple of 0.40 for converting a probit coefficient 
into a linear probability coefficient. We’ll briefly cover probits in Section 13.3.


402
Chapter 13  Dummy Dependent Variable Techniques 
On balance, what do we recommend? For all situations except those 
requiring precise accuracy, we find ourselves gravitating toward the third 
approach. To get a rough approximation of the economic meaning of a 
logit coefficient, multiply by 0.25 (or, equivalently, divide by 4). Remember, 
however, that the dependent variable in question still is the probability that 
Di = 1.
Measuring the overall fit also is not straightforward. Recall from Section 7.5  
that since the functional form of the dependent variable has been changed, 
R2 should not be used to compare the fit of a logit with an otherwise com-
parable linear probability model. In addition, don’t forget the general faults 
inherent in using R2 with equations with dummy dependent variables. Our 
suggestion is to use the mean percentage of correct predictions, R2
p, from 
Section 13.1.
To get some practice interpreting logit estimates, let’s estimate a logit on 
the same women’s labor force participation data that we used in the pre-
vious section. The OLS linear probability model estimate of that model, 
Equation 13.5, was:
	
DN i = -  0.28 - 0.38Mi + 0.09Si	
(13.5)
10.152     10.032
N = 30    R2 = .32         R2
p = .81
where:	
Di = 1 if the ith woman is in the labor force, 0 otherwise
	
Mi = 1 if the ith woman is married, 0 otherwise
	
Si  = the number of years of schooling of the ith woman
If we estimate a logit on the same data (from Table 13.1) and the same inde-
pendent variables, we obtain:
	
L:Pr1Di = 12 = -5.90 - 2.59Mi + 0.69Si	
(13.12)
11.182     10.322
N = 30    R2
p = .81        iterations = 5
Let’s compare Equations 13.5 and 13.12. As expected, the signs and general 
significance of the slope coefficients are the same. Even if we divide the logit 
coefficients by 4, as suggested earlier, they still are larger than the linear 
probability model coefficients. Despite these differences, the overall fits are 
comparable, especially after taking account of the different dependent vari-
ables and estimation techniques. In this example, then, the two estimation 
procedures differ mainly in that the logit does not produce DN is outside the 
range of 0 and 1.
∏


403
  The Binomial Logit Model
However, if the size of the sample in this example is too small for a linear 
probability model, it certainly is too small for a logit, making any in-depth 
analysis of Equation 13.12 problematic. Instead, we’re better off finding an 
example with a much larger sample.
A More Complete Example of the Use of the Binomial Logit
For a more complete example of the binomial logit, let’s look at a model of 
the probability of passing the California State Department of Motor Vehicles 
drivers’ license test. To obtain a license, each driver must pass a written and a 
behind-the-wheel test. Even though the tests are scored from 0 to 100, all that 
matters is that you pass and get your license.
Since the written test requires some boning up on traffic and safety laws, 
driving students have to decide how much time to spend studying. If they 
don’t study enough, they waste time because they have to retake the test. If 
they study too much, however, they also waste time, because there’s no bonus 
for scoring above the minimum, especially since there is no evidence that 
doing well on the written test has much to do with driving well after the test 
(this, of course, might be worth its own econometric study).
Recently, two students decided to collect data on test takers in order to 
build an equation explaining whether someone passed the Department of 
Motor Vehicles written test. They hoped that the model, and in particular the 
estimated coefficient of study time, would help them decide how much time 
to spend studying for the test. (Of course, it took more time to collect the data 
and run the model than it would have taken to memorize the entire traffic 
code, but that’s another story.)
After reviewing the literature, choosing variables, and hypothesizing signs, 
the students realized that the appropriate functional form was a binomial 
logit because their dependent variable was a dummy variable:
Di = e 1 if the ith test taker passed the test on the first try
0 if the ith test taker failed the test on the first try
They chose four independent variables (all with positive expected coefficients):
Ai = the age of the ith test taker
Hi = the number of hours the ith test taker studied (usually less 
than one hour!)
Ei  = a dummy variable equal to 1 if the ith test taker’s primary 
language was English, 0 otherwise
Ci = a dummy variable equal to 1 if the ith test taker had any  
college education, 0 otherwise


404
Chapter 13  Dummy Dependent Variable Techniques 
After collecting data from 480 test takers, the students estimated the follow-
ing equation:
	
L:Pr1Di = 12 = - 1.18 + 0.011Ai + 2.70Hi + 1.62Ei + 3.97Ci	
(13.13)
10.0092    10.542    10.342   10.992
N = 480     R2
p = .74    iterations = 5
Note how similar these results look to a typical linear regression result. All 
the estimated coefficients have the expected signs, and all but one appear to 
be significantly different from 0. Remember that the logit coefficients need 
to be divided by 4 to get meaningful estimates of the impact of the inde-
pendent variables on the probability of passing the test. Note that R2
p is .74, 
indicating that the equation correctly explained almost three quarters of the 
sample based on nothing but the four variables in Equation 13.13.
And what about the two students? Did the equation help them? How 
much did they end up deciding to study? They found that given their 
ages, their college education, and their English-speaking backgrounds, the 
expected value of DN i for each of them was quite high, even if Hi was set equal 
to 0. So what did they actually do? They studied for a half hour “just to be 
on the safe side” and passed with flying colors, having devoted more time to 
passing the test than anyone else in the history of the state.
13.3   Other Dummy Dependent Variable Techniques
Although the binomial logit is the most frequently used estimation tech-
nique for equations with dummy dependent variables, it’s by no means the 
only one. In this section, we’ll mention two alternatives, but our main goal 
is to briefly describe these estimation techniques, not to cover them in any 
detail.8
The Binomial Probit Model
The binomial probit model is an estimation technique for equations with 
dummy dependent variables that avoids the unboundedness problem of 
∏
8. For more, see G. S. Maddala, Limited Dependent Variables and Qualitative Variables in Econometrics 
(Cambridge: Cambridge University Press, 1983) and T. Amemiya, “Qualitative Response Models: 
A Survey,” Journal of Economic Literature, Vol. 19, pp. 1483–1536. These surveys also cover 
additional techniques, like the Tobit model, that are useful with bounded dependent variables 
or other special situations.


405
  Other Dummy Dependent Variable Techniques
the linear probability model by using a variant of the cumulative normal 
distribution.
	
Pi =
1
22π
 3
Zi
- ∞
 e-s2>2 ds	
(13.14)
where:	
Pi = the probability that the dummy variable Di = 1
	
Zi = β0 + β1X1i + β2X2i
	
s  = a standardized normal variable
As different as this probit looks from the logit that we examined in the pre-
vious section, it can be rewritten to look quite familiar:
	
Zi = Φ-11Pi2 = β0 + β1X1i + β2X2i	
(13.15)
where Φ-1 is the inverse of the normal cumulative distribution function. 
Probit models typically are estimated by applying maximum likelihood tech-
niques to the model in the form of Equation 13.14, but the results often are 
presented in the format of Equation 13.15.
The fact that both the logit and the probit are cumulative distribution 
functions means that the two have similar properties. For example, a graph 
of the probit looks almost exactly like the logit in Figure 13.2. In addition, 
the probit has the same requirement of a fairly large sample before hypoth-
esis testing becomes meaningful. Finally, R2 continues to be of questionable 
value as a measure of overall fit.
For an example of a probit, let’s estimate one using the same women’s 
labor force participation data employed in the previous logit and linear prob-
ability examples (standard errors in parentheses):
	
ZN i = Φ-11Pi2 = -  3.44 - 1.44Mi + 0.40Si	
(13.16)
10.622    10.172
N = 30      R2
p = 0.81     iterations = 4
Compare this result with Equation 13.12 from the previous section. Note 
that except for a slight difference in the scale of the coefficients, the logit and 
probit models provide virtually identical results in this example.
Multinomial Models
In many cases, there are more than two qualitative choices available. In some 
cities, for instance, a commuter has a choice of car, bus, or subway for the trip 
to work. How could we build and estimate a model of choosing from more 
than two alternatives?
®


406
Chapter 13  Dummy Dependent Variable Techniques 
One answer is to hypothesize that choices are made sequentially and to 
model a multichoice decision as a series of binary decisions. For example, we 
might hypothesize that the commuter would first decide whether to drive to 
work, and we could build a binary model of car versus public transportation. 
For those commuters who choose public transportation, the next step would 
be to choose whether to take the bus or the subway, and we could build a 
second binary model of that choice. This method, called a sequential binary 
logit, is cumbersome and at times unrealistic, but it does allow a researcher 
to use a binary technique to model an inherently multichoice decision.
If a decision among more than two alternatives truly is made simultane-
ously, then the sequential binary logit can’t be used. There are a number of 
alternative estimation procedures that are appropriate in this situation, but 
unfortunately they are beyond the scope of this text.9
13.4   Summary
	 1.	 A linear probability model is a linear-in-the-coefficients equation 
used to explain a dummy dependent variable 1Di2. DN i is an estimate 
of the probability that Di equals 1.
	 2.	 The estimation of a linear probability model with OLS faces at least 
three major problems:
a.	 R2 is not an accurate measure of overall fit.
b.	The expected value of DN i is not limited by 0 and 1.
c.	 The error term is neither homoskedastic nor normally distributed.
	 3.	 When measuring the overall fit of equations with dummy dependent 
variables, an alternative to R2 is R2
p, the average percentage of the ob-
servations in the sample that a particular estimated equation would 
have explained correctly.
	 4.	 The binomial logit is an estimation technique for equations with 
dummy dependent variables that avoids the unboundedness problem 
of the linear probability model by using a variant of the cumulative 
logistic function:
L:Pr1Di = 12 = lna
Pi
31 - Pi4 b = β0 + β1X1i + β2X2i
9. These alternative procedures include the multinomial logit and the ordered logit. See 
William H. Greene, Econometric Analysis (Boston: Pearson Education, 2012), pp. 803–806 and 
pp. 824–827.


407
Exercises
	 5.	 The binomial logit is best estimated using the maximum likelihood 
(ML) technique and a large sample. A slope coefficient from a logit 
measures the impact of a one-unit increase of the independent vari-
able in question (holding the other explanatory variables constant) 
on the log of the odds of a given choice.
	 6.	 The binomial probit model is an estimation technique for equations 
with dummy dependent variables that uses the cumulative normal 
distribution function. The binomial probit has properties quite similar 
to those of the binomial logit.
Exercises
(The answers to the even-numbered exercises are in Appendix A.)
	 1.	 Write the meaning of each of the following terms without referring 
to the book (or your notes), and compare your definition with the 
version in the text for each:
a.	binomial logit (p. 397)
b.	binomial probit (p. 404)
c.	 interpreting estimated logit coefficients (p. 400)
d.	linear probability model (p. 390)
e.	 maximum likelihood (p. 399)
f.	 R2
p (p. 394)
g.	sequential binary logit (p. 406)
	 2.	 R. Amatya10 estimated the following logit model of birth control for 
1,145 continuously married women aged 35 to 44 in Nepal:
L:Pr1Di = 12 = -  4.47 + 2.03WNi + 1.45MEi
10.362        10.142
where:	
Di
 = 1 if the ith woman has ever used a recognized 
form of birth control, 0 otherwise
	
WNi = 1 if the ith woman wants no more children, 0 
otherwise
	
MEi  = number of methods of birth control known to the 
ith woman
∏
10. Ramesh Amatya, “Supply-Demand Analysis of Differences in Contraceptive Use in Seven 
Asian Nations” (paper presented at the Annual Meetings of the Western Economic Association, 
1988, Los Angeles).


408
Chapter 13  Dummy Dependent Variable Techniques 
a.	Explain the theoretical meaning of the coefficients for WN and 
ME. How would your answer differ if this were a linear probability 
model?
b.	Do the signs, sizes, and significance of the estimated slope coeffi-
cients meet your expectations? Why or why not?
c.	 What is the theoretical significance of the constant term in this 
equation?
d.	If you could make one change in the specification of this equation, 
what would it be? Explain your reasoning.
	 3.	 Because their college had just upgraded its residence halls, two 
seniors decided to build a model of the decision to live on campus. 
They collected data from 533 upper-class students (first-year stu-
dents were required to live on campus) and estimated the following 
equation:
L:Pr1Di = 12 = 3.26 + 0.03UNITi - 0.13ALCOi - 0.99YEARi - 0.39GREKi
10.042          10.082            10.122           10.212
N = 533      R2
p = .668      iterations = 4
where:	
Di
 = 1 if the ith student lived on campus, 0 otherwise
	
UNITi  = the number of academic units the ith student 
was taking
	
ALCOi = the nights per week that the ith student con-
sumed alcohol
	
YEARi  = 2 if the ith student was a sophomore, 3 if a 
junior, and 4 if a senior
	
GREKi = 1 if the ith student was a member of a fraternity/
sorority, 0 otherwise
a.	The two seniors expected UNIT to have a positive coefficient and 
the other variables to have negative coefficients. Do the results 
support these hypotheses?
b.	What problem do you see with the definition of the YEAR vari-
able? What constraint does this definition place on the estimated 
coefficients?
c.	 Carefully state the meaning of the coefficient of ALCO and analyze 
the size of the coefficient. (Hint: Be sure to discuss how the size of 
the coefficient compares with your expectations.)
d.	If you could add one variable to this equation, what would it be? 
Explain.
∏


409
Exercises
	 4.	 Return to our data on women’s labor force participation and consider 
the possibility of adding Ai, the age of the ith woman, to the equation. 
Be careful when you develop your expected sign and functional form 
because the expected impact of age on labor force participation is diffi-
cult to pin down. For instance, some women drop out of the labor force 
when they get married, but others continue working even while they’re 
raising their children. Still others work until they get married, stay at 
home with young children, and then return to the workforce once 
the children reach school age. Malcolm Cohen et al., for example, found 
the age of a woman to be relatively unimportant in determining labor 
force participation, except for women who were 65 and older and were 
likely to have retired.11 The net result for our model is that age appears 
to be a theoretically irrelevant variable. A possible exception, however, is 
a dummy variable equal to 1 if the ith woman is 65 or over, 0 otherwise.
a.	Look over the data set in Table 13.1. What problems do you see 
with adding an independent variable equal to 1 if the ith woman is 
65 or older and 0 otherwise?
b.	To get practice in actually estimating your own linear probability 
and logit equations, test the possibility that age 1Ai2 is actually a 
relevant variable in our women’s labor force participation model. 
That is, take the data from Table 13.1 and estimate linear probability 
and logit versions. Then use our specification criteria to compare 
your equation with the parallel version in the text (without Ai). 
Explain why you do or do not think that age is a relevant variable. 
(Hint: Be sure to calculate R2
p.)
	 5.	 In 2008, Goldman and Romley12 studied hospital demand by analyzing 
how 8,721 Medicare-covered pneumonia patients chose from among 
117 hospitals in the greater Los Angeles area. The authors concluded that 
clinical quality (as measured by a low pneumonia mortality rate) played 
a smaller role in hospital choice than did a variety of other factors.
	
	   Let’s focus on a subset of the Goldman–Romley sample: the 499 
patients who chose either the UCLA Medical Center or the nearby 
Cedars Sinai Medical Center. Typically, economists would expect price 
to have a major influence on such a choice, but Medicare patients pay 
11. Malcolm Cohen, Samuel A. Rea, Jr., and Robert I. Lerman, A Micro Model of Labor Supply 
(Washington, D.C.: U.S. Bureau of Labor Statistics, 1970), p. 212.
12. Dana Goldman and John Romley, “Hospitals as Hotels: The Role of Patient Amenities in 
Hospital Demand,” NBER Working Paper 14619, December 2008. We appreciate the permission 
of the authors to use a portion of their data set.


410
Chapter 13  Dummy Dependent Variable Techniques 
roughly the same price no matter what hospital they choose. Instead, 
factors like the distance the patient lives from the hospital and the age 
and income of the patient become potentially important factors:
L:Pr1Di = 12 = 4.41 - 0.38DISTANCEi - 0.072INCOMEi - 0.29OLDi	
(13.17)
10.052         
10.0362         10.312
N = 499                  R2
p = .66               iterations = 8
where:	
Di
 = 1 if the ith patient chose Cedars Sinai, 0 if 
they chose UCLA
	
DISTANCEi = the distance from the ith patient’s home 
(according to zip code) to Cedars Sinai 
minus the distance from that point to the 
UCLA Medical Center (in miles)
	
INCOMEi  = the income of the ith patient (as measured 
by the average income of their zip code in 
thousands of dollars)
	
OLDi
 = 1 if the ith patient was older than 75, 0 
otherwise
a.	Create and test appropriate hypotheses about the coefficient of 
DISTANCE.
b.	Carefully state the meaning of the estimated coefficient of DISTANCE 
in terms of the “per mile” impact on the probability of choosing 
Cedars Sinai Medical Center.
c.	 Think about the definition of DISTANCE. Why do you think we 
defined DISTANCE as the difference between the distances as 
opposed to entering the distance to Cedars and the distance to 
UCLA as two different independent variables?
d.	This data set is available on our Web site (www.pearsonhighered.
com/studenmund) as datafile = HOSPITAL13. Load the data into 
your computer and use Stata or your computer’s regression pro-
gram to estimate the linear probability model version of this equa-
tion. What is the coefficient of DISTANCE in your estimate? Which 
do you prefer, the logit or the linear probability model? Explain.
e.	 (optional) Now create a slope dummy by adding OLD*DISTANCE 
to Equation 13.17 and estimating a new logit equation. Why do 
you think we’re suggesting this particular slope dummy? Create and 
test the appropriate hypotheses about the slope dummy. Which 
equation do you prefer, Equation 13.17 or the new slope dummy 
logit? Explain.
∏
