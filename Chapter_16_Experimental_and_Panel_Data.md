# Chapter 16: Experimental and Panel Data

**Pages:** 485-578

---

465
Experimental  
and Panel Data
16.1  Experimental Methods in Economics
16.2  Panel Data
16.3  Fixed versus Random Effects
16.4  Summary and Exercises
Chapter 16
This chapter is a brief introduction to experimental data and panel data. The 
first section is devoted to experimental methods in economics.1 The experi-
mental approach is important because it offers a possible way for regression 
analysis to provide evidence of causality. If one group is exposed to a par-
ticular policy (like an increased tax or a decreased price) and a control group 
isn’t, then any meaningful difference between the behavior of the two groups 
is evidence that the policy caused that difference. Such experiments already 
are standard procedure in some areas of research, for example the testing 
of the safety and effectiveness of new medicines by the U.S. Food and Drug 
Administration.
The remainder of the chapter focuses on panel data. As mentioned in 
Chapter 11, panel data are formed when cross-sectional and time-series data 
sets are combined to create a single data set. Although some researchers use 
panel data to increase their sample size, the main reason for working with 
panel data is to provide an insight into analytical questions that can’t be 
answered by using time-series or cross-sectional data alone.
1. We use this awkward phrase to avoid confusion with the already existing field of experimen-
tal economics. Experimental economists run actual laboratory experiments on human subjects. 
By offering real-world incentives (usually money), experimental economists can reproduce 
supply and demand equilibria, test economic theories, and study market phenomena that oth-
erwise are difficult to observe. For accessible examples and innovative applications of random 
experiments to economic questions, see Uri Gneezy and John List, The Why Axis (London: 
­Random House Books, 2014).


466
Chapter 16  Experimental and Panel Data 
16.1   Experimental Methods in Economics
Any good statistician knows that correlation doesn’t prove causality, but 
understanding causality is important if we’re going to assess the effectiveness 
of economic policies, the profitability of business practices, or the value of 
not-for-profit programs. To try to solve this problem, some econometricians 
have imported experimental techniques from medicine and psychology. Can 
experimental methods provide evidence of causality in economics?
Random Assignment Experiments
When medical researchers want to examine the effect of a new drug, they 
use an experimental design called random assignment. You’re probably 
familiar with random assignment experiments because medical research 
studies are in the news virtually every week. The experiment generally pro-
ceeds as follows. First, a sample of subjects is chosen or recruited, and then 
they are randomly assigned to one of two groups—the control group or the 
treatment group. The treatment group receives the medicine that is being 
tested, and the control group receives a harmless, ineffective placebo. 
Similar experiments are possible in economics. To test whether a job train-
ing program has an impact on earnings, for example, the treatment group 
would receive the training and the control group wouldn’t. If the treatment 
and control groups are chosen randomly, then such experiments are called 
random assignment experiments.
It’s not hard to see why some researchers refer to random assignment as 
the gold standard in terms of establishing causality. Randomization helps 
ensure that any difference in the outcome between the control and the 
treatment group is causal and that the difference in outcome was caused 
by the treatment and not merely correlated with the treatment. The sub-
jects’ random assignment to the groups should be enough to guarantee 
that the only systematic reason for observed differences between the treat-
ment and control groups is the treatment. Any other differences are the 
chance consequence of the random assignment. For example, the random 
assignment may result in more males in one group than in the other, or 
one of the subjects may die for a reason that is unrelated to the disease 
or treatment being studied. With reasonably sized samples, such random 
fluctuations will most likely balance out so that, on average, the two 
groups are similar except that one group receives the treatment and the 
other doesn’t. The larger the sample, the more likely it is that random 
fluctuations will balance out.


467
  Experimental Methods in Economics
Factors other than the treatment that may affect the outcome are put in the 
error term, and the resulting equation is:
	
OUTCOMEi = β0 + β1TREATMENTi + ei	
(16.1)
where:   OUTCOMEi    = a measure of the desired outcome in the ith  
individual
	
 TREATMENTi = a dummy variable equal to 1 for individuals in 
the treatment group and 0 for individuals in the 
control group
β1 is often called the differences estimator because it measures the difference 
between the average outcome for the treatment group and the average outcome 
for the control group. If the estimated value of β1 is substantially different from 
zero in the direction predicted by theory, then we have evidence that the treat-
ment did indeed cause the outcome to move in the expected direction.
However, random assignment can’t always control for all other possible 
factors, and we may be able to identify some of these factors and add them to 
our equation. In our job training example, suppose that random assignment, 
by chance, results in one group having more males and being slightly older 
than the other group. If gender and age matter in determining earnings, then 
we can control for the different composition of the two groups by including 
gender and age in our regression equation:
	
OUTCOMEi = β0 + β1TREATMENTi + β2X1i + β3X2i + ei	
(16.2)
where X1 is a dummy variable for the individual’s gender and X2 is the indi-
vidual’s age.
Our recommendation is to use Equation 16.2 rather than Equation 16.1 if 
important additional factors are observable. After all, if the estimates of β1 in 
the two equations are quite similar, then the choice doesn’t matter. However, 
if the estimates differ, then we have evidence that random assignment did 
not control for other factors by evenly distributing these factors between the 
treatment and control groups. If that’s the case, then including these other 
factors (as in Equation 16.2) is likely to provide a better estimate of the dif-
ference caused by the treatment.
Unfortunately, random assignment experiments are not common in 
economics because they’re subject to problems that typically do not plague 
medical experiments. For example:
1.	 Non-Random Samples. Many subjects in economic experiments are vol-
unteers, and samples of volunteers often aren’t random. Not everyone is 
willing to volunteer, some potential subjects are willing to participate if 
they’re in the treatment group but not if they’re in the control group, and 


468
Chapter 16  Experimental and Panel Data 
some volunteers change their mind and drop out during the experiment. 
Unsurprisingly, the characteristics of a volunteer sample are not neces-
sarily representative of the population. Suppose, for example, that our 
research question is whether financial incentives for student achievement 
actually increase test scores. The professors and students who are willing 
to participate in this experiment may not be representative of the overall 
population and, as a result, our conclusions may not apply to everyone.
2.	 Unobservable Heterogeneity. In Equation 16.2, we added observable fac-
tors to the equation to avoid omitted variable bias, but not all omitted 
factors in economics are observable. This “unobservable omitted vari-
able” problem is called unobserved heterogeneity. Of course, if we can 
truly randomize the treatment, then this problem goes away because 
treatment is uncorrelated with the unobservables.2
3.	 The Hawthorne Effect. Human subjects typically know that they’re being 
studied, and they usually know whether they’re in the treatment group 
or the control group. The fact that human subjects know that they’re 
being observed sometimes can change their behavior, and this change 
in behavior could clearly change the results of the experiment. For ex-
ample, workers at the Western Electric Company’s Hawthorne Works 
plant were once put in a special room where researchers could study 
their productivity under controlled conditions. In one study, the lights 
were dimmed and the workers seemed to work harder, mainly because 
they knew that the researchers were watching to see if they worked 
harder! The fact that people behave differently when they know they 
are being watched is now called the Hawthorne Effect.
4.	 Impossible Experiments. It’s often impossible (or unethical) to run a ran-
dom assignment experiment in economics. Think about how difficult it 
would be to use a random assignment experiment to study the impact 
of marriage on earnings. On average, married men earn more than sin-
gle men even after accounting for observable differences in factors such 
as education and work experience. Unfortunately, there are a number 
of potential sources of unobservable heterogeneity, such as the possibil-
ity that women are more likely to marry men whom they judge to have 
high future earnings. A random assignment experiment might be able 
to sort these issues out, but imagine what such an experiment would 
entail. You’d have to randomly assign some men to marry and others 
to stay single! As you can see, this experiment, just like many other ran-
dom assignment experiments in economics, simply isn’t feasible.
2. With thanks to David Philips.


469
  Experimental Methods in Economics
Natural Experiments
If random assignment experiments aren’t always feasible in economics, what’s 
a good alternative? One approach is to use data from natural experiments to try 
to get at issues of causality. Natural experiments (or quasi-experiments) are 
similar to random assignment experiments except that observations fall into 
treatment and control groups “naturally” (because of an exogenous event) 
instead of being randomly assigned by the researcher. This approach requires 
finding natural events or policy changes that can be analyzed as if they were 
treatments in a random assignment experiment. As long as the natural event 
is exogenous (for example, not under the control of either of the groups), it 
turns out that a natural experiment can come very close to mimicking a ran-
dom assignment experiment. The key is to find naturally occurring events that 
mimic a random assignment experiment.
For instance, in 1992, New Jersey increased its minimum wage substan-
tially, while Pennsylvania kept its minimum wage constant. This led some 
economists to expect a decrease in employment at New Jersey fast-food res-
taurants (and other businesses that paid workers the minimum wage). In a 
famous study, Card and Krueger compared fast-food restaurants in New Jersey 
(the “treatment group”) with similar restaurants in nearby parts of Pennsylvania 
(the “control group”) and found no indication that the rise in the minimum 
wage reduced employment.3 Their study was a natural experiment!
A strict approach to natural experiments would seem to require that one 
find equivalents of “treatment” and “control” groups that have no systematic 
differences except for the treatment variable and other factors that can be 
observed and added to the equation. However, in economics, the treatment 
and control groups seem quite likely to have started off with different levels 
of the outcome measure. In addition, unobserved heterogeneity or nonran-
dom samples could result in the groups having different outcome measures. 
If the outcomes don’t start off equal, then comparing outcomes after the 
treatment won’t give us a true measure of the impact of the treatment. To 
understand why this is a problem, suppose that you were studying the impact 
of job training on income, and further suppose that your treatment group 
was earning an average of $30,000 per year while the control group was earn-
ing an average of $29,000 before the treatment. If the treatment group ended 
up earning $1,000 more than the control group after the treatment, would 
3. David Card and Alan Krueger, “Minimum Wages and Employment: A Case Study of the 
­Fast-Food Industry in New Jersey and Pennsylvania,” American Economic Review, Vol. 84, No. 4, 
pp. 772–793.


470
Chapter 16  Experimental and Panel Data 
this be convincing evidence that the treatment had a positive causal effect on 
income? Of course not!
To get around this problem, economists who run natural experiments 
don’t compare outcomes between the treatment and control groups. Instead, 
they compare the changes in the outcomes. Using this approach, we compare 
the change in the treatment group caused by the treatment with any change 
in the control group. The resulting “difference in differences” measures the 
impact of the treatment on the outcome in the natural experiment.
In a regression equation, the appropriate dependent variable in such a 
natural experiment thus is the difference in the outcome measure, not the 
outcome level we used in Equation 16.2. If we make this adjustment in 
Equation 16.2, we get:
	
∆OUTCOMEi =  β0 +  β1TREATMENTi +  β2X1i +  β3X2i +  ei	
(16.3)
where ∆OUTCOMEi is defined as the outcome after the treatment minus 
the outcome before the treatment for the ith observation. β1 is called the 
difference-in-differences estimator, and it measures the difference between 
the change in the treatment group and the change in the control group, 
holding constant X1 and X2. If the estimate of β1 is statistically significantly 
different from zero in the expected direction, then we have evidence that the 
treatment caused this change.
In essence, the difference-in-differences estimator uses the change in the 
control group as a measure of what would have happened to the treatment 
group if there hadn’t been a treatment. The validity of this approach thus 
depends on the assumption that the changes in the outcome would have 
been the same in both the treatment and control group had there been no 
treatment.
Be careful, however. Because the dependent variable has changed in 
Equation 16.3 from what it was in Equation 16.2, we also should change 
our interpretation of the independent variables and their coefficients. β2 
now measures the impact of a one-unit increase in X1 on the change in the 
­outcome (holding constant the other independent variables), not the level of 
the outcome. In addition, we should choose independent variables for Equa-
tion 16.3 keeping in mind that the dependent variable now is a difference.4
4. In addition, there’s evidence that the SE(βN )s are underestimated and need to be corrected 
when difference-in-difference models are estimated with OLS. See M. Bertrand, A. Diamond, 
and J. Hainmueller, “Synthetic Control Methods for Comparative Case Studies: Estimating the 
Effect of California’s Tobacco Control Program,” Journal of the American Statistical Association, 
Vol. 105, pp. 113–132.


471
  Experimental Methods in Economics
One final note. It’s important to think through the appropriate “before” 
and “after” time frames when you’re collecting data for a natural experiment. 
Data on the control and treatment groups should come from a time period 
far enough in advance of the policy change (treatment) that you are not pick-
ing up any anticipatory effects of the intended policy change. For example, 
if a company announces that it’s going to increase prices in the future, many 
people will buy the product just before the price increase takes effect in order 
to save money. As a result, data collected just before the price increase will 
overstate the true “before” quantity. Similarly, “after” data need to be col-
lected a reasonable amount of time after the policy change in order to allow 
individuals and firms to adjust to the change.
An Example of a Natural Experiment
Let’s take a look at an example of a natural experiment. In 1997, ARCO, one 
of the largest petroleum refiners and gasoline retailers in the world, acquired 
the Thrifty Oil Company, by far the biggest independent chain of gas stations 
in Southern California.5 Economists and consumers were concerned that the 
acquisition would reduce competition and therefore allow ARCO to increase 
prices.
This topic has the potential to be a good natural experiment, as the gas 
stations can be split into a treatment group (gas stations that competed with 
each other before the merger) and a control group (gas stations that didn’t 
compete with each other before the merger). To measure the impact of the 
merger on gasoline prices, a researcher would compare the difference in 
prices between the treatment and control groups before the acquisition with 
the price difference after the acquisition.
The treatment group consisted of ARCO gas stations that had a competing 
Thrifty station within a one-mile radius, and the control group was made up 
of ARCO gas stations that didn’t compete directly with a Thrifty station. Data 
were collected on a station-by-station basis, and gasoline prices before the 
acquisition were compared to those afterward.
Before the acquisition, prices in the treatment group were, on average, two 
to three cents lower than in the control group, which makes sense because 
the ARCO gas stations had to compete with the nearby Thrifty gas stations. 
After the acquisition, however, the treatment group prices were two to three 
cents higher than those in the control group!
5. This example is drawn from Justine Hastings, “Vertical Relationships and Competition in 
Retail Gasoline Markets: Empirical Evidence from Contract Changes in Southern California,” 
American Economic Review, March 2004, pp. 317–328.


472
Chapter 16  Experimental and Panel Data 
Take a look at Figure 16.1, which illustrates these results for Los Angeles. 
As can be seen, prices in the treatment group were lower than in the control 
group before the acquisition and were higher afterward. In essence, prices at 
ARCO gas stations that competed with Thrifty gas stations rose dramatically 
after ARCO acquired Thrifty.
Does this constitute evidence that the acquisition reduced gasoline price 
competition in Southern California? Take another look at Figure 16.1 
and compare the slopes of the two lines. The price trends in the treatment 
and control groups are virtually parallel in other time periods, suggesting 
that these results do indeed provide preliminary evidence that the elimina-
tion of an independent competitor raised market prices by 4 to 6 cents.6
1.55
1.45
1.35
1.25
1.15
December
February
June
Gasoline Price
October
December
Competed
with Thrifty
(treatment
group)
All Other
Stations
(control
group)
Figure 16.1  Treatment and Control Groups for Los Angeles
Gasoline prices in the treatment group were lower than those in the control group 
­before the acquisition and higher afterward.
6. Ibid., p. 323. Because Prof. Hastings had data from five time periods instead of just two, she 
didn’t estimate her equation using the difference-in-differences model of this section. Instead, 
she used the fixed-effects estimation technique to be described in Section 16.2.


473
  Panel Data
16.2   Panel Data
Let’s think for a second about the data in the ARCO gasoline price example 
of the previous section. Is it a time-series data set? Is it a cross-sectional data 
set? Well, the data set includes gasoline prices from five different months, so 
it clearly has a time-series component. However, the data set also includes 
prices for hundreds of individual gas stations for each month, so it clearly 
has a cross-sectional component. Because it has both time-series and cross-
sectional dimensions, it’s neither time-series nor cross-sectional; it’s a panel 
data set!
What Are Panel Data?
Panel (or longitudinal) data combine time-series and cross-sectional data in 
a very specific way. Panel data include observations on the same variables 
from the same cross-sectional sample from two or more different time peri-
ods. For example, if you surveyed 200 students when they graduated from 
your school and then administered the same questionnaire to the same indi-
viduals five years later, you would have created a panel data set.
Not every data set that combines time-series and cross-sectional data meets 
this definition. In particular, if different variables are observed in the different 
time periods or if the data are drawn from different samples in the different 
time periods, then the data are not considered to be panel data.7
Some panel data sets are created by large-scale, long-term longitudinal sur-
veys, for instance the 1979 National Longitudinal Survey of Youth (NLSY). 
Available through the Bureau of Labor Statistics, the NLSY has followed a 
cohort of 12,686 men and women who were 14 to 22 years old in 1979. 
These individuals were surveyed annually from 1979 through 1994 and have 
been surveyed every other year since then.8 Quite obviously, a panel data set 
of this many individuals collected over such a long time period provides an 
7. Instead, we refer to these data sets as “pooled cross sections across time.” An example of 
pooled cross sections across time would be if you administered a survey to 200 graduating se-
niors from the class of 2009 and combined the results of this survey with the results of a survey 
of 200 graduating seniors from the class of 2004. The combined data set is not a panel data 
set because the sample changed as the time period changed. Equations can be estimated with 
pooled cross sections across time data by using a variant of the difference-in-differences estima-
tor of the previous section. For more, see Jeff Wooldridge, Introductory Econometrics (Mason, 
OH: South-Western, 2009), pp. 445–455.
8. http://www.bls.gov/nls/nlsy79.htm.


474
Chapter 16  Experimental and Panel Data 
extremely rich source of labor force data. Other well-known longitudinal 
surveys include the U.S. Panel Survey of Income Dynamics (PSID), the ­British 
Household Panel Data Survey, and the Canadian National Public Health 
Survey.
Why use panel data? As mentioned earlier, panel data certainly will 
increase sample sizes, but a second advantage of panel data is to provide 
insight into analytical questions that can’t be answered by using time-series 
or cross-sectional data alone. For example, panel data can help policymakers 
design programs aimed at reducing unemployment by allowing research-
ers to determine whether the same people are unemployed year after year 
or whether different individuals are unemployed in different years.9 A final 
advantage of using panel data is that it often allows researchers to avoid 
omitted variable problems that otherwise would cause bias in cross-sectional 
studies. We’ll come back to this topic soon.
There are four different kinds of variables that we encounter when we use 
panel data. First, we have variables that can differ between individuals but 
don’t change over time, such as gender, ethnicity, and race. Second, we have 
variables that change over time but are the same for all individuals in a given 
time period, such as the retail price index and the national unemployment 
rate. Third, we have variables that vary both over time and between individu-
als, such as income and marital status. Fourth, we have trend variables that 
vary in predictable ways such as an individual’s age.
To estimate an equation using panel data, it’s crucial that the data be in 
the right format because regression packages like Stata and EViews need to 
identify which observations belong to which time periods and which cross-
sectional entities. Unfortunately different software programs have different 
format requirements for panel data. Stata, for example, requires that a panel 
data set include a date counter and an id number counter, but it doesn’t 
require that the data be in any particular order. Many other programs, how-
ever, require the data to be in a specific order, typically by grouping all the 
observations from one cross-sectional entity together before moving on to 
another cross-sectional entity. As a result, it’s important to check to make sure 
that your data format matches what is required by your regression program.
Finally, the use of panel data requires a slight expansion of our notation. 
In the past we’ve used the subscript i to indicate the observation number in a 
cross-sectional data set, so Yi indicated Y for the ith cross-sectional observa-
tion. Similarly, we’ve used the subscript t to indicate the observation number 
9. Peter Kennedy, A Guide to Econometrics (Malden, MA: Blackwell, 2008), p. 282.


475
  Panel Data
in a time-series data set, so Yt indicated Y for the tth time-series observation. 
In a panel data set, however, variables will have both a cross-sectional and a 
time-series component, so we’ll use both subscripts. As a result, Yit indicates 
Y for the ith cross-sectional and tth time-series observation. This notation 
expansion also applies to independent variables and error terms.
The Fixed Effects Model
What’s the best way to estimate panel data equations? The two main 
approaches10 are the fixed effects model discussed in this section and the ran-
dom effects model featured in the next section.
The fixed effects model estimates panel data equations by including 
enough dummy variables to allow each cross-sectional entity (like a state or 
country) and each time period to have a different intercept:
	 Yit = β0 + β1Xit + α2EF2 + g + αNEFN + ρ2TF2 + g + ρ  TTF T + eit	(16.4)
where:	
EFi = N - 1 Entity Fixed Effects dummies, equal to 1 for the ith 
       entity and 0 otherwise
	
TFt = T - 1 Time Fixed Effects dummies, equal to 1 for the tth  
	
period and 0 otherwise
βs, αis, and ρts = regression coefficients to be estimated
	
e   = a classical error term
As you’d expect with a panel data set, Y, X, and e have two subscripts. 
Although there is only one X in Equation 16.4, the model can be generalized 
to any number of independent variables.
Why do we need something as complicated as Equation 16.4? To answer, 
let’s begin by taking a look at the problems that would arise if we estimated 
our model without accounting for the fact that our observations are from a 
panel data set. Our equation would look like this:
	
Yit = β0 + β1Xit + Vit	
(16.5)
That looks pretty familiar, except that you’re probably thinking, “Where did 
that weird looking big Vit come from?” It’s the error term, and you’re right, it 
is weird looking.
10. Other methods of estimating panel data equations include the differencing model (the subject 
of Exercise 6) and the demeaned model (in which the mean of Y is subtracted from each observa-
tion of Y, the mean of X is subtracted from each observation of X, and the regression is run on 
these “demeaned” variables).


476
Chapter 16  Experimental and Panel Data 
To understand V, remember that because we’re dealing with panel data, 
we have observations from several, maybe many, entities and from several, 
maybe many, time periods. Just about everyone would agree that no two 
states are exactly alike. They have different cultures, histories, and institutions. 
It’s easy to imagine that those differences might lead to different outcomes in 
all sorts of things we might want to explain. Our Yit could be income, health, 
or crime, for instance.
It’s also easy to see that things like a state’s history and culture are pretty 
constant from year to year. They might be hard to measure, but we know that 
they don’t change, and we know that they make each state different from all 
the others. It is very likely that these unchanging and unmeasured differences 
are correlated with X, but Equation 16.5 doesn’t include them, so they are 
omitted variables.
And that’s a problem, right? In Chapter 6 we learned that omitting a 
relevant variable from a model forces much of its influence into the error 
term. And that partly explains the weird error term V in Equation 16.5. 
But there’s more. Remember that we’re dealing with panel data. Not only 
have we combined several cross sections, but we’ve also combined some 
time series! That means we have even more potential omitted variables. 
Why is that?
Well, it’s entirely possible that during each time period, certain things 
affect all the entities, but that those common influences change from period 
to period. Suppose you’re investigating annual traffic fatalities in states over 
a period of many years. If the federal government raises or lowers the maxi-
mum highway speed limit, it affects traffic fatalities in all states. Similarly, 
changing social norms affect traffic fatalities over time. Attitudes about seat 
belts, for instance, could play a big role. People didn’t always buckle up with-
out thinking! If you doubt this, ask your grandparents how many of them 
used seatbelts back when they were kids.
With the omitted entity characteristics and the omitted time characteristics, 
the error term in Equation 16.5 can be broken down into three components:
Vit = eit + ai + zt
where eit is a classical error term, ai refers to the entity characteristics omitted 
from the equation, and zt refers to the time characteristics omitted from the 
equation. If ai and zt are correlated with Xit, we’re going to have a problem 
because we will have violated Classical Assumption III. Our estimate of β1 
will be biased.
As we learned in Chapter 6, the solution in theory is simple. Just include 
the omitted variables in the model, and the omitted variable bias will disap-
pear. But the omitted variables often are unobservable. And even if we could 


