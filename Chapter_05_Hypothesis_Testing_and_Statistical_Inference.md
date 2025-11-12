# Chapter 5: Hypothesis Testing and Statistical Inference

**Pages:** 135-176

---

115
Chapter 5
Hypothesis Testing and 
Statistical Inference
5.1  What Is Hypothesis Testing?
5.2  The t-Test
5.3  Examples of t-Tests
5.4  Limitations of the t-Test
5.5  Confidence Intervals
5.6  The F-Test
5.7  Summary and Exercises
5.8  Appendix: Econometric Lab #3
In this chapter, we return to the essence of econometrics—an effort to quan-
tify economic relationships by analyzing sample data—and ask what conclu-
sions we can draw from this quantification. Hypothesis testing goes beyond 
calculating estimates of the true population parameters to a much more 
complex set of questions. Hypothesis testing and statistical inference allow 
us to answer important questions about the real world from a sample. Is it 
likely that our result could have been obtained by chance? Would the results 
generated from our sample lead us to reject our original theories? How con-
fident can we be that our estimate is close to the true value of the parameter? 
This chapter starts with a brief introduction to the topic of hypothesis testing. 
We then examine the t-test, typically used for hypothesis tests of individual 
regression coefficients. We next look at the confidence interval, a tool for 
evaluating the precision of our estimates, and we end the chapter by learn-
ing how to use the F-test to determine whether whole groups of coefficients 
affect the dependent variable.
Hypothesis testing and the t-test should be familiar topics to readers with 
strong backgrounds in statistics, who are encouraged to skim this chapter and 
focus on only those applications that seem somewhat new. The development 


116
Chapter 5  Hypothesis Testing and Statistical Inference
of hypothesis testing procedures is explained here in terms of the regression 
model, however, so parts of the chapter may be instructive even to those 
already skilled in statistics.
Our approach will be classical in nature, since we assume that the sample 
data are our best and only information about the population. An alternative, 
Bayesian statistics, uses a completely different definition of probability and 
does not use the sampling distribution concept.1
5.1   What Is Hypothesis Testing?
Hypothesis testing is used in a variety of settings. The Food and Drug Admin-
istration (FDA), for example, tests new products before allowing their sale. 
If the sample of people exposed to the new product shows some side effect 
significantly more frequently than would be expected to occur by chance, 
the FDA is likely to withhold approval of marketing that product. Similarly, 
economists have been statistically testing various relationships between 
consumption and income for almost a century; theories developed by John 
Maynard Keynes and Milton Friedman, among others, have been tested on mac-
roeconomic and microeconomic data sets.
Although researchers are always interested in learning whether the theory 
in question is supported by estimates generated from a sample of real-world 
observations, it’s almost impossible to prove that a given hypothesis is correct. 
All that can be done is to state that a particular sample conforms to a particu-
lar hypothesis. Even though we cannot prove that a given theory is “correct” 
using hypothesis testing, we often can reject a given hypothesis with a certain 
level of confidence. In such a case, the researcher concludes that it is very 
unlikely that the sample result would have been observed if the hypothesized 
theory were correct.
Classical Null and Alternative Hypotheses
The first step in hypothesis testing is to state the hypotheses to be tested. 
This should be done before the equation is estimated because hypotheses 
1. Bayesians, by being forced to state explicitly their prior expectations, tend to do most of their 
thinking before estimation, which is a good habit for a number of important reasons. For more 
on this approach, see Peter Kennedy, A Guide to Econometrics (Malden, MA: Blackwell, 2008), 
pp. 213–231. For more advanced coverage, see Tony Lancaster, An Introduction to Bayesian Econo-
metrics (Oxford: Blackwell Publishing, 2004).


117
  What Is Hypothesis Testing?
developed after estimation run the risk of being justifications of particular 
results rather than tests of the validity of those results.
The null hypothesis typically is a statement of the values that the 
researcher does not expect. The notation used to specify the null hypothesis 
is “H0:” followed by a statement of the range of values you do not expect. For 
example, if you expect a positive coefficient, then you don’t expect a zero or 
negative coefficient, and the null hypothesis is:
	
Null hypothesis H0: β … 0  (the values you do not expect)
The alternative hypothesis typically is a statement of the values that the 
researcher expects. The notation used to specify the alternative hypothesis is 
“HA:” followed by a statement of the range of values you expect. To continue 
our previous example, if you expect a positive coefficient, then the alterna-
tive hypothesis is:
Alternative hypothesis HA: β 7 0  (the values you expect)
To test yourself, take a moment and think about what the null and alternative 
hypotheses will be if you expect a negative coefficient. That’s right, they’re:
	
H0: β Ú 0
	
HA: β 6 0
The above hypotheses are for a one-sided test because the alternative 
hypotheses have values on only one side of the null hypothesis. Another 
approach is to use a two-sided test (or a two-tailed test) in which the alter-
native hypothesis has values on both sides of the null hypothesis. For a 
two-sided test around zero, the null and alternative hypotheses are:
	
H0: β = 0
	
HA: β ≠0
We should note that there are a few rare cases in which we must violate 
our rule that the value you expect goes in the alternative hypothesis. Classical 
hypothesis testing requires that the null hypothesis contain the equal sign 
in some form (whether it be =, …, or Ú). This requirement means that 
researchers are forced to put the value they expect in the null hypothesis if 
their expectation includes an equal sign. This typically happens when the 
researcher specifies a particular value rather than a range. Luckily, such excep-
tions are unusual in elementary applications.
With the exception of the unusual cases previously mentioned, economists 
always put what they expect in the alternative hypothesis. This allows us to 
make rather strong statements when we reject a null hypothesis. However, we 


118
Chapter 5  Hypothesis Testing and Statistical Inference
can never say that we accept the null hypothesis; we must always say that we 
cannot reject the null hypothesis. As put by Jan Kmenta:
Just as a court pronounces a verdict as not guilty rather than  
innocent, so the conclusion of a statistical test is do not reject rather 
than accept.2
Type I and Type II Errors
The typical testing technique in econometrics is to hypothesize an expected sign 
(or value) for each regression coefficient (except the constant term) and then to 
determine whether to reject the null hypothesis. Since the regression coefficients 
are only estimates of the true population parameters, it would be unrealistic 
to think that conclusions drawn from regression analysis will always be right.
There are two kinds of errors we can make in such hypothesis testing:
Type I: We reject a true null hypothesis.
Type II: We do not reject a false null hypothesis.
We will refer to these errors as Type I and Type II Errors, respectively.
Suppose we have the following null and alternative hypotheses:
H0: β … 0
HA: β 7 0
Even if the true parameter β is not positive, the particular estimate obtained 
by a researcher may be sufficiently positive to lead to the rejection of the null 
hypothesis that β … 0. This is a Type I Error; we have rejected the truth!
Alternatively, it’s possible to obtain an estimate of β that is close enough to 
zero (or negative) to be considered “not significantly positive.” Such a result 
may lead the researcher to “accept”3 the hypothesis that β … 0 when in truth 
β 7 0. This is a Type II Error; we have failed to reject a false null hypothesis!
As an example of Type I and Type II Errors, let’s suppose that you’re on 
a jury in a murder case.4 In such a situation, the presumption of “innocent 
until proven guilty” implies that:
H0: The defendant is innocent.
HA: The defendant is guilty.
2. Jan Kmenta, Elements of Econometrics (Ann Arbor: University of Michigan Press, © 1986), 
p. 112. (Emphasis added.)
3. We will consistently put the word accept in quotes whenever we use it. In essence, “accept” 
means do not reject.
4. This example comes from and is discussed in much more detail in Ed Leamer, Specification 
Searches (New York: John Wiley and Sons, 1978), pp. 93–98.


119
  What Is Hypothesis Testing?
What would a Type I Error be? Rejecting the null hypothesis would mean 
sending the defendant to jail, so a Type I Error, rejecting a true null hypoth-
esis, would mean:
Type I Error = Sending an innocent defendant to jail.
Similarly,
Type II Error = Freeing a guilty defendant.
Most reasonable jury members would want both levels of error to be quite 
small, but such certainty is almost impossible. After all, couldn’t there be a 
mistaken identification or a lying witness? In the real world, decreasing the 
probability of a Type I Error (sending an innocent defendant to jail) means 
increasing the probability of a Type II Error (freeing a guilty defendant). If we 
never sent an innocent defendant to jail, we’d be freeing quite a few murderers!
Decision Rules of Hypothesis Testing
A decision rule is a method of deciding whether to reject a null hypothesis. 
Typically, a decision rule involves comparing a sample statistic with a pre­
selected critical value found in tables such as those in the end of this text.
A decision rule should be formulated before regression estimates are 
obtained. The range of possible values of βN  is divided into two regions, 
an “acceptance” region and a rejection region, where the terms are expressed 
relative to the null hypothesis. To define these regions, we must determine a 
critical value (or, for a two-tailed test, two critical values) of βN . Thus, a critical 
value is a value that divides the “acceptance” region from the rejection region 
when testing a null hypothesis. Graphs of these “acceptance” and rejection 
regions are presented in Figures 5.1 and 5.2.
To use a decision rule, we need to select a critical value. Let’s suppose that 
the critical value is 1.8. If the observed βN  is greater than 1.8, we can reject the 
null hypothesis that β is zero or negative. To see this, take a look at Figure 5.1. 
Any βN  above 1.8 can be seen to fall into the rejection region, whereas any βN  
below 1.8 can be seen to fall into the “acceptance” region.
The rejection region measures the probability of a Type I Error if the null 
hypothesis is true. Some students react to this news by suggesting that we 
make the rejection region as small as possible. Unfortunately, decreasing the 
chance of a Type I Error means increasing the chance of a Type II Error (not 
rejecting a false null hypothesis). If you make the rejection region so small 
that you almost never reject a true null hypothesis, then you’re going to be 
unable to reject almost every null hypothesis, whether they’re true or not! As 
a result, the probability of a Type II Error will rise.


120
Chapter 5  Hypothesis Testing and Statistical Inference
0
Distribution of ds
Probability of
Type I Error
1.8
d
“Acceptance” Region
Rejection
Region
N
N
Figure 5.1  “Acceptance” and Rejection Regions for a One-Sided Test of β
For a one-sided test of H0: β … 0 vs. HA: β 7 0, the critical value divides the distribution 
of βN  (centered around zero on the assumption that H0 is true) into “acceptance” and 
rejection regions.
0
Distribution of ds
Probability of
Type I Error
“Acceptance” Region
Rejection
Region
Rejection
Region
dN
N
Figure 5.2  “Acceptance” and Rejection Regions for a Two-Sided Test of β
For a two-sided test of H0: β = 0 vs. HA: β ≠0, we divided the distribution of βN  into an 
“acceptance” region and two rejection regions.


