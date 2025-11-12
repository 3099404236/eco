# Chapter 8: Multicollinearity

**Pages:** 241-292

---

221
Chapter 8
Multicollinearity
8.1  Perfect versus Imperfect Multicollinearity
8.2  The Consequences of Multicollinearity
8.3  The Detection of Multicollinearity
8.4  Remedies for Multicollinearity
8.5  An Example of Why Multicollinearity Often Is Best Left Unadjusted
8.6  Summary and Exercises
8.7  Appendix: The SAT Interactive Regression Learning Exercise
The next three chapters deal with violations of the Classical Assumptions 
and remedies for those violations. This chapter addresses multicollinearity, 
and the next two chapters address serial correlation and heteroskedasticity. 
For each of these three problems, we will attempt to answer the following 
questions:
1.	 What is the nature of the problem?
2.	 What are the consequences of the problem?
3.	 How is the problem diagnosed?
4.	 What remedies for the problem are available?
Strictly speaking, perfect multicollinearity is the violation of Classical 
Assumption VI—that no independent variable is a perfect linear function of 
one or more other independent variables. Perfect multicollinearity is rare, but 
severe imperfect multicollinearity, although not violating Classical Assump-
tion VI, still causes substantial problems.
Recall that the coefficient βk can be thought of as the impact on the depen-
dent variable of a one-unit increase in the independent variable Xk, holding 
constant the other independent variables in the equation. If two explanatory 
variables are significantly related, then the OLS computer program will find 


222
Chapter 8  Multicollinearity
it difficult to distinguish the effects of one variable from the effects of the 
other.
In essence, the more highly correlated two (or more) independent vari-
ables are, the more difficult it becomes to accurately estimate the coefficients 
of the true model. If two variables move identically, then there is no hope of 
distinguishing between their impacts, but if the variables are only roughly 
correlated, then we still might be able to estimate the two effects accurately 
enough for most purposes.
8.1   Perfect versus Imperfect Multicollinearity
Perfect Multicollinearity
Perfect multicollinearity1 violates Classical Assumption VI, which specifies 
that no explanatory variable is a perfect linear function of any other explana-
tory variable. The word perfect in this context implies that the variation in one 
explanatory variable can be completely explained by movements in another 
explanatory variable. Such a perfect linear function between two indepen-
dent variables would be:
	
X1i = α0 + α1X2i	
(8.1)
where the αs are constants and the Xs are independent variables in:
	
Yi = β0 + β1X1i + β2X2i + ei	
(8.2)
Notice that there is no error term in Equation 8.1. This implies that X1 can 
be exactly calculated given X2 and the equation. Typical equations for such 
perfect linear relationships would be:
	
X1i = 3X2i	
(8.3)
	
X1i = 2 + 4X2i	
(8.4)
What are some real-world examples of perfect multicollinearity? The sim-
plest examples involve the same variable measured in different units. Think 
about the distance between two cities measured in miles with X1 and in 
kilometers with X2. The data for the variables look quite different, but they’re 
1. The word collinearity describes a linear correlation between two independent variables, and 
multicollinearity indicates that more than two independent variables are involved. In common 
usage, multicollinearity is used to apply to both cases, and so we’ll typically use that term in 
this text even though many of the examples and techniques discussed relate, strictly speaking, 
to collinearity.


223
  Perfect versus Imperfect Multicollinearity
perfectly correlated! A more subtle example is when the two variables always 
add up to the same amount, for instance P1, the percent of voters who voted 
in favor of a proposition, and P2, the percent who voted against it (assuming 
no abstentions), would always add up to 100% and therefore would be per-
fectly (negatively) correlated.
Figure 8.1 shows a graph of explanatory variables that are perfectly cor-
related. As can be seen in Figure 8.1, a perfect linear function has all data 
points on the same straight line. There is none of the variation that accompa-
nies the data from a typical regression.
What happens to the estimation of an econometric equation where there 
is perfect multicollinearity? OLS is incapable of generating estimates of the 
regression coefficients, and most OLS computer programs will print out an 
error message in such a situation. Using Equation 8.2 as an example, we theo-
retically would obtain the following estimated coefficients and standard errors:
	
βN 1 = indeterminate  SE(βN 1) = ∞	
(8.5)
	
βN 2 = indeterminate  SE(βN 2) = ∞	
(8.6)
Perfect multicollinearity ruins our ability to estimate the coefficients because 
the two variables cannot be distinguished. You cannot “hold all the other 
independent variables in the equation constant” if every time one variable 
changes, another changes in an identical manner.
Figure 8.1  Perfect Multicollinearity
With perfect multicollinearity, an independent variable can be completely explained by the 
movements of one or more other independent variables. Perfect multicollinearity can usu-
ally be avoided by careful screening of the independent variables before a regression is run.
X1
0
X2


224
Chapter 8  Multicollinearity
Fortunately, instances in which one explanatory variable is a perfect linear 
function of another are rare. More important, perfect multicollinearity should 
be fairly easy to discover before a regression is run. You can detect perfect mul-
ticollinearity by asking whether one variable equals a multiple of another or 
if one variable can be derived by adding a constant to another or if a variable 
equals the sum of two other variables. If so, then one of the variables should be 
dropped because there is no essential difference between the two.
A special case related to perfect multicollinearity occurs when a variable 
that is definitionally related to the dependent variable is included as an inde-
pendent variable in a regression equation. Such a dominant variable is by 
definition so highly correlated with the dependent variable that it completely 
masks the effects of all other independent variables in the equation. In a 
sense, this is a case of perfect collinearity between the dependent variable and 
an independent variable.
For example, if you include a variable measuring the amount of raw mate-
rials used by the shoe industry in a production function for that industry, the 
raw materials variable would have an extremely high t-score, but otherwise 
important variables like labor and capital would have quite insignificant 
t-scores. Why? In essence, if you knew how much leather was used by a shoe 
factory, you could predict the number of pairs of shoes produced without 
knowing anything about labor or capital. The relationship is definitional, and 
the dominant variable should be dropped from the equation to get reason-
able estimates of the coefficients of the other variables.
Be careful, though! Dominant variables shouldn’t be confused with highly 
significant or important explanatory variables. Instead, they should be rec-
ognized as being virtually identical to the dependent variable. While the fit 
between the two is superb, knowledge of that fit could have been obtained 
from the definitions of the variables without any econometric estimation.
Imperfect Multicollinearity
Since perfect multicollinearity is fairly easy to avoid, econometricians rarely 
talk about it. Instead, when we use the word multicollinearity, we really are 
talking about severe imperfect multicollinearity. Imperfect multicollinearity 
can be defined as a linear functional relationship between two or more inde-
pendent variables that is so strong that it can significantly affect the estima-
tion of the coefficients of the variables.
In other words, imperfect multicollinearity occurs when two (or more) 
explanatory variables are imperfectly linearly related, as in:
	
X1i = α0 + α1X2i + ui	
(8.7)


225
  Perfect versus Imperfect Multicollinearity
Compare Equation 8.7 to Equation 8.1; notice that Equation 8.7 includes ui, 
a stochastic error term. This implies that although the relationship between 
X1 and X2 might be fairly strong, it is not strong enough to allow X1 to 
be completely explained by X2; some unexplained variation still remains. 
Figure 8.2 shows the graph of two explanatory variables that might be consid-
ered imperfectly multicollinear. Notice that although all the observations in 
the sample are fairly close to the straight line, there is still some variation in 
X1 that cannot be explained by X2.
Imperfect multicollinearity is a strong linear relationship between the 
explanatory variables. The stronger the relationship is between the two 
(or more) explanatory variables, the more likely it is that they’ll be con-
sidered significantly multicollinear. Two variables that might be only 
slightly related in one sample might be so strongly related in another that 
they could be considered to be imperfectly multicollinear. In this sense, it 
is fair to say that multicollinearity is a sample phenomenon as well as a 
theoretical one. This contrasts with perfect multicollinearity because two 
variables that are perfectly related probably can be detected on a logical 
basis. The detection of multicollinearity will be discussed in more detail in 
Section 8.3.
Figure 8.2  Imperfect Multicollinearity
With imperfect multicollinearity, an independent variable is a strong but not perfect 
linear function of one or more other independent variables. Imperfect multicollinearity 
varies in degree from sample to sample.
X1
0
X2


226
Chapter 8  Multicollinearity
8.2   The Consequences of Multicollinearity
If the multicollinearity in a particular sample is severe, what will happen 
to estimates calculated from that sample? The purpose of this section is to 
explain the consequences of multicollinearity and then to explore some 
examples of such consequences.
Recall the properties of OLS estimators that might be affected by this or 
some other econometric problem. In Chapter 4, we stated that the OLS esti-
mators are BLUE (or MvLUE) if the Classical Assumptions hold. This means 
that OLS estimates can be thought of as being unbiased and having the mini-
mum variance possible for unbiased linear estimators.
What Are the Consequences of Multicollinearity?
The major consequences of multicollinearity are:
1.	 Estimates will remain unbiased. Even if an equation has significant mul-
ticollinearity, the estimates of the βs still will be centered around the 
true population βs if the first six Classical Assumptions are met for a 
correctly specified equation.
2.	 The variances and standard errors of the estimates will increase. This is the 
principal consequence of multicollinearity. Since two or more of the 
explanatory variables are significantly related, it becomes difficult to 
precisely identify the separate effects of the multicollinear variables. 
When it becomes hard to distinguish the effect of one variable from 
the effect of another, we’re much more likely to make large errors in 
estimating the βs than we were before we encountered multicollinear-
ity. As a result, the estimated coefficients, although still unbiased, now 
come from distributions with much larger variances and, therefore, 
larger standard errors.
	