477
  Panel Data
see them, we might not be able to measure them. For instance, if the entities 
are states, the unobserved characteristics could be such things as culture or 
history. How in the world would we ever discover what they are, much less 
measure them?
As it happens, we already have something in our econometric toolbox that 
can solve the problem—dummy variables! By including dummy variables 
for every entity (EFi) but one, we can control for those unobservable but 
unchanging entity effects. We call them entity fixed effects. And by including 
dummy variables for every time period (TFt) but one, we can control for time 
fixed effects. These entity and time fixed effects will no longer be omitted 
variables because they will be represented by the dummy variables. Including 
the dummies transforms V into e and transforms Equation 16.5 into the basic 
fixed effects model, Equation 16.4:
	Yit = β0 + β1Xit + α2EF2 + g + αNEFN + ρ2TF2 + g + ρ  TTF T + eit	 (16.4)
The major advantage of the fixed effects model is that it avoids bias due to 
omitted variables that don’t change over time (like geography) or that change 
over time equally for all entities (like the federal speed limit). What we’re in 
essence doing is allowing each entity’s intercept and each time period’s inter-
cept to vary around the omitted condition baseline (when all the fixed effect 
dummies equal zero). And the beauty of it is that we don’t even have to know 
exactly what things go into the entity and time fixed effects. The dummy vari-
ables include them all!
The fixed effects model has some drawbacks, however. Degrees of free-
dom for fixed effects models tend to be low because we lose one degree of 
freedom for every dummy variable (the EFs and the TFs) in the equation. For 
example, if the panel contains 50 states and two years, we lose 50 degrees of 
freedom by using 49 state dummies and one year dummy. Another potential 
pitfall is that no substantive explanatory variables that vary across entities, 
but do not vary over time within each entity, can be used because they would 
create perfect multicollinearity.
Luckily, these drawbacks are minor when compared to the advantages of 
the fixed effects model, so our recommendation is that readers of this text use 
the fixed effects model whenever they estimate panel data models.
An Example of Fixed Effects Estimation
Let’s take a look at a simple application of the fixed effects model. Suppose 
that you’re interested in the relationship between the death penalty and the 
murder rate, and you collect data on the murder rate in the 50 states.


478
Chapter 16  Experimental and Panel Data 
If you were to estimate a cross-sectional model (Table 16.1) of the annual 
murder rate as a function of, say, the number of convicted murderers who 
were executed in the previous three years, you’d end up with:
	
MRDRTEi = 6.20 + 0.90EXECi	
(16.6)
	
(0.22)
	
t = 4.09
	
N = 50 (states  in 1990)  R  2 = .24
where:          MRDRTEi 5 the number of murders per 100,000 people in the 
ith state in 1990
	
EXECi        5 the number of executions in the ith state in 
1987–89
In a cross-sectional model for 1990, the murder rate appears to increase with 
the number of executions, quite probably because of omitted variable bias 
or because of simultaneity. This result implies that the more executions there 
are, the more murders there are! Such a result is completely counter to our 
∏
20
15
10
5
0
5
Total executions, past 3 years
10
0
Fitted values
Murders per 100,000 people
Figure 16.2  In a Single-Year Cross-Sectional Model, the Murder Rate 
­Appears to Increase with Executions
In a cross-sectional model for 1990, the murder rate appears to increase with the 
­number of executions.


479
  Panel Data
Table 16.1  Data for the Murder Example
OBS
STATE
YEAR
MRDRTE
EXEC
TF93
  1
AL
90
11.6
5
0
  2
AL
93
11.6
2
1
  3
AK
90
  7.5
0
0
  4
AK
93
9
0
1
  5
AZ
90
  7.7
0
0
  6
AZ
93
  8.6
3
1
  7
AR
90
10.3
2
0
  8
AR
93
10.2
2
1
  9
CA
90
11.9
0
0
10
CA
93
13.1
2
1
11
CO
90
  4.2
0
0
12
CO
93
  5.8
0
1
13
CT
90
  5.1
0
0
14
CT
93
  6.3
0
1
15
DE
90
5
0
0
16
DE
93
5
0
1
17
FL
90
10.7
8
0
18
FL
93
  8.9
7
1
19
GA
90
11.8
2
0
20
GA
93
11.4
3
1
21
HI
90
4
0
0
22
HI
93
  3.8
0
1
23
ID
90
  2.7
0
0
24
ID
93
  2.9
0
1
25
IL
90
10.3
0
0
26
IL
93
11.4
0
1
27
IN
90
  6.2
0
0
28
IN
93
  7.5
0
1
29
IA
90
  1.9
0
0
30
IA
93
2.3
0
1
31
KS
90
4
0
0
32
KS
93
  6.4
0
1
33
KY
90
  7.2
0
0
34
KY
93
  6.6
0
1
35
LA
90
17.2
4
0
36
LA
93
20.3
2
1
37
ME
90
  2.4
0
0
38
ME
93
  1.6
0
1
39
MD
90
11.5
0
0
40
MD
93
12.7
0
1
41
MA
90
4
0
0
42
MA
93
  3.9
0
1
43
MI
90
10.4
0
0
(continued)


480
Chapter 16  Experimental and Panel Data 
Table 16.1  (continued)
OBS
STATE
YEAR
MRDRTE
EXEC
TF93
44
MI
93
  9.8
0
1
45
MN
90
  2.7
0
0
46
MN
93
  3.4
0
1
47
MS
90
12.2
1
0
48
MS
93
13.5
0
1
49
MO
90
  8.8
5
0
50
MO
93
11.3
6
1
51
MT
90
  4.9
0
0
52
MT
93
3
0
1
53
NE
90
  2.7
0
0
54
NE
93
  3.9
0
1
55
NV
90
  9.7
3
0
56
NV
93
10.4
0
1
57
NH
90
  1.9
0
0
58
NH
93
2
0
1
59
NJ
90
  5.6
0
0
60
NJ
93
  5.3
0
1
61
NM
90
  9.2
0
0
62
NM
93
8
0
1
63
NY
90
14.5
0
0
64
NY
93
13.3
0
1
65
NC
90
10.7
0
0
66
NC
93
11.3
2
1
67
ND
90
  0.8
0
0
68
ND
93
  1.7
0
1
69
OH
90
  6.1
0
0
70
OH
93
6
0
1
71
OK
90
8
1
0
72
OK
93
  8.4
2
1
73
OR
90
  3.8
0
0
74
OR
93
  4.6
0
1
75
PA
90
  6.7
0
0
76
PA
93
  6.8
0
1
77
RI
90
  4.8
0
0
78
RI
93
  3.9
0
1
79
SC
90
11.2
1
0
80
SC
93
10.3
1
1
81
SD
90
2
0
0
82
SD
93
  3.4
0
1
83
TN
90
10.5
0
0
84
TN
93
10.2
0
1
85
TX
90
14.1
11
0
86
TX
93
11.9
34
1
(continued)


481
  Panel Data
expectations. To make things worse, it’s not a fluke. If we collect data from 
another year, 1993, and estimate a single-time-period regression on the 1993 
data set, we also get a positive slope.
However, if we combine the two cross-sectional data sets to create the 
panel data set in Table 16.1, we can estimate a fixed effects model, using the 
fixed effects model of Equation 16.4, adjusted to account for 50 states (with 
Alabama as the omitted condition) and two time periods (with 1990 as the 
omitted condition):
	 MRDRTEit = β0 + β1EXECit + α2EF2 + g + α50EF50 + ρ2TF93 + eit	
(16.7)
If we now estimate Equation 16.7 with the data from Table 16.1, we obtain:
	
MRDRTEit = 7.15 - 0.104EXECit + 0.35TF93	
(16.8)
	
(0.04)	
(0.16)
	
t = 	
- 2.38	
+ 2.23
	
N = 100	
R  2 = .96
As can be seen in Equation 16.8 and Figure 16.3, a fixed effects model 
estimated on panel data from 1990 and 1993 results in a significant negative 
estimated slope for the relationship between the murder rate and the number 
∏
OBS
STATE
YEAR
MRDRTE
EXEC
TF93
87
UT
90
3
1
0
88
UT
93
  3.1
1
1
89
VT
90
  2.3
0
0
90
VT
93
  3.6
0
1
91
VA
90
  8.8
3
0
92
VA
93
  8.3
11
1
93
WA
90
  4.9
0
0
94
WA
93
  5.2
1
1
95
WV
90
  5.7
0
0
96
WV
93
  6.9
0
1
97
WI
90
  4.6
0
0
98
WI
93
  4.4
0
1
99
WY
90
  4.9
0
0
100
WY
93
  3.4
1
1
Source: U.S. Department of Justice, FBI Annual, www.deathpenaltyinfo.org/execution
Datafile 5 MURDER16
Table 16.1  (continued)


482
Chapter 16  Experimental and Panel Data 
of executions.11 This example illustrates how the omitted variable bias arising 
from unobserved heterogeneity can be mitigated with panel data and the fixed 
effects model. When the dataset is expanded to include another year, you’re in 
essence looking at each state and comparing the state to itself over time.
Note that we included TF93, a year fixed effect variable, in Equation 16.8. A 
year fixed effect captures any impact that altered the level of executions across 
the country for a given year. For example, if the Supreme Court declared a mor-
atorium on a type of execution in that year, we would see a decline in execu-
tions across states that used that type of execution during the year for reasons 
unrelated to the relation between murders and executions for each state.12
11. This example was kept simple to illustrate the value of panel data and to show how to apply 
the fixed effects model to panel data, so no inferences about the death penalty should be drawn 
from it. The correct specification surely includes a number of other variables. In addition, 
the state of Texas plays too large a role in determining the coefficients in this sample, in part 
­because many states didn’t allow capital punishment between 1987 and 1993.
12. With thanks to Doug Steigerwald.
Figure 16.3  In a Panel Data Model, the Murder Rate Decreases with 
­Executions
If we use the fixed effects model to estimate panel data from 1990 and 1993, the mur-
der rate decreases with the number of executions, as you’d expect.
20
15
10
5
0
5
Total executions, past 3 years
10
0
Fitted values
Murders per 100,000 people


483
  Fixed versus Random Effects
You might have noticed the big increase in R  2 between Equations 16.7 and 
16.8. The increase comes from the addition of all the dummy variables for 
state and time fixed effects. So why don’t the coefficients of the state dum-
mies appear in Equation 16.8? Unless the entity fixed effects are the main 
focus of the research, the coefficients usually are omitted from the results to 
save space. Some large panel data sets have hundreds or even thousands of 
entity fixed effects!
In our example, we used only two time periods, but the fixed effects model 
can be extended to many more time periods. Fixed effects estimation is a 
standard statistical routine in most econometric software packages, making 
it particularly accessible for researchers. Notice that we report an intercept. 
Depending upon which software program you use to estimate the fixed 
effects model, you may or may not be provided with an intercept estimate.
16.3   Fixed versus Random Effects
The fixed effects model does a good job of estimating panel data equations, 
and it also helps avoid omitted variable bias due to unobservable heterogene-
ity. As a result, the fixed effects model is the panel data estimation procedure 
that we recommend to most readers of this text.
However, if you read the panel data literature, you’ll find that many expe-
rienced researchers use an advanced panel data method called the random 
effects model. Although we don’t suggest that beginning researchers use the 
random effects model, we think that it’s important to have a general under-
standing of that model.
The Random Effects Model
An alternative to the fixed effects model is called the random effects model. 
While the fixed effects model is based on the assumption that each cross-
sectional unit has its own intercept, the random effects model is based on 
the assumption that the intercept for each cross-sectional unit is drawn from 
a distribution that is centered around a mean intercept. Thus each intercept is 
a random draw from an “intercept distribution” and therefore is independent 
of the error term for any particular observation.
The random effects model has several clear advantages over the fixed 
effects model. In particular, a random effects model will have quite a few 
more degrees of freedom than a fixed effects model, because rather than esti-
mating an intercept for virtually every cross-sectional unit, all we need to do 


484
Chapter 16  Experimental and Panel Data 
is to estimate the parameters that describe the distribution of the intercepts. 
Another nice property is that you can estimate coefficients for explanatory 
variables that are constant over time (like race or gender). However, the 
random effects estimator has a major disadvantage in that it requires us 
to assume that the unobserved impact of the omitted variables is uncorre-
lated with the independent variables, the Xs, if we’re going to avoid omitted 
­variable bias.
Choosing Between Fixed and Random Effects
How do researchers decide whether to use the fixed effects model or the ran-
dom effects model? One key is the nature of the relationship between ai and the 
Xs. If they’re likely to be correlated, then it makes sense to use the fixed effects 
model, as that sweeps away the ai and the potential omitted variable bias.13
Many researchers use the Hausman test, which is well beyond the scope 
of this text, to see whether there is correlation between ai and X. Essentially, 
this procedure tests to see whether the regression coefficients under the 
fixed effects and random effects models are statistically different from each 
other.14 If they are different, then the fixed effects model is preferred even 
though it uses up many more degrees of freedom. If the coefficients aren’t 
different, then researchers either use the random effects model (in order to 
conserve degrees of freedom) or provide estimates of both the fixed effects 
and ­random effects models.
16.4   Summary
1.	
Random assignment experiments are considered the gold standard 
when it comes to establishing a causal effect from treatment to out-
come. A randomly chosen treatment group is exposed to a treatment 
while a control group isn’t, and we test to see if the outcome is signifi-
cantly different between the two groups. Unfortunately, such experi-
ments aren’t feasible in many areas of economics.
13. For an excellent explanation of the choice between fixed and random effects, see Peter Ken-
nedy, A Guide to Econometrics (Malden, MA: Blackwell, 2008), pp. 284–292.
14. For an illustration of the Hausman test, see E. DiCioccio and P. Wunnava, “Working and 
Educated Women: Culprits of a European Kinder-Crisis,” Eastern Economic Journal, April 2008, 
pp. 213–222.


485
EXERCISES
2.	
Natural experiments can be used to provide evidence of causality in 
economics if a naturally occurring event (or a policy change) can 
be found that mimics a random assignment treatment. If the event 
causes the mean of the outcome for the treatment group to change 
substantially more than the mean of the outcome for the control 
group does, then we have evidence that the treatment was a causal 
­factor in the outcome.
3.	
Equations involving data from natural experiments can be estimated 
with a difference-in-differences model, which compares the difference 
between the change in the treatment group and the change in the 
control group.
4.	
Panel data combine time-series and cross-sectional data by includ-
ing observations on the same variables from the same cross-sectional 
sample from two or more time periods. Panel data often are produced 
by large, multi-year survey projects and provide a rich source of mate-
rial for econometric analysis.
5.	
Equations involving panel data can be estimated using the fixed effects 
model and a more advanced technique, the random effects model.
EXERCISES
(The answers to the even-numbered questions are in Appendix A.)
	 1.	 Write the meaning of each of the following terms without referring to 
the book (or your notes), and then compare your definition with the 
version in the text for each.
a.	control group (p. 466)
b.	difference-in-differences (p. 470)
c.	 fixed effects model (p. 475)
d.	natural experiments (p. 469)
e.	 panel data (p. 473)
f.	 random assignment experiments (p. 466)
g.	random effects model (p. 483)
h.	treatment group (p. 466)
	 2.	 Fifteen years ago, the town of Easton decided to increase its annual 
spending on education so that its high school graduates would be 
able to earn higher wages. Now Easton has asked you to evaluate the 
effectiveness of the spending increase. Their data show that before 


486
Chapter 16  Experimental and Panel Data 
the spending increase, the average annual salary of recent high school 
graduates was $25,000 and that now that average salary has risen to 
$28,500. Fortunately for your analysis, a neighboring community 
(Allentown) did not change its annual spending on education. Fif-
teen years ago, recent Allentown high school graduates earned an 
average of $22,500, and now that average is $23,750.
a.	Use a difference-in-differences estimator to determine whether 
Easton’s spending increase caused the wages of their high school 
graduates to increase.
b.	What underlying assumption do you have to make in order for 
your estimate to be valid? What might cause your underlying 
­assumption to be invalid?
c.	 This data set contains only two observations. Even if the underlying 
assumption in part b is met, how much confidence can you have in 
conclusions based on two observations?
	 3.	 The discussion of random assignment experiments in Section 16.1 
includes models both with (Equation 16.2) and without (Equa-
tion 16.1) two additional observable factors (X1 and X2). In con-
trast, the discussion of natural experiments in Section 16.1 jumped 
immediately to Equation 16.3 below (which includes these factors) 
without discussing an equation similar to Equation 16.1.
	
∆OUTCOMEi = β0 + β1TREATMENTi + β2X1i + β3X2i + ei	 (16.3)
	
	 Was this a mistake? What reasons are there for thinking that a natural 
experiment is more likely to benefit from the inclusion of additional 
observable factors than is a random assignment experiment? Explain.
	 4.	 In 2003, ten states increased the taxes they placed on cigarettes. 
Because taxes increase the price of cigarettes, we’d expect that a tax 
increase would reduce the consumption of cigarettes. In Table 16.2, 
we present cross-sections of state level data on cigarette consump-
tion for the years 2000 and 2006. Forty-four states plus the District 
of Columbia are listed here, with those states that did not have a tax 
increase in 2003 listed first.
a.	Would you consider this to be a random assignment experiment 
data set, a natural experiment data set, or a panel data set? Explain.
b.	Depending on your answer to part a, use the appropriate estima-
tion technique to determine the impact of the cigarette tax increase 
on the consumption of cigarettes.
c.	 Do these results conform with your expectations? If they don’t, 
what problems do you see with this research design?


Table 16.2  Cigarette Consumption by State
State
Tax
2000
2006
Alabama
0
25.3
23.2
Arizona
0
18.6
18.2
Alaska
0
25
24
Arkansas
0
25.2
23.7
Colorado
0
20.1
17.9
Connecticut
0
20
17
Delaware
0
23
21.7
Hawaii
0
19.7
17.5
Illinois
0
22.3
20.5
Indiana
0
27
24.1
Iowa
0
23.3
21.4
Kentucky
0
30.5
28.5
Louisiana
0
24.1
23.4
Maine
0
23.8
20.9
Maryland
0
20.6
17.7
Massachusetts
0
20
17.8
Michigan
0
24.2
22.4
Minnesota
0
19.8
18.3
Montana
0
18.9
18.9
Nebraska
0
21.4
18.7
New Hampshire
0
25.4
18.7
New Jersey
0
21
18
New York
0
21.6
18.2
North Carolina
0
26.1
22.1
Ohio
0
26.3
22.4
Oklahoma
0
23.3
25.1
Oregon
0
20.8
18.5
Pennsylvania
0
24.3
21.5
Rhode Island
0
23.5
19.2
Tennessee
0
25.7
22.6
Texas
0
22
17.9
Utah
0
12.9
  9.8
Virginia
0
21.5
19.3
Washington
0
20.7
17.1
Wisconsin
0
24.1
20.8
Washington, DC
1
20.9
17.9
Georgia
1
23.6
19.9
Idaho
1
22.4
16.8
Kansas
1
21.1
20
Nevada
1
29.1
22.2
New Mexico
1
23.6
20.1
South Dakota
1
22
20.3
Vermont
1
21.5
18
West Virginia
1
26.1
25.7
Wyoming
1
23.8
21.6
Datafile 5 CIGI6                   
487
EXERCISES


488
Chapter 16  Experimental and Panel Data 
	 5.	 Suppose that you’re interested in the effect of price on the demand for 
a “salon” haircut and that you collect the following data for four U.S. 
cities for 2003:
Location
Year
Average Price
Per Capita Quantity
New York
2003
$75
2
Boston
2003
$50
1
Washington, DC
2003
$60
1.5
Philadelphia
2003
$55
0.8
	
	 and for 2008:
Location
Year
Average Price
Per Capita Quantity
New York
2008
$85
1.8
Boston
2008
$48
1.1
Washington, DC
2008
$65
1.4
Philadelphia
2008
$60
0.7
a.	Estimate a cross-sectional OLS regression of per capita quantity as a 
function of average price for 2003. Is the slope positive or negative? 
Does that meet your expectations?
b.	Now estimate a cross-sectional regression on the data for 2008. 
How is the result different?
c.	 Now estimate a fixed effects model on the combined data and 
compare your results with parts a and b.
d.	What’s your conclusion? Which model offers the best approach to 
answering your question?
	 6.	 A simple alternative to the fixed effects model is called the differencing 
model, in which all the variables and the error term are expressed as 
differences. For a panel data set with two time periods, the estimating 
equation would be:
∆Yi = β0 + β1∆Xi + ∆ei
	
	 where: 
∆Yi = Y2i - Y1i, ∆Xi = X2i - X1i, and ∆ei = e2i - e1i.
a.	Using the data in Exercise 5, estimate a differencing model for the 
price of salon haircuts.


b.	Now compare your answer in part a to your answer for part c of 
Exercise 5. What do you notice? What does this tell you about the 
relationship between the differencing model and the fixed effects 
model when there are exactly two time periods?
c.	 Think about the error term in the differencing model. Which of the 
Classical Assumptions does ∆ei seem likely to violate? How might 
you deal with this problem?
489
EXERCISES


This page intentionally left blank


491
Answers
Appendix A
Chapter 1
1.2.	
Using Stata:
	
a.	Install and launch the regression software.
	
b.	Open the datafile. All datafiles can be found in Stata format at 
www.pearsonhighered.com/studenmund. This particular datafile 
is “HTWT1.”
	
c.	 Run the regression. Type “reg Y X” in the command window. This 
tells Stata to run a regression using Y as the dependent variable 
and X as the independent variable. Hit enter and the results will 
appear in the results window.
	
Using EViews:
	
a.	Install and launch the software.
	
b.	Open the datafile. All datafiles can be found in EViews format at 
www.pearsonhighered.com/studenmund. This particular datafile 
is “HTWT1.”
	
c.	 Run the regression. Type “LS Y C X” on the top line, making sure 
to leave spaces between the variable names. (LS stands for Least 
Squares and C stands for constant.) Press Enter, and the regres-
sion results will appear on your screen.
1–4.	
a.	The estimated slope coefficient of 3.62 represents the change in 
the size of a house (in square feet) given a one thousand dol-
lar increase in the price of the house. The estimated intercept of 
-290 is the value of SIZE when PRICE equals zero. The estimated 
intercept is negative, but because the estimate includes the con-
stant value of any omitted variables, any measurement errors, 
and/or an incorrect functional form, we shouldn’t attach any 
importance to the negative sign.
	
b.	No. All we have shown is that a statistical relationship exists 
between the price of a house and its size.
	
