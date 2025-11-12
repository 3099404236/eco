# Chapter 6: Specification: Choosing the Independent  Variables

**Pages:** 177-208

---

157
Chapter 6
Specification: Choosing  
the Independent Variables
6.1  Omitted Variables
6.2  Irrelevant Variables
6.3  An Illustration of the Misuse of Specification Criteria
6.4  Specification Searches
6.5  An Example of Choosing Independent Variables
6.6  Summary and Exercises
6.7  Appendix: Additional Specification Criteria
Before any equation can be estimated, it must be specified. Specifying an 
econometric equation consists of three parts: choosing the correct indepen-
dent variables, the correct functional form, and the correct form of the 
stochastic error term.
A specification error results when any one of these choices is made 
incorrectly. This chapter is concerned with only the first of these, choosing 
the variables; the second and third choices will be taken up in later chapters.
The fact that researchers can decide which independent variables to 
include in regression equations is a source of both strength and weakness 
in econometrics. The strength is that the equations can be formulated to fit 
individual needs, but the weakness is that researchers can estimate many 
different specifications until they find the one that “proves” their point, 
even if many other results disprove it. A major goal of this chapter is to 
help you understand how to choose variables for your regressions with-
out falling prey to the various errors that result from misusing the ability 
to choose.
The primary consideration in deciding whether an independent variable 
belongs in an equation is whether the variable is essential to the regression 
on the basis of theory. If the answer is an unambiguous yes, then the vari-
able definitely should be included in the equation, even if it seems to be 


158
Chapter 6  Specification: Choosing the Independent Variables 
lacking in statistical significance. If theory is ambivalent or less emphatic, 
a dilemma arises. Leaving a relevant variable out of an equation is likely 
to bias the remaining estimates, but including an irrelevant variable leads 
to higher variances of the estimated coefficients. Although we’ll develop 
statistical tools to help us deal with this decision, it’s difficult in practice 
to be sure that a variable is relevant, and so the problem often remains 
unresolved.
We devote the fourth section of the chapter to specification searches and 
the pros and cons of various approaches to such searches. For example, 
poorly done specification searches often cause bias or make the usual tests of 
significance inapplicable. Instead, we suggest trying to minimize the number 
of regressions estimated and relying as much as possible on theory rather 
than statistical fit when choosing variables. There are no pat answers, how-
ever, and so the final decisions must be left to each individual researcher.
6.1   Omitted Variables
Suppose that you forget to include one of the relevant independent variables 
when you first specify an equation (after all, no one’s perfect!). Or suppose 
that you can’t get data for one of the variables that you do think of. The result 
in both these situations is an omitted variable, defined as an important 
explanatory variable that has been left out of a regression equation.
Whenever you have an omitted (or left-out) variable, the interpretation and 
use of your estimated equation become suspect. Leaving out a relevant vari-
able, like price from a demand equation, not only prevents you from getting 
an estimate of the coefficient of price but also usually causes bias in the esti-
mated coefficients of the variables that are in the equation.
The bias caused by leaving a variable out of an equation is called omitted 
variable bias. In an equation with more than one independent variable, the 
coefficient βk represents the change in the dependent variable Y caused by a 
one-unit increase in the independent variable Xk, holding constant the other 
independent variables in the equation. If a variable is omitted, then it is not 
included as an independent variable, and it is not held constant for the calcu-
lation and interpretation of βN k. This omission can cause bias: It can force the 
expected value of the estimated coefficient away from the true value of the 
population coefficient.
Thus, omitting a relevant variable is usually evidence that the entire 
estimated equation is suspect, because of the likely bias in the coefficients 
of the variables that remain in the equation. Let’s look at this issue in 
more detail.


159
  Omitted Variables
The Consequences of an Omitted Variable
What happens if you omit an important variable from your equation (per-
haps because you can’t get the data for the variable or didn’t even think of 
the variable in the first place)? The major consequence of omitting a relevant 
independent variable from an equation is to cause bias in the regression coef-
ficients that remain in the equation. Suppose that the true regression model is:
	
Yi = β0 + β1X1i + β2X2i + ei	
(6.1)
where ei is a classical error term. If you omit X2 from the equation, then the 
equation becomes:
	
Yi = β0* + β1*X1i + ei*	
(6.2)
where ei* equals:
	
ei* = ei + β2X2i	
(6.3)
because the stochastic error term includes the effects of any omitted vari-
ables, as mentioned in Section 1.2. Why does Equation 6.2 include β0* and 
β1* instead of β0 and β1? The answer lies in the meaning of a regression coef-
ficient. β1 is the impact of a one-unit increase in X1 on Y, holding X2 constant, 
but X2 isn’t in Equation 6.2, so OLS can’t hold it constant. As a result, β1* is 
the impact of a one-unit increase in X1 on Y, not holding X2 constant.
From Equations 6.2 and 6.3, it might seem as though we could get unbi-
ased estimates even if we left X2 out of the equation. Unfortunately, this is 
not the case,1 because the included coefficients almost surely pick up some of 
the effect of the omitted variable and therefore will change, causing bias. To 
see why, take another look at Equations 6.2 and 6.3. Most pairs of variables 
are correlated to some degree, so X1 and X2 almost surely are correlated. 
When X2 is omitted from the equation, the impact of X2 goes into e*, so e* 
and X2 are correlated. Thus if X2 is omitted from the equation and X1 and X2 
are correlated, both X1 and e* will change when X2 changes, and the error 
term will no longer be independent of the explanatory variable. That violates 
Classical Assumption III!
In other words, if we leave an important variable out of an equation, we 
violate Classical Assumption III (that the explanatory variables are indepen-
dent of the error term), unless the omitted variable is uncorrelated with all 
the included independent variables (which is extremely unlikely). In general, 
1. To avoid bias, X1 and X2 must be perfectly uncorrelated in the sample—an extremely unlikely 
result.


160
Chapter 6  Specification: Choosing the Independent Variables 
when there is a violation of one of the Classical Assumptions, the Gauss–
Markov Theorem does not hold, and the OLS estimates are not BLUE. Given 
linear estimators, this means that the estimated coefficients are no longer 
unbiased or are no longer minimum variance (for all linear unbiased estima-
tors), or both. In such a circumstance, econometricians first determine the 
exact property (unbiasedness or minimum variance) that no longer holds 
and then suggest an alternative estimation technique that might be better 
than OLS.
An omitted variable causes Classical Assumption III to be violated in a way 
that causes bias. Estimating Equation 6.2 when Equation 6.1 is the truth will 
cause bias. This means that:
	
E1βN 1*2 ≠β1	
(6.4)
Instead of having an expected value equal to the true β1, the estimate will 
compensate for the fact that X2 is missing from the equation. If X1 and X2 
are correlated and X2 is omitted from the equation, then the OLS estimation 
procedure will attribute to X1 variations in Y that are actually caused by X2, 
and a biased estimate of β1 will result.
To see how an omitted variable can cause bias, let’s look at an extremely 
early application of regression analysis.2 During World War II, the Allies were 
interested in improving the accuracy of their bombers, so they estimated 
an equation where the dependent variable was bomber accuracy and the 
independent variables included such things as the speed and altitude of the 
bombing group and the amount of enemy fighter opposition. As expected, 
the estimated coefficients supported the hypotheses that higher speeds and 
higher altitudes led to larger aiming errors, but the researchers were shocked 
to discover that more enemy fighter opposition appeared to improve the 
accuracy of the pilot and bombardier! What was going on?
The answer is omitted variable bias. It turns out that the equation didn’t 
include a variable for cloud cover over the target, and cloud cover typically 
prevented enemy fighters from flying. When it was cloudy, the bombers 
couldn’t see the ground and made large errors, but OLS attributed these 
errors to the lack of enemy fighter opposition because there was no variable 
for cloud cover in the equation and because few fighters could fly when it 
was cloudy. Put differently, the coefficient of enemy fighters picked up the 
impact of the omitted variable of cloud cover because the two variables were 
highly correlated. This is omitted variable bias!
2. Adapted from Frederick Mosteller and John Tukey, Data Analysis and Regression: A Second 
Course in Statistics (Reading, MA: Addison-Wesley, 1977), p. 318.