Even though the variances and standard errors are larger with mul-
ticollinearity than they are without it, OLS is still BLUE when multicol-
linearity exists. That is, no other linear unbiased estimation technique 
can get lower variances than OLS even in the presence of multicol-
linearity. Thus, although the effect of multicollinearity is to increase the 
variance of the estimated coefficients, OLS still has the property of mini-
mum variance. These “minimum variances” are just fairly large.
	
Figure 8.3 compares a distribution of βN s from a sample with severe 
multicollinearity to one with virtually no correlation between any of 
the independent variables. Notice that the two distributions have the 
same mean, indicating that multicollinearity does not cause bias. Also 


227
  The Consequences of Multicollinearity
note how much wider the distribution of βN  becomes when multicol-
linearity is severe; this is the result of the increase in the standard error 
of βN  that is caused by multicollinearity.
	
Because of this larger variance, multicollinearity increases the likeli-
hood of obtaining an unexpected sign2 for a coefficient even though, 
as mentioned earlier, multicollinearity causes no bias.
3.	 The computed t-scores will fall. Multicollinearity tends to decrease the 
t-scores of the estimated coefficients mainly because of the formula for 
the t-statistic:
	
tk =
1βN k - βH02
SE1βN k2
	
(8.8)
Figure 8.3  Severe Multicollinearity Increases the Variances of the 훃N s
Severe multicollinearity produces a distribution of the βNs that is centered around the 
true β but that has a much wider variance. Thus, the distribution of βNs with multicol-
linearity is much wider than otherwise.
b
b
With Severe
Multicollinearity
Without Severe
Multicollinearity
2. These unexpected signs generally occur because the distribution of the βN s with multicol-
linearity is wider than it would be without it, increasing the chance that a particular observed βN  
will be on the other side of zero from the true β (have an unexpected sign).


228
Chapter 8  Multicollinearity
Notice that this equation is divided by the standard error of the es-
timated coefficient. Multicollinearity increases the standard error of 
the estimated coefficient, and if the standard error increases, then the 
t-score must fall, as can be seen from Equation 8.8. Not surprisingly, 
it’s quite common to observe low t-scores in equations with severe 
multicollinearity.
	
Similarly, the computed confidence intervals will widen. Because 
multicollinearity increases the standard error of the estimated coef-
ficient, it makes the confidence interval wider (see Equation 5.9). Put 
differently, since βN  is likely to be farther from the true β, the confi-
dence interval is forced to increase.
4.	 Estimates will become very sensitive to changes in specification. The addi-
tion or deletion of an explanatory variable or of a few observations 
will often cause major changes in the values of the βN s when significant 
multicollinearity exists. If you drop a variable, even one that appears to 
be statistically insignificant, the coefficients of the remaining variables 
in the equation sometimes will change dramatically.
	
These large changes occur because OLS estimation is sometimes 
forced to emphasize small differences between variables in order 
to distinguish the effect of one multicollinear variable from that of 
another. If two variables are virtually identical throughout most of 
the sample, the estimation procedure relies on the observations in 
which the variables move differently in order to distinguish between 
them. As a result, a specification change that drops a variable that 
has an unusual value for one of these crucial observations can cause 
the estimated coefficients of the multicollinear variables to change 
dramatically.
5.	 The overall fit of the equation and the estimation of the coefficients of 
nonmulticollinear variables will be largely unaffected. Even though the 
individual t-scores are often quite low in a multicollinear equation, 
the overall fit of the equation, as measured by R  2, will not fall much, 
if at all, in the face of significant multicollinearity. Given this, one of 
the first indications of severe multicollinearity is the combination of 
a high R  2 with no statistically significant individual regression coeffi-
cients. Similarly, if an explanatory variable in an equation is not multi-
collinear with the other variables, then the estimation of its coefficient 
and standard error usually will not be affected.
	
Because the overall fit is largely unchanged, it’s possible for the 
F-test of overall significance to reject the null hypothesis even though 
none of the t-tests on individual coefficients can do so. Such a result is 
a clear indication of severe imperfect multicollinearity.


229
  The Consequences of Multicollinearity
	
Finally, since multicollinearity has little effect on the overall fit of 
the equation, it also will have little effect on the use of that equation 
for prediction or forecasting, as long as the independent variables 
maintain the same pattern of multicollinearity in the forecast period 
that they demonstrated in the sample.
Two Examples of the Consequences of Multicollinearity
To see what severe multicollinearity does to an estimated equation, let’s look 
at a hypothetical example. Suppose you decide to estimate a “student con-
sumption function.” After the appropriate preliminary work, you come up 
with the following hypothesized equation:
	
+ 	
-
	
COi = β0 + β1Ydi + β2LAi + ei	
(8.9)
where:	
COi = the annual consumption expenditures of the ith student 
on items other than tuition and room and board
	
Ydi  = the annual disposable income (including gifts) of that 
student
	
LAi  = the liquid assets (savings, etc.) of the ith student
	
ei
 = a stochastic error term
You then collect a small amount of data from people who are sitting near you 
in class:
Student
COi
Ydi
LAi
Mary
$2000
$2500
$25000
Robby
2300
3000
31000
Bevin
2800
3500
33000
Lesley
3800
4000
39000
Brandon
3500
4500
48000
Bruce
5000
5000
54000
Harwood
4500
5500
55000
Datafile = CONS8
If you run an OLS regression on your data set for Equation 8.9, you obtain:
	
 COi = -367.83 + 0.5113Ydi +  0.0427LAi	
(8.10)
	
 11.03072
 10.09422
	
 t = 0.496
 0.453
	
R2 = .835
8


230
Chapter 8  Multicollinearity
On the other hand, if you had consumption as a function of disposable 
income alone, then you would have obtained:
	
 COi = - 471.43 + 0.9714Ydi	
(8.11)
	
 10.1572
	
 t = 6.187
	
R  2 = .861
Notice from Equations 8.10 and 8.11 that the t-score for disposable income 
increases more than tenfold when the liquid assets variable is dropped from 
the equation. Why does this happen? First of all, the correlation between 
Yd and LA is quite high. This high degree of correlation causes the standard 
errors of the estimated coefficients to be very high when both variables are 
included. In the case of βN Yd, the standard error goes from 0.157 to 1.03 with 
the inclusion of LA! In addition, the coefficient estimate itself changes some-
what. Further, note that the R  2s of the two equations are quite similar despite 
the large differences in the significance of the explanatory variables in the 
two equations. It’s quite common for R  2 to stay virtually unchanged when 
multicollinear variables are dropped. All of these results are typical of equa-
tions with multicollinearity.
Which equation is better? If the liquid assets variable theoretically belongs 
in the equation, then to drop it will run the risk of omitted variable bias, but 
to include the variable will mean certain multicollinearity. There is no auto-
matic answer when dealing with multicollinearity. We’ll discuss this issue in 
more detail in Sections 8.4 and 8.5.
A second example of the consequences of multicollinearity is based on 
actual rather than hypothetical data. Suppose you’ve decided to build a cross-
sectional model of the demand for gasoline by state:
	
+ 	
- 	
+
	
PCONi = β0 + β1UHMi + β2TAXi + β3REGi + ei	
(8.12)
where:	
PCONi = petroleum consumption in the ith state (trillions of 
BTUs)
	
UHMi  = urban highway miles within the ith state
	
TAXi
 = the gasoline tax rate in the ith state (cents per gallon)
	
REGi
 = motor vehicle registrations in the ith state (thousands)
Given the definitions, let’s move on to the estimation of Equation 8.12 
using a linear functional form (assuming a classical error term):
	
 PCONi = 389.6 +  60.8UHMi -  36.5TAXi -  0.061REGi	
(8.13)
	
 110.32
 113.22
 10.0432
	
 t = 5.92
 - 2.77
 - 1.43
	
N = 50  R2 = .919	
8
h


231
  The Consequences of Multicollinearity
What’s wrong with this equation? The motor vehicle registrations variable 
has an insignificant coefficient with an unexpected sign, but it’s hard to 
believe that the variable is irrelevant. Is an omitted variable causing bias? It’s 
possible, but adding a variable is unlikely to fix things. Does it help to know 
that the correlation between REG and UHM is extremely high? Given that, it 
seems fair to say that one of the two variables is redundant; both variables are 
really measuring the size of the state, so we have multicollinearity.
Notice the impact of the multicollinearity on the equation. The coefficient 
of a variable such as motor vehicle registrations, which has a very strong theo-
retical relationship to petroleum consumption, is insignificant and has a sign 
contrary to our expectations. This is mainly because the multicollinearity has 
increased the variance of the distribution of the estimated βN s.
What would happen if we were to drop one of the multicollinear variables?
	
 PCONi = 551.7 - 53.6TAXi +  0.186REGi	
(8.14)
	
 116.92
 10.0122
	
 t = - 3.18
 15.88
	
N = 50  R  2 = .861	
Dropping UHM has made REG extremely significant. Why did this occur? 
The answer is that the standard error of the coefficient of REG has fallen 
substantially (from 0.043 to 0.012) now that the multicollinearity has been 
removed from the equation. Also note that the sign of the estimated coeffi-
cient has now become positive as hypothesized. The reason is that REG and 
UHM are virtually indistinguishable from an empirical point of view, and so 
the OLS program latched on to minor differences between the variables to 
explain the movements of PCON. Once the multicollinearity was removed, 
the direct positive relationship between REG and PCON was obvious.
Either UHM or REG could have been dropped with similar results because 
the two variables are, in a quantitative sense, virtually identical. In fact, our 
guess is that a majority of experienced econometricians, when faced with the 
results in Equation 8.13 and the high correlation between REG and UHM, 
would have dropped REG and kept UHM. Why did we do the opposite? Our 
opinion is that because UHM is an urban variable and REG is a statewide 
variable, REG is preferable from a theoretical standpoint if we’re trying to 
understand statewide petroleum consumption. Since the two are identical 
quantitatively and REG is preferable theoretically, we’d keep REG, but we rec-
ognize that others could look at the same results and come to a different con-
clusion. Even though R  2 fell when UHM was dropped, Equation 8.14 should 
be considered superior to Equation 8.13. This is an example of the point, first 
made in Chapter 2, that the fit of the equation is not the most important cri-
terion to be used in determining its overall quality.
h