c.	 The new slope coefficient would be 0.00362 (or 3.62/1000), but 
nothing else would change.


492
aPPENDIX A
1–6.	
a.	2.29 is the estimated constant term, and it is an estimate of the 
gift when the alum has no income and no calls were made to that 
alum. 0.001 is an estimate of the slope coefficient of INCOME, 
and it tells us how much the gift would be likely to increase 
when the alum’s income increases by a dollar, holding constant 
the number of calls to that alum. 4.62 is an estimate of the slope 
coefficient of CALLS, and it tells us how much the gift would be 
likely to increase if the college made one more call to the alum, 
holding constant the alum’s income. The signs of the estimated 
slope coefficients are as expected, but we typically do not develop 
hypotheses involving constant terms.
	
b.	Once we estimate the equation, the left-hand variable now is the 
estimated value of the dependent variable because the right-hand 
side of the equation also consists of estimated coefficients (in all 
but one case multiplied by independent variables).
	
c.	 An error term is unobservable and couldn’t be included in an 
estimated equation from which we actually calculate a Yn.
	
d.	The 
right-hand 
side 
of 
the 
equation 
would 
become 
2.29 + 1.0INCOME + 4.62CALLS. Nothing has changed except 
the scale of the coefficient of INCOME.
	
e.	 Many good possibilities exist. However, we don’t suggest adding 
“last year’s GIFT” (as tempting as that may seem). While the fit 
would be good, there would be very little analytical content to 
the result.
1–8.	
a.	At first glance, the answer is yes, because both coefficients are 
positive (as we’d expect) and the coefficient of HOT is 59 times 
the size of the coefficient of EASE (as the article predicted). 
However, the variable HOT has a maximum value of 5 while 
the variable EASE has a maximum value of 1, so the two coef-
ficients aren’t directly comparable. In addition, there surely 
are some important variables that have been omitted from this 
equation, and it’s very risky to draw conclusions from regres-
sion results when important variables have been left out. We’ll 
address this topic (omitted variable bias) in more detail in 
Chapter 6.
	
b.	Other possibly important variables include communication 
skills, knowledge of the field, enthusiasm, organization, etc.
	
c.	 Our guess is that the coefficient of HOT would decrease in size 
quite a bit. The coefficient of EASE already is extremely low, so it 
might actually go up.


493
ANSWERS
Chapter 2
2–2.	
a.	 βn 1 = -0.55, βn 0 = 12.29
	
b.	R2 = .46, R  2 = .40
	
c.	 Income = 12.29 - 0.55 (8) = 7.89
2–4.	
a.	Yes. The new coefficient represents the impact of HEIGHT on 
WEIGHT, holding MAIL constant, while the original coefficient 
did not hold MAIL constant. We’d expect the estimated coeffi-
cient to change (at least slightly) because of this new constraint.
	
b.	One weakness of R2 is that adding a variable will usually decrease 
(and will never increase) the summed squared residuals no mat-
ter how nonsensical the variable is. As a result, adding a nonsen-
sical variable will usually increase (and will never decrease) R2.
	
c.	 R  2 is adjusted for degrees of freedom and R2 isn’t, so it’s com-
pletely possible that the two measures could move in opposite 
directions when a variable is added to an equation.
	
d.	The coefficient is indeed equal to zero in theory, but in any 
given sample, MAIL may have some random correlation with 
WEIGHT and therefore may provide some minor explanatory 
power beyond that provided by HEIGHT. In fact, it’s typical to get 
a nonzero estimated coefficient even for nonsensical variables.
2–6.	
	
As we’ll learn in future chapters, there’s a lot more to getting the 
best equation than maximizing R  2. For example, see pp. 55–56.
Chapter 3
3–2.	
a.	 D = 1 if graduate student and D = 0 if undergraduate.
	
b.	Yes; for example, E = how many exercises the student did.
	
c.	 If D is defined as in answer a, then its coefficient’s sign would be 
expected to be positive. If D is defined as 0 if graduate student, 1 
if undergraduate, then the expected sign would be negative.
	
d.	A coefficient with value of 0.5 indicates that holding constant 
the other independent variables in the equation, a graduate stu-
dent would be expected to earn half a grade point higher than an 
undergraduate. If there were only graduate students or only under-
graduates in class, the coefficient of D could not be estimated.
	
e.	 With three categories, use two dummies. It doesn’t matter which 
two you pick.


494
aPPENDIX A
3–4.	
If you need help getting started, see the answer to Exercise 1–2.
3–6.	
a.	All positive except for the coefficient of Fi, which in today’s male-
dominated movie industry probably has a negative expected 
sign. The sign of βn B certainly is unexpected.
	
b.	Fred, because $500,000 6 1$4,000,000 - $3,027,0002.
	
c.	 Yes, since 200 * 15.4 = $3,080,000 7 $1,200,000.
	
d.	Yes, since $1,770,000 7 $1,000,000.
	
e.	 Yes, the unexpected sign of βn B.
Chapter 4
4–2.	
a.	An additional pound of fertilizer per acre will cause corn yield to 
increase by 0.10 bushels per acre, holding rainfall constant. An 
additional inch of rain will increase corn yield by 5.33 bushels 
per acre, holding fertilizer per acre constant.
	
b.	No, for a couple of reasons. First, it’s hard to imagine zero inches 
of rain falling in an entire year, so this particular intercept has no 
real-world meaning. More generally, recall that the OLS estimate 
of the intercept includes the nonzero mean of the error term, so 
even if rainfall were zero, it wouldn’t make sense to attempt to 
analyze the OLS estimate of the intercept.
	
c.	 No. An unbiased estimator will produce a distribution of esti-
mates that is centered around the true β, but individual estimates 
can vary widely from that true value. 0.10 is the estimated coef-
ficient for this sample, not for the entire population, so it could 
be an unbiased estimate.
	
d.	Not necessarily: 5.33 still could be close to or even equal to the 
true value. More generally, an estimated coefficient produced by 
an estimator that is not BLUE still could be accurate. For exam-
ple, the amount of the bias could be very small, or the variation 
due to sampling could offset the bias.
4–4.	
a.	Classical Assumption II.
	
b.	Classical Assumption VI.
	
c.	 R: A one-unit increase in yesterday’s R will result in a 0.1 percent 
increase in today’s Dow Jones average, holding constant the other 
independent variables in the equation.
	
	
M: The Dow Jones will be 0.017 percent lower on a Monday, 
holding constant the other independent variables in the equation.


495
Answers
	
d.	Technically, C is not a dummy variable because it can take on 
three different values. Saunders assumed (at least implicitly) that 
all levels of cloud cover between 0 percent and 20 percent have 
the same impact on the Dow and also that all levels of cloud 
cover between 21 percent and 99 percent have the same impact 
on the Dow. In addition, by using the same variable to represent 
both sunny and cloudy days, the equation constrains the impact 
of 100 percent sunny and 100 percent cloudy to be equal (though 
in opposite directions).
	
e.	 In our opinion, this particular equation does little to support 
Saunders’ conclusion. The poor fit and the constrained specifi-
cation combine to outweigh the significant coefficients of Rt−1 
and M.
4–6.	
a.	The coefficient of DIVSEP implies that a divorced or separated 
individual will drink 2.85 more drinks than otherwise, holding 
constant the other independent variables in the equation. The 
coefficient of UNEMP implies that an unemployed individual 
will drink 14.20 more drinks than otherwise, holding constant 
the other independent variables in the equation. The signs of the 
estimated coefficients make sense, but we wouldn’t have expected 
the coefficient of UNEMP to be five times the size of the coeffi-
cient of DIVSEP.
	
b.	The coefficient of ADVICE implies that an individual will drink 
11.36 more drinks, holding constant the other independent vari-
ables in the equation, if a physician advises them to cut back on 
drinking alcohol. This coefficient certainly has an unexpected 
sign! Our guess is that DRINKS and ADVICE are simultaneously 
determined, since a physician is more likely to advise an indi-
vidual to cut back on their drinking if that individual is drink-
ing quite a bit. As a result, this equation almost surely violates 
­Classical Assumption III. For more, see Chapter 14.
	
c.	 We’d expect each sample to produce different estimates of 
βADVICE. The entire group of sample means is called a sampling 
distribution of βn S.
	
d.	The βn ADVICE for this subsample is 8.62, which is a little lower 
than the coefficient for the entire sample. The other coefficients 
for this subsample differ even more from the coefficients for the 
entire sample, and the estimated coefficient of EDUC actually 
has an unexpected sign. These results are clear evidence of the 
advantages of large samples.


496
aPPENDIX A
Chapter 5
5–2.	
For all three parts:
X1
X2
X3
H0:
β1 … 0
β2 Ú 0
β3 Ú 0
HA:
β1 7 0
β2 6 0
β3 6 0
t1 = 2.1
t2 = 5.6
t3 = -0.1
	
a.	 tc = 1.363. For β1, we reject H0, because t1 7 1.363 and the 
sign of t1 is that implied by HA. For β2, we cannot reject H0, even 
though t2 7 1.363, because the sign of t2 does not agree with 
HA. For β3, we cannot reject H0, even though the sign of t3 agrees 
with HA, because t3 6 1.363.
	
b.	tc = 1.318. The decisions are identical to those in part a, except 
that tc = 1.318.
	
c.	 tc = 3.143. For β1, we cannot reject H0, even though the sign of 
t1 is that implied by HA, because t1 6  3.143. For β2 and β3, 
the decisions are identical to those in parts a and b, except that 
tc = 3.143.
5–4.	
For βN: Reject H0: β … 0, HA: β 7 0, if  -4.42 7 tc and -4.42 
is negative.
	
For βP: Reject H0: β Ú 0, HA: β 6 0, if 4.88 7 tc and 4.88 is 
positive.
	
For βI: Reject H0: β Ú 0, HA: β 6 0, if 2.37 7 tc and 2.37 
is positive.
	
a.	 tc = 1.943; reject the null hypothesis for all three coefficients.
	
b.	tc = 1.311; reject H0 for all three coefficients.
	
c.	 tc = 6.965; cannot reject the null hypothesis for any of the three 
coefficients.
5–6.	
a.	For all three, H0: β … 0,   HA: β 7 0, and the critical 5-percent, 
one-sided t-value for 24 degrees of freedom is 1.711. For LOT, 
we can reject H0 because  +7.0 7 1.711 and +7.0 is positive. 
For BED, we cannot reject H0 because  +1.0 6 1.711 even 
though +1.0 is positive. For BEACH, we can reject H0 because 
 +10.0 7 1.711 and +10.0 is positive.
	
b.	H0: β Ú 0,   HA: β 6 0, and the critical 10-percent, one-sided 
t-value for 24 degrees of freedom is 1.318, so we reject H0 
because  -2.0 7 1.318 and -2.0 is negative.


497
Answers
	
c.	 H0: β = 0,   HA: β ≠0, and the critical 5-percent, two-sided t-value 
for 24 degrees of freedom is 2.064, so we cannot reject H0 because 
 -1.0 6 2.064. Note that we don’t check the sign because the test 
is two-sided and both signs are in the alternative hypothesis.
	
d.	The main concern is the possibility that BED and/or FIRE may be 
irrelevant.
	
e.	 Given that we weren’t sure what sign to expect for the coeffi-
cient of FIRE, the insignificant coefficient for BED is the most 
worrisome.
	
f.	 Unless you’ve read Chapter 6, this will be a difficult question to 
answer. The most likely answer is that BED doesn’t belong in the 
equation if LOT also is in it. Beach houses on large lots tend to 
have more bedrooms than beach houses on small lots.
5–8.	
a.	NEW: H0: β … 0, HA: β 7 0. Reject H0 since 5.34 7 1.658 and 
+5.34 has the sign of HA.
	
	
SCRATCH: H0: β Ú 0, HA: β 6 0. Reject H0 since  -4.00 7 1.658 
and -4.00 has the sign of HA.
	
b.	BIDRS: 
H0: β … 0, HA: β 7 0. 
Cannot 
reject 
H0 
since 
1.23 6 2.358 even though +1.23 has the sign of HA.
	
c. Some econometricians might drop BIDRS from the equation 
because of its low t-score, but we’d be inclined to keep the vari-
able. The theory is strong, and the estimated coefficient is in the 
expected direction. As we’ll see in Chapter 6, consistently drop-
ping variables with low t-scores will result in coefficient bias.
	
d.	Most good variables are attributes of the iPod, but attributes of 
the auction of that iPod (like the length of time of the auction or 
whether there was a “buy it now” option available) also make sense.
	
e.	 Reject H0 (that all three slope coefficients equal zero) because 
55.09 is larger than 2.68, the 5-percent critical F-value with 3 and 
120 degrees of freedom.
Chapter 6
6–2.    a.
Wi
Ti
Ci
Li
H0:
β1 … 0
β2 … 0
β3 … 0
β4 … 0
HA:
β1 7 0
β2 7 0
β3 7 0
β4 7 0
tW = 4
tT = 3
tC = 2
tL = 0.95
tc = 1.697
tc = 1.697
tc = 1.697
tc = 1.697


498
aPPENDIX A
	
	
For the first three coefficients, we can reject the null hypothesis, 
because the absolute value of tk is greater than tc and the sign 
of tk is that specified in HA. For L, however, we cannot reject the 
null hypothesis, even though the sign is as expected, because the 
absolute value of tL is less than 1.697.
	
b.	Almost any equation potentially could have an omitted variable, 
and this one is no exception. In addition, Li might be an irrel-
evant variable. Finally, the coefficient of C seems far too large, 
suggesting at least one omitted variable. C appears to be acting as 
a proxy for other luxury options or the general quality of the car.
	
c.	 Theory: Bigger engines cost more, so the variable’s place in the 
equation seems theoretically sound. However, sedans with large 
engines tend to weigh more, so perhaps the two variables are 
measuring more or less the same thing.
	
	
t-Test: The variable’s estimated coefficient is insignificant in the 
expected direction.
	
	
R  2: The overall fit of the equation (adjusted for degrees of 
­freedom) improves when the variable is dropped from the equation.
	
	
Bias: When the variable is dropped from the equation, the esti-
mated coefficients remain virtually unchanged.
	
	
The last three criteria are evidence in favor of dropping Li and 
the theoretical argument for keeping it isn’t overwhelming, so we 
prefer Model T. However, a researcher who firmly believed in the 
theoretical importance of engine size would pick Model A.
6–4.	
Expected bias = 1βomitted2 # αn 1
	
a.	Expected bias = 1-2 # 1+2 = 1-2 = negative bias. (This assumes 
that peanut butter is a normal good.)
	
b.	1 + 2 # 1 + 2 = 1 + 2 = positive bias; this bias will be potentially 
large since age and experience are highly correlated.
	
c.	 1 + 2 # 1 + 2 = 1 + 2 = positive bias.
	
d.	1 - 2 # 102 = 0 = no bias; it may seem as though it rains more 
on the weekends, but there is no relationship between the two.
6–6.	
a.	 X1 = either dummy variable
	
	
X2 = either dummy variable
	
	
X3 = Parents’ educational background
	
	
X4 = Iowa Test score
	
b.	We have two variables for which we expect positive coefficients 
(Iowa score and Parents’ education) and two positive estimated 
coefficients (βn 3 and βn 4), so we’d certainly expect X3 and X4 to be 


499
Answers
those two variables. Choosing between the two is difficult, but 
we certainly expect the Iowa test score to be more significant. 
Next, we have two variables for which we expect a zero coeffi-
cient (the dummies) and two estimated coefficients (βn 1 and βn 2) 
that are not significantly different from zero, so we’d certainly 
expect X1 and X2 to be the dummies. There is no evidence to 
allow us to distinguish which dummy is X1 and which is X2. (If 
you expected negative signs for the coefficients of the two dum-
mies, note that the presence of the Iowa test score variable in the 
equation should control for any bias in multiple-choice tests 
against females and students of color.)
	
c.	 Coefficient:	
βD	
βD	
βPE	
βIT
	
	
Hypoth. sign:	
0	
0	
+	
+
	
	
t-value:	
-1.0	
-0.25	
+2.0	
+12.0
	
	
tc = 2.093	
do not	
do not
	
	
(5-percent 	
reject	
reject	
	
	
	
two-sided with 19 d.f.)
	
	
tc = 1.729	
	
	
reject	
reject
	
	
(5-percent one-sided 	
	
	
	
	
with 19 d.f.)
	
d.	As you can see, we used a one-sided test for those coefficients for 
which we had a specific prior expectation but a two-sided test 
around zero for those coefficients for which we did not.
6–8.	
a.	 i.  The coefficient of CV is -0.19 with a SE1βn 2 of 0.23.
	
	
	  The R  2 is .773, and the rest of the equation is extremely simi-
lar to Equation 5.15 except that the coefficient of CVN falls to 
-0.48 with a t-score of -1.86.
	
	
ii.  The coefficient of N is 0.00054 with a SE1βn 2 of 0.063. The R  2 
is .766, and the rest of the equation is identical (for all intents 
and purposes) to Equation 5.15.
	
b.	Theory: P is a price ratio, and while it’s possible that a price ratio 
would be a function of the size of a market or a country, 
it’s not at all obvious that either variable would add any-
thing since CVN is already in the equation.
	
	
t-score: Both t-scores are insignificant.
	
	
R  2: R  2 falls when either variable is added.
	
	
bias: None of the coefficients change at all when N is added, so 
it clearly is irrelevant. The omission of CV does change the 
coefficient of CVN somewhat, making it likely that CV is 
redundant since CVN is in the equation.


500
aPPENDIX A
	
c.	 Since CVN = f3CV/N4, it would make little theoretical sense to 
include all three variables in an equation, even though techni-
cally you don’t violate Classical Assumption VI by doing so.
	
d.	It’s good econometric practice to report all estimated equations 
in a research report, especially those that were undertaken for 
specification choice or sensitivity analysis.
Chapter 7
7–2.	
a.	Semilog right; as income increases, the sales of shoes will in-
crease, but at a declining rate.
	
b.	Linear (intercept dummy).
	
c.	 Semilog right or linear are both justifiable.
	
d.	Double-log; some researchers prefer the inverse form mentioned 
in footnote 4 on page 197.
	
e.	 Quadratic function; to show diminishing returns to scale.
7–4.	
a.	To avoid confusion with β, let’s use αs as the coefficients.
	
	
Coefficient	
αBETA	
αEARN	
αDIV
	
	
Hypothesized sign:	
-	
+	
+
	
	
Calculated t-score:	
-1.99	
1.44	
3.33
	
	
tc = 1.671 (5% level), so:	
sig.	
insig.	
sig.
	
b.	It’s unusual to have a lagged variable in a cross-sectional model, 
but in this equation all the variables are for 1996–2000 except 
for BETA, which is for 1958–1994 and therefore is indeed lagged. 
Fair assumed that the risk characteristics of companies don’t 
change rapidly over time and stated that “five observations per 
company is not enough to get trustworthy estimates.” (p. 17)
	
c.	 We don’t believe that any of Fair’s variables are potentially irrel-
evant, because the theory behind each variable is exceptionally 
strong. Some students will think that EARN might be irrelevant 
because its coefficient has a low t-score, but we disagree with this 
concern because earnings growth is one of the most important 
determinants of stock prices. A student who drops EARN should 
conclude, based on the four specification criteria, that the vari-
able belongs in the equation, because three of the four criteria 
support keeping EARN in the equation, and the t-score is close to 
being significant in the expected direction.
	
d.	The functional form is a semi-log left, which is indeed appropri-
ate on a theoretical basis and also because two of the indepen-
dent variables are expressed as percentages.


501
Answers
	
e.	 This optional question is intentionally difficult. EARN and DIV 
both include negative values, so it might seem impossible to run 
the regression. However, since the negative values are extremely 
small, one possible way to estimate the equation is to set all the 
negative values equal to +0.01, obtaining:
	
	
LNPE = 3.23 - 0.19LNBETA + 0.071LNEARN + 0.098LNDIV
	
	
	
	
10.112	
10.0352	
10.0282
	
	
	
t = -1.69	
2.02	
3.49
	
	
	
N = 65	
R  2 = .23
	
	
However, these results, while completely reasonable, shed very 
little light on whether to use a double-log functional form, 
because we urge researchers to focus on theory, and not fit, to 
choose their functional forms. We think that Fair’s choice of a 
semi-log left is supported by the literature and by the fact that 
two of the independent variables are expressed in percentage 
growth terms.
7–6.	
a.	polynomial (second-degree, with a negative expected coefficient 
for age and a positive expected coefficient for age squared)
	
b.	double-log (We would not quibble with those who chose a linear 
form to avoid the constant elasticity properties of a double-log.)
	
c.	 semilog (lnX)
	
d.	linear (All intercept dummies have a linear functional relation-
ship with the dependent variable by definition.)
7–8.	
a.	Coefficient	
βB	
βS	
βD
	
	
Hypothesized sign:	
+	
+	
-
	
	
Calculated t-score:	
-0.08	
1.85	
-1.29
	
	
tc = 1.682, so:	
insig.	
sig.	
insig.
	
	
The insignificance of βn B could be caused by an omitted variable, 
but it’s likely that the interaction variable has “soaked up” the 
entire effect of beer consumption. Although we cannot reject the 
null hypothesis for βn D, we see no reason to consider D to be an 
irrelevant variable because of its sound theory and reasonable 
statistics.
	
b.	The interaction variable is a measure of whether the impact of 
beer drinking on traffic fatalities rises as the altitude of the city 
rises. For each unit increase in the multiple of B and A, F rises by 
0.011, holding constant all the other independent variables in the 
equation. Thus, the size of the coefficient has no real intuitive 
meaning in and of itself.
h


502
aPPENDIX A
	
c.	 H0: βBA … 0
	
	
HA: βBA 7 0
	
	
Reject H0 because  +4.05 7 tc = 1.682 and 4.05 is positive and 
thus matches the sign implied by HA.
	
d.	Although there is no ironclad rule (as there is with slope 
­dummies) most econometricians include both interaction-term 
components as independent variables. The major reason for this 
practice is to avoid the possibility that an interaction term’s coef-
ficient might be significant only because it is picking up the effect 
of the omitted interaction-term component.
	
e.	 The exception to this general practice occurs when there is no 
reason to expect the interaction-term component to have any 
theoretical validity on its own. We prefer Equation 7.22 to 
7.23 because we don’t believe that altitude typically would be 
included as an independent variable in a highway fatality equa-
tion. Of our other three specification criteria, only the increase 
in R  2 supports considering A to be a relevant variable. However, 
even moderate theoretical support for the inclusion of A on its 
own would result in our preferring Equation 7.23.
Chapter 8
8–2.	
a.		
EMPi	
UNITSi	
LANGi	
EXPi
	
	
H0	
β1 … 0	
β2 … 0	
β3 … 0	
β4 … 0
	
	
HA	
β1 7 0	
β2 7 0	
β3 7 0	
β4 7 0
	
	
	
tEM = -.098	
tU = 2.39	
tL = 2.08	
tEX =  4.97
	
	
	
tc = 1.725	
tc = 1.725	
tc = 1.725	
tc = 1.725
	
	
For the last three coefficients, we can reject H0, because the 
­absolute value of tk is greater than tc and the sign of tk is that 
specified in HA. For EMP, however, we cannot reject H0, because 
the sign of the coefficient is unexpected and because the absolute 
value of tEM is less than 1.725.
	