121
THE t-TEST
Given that, how do you choose between Type I and Type II Errors? The 
answer is easiest if you know that the cost (to society or the decision maker) 
of making one kind of error is dramatically larger than the cost of making the 
other. If you worked for the FDA, for example, you’d want to be very sure that 
you hadn’t released a product that had horrible side effects. We’ll discuss this 
dilemma for the t-test on page 126.
5.2   The t-Test
Econometricians generally use the t-test to test hypotheses about individual 
regression slope coefficients. Tests of more than one coefficient at a time 
(joint hypotheses) are typically done with the F-test, presented in Section 5.6.
The t-test is easy to use because it accounts for differences in the units of 
measurement of the variables and in the standard deviations of the estimated 
coefficients. More important, the t-statistic is the appropriate test to use when 
the stochastic error term is normally distributed and when the variance of that 
distribution must be estimated. Since these usually are the case, the use of the 
t-test for hypothesis testing has become standard practice in econometrics.
The t-Statistic
For a typical multiple regression equation:
	
Yi = β0 + β1X1i + β2X2i + ei	
(5.1)
we can calculate t-values for each of the estimated coefficients in the equa-
tion. For reasons that will be explained in Section 7.1, t-tests are usually done 
only on the slope coefficients; for these, the relevant form of the t-statistic 
for the kth coefficient is
	
tk =
1βN k - βH02
SE1βN k2   1k = 1, 2, c, K2	
(5.2)
where:	
βN k
 = the estimated regression coefficient of the kth variable
	
βH0
 = the border value (usually zero) implied by the null hy-
pothesis for βk
	
SE1βN k2 = the estimated standard error of βN k (that is, the square 
root of the estimated variance of the distribution of the 
βN k; note that there is no “hat” attached to SE because 
SE is already defined as an estimate)


122
Chapter 5  Hypothesis Testing and Statistical Inference
How do you decide what border is implied by the null hypothesis? Some null 
hypotheses specify a particular value. For these, βH0 is simply that value; if 
H0: β = S, then βH0 = S. Other null hypotheses involve ranges, but we are 
concerned only with the value in the null hypothesis that is closest to the 
border between the “acceptance” region and the rejection region. This border 
value then becomes the βH0. For example, if H0: β Ú 0 and HA: β 6 0, then 
the value in the null hypothesis closest to the border is zero, and βH0 = 0.
Since most regression hypotheses test whether a particular regression coef-
ficient is significantly different from zero, βH0 is typically zero. Zero is partic-
ularly meaningful because if the true β equals zero, then the variable doesn’t 
belong in the equation. Before we drop the variable from the equation and 
effectively force the coefficient to be zero, however, we need to be careful and 
test the null hypothesis that β = 0. Thus, the most-used form of the t-statistic 
becomes
	
tk = 1βN k - 02
SE1βN k2   1k = 1, 2, c, K2
which simplifies to
	
tk =
βN k
SE1βN k2  1k = 1, 2, c, K2	
(5.3)
or the estimated coefficient divided by the estimate of its standard error. This 
is the t-statistic formula used by most computer programs.
For an example of this calculation, let’s consider the equation for the 
check volume at Woody’s restaurants from Section 3.2:
	
YNi = 102,192 - 9075Ni + 0.3547Pi + 1.288Ii	
(5.4)
120532    10.07272   10.5432
t = -4.42      4.88      2.37
N = 33  R  2 = .579
In Equation 5.4, the numbers in parentheses underneath the estimated 
regression coefficients are the estimated standard errors of the estimated βN s, 
and the numbers below them are t-values calculated according to Equation 5.3. 
The format used to document Equation 5.4 is the one we’ll use whenever 
possible throughout this text. Note that the sign of the t-value is always the 
same as that of the estimated regression coefficient, and the standard error is 
always positive.
Using the regression results in Equation 5.4, let’s calculate the t-value for 
the estimated coefficient of P, the population variable. Given the values in 


123
THE t-TEST
Equation 5.4 of 0.3547 for βN P and 0.0727 for SE1βN P2, and given H0: βP … 0, 
the relevant t-value is indeed 4.88, as specified in Equation 5.4:
	
tP =
βN P
SE1βN P2
= 0.3547
0.0727 = 4.88
The larger in absolute value this t-value is, the greater the likelihood that the 
estimated regression coefficient is different from zero.
The Critical t-Value and the t-Test Decision Rule
To decide whether to reject or not to reject a null hypothesis based on a 
calculated t-value, we use a critical t-value. A critical t-value is the value that 
distinguishes the “acceptance” region from the rejection region. The critical 
t-value, tc, is selected from a t-table (see Statistical Table B-1 in the back of 
the book) depending on whether the test is one-sided or two-sided, on the 
level of Type I Error you specify, and on the degrees of freedom, which we 
have defined as the number of observations minus the number of coefficients 
estimated (including the constant) or N - K - 1. The level of Type I Error in a 
hypothesis test is also called the level of significance of that test and will be dis-
cussed in more detail later in this section. The t-table was created to save time 
during research; it consists of critical t-values given specific areas underneath 
curves such as those in Figure 5.1 for Type I Errors. A critical t-value is thus a 
function of the probability of Type I Error that the researcher wants to specify.
Once you have obtained a calculated t-value tk and a critical t-value tc, you 
reject the null hypothesis if the calculated t-value is greater in absolute value 
than the critical t-value and if the calculated t-value has the sign implied by HA.
Thus, the rule to apply when testing a single regression coefficient is that 
you should:
Reject H0 if tk 7 tc and if tk also has the sign implied by HA. Do not 
reject H0 otherwise.
This decision rule works for calculated t-values and critical t-values for one-
sided hypotheses around zero:
	
H0: βk … 0
	
HA: βk 7 0
	
H0: βk Ú 0
	
HA: βk 6 0


124
Chapter 5  Hypothesis Testing and Statistical Inference
for two-sided hypotheses around zero:
	
H0: βk = 0
	
HA: βk ≠0
for one-sided hypotheses based on hypothesized values other than zero:
	
H0: βk … S
	
HA: βk 7 S
	
H0: βk Ú S
	
HA: βk 6 S
and for two-sided hypotheses based on hypothesized values other than zero:
	
H0: βk = S
	
HA: βk ≠S
The decision rule is the same: Reject the null hypothesis if the appropriately 
calculated t-value, tk, is greater in absolute value than the critical t-value, tc, as 
long as the sign of tk is the same as the sign of the coefficient implied in HA. 
Otherwise, do not reject H0. Always use Equation 5.2 whenever the hypoth-
esized value is not zero.
Statistical Table B-1 contains the critical values tc for varying degrees of 
freedom and levels of significance. The columns indicate the levels of sig-
nificance according to whether the test is one-sided or two-sided, and the 
rows indicate the degrees of freedom. For an example of the use of this table 
and the decision rule, let’s return to the Woody’s restaurant example and, in 
particular, to the t-value for βN P calculated in the previous section. Recall that 
we hypothesized that population’s coefficient would be positive, so this is a 
one-sided test:
	
H0: βp … 0
	
HA: βp 7 0
There are 29 degrees of freedom (equal to N - K - 1, or 33 - 3 - 1) in this 
regression, so the appropriate t-value with which to test the calculated t-value 
is a one-tailed critical t-value with 29 degrees of freedom. To find this value, 
pick a level of significance, say 5 percent, and turn to Statistical Table B-1. 
Take a look for yourself. Do you agree that the number there is 1.699?
Given that, should you reject the null hypothesis? The decision rule is to 
reject H0 if tk 7 tc and if tk has the sign implied by HA. Since the 5-percent, 
one-sided, 29 degrees of freedom critical t-value is 1.699, and since the sign 
implied by HA is positive, the decision rule (for this specific case) becomes:
	
Reject H0 if tP 7 1.699 and if tP is positive


125
THE t-TEST
or, combining the two conditions:
	
Reject H0 if tP 7 1.699
What is tP? In the previous section, we found that tP was +4.88, so we would 
reject the null hypothesis and conclude that population does indeed tend to 
have a positive relationship with Woody’s check volume (holding the other 
variables in the equation constant).
Note from Statistical Table B-1 that the critical t-value for a one-tailed test 
at a given level of significance is exactly equal to the critical t-value for a two-
tailed test at twice the level of significance as the one-tailed test. This rela-
tionship between one-sided and two-sided tests is illustrated in Figure 5.3. 
The critical value tc = 1.699 is for a one-sided, 5-percent level of signifi-
cance, but it also represents a two-sided, 10-percent level of significance 
because if one tail represents 5 percent, then both tails added together rep-
resent 10 percent.
0
Area = .05
1.699
5% One-Sided
Level of Signiﬁcance
-1.699
10% Two-Sided Level of Signiﬁcance
Figure 5.3  One-Sided and Two-Sided t-Tests
The tc for a one-sided test at a given level of significance is equal exactly to the tc for a 
two-sided test with twice the level of significance of the one-sided test. For example,  
tc = 1.699 for a 10-percent two-sided test and for a 5-percent one-sided test (for 29  
degrees of freedom).