232
Chapter 8  Multicollinearity
8.3   The Detection of Multicollinearity
How do we decide whether an equation has a severe multicollinearity problem? 
A first step is to recognize that some multicollinearity exists in every equation. It’s 
virtually impossible in a real-world example to find a set of explanatory variables 
that are totally uncorrelated with each other (except for designed experiments). 
Our main purpose in this section will be to learn to determine how much multi-
collinearity exists in an equation, not whether any multicollinearity exists.
A second key point is that the severity of multicollinearity in a given equa-
tion can change from sample to sample depending on the characteristics of 
the sample. As a result, the theoretical underpinnings of the equation are 
not quite as important in the detection of multicollinearity as they are in the 
detection of an omitted variable or an incorrect functional form. Instead, 
we tend to rely more on data-oriented techniques to determine the severity 
of the multicollinearity in a given sample. Of course, we can never ignore the 
theory behind an equation. The trick is to find variables that are theoretically 
relevant (for meaningful interpretation) and that are also statistically non-
multicollinear (for meaningful inference).
Because multicollinearity is a sample phenomenon and the level of dam-
age of its impact is a matter of degree, many of the methods used to detect 
it are informal tests without critical values or levels of significance. Indeed, 
there are no generally accepted, true statistical tests for multicollinearity. 
Most researchers develop a general feeling for the severity of multicollinearity 
in an estimated equation by looking at a number of the characteristics of that 
equation. Let’s examine two of the most frequently used characteristics.
High Simple Correlation Coefficients
One way to detect severe multicollinearity is to examine the simple correla-
tion coefficients between the explanatory variables. The simple correlation 
coefficient, r, is a measure of the strength and direction of the linear relation-
ship between two variables.3 The range of r is from +1 to -1, and the sign 
of r indicates the direction of the correlation between the two variables. The 
3. The equation for r12, the simple correlation coefficient between X1 and X2, is:
	
r12 =
g31X1i - X121X2i - X224
2g1X1i - X122 g1X2i - X222
Interestingly, it turns out that r and R2 are related if the estimated equation has exactly one in-
dependent variable. The square of r equals R2 for a regression where one of the two variables is 
the dependent variable and the other is the only independent variable.


233
  The Detection of Multicollinearity
closer the absolute value of r is to 1, the stronger is the correlation between 
the two variables. Thus:
If two variables are perfectly positively correlated, then r = +1
If two variables are perfectly negatively correlated, then r = -1
If two variables are totally uncorrelated, then r = 0
If an r is high in absolute value, then we know that these two particular 
Xs are quite correlated and that multicollinearity is a potential problem. For 
example, in Equation 8.10, the simple correlation coefficient between dispos-
able income and liquid assets is 0.986. A simple correlation coefficient this 
high, especially in an equation with only two independent variables, is a cer-
tain indication of severe multicollinearity.
How high is high? Some researchers pick an arbitrary number, such as 
0.80, and become concerned about multicollinearity any time the absolute 
value of a simple correlation coefficient exceeds 0.80. A better answer might 
be that r is high if it causes unacceptably large variances in the coefficient esti-
mates in which we’re interested.
Be careful: The use of simple correlation coefficients as an indication of the 
extent of multicollinearity involves a major limitation if there are more than two 
explanatory variables. It is quite possible for groups of independent variables, 
acting together, to cause multicollinearity without any single simple correlation 
coefficient being high enough to indicate that multicollinearity is in fact severe. 
As a result, simple correlation coefficients must be considered to be sufficient but 
not necessary tests for multicollinearity. Although a high r does indeed indicate 
the probability of severe multicollinearity, a low r by no means proves otherwise.4
High Variance Inflation Factors (VIFs)
The use of tests to give an indication of the severity of multicollinearity in 
a particular sample is controversial. Some econometricians reject even the 
simple correlation coefficient, mainly because of the limitations cited. Others 
tend to use a variety of more formal tests.5
4. Most authors criticize the use of simple correlation coefficients to detect multicollinearity in 
equations with large numbers of explanatory variables, but many researchers continue to do so 
because a scan of the simple correlation coefficients is a “quick and dirty” way to get a feel for 
the degree of multicollinearity in an equation.
5. Perhaps the best of these is the Condition number. For more on the Condition number, 
which is a single index of the degree of multicollinearity in the overall equation, see D. A. 
Belsley, Conditioning Diagnostics (New York: Wiley, 1991).


234
Chapter 8  Multicollinearity
One measure of the severity of multicollinearity that is easy to use and that 
is gaining in popularity is the variance inflation factor. The variance infla-
tion factor (VIF) is a method of detecting the severity of multicollinearity by 
looking at the extent to which a given explanatory variable can be explained 
by all the other explanatory variables in the equation. There is a VIF for each 
explanatory variable in an equation. The VIF is an index of how much multi-
collinearity has increased the variance of an estimated coefficient. A high VIF 
indicates that multicollinearity has increased the estimated variance of the 
estimated coefficient by quite a bit, yielding a decreased t-score.
Suppose you want to use the VIF to attempt to detect multicollinearity in 
an original equation with K independent variables:
	
Y = β0 + β1X1 + β2X2 + g + βKXK + e
Doing so requires calculating K different VIFs, one for each Xi. Calculating 
the VIF for a given Xi involves two steps:
1.	 Run an OLS regression that has Xi as a function of all the other explanatory 
variables in the equation. For i = 1, this equation would be:
	
X1 = α1 + α2X2 + α3X3 + g + αKXK + v	
(8.15)
	
where v is a classical stochastic error term. Note that X1 is not included 
on the right-hand side of Equation 8.15, which is referred to as an 
auxiliary or secondary regression. Thus there are K auxiliary regres-
sions, one for each independent variable in the original equation.
2.	 Calculate the variance inflation factor for βN i:
	
VIF1βN i2 =
1
11 - R2
i 2	
(8.16)
	
where R2
i  is the coefficient of determination (the unadjusted R2) of the 
auxiliary regression in step one. Since there is a separate auxiliary re-
gression for each independent variable in the original equation, there 
also is an R2
i  and a VIF1βN i2 for each Xi. The higher the VIF, the more 
severe the effects of multicollinearity.
How high is high? An R2
i  of 1, indicating perfect multicollinearity, pro-
duces a VIF of infinity, whereas an R2
i  of 0, indicating no multicollinearity at 
all, produces a VIF of 1. While there is no table of formal critical VIF values, a 
common rule of thumb is that if VIF1βi2 7 5, the multicollinearity is severe. 
As the number of independent variables increases, it makes sense to increase 
this number slightly.
For example, let’s return to Equation 8.10 and calculate the VIFs for both 
independent variables. Both VIFs equal 36, confirming the quite severe 


235
  Remedies for Multicollinearity
multicollinearity we already know exists. It’s no coincidence that the VIFs 
for the two variables are equal. In an equation with exactly two independent 
variables, the two auxiliary equations will have identical R2
i s, leading to equal 
VIFs.6
Some authors and statistical software programs replace the VIF with its 
reciprocal, 11 - R2
i 2, called tolerance, or TOL. Whether we calculate VIF or 
TOL is a matter of personal preference, but either way, the general approach 
is the most comprehensive multicollinearity detection technique we’ve dis-
cussed in this text.
Unfortunately, there are a couple of problems with using VIFs. First, as 
mentioned, there is no hard-and-fast VIF decision rule. Second, it’s pos-
sible to have multicollinear effects in an equation that has no large VIFs. For 
instance, if the simple correlation coefficient between X1 and X2 is 0.88, mul-
ticollinear effects are quite likely, and yet the VIF for the equation (assuming 
no other Xs) is only 4.4.
In essence, then, the VIF is a sufficient but not necessary test for multicol-
linearity, just like the other test described in this section. Indeed, as is prob-
ably obvious to the reader by now, there is no test that allows a researcher to 
reject the possibility of multicollinearity with any real certainty.
8.4   Remedies for Multicollinearity
What can be done to minimize the consequences of severe multicollinearity? 
There is no automatic answer to this question because multicollinearity is a 
phenomenon that could change from sample to sample even for the same 
specification of a regression equation. The purpose of this section is to out-
line a number of alternative remedies for multicollinearity that might be 
appropriate under certain circumstances.
Do Nothing
The first step to take once severe multicollinearity has been diagnosed is to 
decide whether anything should be done at all. As we’ll see, it turns out that 
every remedy for multicollinearity has a drawback of some sort, and so it 
often happens that doing nothing is the correct course of action.
One reason for doing nothing is that multicollinearity in an equation will 
not always reduce the t-scores enough to make them insignificant or change 
6. Another use for the R2s of these auxiliary equations is to compare them with the overall 
equation’s R2. If an auxiliary equation’s R2 is higher, it’s yet another sign of multicollinearity.