b.	The functional form is semilog left (or semilog lnY). Semilog 
left is an appropriate functional form for an equation with sal-
ary as the dependent variable, because salaries often increase in 
percentage terms when an independent variable (like experience) 
increases by one unit.
	
c.	 There’s a chance that an omitted variable is pulling down the 
coefficient of EMP, but it’s more likely that EMP and EXP are 
redundant (because in essence they measure the same thing) and 
are causing multicollinearity.


503
Answers
	
d.	This lends support to our opinion that EMPi and EXPi are 
redundant.
	
e.	 If we knew that this particular school district didn’t give credit for 
teaching experience elsewhere, then it would make sense to drop 
EXP. Without that specific knowledge, however, we’d drop EMP 
because EXP includes EMP.
	
f.	 Theory: EMP clearly has a theoretically strong impact on salary, 
but EMP and EXP are redundant, so we should keep only one.
	
	
t-Test: The variable’s estimated coefficient is insignificant in the 
unexpected direction.
	
	
R2: The overall fit of the equation (adjusted for degrees of 
­freedom) improves when the variable is dropped from the 
equation.
	
	
Bias: The exercise gives t-scores only, but if you work back-
ward, you can calculate the SE1βn 2s. If you do this, you’ll find 
that the coefficient of EXP does indeed change by more than a 
standard error when EMP is dropped from the equation. This 
is exactly what you’d expect to happen when a redundant vari-
able is dropped from an equation; the coefficient of the remain-
ing redundant variable will adjust to pick up the effect of both 
variables.
	
	
    Thus even though it might appear that two of the specifica-
tion criteria support keeping EMP in the equation, in actuality all 
four support the conclusion that they’re redundant and that EMP 
should be removed. As a result, we have a strong preference for 
Equation 8.22 over Equation 8.21.
8-4.	
Dominant variables are likely in a and d. In a, the number of 
games won should equal the number of games played (which is 
a ­constant) minus the number of games lost. In d, the number of 
autos produced should equal four times the number of tires bought 
(if no spare is sold with the cars or five if a spare is included).
8–6.	
a.	Coefficient:	
βM	
βB	
βA	
βS
	
	
Hypoth. sign:	
+	
+	
+	
+
	
	
t-value:	
5.0	
1.0	
−1.0	
2.5
	
	
tc = 1.645	
reject	
do not	
do not	
reject
	
	
(5% one-sided	
	
reject	
reject 
	
	
with infinite d.f.)
	
b.	The insignificant t-scores of the coefficients of A and B could have 
been caused by omitted variables, irrelevance, or multicollinearity 


504
aPPENDIX A
(a good choice, since that’s the topic of this chapter). Since many 
MBA students are in their 20s, the collinearity between A and B 
must be fairly spectacular (Stanford gave us no clues). In addi-
tion, experienced econometricians would be concerned that the 
dependent variable is “truncated” because it can’t be higher than 
4.0. This implies that the equation should have been estimated 
by a technique (similar to those we cover in Chapter 13) that is 
unfortunately beyond the scope of this text.
	
c.	 It’s probably a good idea, since the improvement in GPA caused 
by extra maturity may eventually be offset by a worsening in GPA 
due to separation from an academic environment.
	
d.	We believe in making just one change at a time to best analyze 
the impact of each change on the estimated regression. Thus, our 
first choice would be to drop either A or B (we’d prefer to drop 
A, but on theoretical grounds, not as a result of the unexpected 
sign). Switching to a polynomial before dropping one of the 
redundant variables will only make things worse, in our opinion.
Chapter 8
Hints for the SAT Interactive Regression Learning Exercise
	
1.	Severe multicollinearity between APMATH and APENG is the 
only possible problem in this regression. You should switch to 
the AP linear combination immediately.
	
2.	An omitted variable is a distinct possibility, but be sure to choose 
the one to add on the basis of theory.
	
3.	Either an omitted or irrelevant variable is a possibility. In this 
case, theory seems more important than any mild statistical 
­insignificance.
	
4.	On balance, this is a reasonable regression. We see no reason to 
worry about theoretically sound variables that have slightly in-
significant coefficients with expected signs. We’re concerned that 
the coefficient of GEND seems larger in absolute size than those 
reported in the literature, but none of the specification alterna-
tives seems remotely likely to remedy this problem.
	
5.	An omitted variable is a possibility, but there are no signs of bias 
and this is a fairly reasonable equation already.
	
6.	We’d prefer not to add PREP (since many students take prep 
courses because they did poorly on their first shots at the SAT) or 


505
Answers
RACE (because of its redundancy with ESL and the lack of real 
diversity at Arcadia High). If you make a specification change, be 
sure to evaluate the change with our four specification criteria.
	
7.	Either an omitted or irrelevant variable is a possibility, although 
GEND seems theoretically and statistically strong.
	
8.	The unexpected sign makes us concerned with the possibility that 
an omitted variable is causing bias or that PREP is irrelevant. If 
PREP is relevant, what omission could have caused this result? 
How strong is the theory behind PREP?
	
9.	This is a case of imperfect multicollinearity. Even though the VIFs 
are only between 3.8 and 4.0, the definitions of ESL and RACE 
(and the high simple correlation coefficient between them) make 
them seem like redundant variables. Remember to use theory 
(and not statistical fit) to decide which one to drop.
	
10.	An omitted variable or irrelevant variable is a possibility, but 
there are no signs of bias and this is a fairly reasonable equation 
already.
	
11.	Despite the switch to the AP linear combination, we still have an 
unexpected sign, so we’re still concerned with the possibility that 
an omitted variable is causing bias or that PREP is irrelevant. If 
PREP is relevant, what omission could have caused this result? 
How strong is the theory behind PREP?
	
12.	All of the choices would improve this equation except switching 
to the AP linear combination. If you make a specification change, 
be sure to evaluate the change with our four specification criteria.
	
13.	To get to this result, you had to have made at least three suspect 
specification decisions, and you’re running the risk of bias due 
to a sequential specification search. Our advice is to stop, take a 
break, review Chapters 6–8, and then try this interactive exercise 
again.
	
14.	We’d prefer not to add PREP (since many students take prep 
courses because they did poorly on their first shots at the SAT) or 
ESL (because of its redundancy with RACE and the lack of real 
diversity at Arcadia High). If you make a specification change, be 
sure to evaluate the change with our four specification criteria.
	
15.	Unless you drop one of the redundant variables, you’re going to 
continue to have severe multicollinearity.
	
16.	From theory and from the results, it seems as if the decision to 
switch to the AP linear combination was a waste of a regression 
run. Even if there were severe collinearity between APMATH 
and APENG (which there isn’t), the original coefficients are 


506
APPENDIX A
­significant enough in the expected direction to suggest taking no 
action to offset any multicollinearity.
	
17.	On reflection, PREP probably should not have been chosen in 
the first place. Many students take prep courses only because 
they did poorly on their first shots at the SAT or because they 
anticipate doing poorly. Thus, even if the PREP courses improve 
SAT scores, which they probably do, the students who think they 
need to take them were otherwise going to score worse than their 
colleagues (holding the other variables in the equation constant). 
The two effects seem likely to offset each other, making PREP an 
irrelevant variable. If you make a specification change, be sure to 
evaluate the change with our four specification criteria.
	
18.	Either adding GEND or dropping PREP would be a good choice, 
and it’s hard to choose between the two. If you make a specifica-
tion change, be sure to evaluate the change with our four specifi-
cation criteria.
	
19.	On balance, this is a reasonable regression. We’d prefer not to 
add PREP (since many students take prep courses because they 
did poorly on their first shots at the SAT), but the theoretical case 
for ESL (or RACE) seems strong. We’re concerned that the coef-
ficient of GEND seems larger in absolute size than those reported 
in the literature, but none of the specification alternatives seems 
remotely likely to remedy this problem. If you make a specifica-
tion change, be sure to evaluate the change with our four specifi-
cation criteria.
Chapter 9
9–2.	
a.		
lnYt	
PBt	
PRPt	
Dt
	
	
H0	
β1 … 0	
β2 Ú 0	
β3 … 0	
β4 Ú 0
	
	
HA	
β1 7 0	
β2 6 0	
β3 7 0	
β4 6 0
	
	
	
tY = 6.6	
tPB = -2.6	
tPRP = 2.7	
tD = -3.17
	
	
	
tc = 1.714	
tc = 1.714	
tc = 1.714	 tc = 1.714
	
	
We can reject the null hypothesis for all four coefficients because 
the t-scores all are in the expected direction with absolute values 
greater than 1.714 (the 5-percent one-sided critical t-value for 23 
degrees of freedom).
	
b.	With a 5-percent, one-sided test and N = 28, K = 4, the critical 
values are dL = 1.10 and dU = 1.75. Since d = 0.94 6 1.10, we 
can reject the null hypothesis of no positive serial correlation.


507
Answers
	
c.	 The probable serial correlation suggests GLS or Newey-West.
	
d.	We prefer the GLS equation to OLS, because we’ve rid the equa-
tion of much of the serial correlation while retaining estimated 
coefficients that make economic sense. Note that the dependent 
variables in the two equations are different, so an improved fit is 
not evidence of a better equation.
9–4.	
a.	Except for the first and last observations in the sample, the DW 
test’s ability to detect first-order serial correlation is unchanged.
	
b.	GLS can be applied mechanically to correct for serial correlation, 
but this procedure generally does not make sense; this time’s 
error term is now hypothesized to be a function of next time’s 
error term.
	
c.	 First-order serial correlation in data that have been entered in 
reverse chronological order means that this time’s observation 
of the error term is a function of next time’s, which would be 
very unusual. This might occur if decision makers are able to 
accurately predict and adjust to future random events before they 
occur (which would be the case in a world of rational expecta-
tions and perfect future information).
9–6.	
a.	Equation 9.29:
	
	
Coefficient:	
β1	
β2	
β3
	
	
Hypothesized sign:	
+	
+	
+
	
	
Calculated t-score:	
0.76	
14.98	
1.80
	
	
tc = 1.721, so:	
insig.	
sig.	
sig.
	
	
Equation 9.30:
	
	
Coefficient:	
β1	
β2
	
	
Hypothesized sign:	
+	
+
	
	
Calculated t-score:	
1.44	
28.09
	
	
tc = 1.717, so:	
insig.	
sig.
	
b.	The three statistical specification criteria imply that SP is a rel-
evant variable: R  2 increases when SP is added, SP’s coefficient is 
significantly different from zero, and the estimated coefficient of 
SY changes by more than one standard error. However, the sign 
of the coefficient of SP is an issue. Many researchers would expect 
the sign of βn 3 to be negative (an idea supported by the fact that 
the authors obtained a negative sign for the subset of the sample 
from 1960 to 1976), but the authors explain a positive sign by 
stating that the Soviet leadership became “more competitive” 


508
aPPENDIX A
after 1977, leading the USSR to increase defense spending as SP 
increased.
	
c.	 For both equations, DW is far below the critical value for a 
­5-percent one-sided test, so we can reject the null hypothesis of 
no positive serial correlation. (For Equation 9.29, 0.49 6 1.12, 
and for Equation 9.30, 0.43 6 1.21.) This result raises the pos-
sibility that βn 3’s t-score might be inflated, making it possible that 
SP is an irrelevant variable.
	
d.	Such a small improvement in the DW statistic is no evidence 
whatsoever that the serial correlation is impure.
	
e.	 Just as we suspected, running GLS makes βn 3 insignificant, resulting 
in it being even more likely that lnSP is an irrelevant variable.
Chapter 10
10–2.	
a.	Yes, heteroskedasticity is much more likely when CV is the de-
pendent variable than it is when P is the dependent variable, 
because the aggregate consumption of pharmaceuticals will vary 
much more widely by country than will the prices of those 
­pharmaceuticals.
	
b.	Breusch–Pagan Test: NR2 = 10.91 7 7.81, so we can reject the 
null hypothesis of homoskedasticity.
	
	
White Test: NR2 = 28.62 7 the critical chi-square value of 15.51, 
so we can reject the null hypothesis of homoskedasticity. 15.51 is 
the critical value because there are only eight degrees of freedom 
because PC is a dummy variable.
	
c.	 The HC standard error for N is 0.107; for P it is 0.127; and for PC 
it is 10.61.
	
d.	lnCVi = -8.21 + 1.11lnNi + 1.46lnPi + 0.88PCi
	
	
	
	
10.142	
10.442	
10.482
	
	
t	
= 	
7.94	
3.30	
1.82
	
	
	
N = 32	
R  2 = .71
	
e.	 CVNi = 10.89 + 1.17GDPNi - 0.36Pi - 1.95PCi
	
	
	
10.132	
10.112	 15.522
	
	
t	
= 	
9.22	
-3.23	
-0.35
	
	
	
N = 32	
R  2 = .80
	
	
where CVN = CV/N and GDPN = GDP/N.
	
f.	 Most experienced econometricians use HC standard errors to 
deal with heteroskedasticity, so the most obvious answer is to 
choose that approach.
h
h


509
Answers
	
g.	Although Classical Assumption V is the focus of this chapter, we 
also have to worry about violating Classical Assumption III in 
this situation. If P is a function of CV and if CV is a function of 
P, then we have a simultaneous system, and the error term is no 
longer independent of the explanatory variables. For more on 
this, see Chapter 14.
10–4.	
a.	 COi = 1273.2 + 0.720Ii	
	
10.0442
	
t = 16.21	
R  2 = .97
	
	
where: CO = average consumption
	
	
	
I = average income.
	
b.	NR2 = 3.00 6 3.84, so we cannot reject the null hypothesis of 
homoskedasticity.
	
c.	 The White test does not agree with the Breusch–Pagan test result.
	
d.	Most econometricians would consider HC standard errors if 
the Breusch–Pagan test or White test indicated heteroskedastic-
ity. In this case, however, there’s another reason for considering 
HC standard errors. The ranges of the income brackets are not 
constant in Ando and Modigliani’s dataset, so the variables are 
means of ranges of differing widths. Thus it would seem reason-
able to think that different range widths might produce different 
variances for the error term, making heteroskedasticity even more 
likely.
10–6.	
a.	Coefficient:	
βP	
βI	
βQ	
βA	
βS	
βT
	
	
Hypoth. sign:	
-	
+	
+	
+	
-	
+?
	
	
t-value:	
-0.97	
6.43	 3.62	
1.93	
1.6	
-2.85
	
	
tc = 1.684	
do not	 reject	 reject	 reject	 do not	 do not
	
	
(5-percent	
reject	
	
	
	
reject	
reject
	
	
one-sided with  
	
	
40 d.f., closest to 43)
	
	
The expected signs for the coefficients of the last two variables 
are tricky. Our opinion is that having more suburban newspa-
pers should hurt metropolitan newspaper circulation but that 
the number of television stations is a measure more of the size 
of a city than of the competition a newspaper faces. By the way, 
we see Q as a proxy for quality and A as an endogenous variable 
(note that the authors did indeed estimate the equation with 
2SLS, a technique that covered in Chapter 14).
8


510
aPPENDIX A
	
b.	Heteroskedasticity seems extremely likely, since larger cities will 
have larger newspaper circulation, leading to larger error term 
variances, and it turns out that we can indeed reject the null 
hypothesis of homoskedasticity.
	
c.	 Heteroskedasticity, multicollinearity, and omitted variables all 
seem likely.
	
d.	While it’s tempting to reformulate the equation by making 
the dependent variable per capita circulation, this probably 
would lessen the equation’s usefulness. Instead, we would try 
to improve the specification. Reasonable possibilities include 
attempting to reduce some of the multicollinearity (redundancy) 
among the independent variables, trying to find a better measure 
of quality than the number of editorial personnel, and substitut-
ing the number of major metropolitan newspaper competitors 
for S and T.
Chapter 11
Hints for the Housing Price Interactive Exercise
	
The biggest problem most students have with this interactive ex-
ercise is that they run far too many different specifications “just to 
see” what the results look like. In our opinion, all but one or two of 
the specification decisions involved in this exercise should be made 
before the first regression is estimated, so one measure of the qual-
ity of your work is the number of different equations you estimated. 
Typically, the fewer the better.
	
  As to which specification to run, most of the decisions involved 
are matters of personal choice and experience. Our favorite model 
on theoretical grounds is:
	
+	
-	
-	
+	
+	
+
Pi =  β0 +  β1Si +  β2Ni +  β3Ai +  β4A2
i  +  β5Yi +  β6CAi +  ei
	
We think that BE and BA are redundant with S. In addition, we can 
justify both positive and negative coefficients for SP, giving it an 
ambiguous expected sign, so we’d avoid including it. We would not 
quibble with someone who preferred a linear functional form for 
A to our quadratic. In addition, we recognize that CA is quite insig-
nificant for this sample, but we’d retain it, at least in part because it 
gets quite hot in Monrovia in the summer.


511
ANSWERS
	
  As to interactive variables, the only one we can justify is between 
S and N. Note, however, that the proper variable is not S # N but 
instead is S # (5 - N), or something similar, to account for the differ-
ent expected signs. This variable turns out to improve the fit while 
being quite collinear (redundant) with N and S.
	
  In none of our specifications did we find evidence of serial cor-
relation or heteroskedasticity, although the latter is certainly a pos-
sibility in such cross-sectional data.
Chapter 12
12–2.	
a.	The double-log functional form doesn’t change the fact that this 
is a dynamic model. As a result, Y and M almost surely are related 
by a distributed lag.
	
b.	In their relationship to M, both Y and R have the same distrib-
uted lag pattern over time, since the λn  of 0.60 applies to both. 
(The equation is in double-log form, so technically the relation-
ships are between the logs of those variables.)
	
c.	 Serial correlation is always a concern in a dynamic model. Many 
students will look at the Durbin–Watson statistic of 1.80 and 
conclude that there is no evidence of positive serial correlation 
in this equation, but that statistic is biased toward 2 in the pres-
ence of a lagged dependent variable. Ideally, we would use the 
Lagrange Multiplier Serial Correlation Test, but we don’t have 
the data to do so. Durbin’s h test, which is beyond the scope of 
this text, provides evidence that there is indeed serial correlation 
in the equation. For more, see Robert Raynor, “Testing for Serial 
Correlation in the Presence of Lagged Dependent Variables,” The 
Review of Economics and Statistics, Vol. 75, No. 4, pp. 716–721.
12–4.	
LM = NR2 = 24*0.0056 = 0.134 6 3.84 = 5-percent critical chi-
square value with one degree of freedom, so we cannot reject the 
null hypothesis of no serial correlation.
Chapter 13
13–2.	
a.	WN: The log of the odds that a woman has used a recognized form 
of birth control is 2.03 higher if she doesn’t want any more chil-
dren than it is if she wants more children, holding ME constant.


512
aPPENDIX A
	
	
ME: A one-unit increase in the number of methods of birth con-
trol known to a woman increases the log of the odds that she has 
used a form of birth control by 1.45, holding WN constant.
	
	
LPM: If the model were a linear probability model, then each 
individual slope coefficient would represent the impact of a one-
unit increase in the independent variable on the probability that 
the ith woman had ever used a recognized form of birth control, 
holding the other independent variable constant.
	
b.	Yes, but we didn’t expect βn ME to be more significant than βn WN.
	
c.	 As we’ve said before, β0 has virtually no theoretical significance. 
See Section 7.1.
	
d.	We’d add one of a number of potentially relevant variables; for 
instance, the educational level of the ith woman, whether the ith 
woman lives in a rural area, and so on.
13–4.	
a.	There are only two women in the sample who are over 65, and 
both of them are out of the workforce. Because this causes a near 
singular matrix, most Logit programs, including Stata’s, will not 
be able to estimate this equation.
	
b.	In both models, the coefficient of A is insignificantly different 
from zero, R  2
P falls when A is added, and the other coefficients 
don’t change by a standard error when A is added. As a result, 
you’d include A in the equation only if you believe it clearly 
belongs there on the basis of theory.
	
a.	 Dn i = - 0.22 - 0.38Mi - 0.001Ai + 0.09Si
	
	
	
10.162	
10.0072	 10.042
	
	
	
t = -2.43	
-0.14	
2.42
	
	
	
R  2 = .29	
N = 30	
R  2
p = .806
	
b.	ln3Di/11 - Di24 = -5.27 - 2.61Mi - 0.01Ai + 0.67Si
	
	
	
11.202	
10.042	 10.322
	
	
	
-2.17	
-0.25	
2.10
	
	
	
R  2
p = .76
Chapter 14
14–2.	
a.	If e2 decreases, Y2 decreases and then Y1 decreases.
	
b.	If eD increases, QD increases, and then QS increases (equilibrium 
condition) and Pt increases. (Remember that the variables are 
simultaneously determined, so it doesn’t matter which one is on 
the left-hand side.)
∏


513
Answers
	
c.	 If e1 increases, CO increases, and then Y increases and YD 
increases.
14–4.	
a.	There are three predetermined variables in the system, and both 
equations have three slope coefficients, so both equations are 
exactly identified. (If the model specified that the price of beef 
was determined jointly with the price and quantity of chicken, 
then it would not be predetermined, and the equations would be 
­underidentified.)
	
b.	There are two predetermined variables in the system, and both 
equations have two slope coefficients, so both equations are 
exactly identified.
	
c.	 There are seven predetermined variables in the system, and there 
are three slope coefficients in both equations, so the first two 
equations are overidentified. Note that we don’t worry about the 
identification properties of the third equation because it isn’t 
part of the simultaneous system.
	
d.	There are five predetermined variables in the system, and there 
are three, two, and four slope coefficients in the first, second, 
and third equations, respectively, so all three equations are 
overidentified.
14–6.	
a.	OLS estimation will still encounter simultaneity bias because 
price and quantity are simultaneously determined. Not all en-
dogenous variables will appear on the left-hand side of a struc-
tural equation.
	
b.	The direction of the bias depends on the correlation between the 
error term and the right-hand-side endogenous variable. If the 
correlation between the error term and price is positive, as it most 
likely is, then the simultaneity bias will also be positive.
	
c.	 Three: stage one: P as a function of YD and W
	
	
stage two: QD as a function of Pn and YD: QS as a function of Pn and W
	
d.	OLS:  Qn D = 57.3 - 0.86P + 1.03YD
	
	
	
 Qn S = 167.5 + 3.95P - 1.42W
	
	
2SLS: Qn D = 95.1 - 6.11Pn + 2.71YD
	
	
	
Qn S = 480.2 + 13.5Pn - 5.50W
Chapter 15
15–2.	
a.	$310,120.00
	
b.	117,276; 132,863; 107,287; Nowheresville


514
APPENDIX A
15–4.	
a.	P isn’t a dummy variable. Instead, it’s a variable whose main function 
is to be multiplied by other variables so that the sign of the resulting 
interaction variable changes depending on the incumbent’s party.
	
b.	The interaction variables were required because the dependent 
variable measures the percentage of votes won by the Democrats, 
but the independent variables measure items that support (or 
damage) public support for the incumbent party. For example, if a 
Democrat is in office in a time of high growth, that growth should 
increase the share of votes won by Democrats, so a positive sign 
makes sense. However, if a Republican is in office in a time of high 
growth, the growth should decrease the share of votes won by the 
Democrats, so a negative sign makes sense. Multiplying GROWTH 
by +1 if the incumbent is a Democrat and -1 if the incumbent is 
a Republican (by using P) is a way of accomplishing this goal.
	
