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