126
Chapter 5  Hypothesis Testing and Statistical Inference
Choosing a Level of Significance
To complete the previous example, it was necessary to pick a level of sig-
nificance before a critical t-value could be found in Statistical Table B-1. The 
words “significantly positive” usually carry the statistical interpretation that 
H0 1β … 02 was rejected in favor of HA 1β 7 02 according to the preestab-
lished decision rule, which was set up with a given level of significance. The 
level of significance indicates the probability of observing an estimated 
t-value greater than the critical t-value if the null hypothesis were correct. It 
measures the amount of Type I Error implied by a particular critical t-value. 
If the level of significance is 10 percent and we reject the null hypothesis 
at that level, then this result would have occurred only 10 percent of the time 
that the null hypothesis was indeed correct.
How should you choose a level of significance? Most beginning econome-
tricians (and many published ones, too) assume that the lower the level of 
significance, the better. After all, they say, doesn’t a low level of significance 
guarantee a low probability of making a Type I Error? Unfortunately, an 
extremely low level of significance also dramatically increases the probability 
of making a Type II Error. Therefore, unless you’re in the unusual situation of 
not caring about mistakenly “accepting” a false null hypothesis, minimizing 
the level of significance is not good standard practice.
Instead, we recommend using a 5-percent level of significance except in 
those circumstances when you know something unusual about the relative 
costs of making Type I and Type II Errors. If you know that a Type II Error 
will be extremely costly, for example, then it makes sense to consider using a 
10-percent level of significance when you determine your critical value. Such 
judgments are difficult, however, so we encourage beginning researchers to 
adopt a 5-percent level of significance as standard.
If we can reject a null hypothesis at the 5-percent level of significance, 
we can summarize our results by saying that the coefficient is “statistically 
significant” at the 5-percent level. Since the 5-percent level is arbitrary, we 
shouldn’t jump to conclusions about the value of a variable simply because 
its coefficient misses being significant by a small amount; if a different level 
of significance had been chosen, the result might have been different.
Some researchers produce tables of regression results, typically without 
hypothesized signs for their coefficients, and then mark “significant” coef-
ficients with asterisks. The asterisks indicate when the t-score is larger in 
absolute value than the two-sided 10-percent critical value (which merits one 
asterisk), the two-sided 5-percent critical value (**), or the two-sided 1-percent 
critical value (***). Such a use of the t-value should be regarded as a descrip-
tive rather than a hypothesis-testing use of statistics.


127
THE t-TEST
Now and then researchers will use the phrase “degree of confidence” or 
“level of confidence” when they test hypotheses. What do they mean? The 
level of confidence is nothing more than 100 percent minus the level of signifi-
cance. Thus a t-test for which we use a 5-percent level of significance can also 
be said to have a 95-percent level of confidence. Since the two terms have 
identical meanings, we will use level of significance throughout this text. 
Another reason we prefer the term level of significance to level of confidence 
is to avoid any possible confusion with the related concept of confidence 
intervals, which will be covered in Section 5.5.
Some researchers avoid choosing a level of significance by simply stating 
the lowest level of significance possible for each estimated regression coeffi-
cient. The resulting significance levels are called p-values.
p-Values
There’s an alternative to the t-test based on a measure called the p-value, or 
marginal significance level. A p-value for a t-score is the probability of observ-
ing a t-score that size or larger (in absolute value) if the null hypothesis were 
true. Graphically, it’s two times the area under the curve of the t-distribution 
between the absolute value of the actual t-score and infinity.
A p-value is a probability, so it runs from 0 to 1. It tells us the lowest level 
of significance at which we could reject the null hypothesis (assuming that 
the estimate is in the expected direction). A small p-value casts doubt on the 
null hypothesis, so to reject a null hypothesis, we need a low p-value.
How do we calculate a p-value? One option would be to comb through 
pages and pages of statistical tables, looking for the level of significance that 
exactly matches the regression result. That could take days! Luckily, standard 
regression software packages calculate p-values automatically and print them 
out for every estimated coefficient.5 You’re thus able to read p-values off your 
regression output just as you would your βN s. Be careful, however, because 
virtually every regression package prints out p-values for two-sided alternative 
hypotheses. Such two-sided p-values include the area in both “tails,” so two-
sided p-values are twice the size of one-sided ones. If your test is one-sided, 
you need to divide the p-value in your regression output by 2 before doing 
any tests.
How would you use a p-value to run a t-test? If your chosen level of sig-
nificance is 5 percent and the p-value is less than .05, then you can reject 
5. Different software packages use different names for p-values. Stata uses P 7 t . To see this, turn 
to page 77 and look in the center of the top of the page. Note that such p-values are for H0: β = 0.


128
Chapter 5  Hypothesis Testing and Statistical Inference
your null hypothesis as long as the sign is in the expected direction. Thus the 
p-value decision rule is:
Reject H0 if p@valueK 6 the level of significance and if βN K has the sign 
implied by HA. Do not reject H0 otherwise.
Let’s look at an example of the use of a p-value to run a t-test. If we return 
to the Woody’s example of Equation 5.4 and run a one-sided test on the coef-
ficient of I, the income variable, we have the following null and alternative 
hypotheses:
	
H0: βI … 0
	
HA: βI 7 0
As you can see from the regression output for the Woody’s equation on 
page 77, the p-value for βN I is .025. This is a two-sided p-value and we’re run-
ning a one-sided test, so we need to divide .025 by 2, getting .0125. Since 
.0125 is lower than our chosen level of significance of .05, and since the sign 
of βN I is positive and agrees with that in HA, we can reject H0. Not surprisingly, 
this is the same result we’d get if we ran a conventional t-test.
p-values have a number of advantages. They’re easy to use, and they allow 
readers of research to choose their own levels of significance instead of being 
forced to use the level chosen by the original researcher. In addition, p-values 
convey information to the reader about the relative strength with which we 
can reject a null hypothesis. Because of these benefits, many researchers use 
p-values on a consistent basis.
Despite these advantages, we will not use p-values in this text. We think that 
beginning researchers benefit from learning the standard t-test procedure, par-
ticularly since it’s more likely to force them to remember to hypothesize the 
sign of the coefficient and to use a one-sided test when a particular sign can be 
hypothesized. In addition, if you know how to use the standard t-test approach, 
it’s easy to switch to the p-value approach, but the reverse isn’t necessarily true.
However, we acknowledge that practicing econometricians today spend 
far more energy estimating models and coefficients than they spend test-
ing hypotheses. This is because most researchers are more confident in their 
theories (say, that demand curves slope downward) than they are in the qual-
ity of their data or their regression methods. In such situations, where the 
statistical tools are being used more for descriptive purposes than for hypoth-
esis testing purposes, it’s clear that the use of p-values saves time and conveys 
more information than does the standard t-test procedure.


129
EXAMPLES OF t-TESTS
5.3   Examples of t-Tests
Examples of One-Sided t-Tests
The most common use of the one-sided t-test is to determine whether a 
regression coefficient is significantly different from zero in the direction pre-
dicted by theory. Let’s face it: if you expect a positive sign for a coefficient and 
you get a negative βN , it’s hard to reject the possibility that the true β might 
be negative (or zero). On the other hand, if you expect a positive sign and 
get a positive βN , things get a bit tricky. If βN  is positive but fairly close to zero, 
then a one-sided t-test should be used to determine whether the βN  is different 
enough from zero to allow the rejection of the null hypothesis. Recall that in 
order to be able to control the amount of Type I Error we make, such a theory 
implies an alternative hypothesis of HA: β 7 0 (the expected sign) and a null 
hypothesis of H0: β … 0. Let’s look at some complete examples of these kinds 
of one-sided t-tests.
Consider a simple model of the aggregate annual retail sales of new cars 
that specifies that sales of new cars (CARS) are a function of real disposable 
income (YD) and the average retail price of a car adjusted by the consumer 
price index (PRICE). Suppose you spend some time reviewing the literature 
on the automobile industry and are inspired to test a new theory. You decide 
to add a third independent variable, the number of sports utility vehicles sold 
(SUV) to take account of the fact that some potential new car buyers pur-
chase SUVs instead. You therefore hypothesize the following model:
	
+	
-	
-
	
CARS = β0 + β1YD + β2PRICE + β3SUV + e	
(5.5)
As you can see from the hypothesized signs above the coefficients in Equa-
tion 5.5, you expect β1 to be positive and β2 and β3 to be negative. This 
makes sense, since you’d expect higher incomes, lower prices, or lower 
sales of SUVs to increase new car sales, holding the other variables in the 
equation constant.
The four steps to use when working with the t-test are:
1.	 Set up the null and alternative hypotheses.
2.	 Choose a level of significance and therefore a critical t-value.
3.	 Run the regression and obtain an estimated t-value (or t-score).
4.	 Apply the decision rule by comparing the calculated t-value  
with the critical t-value in order to reject or not reject the null  
hypothesis.


130
Chapter 5  Hypothesis Testing and Statistical Inference
Let’s look at each step in more detail.
1.	 Set up the null and alternative hypotheses.6 From Equation 5.5, the one-
sided hypotheses are set up as:
1.  H0: β1 … 0 
HA: β1 7 0
2.  H0: β2 Ú 0 
HA: β2 6 0
3.  H0: β3 Ú 0 
HA: β3 6 0
	
Remember that a t-test typically is not run on the estimate of the con-
stant term β0.
2.	 Choose a level of significance and therefore a critical t-value. Assume that 
you have considered the various costs involved in making Type I and 
Type II Errors and have chosen 5 percent as the level of significance 
with which you want to test. There are 10 observations in the data 
set that is going to be used to test these hypotheses, and so there are 
10 - 3 - 1 = 6 degrees of freedom. At a 5-percent level of significance, 
the critical t-value, tc, can be found in Statistical Table B-1 to be 1.943. 
Note that the level of significance does not have to be the same for all 
the coefficients in the same regression equation. It could well be that 
the costs involved in an incorrectly rejected null hypothesis for one 
coefficient are much higher than for another, so lower levels of signifi-
cance would be used. In this equation, though, for all three variables:
	
tc = 1.943
3.	 Run the regression and obtain an estimated t-value. You now use the data 
(annual from 2000 to 2009) to run the regression on your OLS com-
puter package, getting:
	
CARSt = 1.30 + 4.91YDt + 0.00123PRICEt - 7.14SUVt	 (5.6)
12.382      10.000442          171.382
t = 2.1            2.8                      -0.1
6. The null hypothesis can be stated either as H0: β … 0 or H0: β = 0 because the value used to 
test H0: β … 0 is the value in the null hypothesis closest to the border between the acceptance 
and the rejection regions. When the amount of Type I Error is calculated, this border value of 
β is the one that is used, because over the whole range of β … 0, the value β = 0 gives the 
maximum amount of Type I Error. The classical approach limits this maximum amount to a 
preassigned level—the chosen level of significance.


131
Examples of t-Tests
where:	
CARSt  = new car sales (in hundreds of thousands of units) 
in year t
	
YDt
 = real U.S. disposable income (in hundreds of 
­billions of dollars)
	
PRICEt = the average real price of a new car in year t  
(in dollars)
	
SUVt
 = the number of sports utility vehicles sold in year t  
(in millions)
	