236
Chapter 8  Multicollinearity
the βN s enough to make them differ from expectations. In other words, the 
mere existence of multicollinearity does not necessarily mean anything. A 
remedy for multicollinearity should be considered only if the consequences 
cause insignificant t-scores or unreliable estimated coefficients. For example, 
it’s possible to observe a simple correlation coefficient of .97 between two 
explanatory variables and yet have each individual t-score be significant. It 
makes no sense to consider remedial action in such a case, as long as both 
variables belong in the equation on theoretical grounds, because any remedy 
for multicollinearity would probably cause other problems for the equation. 
In a sense, multicollinearity is similar to a non-life-threatening human dis-
ease that requires general anesthesia to operate on the patient: The risk of the 
operation should be undertaken only if the disease is causing a significant 
problem.
A second reason for doing nothing is that the deletion of a multicollinear 
variable that belongs in an equation will cause specification bias. If we drop 
a theoretically important variable, then we are purposely creating bias. Given 
all the effort typically spent avoiding omitted variables, it seems foolhardy 
to consider running that risk on purpose. As a result, experienced econo-
metricians often will leave multicollinear variables in equations despite low 
t-scores.
The final reason for considering doing nothing to offset multicollinearity 
is that every time a regression is rerun, we risk encountering a specification 
that fits because it accidentally works for the particular data set involved, not 
because it is the truth. The larger the number of experiments, the greater the 
chances of finding the accidental result. To make things worse, when there 
is significant multicollinearity in the sample, the odds of strange results 
increase rapidly because of the sensitivity of the coefficient estimates to slight 
specification changes.
To sum, it is often best to leave an equation unadjusted in the face of all 
but extreme multicollinearity. Such advice might be difficult for beginning 
researchers to take, however, if they think that it’s embarrassing to report that 
their final regression is one with insignificant t-scores. Compared to the alter-
natives of possible omitted variable bias or accidentally significant regression 
results, the low t-scores seem like a minor problem. For an example of “doing 
nothing” in the face of severe multicollinearity, see Section 8.5.
Drop a Redundant Variable
On occasion, the simple solution of dropping one of the multicollinear vari-
ables is a good one. For example, some inexperienced researchers include too 
many variables in their regressions, not wanting to face omitted variable bias. 


237
  Remedies for Multicollinearity
As a result, they often have two or more variables in their equations that are 
measuring essentially the same thing. In such a case the multicollinear vari-
ables are not irrelevant, since any one of them is quite probably theoretically 
and statistically sound. Instead, the variables might be called redundant; 
only one of them is needed to represent the effect on the dependent variable 
that all of them currently represent. For example, in an aggregate demand 
function, it would not make sense to include disposable income and GDP 
because both are measuring the same thing: income. A bit more subtle is 
the inference that population and disposable income should not both be 
included in the same aggregate demand function because, once again, they 
really are measuring the same thing: the size of the aggregate market. As pop-
ulation rises, so too will income. Dropping these kinds of redundant multi-
collinear variables is doing nothing more than making up for a specification 
error; the variables should never have been included in the first place.
To see how this solution would work, let’s return to the student consump-
tion function example of Equation 8.10:
	
 COi = -367.83 + 0.5113Ydi +  0.0427LAi
	
(8.10)
	
 11.03072
 10.09422
	
 t = 0.496  0.453  R  2 = .835
where CO = consumption, Yd = disposable income, and LA = liquid 
assets. When we first discussed this example, we compared this result to the 
same equation without the liquid assets variable:
	
 COi = -471.43 + 0.9714Ydi
	
(8.11)
	
 10.1572
	
 t = 6.187  R  2 = .861	
If we had instead dropped the disposable income variable, we would have 
obtained:
	
 COi = -199.44 + 0.08876LAi
	
(8.17)
	
 10.014432
	
 t = 6.153  R  2 = .860	
Note that dropping one of the multicollinear variables has eliminated both 
the multicollinearity between the two explanatory variables and the low t-score 
of the coefficient of the remaining variable. By dropping Yd, we were able to 
increase tLA from 0.453 to 6.153. Since dropping a variable changes the mean-
ing of the remaining coefficient (because the dropped variable is no longer 
being held constant), such dramatic changes are not unusual. The coefficient 
of the remaining included variable also now measures almost all of the joint 
impact on the dependent variable of the multicollinear explanatory variables.
8
8
8


238
Chapter 8  Multicollinearity
Assuming you want to drop a variable, how do you decide which variable 
to drop? In cases of severe multicollinearity, it makes no statistical differ-
ence which variable is dropped. As a result, it doesn’t make sense to pick the 
variable to be dropped on the basis of which one gives superior fit or which 
one is more significant (or has the expected sign) in the original equation. 
Instead, the theoretical underpinnings of the model should be the basis for 
such a decision. In the example of the student consumption function, there 
is more theoretical support for the hypothesis that disposable income deter-
mines consumption than there is for the liquid assets hypothesis. Therefore, 
Equation 8.11 should be preferred to Equation 8.17.
Increase the Size of the Sample
Another way to deal with multicollinearity is to attempt to increase the size 
of the sample to reduce the degree of multicollinearity. Although such an 
increase may be impossible, it’s a useful alternative to be considered when 
feasible.
The idea behind increasing the size of the sample is that a larger data set 
(often requiring new data collection) will allow more accurate estimates than 
a small one, since the larger sample normally will reduce the variance of the 
estimated coefficients, diminishing the impact of the multicollinearity.
For most time series data sets, however, this solution isn’t feasible. After 
all, samples typically are drawn by getting all the available data that seem 
similar. As a result, new data are generally impossible or quite expensive to 
find. Going out and generating new data is much easier with a cross-sectional 
or experimental data set than it is when the observations must be generated 
by the passage of time.
8.5   An Example of Why Multicollinearity Often Is Best 
Left Unadjusted
Let’s look at an example of the idea that multicollinearity often should be left 
unadjusted. Suppose you work in the marketing department of a hypotheti-
cal soft drink company and you build a model of the impact on sales of your 
firm’s advertising:
	
 SN t = 3080 - 75,000Pt +  4.23At -  1.04Bt	
(8.18)
	
 125,0002
 11.062
 10.512
	
 t = - 3.00
 3.99
 - 2.04
	
R  2 = .825  N = 28	


239
  An Example of Why Multicollinearity Often Is Best Left Unadjusted
where:	
St  = sales of the soft drink in year t
	
Pt = average relative price of the drink in year t
	
At = advertising expenditures for the company in year t
	
Bt = advertising expenditures for the company’s main 
competitor in year t
Assume that there are no omitted variables. All variables are measured in real 
dollars; that is, the nominal values are divided, or deflated, by a price index.
On the face of it, this is a reasonable-looking result. Estimated coefficients 
are significant in the directions implied by the underlying theory, and both the 
overall fit and the size of the coefficients seem acceptable. Suppose you now 
were told that advertising in the soft drink industry is cut-throat in nature and 
that firms tend to match their main competitor’s advertising expenditures. This 
would lead you to suspect that significant multicollinearity was possible. Fur-
ther suppose that the simple correlation coefficient between the two advertis-
ing variables is .974 and that their respective VIFs are well over 5.
Such a correlation coefficient is evidence that there is severe multicol-
linearity in the equation, but there is no reason even to consider doing 
anything about it, because the coefficients are so powerful that their t-scores 
remain significant, even in the face of severe multicollinearity. Unless multi-
collinearity causes problems in the equation, it should be left unadjusted. To 
change the specification might give us better-looking results, but the adjust-
ment would decrease our chances of obtaining the best possible estimates of 
the true coefficients. Although it’s certainly lucky that there were no major 
problems due to multicollinearity in this example, that luck is no reason to 
try to fix something that isn’t broken.
When a variable is dropped from an equation, its effect will be absorbed 
by the other explanatory variables to the extent that they are correlated with 
the newly omitted variable. It’s likely that the remaining multicollinear 
variable(s) will absorb virtually all the bias, since the variables are highly cor-
related. This bias may destroy whatever usefulness the estimates had before 
the variable was dropped.
For example, if a variable, say B, is dropped from the equation to fix the 
multicollinearity, then the following might occur:
	
 SN t = 2586 - 78,000Pt +  0.52At	
(8.19)
	
 124,0002  14.322
	
 t = - 3.25
 0.12
	
R2 = .531  N = 28
What’s going on here? The company’s advertising coefficient becomes less 
significant instead of more significant when one of the multicollinear 
variables is dropped. To see why, first note that the expected bias on βN A is 


240
Chapter 8  Multicollinearity
negative because the product of the expected sign of the coefficient of B and 
of the correlation between A and B is negative:
	
Bias = βB # αN 1 = 1 - 21 + 2 = -	
(8.20)
Second, this negative bias is strong enough to decrease the estimated coef-
ficient of A until it is insignificant. Although this problem could have been 
avoided by using a relative advertising variable (A divided by B, for instance), 
that formulation would have forced identical absolute coefficients on A and 
1/B. Such identical coefficients will sometimes be theoretically expected or 
empirically reasonable but, in most cases, these kinds of constraints will force 
bias onto an equation that previously had none.
This example is simplistic, but its results are typical in cases in which equa-
tions are adjusted for multicollinearity by dropping a variable without regard 
to the effect that the deletion is going to have. The point here is that it’s quite 
often theoretically or operationally unwise to drop a variable from an equa-
tion and that multicollinearity in such cases is best left unadjusted.
8.6   Summary
	 1.	 Perfect multicollinearity is the violation of the assumption that no 
explanatory variable is a perfect linear function of other explana-
tory variable(s). Perfect multicollinearity results in indeterminate 
estimates of the regression coefficients and infinite standard errors of 
those estimates, making OLS estimation impossible.
	 2.	 Imperfect multicollinearity, which is what is typically meant when the 
word “multicollinearity” is used, is a linear relationship between two 
or more independent variables that is strong enough to significantly 
affect the estimation of the equation. Multicollinearity is a sample 
phenomenon as well as a theoretical one. Different samples can ex-
hibit different degrees of multicollinearity.
	 3.	 The major consequence of severe multicollinearity is to increase 
the variances of the estimated regression coefficients and therefore 
decrease the calculated t-scores of those coefficients and expand the 
confidence intervals. Multicollinearity causes no bias in the estimated 
coefficients, and it has little effect on the overall significance of the 
regression or on the estimates of the coefficients of any nonmulticol-
linear explanatory variables.
	 4.	 Since multicollinearity exists, to one degree or another, in virtually 