161
  Omitted Variables
To generalize for a model with two independent variables, the expected 
value of the coefficient of an included variable 1X12 when a relevant vari-
able 1X22 is omitted from the equation equals:
	
E1βN 1*2 = β1 + β2 # αN 1	
(6.5)
where αN 1 is an estimate of the slope coefficient of the secondary regression 
that relates X2 to X1:
	
XN 2i = αN 0 + αN 1X1i	
(6.6)
If X1 and X2 are positively correlated, αN 1 will be positive. If X1 and X2 are 
negatively correlated, αN 1 will be negative. If X1 and X2 are uncorrelated, αN 1 
will be zero.
Let’s take a look at Equation 6.5. It states that the expected value of the 
included variable’s coefficient is equal to its true value plus the omitted 
variable’s true coefficient times a function of the correlation between the 
included and omitted variables.3 Since the expected value of an unbiased 
estimate equals the true value, the right-hand term in Equation 6.5 measures 
the omitted variable bias in the equation:
3. Equations 6.5 and 6.7 hold when there are exactly two independent variables, but the more 
general equations are quite similar.
	
Bias = β2αN 1	
(6.7)
In general terms, the bias thus equals the coefficient of the omitted variable 
times a function of the correlation between the included and omitted variables.
This bias exists unless:
1.	 the true coefficient equals zero, or
2.	 the included and omitted variables are uncorrelated in the sample.
The term β2αN 1 is the amount of expected bias introduced into the esti-
mate of the coefficient of the included variable by leaving out the omitted 
variable. Although it’s true that there is no bias if the included and excluded 
variables are uncorrelated, there almost always is some correlation between 
any two variables in the real world, and so bias is almost always caused by the 
omission of a relevant variable.


162
Chapter 6  Specification: Choosing the Independent Variables 
An Example of Omitted Variable Bias
For an example of omitted variable bias, let’s go back to Equation 5.4, the 
Woody’s restaurants model that we first studied in Section 3.2:
	
YNi = 102,192 - 9075Ni + 0.3547Pi + 1.288Ii	
(5.4)
120532    10.07272   10.5432
t = -4.42     4.88      2.37
N = 33    R  2 = .579
where Y = customers (check volume), N = the number of competitive res-
taurants nearby, P = the population nearby, and I = the average household 
income nearby.
Let’s take a look at what happens if we drop population (P) from the 
equation:
	
Yi = 84,439 - 1487Ni + 2.322Ii	
(6.8)
117782 
10.6642
t =   
 -  0.84   
+3.50
N = 33 
 
   R  2 = .258
Stop for a minute and compare Equations 5.4 and 6.8. The most noticeable 
difference is that R  2 has fallen from .579 to .258 because we’ve omitted 
population. However, check out the estimated coefficient and t-score for 
competition (N). The coefficient has changed from -9075 to -1487, and the 
t-score has changed from -4.42 to -0.84. What a disaster! The coefficient of 
N now is insignificantly different from zero! How could this have happened?
The answer is omitted variable bias. Population and competition are 
understandably quite correlated; the more people there are in an area, 
the more restaurants you’d expect to find. As a result, when population is 
dropped from the equation, OLS attributes the impact of the omitted vari-
able to the included variables to the extent that they’re correlated with the 
omitted variable. Was this positive or negative bias? Well, βN N increased from 
a large negative number to a smaller negative number, so the bias is posi-
tive. The positive impact of population almost completely offset the negative 
impact of competition, resulting in a coefficient not far from zero.
Note that we could have predicted that the bias was going to be positive by 
using our expected bias equation,4 Equation 6.7. Because the expected sign of 
4. It is important to note the distinction between expected bias and any actual observed dif-
ferences between coefficient estimates. Because of the random nature of the error term (and 
hence the βN s), the change in an estimated coefficient brought about by dropping a relevant 
variable from the equation will not necessarily be in the expected direction. Biasedness refers 
to the central tendency of the sampling distribution of the βNs, not to every single drawing from 
that distribution. However, we usually (and justifiably) rely on these general tendencies.


163
  Omitted Variables
βP is positive and because we’d expect αN 1 (related to the correlation between 
population and competition) to be positive, the expected bias in βN N is positive:
	
Expected bias in βN N = βP # αN 1 = 1 + 21 + 2 = +	
(6.9)
Just as we would have predicted, omitting N caused positive bias. Leaving pop-
ulation out of the equation caused the coefficient of competition to pick up 
the impact of population to the extent that the two variables were correlated.
To sum, if a relevant variable is left out of a regression equation,
1.	 there is no longer an estimate of the coefficient of that variable in the 
equation, and
2.	 the coefficients of the remaining variables are likely to be biased.
Although the amount of the bias might not be very large in some cases 
(when, for instance, there is little correlation between the included and 
excluded variables), it is extremely likely that at least a small amount of omit-
ted variable bias will be present in all such situations.
Correcting for an Omitted Variable
In theory, the solution to a problem of omitted variable bias seems easy: Add 
the omitted variable to the equation! Unfortunately, that’s easier said than 
done, for a couple of reasons.
First, omitted variable bias is hard to detect. The amount of bias intro-
duced can be small and not immediately detectable. This is especially true 
when there is no reason to believe that you have misspecified the model. 
Some indications of specification bias are obvious (such as an estimated 
coefficient that is significant in the direction opposite from that expected), 
but others are not so clear. The best indicators of an omitted relevant variable 
are the theoretical underpinnings of the model itself. What variables must 
be included? What signs do you expect? Do you have any notions about the 
range into which the coefficient values should fall? The best way to avoid 
omitting an important variable is to invest the time in thinking carefully 
through the equation before the data are entered into the computer.
A second source of complexity is the problem of choosing which vari-
able to add to an equation once you decide that it is suffering from omitted 
variable bias. Some beginning researchers, when faced with this dilemma, 
will add all the possible relevant variables to the equation at once, but this 
process leads to less precise estimates, as will be discussed in the next section. 
Other beginning researchers will test a number of different variables and 
keep the one in the equation that does the best statistical job of appearing 


164
Chapter 6  Specification: Choosing the Independent Variables 
to reduce the bias (by giving plausible signs and satisfactory t-values). This 
technique, adding a “left-out” variable to “fix” a strange-looking regression 
result, is invalid because the variable that best corrects a case of specification 
bias might do so only by chance rather than by being the true solution to the 
problem. In such an instance, the “fixed” equation may give superb statisti-
cal results for the sample at hand but then do terribly when applied to other 
samples because it does not describe the characteristics of the true population.
Dropping a variable will not help cure omitted variable bias. If the sign 
of an estimated coefficient is different from expected, it cannot be changed 
to the expected direction by dropping a variable that has a t-score lower (in 
absolute value) than the t-score of the coefficient estimate that has the unex-
pected sign. Furthermore, the sign in general will not likely change even if the 
variable to be deleted has a large t-score.5
If an unexpected result leads you to believe that you have an omitted 
variable, one way to decide which variable to add to the equation is to use 
expected bias analysis. If the sign of the expected bias (using Equation 6.7) 
is the same as the sign of your unexpected result, then the variable might 
be the source of the apparent bias. If the sign of the expected bias is not 
the same as the sign of your unexpected result, however, then the variable 
is extremely unlikely to have caused your unexpected result. Expected bias 
analysis should be used only when you’re choosing between theoretically 
sound potential variables.
Although you can never actually observe bias (since you don’t know the 
true β), the use of this technique to screen potential causes of specification 
bias should reduce the number of regressions run and increase the validity of 
the results.
A brief warning: It may be tempting to conduct what might be called 
“residual analysis” by examining a plot of the residuals in an attempt to find 
patterns that suggest variables that have been accidentally omitted. A major 
problem with this approach is that the coefficients of the estimated equation 
will possibly have some of the effects of the left-out variable already altering 
their estimated values. Thus, residuals may show a pattern that only vaguely 
resembles the pattern of the actual omitted variable. The chances are high 
that the pattern shown in the residuals may lead to the selection of an incor-
rect variable. In addition, care should be taken to use residual analysis only 
to choose between theoretically sound candidate variables rather than to 
generate those candidates.
5. Ignazio Visco, “On Obtaining the Right Sign of a Coefficient Estimate by Omitting a Variable 
from the Regression,” Journal of Econometrics, Vol. 7, No. 1, pp. 115–117.