c.	
VOTE = 48.70 + 8.183P - 1.845DUR*P + 0.087DOW*P + 0.535GROWTH*P
	
	
	
12.3962	 10.8432	
10.0702	
10.1972
	
t = 	 	
3.42	
-2.19	
1.25	
2.71
	
-0.762INFLATION*P + 0.040ARMY*P - 0.078SPEND*P
	
10.3632	
10.0342	
10.0362
	
-2.10	
1.15	
-2.18
	
N = 21  R  2 = .77  DW = 2.20
	
d.	The coefficient of DUR*P is negative, while the coefficient of 
ARMY*P is positive, both opposite of their expected signs. The 
coefficients of the other interactive terms have the expected signs. 
We can reject the null hypotheses for P (assuming a positive 
expected sign), GROWTH*P, INFLATION*P, and SPEND*P. We 
cannot reject for DUR*P, DOW*P, and ARMY*P.
	
e.	 Plugging the actual values for 2000 into the equation, we get a 
forecast of 52.740, which is 2.475 percentage points higher than 
the actual 50.265. For 2004, we get a forecast of 44.280, which is 
4.306 percentage points below the actual 48.586.
	
f.	 To do this, we should estimate Equation 15.20 with data through 
2004, producing:
VOTE = 48.76 + 7.340P - 1.659DUR*P + 0.116DOW*P + 0.496GROWTH*P
	
12.2082	
10.8122	
10.0642	
10.1892
	
t = 	 3.32	
-2.04	
1.80	
2.63
	
-0.727INFLATION*P + 0.039ARMY*P - 0.081SPEND*P
	
10.3422	
10.0342	
10.0342
	
-2.13	
1.14	
-2.36
	
	
	 N = 23	
R  2 = .75	
DW = 2.23
h
h


515
Answers
	
	
Plugging the actual values for 2008 into this equation, we get 
a forecast of 42.892, surprisingly below the share that Barack 
Obama actually earned.
Chapter 16
16–2.	
a.	 ∆OUTCOMEEaston = 28,500 - 25,000 = 3,500
	
	
∆OUTCOMEAllentown = 23,750 - 22,500 = 1,250
	
b.	We must assume that the changes in the outcome would have 
been the same in both the treatment and control group (had 
there been no treatment) in order for this estimation to be valid. 
However, there was a $2,500 disparity between the average 
incomes prior to the treatment, so there most likely are several 
differences between the two groups.
	
c.	 Even if the underlying assumption in part b is met, we should be 
cautious when interpreting our conclusions. A data set with only 
two observations is absurdly small and is unlikely to provide 
accurate results except by chance.
16–4.	
a.	This is a natural experiment dataset that also happens to be a 
panel dataset because it contains observations on the same vari-
able from the same cross-sectional sample from two different 
time periods.
	
b.	The appropriate technique is the difference-in-differences estima-
tor, resulting in:
	
	
∆SMOKE = -2.43 - 0.73TAX
	
	
	
10.572
	
	
	
t = 	
-1.29
	
	
	
N = 45	
R  2 = .015
	
c.	 The estimated coefficient is almost significant in the expected 
direction, but the fit is terrible. Most experienced researchers 
won’t be surprised by this result, because of the design of the 
research. In particular, it seems extremely optimistic to expect 
to explain cigarette consumption by state using a dummy for 
whether the cigarette tax rate increased as the only independent 
variable. Variables other than tax rates certainly play a role, as 
does the fact that some states increased cigarette taxes by substan-
tially more than did others, and yet that information is lost if you 
limit yourself to a dummy variable, since it tells you only whether 
taxes increased, not the amount by which they increased.
®


516
aPPENDIX A
16–6.	
a.	 ∆Q = 0.039 - 0.025∆P
	
	
	
(0.002)
	
	
	
t = 	
-12.33
	
	
	 N = 4	
R 2 = .98
	
b.	Fixed effects and differencing produce identical results for the 
coefficient and standard error on the price variable. The fixed 
effect approach, however, produces estimates for coefficients 
on time and entity dummy variables. The adjusted R-squared 
will also differ. But since the variables of interest should be the 
same in the differencing and fixed effect approaches, the identi-
cal results for the price variable produced by the two methods is 
reassuring. They produce identical answers.
	
c.	 The error term in the differencing model certainly appears to be 
defined in such a way as to be serially correlated.
8


517
Statistical Tables
Appendix B
The following tables present the critical values of various statistics used pri-
marily for hypothesis testing. The primary applications of each statistic are 
explained and illustrated. The tables are:
B-1	
Critical Values of the t-Distribution
B-2	
Critical Values of the F-Statistic: 5-Percent Level of Significance
B-3	
Critical Values of the F-Statistic: 1-Percent Level of Significance
B-4	
Critical Values of the Durbin–Watson Test Statistics dL and dU
B-5	
The Normal Distribution
B-6	
The Chi-Square Distribution


518
aPPENDIX B
Table B-1: The t-Distribution
The t-distribution is used in regression analysis to test whether an estimated 
slope coefficient (say, βn k) is significantly different from a hypothesized value 
(such as βH0). The t-statistic is computed as:
tk = 1βn k - βH02/SE1βn k2
where βn k is the estimated slope coefficient and SE1βn k2 is the estimated stan-
dard error of βn k. To test the one-sided hypothesis:
 H0: βk … βH0
 HA: βk 7 βH0
the computed t-value is compared with a critical t-value tc, found in the t-table 
on the opposite page in the column with the desired level of significance 
for a one-sided test (usually 5 percent) and the row with N - K - 1 degrees 
of freedom, where N is the number of observations and K is the number of 
explanatory variables. If 0 tk0 7 tc and if tk has the sign implied by the alterna-
tive hypothesis, then reject H0; otherwise, do not reject H0. In most econo-
metric applications, βH0 is zero and most computer regression programs will 
calculate tk for βH0 = 0. For example, for a 5-percent one-sided test with 15 
degrees of freedom, tc = 1.753, so any positive tk larger than 1.753 would 
lead us to reject H0 and declare that βn k is statistically significant in the hy-
pothesized direction at the 5-percent level.
For a two-sided test, H0: βk = βH0 and HA: βk ≠βH0, the procedure is 
identical except that the column corresponding to the two-sided level of sig-
nificance is used. For example, for a 5-percent two-sided test with 15 degrees 
of freedom, tc = 2.131, so any tk larger in absolute value than 2.131 would 
lead us to reject H0 and declare that βn k is significantly different from βH0 at 
the 5-percent level of significance. For more on the t-test, see Chapter 5.


519
Statistical Tables
Table B-1  Critical Values of the t-Distribution
Level of Significance
Degrees of 
Freedom
One-Sided: 10% 
Two-Sided: 20%
5% 
10%
2.5% 
5%
1% 
2%
0.5% 
1%
  1
3.078
6.314
12.706
31.821
63.657
  2
1.886
2.920
4.303
6.965
9.925
  3
1.638
2.353
3.182
4.541
5.841
  4
1.533
2.132
2.776
3.747
4.604
  5
1.476
2.015
2.571
3.365
4.032
  6
1.440
1.943
2.447
3.143
3.707
  7
1.415
1.895
2.365
2.998
3.499
  8
1.397
1.860
2.306
2.896
3.355
  9
1.383
1.833
2.262
2.821
3.250
10
1.372
1.812
2.228
2.764
3.169
11
1.363
1.796
2.201
2.718
3.106
12
1.356
1.782
2.179
2.681
3.055
13
1.350
1.771
2.160
2.650
3.012
14
1.345
1.761
2.145
2.624
2.977
15
1.341
1.753
2.131
2.602
2.947
16
1.337
1.746
2.120
2.583
2.921
17
1.333
1.740
2.110
2.567
2.898
18
1.330
1.734
2.101
2.552
2.878
19
1.328
1.729
2.093
2.539
2.861
20
1.325
1.725
2.086
2.528
2.845
21
1.323
1.721
2.080
2.518
2.831
22
1.321
1.717
2.074
2.508
2.819
23
1.319
1.714
2.069
2.500
2.807
24
1.318
1.711
2.064
2.492
2.797
25
1.316
1.708
2.060
2.485
2.787
26
1.315
1.706
2.056
2.479
2.779
27
1.314
1.703
2.052
2.473
2.771
28
1.313
1.701
2.048
2.467
2.763
29
1.311
1.699
2.045
2.462
2.756
30
1.310
1.697
2.042
2.457
2.750
40
1.303
1.684
2.021
2.423
2.704
60
1.296
1.671
2.000
2.390
2.660
120
1.289
1.658
1.980
2.358
2.617
(Normal)
∞
1.282
1.645
1.960
2.326
2.576
Source: Reprinted from Table IV in Sir Ronald A. Fisher, Statistical Methods for Research 
Workers, 14th ed. (copyright © 1970, University of Adelaide) with permission of Hafner, a  
division of the Macmillan Publishing Company, Inc.


520
aPPENDIX B
Table B-2: The F-Distribution
The F-distribution is used in regression analysis to deal with a null hypoth-
esis that contains multiple hypotheses or a single hypothesis about a group 
of coefficients. To test the most typical joint hypothesis (a test of the overall 
significance of the regression):
 H0: β1 = β2 = g
  = βK = 0
 HA: H0 is not true
the computed F-value is compared with a critical F-value, found in one of 
the two tables that follow. The F-statistic has two types of degrees of free-
dom, one for the numerator (columns) and one for the denominator (rows). 
For the null and alternative hypotheses above, there are K numerator (the 
number of restrictions implied by the null hypothesis) and N - K - 1 de-
nominator degrees of freedom, where N is the number of observations and 
K is the number of explanatory variables in the equation. This particular F-
statistic is printed out by most computer regression programs. For example, 
if K = 5 and N = 30, there are 5 numerator and 24 denominator degrees 
of freedom, and the critical F-value for a 5-percent level of significance 
(Table B-2) is 2.62. A computed F-value greater than 2.62 would lead us to 
reject the null hypothesis and declare that the equation is statistically signifi-
cant at the 5-percent level. For more on the F-test, see Section 5.6.


521
Statistical Tables
Table B-2  Critical Values of the F-Statistic: 5-Percent Level of Significance
v1 = Degrees of Freedom for Numerator
1
2
3
4
5
6
7
8
10
12
20
H
  1
161
200
216
225
230
234
237
239
242
244
248
254
  2
18.5 19.0 19.2 19.2 19.3 19.3 19.4 19.4 19.4 19.4 19.4 19.5
  3
10.1 9.55 9.28 9.12 9.01 8.94 8.89 8.85 8.79 8.74 8.66 8.53
  4
7.71 6.94 6.59 6.39 6.26 6.16 6.09 6.04 5.96 5.91 5.80 5.63
  5
6.61 5.79 5.41 5.19 5.05 4.95 4.88 4.82 4.74 4.68 4.56 4.36
  6
5.99 5.14 4.76 4.53 4.39 4.28 4.21 4.15 4.06 4.00 3.87 3.67
  7
5.59 4.74 4.35 4.12 3.97 3.87 3.79 3.73 3.64 3.57 3.44 3.23
  8
5.32 4.46 4.07 3.84 3.69 3.58 3.50 3.44 3.35 3.28 3.15 2.93
  9
5.12 4.26 3.86 3.63 3.48 3.37 3.29 3.23 3.14 3.07 2.94 2.71
10
4.96 4.10 3.71 3.48 3.33 3.22 3.14 3.07 2.98 2.91 2.77 2.54
11
4.84 3.98 3.59 3.36 3.20 3.09 3.01 2.95 2.85 2.79 2.65 2.40
12
4.75 3.89 3.49 3.26 3.11 3.00 2.91 2.85 2.75 2.69 2.54 2.30
13
4.67 3.81 3.41 3.18 3.03 2.92 2.83 2.77 2.67 2.60 2.46 2.21
14
4.60 3.74 3.34 3.11 2.96 2.85 2.76 2.70 2.60 2.53 2.39 2.13
15
4.54 3.68 3.29 3.06 2.90 2.79 2.71 2.64 2.54 2.48 2.33 2.07
16
4.49 3.63 3.24 3.01 2.85 2.74 2.66 2.59 2.49 2.42 2.28 2.01
17
4.45 3.59 3.20 2.96 2.81 2.70 2.61 2.55 2.45 2.38 2.23 1.96
18
4.41 3.55 3.16 2.93 2.77 2.66 2.58 2.51 2.41 2.34 2.19 1.92
19
4.38 3.52 3.13 2.90 2.74 2.63 2.54 2.48 2.38 2.31 2.16 1.88
20
4.35 3.49 3.10 2.87 2.71 2.60 2.51 2.45 2.35 2.28 2.12 1.84
21
4.32 3.47 3.07 2.84 2.68 2.57 2.49 2.42 2.32 2.25 2.10 1.81
22
4.30 3.44 3.05 2.82 2.66 2.55 2.46 2.40 2.30 2.23 2.07 1.78
23
4.28 3.42 3.03 2.80 2.64 2.53 2.44 2.37 2.27 2.20 2.05 1.76
24
4.26 3.40 3.01 2.78 2.62 2.51 2.42 2.36 2.25 2.18 2.03 1.73
25
4.24 3.39 2.99 2.76 2.60 2.49 2.40 2.34 2.24 2.16 2.01 1.71
30
4.17 3.32 2.92 2.69 2.53 2.42 2.33 2.27 2.16 2.09 1.93 1.62
40
4.08 3.23 2.84 2.61 2.45 2.34 2.25 2.18 2.08 2.00 1.84 1.51
60
4.00 3.15 2.76 2.53 2.37 2.25 2.17 2.10 1.99 1.92 1.75 1.39
120
3.92 3.07 2.68 2.45 2.29 2.18 2.09 2.02 1.91 1.83 1.66 1.25
∞
3.84 3.00 2.60 2.37 2.21 2.10 2.01 1.94 1.83 1.75 1.57 1.00
Source: Abridged from M. Merrington and C. M. Thompson, “Tables of percentage points 
of the inverted beta (F) distribution,” Biometrika, Vol. 33, 1943, p. 73, by permission of the 
Biometrika trustees.
v2 =  Degrees of Freedom for Denominator


522
aPPENDIX B
Table B-3: The F-Distribution
The F-distribution is used in regression analysis to deal with a null hypoth-
esis that contains multiple hypotheses or a single hypothesis about a group 
of coefficients. To test the most typical joint hypothesis (a test of the overall 
significance of the regression):
 H0: β1 = β2 = g
   = βK = 0
 HA: H0 is not true
the computed F-value is compared with a critical F-value, found in Tables B-2 
and B-3. The F-statistic has two types of degrees of freedom, one for the 
­numerator (columns) and one for the denominator (rows). For the null and 
alternative hypotheses above, there are K numerator (the number of restric-
tions implied by the null hypothesis) and N - K - 1 denominator degrees 
of freedom, where N is the number of observations and K is the number of 
explanatory variables in the equation. This particular F-statistic is printed out 
by most computer regression programs. For example, if K = 5 and N = 30, 
there are 5 numerator and 24 denominator degrees of freedom, and the criti-
cal F-value for a 1-percent level of significance (Table B-3) is 3.90. A com-
puted F-value greater than 3.90 would lead us to reject the null hypothesis 
and declare that the equation is statistically significant at the 1-percent level. 
For more on the F-test, see Section 5.6.


523
Statistical Tables
Table B-3  Critical Values of the F-Statistic: 1-Percent Level of Significance
v1 = Degrees of Freedom for Numerator
1
2
3
4
5
6
7
8
10
12
20
H
1 4052 5000 5403 5625 5764 5859 5928 5982 6056 6106 6209 6366
2
98.5 99.0 99.2 99.2 99.3 99.3 99.4 99.4 99.4 99.4 99.4 99.5
3
34.1 30.8 29.5 28.7 28.2 27.9 27.7 27.5 27.2 27.1 26.7 26.1
4
21.2 18.0 16.7 16.0 15.5 15.2 15.0 14.8 14.5 14.4 14.0 13.5
5
16.3 13.3 12.1 11.4 11.0 10.7 10.5 10.3 10.1 9.89 9.55 9.02
6
13.7 10.9 9.78 9.15 8.75 8.47 8.26 8.10 7.87 7.72 7.40 6.88
7
12.2 9.55 8.45 7.85 7.46 7.19 6.99 6.84 6.62 6.47 6.16 5.65
8
11.3 8.65 7.59 7.01 6.63 6.37 6.18 6.03 5.81 5.67 5.36 4.86
9
10.6 8.02 6.99 6.42 6.06 5.80 5.61 5.47 5.26 5.11 4.81 4.31
10
10.0 7.56 6.55 5.99 5.64 5.39 5.20 5.06 4.85 4.71 4.41 3.91
11
9.65 7.21 6.22 5.67 5.32 5.07 4.89 4.74 4.54 4.40 4.10 3.60
12
9.33 6.93 5.95 5.41 5.06 4.82 4.64 4.50 4.30 4.16 3.86 3.36
13
9.07 6.70 5.74 5.21 4.86 4.62 4.44 4.30 4.10 3.96 3.66 3.17
14
8.86 6.51 5.56 5.04 4.70 4.46 4.28 4.14 3.94 3.80 3.51 3.00
15
8.68 6.36 5.42 4.89 4.56 4.32 4.14 4.00 3.80 3.67 3.37 2.87
16
8.53 6.23 5.29 4.77 4.44 4.20 4.03 3.89 3.69 3.55 3.26 2.75
17
8.40 6.11 5.19 4.67 4.34 4.10 3.93 3.79 3.59 3.46 3.16 2.65
18
8.29 6.01 5.09 4.58 4.25 4.01 3.84 3.71 3.51 3.37 3.08 2.57
19
8.19 5.93 5.01 4.50 4.17 3.94 3.77 3.63 3.43 3.30 3.00 2.49
20
8.10 5.85 4.94 4.43 4.10 3.87 3.70 3.56 3.37 3.23 2.94 2.42
21
8.02 5.78 4.87 4.37 4.04 3.81 3.64 3.51 3.31 3.17 2.88 2.36
22
7.95 5.72 4.82 4.31 3.99 3.76 3.59 3.45 3.26 3.12 2.83 2.31
23
7.88 5.66 4.76 4.26 3.94 3.71 3.54 3.41 3.21 3.07 2.78 2.26
24
7.82 5.61 4.72 4.22 3.90 3.67 3.50 3.36 3.17 3.03 2.74 2.21
25
7.77 5.57 4.68 4.18 3.86 3.63 3.46 3.32 3.13 2.99 2.70 2.17
30
7.56 5.39 4.51 4.02 3.70 3.47 3.30 3.17 2.98 2.84 2.55 2.01
40
7.31 5.18 4.31 3.83 3.51 3.29 3.12 2.99 2.80 2.66 2.37 1.80
60
7.08 4.98 4.13 3.65 3.34 3.12 2.95 2.82 2.63 2.50 2.20 1.60
120
6.85 4.79 3.95 3.48 3.17 2.96 2.79 2.66 2.47 2.34 2.03 1.38
∞
6.63 4.61 3.78 3.32 3.02 2.80 2.64 2.51 2.32 2.18 1.88 1.00
Source: Abridged from M. Merrington and C. M. Thompson, “Tables of percentage points 
of the inverted beta (F ) distribution,” Biometrika, Vol. 3, 1943, p. 73, by permission of the 
Biometrika trustees.
v2 = Degrees of Freedom for Denominator


524
aPPENDIX B
Table B-4: The Durbin–Watson Statistic
The Durbin–Watson statistic is used to test for first-order serial correla-
tion in the residuals. First-order serial correlation is characterized by 
et = ρet-1 + ut, where et is the error term found in the regression equation 
and ut is a classical (not serially correlated) error term. Since ρ = 0 im-
plies no serial ­correlation, and since most economic and business models 
imply positive serial correlation if any pure serial correlation exists, the 
typical hypotheses are:
 H0: ρ … 0
 HA: ρ 7 0
To test the null hypothesis of no positive serial correlation, the Durbin–­
Watson statistic must be compared to two different critical d-values, dL and 
dU found in Table B-4, depending on the level of significance, the number of 
explanatory variables (K) and the number of observations (N). For example, 
with 2 explanatory variables and 30 observations, the 5-percent one-tailed crit-
ical values are dL = 1.28 and dU = 1.57, so any computed Durbin–­Watson 
statistic less than 1.28 would lead to the rejection of the null hypothesis. 
For computed DW d-values between 1.28 and 1.57, the test is inconclusive, 
and for values greater than 1.57, we can say that there is no evidence of posi-
tive serial correlation at the 5-percent level. These ranges are illustrated in the 
following diagram:
0
2
4
dL
1.28  
dU
  1.57
Reject H0
Test
Inconclusive
1-Percent One-Sided Test of H0 :  t … 0 vs. HA : t 7 0
Do Not Reject H0
Two-sided tests are done similarly, with 4 - dU and 4 - dL being the 
­critical DW d-values between 2 and 4.