Once again, we use our standard documentation notation, so the 
figures in parentheses are the estimated standard errors of the βN s. The 
t-values to be used in these hypothesis tests are printed out by standard 
OLS programs:
	
tk =
βN k
SE1βN k2  1k = 1, 2, c, K2	
(5.3)
	
For example, the estimated coefficient of SUV divided by its estimated 
standard error is -7.14/71.38 = -0.1. Note that since standard errors 
are always positive, a negative estimated coefficient implies a negative 
t-value.
4.	 Apply the decision rule by comparing the calculated t-value with the critical 
t-value in order to reject or not reject the null hypothesis. As stated in Sec-
tion 5.2, the decision rule for the t-test is to
Reject H0 if tk 7 tc and if tk also has the sign implied by HA.
Do not reject H0 otherwise.
What would these decision rules be for the three hypotheses, given the rel-
evant critical t-value (1.943) and the calculated t-values?
	
For β1: Reject H0 if 2.1 7 1.943 and if 2.1 is positive.
In the case of disposable income, you reject the null hypothesis that β1 … 0 
since 2.1 is indeed greater than 1.943. The result (that is, HA: β1 7 0) is as 
you expected on the basis of theory, since the more income in the country, 
the more new car sales you’d expect.
	
For β2: Reject H0 if 2.8 7 1.943 and if 2.8 is negative.
For prices, the t-statistic is large in absolute value (being greater than 
1.943) but has a sign that is contrary to our expectations, since the alter-
native hypothesis implies a negative sign. Since both conditions in the 
decision rule must be met before we can reject H0, you cannot reject the 
null hypothesis that prices have a zero or positive effect on new car sales! 


132
Chapter 5  Hypothesis Testing and Statistical Inference
Despite your surprise,7 you stick with your contention that prices belong in 
the equation and that their expected impact should be negative.
Notice that the coefficient of PRICE is quite small, 0.00123, but that this 
size has no effect on the t-calculation other than its relationship to the stan-
dard error of the estimated coefficient.
	
For β3: Reject H0 if  -0.1 7 1.943 and if -0.1 is negative.
For sales of sports utility vehicles, the coefficient βN 3 is not statistically 
different from zero, since  -0.1 6 1.943, and you cannot reject the null 
hypothesis that β Ú 0 even though the estimated coefficient has the sign 
implied by the alternative hypothesis. After thinking this model over again, 
you come to the conclusion that you were hasty in adding the variable to the 
equation.
Figure 5.4 illustrates all three of these outcomes by plotting the criti-
cal t-value and the calculated t-values for all three null hypotheses on a 
t-distribution that is centered around zero (the value in the null hypothesis 
closest to the border between the acceptance and rejection regions). Students 
are urged to analyze the results of tests on the estimated coefficients of 
Equation 5.6 assuming different numbers of observations and different 
levels of significance. Exercise 2 has a number of such specific combinations, 
with answers in Appendix A.
The purpose of this example is to provide practice in testing hypotheses, 
and the results of such a poorly thought-out equation for such a small 
number of observations should not be taken too seriously. Given all that, 
however, it’s still instructive to note that you did not react the same way to 
your inability to reject the null hypotheses for the price and sports utility 
vehicle variables. That is, the failure of the sports utility vehicle variable’s 
coefficient to be significantly negative caused you to realize that perhaps 
the addition of this variable was ill-advised. The failure of the price vari-
able’s coefficient to be significantly negative did not cause you to consider 
the possibility that price has no effect on new car sales. Put differently, 
estimation results should never be allowed to cause you to want to adjust 
theoretically sound variables or hypotheses, but if they make you realize you 
7. Actually, it shouldn’t be a surprise to occasionally get a positive estimated coefficient for price 
in a demand equation, particularly in such a small sample. Supply and demand are determined 
simultaneously, but we didn’t specify a supply equation in our model. Thus our “demand” 
equation might be picking up the positive impact of price on quantity from the omitted supply 
equation. We’ll deal with the simultaneity issue in Chapter 14.


133
EXAMPLES OF t-TESTS
have made a serious mistake, then it would be foolhardy to ignore that 
mistake. What to do about the positive coefficient of price, on the other 
hand, is what the “art” of econometrics is all about. Surely a positive coef-
ficient is unsatisfactory, but throwing the price variable out of the equation 
seems even more so. Possible answers to such issues are addressed more than 
once in the chapters that follow.
0
t
1.943 2.1
td1
H0 : d1 … 0
HA : d1 7 0
Rejection
Region
Critical
Value
Critical
Value
“Acceptance”
Region
-0.1
t
-1.943
2.8
H0 : d2 Ú 0
HA : d2 6 0
Rejection
Region
“Acceptance”
Region
H0 : d3 Ú 0
HA : d3 6 0
N
td3
N
td2
N
Figure 5.4  One-Sided t-Tests of the Coefficients of the New Car Sales Model
Given the estimates in Equation 5.6 and the critical t-value of 1.943 for a 5-percent level 
of significance, one-sided, 6 degrees of freedom t-test, we can reject the null hypothesis for 
βN 1, but not for βN 2 or βN 3.


134
Chapter 5  Hypothesis Testing and Statistical Inference
Examples of Two-Sided t-Tests
Although most hypotheses in regression analysis should be tested with 
one-sided t-tests, two-sided t-tests are appropriate in particular situations. 
Researchers sometimes encounter hypotheses that should be rejected if esti-
mated coefficients are significantly different from zero, or a specific nonzero 
value, in either direction. This situation requires a two-sided t-test. The kinds 
of circumstances that call for a two-sided test fall into two categories:
1.	 Two-sided tests of whether an estimated coefficient is significantly  
different from zero, and
2.	 Two-sided tests of whether an estimated coefficient is significantly  
different from a specific nonzero value.
Let’s take a closer look at these categories:
1.	 Testing whether a 훃N  is statistically different from zero. The first 
case for a two-sided test of βN  arises when there are two or more conflict-
ing hypotheses about the expected sign of a coefficient. For example, in 
the Woody’s restaurant equation of Section 3.2, the impact of the aver-
age income of an area on the expected number of Woody’s customers in 
that area is ambiguous. A high-income neighborhood might have more 
total customers going out to dinner, but those customers might decide 
to eat at a more formal restaurant than Woody’s. As a result, you might 
run a two-sided t-test around zero to determine whether the estimated 
coefficient of income is significantly different from zero in either direc-
tion. In other words, since there are reasonable cases to be made for 
either a positive or a negative coefficient, it is appropriate to test the βN  
for income with a two-sided t-test:
	
H0: βI = 0
	
HA: βI ≠0
	
As Figure 5.5 illustrates, a two-sided test implies two different rejection 
regions (one positive and one negative) surrounding the acceptance 
region. A critical t-value, tc, must be increased in order to achieve the 
same level of significance with a two-sided test as can be achieved with 
a one-sided test.8 As a result, there is an advantage to testing hypotheses 
with a one-sided test if the underlying theory allows because, for the same 
t-values, the possibility of Type I Error is half as much for a one-sided 
8. See Figure 5.3. In that figure, the same critical t-value has double the level of significance for 
a two-sided test as for a one-sided test.