every data set, the question to be asked in detection is how severe the 
multicollinearity in a particular sample is.


241
Exercises
	 5.	 Two useful methods for the detection of severe multicollinearity are:
a.	Are the simple correlation coefficients between the explanatory 
variables high?
b.	Are the variance inflation factors high?
	
	 If either of these answers is yes, then multicollinearity certainly exists, 
but multicollinearity can also exist even if the answers are no.
	 6.	 The three most common remedies for multicollinearity are:
a.	Do nothing (and thus avoid specification bias).
b.	Drop a redundant variable.
c.	 Increase the size of the sample.
	 7.	 Quite often, doing nothing is the best remedy for multicollinearity. If 
the multicollinearity has not decreased t-scores to the point of insig-
nificance, then no remedy should even be considered as long as the 
variables are theoretically strong. Even if the t-scores are insignificant, 
remedies should be undertaken cautiously, because all impose costs 
on the estimation that may be greater than the potential benefit of 
ridding the equation of multicollinearity.
Exercises
(The answers to the even-numbered exercises are in Appendix A.)
	 1.	 Write the meaning of each of the following terms without referring to 
the book (or your notes), and compare your definition with the ver-
sion in the text for each.
a.	dominant variable (p. 224)
b.	imperfect multicollinearity (p. 224)
c.	 perfect multicollinearity (p. 222)
d.	redundant variable (p. 237)
e.	 simple correlation coefficient (p. 232)
f.	 variance inflation factor (p. 234)
	 2.	 A recent study of the salaries of elementary school teachers in a small 
school district in Northern California came up with the following 
estimated equation (Note: t-scores in parentheses!):
lnSALi = 10.5 -  0.006EMPi +  0.002UNITSi +  0.079LANGi +  0.020EXPi
 1 -0.982 
 12.392 
 12.082 
 14.972
	
 R  2 = .866   N = 25	
(8.21)
h


242
Chapter 8  Multicollinearity
	
where:	
SALi
 = the salary of the ith teacher (in dollars)
	
	
EMPi
 = the years that the ith teacher has worked in 
this school district
	
	
UNITSi = the units of graduate work completed by the ith 
teacher
	
	
LANGi  = a dummy variable equal to 1 if the ith teacher 
speaks two languages
	
	
EXPi
 = the total years of teaching experience of the ith 
teacher
a.	Make up and test appropriate hypotheses for the coefficients of this 
equation at the 5-percent level.
b.	What is the functional form of this equation? Does it seem appro-
priate? Explain.
c.	 What econometric problems (out of irrelevant variables, omitted 
variables, and multicollinearity) does this equation appear to have? 
Explain.
d.	Suppose that you now are told that the simple correlation coef-
ficient between EMP and EXP is .89 and that the VIFs for EMP and 
EXP are both just barely over 5. Does this change your answer to 
part c above? How?
e.	 What remedy for the problem you identify in part d do you recom-
mend? Explain.
f.	 If you drop EMP from the equation, the estimated equation be-
comes Equation 8.22. Use our four specification criteria to decide 
whether you prefer Equation 8.21 or Equation 8.22. Which do you 
like better? Why?
	
lnSALi = 10.5 +  0.002UNITSi +  0.081LANGi +  0.015EXPi	 (8.22)
	
 
 12.472  
 12.092  
 18.652
	
 R  2 = .871  N = 25	
	 3.	 A researcher once attempted to estimate an asset demand equa-
tion that included the following three explanatory variables: current 
wealth Wt, wealth in the previous quarter Wt-1, and the change in 
wealth ∆Wt = Wt - Wt-1. What problem did this researcher encoun-
ter? What should have been done to solve this problem?
	 4.	 In each of the following situations, determine whether the variable 
involved is a dominant variable:
a.	games lost in year t in an equation for the number of games won in 
year t by a baseball team that plays the same number of games each 
year
h


243
Exercises
b.	number of Woody’s restaurants in a model of the total sales of the 
entire Woody’s chain of restaurants
c.	 disposable income in an equation for aggregate consumption 
expenditures
d.	number of tires purchased in an annual model of the number of auto-
mobiles produced by an automaker that does not make its own tires
e.	 number of acres planted in an agricultural supply function
	 5.	 In 1998, Mark McGwire hit 70 homers to break Roger Maris’s old 
record of 61, and yet McGwire wasn’t voted the Most Valuable Player 
(MVP) in his league. To try to understand how this happened, you 
collect the following data on MVP votes, batting average (BA), home 
runs (HR), and runs batted in (RBI) from the 1998 National League:
Name
Votes
BA
HR
RBI
Sosa
438
.308
66
158
McGwire
272
.299
70
147
Alou
215
.312
38
124
Vaughn
185
.272
50
119
Biggio
163
.325
20
88
Galarraga
147
.305
44
121
Bonds
66
.303
37
122
Jones
56
.313
34
107
Datafile = MVP8
	
	 Just as you are about to run the regression, your friend warns you that 
you probably have multicollinearity.
a.	What should you do about your friend’s warning before running 
the regression?
b.	Run the regression implied in this example (votes as a function of 
BA, HR, and RBI), with positive expected signs for all three slope 
coefficients. What signs of multicollinearity are there?
c.	 What suggestions would you make for another run of this equation? 
In particular, what would you do about multicollinearity?
	 6.	 Consider the following regression result paraphrased from a study 
conducted by the admissions office at the Stanford Business School 
(standard errors in parentheses):
	
 GN i = 1.00 + 0.005Mi +  0.20Bi -  0.10Ai +  0.25Si
	
 10.0012
 10.202
 10.102
 10.102
	
R  2 = .20  N = 1000


244
Chapter 8  Multicollinearity
	
where:	
Gi = the Stanford Business School GPA of the ith 
student (4 = high)
	
	
Mi = the score on the graduate management admission 
test of the ith student (800 = high)
	
	
Bi  = the number of years of business experience of the 
ith student
	
	
Ai  = the age of the ith student
	
	
Si  = dummy equal to 1 if the ith student was an eco-
nomics major, 0 otherwise
a.	Theorize the expected signs of all the coefficients (try not to look at 
the results) and test these expectations with appropriate hypotheses 
(including choosing a significance level).
b.	Do any problems appear to exist in this equation? Explain your 
answer.
c.	 How would you react if someone suggested a polynomial func-
tional form for A? Why?
d.	What suggestions (if any) would you have for another run of this 
equation?
	 7.	 Calculating VIFs typically involves running sets of auxiliary regres-
sions, one regression for each independent variable in an equation. 
To get practice with this procedure, calculate the following:
a.	the VIFs for N, P, and I from the Woody’s data in Table 3.1
b.	the VIFs for BETA, EARN, and DIV from the stock price example 
data in Table 7.2
c.	 the VIF for X1 in an equation where X1 and X2 are the only inde-
pendent variables, given that the VIF for X2 is 3.8 and N = 28
d.	the VIF for X1 in an equation where X1 and X2 are the only inde-
pendent variables, given that the simple correlation coefficient be-
tween X1 and X2 is 0.80 and N = 15
8.7   Appendix: The SAT Interactive Regression  
Learning Exercise
Econometrics is difficult to learn by reading examples, no matter how good 
they are. Most econometricians, the author included, had trouble under-
standing how to use econometrics, particularly in the area of specification 
choice, until they ran their own regression projects. This is because there’s an 
element of econometric understanding that is better learned by doing than by 
reading about what someone else is doing.


245
  Appendix: The SAT Interactive Regression Learning Exercise 
Unfortunately, mastering the art of econometrics by running your own 
regression projects without any feedback is also difficult because it takes 
quite a while to learn to avoid some fairly simple mistakes. Probably the 
best way to learn is to work on your own regression project, analyzing your 
own problems and making your own decisions, but with a more experienced 
econometrician nearby to give you one-on-one feedback on exactly which of 
your decisions were inspired and which were flawed (and why).
This section is an attempt to give you an opportunity to make indepen-
dent specification decisions and to then get feedback on the advantages or 
disadvantages of those decisions. Using the interactive learning exercise of 
this section requires neither a computer nor a tutor, although either would 
certainly be useful. Instead, we have designed an exercise that can be used on 
its own to help to bridge the gap between the typical econometrics examples 
(which require no decision making) and the typical econometrics projects 
(which give little feedback). An additional interactive learning exercise is pre-
sented in Chapter 11.
STOP!
To get the most out of the exercise, it’s important to follow the instructions 
carefully. Reading the pages in order as with any other example will waste 
your time, because once you have seen even a few of the results, the benefits 
to you of making specification decisions will diminish. In addition, you 
shouldn’t look at any of the regression results until you have specified your 
first equation.
Building a Model of Scholastic Aptitude Test Scores
The dependent variable for this interactive learning exercise is the combined 
“two-test” SAT score, math plus verbal, earned by students in the senior class 
at Arcadia High School. Arcadia is an upper-middle-class suburban commu-
nity located near Los Angeles, California. Out of a graduating class of about 
640, a total of 65 students who had taken the SATs were randomly selected 
for inclusion in the data set. In cases in which a student had taken the test 
more than once, the highest score was recorded.
A review of the literature on the SAT shows many more psychological stud-
ies and popular press articles than econometric regressions. Many articles have 
been authored by critics of the SAT, who maintain (among other things) that 
it is biased against women and minorities. In support of this argument, these 
critics have pointed to national average scores for women and some minorities, 
which in recent years have been significantly lower than the national averages 