165
  Irrelevant Variables
6.2   Irrelevant Variables
What happens if you include a variable in an equation that doesn’t belong 
there? This case, irrelevant variables, is the converse of omitted variables and 
can be analyzed using the model we developed in Section 6.1. The addition of a 
variable to an equation where it doesn’t belong does not cause bias, but it does 
increase the variances of the estimated coefficients of the included variables.
Impact of Irrelevant Variables
If the true regression specification is:
	
Yi = β0 + β1X1i + ei	
(6.10)
but the researcher for some reason includes an extra variable,
	
Yi = β0 + β1X1i + β2X2i + ei**	
(6.11)
the misspecified equation’s error term can be seen to be:
	
ei** = ei - β2X2i	
(6.12)
Such a mistake won’t cause bias if the true coefficient of the irrelevant variable 
is zero. That is, an estimate of β1 in Equation 6.11 is unbiased when β2 = 0.
However, the inclusion of an irrelevant variable will increase the variance 
of the estimated coefficients, and this increased variance will tend to decrease 
the absolute magnitude of their t-scores. Also, an irrelevant variable usually 
will decrease the R  2 (but not the R2).
Thus, although the irrelevant variable causes no bias, it causes problems 
for the regression because it reduces the t-scores and R  2.
An Example of an Irrelevant Variable
Let’s return to the Woody’s equation and see what happens when we add an 
irrelevant variable to the model. The original equation was:
	
YNi = 102,192 - 9075Ni + 0.3547Pi + 1.288Ii	
(5.4)
120532    10.07272   10.5432
t = -4.42     4.88      2.37
N = 33    R  2 = .579
where Y = customers (check volume), N = the number of competitive res-
taurants nearby, P = the population nearby, and I = the average household 
income nearby.


166
Chapter 6  Specification: Choosing the Independent Variables 
What’s the most irrelevant variable that you can think of? How about 
Ai = the last three digits of the street address of the ith Woody’s restaurant? 
That’s pretty random! If we add Ai to Equation 5.4, we get:
	
YNi = 98,125 - 8975Ni + 0.360Pi + 1.301Ii + 58.07Ai	
(6.13)
120822    10.0742   10.5502  195.212
t =      - 4.31   + 4.86  
+ 2.37    + 0.61
N = 33        R  2 = .569
A comparison of Equations 5.4 and 6.13 will make the theory in Section 6.2 
come to life. First of all, R  2 has fallen slightly, indicating the reduction in fit 
adjusted for degrees of freedom. Second, none of the regression coefficients 
from the original equation changed very much; compare these results with the 
larger differences between Equations 5.4 and 6.9. Further, the standard errors 
of the estimated coefficients increased. Finally, the t-score for the potential 
variable (A) is small, indicating that it is not significantly different from zero. 
Given the theoretical shakiness of the new variable, these results indicate that 
it is irrelevant and never should have been included in the regression.
Four Important Specification Criteria
We have now discussed at least four valid criteria to help decide whether a 
given variable belongs in the equation. We think these criteria are so impor-
tant that we urge beginning researchers to work through them every time a 
variable is added or subtracted.
	1.	 Theory: Is the variable’s place in the equation unambiguous and 
theoretically sound?
	2.	 t-Test: Is the variable’s estimated coefficient significant in the  
expected direction?
	3.	 R  2: Does the overall fit of the equation (adjusted for degrees of  
freedom) improve when the variable is added to the equation?
	4.	 Bias: Do other variables’ coefficients change significantly when the 
variable is added to the equation? 
If all these conditions hold, the variable belongs in the equation; if none of 
them do, the variable is irrelevant and can be safely excluded from the equa-
tion. When a typical omitted relevant variable is included in the equation, its 
inclusion probably will increase R  2 and change at least one other coefficient. 


167
  An Illustration of the Misuse of Specification Criteria
If an irrelevant variable, on the other hand, is included, it will reduce R  2, have 
an insignificant t-score, and have little impact on the other variables’ coefficients.
In many cases, all four criteria do not agree. It is possible for a variable to 
have an insignificant t-score that is greater than one, for example. In such a 
case, it can be shown that R  2 will go up when the variable is added to the 
equation and yet the t-score still will be insignificant.
Whenever our four specification criteria disagree, the econometrician must 
use careful judgment and should not rely on a single criterion like R  2 to deter-
mine the specification. Researchers should not misuse this freedom by testing 
various combinations of variables until they find the results that appear to sta-
tistically support the point they want to make. All such decisions are a bit easier 
when you realize that the single most important determinant of a variable’s rel-
evance is its theoretical justification. No amount of statistical evidence should 
make a theoretical necessity into an “irrelevant” variable. Once in a while, a 
researcher is forced to leave a theoretically important variable out of an equa-
tion for lack of data; in such cases, the usefulness of the equation is limited.
6.3   An Illustration of the Misuse of Specification Criteria
At times, the four specification criteria outlined in the previous section will 
lead the researcher to an incorrect conclusion if those criteria are applied to a 
problem without proper concern for economic principles or common sense. 
In particular, a t-score can often be insignificant for reasons other than the pres-
ence of an irrelevant variable. Since economic theory is the most important test 
for including a variable, an example of why a variable should not be dropped 
from an equation simply because it has an insignificant t-score is in order.
Suppose you believe that the demand for Brazilian coffee in the United 
States is a negative function of the real price of Brazilian coffee 1Pbc2 and a 
positive function of both the real price of tea 1Pt2 and real disposable income 
in the United States 1Yd2.6 Suppose further that you obtain the data, run the 
implied regression, and observe the following results:
	
COFFEE = 9.1 + 7.8Pbc + 2.4Pt + 0.0035Yd	
(6.14)
115.62     11.22   10.00102
t = 0.5     2.0       3.5
R  2 = .60    N = 25
®
6. This example was inspired by a similar one concerning Ceylonese tea published in Potluri 
Rao and Roger LeRoy Miller, Applied Econometrics (Belmont, CA: Wadsworth, 1971), pp. 38–40. 
This wonderful book is now out of print.


168
Chapter 6  Specification: Choosing the Independent Variables 
The coefficients of the second and third variables, Pt and Yd, appear to be 
fairly significant in the direction you hypothesized, but the first variable, Pbc, 
appears to have an insignificant coefficient with an unexpected sign. If you 
think there is a possibility that the demand for Brazilian coffee is price-inelastic 
(that is, its coefficient is zero), you might decide to run the same equation 
without the price variable, obtaining:
	
COFFEE = 9.3 + 2.6Pt + 0.0036Yd	
(6.15)
11.02   10.00092
t = 2.6     4.0
R  2 = .61   N = 25
By comparing Equations 6.14 and 6.15, we can apply our four specification 
criteria for the inclusion of a variable in an equation that were outlined in 
the previous section:
1.	 Theory: If it’s possible that the demand for coffee could be price-inelastic, 
the theory behind dropping the variable seems plausible.
2.	 t-Test: The t-score of the possibly irrelevant variable is 0.5, insignificant 
at any level.
3.	 R  2: R  2 increases when the variable is dropped, indicating that the  
variable is irrelevant.
4.	 Bias: The remaining coefficients change only a small amount when 
Pbc is dropped, suggesting that there is little—if any—bias caused by 
excluding the variable.
Based upon this analysis, you might conclude that the demand for Brazilian 
coffee is indeed price-inelastic and that the variable is therefore irrelevant 
and should be dropped from the model. As it turns out, this conclusion 
would be unwarranted. Although the elasticity of demand for coffee in gen-
eral might be fairly low (actually, the evidence suggests that it is inelastic only 
over a particular range of prices), it is hard to believe that Brazilian coffee is 
immune to price competition from other kinds of coffee. Indeed, one would 
expect quite a bit of sensitivity in the demand for Brazilian coffee with 
respect to the price of, for example, Colombian coffee. To test this hypoth-
esis, the price of Colombian coffee 1Pcc2 should be added to the original 
Equation 6.14:
	