525
Statistical Tables
Table B-4  Critical Values of the Durbin–Watson Test Statistics dL and dU: 
5-Percent One-Sided Level of Significance  
(10-Percent Two-Sided Level of Significance)
N
K = 1
K = 2
K = 3
K = 4
K = 5
K = 6
K = 7
dL
dU
dL
dU
dL
dU
dL
dU
dL
dU
dL
dU
dL
dU
15 1.08 1.36 0.95 1.54 0.81 1.75 0.69 1.97 0.56 2.21 0.45 2.47 0.34 2.73
16 1.11 1.37 0.98 1.54 0.86 1.73 0.73 1.93 0.62 2.15 0.50 2.39 0.40 2.62
17 1.13 1.38 1.02 1.54 0.90 1.71 0.78 1.90 0.66 2.10 0.55 2.32 0.45 2.54
18 1.16 1.39 1.05 1.53 0.93 1.69 0.82 1.87 0.71 2.06 0.60 2.26 0.50 2.46
19 1.18 1.40 1.07 1.53 0.97 1.68 0.86 1.85 0.75 2.02 0.65 2.21 0.55 2.40
20 1.20 1.41 1.10 1.54 1.00 1.68 0.89 1.83 0.79 1.99 0.69 2.16 0.60 2.34
21 1.22 1.42 1.13 1.54 1.03 1.67 0.93 1.81 0.83 1.96 0.73 2.12 0.64 2.29
22 1.24 1.43 1.15 1.54 1.05 1.66 0.96 1.80 0.86 1.94 0.77 2.09 0.68 2.25
23 1.26 1.44 1.17 1.54 1.08 1.66 0.99 1.79 0.90 1.92 0.80 2.06 0.72 2.21
24 1.27 1.45 1.19 1.55 1.10 1.66 1.01 1.78 0.93 1.90 0.84 2.04 0.75 2.17
25 1.29 1.45 1.21 1.55 1.12 1.66 1.04 1.77 0.95 1.89 0.87 2.01 0.78 2.14
26 1.30 1.46 1.22 1.55 1.14 1.65 1.06 1.76 0.98 1.88 0.90 1.99 0.82 2.12
27 1.32 1.47 1.24 1.56 1.16 1.65 1.08 1.76 1.00 1.86 0.93 1.97 0.85 2.09
28 1.33 1.48 1.26 1.56 1.18 1.65 1.10 1.75 1.03 1.85 0.95 1.96 0.87 2.07
29 1.34 1.48 1.27 1.56 1.20 1.65 1.12 1.74 1.05 1.84 0.98 1.94 0.90 2.05
30 1.35 1.49 1.28 1.57 1.21 1.65 1.14 1.74 1.07 1.83 1.00 1.93 0.93 2.03
31 1.36 1.50 1.30 1.57 1.23 1.65 1.16 1.74 1.09 1.83 1.02 1.92 0.95 2.02
32 1.37 1.50 1.31 1.57 1.24 1.65 1.18 1.73 1.11 1.82 1.04 1.91 0.97 2.00
33 1.38 1.51 1.32 1.58 1.26 1.65 1.19 1.73 1.13 1.81 1.06 1.90 0.99 1.99
34 1.39 1.51 1.33 1.58 1.27 1.65 1.21 1.73 1.14 1.81 1.08 1.89 1.02 1.98
35 1.40 1.52 1.34 1.58 1.28 1.65 1.22 1.73 1.16 1.80 1.10 1.88 1.03 1.97
36 1.41 1.52 1.35 1.59 1.30 1.65 1.24 1.73 1.18 1.80 1.11 1.88 1.05 1.96
37 1.42 1.53 1.36 1.59 1.31 1.66 1.25 1.72 1.19 1.80 1.13 1.87 1.07 1.95
38 1.43 1.54 1.37 1.59 1.32 1.66 1.26 1.72 1.20 1.79 1.15 1.86 1.09 1.94
39 1.43 1.54 1.38 1.60 1.33 1.66 1.27 1.72 1.22 1.79 1.16 1.86 1.10 1.93
40 1.44 1.54 1.39 1.60 1.34 1.66 1.29 1.72 1.23 1.79 1.18 1.85 1.12 1.93
45 1.48 1.57 1.43 1.62 1.38 1.67 1.34 1.72 1.29 1.78 1.24 1.84 1.19 1.90
50 1.50 1.59 1.46 1.63 1.42 1.67 1.38 1.72 1.34 1.77 1.29 1.82 1.25 1.88
55 1.53 1.60 1.49 1.64 1.45 1.68 1.41 1.72 1.37 1.77 1.33 1.81 1.29 1.86
60 1.55 1.62 1.51 1.65 1.48 1.69 1.44 1.73 1.41 1.77 1.37 1.81 1.34 1.85
65 1.57 1.63 1.54 1.66 1.50 1.70 1.47 1.73 1.44 1.77 1.40 1.81 1.37 1.84
70 1.58 1.64 1.55 1.67 1.53 1.70 1.49 1.74 1.46 1.77 1.43 1.80 1.40 1.84
75 1.60 1.65 1.57 1.68 1.54 1.71 1.52 1.74 1.49 1.77 1.46 1.80 1.43 1.83
80 1.61 1.66 1.59 1.69 1.56 1.72 1.53 1.74 1.51 1.77 1.48 1.80 1.45 1.83
85 1.62 1.67 1.60 1.70 1.58 1.72 1.55 1.75 1.53 1.77 1.50 1.80 1.47 1.83
90 1.63 1.68 1.61 1.70 1.59 1.73 1.57 1.75 1.54 1.78 1.52 1.80 1.49 1.83
95 1.64 1.69 1.62 1.71 1.60 1.73 1.58 1.75 1.56 1.78 1.54 1.80 1.51 1.83
100 1.65 1.69 1.63 1.72 1.61 1.74 1.59 1.76 1.57 1.78 1.55 1.80 1.53 1.83
Source: N. E. Savin and Kenneth J. White, “The Durbin–Watson Test for Serial Correlation 
with Extreme Sample Sizes or Many Regressors,” Econometrica, November 1977, p. 1994. 
­Reprinted with permission.
Note: N = number of observations, K = number of explanatory variables excluding the constant 
term. We assume that the equation contains a constant term and no lagged dependent variables.


526
aPPENDIX B
Table B-5: The Normal Distribution
The normal distribution is usually assumed for the error term in a regression 
equation. Table B-5 indicates the probability that a randomly drawn number 
from the standardized normal distribution (mean = 0 and variance = 1) 
will be greater than or equal to the number identified in the side tabs, 
called Z. For a normally distributed variable e with mean μ and variance σ2, 
Z = 1e - μ2/σ. The row tab gives Z to the first decimal place, and the 
­column tab adds the second decimal place of Z.


527
Statistical Tables
Table B-5  The Normal Distribution
z
.00
.01
.02
.03
.04
.05
.06
.07
.08
.09
0.0
.5000
.4960
.4920
.4880
.4840
.4801
.4761
.4721
.4681
.4641
0.1
.4602
.4562
.4522
.4483
.4443
.4404
.4364
.4325
.4286
.4247
0.2
.4207
.4168
.4129
.4090
.4052
.4013
.3974
.3936
.3897
.3859
0.3
.3821
.3783
.3745
.3707
.3669
.3632
.3594
.3557
.3520
.3483
0.4
.3446
.3409
.3372
.3336
.3300
.3264
.3228
.3192
.3156
.3121
0.5
.3085
.3050
.3015
.2981
.2946
.2912
.2877
.2843
.2810
.2776
0.6
.2743
.2709
.2676
.2643
.2611
.2578
.2546
.2514
.2483
.2451
0.7
.2420
.2389
.2358
.2327
.2296
.2266
.2236
.2206
.2177
.2148
0.8
.2119
.2090
.2061
.2033
.2005
.1977
.1949
.1922
.1894
.1867
0.9
.1841
.1814
.1788
.1762
.1736
.1711
.1685
.1660
.1635
.1611
1.0
.1587
.1562
.1539
.1515
.1492
.1469
.1446
.1423
.1401
.1379
1.1
.1357
.1335
.1314
.1292
.1271
.1251
.1230
.1210
.1190
.1170
1.2
.1151
.1131
.1112
.1093
.1075
.1056
.1038
.1020
.1003
.0985
1.3
.0968
.0951
.0934
.0918
.0901
.0885
.0869
.0853
.0838
.0823
1.4
.0808
.0793
.0778
.0764
.0749
.0735
.0721
.0708
.0694
.0681
1.5
.0668
.0655
.0643
.0630
.0618
.0606
.0594
.0582
.0571
.0559
1.6
.0548
.0537
.0526
.0516
.0505
.0495
.0485
.0475
.0465
.0455
1.7
.0446
.0436
.0427
.0418
.0409
.0401
.0392
.0384
.0375
.0367
1.8
.0359
.0351
.0344
.0336
.0329
.0322
.0314
.0307
.0301
.0294
1.9
.0287
.0281
.0274
.0268
.0262
.0256
.0250
.0244
.0239
.0233
2.0
.0228
.0222
.0217
.0212
.0207
.0202
.0197
.0192
.0188
.0183
2.1
.0179
.0174
.0170
.0166
.0162
.0158
.0154
.0150
.0146
.0143
2.2
.0139
.0136
.0132
.0129
.0125
.0122
.0119
.0116
.0113
.0110
2.3
.0107
.0104
.0102
.0099
.0096
.0094
.0091
.0089
.0087
.0084
2.4
.0082
.0080
.0078
.0075
.0073
.0071
.0069
.0068
.0066
.0064
2.5
.0062
.0060
.0059
.0057
.0055
.0054
.0052
.0051
.0049
.0048
2.6
.0047
.0045
.0044
.0043
.0041
.0040
.0039
.0038
.0037
.0036
2.7
.0035
.0034
.0033
.0032
.0031
.0030
.0029
.0028
.0027
.0026
2.8
.0026
.0025
.0024
.0023
.0023
.0022
.0021
.0020
.0020
.0019
2.9
.0019
.0018
.0018
.0017
.0016
.0016
.0015
.0015
.0014
.0014
3.0
.0013
.0013
.0013
.0012
.0012
.0011
.0011
.0011
.0011
.0010
Source: Based on Biometrika Tables for Statisticians, Vol. 1, 3rd ed., 1966, with the permission 
of the Biometrika trustees.
Note: The table plots the cumulative probability Z 7 z.


528
aPPENDIX B
Table B-6: The Chi-Square Distribution
The chi-square distribution describes the distribution of the estimate of the 
variance of the error term. It is useful in a number of tests, including the 
White test of Section 10.3 and the Lagrange Multiplier Serial Correlation 
Test of Section 9.4. The rows represent degrees of freedom, and the columns 
denote the probability that a number drawn randomly from the chi-square 
distribution will be greater than or equal to the number shown in the body 
of the table. For example, the probability is 10 percent that a number drawn 
randomly from any chi-square distribution will be greater than or equal to 
22.3 for 15 degrees of freedom.
To run a White test for heteroskedasticity, calculate NR2, where N is the 
sample size and R2 is the coefficient of determination (unadjusted R2) from 
Equation 10.9. (This equation has as its dependent variable the squared 
residual of the equation to be tested and has as its independent variables 
the independent variables of the equation to be tested plus the squares and 
cross-products of these independent variables.)
The test statistic NR2 has a chi-square distribution with degrees of freedom 
equal to the number of slope coefficients in Equation 10.9. If NR2 is larger 
than the critical chi-square value found in Statistical Table B-6, then we reject 
the null hypothesis and conclude that it’s likely that we have heteroskedastic-
ity. If NR2 is less than the critical chi-square value, then we cannot reject the 
null hypothesis of homoskedasticity.


529
Statistical Tables
Table B-6  The Chi-Square Distribution
Degrees  
of  
Freedom
Level of Significance 
(Probability of a Value at Least as Large as the Table Entry)
10%
5%
2.5%
1%
1
2.71
3.84
5.02
6.63
2
4.61
5.99
7.38
9.21
3
6.25
7.81
9.35
11.34
4
7.78
9.49
11.14
13.28
5
9.24
11.07
12.83
15.09
6
10.64
12.59
14.45
16.81
7
12.02
14.07
16.01
18.48
8
13.36
15.51
17.53
20.1
9
14.68
16.92
19.02
21.7
10
15.99
18.31
20.5
23.2
11
17.28
19.68
21.9
24.7
12
18.55
21.0
23.3
26.2
13
19.81
22.4
24.7
27.7
14
21.1
23.7
26.1
29.1
15
22.3
25.0
27.5
30.6
16
23.5
26.3
28.8
32.0
17
24.8
27.6
30.2
33.4
18
26.0
28.9
31.5
34.8
19
27.2
30.1
32.9
36.2
20
28.4
31.4
34.2
37.6
Source: Based on Biometrika Tables for Statisticians, Vol. 1, 3rd ed., 1966, with the permission 
of the Biometrika trustees.
Note: The table plots the cumulative probability Z 7 z.


This page intentionally left blank


Applied regression analysis, steps in
data collection, inspection, and  
cleaning, 69–71, 75, 76–77, 
90–91
defined, 66
documenting results, 72–73, 78–79, 91
dummy variables and, 79–83, 80
equation estimating and evaluating, 
72, 78, 91
exercise (econometric lab), 89–91
hypothesize expected signs of coeffi-
cients, 68–69, 75, 90
independent variables and functional 
form selection, 67–68, 74–75, 90
literature review and theoretical 
­modeling, 66–67, 74, 89–90
overview, 66–73
practical tips, 351–352
restaurant location decisions, 73–79. 
See also Woody’s restaurant 
­locations example
ARIMA forecasting technique
defined, 456
models, 457–459
Assumptions, in Classical model.  
See Classical Assumptions
Atukeren, Erdal, 375n8
Autocorrelation. See Serial correlation
Autoregressive equations, 367, 378
Autoregressive process, defined, 457
Average observations, 401
Barkley, Andrew, 176n10
Batte, Marvin T., 217, 217n9
Baum, Christopher F., 320n11
Acceptance regions, 119, 120, 133, 135, 
287, 287
Additive error term, 93–94
Adjusted R2, 52–54
dummy dependent variable models 
and, 402
incorrect functional form and,  
206–207
misuse example, 55–56
specification criteria for potential 
variable, 166
misuse example, 168
selection example, 177
specification search bias and,  
171–172
AIC (Akaike’s Information Criterion), 
187–188
Akaike, Hirotogu, 187n19
Akaike’s Information Criterion (AIC), 
187–188
Allen, R. C., 190n1
Alternative functional forms,  
192–201
Alternative hypotheses, 116–118
defined, 117
Amatya, Ramesh, 408n10
Amemiya, T., 404n8
American Economic Review, 73n5
Analysis
regression, 5–14. See also Regression 
analysis
residual, 164
sensitivity, 72, 174, 177
single-equation linear regression, 5
Ando, Albert, 332n17
INDEX
NOTE: Page numbers in italics refer to figures and tables; footnotes are indicated by 
“n” following the page number.
531


Bayaner, Ahmet, 217n9
Bayesian Information Criterion (BIC), 
187–188
Bayesian statistics, 116, 116n1
Becketti, Sean, 373n4
Belsley, D. A., 233n5
Bertrand, M., 470n4
Best Linear Unbiased Estimator (BLUE), 
106
Best practices, for specification searches, 
170
βn
sampling distribution of, 100–105, 
103, 104
SE(βn), 105
β0 (constant or intercept term), 7, 8, 
190–192
Classical Assumptions, 191
components, 190–191, 190n1
dummy variable and, 80n8
estimates, 192
regression equation and, 71
suppression, 191, 191–192
use and interpretation, 190–192
β1 (slope coefficient), 7–8
cross-sectional model, 22
Bias
Best Linear Unbiased Estimator, 106
in distributions of βn, 103
Durbin–Watson test, 284n5
in dynamic models, 368
expected, 161, 162–163, 162n4, 164
Generalized Least Squares, 295
heteroskedasticity, 312–313
measurement errors, 442
multicollinearity, 226–227, 236
Newey–West standard errors, 296
omitted variable. See Omitted 
­variable bias
Ordinary Least Squares, 418–421
serial correlation, 280n1
specification, 158
specification criteria, 166
independent variable selection 
­example, 177
misuse example, 168
specification searches, 171–172
t-tests, 171–172
Two-Stage Least Squares, 424n5
Bias equations, omitted variables, 161, 
162–163, 162n4
Biased estimator, 102, 102n7
BIC (Bayesian Information Criterion), 
187–188
Binomial logit, defined, 397
Binomial logit model, 397–404
example, 403–404
Binomial probit
defined, 404
model, 404–405
BLUE (Best Linear Unbiased Estimator), 
106
Borders
null hypothesis, 122
values, 130n8
Brada, Josef C., 300n18, 301
Brazilian black market for dollars  
(data set), 336–337
Breusch, T. S., 316n6
Breusch–Godfrey test, 289n11
Breusch–Pagan test, 316–318, 317n8, 320
defined, 316
British Household Panel Data Survey, 
474
Brown, Eleanor, 86
Bruggink, Thomas H., 150n15
Buckles, Stephen, 181n11
Bucklin, R. E., 334, 334n19
Bureau of Labor Statistics, 473
Cahill, Preston, 218n10
Campbell, J., 378n12
Campbell, John Y., 380n15
Canadian National Public Health 
­Survey, 474
Card, David, 469, 469n3
Carnot, N., 444n3
Cassel, Eric, 360n8
Causality
dual, 412
Granger, 374–376
regression analysis and, 5–6
532
INDEX


Caves, R. E., 334, 334n19
Census Catalog and Guide, 345
Checklist, regression projects,  
354–355
Chi-square test
heteroskedasticity, 317, 319, 327
serial correlation, 373
Chicken consumption example
Durbin–Watson statistic, 288n8, 452
forecasting and, 445–447, 447, 452
Generalized Least Squares,  
294–295
Cigarette consumption (data set), 487
City expenditures functions
aggregate, 323
per capita, 324
Classical Assumptions, 92
constant variance for error term (V), 
96–98, 97
explanatory variables uncorrelated 
with error term (III), 95–96
independence of observations of error 
term (IV), 96
linear regression model (I), 93–94, 
93n1
multicollinearity of explanatory 
­variables (VI), 98
normal distribution for error term 
(VII), 98–99, 99
violations
constant term, 191
heteroskedasticity, 306, 307
instrumental variables, 421–422
multicollinearity, 221–222
omitted variables and, 
­consequences of, 159–160
serial correlation, 273, 275, 282, 
371–372
simultaneous equations, 411,  
415, 416
zero population mean, error terms 
with (II), 94, 94–95
Classical error term, 93
Classical model, 92–108
Classical Assumptions, 92–99, 93n1
Gauss–Markov Theorem, 106–107
sampling distribution of βn, 100–105
standard econometric notation,  
107–108, 108
Classical normal error term, 93
Classical null hypothesis, 116–118
Cleaning data, 71, 75, 90–91
Cochrane, D., 293n14
Cochrane–Orcutt method, 293, 293n15
Coefficient errors, applied regression 
analysis, 72, 73n4, 78, 78n7
Coefficient estimators, properties, 107
Coefficients, 7
double-log functions, 195, 195
dummy variable, 81–82
estimated/estimating, 78, 78n7
t-values and, 78, 78n7
estimated logit, interpreting, 400–403
expected signs, 68–69, 75, 90
F-tests, 142
heteroskedasticity, 312–313
linear in the, 93n1, 193
multicollinearity, 226–228
multivariate regression, 12, 41–42
omitted variable, 158
Ordinary Least Squares and, 38, 
38n3, 392
partial regression, 41–42
random, estimation of, 105
reduced-form, 417
regression, notation for, 108
seasonal dummy, 147
serial correlation, 275
simple correlation, 232–233, 232n3, 
233n4
slope. See Slope coefficient (β1)
structural, 413
true, 15n9
unexpected sign, handling of,  
348–350
Cohen, Kalman, 335n21
Cohen, Malcolm, 409n11
Cointegration, 382–384
defined, 383
Cola supply and demand model,  
414, 416
Collection, of data, 69–71, 75
533
INDEX


534
INDEX
Critical values
defined, 119
F-value, 145, 145n14
t-values, 119, 123–125, 132, 133, 135
selecting, 130
Cross-sectional data sets/models
defined, 21
heteroskedasticity in, 309
housing prices, 20–23, 22
pooled cross sections across time, 
473n7
time series studies vs., 274–275
Data
cleaning, 71, 75, 90–91
collecting, 69–71, 75, 90–91
inspecting, 71, 75, 90–91
missing, 346
panel. See Panel data
research projects, 342–346
Data collection
advanced sources for, 346–348
missing data, 346
panel data, 347–348
for regression projects, 342–346
surveys, 347
Data entry errors, finding, 71, 91
Data mining, 172–173
Data sets
Brazilian black market for dollars, 
336–337
cigarette consumption, 487
college application, 61–62
cross-sectional. See Cross-sectional 
data sets/models
financial aid example, 46–47
Four Musketeers, 388
heteroskedasticity in, 308–309
homeowners’ (non-self-employed) 
income and consumption, 333
housing prices, 361–362
labor force participation of women, 396
murder rate example, 479–481
MVP 1998, 243
petroleum consumption, 326–327
pharmaceutical price discrimination, 
154
College application (data set), 61–62
Collinearity, 98, 222n1. See also 
­Multicollinearity
Common Application, 60, 60n9
data set example, 61–62
Compound null hypotheses, 142, 147
Condition number, 233n5
Conditional forecast/forecasting, 
450–451
defined, 450
Conditions
omitted, dummy variables and, 80, 
82–83
order, 433–434
rank, 433n11
Confidence intervals, 139–142
defined, 139
forecasting, 449, 452–454, 455
Confidence level, 127
Consequences
heteroskedasticity, 312–314
irrelevant variables, 165
multicollinearity, 226–231
omitted variables, 159–160
serial correlation, 281–284
Constant term, defined, 7. See also β0 
(constant or intercept term)
Constant variance, 96–98, 97, 306
Constants, 7
Control groups, 465–472, 472
defined, 465
Corrections
Error Correction Model, 384n20
heteroskedasticity, 320–324,  
337–339
multicollinearity, 235–240
omitted variables, 163–164
serial correlation, 291–296
in dynamic models, 373–374
Correlation
serial. See Serial correlation
simple correlation coefficients,  
232–233, 232n3, 233n4
spurious, 376–385
Covariance stationarity, 377n11
Criteria specification, 166–167
misuse example, 167–169


535
INDEX
measurement errors, 440–441
other techniques, 404–406
variations in. See under Y variable
Derivatives, partial, 401
Description, 2–3
Deseasonalizing data, 146
Detection
heteroskedasticity, 314–320
econometric lab exercise, 337–338
multicollinearity, 232–235
nonstationarity, 386
serial correlation, 284–291
Deterministic component, regression 
equation, 9
Deviations, standard, 107
Dewald, W. G., 73n5
Diamond, A., 470n4
Diaz, Jaime, 25n11
DiCioccio, E., 484n14
Dickey, D. A., 380n14
Dickey–Fuller test, 379–382
defined, 380
Diekmann, Florian, 217, 217n9
Difference-in-differences estimator, 
­defined, 470
Differences
estimator, 467
observed, systematic reasons for, 466
Differencing models, 475n10, 
 488–489
Discrete heteroskedasticity, 308, 309
Dispersion. See Variance
Distributed lag models, 365–367
defined, 365
Distributions
biases, 103
discrete heteroskedasticity, 309
homoskedasticity vs., 307, 308
impure serial correlation, 278
intercept, 484
multicollinearity, 226–227, 227
normal, 420n4
error terms and, 98–99, 99
sampling distribution of βn, 100–105, 
103, 104
simultaneity bias, 421
Standard Normal, 99
pooled cross sections across time, 
473n7
Presidential election, 463
from RateMyProfessor.com, 29
salon haircut, 488
SAT interactive learning exercise, 
248–249
small macromodel, 426
Soviet defense spending, 301
stock price, 212–213
student consumption, 229
Woody’s restaurant locations 
­example, 76–77
Decision rules
acceptance and rejection regions,  
285, 287
defined, 119
F-test, 143
hypothesis testing, 119, 120, 121
t-test, 123–125, 131
Decomposition, variance, 47, 48
Degree of confidence, 127
Degrees of freedom
critical t-value and, 123
defined, 53
dynamic models, 366–368
F-tests, 143–145
heteroskedasticity and, 319, 320n11, 
327n15
number of observations and, 69–70
regression equation and
adjustment, 54
calculating, 70, 70n3
sequential specification criteria and, 
186, 187
t-tests, 123, 124
variance of distribution and, 104
Δ notation, 194n2
Demeaned model, 475n10
Denny’s restaurants, 73n6. See also 
Woody’s restaurant locations 
­example
Dent, W., 375n9
Dependent variables, 5–6, 390
binomial logit model, 397–404
estimated vs. actual value, 15–16
linear probability model, 390–397