135
EXAMPLES OF t-TESTS
test as for a two-sided test. In cases where there are powerful theoretical 
arguments on both sides, however, the researcher has no alternative to 
using a two-sided t-test around zero. To see how this works, let’s follow 
through the Woody’s income variable example in more detail.
a.	 Set up the null and alternative hypotheses.
H0: βI = 0
HA: βI ≠0
b.	 Choose a level of significance and therefore a critical t-value. You decide 
to keep the level of significance at 5 percent, but now this amount 
must be distributed between two rejection regions for 29 degrees 
of freedom. Hence, the correct critical t-value is 2.045 (found in 
Statistical Table B-1 for 29 degrees of freedom and a 5-percent, two-
sided test). Note that, technically, there now are two critical t-values, 
+2.045 and -2.045.
0
t
+2.045
Critical
Value
-2.045
Critical
Value
+2.37
Estimated
t-Value
H0 : dI = 0
HA : dI Z 0
Rejection
Region
Rejection
Region
“Acceptance”
Region
tdIN
Figure 5.5  Two-Sided t-Test of the Coefficient of Income  
in the Woody’s Model
Given the estimates of Equation 5.4 and the critical t-values of {2.045 for a 5-percent 
level of significance, two-sided, 29 degrees of freedom t-test, we can reject the null  
hypothesis that βI = 0.


136
Chapter 5  Hypothesis Testing and Statistical Inference
c.	 Run the regression and obtain an estimated t-value. Since the value 
implied by the null hypothesis is still zero, the estimated t-value of 
+2.37 given in Equation 5.4 is applicable.
d.	 Apply the decision rule by comparing the calculated t-value with the critical 
t-value in order to reject or not reject the null hypothesis. We once again 
use the decision rule stated in Section 5.2, but since the alternative 
hypothesis specifies either sign, the decision rule simplifies to:
For βI: Reject H0 if 2.37 7 2.045
	
In this case, you reject the null hypothesis that βI equals zero because 
2.37 is greater than 2.045 (see Figure 5.5). Note that the positive sign 
implies that, at least for Woody’s restaurants, income increases cus-
tomer volume (holding constant population and competition). Given 
this result, we might well choose to run a one-sided t-test on the next 
year’s Woody’s data set. For more practice with two-sided t-tests, see 
Exercise 5.
2.	 Two-sided t-tests of a specific nonzero coefficient value. The sec-
ond case for a two-sided t-test arises when there is reason to expect a 
specific nonzero value for an estimated coefficient. For example, if a 
previous researcher has stated that the true value of some coefficient al-
most surely equals a particular number, βH0, then that number would 
be the one to test by creating a two-sided t-test around the hypoth-
esized value, βH0.
	
  In such a case, the null and alternative hypotheses become:
H0: βk = βH0
HA: βk ≠βH0
	
where βH0 is the specific nonzero value hypothesized.
	
  Since the hypothesized β value is no longer zero, the formula with 
which to calculate the estimated t-value is Equation 5.2, repeated here:
	
tk =
1βN k - βH02
SE1βN k2   1k = 1, 2, c, K2	
(5.2)
	
This t-statistic is still distributed around zero if the null hypothesis is 
correct, because we have subtracted βH0 from the estimated regression 
coefficient whose expected value is supposed to be βH0 when H0 is 
true. Since the t-statistic is still centered around zero, the decision rule 
developed earlier still is applicable.


137
LIMITATIONS OF THE t-TEST
5.4   Limitations of the t-Test
One problem with the t-test is that it is easy to misuse. t-scores are printed 
out by computer regression packages and the t-test seems easy to work with, 
so beginning researchers sometimes attempt to use the t-test to “prove” things 
that it was never intended to even test. For that reason, it’s probably just as 
important to know the limitations of the t-test9 as it is to know the applica-
tions of that test. Perhaps the most important of these limitations, that the 
usefulness of the t-test diminishes rapidly as more and more specifications are 
estimated and tested, is the subject of Section 6.4. The purpose of the present 
section is to give additional examples of how the t-test should not be used.
The t-Test Does Not Test Theoretical Validity
Recall that the purpose of the t-test is to help the researcher make inferences 
about a particular population coefficient based on an estimate obtained from 
a sample of that population. Some beginning researchers conclude that any 
statistically significant result is also a theoretically correct one. This is dangerous 
because such a conclusion confuses statistical significance with theoretical validity.
Consider for instance, the following estimated regression that explains the 
consumer price index in the United Kingdom:10
	
PN = 10.9 - 3.2C + 0.39C2	
(5.7)
10.232 10.022
t = -13.9   19.5
R  2 = .982     N = 21
Apply the t-test to these estimates. Do you agree that the two slope coeffi-
cients are statistically significant?
The catch is that P is the consumer price index and C is the cumulative 
amount of rainfall in the United Kingdom! We have just shown that rain is 
statistically significant in explaining consumer prices, but does that also show 
that the underlying theory is valid? Of course not. Why is the statistical result 
so significant? The answer is that by chance there is a common trend on both 
sides of the equation. This common trend does not have any meaning. The 
9. These limitations also apply to the use of p-values. For example, many beginning students 
conclude that the variable with the lowest p-value is the most important variable in an equation, 
but this is just as false for p-values as it is for the t-test.
10. These results, and others similar to them, can be found in David F. Hendry, “Econometrics— 
Alchemy or Science?” Economica, Vol. 47, pp. 383–406. This is another example of spurious 
regression, first mentioned in Section 2.5 and covered in more detail in Section 12.4.


138
Chapter 5  Hypothesis Testing and Statistical Inference
moral should be clear: Never conclude that statistical significance, as shown 
by the t-test, is the same as theoretical validity.
Occasionally, estimated coefficients will be significant in the direction 
opposite from that hypothesized, and some beginning researchers may be 
tempted to change their hypotheses. For example, a student might run a regres-
sion in which the hypothesized sign is positive, get a “statistically significant” 
negative sign, and be tempted to change the theoretical expectations to 
“expect” a negative sign after “rethinking” the issue. Although it is admirable 
to be willing to reexamine incorrect theories on the basis of new evidence, that 
evidence should be, for the most part, theoretical in nature. If the evidence 
causes a researcher to go back to the theoretical underpinnings of a model and 
find a mistake, then the null hypothesis should be changed, but then this new 
hypothesis should be tested using a completely different data set. After all, we 
already know what the result will be if the hypothesis is tested on the old one.
The t-Test Does Not Test “Importance”
One possible use of a regression equation is to help determine which inde-
pendent variable has the largest relative effect (importance) on the depen-
dent variable. Some beginning researchers draw the unwarranted conclusion 
that the most statistically significant variable in their estimated regression is 
also the most important in terms of explaining the largest portion of the 
movement of the dependent variable. Statistical significance says little—if 
anything—about which variables determine the major portion of the variation 
in the dependent variable. To determine importance, a measure such as the 
size of the coefficient multiplied by the average size of the independent vari-
able or the standard error of the independent variable would make more sense.
Consider the following hypothetical equation:
	
YN = 300.0 + 10.0X1 + 200.0X2	
(5.8)
11.02      125.02
t = 10.0         8.0
R  2 = .90     N = 30
where:	
Y  = mail-order sales of O’Henry’s Oyster Recipes
	
X1 = hundreds of dollars of advertising expenditures in Gourmets’ 
Magazine
	
X2 = hundreds of dollars of advertising expenditures on the Julia 
Adult TV Cooking Show
Assume that all other factors, including prices, quality, and competition, 
remain constant during the estimation period. Where should O’Henry be 
spending his advertising money? That is, which independent variable has 


139
  Confidence Intervals
the biggest impact per dollar on Y? Given that X2’s coefficient is 20 times X1’s 
coefficient, you’d have to agree that X2 is more important as defined, and yet 
which coefficient is more statistically significantly different from zero? With a 
t-score of 10.0, X1 is more statistically significant than X2 and its t-score of 8.0, 
but all that means is that we have more evidence that the coefficient is posi-
tive, not that the variable itself is necessarily more important in determining Y.
The t-Test Is Not Intended for Tests of the Entire Population
The t-test helps make inferences about the true value of a parameter from an 
estimate calculated from a sample of the population (the group from which 
the sample is being drawn). If a coefficient is calculated from the entire pop-
ulation, then an unbiased estimate already measures the population value 
and a significant t-test adds nothing to this knowledge. One might forget this 
property and attach too much importance to t-scores that have been obtained 
from samples that approximate the population in size.
This point can perhaps best be seen by remembering that the t-score is 
the estimated regression coefficient divided by the standard error of the esti-
mated regression coefficient. If the sample size is large enough to approach 
the population, then the standard error will approach zero and the t-score 
will eventually become:
	
t = βN
0 = ∞
Thus, the mere existence of a large t-score for a huge sample has no real sub-
stantive significance.
5.5   Confidence Intervals
Now that you’ve learned how to do hypothesis tests using the t-statistic and 
the p-value, you’re probably thinking it would be fun to learn a third way. 
OK, maybe not! But there is indeed a third way. It’s based on the concept of 
a confidence interval.
A confidence interval is a range of values that will contain the true value 
of β a certain percentage of the time, say 90 or 95 percent. The formula for a 
confidence interval is
	
Confidence interval = βN { tc # SE1βN 2	
(5.9)
where tc is the two-sided critical value of the t-statistic for whatever sig-
nificance level we choose. If you want a 90-percent confidence interval, 


140
Chapter 5  Hypothesis Testing and Statistical Inference
you’d choose the critical value for the 10-percent significance level. For a 
95-percent confidence interval, you’d use a 5-percent critical value.
To see how confidence intervals can be used for hypothesis tests, let’s 
return to Equation 5.4 and test the significance of the income coefficient:
	
YNi = 102,192 - 9075Ni + 0.3547Pi + 1.288Ii	
(5.4)
120532 
10.07272   10.5432
t = -4.42     4.88        2.37
N = 33      R  2 = .579
We’d typically expect sales at a restaurant to rise as income rises (a normal 
good), but Woody’s is a fairly low-priced restaurant chain, so there’s a chance 
that sales will tail off if income gets too high (an inferior good). As a result, 
many econometricians would choose βI = 0 as their null hypothesis and 
therefore run a two-sided test of βI. In a situation where a two-sided test is 
appropriate, a confidence interval makes a lot of sense.
What would a 90-percent confidence interval for βI look like? Well, 
βN I = 1.288 and SE1βN I2 = 0.543, so all we need is a 10-percent two-sided 
critical t-value for 29 degrees of freedom. Using Statistical Table B-1, we see 
tc = 1.699. Substituting these values into Equation 5.9, we get:
 90@percent confidence interval around βN I = 1.288 { 1.699 # 0.543
 = 1.288 { 0.923
and therefore 0.365 … βI … 2.211
What exactly does this mean? If the Classical Assumptions hold true, the confi-
dence interval formula produces ranges that contain the true value of β 90 per-
cent of the time. In this case, there’s a 90 percent chance the true value of βI is 
between 0.365 and 2.211. If it’s not in that range, it’s due to an unlucky sample.
How can we use a confidence interval for a two-tailed hypothesis test? If the 
null hypothesis is βI = 0, we can reject it at the 10-percent level because 0 is 
not in the confidence interval. If the null hypothesis is that βI = 1.0, we cannot 
reject it because 1.0 is in the interval. In general, if your null hypothesis border 
value is in the confidence interval, you cannot reject the null hypothesis.
Thus, confidence intervals can be used for two-sided tests, but they are 
more complicated. So why bother with them? It turns out that confidence 
intervals are very useful in telling us how precise a coefficient estimate is. 
And for many people using econometrics in the real world, this may be 
more important than hypothesis testing. An example will make it easier to 
understand.
Meet Grace, a building contractor who specializes in starter homes for 
young families. It’s a really competitive business, so to make a profit she 
needs to build appealing but inexpensive houses. As a result, Grace wants to 


141
  Confidence Intervals
know which features she can add to her houses that will increase the selling 
price more than they increase her costs. Since she took econometrics in col-
lege, she decides to estimate a model of starter home prices in her city using 
13 independent variables (such as square footage, number of bathrooms, etc.). 
She hopes to use the results to decide which features might turn a profit for 
her on the houses that she’s planning on building.
Let’s focus on how much an additional bathroom might increase the sales 
price. Grace knows that her marginal cost of adding a bathroom is about 
$8,000. She collects 100 observations on recently sold starter homes in her 
city and estimates her model.
The results appear in the first row of Table 5.1. The estimate of the coef-
ficient of bathrooms is about $21,770, well above the $8,000 marginal cost. 
Sounds like a no-brainer to add a bathroom, right? Not so fast. Look at the 
90-percent confidence interval in the first row of Table 5.1. It is huge, ranging 
from about $187 to $43,356. If the true value is in that interval, there’s a 
pretty big chance it could be below $8,000, meaning Grace would lose money 
by adding a bathroom. Or, she could come out way ahead. What should she do?
Remember one of the lessons of Section 4.2 on sampling distributions: 
Bigger samples decrease the variance of βN . In plain English, as the sample size 
grows, βN  tends to get closer and closer to the true value of β. As a result, the 
confidence interval for β shrinks. Let’s see what happens if Grace increases 
her sample to 1,000 observations.
The results for βN bath when N = 1,000 appear in Table 5.1, right below those 
for N = 100. Notice that βN bath has fallen from almost $22,000 to less than 
$13,000. Does this mean Grace should not add a bathroom? Not at all! Look 
at the 90-percent confidence interval. The lower end has risen to $8,346.29, a 
bit more than the $8,000 marginal cost. While Grace could still lose money on 
the deal, it looks like a much safer bet than the small sample results suggest.
Why does a confidence interval become so much narrower with a bigger 
sample? Well, take a look at Equation 5.9. As you can see, the width of a 
Table 5.1  Selected Results from Two Regressions on Selling Prices  
of Starter Homes as a Function of House Characteristics
obs
variable
Coef.
Std. Err.
t
p-value
[90% Conf. Interval]
  100
bath
21771.65
12981.1
1.68
0.097
187.1275 to 43356.18
1000
bath
12935.06
  2787.154
4.64
0.000
8346.288 to 17523.83
These results were generated with data from Nashville, TN house sales in 2012. Because the 
model included 13 independent variables, the first regression has 86 degrees of freedom, and 
the second has 986 degrees of freedom.


142
Chapter 5  Hypothesis Testing and Statistical Inference
confidence interval depends entirely on the product of tc and SE1βN 2. What 
happens to tc and SE1βN 2 as the sample size rises? If you take a look at 
Table B-1, you’ll see that as the sample size rises, tc falls. Simultaneously, as 
the sample size rises, the variance of the sampling distribution falls, so the 
SE1βN 2 (the square root of the estimated variance) must fall as well. If both tc 
and SE1βN 2 fall, then their multiple must fall, and a bigger sample will indeed 
lead to a narrower confidence interval.
This example illustrates how confidence intervals provide information on 
how precise an estimated coefficient is. In addition, confidence intervals also 
are extremely useful in forecasting, and we’ll cover that topic in Chapter 15.
5.6   The F-Test
Although the t-test is invaluable for hypotheses about individual regression 
coefficients, it can’t be used to test multiple hypotheses simultaneously. Such a 
limitation is unfortunate because many interesting ideas involve a number of 
hypotheses or involve one hypothesis about multiple coefficients. For exam-
ple, suppose that you want to test the null hypothesis that there is no seasonal 
variation in a quarterly regression equation that has dummy variables for the 
seasons. To test such a hypothesis, most researchers would use the F-test.
What Is the F-Test?
The F-test is a formal hypothesis test that is designed to deal with a null 
hypothesis that contains multiple hypotheses or a single hypothesis about 
a group of coefficients.11 Such “joint” or “compound” null hypotheses are 
appropriate whenever the underlying economic theory specifies values for 
multiple coefficients simultaneously.
The way in which the F-test works is fairly ingenious. The first step is to 
translate the particular null hypothesis in question into constraints that 
will be placed on the equation. The resulting constrained equation can be 
thought of as what the equation would look like if the null hypothesis were 
correct; you substitute the hypothesized values into the regression equation 
in order to see what would happen if the equation were constrained to agree 
with the null hypothesis. As a result, in the F-test the null hypothesis always 
leads to a constrained equation, even if this violates our standard practice 
that the alternative hypothesis contains what we expect is true.
11. As you will see, the F-test works by placing constraints or restrictions on the equation to 
be tested. Because of this, it’s equivalent to say that the F-test is for tests that involve multiple 
linear restrictions.


143
THE F-TEST
The second step in an F-test is to estimate this constrained equation 
with OLS and compare the fit of this constrained equation with the fit of 
the unconstrained equation. If the fits of the constrained equation and the 
unconstrained equation are not substantially different, the null hypothesis 
should not be rejected. If the fit of the unconstrained equation is substan-
tially better than that of the constrained equation, then we reject the null 
hypothesis. The fit of the constrained equation is never superior to the fit of 
the unconstrained equation, as we’ll explain next.
The fits of the equations are compared with the general F-statistic:
	
F = 1RSSM - RSS2/M
RSS/1N - K - 12	
(5.10)
where:	
RSS
 = residual sum of squares from the unconstrained 
equation
	
RSSM
 = residual sum of squares from the constrained 
equation
	
M
 = number of constraints placed on the equation 
(usually equal to the number of βs eliminated 
from the unconstrained equation)
	
1N - K - 12 = degrees of freedom in the unconstrained equation
RSSM is always greater than or equal to RSS. Imposing constraints on the 
coefficients instead of allowing OLS to select their values can never decrease 
the summed squared residuals. (Recall that OLS selects that combination of 
values of the coefficients that minimizes RSS.) At the extreme, if the uncon-
strained regression yields exactly the same estimated coefficients as does the 
constrained regression, then the RSS are equal and the F-statistic is zero. In 
this case, H0 is not rejected because the data indicate that the constraints 
appear to be correct. As the difference between the constrained coefficients 
and the unconstrained coefficients increases, the data indicate that the null 
hypothesis is less likely to be true. Thus, when F gets larger than the critical 
F-value, the hypothesized restrictions specified in the null hypothesis are 
rejected by the test.
The decision rule to use in the F-test is to reject the null hypothesis if the 
calculated F-value (F) from Equation 5.10 is greater than the appropriate 
critical F-value 1Fc2:
Reject
H0 if F 7 Fc
Do not reject
H0 if F … Fc


144
Chapter 5  Hypothesis Testing and Statistical Inference
The critical F-value, Fc, is determined from Statistical Table B-2 or B-3, 
depending on the level of significance chosen by the researcher and on the 
degrees of freedom. The F-statistic has two types of degrees of freedom: the 
degrees of freedom for the numerator of Equation 5.10 (M, the number of 
constraints implied by the null hypothesis) and the degrees of freedom for 
the denominator of Equation 5.10 (N - K - 1, the degrees of freedom in the 
unconstrained regression equation). The underlying principle here is that if 
the calculated F-value (or F-ratio) is greater than the critical value, then the 
estimated equation’s fit is substantially better than the constrained equation’s 
fit, and we can reject the null hypothesis of no effect.
The F-Test of Overall Significance
Although R2 and R  2 measure the overall degree of fit of an equation, they 
don’t provide a formal hypothesis test of that overall fit. Such a test is pro-
vided by the F-test. The null hypothesis in an F-test of overall significance 
is that all the slope coefficients in the equation equal zero simultaneously. 
For an equation with K independent variables, this means that the null and 
alternative hypotheses would be12:
	
H0: β1 = β2 = g = βK = 0
	
HA: H0 is not true
To show that the overall fit of the estimated equation is statistically signifi-
cant, we must be able to reject this null hypothesis using the F-test.
For the F-test of overall significance, Equation 5.10 simplifies to:
	
F =
ESS/K
RSS/1N - K - 12 =
g 1YNi - Y22/K
ge2
i /1N - K - 12	
(5.11)
This is the ratio of the explained sum of squares (ESS) to the residual sum 
of squares (RSS), adjusted for the number of independent variables (K) and 
the number of observations in the sample (N). In this case, the “constrained 
equation” to which we’re comparing the overall fit is:
	
Yi = β0 + ei	
(5.12)
which is nothing more than saying YNi = Y. Thus the F-test of overall sig-
nificance is really testing the null hypothesis that the fit of the equation is no 
better than that provided by using the mean alone.
12. Note that we don’t hypothesize that β0 = 0. This would imply that E1Y2 = 0. Note also 
that for the test of overall significance, M = K.


145
THE F-TEST
To see how this works, let’s test the overall significance of the Woody’s res-
taurant model of Equation 3.4. Since there are three independent variables, 
the null and alternative hypotheses are:
	
H0: βN = βP = βI = 0
	
HA: H0 is not true
To decide whether to reject or not reject this null hypothesis, we need to cal-
culate Equation 5.11 for the Woody’s example. There are three constraints in 
the null hypothesis, so K = 3. If we check the Stata output for the Woody’s 
equation on pages 76 and 77, we can see that N = 33, RSS = 6,133,300,000, 
and ESS = 9,928,900,000.13 Thus the appropriate F-ratio is:
	
F =
ESS/K
RSS/1N - K - 12 = 9,928,900,000/3
6,133,300,000/29 = 15.65	
(5.13)
In practice, this calculation is never necessary, since virtually every computer 
regression package routinely provides the computed F-ratio for a test of over-
all significance as a matter of course. On the Woody’s computer output, the 
value of the F-statistic can be found near the top of the right-hand column.
Our decision rule tells us to reject the null hypothesis if the calculated 
F-value is greater than the critical F-value. To determine that critical F-value, 
we need to know the level of significance and the degrees of freedom. If we 
assume a 5-percent level of significance, the appropriate table to use is 
Statistical Table B-2. The numerator degrees of freedom equal 3 (K), and the 
denominator degrees of freedom equal 29 1N - K - 12, so we need to look 
in Statistical Table B-2 for the critical F-value for 3 and 29 degrees of freedom. 
As the reader can verify,14 Fc = 2.93 is well below the calculated F-value of 
15.65, so we can reject the null hypothesis and conclude that the Woody’s 
equation does indeed have a significant overall fit.
Just as p-values provide an alternative approach to the t-test, so too can 
p-values provide an alternative approach to the F-test of overall significance. 
13. Stata calls the RSS the “Residual SS“ and calls the ESS the “Model SS.” The e + 09 indicates 
that you should move the decimal point nine places to the right.
14. Note that this critical F-value must be interpolated. The critical value for 30 denominator 
degrees of freedom is 2.92, and the critical value for 25 denominator degrees of freedom is 
2.99. Since both numbers are well below the calculated F-value of 15.65, however, the in-
terpolation isn’t necessary to reject the null hypothesis. As a result, many researchers don’t 
bother with such interpolations unless the calculated F-value is inside the range of the inter-
polation.


146
Chapter 5  Hypothesis Testing and Statistical Inference
Most standard regression estimation programs report not only the F-value for 
the test of overall significance but also the p-value associated with that test. 
To see this for the Woody’s output, look for “Prob 7 F” in the right-hand 
column on the top of page 77. If the p-value is less than your chosen level of 
significance, you can reject the null hypothesis.
Other Uses of the F-Test
There are many other uses of the F-test besides the test of overall significance. 
For example, let’s take a look at the problem of testing the significance of 
seasonal dummies. Seasonal dummies are dummy variables that are used 
to account for seasonal variation in the data in time-series models. In a quar-
terly model, if:
X1t = e 1 in quarter 1
0 otherwise
X2t = e 1 in quarter 2
0 otherwise
X3t = e 1 in quarter 3
0 otherwise
then:
	
Yt = β0 + β1X1t + β2X2t + β3X3t + β4X4t + et	
(5.14)
where X4 is a nondummy independent variable and t is quarterly. Notice that 
only three dummy variables are required to represent four seasons. In this 
formulation β1 shows the extent to which the expected value of Y in the first 
quarter differs from its expected value in the fourth quarter, the omitted con-
dition. β2 and β3 can be interpreted similarly.
Inclusion of a set of seasonal dummies “deseasonalizes” Y. This procedure 
may be used as long as Y and X4 are not “seasonally adjusted” prior to esti-
mation. Many researchers avoid the type of seasonal adjustment done prior 
to estimation because they think it distorts the data in unknown and arbi-
trary ways, but seasonal dummies have their own limitations such as remain-
ing constant for the entire time period. As a result, there is no unambiguously 
best approach to deseasonalizing data.
To test the hypothesis of significant seasonality in the data, one must test 
the hypothesis that all the dummies equal zero simultaneously rather than 
test the dummies one at a time. In other words, the appropriate test of sea-
sonality in a regression model using seasonal dummies involves the use of 
the F-test instead of the t-test.


147
  Summary
In this case, the null hypothesis is that there is no seasonality:
	
H0: β1 = β2 = β3 = 0
	
HA: H0 is not true
The constrained equation would then be Y = β0 + β4X4 + e. To determine 
whether the whole set of seasonal dummies should be included, the fit of 
the estimated constrained equation would be compared to the fit of the 
estimated unconstrained equation by using the F-test in Equation 5.10. Note 
that this example uses the F-test to test null hypotheses that include only a 
subset of the slope coefficients. Also note that in this case M = 3, because 
three coefficients (β1, β2, and β3) have been eliminated from the equation.
The exclusion of some seasonal dummies because their estimated coefficients 
have low t-scores is not recommended. Seasonal dummy coefficients should 
be tested with the F-test instead of with the t-test because seasonality is usually 
a single compound hypothesis rather than 3 individual hypotheses (or 11 with 
monthly data) having to do with each quarter (or month). To the extent that 
a hypothesis is a joint one, it should be tested with the F-test. If the hypothesis 
of seasonal variation can be summarized into a single dummy variable, then 
the use of the t-test will cause no problems. Often, where seasonal dummies 
are unambiguously called for, no hypothesis testing at all is undertaken.
5.7   Summary
	 1.	 Hypothesis testing makes inferences about the validity of specific eco-
nomic (or other) theories from a sample of the population for which 
the theories are supposed to be true. The four basic steps of hypoth-
esis testing (using a t-test as an example) are:
a.	Set up the null and alternative hypotheses.
b.	Choose a level of significance and, therefore, a critical t-value.
c.	 Run the regression and obtain an estimated t-value.
d.	Apply the decision rule by comparing the calculated t-value with the 
critical t-value in order to reject or not reject the null hypothesis.
	 2.	 The null hypothesis states the range of values that the regression coef-
ficient is expected to take on if the researcher’s theory is not correct. The 
alternative hypothesis is a statement of the range of values that the re-
gression coefficient is expected to take if the researcher’s theory is correct.
	 3.	 The two kinds of errors we can make in such hypothesis testing are:
	
	 	
Type I: We reject a null hypothesis that is true.
	
	
Type II: We do not reject a null hypothesis that is false.


148
Chapter 5  Hypothesis Testing and Statistical Inference
	 4.	 The t-test tests hypotheses about individual coefficients from regres-
sion equations. The form for the t-statistic is
tk =
1βN k - βH02
SE1βN k2   1k = 1, 2, c, K2
	
	 In many regression applications, βH0 is zero. Once you have calculated 
a t-value and chosen a critical t-value, you reject the null hypothesis 
if the t-value is greater in absolute value than the critical t-value and if 
the t-value has the sign implied by the alternative hypothesis.
	 5.	 The t-test is easy to use for a number of reasons, but care should be 
taken when using the t-test to avoid confusing statistical significance 
with theoretical validity or empirical evidence.
	 6.	 The F-test is a formal hypothesis test designed to deal with a null 
hypothesis that contains multiple hypotheses or a single hypothesis 
about a group of coefficients. The most common use of the F-test is to 
test the overall significance of an estimated equation.
Exercises
(The answers to the even-numbered exercises are in Appendix A.)
	 1.	 Write the meaning of each of the following terms without referring 
to the book (or your notes), and compare your definition with the 
version in the text for each.
a.	 alternative hypothesis (p. 117)
b.	 confidence interval (p. 139)
c.	 critical value (p. 119)
d.	 decision rule (p. 119)
e.	 F-Test (p. 142)
f.	 level of significance (p. 126) 
g.	 null hypothesis (p. 117)
h.	 one-sided test (p. 117)
i.	 p-value (p. 127)
j.	 seasonal dummies (p. 146)
k.	 t-statistic (p. 121)
l.	 two-sided test (p. 117)
m.	Type I Error (p. 118)
n.	 Type II Error (p. 118)


149
Exercises
	 2.	 Return to Section 5.3 and test the hypotheses implied by Equation 5.5 
with the results in Equation 5.6 for all three coefficients under the 
following circumstances:
a.	10 percent significance and 15 observations
b.	10 percent significance and 28 observations
c.	 1 percent significance and 10 observations
	 3.	 Create null and alternative hypotheses for the following coefficients:
a.	the impact of height on weight (Section 1.4)
b.	all the coefficients in Equation A in Exercise 5, Chapter 2
c.	 all the coefficients in Y = β0 + β1X1 + β2X2 + β3X3 + e, where Y is 
total gasoline used on a particular trip, X1 is miles traveled, X2 is 
the weight of the car, and X3 is the average speed traveled
d.	the impact of the decibel level of the grunt of a shot-putter on the 
length of the throw involved (shot-putters are known to make loud 
noises when they throw, but there is little theory about the impact of 
this yelling on the length of the put). Assume all relevant “nongrunt” 
variables are included in the equation.
	 4.	 Return to Section 5.2 and test the appropriate hypotheses with the 
results in Equation 5.4 for all three coefficients under the following 
circumstances:
a.	5 percent significance and 6 degrees of freedom
b.	10 percent significance and 29 degrees of freedom
c.	 1 percent significance and 2 degrees of freedom
	 5.	 Using the techniques of Section 5.3, test the following two-sided 
hypotheses:
a.	For Equation 5.8, test the hypothesis that:
H0: β2 = 160.0
HA: β2 ≠160.0
	
at the 5-percent level of significance.
b.	For Equation 5.4, test the hypothesis that:
H0: β3 = 0
HA: β3 ≠0
	
at the 1-percent level of significance.
c.	 For Equation 5.6, test the hypothesis that:
H0: β2 = 0
HA: β2 ≠0
	
at the 5-percent level of significance.


150
Chapter 5  Hypothesis Testing and Statistical Inference
	 6.	 Suppose that you estimate a model of house prices to determine the 
impact of having beach frontage on the value of a house.15 You do 
some research, and you decide to use the size of the lot instead of the 
size of the house for a number of theoretical and data availability 
reasons. Your results (standard errors in parentheses) are:
PRICEi = 40 + 35.0  LOTi - 2.0  AGEi + 10.0  BEDi - 4.0  FIREi + 100  BEACHi
15.02      11.02     110.02    
14.02       1102
N = 30             R  2 = .63
where:	
PRICEi  = the price of the ith house (in thousands of 
dollars)
	
LOTi
 = the size of the lot of the ith house (in thousands 
of square feet)
	
AGEi
 = the age of the ith house in years
	
BEDi
 = the number of bedrooms in the ith house
	
FIREi
 = a dummy variable for a fireplace (1 = yes for 
the ith house)
	
BEACHi = a dummy for having beach frontage (1 = yes 
for the ith house)
a.	You expect the variables LOT, BED, and BEACH to have positive 
coefficients. Create and test the appropriate hypotheses to evaluate 
these expectations at the 5-percent level.
b.	You expect AGE to have a negative coefficient. Create and test 
the appropriate hypotheses to evaluate these expectations at the 
10-percent level.
c.	 At first you expect FIRE to have a positive coefficient, but one of 
your friends says that fireplaces are messy and are a pain to keep 
clean, so you’re not sure. Run a two-sided t-test around zero to test 
these expectations at the 5-percent level.
d.	What problems appear to exist in your equation? (Hint: Do you 
have any unexpected signs? Do you have any coefficients that are 
not significantly different from zero?)
e.	 Which of the problems that you outlined in part d is the most wor-
risome? Explain your answer.
f.	 What explanation or solution can you think of for this problem?
h
15. This hypothetical result draws on Rachelle Rush and Thomas H. Bruggink, “The Value of 
Ocean Proximity on Barrier Island Houses,” The Appraisal Journal, April 2000, pp. 142–150.


151
Exercises
	 7.	 Suppose that you’ve been asked by the San Diego Padres baseball 
team to evaluate the economic impact of their new stadium by ana-
lyzing the team’s attendance per game in the last year at their old 
stadium. After some research on the topic, you build the following 
model (standard errors in parentheses):
ATTi = 25000 + 15000 WINi + 4000  FREEi - 3000  DAYi - 12000  WEEKi
1150002     120002      130002       130002
N = 35         R  2 = .41
where:	
ATTi
 = the attendance at the ith game
	
WINi  = the winning percentage of the opponent in the 
ith game
	
FREEi  = a dummy variable equal to 1 if the ith game was 
a “promotion” game at which something was 
given free to each fan, 0 otherwise
	
DAYi
 = a dummy variable equal to 1 if the ith game was 
a day game and equal to 0 if the game was a 
night or twilight game
	
WEEKi = a dummy variable equal to 1 if the ith game was 
during the week and equal to 0 if it was on the 
weekend
a.	You expect the variables WIN and FREE to have positive coeffi-
cients. Create and test the appropriate hypotheses to evaluate these 
expectations at the 5-percent level.
b.	You expect WEEK to have a negative coefficient. Create and test 
the appropriate hypotheses to evaluate these expectations at the 
1-percent level.
c.	 You’ve included the day game variable because your boss thinks it’s 
important, but you’re not sure about the impact of day games on 
attendance. Run a two-sided t-test around zero to test these expec-
tations at the 5-percent level.
d.	What problems appear to exist in your equation? (Hint: Do you 
have any unexpected signs? Do you have any coefficients that are 
not significantly different from zero?)
e.	 Which of the problems that you outlined in part d is the most 
worrisome? Explain your answer.
f.	 What explanation or solution can you think of for this problem? 
(Hint: You don’t need to be a sports fan to answer this question. If 
you like music, think about attendance at outdoor concerts.)
h


152
Chapter 5  Hypothesis Testing and Statistical Inference
	 8.	 Let’s return to the model of iPod prices on eBay that was developed in 
Exercise 7 in Chapter 3. That equation was:
PRICEi = 109.24 + 54.99NEWi - 20.44SCRATCHi + 0.73BIDRSi
15.342        15.112           10.592
t = 10.28      
-4.00                1.23
N = 215      F = 55.09
where:	
PRICEi
 = the price at which the ith iPod sold on eBay
	
	 	
NEWi
 = a dummy variable equal to 1 if the ith iPod was 
new, 0 otherwise
	
	 	
SCRATCHi = a dummy variable equal to 1 if the ith iPod had a 
minor cosmetic defect, 0 otherwise
	
	 	
BIDRSi
 = the number of bidders on the ith iPod
a.	Create and test hypotheses for the coefficients of NEW and 
SCRATCH at the 5-percent level. (Hint: Use the critical value for 
120 degrees of freedom.)
b.	In theory, the more bidders there are on a given iPod, the higher 
the price should be. Create and test hypotheses at the 1-percent 
level to see if this theory can be supported by the results.
c.	 Based on the hypothesis tests you conducted in parts a and b, are 
there any variables that you think should be dropped from the 
equation? Explain.
d.	If you could add one variable to this equation, what would it be? 
Explain. (Hint: All the iPods in the sample are silver-colored, 4 GB 
Apple iPod minis.)
e.	 Test the overall significance of this equation with the F-test at the 
5-percent level. Be sure to state the correct null and alternative hy-
potheses and to be specific with respect to your critical value.
	 9.	 Frederick Schut and Peter VanBergeijk16 published an article in which 
they attempted to see if the pharmaceutical industry practiced inter-
national price discrimination by estimating a model of the prices of 
pharmaceuticals in a cross section of 32 countries. The authors felt 
that if price discrimination existed, then the coefficient of per capita 
income in a properly specified price equation would be strongly 
positive. The reason they felt that the coefficient of per capita income 
h
16. Frederick T. Schut and Peter A. G. VanBergeijk, “International Price Discrimination: The 
Pharmaceutical Industry,” World Development, Vol. 14, No. 9, pp. 1141–1150. The estimated 
coefficients we list are those produced by EViews using the original data and differ slightly from 
those in the original article.


153
Exercises
would measure price discrimination went as follows: the higher the 
ability to pay, the lower (in absolute value) the price elasticity of 
demand for pharmaceuticals and the higher the price a price dis-
criminator could charge. In addition, the authors expected that prices 
would be higher if pharmaceutical patents were allowed and that 
prices would be lower if price controls existed, if competition was 
encouraged, or if the pharmaceutical market in a country was rela-
tively large. Their estimates were (standard errors in parentheses):
	
PNi = 38.22 + 1.43GDPNi - 0.6CVNi + 7.31PPi	
(5.15)
10.212       10.222     16.122
t =      6.69        -2.66        1.19
- 15.63DPCi -  11.38PCi
16.932         17.162
t = - 2.25       - 1.59
N = 32    R  2 = .775
where:	
Pi
 = the pharmaceutical price level in the ith country 
divided by that of the United States
	
GDPNi = per capita domestic product in the ith country 
divided by that of the United States
	
CVNi
 = per capita volume of consumption of pharma-
ceuticals in the ith country divided by that of 
the United States
	
PPi
 = a dummy variable equal to 1 if patents for 
pharmaceutical products are recognized in the 
ith country, 0 otherwise
	
DPCi
 = a dummy variable equal to 1 if the ith country 
applied strict price controls, 0 otherwise
	
PCi
 = a dummy variable equal to 1 if the ith country 
encouraged price competition, 0 otherwise
a.	Develop and test appropriate hypotheses concerning the regression 
coefficients using the t-test at the 5-percent level.
b.	Set up 90-percent confidence intervals for each of the estimated 
slope coefficients.
c.	 Do you think Schut and VanBergeijk concluded that international 
price discrimination exists? Why or why not?
d.	How would the estimated results have differed if the authors had 
not divided each country’s prices, per capita income, and per capita 
pharmaceutical consumption by that of the United States? Explain 
your answer.


154
Chapter 5  Hypothesis Testing and Statistical Inference
e.	 Reproduce their regression results by using the Stata computer pro-
gram (datafile DRUGS5) or your own computer program and the 
data from Table 5.2.
Table 5.2  Data for the Pharmaceutical Price Discrimination Exercise
Country
P
GDPN
CV
N
CVN
PP
PC
DPC
Malawi
60.83
    4.9
    0.014
    2.36
    0.6
1
0
0
Kenya
50.63
    6.56
    0.07
    6.27
    1.1
1
0
0
India
31.71
    6.56
  18.66
282.76
    6.6
0
0
1
Pakistan
38.76
    8.23
    3.42
  32.9
  10.4
0
1
1
Sri Lanka
15.22
    9.3
    0.42
    6.32
    6.7
1
1
1
Zambia
96.58
  10.3
    0.05
    2.33
    2.2
1
0
0
Thailand
48.01
  13.0
    2.21
  19.60
  11.3
0
0
0
Philippines
51.14
  13.2
    0.77
  19.70
    3.9
1
0
0
South Korea
35.10
  20.7
    2.20
  16.52
  13.3
0
0
0
Malaysia
70.74
  21.5
    0.50
    5.58
    8.9
1
0
0
Colombia
48.07
  22.4
    1.56
  11.09
  14.1
0
1
0
Jamaica
46.13
  24.0
    0.21
    0.96
  22.0
1
0
0
Brazil
63.83
  25.2
  10.48
  50.17
  21.6
0
1
0
Mexico
69.68
  34.7
    7.77
  28.16
  27.6
0
0
0
Yugoslavia
48.24
  36.1
    3.83
    9.42
  40.6
0
1
1
Iran
70.42
  37.7
    3.27
  15.33
  21.3
0
0
0
Uruguay
65.95
  39.6
    0.44
    1.30
  33.8
0
0
0
Ireland
73.58
  42.5
    0.57
    1.49
  38.0
1
0
0
Hungary
57.25
  49.6
    2.36
    4.94
  47.8
0
1
1
Poland
53.98
  50.1
    8.08
  15.93
  50.7
0
1
1
Italy
69.01
  53.8
  12.02
  26.14
  45.9
0
0
1
Spain
69.68
  55.9
    9.01
  16.63
  54.2
0
0
0
United Kingdom
71.19
  63.9
    9.96
  26.21
  38.0
1
1
1
Japan
81.88
  68.4
  28.58
  52.24
  54.7
0
0
1
Austria
139.53
  69.6
    1.24
    3.52
  35.2
0
0
0
Netherlands
137.29
  75.2
    1.54
    6.40
  24.1
1
0
0
Belgium
101.73
  77.7
    3.49
    4.59
  76.0
1
0
1
France
91.56
  81.9
  25.14
  24.70
101.8
1
0
1
Luxembourg
100.27
  82.0
    0.10
    0.17
  60.5
1
0
1
Denmark
157.56
  82.4
    0.70
    2.35
  29.5
1
0
0
Germany, West
152.52
  83.0
  24.29
  28.95
  83.9
1
0
0
United States
100.00
100.0
100.00
100.00
100.0
1
1
0
Source: Frederick T. Schut and Peter A. G. VanBergeijk, “International Price Discrimination:  
The Pharmaceutical Industry,” World Development, Vol. 14, No. 9, p. 1144.
Datafile = DRUGS5


155
  Appendix: Econometric Lab #3
5.8   Appendix: Econometric Lab #3
This lab focuses on hypothesis testing. You will estimate models of life expec-
tancy at birth across the 50 states and the District of Columbia using eco-
nomic and demographic variables. The data are in the dataset LIFE5 on the 
textbook’s website and include the following variables:
Table 5.3  Variable Listing
Variable
Description
lifeexpecti
Life expectancy at birth, in years, in state i, 2010
medinci
The median household income in state i  
(thousands of dollars), 2010
uninsuredi
The percentage of the population (aged 0–64)  
in state i that was without health insurance  
coverage, 2008–2010
smokei
The percentage of adults in state i who smoked, 
2006–2012
obesityi
The percentage of adults in state i who were 
obese (Body Mass Index greater than or  
equal to 30), 2006–2012
teenbirthi
The number of births to teenaged mothers in 
state i per 1,000 females aged 15 to 19 years, 2010
gunlawi
A dummy variable = 1 if state i had a firearm law 
protecting children, 0 otherwise, 2010
metroi
The percentage of the population in state i that 
lived in a metropolitan statistical area, 2010
Step 1: Specify the Model
Specify (i.e., write out) a linear regression equation for lifeexpect with all 
seven independent variables included, using the format of Equation 5.1 in 
the text. Use proper subscripts and Greek letters where appropriate.
Step 2: Hypothesize the Signs of the Coefficients
For all seven independent variables, hypothesize the sign of each regression 
coefficient.


156
Chapter 5  Hypothesis Testing and Statistical Inference
Step 3: Summary Statistics
Check the means, maximums, and minimums for each of the variables. Do 
you spot any obvious anomalies? If so, what are they? If you see no anoma-
lies, go on to Step 4.
Step 4: Estimation
Run the regression using all seven independent variables and print out your 
regression results.
Step 5: Hypothesis Testing (t-statistics)
Test the slope coefficients of smoke, teenbirth, medinc, and uninsured at 
the 5-percent level of significance using the t-table in the textbook. Show your 
null and alternative hypotheses and list the critical t-statistic used for each 
hypothesis test. For which coefficients can you reject the null hypothesis?
Step 6: Hypothesis Testing (p-values)
Test the slope coefficients of gunlaw, metro, and obesity at the 5-percent 
level of significance using p-values. List the p-value used for each test. For 
which coefficients can you reject the null hypothesis?
Step 7: Overall F-test
Use the overall F-statistic to test whether the regression is significant at the 
5-percent level. Show your null and alternative hypotheses and your decision 
rule, and use the F-table.
Step 8: Drawing Conclusions
The absolute value of the coefficient of gunlaw is much larger than the abso-
lute value of the coefficient of smoke. Does this mean that passing a gun law 
to protect children will have a bigger impact on life expectancy than reducing 
smoking by three percentage points? Explain.