COFFEE = 10.0 + 8.0Pcc - 5.6Pbc + 2.6Pt + 0.0030Yd	
(6.16)
14.02    12.02     11.32   10.00102
t = 2.0     - 2.8       2.0       3.0
R  2 = .65  N = 25
®
®


169
  Specification Searches
By comparing Equations 6.14 and 6.16, we can once again apply our four 
specification criteria:
1.	 Theory: Both prices should always have been included in the model; 
their logical justification is quite strong.
2.	 t-Test: The t-score of the new variable, the price of Colombian coffee, is 
2.0, significant at most levels.
3.	 R  2: R  2 increases with the addition of the variable, indicating that the 
variable was an omitted variable.
4.	 Bias: Although two of the coefficients remain virtually unchanged, 
indicating that the correlations between these variables and the price 
of Colombian coffee variable are low, the coefficient for the price of 
Brazilian coffee does change significantly, indicating bias in the  
original result.
The moral to be drawn is that theoretical considerations never should be 
discarded, even in the face of statistical insignificance. If a variable known to 
be extremely important from a theoretical point of view turns out to be statis-
tically insignificant in a particular sample, that variable should be left in the 
equation despite the fact that it makes the results look bad.
Don’t conclude that the particular path outlined in this example is the 
correct way to specify an equation. Trying a long string of possible variables 
until you get the particular one that makes the coefficient of Pbc turn nega-
tive and significant is not the way to obtain a result that will stand up well to 
other samples or alternative hypotheses. The original equation should never 
have been run without the Colombian coffee price variable. Instead, the 
problem should have been analyzed enough so that such errors of omission 
were unlikely before any regressions were attempted at all. The more thinking 
that’s done before the first regression is run, and the fewer alternative speci-
fications that are estimated, the better the regression results are likely to be.
6.4   Specification Searches
One of the weaknesses of econometrics is that a researcher potentially can 
manipulate a data set to produce almost any result by specifying different 
regressions until estimates with the desired properties are obtained. Because the 
integrity of all empirical work is thus open to question, the subject of how to 
search for the best specification is quite controversial among econometricians. 
Our goal in this section isn’t to summarize or settle this controversy; instead, 
we hope to provide some guidance and insight for beginning researchers.


170
Chapter 6  Specification: Choosing the Independent Variables 
Best Practices in Specification Searches
The issue of how best to choose a specification from among alternative pos-
sibilities is a difficult one, but our experience leads us to make the following 
recommendations:
	1.	 Rely on theory rather than statistical fit as much as possible when 
choosing variables, functional forms, and the like.
	2.	 Minimize the number of equations estimated (except for sensitivity 
analysis, to be discussed later in this section).
	3.	 Reveal, in a footnote or appendix, all alternative specifications  
estimated.
If theory, not R  2 or t-scores, is the most important criterion for the inclu-
sion of a variable in a regression equation, then it follows that most of the 
work of specifying a model should be done before you attempt to estimate 
the equation. Since it’s unreasonable to expect researchers to be perfect, there 
will be times when additional specifications must be estimated. However, 
these new estimates should be few in number and should be thoroughly 
grounded in theory. In addition, they should be explicitly taken into account 
when testing for significance and/or summarizing results. In this way, the 
danger of misleading the reader about the statistical properties of the final 
equation will be reduced.
Sequential Specification Searches
Most econometricians tend to specify equations by estimating an initial equa-
tion and then sequentially dropping or adding variables (or changing func-
tional forms) until a plausible equation is found with “good statistics.” Faced 
with knowing that a few variables are relevant (on the basis of theory) but 
not knowing whether other additional variables also are relevant, the gener-
ally accepted practice appears to be inspecting R  2 and t-tests for all variables 
for each specification. Indeed, casual reading of the previous section might 
make it seem as if such a sequential specification search is the best way to go 
about finding the “truth.” Instead, as we shall see, there is a vast difference 
between a sequential specification search and our recommended approach.
The sequential specification search technique allows a researcher to esti-
mate an undisclosed number of regressions and then present a final choice 


171
  Specification Searches
(which is based upon an unspecified set of expectations about the signs and 
significance of the coefficients) as if it were the only specification estimated. 
Such a method misstates the statistical validity of the regression results for 
two reasons:
1.	 The statistical significance of the results is overestimated because the 
estimations of the previous regressions are ignored.
2.	 The expectations used by the researcher to choose between various  
regression results rarely, if ever, are disclosed. Thus the reader has no 
way of knowing whether all the other regression results had opposite 
signs or insignificant coefficients for the important variables.
Unfortunately, there is no universally accepted way of conducting sequen-
tial searches, primarily because the appropriate test at one stage in the pro-
cedure depends on which tests previously were conducted, and also because 
the tests have been very difficult to invent.
Instead we recommend trying to keep the number of regressions estimated 
as low as possible; to focus on theoretical considerations when choosing 
variables or functional forms; and to document all the various specifications 
investigated. That is, we recommend combining parsimony (using theory 
and analysis to limit the number of specifications estimated) with disclosure 
(reporting all the equations estimated).
Not everyone agrees with our advice. Some researchers feel that the true 
model will show through if given the chance and that the best statistical 
results (including signs of coefficients, etc.) are most likely to have come 
from the true specification. In addition, reasonable people often disagree as 
to what the “true” model should look like. As a result, different researchers 
can look at the same data set and come up with very different “best” equa-
tions. Because this can happen, the distinction between good and bad econo-
metrics is not always as clear-cut as is implied by the previous paragraphs. As 
long as researchers have a healthy respect for the dangers inherent in specifi-
cation searches, they are very likely to proceed in a reasonable way.
Bias Caused by Relying on the t-Test or r  2 to Choose Variables
In the previous section, we stated that sequential specification searches are 
likely to mislead researchers about the statistical properties of their results. 
In particular, the practice of dropping a potential independent variable 
simply because its coefficient has a low t-score or because it lowers R  2 will 
cause systematic bias in the estimated coefficients (and their t-scores) of the 
remaining variables.


172
Chapter 6  Specification: Choosing the Independent Variables 
Let’s say the hypothesized model is:
	
Yi = β0 + β1X1i + β2X2i + ei	
(6.17)
Assume further that, on the basis of theory, we are certain that X1 belongs in 
the equation but that we are not as certain that X2 belongs. Many inexperi-
enced researchers use only the t-test on βN 2 to determine whether X2 should be 
included. If this preliminary t-test indicates that βN 2 is significantly different 
from zero, then these researchers leave X2 in the equation. If, however, the 
t-test does not indicate that βN 2 is significantly different from zero, then such 
researchers drop X2 from the equation and consider Y to be a function of X1.
Two kinds of mistakes can be made using such a system. First, X2 some-
times can be left in the equation when it does not belong there, but such a 
mistake does not change the expected value of βN 1.
Second, X2 sometimes can be dropped from the equation when it belongs. 
In this second case, the estimated coefficient of X1 will be biased. In other 
words, βN 1 will be biased every time X2 belongs in the equation and is left out, 
and X2 will be left out every time that its estimated coefficient is not signifi-
cantly different from zero. We will have systematic bias in our equation!
To summarize, the t-test is biased by sequential specification searches. 
Since most researchers consider a number of different variables before set-
tling on the final model, someone who relies on the t-test or R  2 is likely to 
encounter this problem systematically.
Data Mining
Data mining involves estimating a wide variety of alternative specifications 
before a “best” equation is chosen. Readers of this text will not be surprised to 
hear that we urge extreme caution when data mining. Improperly done data 
mining is worse than doing nothing at all.
Done properly, data mining involves exploring a data set not for the pur-
pose of testing hypotheses or finding a specification, but for the purpose of 
uncovering empirical regularities that can inform economic theory.7 After all, 
we can’t expect economic theorists to think of everything!
Be careful, however! If you develop a hypothesis using data mining tech-
niques, you must test that hypothesis on a different data set (or in a different 
context) than the one you used to develop the hypothesis. A new data set 
7. For an excellent presentation of this approach, see Lawrence H. Summers, “The Scientific 
Illusion in Empirical Macroeconomics,” Scandinavian Journal of Economics, Vol. 93, No. 2, 
pp. 129–148.