246
Chapter 8  Multicollinearity
for white males. Any reader interested in reviewing a portion of the applicable 
literature should do so now before continuing on with the section.7
If you were going to build a single-equation linear model of SAT scores, 
what factors would you consider? First, you’d want to include some measures 
of a student’s academic ability. Three such variables are cumulative high 
school grade point average (GPA) and participation in advanced placement 
math and English courses (APMATH and APENG). Advanced placement (AP) 
classes are academically rigorous courses that may help a student do well 
on the SAT. More important, students are invited to be in AP classes on the 
basis of academic potential, and students who choose to take AP classes are 
revealing their interest in academic subjects, both of which bode well for SAT 
scores. GPAs at Arcadia High School are weighted GPAs; each semester that a 
student takes an AP class adds one extra point to his or her total grade points. 
(For example, a semester grade of “A” in an AP math class counts for five 
grade points as opposed to the conventional four points.)
A second set of important considerations includes qualitative factors that 
may affect performance on the SAT. Available dummy variables in this cat-
egory include measures of a student’s gender (GEND), ethnicity (RACE), and 
native language (ESL). All of the students in the sample are either Asian or 
Caucasian, and RACE is assigned a value of 1 if a student is Asian. Asian stu-
dents are a substantial proportion of the student body at Arcadia High. The 
ESL dummy is given a value of 1 if English is a student’s second language. In 
addition, studying for the test may be relevant, so a dummy variable indicat-
ing whether or not a student has attended an SAT preparation class (PREP) is 
also included in the data.
To sum, the explanatory variables available for you to choose for your 
model are:
GPAi
 = the weighted GPA of the ith student
APMATHi = a dummy variable equal to 1 if the ith student has taken 
AP math, 0 otherwise
APENGi  = a dummy variable equal to 1 if the ith student has taken 
AP English, 0 otherwise
APi
 = a dummy variable equal to 1 if the ith student has taken 
AP math and/or AP English, 0 if the ith student has taken 
neither
7. See, for example, James Fallows, “The Tests and the ‘Brightest’: How Fair Are the College 
Boards?” The Atlantic, Vol. 245, No. 2, pp. 37–48. We are grateful to former Occidental student 
Bob Sego for his help in preparing this interactive exercise.


247
  Appendix: The SAT Interactive Regression Learning Exercise 
ESLi
 = a dummy variable equal to 1 if English is not the ith stu-
dent’s first language, 0 otherwise
RACEi
 = a dummy variable equal to 1 if the ith student is Asian, 0 
if the student is Caucasian
GENDi
 = a dummy variable equal to 1 if the ith student is male, 0 
if the student is female
PREPi
 = a dummy variable equal to 1 if the ith student has 
attended an SAT preparation course, 0 otherwise
The data for these variables are presented in Table 8.1.
Now:
1.	 Hypothesize expected signs for the coefficients of each of these vari-
ables in an equation for the SAT score of the ith student. Examine each 
variable carefully; what is the theoretical content of your hypothesis?
2.	 Choose carefully the best set of explanatory variables. Start off by 
including GPA, APMATH, and APENG; what other variables do you 
think should be specified? Don’t simply include all the variables, 
intending to drop the insignificant ones. Instead, think through the 
problem carefully and find the best possible equation.
Once you’ve specified your equation, you’re ready to move on. Keep fol-
lowing the instructions in the exercise until you have specified your equation 
completely. You may take some time to think over the questions or take a 
break, but when you return to the interactive exercise, make sure to go back 
to the exact point from which you left rather than starting all over again. To 
the extent you can do it, try to avoid looking at the hints until after you’ve 
completed the entire project. The hints are there to help you if you get stuck, 
not to allow you to check every decision you make.
One final bit of advice: Each regression result is accompanied by a series of 
questions. Take the time to answer all these questions, in writing if possible. 
Rushing through this interactive exercise will lessen its effectiveness.
The SAT Score Interactive Regression Exercise
To start, choose the specification you’d like to estimate, find the regression 
run number8 of that specification in the list on pages 250 and 251, and then 
turn to that regression. Note that the simple correlation coefficient matrix for 
this data set is in Table 8.2 just before the results begin.
8. All the regression results appear exactly as they are produced by the Stata regression package.


248
Chapter 8  Multicollinearity
Table 8.1  Data for the SAT Interactive Learning Exercise
SAT
GPA
APMATH
APENG
AP
ESL
GEND
PREP
RACE
1060
3.74
0
1
1
0
0
0
0
740
2.71
0
0
0
0
0
1
0
1070
3.92
0
1
1
0
0
1
0
1070
3.43
0
1
1
0
0
1
0
1330
4.35
1
1
1
0
0
1
0
1220
3.02
0
1
1
0
1
1
0
1130
3.98
1
1
1
1
0
1
0
770
2.94
0
0
0
0
0
1
0
1050
3.49
0
1
1
0
0
1
0
1250
3.87
1
1
1
0
1
1
0
1000
3.49
0
0
0
0
0
1
0
1010
3.24
0
1
1
0
0
1
0
1320
4.22
1
1
1
1
1
0
1
1230
3.61
1
1
1
1
1
1
1
840
2.48
1
0
1
1
1
0
1
940
2.26
1
0
1
1
0
0
1
910
2.32
0
0
0
1
1
1
1
1240
3.89
1
1
1
0
1
1
0
1020
3.67
0
0
0
0
1
0
0
630
2.54
0
0
0
0
0
1
0
850
3.16
0
0
0
0
0
1
0
1300
4.16
1
1
1
1
1
1
0
950
2.94
0
0
0
0
1
1
0
1350
3.79
1
1
1
0
1
1
0
1070
2.56
0
0
0
0
1
0
0
1000
3.00
0
0
0
0
1
1
0
770
2.79
0
0
0
0
0
1
0
1280
3.70
1
0
1
1
0
1
1
590
3.23
0
0
0
1
0
1
1
1060
3.98
1
1
1
1
1
0
1
1050
2.64
1
0
1
0
0
0
0
1220
4.15
1
1
1
1
1
1
1
(continued )


249
  Appendix: The SAT Interactive Regression Learning Exercise 
SAT
GPA
APMATH
APENG
AP
ESL
GEND
PREP
RACE
930
2.73
0
0
0
0
1
1
0
940
3.10
1
1
1
1
0
0
1
980
2.70
0
0
0
1
1
1
1
1280
3.73
1
1
1
0
1
1
0
700
1.64
0
0
0
1
0
1
1
1040
4.03
1
1
1
1
0
1
1
1070
3.24
0
1
1
0
1
1
0
900
3.42
0
0
0
0
1
1
0
1430
4.29
1
1
1
0
1
0
0
1290
3.33
0
0
0
0
1
0
0
1070
3.61
1
0
1
1
0
1
1
1100
3.58
1
1
1
0
0
1
0
1030
3.52
0
1
1
0
0
1
0
1070
2.94
0
0
0
0
1
1
0
1170
3.98
1
1
1
1
1
1
0
1300
3.89
1
1
1
0
1
0
0
1410
4.34
1
1
1
1
0
1
1
1160
3.43
1
1
1
0
1
1
0
1170
3.56
1
1
1
0
0
0
0
1280
4.11
1
1
1
0
0
1
0
1060
3.58
1
1
1
1
0
1
0
1250
3.47
1
1
1
0
1
1
0
1020
2.92
1
0
1
1
1
1
1
1000
4.05
0
1
1
1
0
0
1
1090
3.24
1
1
1
1
1
1
1
1430
4.38
1
1
1
1
0
0
1
860
2.62
1
0
1
1
0
0
1
1050
2.37
0
0
0
0
1
0
0
920
2.77
0
0
0
0
0
1
0
1100
2.54
0
0
0
0
1
1
0
1160
3.55
1
0
1
1
1
1
1
1360
2.98
0
1
1
1
0
1
0
970
3.64
1
1
1
0
0
1
0
Datafile = SAT8
Table 8.1  (continued)


250
Chapter 8  Multicollinearity
Table 8.2  Means, Standard Deviations, and Simple Correlation Coefficients 
for the SAT Interactive Regression Learning Exercise
All the equations include SAT as the dependent variable and GPA, 
APMATH, and APENG as explanatory variables. Find the combination of 
explanatory variables (from ESL, GEND, PREP, and RACE) that you wish to 
include and go to the indicated regression:
None of them, go to regression run 8.1
ESL only, go to regression run 8.2
GEND only, go to regression run 8.3
PREP only, go to regression run 8.4
RACE only, go to regression run 8.5
ESL and GEND, go to regression run 8.6


251
  Appendix: The SAT Interactive Regression Learning Exercise 
ESL and PREP, go to regression run 8.7
ESL and RACE, go to regression run 8.8
GEND and PREP, go to regression run 8.9
GEND and RACE, go to regression run 8.10
PREP and RACE, go to regression run 8.11
ESL, GEND, and PREP, go to regression run 8.12
ESL, GEND, and RACE, go to regression run 8.13
ESL, PREP, and RACE, go to regression run 8.14
GEND, PREP, and RACE, go to regression run 8.15
All four, go to regression run 8.16


252
Chapter 8  Multicollinearity
Answer each of the following questions for this regression run.
a.	 Evaluate this result with respect to its economic meaning, overall fit, 
and the signs and significance of the individual coefficients.
b.	 What econometric problems (out of omitted variables, irrelevant 
variables, or multicollinearity) does this regression have? Why? If 
you need feedback on your answer, see hint 2 in the material on this 
chapter in Appendix A.
c.	 Which of the following statements comes closest to your recommenda-
tion for further action to be taken in the estimation of this equation?
	
	
i.	 No further specification changes are advisable (go to page 272).
	
	
ii.	 I would like to add ESL to the equation (go to run 8.2).
	
	
iii.	 I would like to add GEND to the equation (go to run 8.3).
	
	
iv.	 I would like to add PREP to the equation (go to run 8.4).
	
	
v.	 I would like to add RACE to the equation (go to run 8.5).
If you need feedback on your answer, see hint 6 in the material on this 
chapter in Appendix A.