536
INDEX
Durbin–Watson tables (Stanford 
­University), 289n10
Durbin–Watson test
defined, 284
for serial correlation detection,  
284–286, 285n7
dynamic models, 372, 372n3
examples, 286–289, 287
one-sided, 287
Dynamic models, 364, 367–371
basic form, 367–371
bias, 368
defined, 367
distributed lag models, 365–367
example, 369–370
geometric weighting schemes, 369
Granger causality and, 374–376
serial correlation, 371–374
corrections, 373–374
testing for, 372–373
serial correlation and, 374–376
ECM (Error Correction Model),  
384n20
EconLit, 67, 67n1, 345
Econometric Labs
applied regression analysis, 89–91
heteroskedasticity, detection and 
­correction exercise, 337–339
hypothesis testing, 155–156
regression analysis, 63–64
serial correlation, 303–305
specification, 217–220
Econometrics
alternative approaches, 4–5
Classical model, 92–108
definitions, 1–2
ethical behavior and, 351–352
notation conventions, 107–108, 108
software. See individually named 
­applications; Software
uses, 2–4
Economic activity, relationships 
­describing, 2–3
Economic data, sources, 345. See also 
Data collection
Disturbance (error) terms. See Stochas-
tic error terms
Documentation, results, 72–73,  
78–79, 91
Dominant variable, defined, 224
Dorfman, J. J., 393n2
Dornbusch, Rudiger, 334, 334n20
Double-log functional forms, 194–196, 
195, 201
defined, 194
Driver’s license test, binomial logit 
­example, 403–404
Dropping variables, 162n4, 164,  
170, 171
redundant variables, 236–238
Dual causality, 412
Dummy variable trap, 81
Dummy variables, 14, 146–147, 
319n10
applied regression analysis and, 
79–83, 80
defined, 79
dependent, 390
binomial logit mode, 397–404
binomial probit model, 404–405
linear probability model, 391–392
multinomial models, 405–406
Ordinary Least Squares and, 392
other techniques, 404–406
examples, 175
independent
functional forms, 196, 203–206
in housing price exercise, 359, 361
log of, 196
omitted condition and, 82–83
one-time, 83
seasonal, 146–147
slope, 203–206, 205
Durbin, J., 284n4
Durbin–Watson statistic
heteroskedasticity, 325
serial correlation
equation, 284–286
software calculation, 289n9
tables, 289n11
use examples, 286–289


537
INDEX
estimated regression equation, 16
homoskedastic vs. heteroskedastic, 
310–311, 310–311
notation, 108
observations, 96
standard deviation, notation for, 108
stochastic, 8–11, 94, 94–95, 95n2, 96
with zero population mean, 94, 
94–95
Errors
coefficients, 73n4
data entry, finding, 71, 91
explanatory variables, 95–96
heteroskedasticity, 307, 321
homoskedasticity vs., 310–311, 
310–311
impure serial correlation, 307
irrelevant variables, 165–166
Mean Square Error, 105
measurement, 441–442
Y variation and, 9
nonlinear relationships, 10
normal distribution, 98–99, 99
Ramsey Regression Specification Error 
Test, 185–186
rounding, 39
serial correlation, 275
specification, 68, 157–158
standard. See Standard errors
term distribution with a mean of 
zero, 94, 94–95
Type I Errors, 118–119
Type II Errors, 118–119
variables, 440–442
ESS (explained sum of squares), 48–49, 
48n6, 145, 145n13
defined, 48
estat bgodfrey lag, 289n11
Estimated coefficients, 78, 78n7
logit, interpreting, 400–403
random, 105
regression, weight/height example, 40
Estimated regression equation, 14–17
defined, 14
Ordinary Least Squares technique 
and, 50–54
Economics, experimental, 465n1
methods, 466–472
Efficiency, of estimators, 106
Elasticity, defined, 194
Elder, John, 381n16
Elliott, G., 444n3
Endogenous variables, 412–413, 428n9
defined, 412
Engel curves, 198
Engle, Rob, 290n12, 382n17, 384n19
Equations
autoregressive, 367, 378
Best Linear Unbiased Estimator, 106
bias, omitted variables and, 161, 
162–163, 162n4
distributed lag models, 366
Durbin–Watson test, 284
Generalized Least Squares, 292–295
identification problem, 430–434
independent variables, 161n3
investment, 427n9
linear
in the coefficients, 193
defined, 8, 8n5
in the variables, 192–193
multiple regression, 121
Ordinary Least Squares, 392
Ramsey Regression Specification Error 
Test, 186, 186n16
reduced-form, 416–417
OLS and, 423
regression. See Regression equation
second-degree polynomial, 200, 200, 
201
serial correlation, 282
simultaneous. See Simultaneous 
equations
single-equation linear models, 6–8
stochastic error terms, 8–11
supply and demand simultaneous, 416
weight-guessing, 17–19, 20
Error Correction Model (ECM), 384n20
Error term
additive, 93–94
classical, 93
constant variance, 96–98, 97


538
INDEX
Exogenous variables, 412–413
defined, 412
Expectations
signs of coefficients, 68–69, 75, 90
values, 9
estimated coefficients, notation  
for, 108
Expected bias, 161, 162–163, 162n4, 164
Expected value, defined, 9
Experimental economics, 465n1
methods, 466–472
Experiments
impossible, 468
natural, 469–472
random assignment, 466–468
Explained sum of squares (ESS), 48–49, 
48n6, 145, 145n13
defined, 48
Explanatory variables. See Independent 
variables
F-statistic, 143
Breusch–Pagan test, 316n7
F-test, 142–147, 376, 376n10
defined, 142
other uses, 146–147
overview, 142–144
significance, 144–146
F-values, 143–144
Fair, Ray C., 211, 211n6, 444n2, 
461n13
Fallows, James, 246n7
FDA (Food and Drug Administration), 
116
Feedback effects, 412
Financial aid (multivariate regression 
model example), 43–47
as ability to pay, 45
data set, 46–47
as function of high school rank, 45
First-order autocorrelation coefficient, 
defined, 275
First-order serial correlation, 275
Durbin–Watson test, 284–289, 285n6
Generalized Least Squares, 292
Lagrange Multiplier test, 289
Estimates
constant terms, 192
defined, 36
heteroskedasticity, 312–313
multicollinearity and, 226
Ordinary Least Squares, 384
regression, 288
serial correlation, 282–283
Two-Stage Least Squares, 424n5
validity, 49–50
Estimation
binomial logit, 397–400
coefficients, 78, 78n7
distributed lag models, 365–367
dynamic models, 368, 370
fixed effects models, 472n6, 477–483
linear probability model, 392
Ordinary Least Squares, 37
estimator properties, 106–107
example, 39–40
multivariate regression model, 
40–49
properties, 37, 37n2
regression equations, 50–54, 72, 78
single-independent-variable 
­models, 35–40
random coefficients, 105
sample size and, 69
standard errors, 78, 78n7, 314n4
Two-Stage Least Squares, 428n10
Estimators, 100
Best Linear Unbiased Estimator, 106
biased, 102, 102n7
defined, 37
differences, 467
difference-in-differences, 470
efficiency, 106
Ordinary Least Squares coefficients, 
properties of, 106–107
Two-Stage Least Squares, 424–425, 
424n5
unbiased, 101, 102n7, 106, 107
Ethics, 351–352
EViews, 72
Durbin–Watson statistic, 288n9
Generalized Least Squares, 294n16


539
INDEX
inverse, 197, 197n4
lagged independent variables and, 
202–203
linear, 194, 201
polynomial, 199–201, 200, 201
pure serial correlation and, 275
quadratic, 200, 201, 200
selecting, 201, 201
semilog, 196–199, 198, 201
stochastic error and, 9–10
Functions
double-log, 194–196, 195
investment, 427n8
linear, 98
polynomial, 199–201, 200
semilog, 196–199, 198
Gauss–Markov Theorem, 106–107
heteroskedasticity, 313
GDP (Gross Domestic Product),  
3–4, 344
Generalized Least Squares (GLS), 
292–295
defined, 292
Gensemer, Bruce, 438n12
Geometric weighting schemes, 369
Geweke, John, 375n9
GLS (Generalized Least Squares), 
292–295
defined, 292
Gneezy, Uri, 465n1
Goldman, Dana, 409n12
Goodman, Allen C., 360n9
Goodness-of-fit measures, 50–52, 51
spurious regression and, 56
Granger, C. W. J., 375n7, 379n13, 
382n17, 384n19, 444n3
Granger, Clive, 4n4
Granger causality, 374–376, 389n22
defined, 375
Graves, Ronald L., 300n18, 301
Greene, William H., 406n9, 442n14
Grether, G. M., 359n6
Griffiths, W. E., 187n20
Griliches, Zvi, 290n12, 442n15
Gross Domestic Product (GDP), 3–4, 344
Fit
goodness of. See Goodness of fit 
­measures
mathematical vs. statistical, in X,Y 
­coordinate system, 69–70, 70, 71
measuring, linear probability model 
and, 392
Fixed effects model, 475–477
defined, 475
estimation, 472n6, 477–483
panel data and, 481–482, 482n11
random effects model vs., 484
Fluctuations, random, 466
Food and Drug Administration (FDA), 
116
Forecasting, 3–4, 21, 443–444
ARIMA models, 456–459
complex problems, 449–456
defined, 444
examples, 447
uses, 444–449
Forms. See Functional forms
Forst, Jerry, 176n10
Four Musketeers (data set), 388
Four specification criteria, 166. See also 
Specification criteria
Fowles, Richard, 216, 216n8
FRED (Federal Reserve Economic 
­Database), 345
Freeman, Vera, 181n11
Friedman, Milton, 116
Friend, I., 332n17
Fuller, W. A., 380n14
Functional form test, RESET as, 186n18
Functional forms
alternatives, 192–201, 201
applied regression analysis, 67–68, 
74–75, 90
constant term, use and interpretation 
of, 190–192
double-log, 194–196, 195, 201
dummy variables and, 196, 203–206, 
205
impure serial correlation and,  
278–279, 280, 281
incorrect, problems with, 206–209, 208


540
INDEX
Heteroskedasticity-consistent covari-
ance matrix (HCCM), 321n12
Heteroskedasticity-corrected standard 
errors (HCSEs), 321, 323n11, 
330
detected, 321
Hill, R. Carter, 187n20
Hirschfield, Mary, 86
Homeowners’ (non-self-employed) 
­income and consumption  
(data set), 333
Homoskedasticity, 306, 307, 308
errors, 310–311, 311
heteroskedasticity vs., 307, 308
error terms, 310–311, 310–311
in linear probability model, 392
Hoover, Kevin, 375n8
Housing prices
cross-sectional model, 21–23, 22
data set, 361–362
interactive exercise, 360–363
regression analysis explaining, 20–23
Hypothesis
alternative, 116–118
classical null, 116–118
expected signs of coefficients, 68–69, 
75, 90
priors and, 68
Hypothesis testing, 3, 5, 99, 115–116, 
155–156
confidence level, 127
data mining and, 172–173
decision rules, 119, 120, 121
error types, 118–119
exercise (econometric lab), 155–156
overview, 116–121
serial correlation, 283–284
t-tests, 121–139
“i” subscript, in regression equation, 
13–14
order, 14n8
Identification
defined, 430
problem, 430–434
Ihlanfeldt, Keith, 360, 360n8
Groups
control, 465–472, 472
treatment, 465–472, 472
Grubb, David, 368n2
Guides, regression projects, 356, 357
Hainmueller, J., 470n4
Hamermesh, Daniel S., 73n5
Hastings, Justine, 471n5, 471n6
Hausman test, 484
Hawthorne Effect, 468
Haynes, Stephen, 461n14, 462n15, 463
HCCM (heteroskedasticity-consistent 
covariance matrix), 321n12
HCSEs (heteroskedasticity-corrected 
standard errors), 321, 323n11, 
330
detected, 321
Hedonic models, 21n10, 87–89, 87n11
housing prices, 358–360
Hendry, David F., 137n10
Heo, Uk, 389, 389n21
Heterogeneity, unobservable, 468
Heteroskedasticity
bias, 312–313
Classical Assumptions, 97, 98, 306, 
307
coefficients, 312–313
consequences, 312–314
data sets, 308–309
defined, 307
detection and correction exercise 
(econometric lab), 337–339
discrete, 308, 309
errors, 310–311, 311
estimates, 312–313
example, 324–330
Gauss–Markov Theorem, 313
homoskedasticity vs., 307, 308
error terms, 310–311, 310–311
impure, 311–312
pure, 307–311
remedies for, 320–324
statistics, 313n3
testing for, 314–320
time-series models, 311


541
INDEX
Indifference curves, 195, 195–196
Inflation, high variance inflation factors 
and, 233–235, 233n5, 235n6
Inspection, of data, 71, 75, 90–91
Instrumental variables, 421–422, 
428n9, 442
defined, 421
Interaction terms, 203–204
defined, 203
Intercept dummy, 205
defined, 203
Intercept term. See also β0 (constant or 
intercept term)
defined, 7
distribution, 484
Internet resources, for project data, 345
Interpreting estimated logit coefficients, 
400–403
defined, 400
Intervals, confidence, 139–142
Intriligator, M. D., 290n12
Inverse functional form, 197, 197n4
Investment functions, 427n8
Irrelevant variables, 165–167
defined, 165
Isoquant, 195, 195
Jacobs, Rodney, 375n9
Jevons, Stanley, 6
Johnson, Bruce, 55n7, 63n11
Joint null hypotheses, 142, 147
Jones, R., 332n17
Journal of Economic Literature, 67
Journal of Money, Credit, and Banking, 
73n5
Judge, George C., 187n20
Kain, J., 359n6
Keele, Luke, 374n6
Keeler, James, 438n12
Kelly, Nathan, 374n6
Kenkel, Donald S., 113n10
Kennedy, Peter, 100n6, 116n1, 350n5, 
381n16, 383n18, 384n20, 
446n5, 474n9, 484n13
Keynes, John Maynard, 89, 116
Impact multipliers, defined, 417
Imperfect multicollinearity, 224–225, 
225
defined, 224
“Importance,” testing of, 138–139
Impossible experiments, 488
Impure heteroskedasticity, 311–312
defined, 311
Impure serial correlation, 278–281, 
279, 281
defined, 278
Lagrange Multiplier test, 365
simple lags, 365
Inconclusive region, serial correlation 
detection, 285n7, 287
Incorrect functional forms, problems 
with, 206–209, 208
Independent variables, 5–6, 12
data mining, 172–173
equations, 161n3
error term relationship and, 96
examples, 174–177
interaction terms as, 203–204
lagged, 202–203
measurement errors, 441–442
multicollinearity, 222n1
multivariate regression coefficients 
and, 41
notation in regression analysis, 11–12
omitted. See Omitted variables
omitted variables, 158–164
in regression equation, examples, 
13–14
selecting
in applied regression analysis,  
67–68, 74–75, 90
example, 174–177
sensitivity analysis, 174, 177
single-independent-variable models, 
OLS and, 35–40
specification, 170–174. See also 
­Specification
errors, 68, 157–158
stochastic error and, 8, 8n6
Index of Leading Indicators, 450
Indicator, leading, 450–451


542
INDEX
defined, 126
marginal, 127
t-test value, 123, 130
selecting, 126–127
Likelihood ratio test, 185n14
Linear equations, 8n5
defined, 8
Linear functional forms, 98, 198, 201, 
281
nonlinear forms vs, 208, 208–209
Linear in the coefficients, 93n1
defined, 193
Linear in the variables, 192–193
defined, 192
Linear probability model, 390–397
defined, 390
example of, 394–396
Ordinary Least Squares and, 392, 399
problems with, 392–394, 393
Linear regression model, 93–94, 93n1, 
194, 280
Linneman, Peter, 359, 359n7
List, John, 465n1
Literature review, in applied regression 
analysis, 66–67, 74, 89–90
Lo, A. W., 334, 334n19
Loeb, Peter D., 216, 216n8
Log-log (double-log) functional forms, 
194–196, 195, 201
Log (logarithm)
defined, 196
natural, 196–197
zero value and, 196, 197n4
Longitudinal data. See Panel data
Lott, William F., 334n20, 337
Lutkepohl, Helmut, 187n20
MacKinnon, J. G., 382n17, 384n19
Macromodel, small (data set), 426
Maddala, G. S., 186n18, 399n5, 404n8
Maeshiro, Asatoshi, 374n5
Malkiel, Burton, 449n6
Mankiw, N. G., 378n12
MAPE (mean absolute percentage 
error), defined, 446
Marginal significance level, 127
Keynesian macroeconomic model, 
naive linear, 425–429, 427n7
Kmenta, Jan, 118, 118n2
Kobayashi, Masahito, 293n15
Koen, V., 444n3
Koopmans, T. C., 1n1
Koyck, L. M., 368n1
Koyck distributed lag models, 368n1
Krueger, Alan, 469, 469n3
Labor force participation of women 
(data set), 396
Lagged independent variables,  
202–203, 413, 416, 423
Lagrange Multiplier (LM) test
defined, 289
heteroskedasticity and, 314n5
for serial correlation, 289–291, 
289n11
dynamic models and, 372–373
Lags
defined, 202
distributed lag models, 365–367
estat bgodfrey, 289n11
Koyck distributed lag models, 368n1
lagged values, 364
lagged variables, 202–203, 413, 416, 
423
dependent as independent, 364–372
time, 412n1
Lancaster, Tony, 116n1
Leading indicator, 450–451
defined, 450
Leamer, Ed, 1n1, 118n4, 375n9
Least squares. See Generalized Least 
Squares (GLS); Ordinary Least 
Squares (OLS); Two-Stage Least 
Squares (2SLS); Weighted Least 
Squares (WLS)
Lee, Tsoung-Chao, 187n20
Left-out variables. See Omitted variables
Left-side semilog, 199, 208
Lerman, Robert I., 409n11
Level of confidence, 127
Level of significance
choosing, 130


543
INDEX
demeaned, 475n10
differencing, 475n10, 488–489
distributed lag, 365–367
dynamic. See Dynamic models
Error Correction, 384n20
fixed effects, 475–477
estimation, 477–483
random effects model vs., 484
forecasting. See Forecasting
functional forms. See Functional 
forms
hedonic, 21n10, 87–89, 87n11, 
358–360
Keynesian, 427n7
Koyck distributed lag, 368n1
linear probability, 390–397
multinomial, 405–406
multivariate regression, estimating 
with OLS, 40–49
Ordinary Least Squares, 392, 399
panel data, 482
random effects, 483–484
simultaneous equation, forecasting 
and, 449
single-equation linear, 6–8
single-independent-variable, 
­estimating with OLS, 35–40
specifying, in applied regression 
­analysis, 67–68, 74–75, 90
supply and demand, 414, 416
theoretical, in applied regression 
analysis, 66–67, 74, 89–90
time-series. See Time-series models
Modigliani, Franco, 332n17
Monte Carlo studies, 187n20, 419n3
Moore, Robert L., 86
Mosteller, Frederick, 160n2
Moving-average process, defined, 457
MSE (Mean Square Error), 105
Multicollinearity, 98
bias, 236
consequences, 226–231
correction, 235–240
defined, 222n1
detection of, 232–235
distribution, 226–227, 227
Markov scheme, 275
Martinez-Vasquez, Jorge, 360, 360n8
Maximum likelihood (ML), 399, 399n4
Mayer, Thomas, 173n9
McCulloch, J. Huston, 306n1
McCullough, B. D., 290n12
McGillvray, R. G., 392n1
McIntosh, C. S., 393n2
Mean
forecasting methods and, 446
properties, 102–103
zero population, 94, 94–95
Mean absolute percentage error 
(MAPE), defined, 446
Mean Square Error (MSE), 105
Measurement error
simultaneous equations, 441–442, 
442n15
Y variation and, 9
Measurement unit, of variables, 70–71
Measurements. See also Equations
economic, 1–2. See also Econometrics
forecasting accuracy, 445–447, 447
overall fit, linear probability model, 
392
Meese, R., 375n9
Mendelsohn, Robert, 360n8
Methods
Cochrane–Orcutt, 293, 293n15
experimental economics, 466–472
mean absolute percentage error, 446
Prais–Winsten, 293, 293n15
Root mean square error, 446
Michener, Ron, 329
Mieszkowski, Peter, 359n6
Miller, Roger Leroy, 167n6
Missing data, 346
Misuse of adjusted R2, 55–56
ML (maximum likelihood), 399, 399n4
Models
ARIMA, 456–459
binomial logit, 397–404
binomial probit, 404–405
classical. See Classical model
cross-sectional. See Cross-sectional 
data sets/models


544
INDEX
Newey–West standard errors, 295–296
defined, 295
heteroskedasticity, 321n12
Nixon, Clair J., 217n9
NLSY (National Longitudinal Survey of 
Youth), 473
No serial correlation, 278
Non-random samples, 467–468
Nonexperimental quantitative research, 
steps in, 4–5
Nonstationarity, 376–385
cointegration, 382–384
detecting, 386
Dickey–Fuller test, 382–384
macroeconomic model, 429
sequences for dealing with, 384–385
spurious correlation and, 376–385
spurious regression, 379
testing for, 379–382
Nonstationary
defined, 377
time series, 377–378
Normal distributions, 420n4
error terms, 98–99, 99
Notation
delta, as used in text, 194n2
independent variables, 11–12
regression, extending, 11–14
standard econometric, 107–108, 108
time series studies, 274
Null hypothesis, 116–118
acceptance, 119, 120, 121
border for, 121–122, 130n6
defined, 117
F-test, 142–147
heteroskedasticity, 320, 320n11, 327, 
327n15, 328
homoskedasticity, 316–317
rejection, 117–119, 120, 123–125
stating, 130n8
testing, 155–156
Oat market supply and demand model, 
437–438
Observations
average, 401
Multicollinearity (continued)
imperfect, 224–225, 225
perfect, 98, 221, 222–224, 224
remedies for, 235–238
severe, 227, 366, 370
t-scores, 227–228
unadjusted, 238–240
unavoidable, 366
unexpected sign and, 349
variances, 226–227, 227
Multinomial logit, 406n9
Multinomial models, 405–406
Multiple regression equations, t-statistic 
and, 121
Multipliers
impact, 417
Lagrange. See Lagrange Multiplier 
(LM) test
Multivariate regression coefficients, 12, 
41–42
defined, 41
Multivariate regression model
defined, 12
equation, 12, 42–43, 43n4
estimating with OLS, 40–49
example, 43–47
Murder rate (data set), 479–481
Murti, V. N., 216, 216n7
MVP 1998 (data set), 243
Narrow distribution, 308, 309
National Health Interview Survey 
(1990), 113n11
National Longitudinal Survey of Youth 
(NLSY), 473
Natural experiments, 469–471
defined, 469
example, 471–472
Natural logs, 196–197
defined, 196
Negative critical values, 382n17
Negative serial correlation,  
276, 279
Nelson, C. R., 378n12, 457n10
Newbold, P., 379n13
Newey, W. K., 295n17


545
INDEX
distributed lag models, 365–367
estimation using
estimator properties, 106–107
example, 39–40
multivariate regression model, 
40–49
regression equations, 50–54, 72, 78
single-independent-variable 
­models, 35–40
F-test, 143
heteroskedasticity and, 313–314
linear equations and, 195
linear probability models, 392, 399
mechanics, 38
misuse of adjusted R2, 55–56
multicollinearity and, 223, 228
reduced-form equations and, 423
regression equations, evaluating 
­quality of, 49–50
serial correlation, 282–283
simultaneous equations and, 411
using, reasons for, 36–37
Otto, James, 28n13
Outlier, 71
Overall fit, measuring, 392
p-values, 127–128
defined, 127
limitations, 137n9
Pagan, A. R., 316n6
Panel data, 473–475, 482
defined, 473
fixed effects model applied to,  
481–482, 482n11
formation, 465
regression project and, 347–348
Parameters, Ordinary Least Squares 
­estimate, 37
Park, R. E., 317n8
Park test, 317n8
Partial derivatives, 401
Partial regression coefficients, 41–42
Pechman, Clarice, 334, 334n20
Perfect multicollinearity, 98, 221, 
 222–224, 224