173
  Specification Searches
must be used because our typical statistical tests have little meaning if the 
new hypothesis is tested on the data set that was used to generate it. After all, 
the researcher already knows ahead of time what the results will be! The use 
of dual data sets is easiest when there is a plethora of data. This sometimes 
is the case in cross-sectional research projects but rarely is the case for time 
series research.
Data mining without using dual data sets is almost surely the worst way 
to choose a specification. In such a situation, a researcher could estimate 
virtually every possible combination of the various alternative independent 
variables, could choose the results that “look” the best, and then could report 
the “best” equation as if no data mining had been done. This improper use of 
data mining ignores the fact that a number of specifications have been exam-
ined before the final one is reported.
In addition, data mining will cause you to choose specifications that 
reflect the peculiarities of your particular data set. How does this happen? 
Suppose you have 100 true null hypotheses and you run 100 tests of these 
hypotheses. At the 5-percent level of significance, you’d expect to reject about 
five true null hypotheses and thus make about five Type I Errors. By look-
ing for high t-values, a data mining search procedure will find these Type I 
Errors and incorporate them into your specification. As a result, the reported 
t-scores will overstate the statistical significance of the estimated coefficients.
In essence, improper data mining to obtain desired statistics for the final 
regression equation is a potentially unethical empirical research method. 
Whether the improper data mining is accomplished by estimating one 
equation at a time or by estimating batches of equations or by techniques 
like stepwise regression procedures,8 the conclusion is the same. Hypotheses 
developed by data mining should always be tested on a data set different from 
the one that was used to develop the hypothesis. Otherwise, the researcher 
hasn’t found any scientific evidence to support the hypothesis; rather, a speci-
fication has been chosen in a way that is essentially misleading. As put by one 
econometrician, “if you torture the data long enough, they will confess.”9
8. A stepwise regression involves the use of an automated computer program to choose the 
independent variables in an equation. The researcher specifies a “shopping list” of possible 
independent variables, and then the computer estimates a number of equations until it finds 
the one that maximizes R  2. Such stepwise techniques are deficient in the face of multicollinearity 
(to be discussed in Chapter 8) and they run the risk that the chosen specification will have little 
theoretical justification and/or will have coefficients with unexpected signs. Because of these 
pitfalls, econometricians avoid stepwise procedures.
9. Thomas Mayer, “Economics as a Hard Science: Realistic Goal or Wishful Thinking?” Economic 
Inquiry, Vol. 18, No. 2, p. 175. (This quote also has been attributed to Ronald Coase.)


174
Chapter 6  Specification: Choosing the Independent Variables 
Sensitivity Analysis
Throughout this text, we’ve encouraged you to estimate as few specifications 
as possible and to avoid depending on fit alone to choose between those 
specifications. If you read the current economics literature, however, it won’t 
take you long to find well-known researchers who have estimated five or more 
specifications and then have listed all their results in an academic journal 
article. What’s going on?
In almost every case, these authors have employed a technique called 
sensitivity analysis. Sensitivity analysis consists of purposely running a 
number of alternative specifications to determine whether particular results 
are robust (not statistical flukes). In essence, we’re trying to determine how 
sensitive a potential “best” equation is to a change in specification because 
the true specification isn’t known. Researchers who use sensitivity analysis 
run (and report on) a number of different reasonable specifications and 
tend to discount a result that appears significant in some specifications and 
insignificant in others. Indeed, the whole purpose of sensitivity analysis is to 
gain confidence that a particular result is significant in a variety of alternative 
specifications, functional forms, variable definitions, and/or subsets of the 
data.
6.5   An Example of Choosing Independent Variables
It’s time to get some experience choosing independent variables. After all, 
every equation so far in the text has come with the specification already 
determined, but once you’ve finished this course you’ll have to make all such 
specification decisions on your own. In future chapters, we’ll use a technique 
called “interactive regression learning exercises” to allow you to make your 
own actual specification choices and get feedback on your choices. To start, 
though, let’s work through a specification together.
To keep things as simple as possible, we’ll begin with a topic near and dear 
to your heart—your GPA! Suppose a friend who attends a small liberal arts 
college surveys all 25 members of her econometrics class, obtains data on the 
variables listed here, and asks for your help in choosing a specification:
GPAi
 = the cumulative college grade point average of the ith student on a 
four-point scale
HGPAi = the cumulative high school grade point average of the ith student 
on a four-point scale
MSATi  = the highest score earned by the ith student on the math section of 
the SAT test (800 maximum)


175
  An Example of Choosing Independent Variables
VSATi
 = the highest score earned by the ith student on the verbal section 
of the SAT test (800 maximum)
SATi
 = MSATi + VSATi
GREKi  = a dummy variable equal to 1 if the ith student is a member of a 
fraternity or sorority, 0 otherwise
HRSi
 = the ith student’s estimate of the average number of hours spent 
studying per course per week in college
PRIVi
 = a dummy variable equal to 1 if the ith student graduated from a 
private high school, 0 otherwise
JOCKi  = a dummy variable equal to 1 if the ith student is or was a member 
of a varsity intercollegiate athletic team for at least one season,  
0 otherwise
lnEXi
 = the natural log of the number of full courses that the ith student 
has completed in college
Assuming that GPAi is the dependent variable, which independent vari-
ables would you choose? Before you answer, think through the possibilities 
carefully. What does the literature tell us on this subject? (Is there literature?) 
What are the expected signs of each of the coefficients? How strong is the 
theory behind each variable? Which variables seem obviously important? 
Which variables seem potentially irrelevant or redundant? Are there any 
other variables that you wish your friend had collected?
To get the most out of this example, you should take the time to write down 
the exact specification that you would run:
	
GPAi = f1?, ?, ?, ?, ?2 + e	
It’s hard for most beginning econometricians to avoid the temptation of 
including all of these variables in a GPA equation and then dropping any 
variables that have insignificant t-scores. Even though we mentioned in the 
previous section that such a specification search procedure will result in 
biased coefficient estimates, most beginners don’t trust their own judgment 
and tend to include too many variables. With this warning in mind, do you 
want to make any changes in your proposed specification?
No? OK, let’s compare notes. We believe that grades are a function of a 
student’s ability, how hard the student works, and the student’s experience 
taking college courses. Consequently, our specification would be:
	
+	
+	
+
	
GPAi = β0 + β1HGPAi + β2HRSi + β3lnEXi + ei
We can already hear you complaining! What about SATs, you say? Everyone 
knows they’re important. How about jocks and Greeks? Don’t they have lower 


176
Chapter 6  Specification: Choosing the Independent Variables 
GPAs? Don’t prep schools grade harder and prepare students better than 
public high schools?
Before we answer, it’s important to note that we think of specification 
choice as choosing which variables to include, not which variables to exclude. 
That is, we don’t assume automatically that a given variable should be 
included in an equation simply because we can’t think of a good reason for 
dropping it.
Given that, however, why did we choose the variables we did? First, we 
think that the best predictor of a student’s college GPA is his or her high 
school GPA. We have a hunch that once you know HGPA, SATs are redun-
dant, at least at a liberal arts college10 where there are few multiple choice 
tests. In addition, we’re concerned that possible racial and gender bias in the 
SAT test makes it a questionable measure of academic potential, but we rec-
ognize that we could be wrong on this issue.
As for the other variables, we’re more confident. For example, we feel 
that once we know how many hours a week a student spends studying, we 
couldn’t care less what that student does with the rest of his or her time, 
so JOCK and GREK are superfluous once HRS is included. In addition, the 
higher lnEX is, the better student study habits are and the more likely stu-
dents are to be taking courses in their major. Finally, while we recognize that 
some private schools are superb and that some public schools are not, we’d 
guess that PRIV is irrelevant; it probably has only a minor effect.
If we estimate this specification on the 25 students, we obtain:
	