253
  Appendix: The SAT Interactive Regression Learning Exercise 
Answer each of the following questions for this regression run.
a.	 Evaluate this result with respect to its economic meaning, overall fit, 
and the signs and significance of the individual coefficients.
b.	 What econometric problems (out of omitted variables, irrelevant 
variables, or multicollinearity) does this regression have? Why? If 
you need feedback on your answer, see hint 3 in the material on this 
chapter in Appendix A.
c.	 Which of the following statements comes closest to your recommenda-
tion for further action to be taken in the estimation of this equation?
	
	
i.	 No further specification changes are advisable (go to page 272).
	
	
ii.	 I would like to drop ESL from the equation (go to run 8.1).
	
	
iii.	 I would like to add GEND to the equation (go to run 8.6).
	
	
iv.	 I would like to add RACE to the equation (go to run 8.8).
	
	
v.	 I would like to add PREP to the equation (go to run 8.7).
If you need feedback on your answer, see hint 6 in the material on this chap-
ter in Appendix A.


254
Chapter 8  Multicollinearity
Answer each of the following questions for this regression run.
a.	 Evaluate this result with respect to its economic meaning, overall fit, 
and the signs and significance of the individual coefficients.
b.	 What econometric problems (out of omitted variables, irrelevant 
variables, or multicollinearity) does this regression have? Why? If you 
need feedback on your answer, see hint 5 in the material on this chap-
ter in Appendix A.
c.	 Which of the following statements comes closest to your recommenda-
tion for further action to be taken in the estimation of this equation?
	
	
i.	 No further specification changes are advisable (go to page 272).
	
	
ii.	 I would like to add ESL to the equation (go to run 8.6).
	
	
iii.	 I would like to add PREP to the equation (go to run 8.9).
	
	
iv.	 I would like to add RACE to the equation (go to run 8.10).
If you need feedback on your answer, see hint 19 in the material on this 
chapter in Appendix A.


255
  Appendix: The SAT Interactive Regression Learning Exercise 
Answer each of the following questions for this regression run.
a.	 Evaluate this result with respect to its economic meaning, overall fit, 
and the signs and significance of the individual coefficients.
b.	 What econometric problems (out of omitted variables, irrelevant 
variables, or multicollinearity) does this regression have? Why? If you 
need feedback on your answer, see hint 8 in the material on this chap-
ter in Appendix A.
c.	 Which of the following statements comes closest to your recommenda-
tion for further action to be taken in the estimation of this equation?
	
	
i.	 No further specification changes are advisable (go to page 272).
	
	
ii.	 I would like to drop PREP from the equation (go to run 8.1).
	
	
iii.	 I would like to add ESL to the equation (go to run 8.7).
	
	
iv.	 I would like to add GEND to the equation (go to run 8.9).
	
	
v.	 I would like to replace APMATH and APENG with AP, a linear 
combination of the two variables (go to run 8.17).
If you need feedback on your answer, see hint 12 in the material on this 
chapter in Appendix A.


256
Chapter 8  Multicollinearity
Answer each of the following questions for this regression run.
a.	 Evaluate this result with respect to its economic meaning, overall fit, 
and the signs and significance of the individual coefficients.
b.	 What econometric problems (out of omitted variables, irrelevant 
variables, or multicollinearity) does this regression have? Why? If 
you need feedback on your answer, see hint 3 in the material on this 
chapter in Appendix A.
c.	 Which of the following statements comes closest to your recommenda-
tion for further action to be taken in the estimation of this equation?
	
	
i.	 No further specification changes are advisable (go to page 272).
	
	
ii.	 I would like to drop RACE from the equation (go to run 8.1).
	
	
iii.	 I would like to add ESL to the equation (go to run 8.8).
	
	
iv.	 I would like to add GEND to the equation (go to run 8.10).
	
	
v.	 I would like to add PREP to the equation (go to run 8.11).
If you need feedback on your answer, see hint 14 in the material on this 
chapter in Appendix A.


257
  Appendix: The SAT Interactive Regression Learning Exercise 
Answer each of the following questions for this regression run.
a.	 Evaluate this result with respect to its economic meaning, overall fit, 
and the signs and significance of the individual coefficients.
b.	 What econometric problems (out of omitted variables, irrelevant 
variables, or multicollinearity) does this regression have? Why? If 
you need feedback on your answer, see hint 7 in the material on this 
chapter in Appendix A.
c.	 Which of the following statements comes closest to your recommenda-
tion for further action to be taken in the estimation of this equation?
	
	
i.	 No further specification changes are advisable (go to page 272).
	
	
ii.	 I would like to drop ESL from the equation (go to run 8.3).
	
	
iii.	 I would like to add PREP to the equation (go to run 8.12).
	
	
iv.	 I would like to add RACE to the equation (go to run 8.13).
If you need feedback on your answer, see hint 4 in the material on this chap-
ter in Appendix A.


258
Chapter 8  Multicollinearity
Answer each of the following questions for this regression run.
a.	 Evaluate this result with respect to its economic meaning, overall fit, 
and the signs and significance of the individual coefficients.
b.	 What econometric problems (out of omitted variables, irrelevant 
variables, or multicollinearity) does this regression have? Why? If 
you need feedback on your answer, see hint 8 in the material on this 
chapter in Appendix A.
c.	 Which of the following statements comes closest to your recommenda-
tion for further action to be taken in the estimation of this equation?
	
	
i.	 No further specification changes are advisable (go to page 272).
	
	
ii.	 I would like to drop ESL from the equation (go to run 8.4).
	
	
iii.	 I would like to drop PREP from the equation (go to run 8.2).
	
	
iv.	 I would like to add GEND to the equation (go to run 8.12).
	
	
v.	 I would like to add RACE to the equation (go to run 8.14).
If you need feedback on your answer, see hint 18 in the material on this 
chapter in Appendix A.


259
  Appendix: The SAT Interactive Regression Learning Exercise 
Answer each of the following questions for this regression run.
a.	 Evaluate this result with respect to its economic meaning, overall fit, 
and the signs and significance of the individual coefficients.
b.	 What econometric problems (out of omitted variables, irrelevant 
variables, or multicollinearity) does this regression have? Why? If 
you need feedback on your answer, see hint 9 in the material on this 
chapter in Appendix A.
c.	 Which of the following statements comes closest to your recommenda-
tion for further action to be taken in the estimation of this equation?
	
	
i.	 No further specification changes are advisable (go to page 272).
	
	
ii.	 I would like to drop ESL from the equation (go to run 8.5).
	
	
iii.	 I would like to drop RACE from the equation (go to run 8.2).
	
	
iv.	 I would like to add GEND to the equation (go to run 8.13).
	
	
v.	 I would like to add PREP to the equation (go to run 8.14).
If you need feedback on your answer, see hint 15 in the material on this 
chapter in Appendix A.


260
Chapter 8  Multicollinearity
Answer each of the following questions for this regression run.
a.	 Evaluate this result with respect to its economic meaning, overall fit, 
and the signs and significance of the individual coefficients.
b.	 What econometric problems (out of omitted variables, irrelevant 
variables, or multicollinearity) does this regression have? Why? If 
you need feedback on your answer, see hint 8 in the material on this 
chapter in Appendix A.
c.	 Which of the following statements comes closest to your recommenda-
tion for further action to be taken in the estimation of this equation?
	
	
i.	 No further specification changes are advisable (go to page 272).
	
	
ii.	 I would like to drop PREP from the equation (go to run 8.3).
	
	
iii.	 I would like to add ESL to the equation (go to run 8.12).
	
	
iv.	 I would like to add RACE to the equation (go to run 8.15).
If you need feedback on your answer, see hint 17 in the material on this 
chapter in Appendix A.


261
  Appendix: The SAT Interactive Regression Learning Exercise 
Answer each of the following questions for this regression run.
a.	 Evaluate this result with respect to its economic meaning, overall fit, 
and the signs and significance of the individual coefficients.
b.	 What econometric problems (out of omitted variables, irrelevant 
variables, or multicollinearity) does this regression have? Why? If you 
need feedback on your answer, see hint 10 in the material on this 
chapter in Appendix A.
c.	 Which of the following statements comes closest to your recommenda-
tion for further action to be taken in the estimation of this equation?
	
	
i.	 No further specification changes are advisable (go to page 272).
	
	
ii.	 I would like to drop RACE from the equation (go to run 8.3).
	
	
iii.	 I would like to add ESL to the equation (go to run 8.13).
	
	
iv.	 I would like to add PREP to the equation (go to run 8.15).
If you need feedback on your answer, see hint 4 in the material on this chap-
ter in Appendix A.


262
Chapter 8  Multicollinearity
Answer each of the following questions for this regression run.
a.	 Evaluate this result with respect to its economic meaning, overall fit, 
and the signs and significance of the individual coefficients.
b.	 What econometric problems (out of omitted variables, irrelevant 
variables, or multicollinearity) does this regression have? Why? If 
you need feedback on your answer, see hint 8 in the material on this 
chapter in Appendix A.
c.	 Which of the following statements comes closest to your recommenda-
tion for further action to be taken in the estimation of this equation?
	
	
i.	 No further specification changes are advisable (go to page 272).
	
	
ii.	 I would like to drop PREP from the equation (go to run 8.5).
	
	
iii.	 I would like to drop RACE from the equation (go to run 8.4).
	
	
iv.	 I would like to add GEND to the equation (go to run 8.15).
	
	
v.	 I would like to replace APMATH and APENG with AP, a linear 
combination of the two variables (go to run 8.18).
If you need feedback on your answer, see hint 18 in the material on this 
chapter in Appendix A.


263
  Appendix: The SAT Interactive Regression Learning Exercise 