defined, 222
differences in, systematic reasons for, 
466
error term, 96
error variance and, 97n5
estimated regression equation, 16
number, 69
order, 273, 274, 291n13, 294
outlier, 71
sampling distribution, 104
serial correlation, 273
OLS. See Ordinary Least Squares (OLS)
Omitted condition
defined, 80
dummy variables and, 82–83
Omitted variable bias
avoiding, 159n1
defined, 158
example, 162–163
expected, 161, 162–163, 162n4, 164
multicollinearity, 230–231
Omitted variables, 158–164
bias. See Omitted variable bias
consequences, 159–161
correcting for, 163–164
defined, 158
evidence, 158
heteroskedasticity, 312, 328
serial correlation, 280n1
One-sided critical values, 382
One-sided test
defined, 117
Durbin–Watson test, 287
t-test, 125, 129–133, 133
One-time dummy variable, 83
Online computer databases, 345
Orcutt, G. H., 293n14
Order, observation, 273, 274, 291n13, 
294
Order condition, 433–434
defined, 433
Ordered logit model, 406n9
Ordinary Least Squares (OLS), 35–57
bias, 418–421
Classical Assumptions, 92–99, 93n1
coefficients, 38, 38n3
defined, 36


546
index
Proportionality factor, defined, 310
Proxy variables, 346
PSID (U.S. Panel Survey of Income 
­Dynamics), 474
Publications, as data sources, 345
Pure heteroskedasticity, 307–311
defined, 307
Pure serial correlation, 275–278, 282, 
373
defined, 275
Quadratic functional form, 200, 201, 
200
Qualitative conditions, dummy 
­variables and, 203, 205
Quantitative research, nonexperimental, 
steps in, 4–5
Quasi-experiments. See Natural 
­experiments
Quigley, J., 359n6
R2, 50–52, 51
adjusted. See Adjusted R2
R 2, 54. See also Adjusted R2
R 2p, defined, 394
Ragan, James F., Jr., 439n13
Ramanathan, Ramu, 185n14
Ramsey, J. B., 185n15
Ramsey Regression Specification Error 
Test (RESET), 185–186
equations, 186, 186n16
Random assignment experiments, 
466–468
defined, 466
Random coefficient estimation, 105
Random component, regression 
­equation, 9
Random effects model, 483–484
defined, 483
fixed effects model vs., 484
Random error term. See Stochastic error 
term
Random fluctuations, 466
Random occurrences, 105
Random variation, stochastic error 
term, 9
Peron, Pierre, 380n15
Perry, Gregory, 217n9
Perry, John, 30n15
Petroleum consumption (data set), 
326–327
Pharmaceutical price discrimination 
(data set), 154
Philips, David, 468n2
Phillips, P. C. B., 186n18
Pindyck, Robert S., 399n4, 456n8, 
457n10
Plosser, C. I., 378n12
Polynomial functional form, 199–201, 
200, 201
defined, 199
Polynomials, 185
regression, 201
serial correlation, 280
Pooled cross sections across time, 
473n7
Populations. See also Sampling
testing limits on, 139
zero population means, 94, 94–95
Positive serial correlation, 278
defined, 276
Prais, S. J., 293n15
Prais–Winsten method, 293n15, 294, 
295
defined, 293
Precedence, 374–376
Predetermined variables, 428n9
defined, 413
Presidential election (data set), 463
Priors, regression equation and, 68
Probability, 96
Durbin–Watson test, 285n7
linear probability model, 390–397
Processes
autoregressive, 457–458
moving-average, 457–458
Properties
estimators, 106–107
mean, 102–103
OLS coefficient estimators, 107
Two-Stage Least Squares, 424–425
variances, 103–105


547
INDEX
research projects in. See Regression 
projects
sensitivity analysis, 352
single-equation linear, 5
models, 6–8
variations, 8, 8n6
Regression coefficients, 12
double-log functions, 195, 195
estimated, weight/height example, 40
notation, 108
Regression equation
adjusted for degrees of freedom, 54
calculating degrees of freedom in, 70, 
70n3
estimated/estimating, 14–17, 72,  
78, 91
evaluating, 49–50, 72, 78, 91
“i” subscripts in, 13
order of, 14n8
Ordinary Least Squares estimate 
­validity and, 50–54
priors and, 68
quality of, 49–50
stochastic error term in, 9
“t” subscripts in, 14
order of, 14n8
weight guessing, 17–20
Regression lines
goodness-of-fit measures and,  
51, 52
slope, 22, 22
true and estimated, 16, 16–17
Regression projects
advanced data sources, 346–348
checklist, 353, 354–355, 355
data collection, 342–346
practical advice for, 348–352
running, 340–341
topic selection, 341–342
User’s Guide, 356, 357
writing, 352–353
Rejection, of null hypotheses, 117–119, 
120, 123–125
Rejection regions, 119, 120, 133, 135, 
287, 287
Research topics. See Topics
Random walk, defined, 378
Range of sample, functional forms and, 
207–209, 208
Rank condition, 433n11
Rao, Potluri, 167n6
RateMyProfessor.com, 28
ratings data set, 29
Ratio tests, 185n14
Rau, B. Bhaskara, 383n18
Ray, Subhash C., 334n20, 337
Rea, Samuel A., Jr., 409n11
Redefining variables, 321–324,  
323–324
Reduced-form coefficients, 417
Reduced-form equations, 416–417
defined, 416
Redundant variables, 236–238
defined, 237
Regression. See also Regression analysis
autoregressive equations, 367, 378
estimation, 288
Ordinary Least Squares technique 
for, 36
multivariate linear models, 12
polynomial, 201
SAT interactive regression learning 
exercise, 244–272
data set, 248–249
serial correlation and, 282n2
software packages, 319n10, 321, 
321n12
spurious, 56, 379
stepwise, 173n8
Regression analysis, 5–14
applied. See Applied regression 
­analysis
checklist, 354–355
Classical Assumptions, 92–99
defined, 5
example, 17–20
exercise (econometric lab), 63–64
housing prices, 20–23, 22
linear, 193, 194
multivariate coefficients, 12
notation extension, 11–14
practical tips, 350–351


548
INDEX
Sampling distribution
βn, 100–105, 103, 104
simultaneity bias and, 421
Samuelson, Paul A., 1n1
Sanford, Douglas, 28n13
Sastri, V. K., 216, 216n7
SAT interactive regression learning 
­exercise, 244–272
data set for, 248–249
Saunders, Edward M., Jr., 110n9
SC (Schwarz Criterion), 187n19
Schut, Frederick T., 152, 152n16, 153, 
154, 183n13
Schwarz, G., 187n19
Schwarz Criterion (SC), 187n19
Searches. See Specification searches
Seasonal dummies, 146–147
defined, 146
Seasonally-based serial correlation, 276
SE(βn), 105
Second-degree (quadratic) polynomial 
equations, 200, 200, 201
Second-order serial correlation, 277, 
289n10
Sego, Bob, 246n7
Selection
critical values, 130
functional form, 201, 201
independent variables, 157–158.  
See also Independent variables
applied regression analysis, 67–68, 
74–75, 90
level of significance, t-test, 126–127
Semilog
left, 199, 208
right, 199, 208
Semilog functional form, 196–199, 
198, 201
defined, 196
Sensitivity analysis, 72, 177
defined, 174
Sequences, time-series models, 384–385
Sequential binary logit, defined, 406
Sequential specification searches, 
170–171
defined, 170
RESET (Ramsey Regression ­Specification 
Error Test), 185–186
equations, 186, 186n16
Residual analysis, 164
Residual sum of squares (RSS), 48–49, 
48n6, 143, 145, 145n13
defined, 48
Residuals
defined, 15
estimated regression equation, 16
heteroskedasticity, 314, 315,  
316–318, 322
Ordinary Least Squares estimate and, 
36–37
serial correlation, 280n1
Restaurant locations. See Woody’s 
­restaurant locations example
Results, documenting, 72–73, 78–79, 
91
Rezende, Leonardo, 88, 88n12,  
182n12
Rho (ρ), 275–277
Right-hand-side variables, 3n3
Right-side semilog, 199, 208
RMSE (root mean square error 
­criterion), defined, 446
Roe, Brian E., 217, 217n9
Romley, John, 409n12
Root mean square error criterion 
(RMSE), defined, 446
Ross, Douglas, 28n13
Rounding errors, 39
RSS (residual sum of squares), 48–49, 
48n6, 143, 145, 145n13
defined, 48
Rubinfeld, Daniel I., 399n4, 456n8, 
457n10
Rules. See Decision rules
Rush, Racelle, 150n15
Salon haircuts (data set), 488
Sample range, incorrect functional 
forms and, 207–209, 208
Samples
increasing size of, 238
non-random, 467–468


549
INDEX
Simons, James, 368n2
Simple correlation coefficients,  
232–233, 232n3, 233n4
defined, 232
Simple lags, 365
Simulation, forecasting in, 456
Simultaneity bias, 418–419
defined, 418
example, 419–420, 421
sampling distribution, 421
Simultaneous equation models, 449, 
454–456
Simultaneous equations, 3n3, 411–412
bias of Ordinary Least Squares, 
418–421
Classical Assumptions and, 415, 416
identification problem, 430–434
reduced-form, 416–417
structural, 413
systems, nature of, 412–417
Two-Stage Least Squares, 421–429
Single-equation linear regression 
­analysis, 5
models, 6–8
Single-independent-variable models, 
estimating with OLS, 35–40
Six steps in applied regression analysis,  
defined, 66. See also Applied 
­regression analysis, steps in
Slope coefficient (β1), 7–8, 69–70, 71
defined, 7
hypothesizing expected signs of, 
68–69, 69n2, 75, 90
Slope dummy
defined, 204
variables, 203–206, 205
Slopes
regression line, 22, 22
slope and intercept dummies, 205
Small macromodel (data set), 426
Software. See also EViews; Stata
Durbin–Watson statistic, 288
heteroskedasticity and, 319n10, 321, 
321n12
for OLS estimation of multivariate 
regression models, 43
Serial correlation
bias in dynamic models, 371–374
chi-square tests in, 373
Classical Assumptions, 273, 275, 282, 
371–372
consequences, 281–284
corrections, 373–374
detection of, 284–291
Durbin–Watson test, 284–289
dynamic models and, 371–374
equations, 371
error terms, 371–372
observation of, 96
exercise (econometric lab), 303–305
first-order. See First-order serial 
­correlation
forecasting, 449, 451–452
Generalized Least Squares, 292–295
hypothesis testing, 283–284
impure, 278–281, 279, 281, 365, 373
Lagrange Multiplier test, 372–373
negative, 276, 279
Newey–West standard errors, 295–296
no (absent), 278
Ordinary Least Squares, 292–295
positive, 276, 278, 287
pure, 275–278, 282, 373
remedies for, 291–296
seasonally-based, 276
second-order, 277, 289n10
statistics, 283n3
t-scores, 283–284, 296
testing for, 284–291
in dynamic models, 372–373
unreliability, 283n3
values, 280n1
Severe multicollinearity, 227, 366, 370
remedies for, 235–238
Shifting demand curve, 432
Shifting supply curve, 431, 432
Shiller, Robert J., 444n2
Sign, unexpected vs. expected, 348–349
Significance
F-test, 144–146, 144n12
level. See Level of significance, t-test
Silva, Fabio, 26n12


550
INDEX
Standard deviations, 107
error terms, notation for, 108
estimated coefficient terms, notation 
for, 108
Standard econometric notation,  
107–108, 108
Standard errors
border values and, 130n8
coefficients, 72, 73n4, 78, 78n7, 97, 
97n5
estimated, 78, 78n7
confidence level and, 126
data mining and, 173
heteroskedasticity and, 313–314, 
314n4
heteroskedasticity-corrected, 321, 
323n11
Newey–West. See Newey–West 
­standard errors
SE(βn), 105
White, 321n12
Standard Normal Distribution, 99
Stanford University Durbin–Watson 
tables, 289n10
Stata, 72
Durbin–Watson test, 288, 289n10
Lagrange Multiplier test, 289n11
p-value, 127n5
Prais–Winsten method, 294, 294n16
Ramsey Regression Specification Error 
Test, 185, 185n17
specification exercise, 217
terminology used by, 145n13
using, 30–34
Woody’s restaurant data set from, 
76–77
Stationarity, definitions of, 377n11
Stationary
defined, 377
time series, 377, 458
Statistical Abstract of the United States, 
345n2
Statistics
Durbin–Watson test. See  
­Durbin–Watson statistic
heteroskedasticity, 313n3
Sonstelle, Jon, 26n12
Sources, for project data, 345
advanced sources, 346–348
Soviet defense spending (data set), 301
Specification
bias, 158
criteria. See Specification criteria
defined, 67
errors, 157–158
exercise (econometric lab), 217–220
heteroskedasticity, 307
models, 67–68, 74–75, 90
multicollinearity, 228
omitted variable bias and, 158
searches. See Specification searches
Specification criteria, 166–167,  
185–188
Akaike’s Information Criterion, 
187–188
Bayesian Information Criterion, 
187–188
definitions, 166
misuse, 167–169
Ramsey’s Regression Specification 
Error Test, 185–186
Schwarz Criterion, 187–188
use cautions, 184
Specification errors, 157–158
definitions, 68, 157
Specification searches, 169–174
best practices, 170
bias, causes of, 171–172
data mining, 172–173
sensitivity analysis, 174
sequential, 170–171
Spurious correlation, 376–385
cointegration, 382–384
defined, 376
Dickey–Fuller test, 382–384
nonstationarity and, 376–385
spurious regression and, 379
time series, 377–378
sequence of steps for dealing with, 
384–385
Spurious regression, 56, 379
Srinivasan, T. N., 186n18


551
INDEX
t-scores, 126, 167, 168
multicollinearity, 227–228, 235–236
serial correlation, 283–284, 296
t-statistic, 121–123
defined, 121
“t” subscript, in regression equation, 14
order of, 14n8
t-test, 121–139
bias, 171–172
confidence intervals, 139–142
confidence level, 126–127
decision rules, 123–125
estimated logit coefficients, 400n6
examples, 129–136
“importance” and, 138–139
level of significance, choosing,  
126–127
limitations, 137–139
null hypothesis border, 122
one-sided, 125
examples, 129–133, 133
p-values and, 127–128
population, limits on, 139
specification criteria, 166
independent variable selection 
­example, 177
misuse example, 168
specification search bias and, 171–172
t-statistic, 121–123
theoretical validity, 137–138
two-sided, 125
examples, 134–136, 135
t-value, 78, 78n7
critical, t-test and, 119, 123–125, 130, 
132, 133, 135
estimating, 130–131
Tan, Alexander, 389, 389n21
Terza, Joseph V., 113n10
Tests/testing
Breusch–Godfrey, 289n11
Breusch–Pagan, 316–318, 320
chi-square. See Chi-square test
Dickey–Fuller, 382–384
Durbin–Watson. See Durbin–Watson 
test
errors, 118–119
serial correlation, 283n3
t-tests, 121–123
Steigerwald, Doug, 482n12
Stepwise regression, 173n8
Stochastic component, regression 
­equation, 9
Stochastic error terms, 94, 94–95,  
95n2, 96
components, 8–11
defined, 8
notation, 108
omitted variables, 159
Stock, J., 424n6
Stock, James, 333, 333n18, 428n9
Stock prices
data set, 212–213
forecasting and, 447, 447–449
Stone, J. H., 190n1
Stone, J. R., 1n1
Stone, Joe, 461n14, 462n15, 463
Structural coefficients, 413
Structural equations, defined, 413
Student consumption (data set), 229
Subscripts, order of, 14n8
Sum of squares
explained, 48–49
residual, 48–49, 48n6
total, 47, 49
Summation symbol (Σ), 36n1
Durbin–Watson test, 284–285,  
285n6
Ordinary Least Squares and, 36, 38
Summed squared residuals, 37, 38, 
42–43
Summers, Lawrence H., 172n7
Supply and demand models, 414, 416, 
437–438
Surveys
administration, 473n7
best practices, 347n4
regression project, 347
Symbols, used for stochastic error term, 
8–9
t-distribution, estimated logit 
­coefficients, 400n6


552
INDEX
Timmerman, A. G., 444n3
Tissot, B., 444n3
Tolerance, 235
Topics
data types for, 343–345. See also Data 
collection
selecting for regression projects, 
341–342
potential sources, 342
Total sum of squares (TSS), 49, 207
defined, 47
Transformations, Y, 206–207
Treatment groups, 465–472, 472
defined, 466
Trends, Durbin–Watson test, 285n7
True, defined, 15n9
True relationships, between variables, 16
TSS (total sum of squares), 49, 207
defined, 47
Tukey, John, 160n2
Two-sided test
defined, 117
t-test, 125
examples of, 134–136, 135
Two-Stage Least Squares (2SLS),  
421–429
defined, 422
example, 425–429
explained, 422–424
identification problem, 430–434
instrumental variables, 421–422
naive linear Keynesian macroeco-
nomic model, 425–429, 427n7
order condition, 433–434
properties of, 424–425
simultaneity bias and, 422
simultaneous equations and, 411
Two-tailed test, 117
2SLS. See Two-Stage Least Squares 
(2SLS)
Type I Errors, 118–119
border values and, 130n8
critical t-values, 123
data mining and, 173
defined, 118
level of significance and, 126
Tests/testing (continued)
F-test, 142–147, 376, 376n10
Granger causality, 374–376
Hausman, 484
for heteroskedasticity, 314–320
hypothesis. See Hypothesis testing
“importance” and, 138–139
Lagrange Multiplier. See Lagrange 
Multiplier (LM) test
likelihood ratio, 185n14
null hypotheses and, 155–156
one-sided, 117
Park, 317n8
population, limits on, 139
Ramsey Regression Specification Error 
Test, 185–186
ratios, 185n14
for serial correlation in dynamic 
models, 372–373
t-test, 121–139. See also t-test
unreliability, serial correlation and, 
283n3
White. See White test
Theoretical models, in applied regres-
sion analysis, developing, 66–67, 
74, 89–90
Theoretical validity, 137–138
Theory, specification criteria, 166
independent variable selection 
­example, 177
misuse example, 168
Time lags, 412n1
variables, 202–203, 413, 416, 423
Time series, 14
nonstationary, 377–378
stationary, 377–378
studies, 274–275
Time-series models, 364–365
dynamic models, 367–371
Granger causality, 374–376
heteroskedasticity in, 311
sequences, 384–385
serial correlation and dynamic 
­models, 371–374
spurious correlation, 376–385
stationary, 458


553
INDEX
Variables
bias, 171–172
dependent. See Dependent variables
dominant, 224
dropping, 162n4, 164, 170, 171
dummy. See Dummy variables
endogenous, 412–413
errors in the, 440–442
exogenous, 412–413
explanatory. See Independent variables
functional (mathematical) form of, 
67–68, 74–75, 90
independent. See Independent variables
instrumental, 421–422, 442
irrelevant, 165–167
linear in the, 192–193
movement of, 6
multicollinearity, 222n1
omitted. See Omitted variables
predetermined, 413
proxy, 346
random walk, 378
redefining, 321–324, 323–324
redundant, 236–238
relationship between, 412–413
right-hand-side, 3n3
single-independent-variable models, 
OLS and, 35–40
slope dummy, 203–206, 205
true relationships between, 16
units of measurement of, 70
Variance
coefficient estimators
notation for, 108
properties, 107
constant, 96–98, 97, 306
decomposition of, 47, 48
error terms, notation for, 108
heteroskedasticity, 307, 309–310
multicollinearity, 226–227, 227
properties, 103–105
Variance inflation factor (VIF),  
233–235, 233n5, 235n6
defined, 234
Variation. See Errors
Veal, M. R., 393n2
Type II Errors, 118–119
defined, 118
level of significance and, 126
Unbiased estimators, 101, 102n7,  
106, 107
defined, 102
Unboundedness, 397–400
Unconditional forecast, defined, 450
Unexpected sign, in regression analysis, 
handling, 348–350
Unit root, defined, 378
Units of measurement, of the variables, 
70–71
Unknown Xs, 449, 450–451
Unobservable heterogeneity, 468
U.S. economy (1945–2014),  
applied regression analysis  
(econometric lab), 89–91
U.S. News and World Report, 60n10
U.S. Panel Survey of Income Dynamics 
(PSID), 474
User’s Guides, regression projects,  
356, 357
Validity
estimates, 49–50
theoretical, 137–138
Values
borders, 130n8
critical, 119
for chi-square test, 327
for Dickey–Fuller test, 382,  
382n17
selecting, 130
t-value. See under Critical values
current, 364
double-log functions, 195, 195
expected, 9
F-value, 143, 145, 145n14
lagged, 364
p-values, 127–128
serial correlation, 280n1
t-values, 130. See also Critical t-values
VanBergeijk, Peter A. G., 152, 152n16, 
153, 154, 183n13


554
INDEX
Woody’s restaurant locations example, 
73–79
critical t-test values, 124, 125
data set from Stata, 76–77
data source for, 73n6
heteroskedasticity, 317–318, 320
irrelevant variables and, 165–166
omitted variable bias, 162
p-value, 128
two-sided t-test, 135
Wooldridge, Jeffrey M., 186n18, 401n7, 
473n7
Writing, regression projects, 352–353
Wunnava, P., 484n14
X variables
simultaneous equations and,  
412–413
unknown, 449, 450–451
X,Y coordinate system, 69, 70
mathematical vs. statistical fit in, 
69–70, 70, 71
Y variables
simultaneous equations and,  
412–413, 423
transformations, 206–207
variations
additional, 8, 8n6
sources, 8, 9
Yogo, M., 424n6
Zimmerman, K. F., 393n2
VIF (variance inflation factor),  
233–235, 233n5, 235n6
defined, 234
Vigen, Tyler, 55n7
Vinod, H. D., 290n12
Visco, Ignazio, 164n5
Ward, Michael, 375n9
Watson, G. S., 284n4
Watson, Mark, 333, 333n18, 428n9
Weak stationarity, 377n11
Weight-guessing equation, 20
forecasting and, 444–445
using height data, 17–18, 19
Weight/height data
estimated regression coefficients, 40
regression analysis (econometric lab), 
63–64
weight-guessing equation using, 
17–18, 19
Weighted Least Squares (WLS), 323n11, 
323n13
Weighting schemes, geometric, 369
West, K. D., 295n17
White, Halbert, 107n8, 318n9, 321
White standard errors, 321n12
White test, 290n12, 318–320, 321
alternative form, 320n11
defined, 318
Wide distribution, 308, 309
Wide-sense stationarity, 377n11
Winsten, C. B., 293n15
WLS (Weighted Least Squares), 323n11, 
323n13
Women’s participation in labor force 
(data set), 396


This page intentionally left blank


This page intentionally left blank


This page intentionally left blank


This page intentionally left blank