GPAi = -0.26 + 0.49HGPAi + 0.06HRSi + 0.42lnEXi	
(6.18)
10.212     
10.022       10.142
t = 2.33           3.00       3.00
N = 25  R  2 = .585
Since we prefer this specification on theoretical grounds, since the overall fit 
seems reasonable, and since each coefficient meets our expectations in terms 
of sign, size, and significance, we consider this an acceptable equation. The 
only circumstance under which we’d consider estimating a second specifica-
tion would be if we had theoretical reasons to believe that we had omitted a 
h
10. In contrast, SATs tend to have a statistically significant effect on GPAs at large research 
universities. For example, see Andrew Barkley and Jerry Forst, “The Determinants of First-Year 
Academic Performance in the College of Agriculture at Kansas State University, 1990–1999,” 
Journal of Agricultural and Applied Economics, Vol. 36, No 2, pp. 437–448.


177
  Summary
relevant variable. The only variable that might meet this description is SATi 
(which we prefer to the individual MSAT and VSAT):
	
GPAi = -0.92 + 0.47HGPAi + 0.05HRSi	
(6.19)
10.222        10.022
t = 2.12         2.50
+ 0.44lnEXi   + 0.00060SATi
10.142     
10.000642
t = 3.12        0.93
N = 25  R  2 = .583
Let’s use our four specification criteria to compare Equations 6.18 and 6.19:
1.	 Theory: As discussed previously, the theoretical validity of SAT tests is 
a matter of some academic controversy, but they still are one of the 
most-cited measures of academic potential in this country.
2.	 t-Test: The coefficient of SAT is positive, as we’d expect, but it’s not  
significantly different from zero.
3.	 R  2: As you’d expect (since SAT’s t-score is under 1), R  2 falls slightly 
when SAT is added.
4.	 Bias: None of the estimated slope coefficients changes substantially 
when SAT is added, though some of the t-scores do change because of 
the increase in the SE1βN 2s caused by the addition of SAT.
Thus, the statistical criteria do not convincingly contradict our theoretical 
contention that SAT is irrelevant.
Finally, it’s important to recognize that different researchers could come 
up with different final equations on this topic. A researcher whose prior 
expectation was that SAT unambiguously belonged in the equation would 
have estimated Equation 6.19 and accepted that equation without bothering 
to estimate Equation 6.18. Other researchers, in the spirit of sensitivity analy-
sis, would report both equations.
6.6   Summary
	 1.	 The omission of a variable from an equation will cause bias in the 
estimates of the remaining coefficients to the extent that the omitted 
variable is correlated with included variables.
	 2.	 The bias to be expected from leaving a variable out of an equation 
equals the coefficient of the excluded variable times a function of the 
simple correlation coefficient between the excluded variable and the 
included variable in question.
h


178
Chapter 6  Specification: Choosing the Independent Variables 
	 3.	 Including a variable in an equation in which it is actually irrelevant 
does not cause bias, but it will usually increase the variances of the 
included variables’ estimated coefficients, thus lowering their t-values, 
widening their confidence intervals, and lowering R  2.
	 4.	 Four useful criteria for the inclusion of a variable in an equation are:
a.	theory
b.	t-test
c.	 R  2
d.	bias
	 5.	 Theory, not statistical fit, should be the most important criterion for 
the inclusion of a variable in a regression equation. To do otherwise 
runs the risk of producing incorrect and/or disbelieved results.
Exercises
(The answers to the even-numbered exercises are in Appendix A.)
	 1.	 Write the meaning of each of the following terms without referring to 
the book (or your notes), and compare your definition with the ver-
sion in the text for each:
a.	expected bias (p. 161)
b.	irrelevant variable (p. 165)
c.	 omitted variable (p. 158)
d.	omitted variable bias (p. 158)
e.	 sensitivity analysis (p. 174)
f.	 sequential specification search (p. 170)
g.	specification error (p. 157)
h.	the four specification criteria (p. 166)
	 2.	 You’ve been hired by “Indo,” the new Indonesian automobile manu-
facturer, to build a model of U.S. car prices in order to help the com-
pany undercut U.S. prices. Allowing Friedmaniac zeal to overwhelm 
any patriotic urges, you build the following model of the price of 
35 different American-made 2016 U.S. sedans (standard errors in 
parentheses):
Model A: PNi = 9.0 + 0.28Wi + 1.2Ti + 5.8Ci + 0.19Li
10.072    10.42   12.92    10.202
R  2 = .92


179
Exercises
where:	
Pi  = the list price of the ith car (thousands of dollars)
	
	 	
Wi = the weight of the ith car (hundreds of pounds)
	
	 	
Ti  = a dummy equal to 1 if the ith car has an automatic trans-
mission, 0 otherwise
	
	 	
Ci  = a dummy equal to 1 if the ith car has cruise control, 0 
otherwise
	
	 	
Li  = the size of the engine of the ith car (in liters)
a.	Your firm’s pricing expert hypothesizes positive signs for all the 
slope coefficients in Model A. Test her expectations at the 5-percent 
level.
b.	What econometric problems appear to exist in Model A? In particu-
lar, does the size of the coefficient of C cause any concern? Why? 
What could be the problem?
c.	 You decide to test the possibility that L is an irrelevant variable by 
dropping it and rerunning the equation, obtaining the following 
Model T equation. Which model do you prefer? Why? (Hint: Be 
sure to use our four specification criteria.)
Model T: PN = 24 + 0.29Wi + 1.2Ti + 5.9Ci
10.072    10.302 12.92
       R  2 = .93  
	 3.	 Consider the following annual model of the death rate (per million 
population) due to coronary heart disease in the United States 1Yt2:
YNt = 140 + 10.0Ct + 4.0Et - 1.0Mt
12.52    11.02   10.52
t = 4.0        4.0   - 2.0
N = 31 11975-20052  R  2 = .678
where:	
Ct  = per capita cigarette consumption (pounds of tobacco) 
in year t
	
	 	
Et  = per capita consumption of edible saturated fats 
(pounds of butter, margarine, and lard) in year t
	
	 	
Mt = per capita consumption of meat (pounds) in year t
a.	Create and test appropriate hypotheses at the 10-percent level. What, 
if anything, seems to be wrong with the estimated coefficient of M?
b.	The most likely cause of a coefficient that is significant in the un-
expected direction is omitted variable bias. Which of the following 
variables could possibly be an omitted variable that is causing βN M’s 
unexpected sign? Explain. (Hint: Be sure to analyze expected bias in 
your explanation.)


180
Chapter 6  Specification: Choosing the Independent Variables 
Bt  = per capita consumption of hard liquor (gallons) in year t
Ft  = the average fat content (percentage) of the meat that was 
consumed in year t
Wt = per capita consumption of wine and beer (gallons) in year t
Rt  = per capita number of miles run in year t
Ht = per capita open-heart surgeries in year t
Ot = per capita amount of oat bran eaten in year t
c.	 If you had to choose a variable not listed in part b to add to the 
equation, what would it be? Explain your answer.
	 4.	 For each of the following situations, determine the sign (and, if pos-
sible, comment on the likely size) of the expected bias introduced by 
omitting a variable:
a.	In an equation for the demand for peanut butter, the impact on the 
coefficient of disposable income of omitting the price of peanut 
butter variable. (Hint: Start by hypothesizing signs.)
b.	In an earnings equation for workers, the impact on the coefficient 
of experience of omitting the variable for age.
c.	 In a production function for airplanes, the impact on the coeffi-
cient of labor of omitting the capital variable.
d.	In an equation for daily attendance at outdoor concerts, the impact 
on the coefficient of the weekend dummy variable (1 = weekend) 
of omitting a variable that measures the probability of precipita-
tion at concert time.
	 5.	 Let’s return to the model of financial aid awards at a liberal arts college 
that was first introduced in Section 2.2. In that section, we estimated 
the following equation (standard errors in parentheses):
	
FINAIDi = 8927 - 0.36 PARENTi + 87.4 HSRANKi	
(6.20)
10.032         120.72
t =       -11.26             4.22
R  2 = .73        N = 50
where:	
FINAIDi  = the financial aid (measured in dollars of 
grant) awarded to the ith applicant
	
PARENTi  = the amount (in dollars) that the parents of 
the ith student are judged able to contribute 
to college expenses
	
HSRANKi = the ith student’s GPA rank in high school, 
measured as a percentage (ranging from a 
low of 0 to a high of 100)
®