Answer each of the following questions for this regression run.
a.	 Evaluate this result with respect to its economic meaning, overall fit, 
and the signs and significance of the individual coefficients.
b.	 What econometric problems (out of omitted variables, irrelevant 
variables, or multicollinearity) does this regression have? Why? If 
you need feedback on your answer, see hint 8 in the material on this 
chapter in Appendix A.
c.	 Which of the following statements comes closest to your recommenda-
tion for further action to be taken in the estimation of this equation?
	
	
i.	 No further specification changes are advisable (go to page 272).
	
	
ii.	 I would like to drop ESL from the equation (go to run 8.9).
	
	
iii.	 I would like to drop PREP from the equation (go to run 8.6).
	
	
iv.	 I would like to add RACE to the equation (go to run 8.16).
If you need feedback on your answer, see hint 17 in the material on this 
chapter in Appendix A.


264
Chapter 8  Multicollinearity
Answer each of the following questions for this regression run.
a.	 Evaluate this result with respect to its economic meaning, overall fit, 
and the signs and significance of the individual coefficients.
b.	 What econometric problems (out of omitted variables, irrelevant 
variables, or multicollinearity) does this regression have? Why? If 
you need feedback on your answer, see hint 9 in the material on this 
chapter in Appendix A.
c.	 Which of the following statements comes closest to your recommenda-
tion for further action to be taken in the estimation of this equation?
	
	
i.	 No further specification changes are advisable (go to page 272).
	
	
ii.	 I would like to drop ESL from the equation (go to run 8.10).
	
	
iii.	 I would like to drop RACE from the equation (go to run 8.6).
	
	
iv.	 I would like to add PREP to the equation (go to run 8.16).
If you need feedback on your answer, see hint 15 in the material on this 
chapter in Appendix A.


265
  Appendix: The SAT Interactive Regression Learning Exercise 
Answer each of the following questions for this regression run.
a.	 Evaluate this result with respect to its economic meaning, overall fit, 
and the signs and significance of the individual coefficients.
b.	 What econometric problems (out of omitted variables, irrelevant 
variables, or multicollinearity) does this regression have? Why? If 
you need feedback on your answer, see hint 9 in the material on this 
chapter in Appendix A.
c.	 Which of the following statements comes closest to your recommenda-
tion for further action to be taken in the estimation of this equation?
	
	
i.	 No further specification changes are advisable (go to page 272).
	
	
ii.	 I would like to drop ESL from the equation (go to run 8.11).
	
	
iii.	 I would like to drop PREP from the equation (go to run 8.8).
	
	
iv.	 I would like to add GEND to the equation (go to run 8.16).
	
	
v.	 I would like to replace APMATH and APENG with AP, a linear 
combination of the two variables (go to run 8.19).
If you need feedback on your answer, see hint 15 in the material on this 
chapter in Appendix A.


266
Chapter 8  Multicollinearity
Answer each of the following questions for this regression run.
a.	 Evaluate this result with respect to its economic meaning, overall fit, 
and the signs and significance of the individual coefficients.
b.	 What econometric problems (out of omitted variables, irrelevant 
variables, or multicollinearity) does this regression have? Why? If 
you need feedback on your answer, see hint 8 in the material on this 
chapter in Appendix A.
c.	 Which of the following statements comes closest to your recommenda-
tion for further action to be taken in the estimation of this equation?
	
	
i.	 No further specification changes are advisable (go to page 272).
	
	
ii.	 I would like to drop PREP from the equation (go to run 8.10).
	
	
iii.	 I would like to drop RACE from the equation (go to run 8.9).
	
	
iv.	 I would like to add ESL to the equation (go to run 8.16).
If you need feedback on your answer, see hint 17 in the material on this 
chapter in Appendix A.


267
  Appendix: The SAT Interactive Regression Learning Exercise 
Answer each of the following questions for this regression run.
a.	 Evaluate this result with respect to its economic meaning, overall fit, 
and the signs and significance of the individual coefficients.
b.	 What econometric problems (out of omitted variables, irrelevant 
variables, or multicollinearity) does this regression have? Why? If 
you need feedback on your answer, see hint 9 in the material on this 
chapter in Appendix A.
c.	 Which of the following statements comes closest to your recommenda-
tion for further action to be taken in the estimation of this equation?
	
	
i.	 No further specification changes are advisable (go to page 272).
	
	
ii.	 I would like to drop ESL from the equation (go to run 8.15).
	
	
iii.	 I would like to drop PREP from the equation (go to run 8.13).
	
	
iv.	 I would like to drop RACE from the equation (go to run 8.12).
If you need feedback on your answer, see hint 15 in the material on this 
chapter in Appendix A.


268
Chapter 8  Multicollinearity
Answer each of the following questions for this regression run.
a.	 Evaluate this result with respect to its economic meaning, overall fit, 
and the signs and significance of the individual coefficients.
b.	 What econometric problems (out of omitted variables, irrelevant 
variables, or multicollinearity) does this regression have? Why? If you 
need feedback on your answer, see hint 11 in the material on this 
chapter in Appendix A.
c.	 Which of the following statements comes closest to your recommenda-
tion for further action to be taken in the estimation of this equation?
	
	
i.	 No further specification changes are advisable (go to page 272).
	
	
ii.	 I would like to drop PREP from the equation (go to run 8.20).
	
	
iii.	 I would like to add RACE to the equation (go to run 8.18).
	
	
iv.	 I would like to replace the AP combination variable with APMATH 
and APENG (go to run 8.4).
If you need feedback on your answer, see hint 16 in the material on this 
chapter in Appendix A.


269
  Appendix: The SAT Interactive Regression Learning Exercise 
Answer each of the following questions for this regression run.
a.	 Evaluate this result with respect to its economic meaning, overall fit, 
and the signs and significance of the individual coefficients.
b.	 What econometric problems (out of omitted variables, irrelevant 
variables, or multicollinearity) does this regression have? Why? If you 
need feedback on your answer, see hint 11 in the material on this 
chapter in Appendix A.
c.	 Which of the following statements comes closest to your recommenda-
tion for further action to be taken in the estimation of this equation?
	
	
i.	 No further specification changes are advisable (go to page 272).
	
	
ii.	 I would like to drop RACE from the equation (go to run 8.17).
	
	
iii.	 I would like to add ESL to the equation (go to run 8.19).
	
	
iv.	 I would like to replace the AP combination variable with APMATH 
and APENG (go to run 8.11).
If you need feedback on your answer, see hint 16 in the material on this 
chapter in Appendix A.


270
Chapter 8  Multicollinearity
Answer each of the following questions for this regression run.
a.	 Evaluate this result with respect to its economic meaning, overall fit, 
and the signs and significance of the individual coefficients.
b.	 What econometric problems (out of omitted variables, irrelevant 
variables, or multicollinearity) does this regression have? Why? If you 
need feedback on your answer, see hint 11 in the material on this 
chapter in Appendix A.
c.	 Which of the following statements comes closest to your recommenda-
tion for further action to be taken in the estimation of this equation?
	
	
i.	 No further specification changes are advisable (go to page 272).
	
	
ii.	 I would like to drop ESL from the equation (go to run 8.18).
	
	
iii.	 I would like to replace the AP combination variable with APMATH 
and APENG (go to run 8.14).
If you need feedback on your answer, see hint 16 in the material on this 
chapter in Appendix A.


271
  Appendix: The SAT Interactive Regression Learning Exercise 
Answer each of the following questions for this regression run.
a.	 Evaluate this result with respect to its economic meaning, overall fit, 
and the signs and significance of the individual coefficients.
b.	 What econometric problems (out of omitted variables, irrelevant 
variables, or multicollinearity) does this regression have? Why? If you 
need feedback on your answer, see hint 13 in the material on this 
chapter in Appendix A.
c.	 Which of the following statements comes closest to your recommenda-
tion for further action to be taken in the estimation of this equation?
	
	
i.	 No further specification changes are advisable (go to page 272).
	
	
ii.	 I would like to add PREP to the equation (go to run 8.17).
	
	
iii.	 I would like to replace the AP combination variable with APMATH 
and APENG (go to run 8.1).
If you need feedback on your answer, see hint 13 in the material on this 
chapter in Appendix A.


272
Chapter 8  Multicollinearity
Evaluating the Results from Your Interactive Exercise
Congratulations! If you’ve reached this section, you must have found a speci-
fication that met your theoretical and econometric goals. Which one did you 
pick? Our experience is that most beginning econometricians end up with 
either regression run 8.3, 8.6, or 8.10, but only after looking at three or more 
regression results (or a hint or two) before settling on that choice.
In contrast, we’ve found that most experienced econometricians gravitate 
to regression run 8.6, usually after inspecting, at most, one other specifica-
tion. What lessons can we learn from this difference?
1.	 Learn that a variable isn’t irrelevant simply because its t-score is low. In our 
opinion, ESL belongs in the equation for strong theoretical reasons, 
and a slightly insignificant t-score in the expected direction isn’t 
enough evidence to get us to rethink the underlying theory.
2.	 Learn to spot redundant (multicollinear) variables. ESL and RACE 
wouldn’t normally be redundant, but in this high school, with its par-
ticular ethnic diversity, they are. Once one is included in the equation, 
the other shouldn’t even be considered.
3.	 Learn to spot false variables. At first glance, PREP is a tempting vari-
able to include because prep courses almost surely improve the SAT 
scores of the students who choose to take them. The problem is that 
a student’s decision to take a prep course isn’t independent of his or 
her previous SAT scores (or expected scores). We trust the judgment of 
students who feel a need for a prep course, and we think that all the 
course will do is bring them up to the level of their peers who didn’t 
feel they needed a course. As a result, we wouldn’t expect a significant 
effect in either direction.
If you enjoyed and learned from this interactive regression learning exercise, 
you’ll be interested to know that there is another in Chapter 11. Good luck!