181
Exercises
a.	Create and test hypotheses for the coefficients of the independent 
variables.
b.	What econometric problems do you see in the equation? Are there 
any signs of an omitted variable? Of an irrelevant variable? Explain 
your answer.
c.	 Suppose that you now hear a charge that financial aid awards at the 
school are unfairly tilted toward males, so you decide to attempt to 
test this charge by adding a dummy variable for gender (MALEi = 1 
if the ith student is a male, 0 if female) to your equation, getting the 
following results:
FINAIDi = 9813 - 0.34 PARENTi + 83.3 HSRANKi - 1570 MALEi	
(6.21)
10.032         120.12         
17842
t =    
-10.88             4.13          -2.00
R  2 = .75       N = 50
d.	Carefully explain the real-world meaning of the estimated coef-
ficient of MALE. What would Equation 6.21 look like if you used 
FEMALE (= 1 if the ith student is a female and 0 otherwise) instead 
of MALE in the equation? (Hint: Be specific.)
e.	 Which equation is better, Equation 6.20 or Equation 6.21? Care-
fully use our four specification criteria to make your decision, 
being sure to state which criteria support which equation and why.
	 6.	 Suppose that you run a regression to determine whether gender or 
race has any significant impact on scores on a test of the economic 
understanding of children.11 You model the score of the ith student 
on the test of elementary economics 1Si2 as a function of the com-
posite score on the Iowa Tests of Basic Skills of the ith student, a 
dummy variable equal to 1 if the ith student is female (0 otherwise), 
the average number of years of education of the parents of the ith stu-
dent, and a dummy variable equal to 1 if the ith student is nonwhite 
(0 otherwise). Unfortunately, a rainstorm floods the computer center 
and makes it impossible to read the part of the computer output that 
identifies which variable is which. All you know is that the regression 
results are (standard errors in parentheses):
SN i = 5.7 - 0.63X1i - 0.22X2i + 0.16X3i + 1.20X4i
10.632     10.882     10.082     10.102
N = 24  R  2 = .54
®
11. These results have been jiggled to meet the needs of this question, but this research actually 
was done. See Stephen Buckles and Vera Freeman, “Male-Female Differences in the Stock and 
Flow of Economic Knowledge,” Review of Economics and Statistics, Vol. 65, No. 2, pp. 355–357.


182
Chapter 6  Specification: Choosing the Independent Variables 
a.	Attempt to identify which result corresponds to which variable. Be 
specific.
b.	Explain the reasoning behind your answer to part a.
c.	 Assuming that your answer is correct, create and test appropriate 
hypotheses (at the 5-percent level) and come to conclusions about 
the effects of gender and race on the test scores of this particular 
sample.
d.	Did you use a one-tailed or two-tailed test in part c? Why?
	 7.	 Let’s return to the model of Exercises 3-7 and 5-8 of the auction price 
of iPods on eBay. In that model, we used datafile IPOD3 to estimate 
the following equation:
PRICEi = 109.24 + 54.99NEWi - 20.44SCRATCHi + 0.73BIDRSi	
(6.22)
15.342        15.112           10.592
t =        
10.28       -4.00             1.23
N = 215
where:	
PRICEi
 = the price at which the ith iPod sold on eBay
	
	 	
NEWi
 = a dummy variable equal to 1 if the ith iPod 
was new, 0 otherwise
	
	 	
SCRATCHi = a dummy variable equal to 1 if the ith iPod 
had a minor cosmetic defect, 0 otherwise
	
	 	
BIDRSi
 = the number of bidders on the ith iPod
	
	 The dataset also includes a variable 1PERCENTi2 that measures the 
percentage of customers of the seller of the ith iPod who gave that seller 
a positive rating for quality and reliability in previous transactions.12 
In theory, the higher the rating of a seller, the more a potential bidder 
would trust that seller, and the more that potential bidder would be 
willing to bid. If you add PERCENT to the equation, you obtain
PRICEi = 82.67 + 55.42NEWi - 20.95SCRATCHi + 0.63BIDRSi + 0.28PERCENTi
15.342       15.122                 10.592           10.202
t =        10.38     
-4.10           1.07         1.40
N = 215	
(6.23)
a.	Use our four specification criteria to decide whether you think 
PERCENT belongs in the equation. Be specific. (Hint: R  2 isn’t given, 
but you’re capable of determining which equation had the higher R  2.)
h
h
12. For more on this dataset and this variable, see Leonardo Rezende, “Econometrics of Auctions 
by Least Squares,” Journal of Applied Econometrics, November/December 2008, pp. 925–948.


183
Exercises
b.	Do you think that PERCENT is an accurate measure of the quality and 
reliability of the seller? Why or why not? (Hint: Among other things, 
consider the case of a seller with very few previous transactions.)
c.	 (optional) With datafile IPOD3, use Stata, EViews, or your own regres-
sion program to estimate the equation with and without PERCENT. 
What are the R  2 figures for the two specifications? Were you correct in 
your determination (in part a) as to which equation had the higher R  2?
	 8.	 Look back at Exercise 9 in Chapter 5, the equation on international 
price discrimination in pharmaceuticals. In that cross-sectional study, 
Schut and VanBergeijk estimated two equations in addition to the 
one cited in the exercise.13 These two equations tested the possibility 
that CVi, total volume of consumption of pharmaceuticals in the ith 
country, and Ni, the population of the ith country, belonged in the 
original equation, Equation 5.15, repeated here:
	
PNi = 38.22 + 1.43GDPNi - 0.6CVNi + 7.31PPi	
(5.15)
10.212        10.222       16.122
t =         6.69      
-2.66       1.19
-15.63DPCi - 11.38PCi
16.932           17.162
t =        -2.25       -1.59
N = 32  R  2 = .775
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
 = a dummy variable equal to 1 if patents for phar-
maceutical products are recognized in the ith 
country, 0 otherwise
	
DPCi
 = a dummy variable equal to 1 if the ith country 
applied strict price controls, 0 otherwise
	
PCi
 = a dummy variable equal to 1 if the ith country 
encouraged price competition, 0 otherwise
13. Frederick T. Schut and Peter A. G. VanBergeijk, “International Price Discrimination: The 
Pharmaceutical Industry,” World Development, Vol. 14, No. 9, pp. 1141–1150.


184
Chapter 6  Specification: Choosing the Independent Variables 
a.	Using Stata, or your own computer program, and datafile DRUG5 
(or Table 5.2), estimate:
	
 i.  Equation 5.15 with CVi added, and
	
ii.  Equation 5.15 with Ni added
b.	Use our four specification criteria to determine whether CV and N 
are irrelevant or omitted variables. (Hint: The authors expected that 
prices would be lower if market size were larger because of possible 
economies of scale and/or enhanced competition.)
c.	 Why didn’t the authors run Equation 5.15 with both CV and N 
included? (Hint: While you can estimate this equation yourself, 
you don’t have to do so to answer the question.)
d.	Why do you think that the authors reported all three estimated 
specifications in their results when they thought that Equation 5.15 
was the best?
6.7   Appendix: Additional Specification Criteria
So far in this chapter, we’ve suggested four criteria for choosing the inde-
pendent variables (economic theory, R  2, the t-test, and possible bias in the 
coefficients). Sometimes, however, these criteria don’t provide enough infor-
mation for a researcher to feel confident that a given specification is best. For 
instance, there can be two different specifications that both have excellent 
theoretical underpinnings. In such a situation, many econometricians use 
additional, often more formal, specification criteria to provide comparisons 
of the properties of the alternative estimated equations.
The use of formal specification criteria is not without problems, however. 
First, no test, no matter how sophisticated, can “prove” that a particular 
specification is the true one. The use of specification criteria, therefore, must 
be tempered with a healthy dose of economic theory and common sense. A 
second problem is that more than 20 such criteria have been proposed. How 
do we decide which one(s) to use? Because many of these criteria overlap 
with one another or have varying levels of complexity, a choice between the 
alternatives is a matter of personal preference.
In this section, we’ll describe the use of three of the most popular specifi-
cation criteria, J. B. Ramsey’s RESET test, Akaike’s Information Criterion, and 
the Bayesian Information Criterion. Our inclusion of just these techniques 
does not imply that other tests and criteria are not appropriate or useful. 
Indeed, the reader will find that most other formal specification criteria have 
quite a bit in common with at least one of the techniques that we include. We 


185
  Appendix: Additional Specification Criteria
think that you’ll be better able to use and understand other formal specifica-
tion criteria14 once you’ve mastered these three.
Ramsey’s Regression Specification Error Test (RESET)
One of the most-used formal specification criteria other than R  2 is the 
Ramsey Regression Specification Error Test (RESET).15 The Ramsey RESET 
test is a general test that determines the likelihood of specification error by 
measuring whether the fit of a given equation can be significantly improved 
by the addition of YN 2, YN 3, and YN 4 terms.
What’s the intuition behind RESET? The additional terms act as proxies for 
any possible (unknown) omitted variables or incorrect functional forms. If the 
proxies can be shown by the F-test to have improved the overall fit of the original 
equation, then we have evidence that there is some sort of specification error in 
our equation. The YN 2, YN 3, and YN 4 terms form a polynomial functional form. Such 
a polynomial is a powerful curve-fitting device that has a good chance of acting 
as a proxy for a specification error if one exists. If there is no specification error, 
then we’d expect the coefficients of the added terms to be insignificantly different 
from zero because there is nothing for them to act as a proxy for.
The Ramsey RESET test involves three steps:
1.	 Estimate the equation to be tested using OLS:
	
YNi = βN 0 + βN 1X1i + βN 2X2i	
(6.24)
2.	 Take the YNi values from Equation 6.24 and create YN 2
i , YN 3
i , and YN 4
i  terms. 
Then add these terms to the original equation as additional explanatory 
variables and estimate the new equation with OLS:
	
Yi = β0 + β1X1i + β2X2i + β3YN 2
i + β4YN 3
i + β5YN 4
i + ei	
(6.25)
3.	 Compare the fits of Equations 6.24 and 6.25, using the F-test. Specifi-
cally, test the hypothesis that the coefficients of all three of the added 
terms are equal to zero:
H0: β3 = β4 = β5 = 0
HA: otherwise
14. For example, the likelihood ratio test can be used as a specification test. For an introduc-
tory level summary of six other specification criteria, see Ramu Ramanathan, Introductory Econo-
metrics (Fort Worth: Harcourt Brace Jovanovich, 1998, pp. 164–166).
15. J. B. Ramsey, “Tests for Specification Errors in Classical Linear Squares Regression Analysis,” 
Journal of the Royal Statistical Society, Vol. 31, No. 2, pp. 350–371.


186
Chapter 6  Specification: Choosing the Independent Variables 
	
If the two equations are significantly different in overall fit, we can con-
clude that it’s likely that Equation 6.24 is misspecified.
The appropriate F-statistic to use is Equation 5.10 from Section 5.6:
	
F = 1RSSM - RSS2/M
RSS/1N - K - 12	
(5.10)
where RSSM is the residual sum of squares from the constrained equation 
(Equation 6.24), RSS is the residual sum of squares from the unconstrained 
equation16 (Equation 6.25), M is the number of constraints (3 in this case), 
and 1N - K - 12 is the number of degrees of freedom in the unconstrained 
equation. If F is greater than the critical F-value with M and 1N - K - 12 
degrees of freedom, then we can reject the null hypothesis and conclude that 
there is a specification error in Equation 6.24. Many econometric software 
programs, including Stata,17 have a command that will automatically run 
Equation 6.25 and calculate the F-statistic using Equation 5.10.
While the Ramsey RESET test is fairly easy to use, it does little more than 
signal when a major specification error might exist. If you encounter a sig-
nificant Ramsey RESET test, then you face the daunting task of figuring out 
exactly what the error is! Thus, the test often ends up being more useful in 
“supporting” (technically, not refuting) a researcher’s contention that a given 
specification has no major specification errors than it is in helping find an 
otherwise undiscovered flaw.18
16. Because of the obvious correlation between the three YN values, Equation 6.25 (with most 
RESET equations) suffers from extreme multicollinearity. Since the purpose of the RESET equation 
is to see whether the overall fit can be improved by adding in proxies for an omitted variable 
(or other specification error), this extreme multicollinearity is not a concern.
17. To carry out the Ramsey RESET test in Stata, estimate Equation 6.24 and then run the 
“ovtest” command. For details, see the Using Stata guide on the textbook’s website at http://
www.pearsonhighered.com/studenmund.
18. The particular version of the Ramsey RESET test we describe in this section is only one of a 
number of possible formulations of the test. For example, some researchers delete the YN 4 term 
from Equation 6.25. At present, there is a mild split among econometricians about RESET. Jeff 
Wooldridge, “Score Diagnostics for Linear Models Estimated by Two Stage Least Squares,” in G.S. 
Maddala, P.C.B. Phillips, and T.N. Srinivasan (eds.), Advances in Econometrics and Quantitative 
Economics (Oxford: Blackwell, 1995), pp. 66–87, argues that RESET is primarily a functional 
form test. However, many applied econometricians continue to rely on RESET for a variety of 
specification tests, some even going so far as to use RESET in an to attempt to distinguish be-
tween pure and impure serial correlation and heteroskedasticity (to be discussed in Chapters 9 
and 10).


187
  Appendix: Additional Specification Criteria
Akaike’s Information Criterion and the Bayesian  
Information Criterion
A second category of formal specification criteria involves adjusting the 
summed squared residuals (RSS) by one factor or another to create an index 
of the fit of an equation. The most popular criterion of this type is R  2, but a 
number of interesting alternatives have been proposed.
Akaike’s Information Criterion (AIC) and the Bayesian Information 
Criterion (BIC) are methods of comparing alternative specifications by 
adjusting RSS for the sample size (N) and the number of independent 
variables (K).19 These criteria can be used to augment our four basic speci-
fication criteria when we try to decide if the improved fit caused by an 
additional variable is worth the decreased degrees of freedom and increased 
complexity caused by the addition. Their equations are:
	
 AIC = Log1RSS/N2 + 21K + 12/N
	
(6.26)
	
 BIC = Log1RSS/N2 + Log1N21K + 12/N	
(6.27)
In practice, these calculations may not be necessary because AIC and BIC are 
automatically calculated by some regression software packages, including Stata.
To use AIC and BIC, estimate two alternative specifications and calculate 
AIC and BIC for each equation. The lower AIC or BIC are, the better the 
specification. Note that even though the two criteria were developed inde-
pendently to maximize different object functions, their equations are quite 
similar. Both criteria tend to penalize the addition of another explanatory 
variable more than R  2 does. As a result, AIC and BIC will quite often20 be 
19. Hirotogu Akaike, “Likelihood of a Model and Information Criteria,” Journal of Econometrics, 
Vol. 16, No. 1, pp. 3–14 and G. Schwarz, “Estimating the Dimension of a Model,” The Annals of 
Statistics, Vol. 6, pp. 461–464. (The BIC is sometimes called the Schwarz Criterion.) The defini-
tions of AIC and BIC we use produce slightly different numbers than the versions used by Stata, 
but the versions map on a one-to-one basis and therefore produce identical conclusions.
20. Using a Monte Carlo study, Judge et al. showed that (given specific simplifying assumptions) 
a specification chosen by maximizing R  2 is more than 50 percent more likely to include an ir-
relevant variable than is one chosen by minimizing AIC or BIC. See George C. Judge, R. Carter 
Hill, W. E. Griffiths, Helmut Lutkepohl, and Tsoung-Chao Lee, Introduction to the Theory and 
Practice of Econometrics (New York: Wiley, 1988), pp. 849–850. At the same time, minimizing 
AIC or BIC will omit a relevant variable more frequently than will maximizing R  2


188
Chapter 6  Specification: Choosing the Independent Variables 
minimized by an equation with fewer independent variables than the ones 
that maximize R  2.
AIC and BIC require the researcher to come up with a particular alternative 
specification, whereas Ramsey’s RESET does not. Such a distinction makes 
RESET easier to use, but it makes AIC and BIC more informative if a specifica-
tion error is found. Thus our additional specification criteria serve different 
purposes. RESET is useful as a general test of the existence of a specification 
error, whereas AIC and BIC are useful as means of comparing two or more 
alternative specifications.
