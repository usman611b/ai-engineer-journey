"""
LESSON 6 - CENTRAL LIMIT THEOREM (CLT)
=======================================

Goal: take a non-Gaussian distribution, repeatedly average independent samples,
and watch the distribution of those averages become bell-shaped.

Run with:

    python 11_central_limit_theorem.py


===============================================================================
1. WHAT THE CLT SAYS
===============================================================================

Under useful conditions, if we:

    1. draw many independent observations from a population,
    2. calculate their sample mean,
    3. repeat the whole experiment many times,

then the distribution of those repeated sample means becomes approximately
Normal as sample size grows, even when the original population is not Normal.

Critical distinction:

    CLT does not say the raw data becomes Normal.
    It says the sampling distribution of sums/means becomes approximately Normal.


===============================================================================
2. START WITH A FAIR DIE
===============================================================================

One die is uniform, not Gaussian:

    1  2  3  4  5  6
    #  #  #  #  #  #

Its expected value is 3.5. We use it precisely because the starting distribution
is clearly not bell-shaped.


===============================================================================
3. THE ROADMAP FUNCTION
===============================================================================

    def demonstrate_clt(dist_fn, n_samples, n_averages):
        averages=[]
        for _ in range(n_averages):
            samples=[dist_fn() for _ in range(n_samples)]
            avg=sum(samples)/len(samples)
            averages.append(avg)
        return averages

Parameters:

    dist_fn    -> where does each original random value come from?
    n_samples  -> how many values are averaged in one experiment?
    n_averages -> how many times do we repeat that experiment?

We store averages, not individual die rolls.


===============================================================================
4. n_samples=1
===============================================================================

Each experiment rolls one die:

    experiment 1 -> [3] -> average 3
    experiment 2 -> [6] -> average 6
    experiment 3 -> [1] -> average 1

The average of one value is that value, so the histogram remains roughly flat.
No bell shape yet.


===============================================================================
5. n_samples=2
===============================================================================

Examples:

    [2,5] -> average 3.5
    [4,3] -> average 3.5
    [1,1] -> average 1.0

Many pairs create central averages:

    1+6, 2+5, 3+4, 4+3, 5+2, 6+1 -> average 3.5

Only one pair creates average 1:

    1+1

Therefore central averages become more common than extreme averages.


===============================================================================
6. n_samples=30
===============================================================================

One experiment might average 30 rolls to 3.43. Repeated experiments might give:

    3.43, 3.61, 3.48, 3.55, ...

Most averages cluster near 3.5. An average like 1.2 would require many dice to
push toward the same extreme, so it is rare. The histogram becomes bell-shaped.


===============================================================================
7. CENTER AND SPREAD OF SAMPLE MEANS
===============================================================================

If original observations have mean mu and standard deviation sigma:

    mean of sample means = mu
    standard deviation of sample means = sigma/sqrt(n)

The second quantity is called standard error.

As n grows, sqrt(n) grows, so the averages become less spread out. Averaging
stabilizes random noise.

For a fair die:

    mu=3.5
    variance=35/12
    sigma=sqrt(35/12), about 1.708

For n=100, standard error is about 1.708/10=0.1708.


===============================================================================
8. CONDITIONS AND LIMITS
===============================================================================

The beginner version assumes independent, identically distributed observations
with finite mean and variance. More advanced CLTs relax some conditions.

CLT is not magic permission to ignore:

    strong dependence, extremely heavy tails/infinite variance, tiny samples,
    or the fact that approximation quality depends on the original distribution.


===============================================================================
9. AI CONNECTION: MINI-BATCH GRADIENTS
===============================================================================

One training example can produce a noisy gradient. A mini-batch averages:

    (g1+g2+...+g32)/32

The average is generally more stable than a single-example gradient. Under useful
conditions, aggregated noise can become approximately Gaussian-like. This helps
explain why batch size affects gradient variance and training behavior.


===============================================================================
10. COMMON CONFUSIONS
===============================================================================

1. Raw die rolls do not become Normal; repeated averages do.
2. n_samples and n_averages have different jobs.
3. CLT describes an approximation as n grows, not exact Normality at every n.
4. Larger n narrows the distribution by sigma/sqrt(n).
5. Law of Large Numbers says one sample mean stabilizes near mu; CLT describes
   the shape and spread across repeated sample means.

Final flow:

    non-Gaussian source -> average n samples -> repeat -> histogram of averages
    -> approximately Gaussian and increasingly concentrated around mu
"""

import random


def roll_die():
    return random.randint(1,6)


def demonstrate_clt(dist_fn,n_samples,n_averages):
    averages=[]
    for _ in range(n_averages):
        samples=[dist_fn() for _ in range(n_samples)]
        avg=sum(samples)/len(samples)
        averages.append(avg)
    return averages


def mean_and_sd(values):
    mean=sum(values)/len(values)
    variance=sum((x-mean)**2 for x in values)/len(values)
    return mean,variance**0.5


def text_histogram(values,bins=20,width=40):
    low,high=min(values),max(values)
    bin_width=(high-low)/bins or 1
    counts=[0]*bins
    for value in values:
        index=min(int((value-low)/bin_width),bins-1)
        counts[index]+=1
    largest=max(counts)
    for i,count in enumerate(counts):
        left=low+i*bin_width
        bar="#"*round(count/largest*width)
        print(f"{left:5.2f} | {bar}")


def demonstrate_one_dry_run():
    print("\n"+"="*78)
    print("DEMO 1 - ONE EXPERIMENT BY HAND")
    print("="*78)
    samples=[2,5,3,6,1]
    print("samples=",samples)
    print("average=sum(samples)/5 =",sum(samples)/len(samples))
    print("This creates one point in the distribution of sample means.")


def demonstrate_sample_sizes():
    print("\n"+"="*78)
    print("DEMO 2 - INCREASING n")
    print("="*78)
    random.seed(11)
    die_sd=(35/12)**0.5
    for n in (1,2,5,30,100):
        averages=demonstrate_clt(roll_die,n,10_000)
        observed_mean,observed_sd=mean_and_sd(averages)
        theory_sd=die_sd/(n**0.5)
        print(f"n={n:>3}: mean={observed_mean:.3f}, SD={observed_sd:.3f}, theory SE={theory_sd:.3f}")


def demonstrate_shape():
    print("\n"+"="*78)
    print("DEMO 3 - HISTOGRAM OF 30-ROLL AVERAGES")
    print("="*78)
    random.seed(12)
    text_histogram(demonstrate_clt(roll_die,30,20_000))


def practice_questions():
    print("\n"+"="*78)
    print("PRACTICE - ANSWER BEFORE READING SOLUTIONS")
    print("="*78)
    print("""
1. What becomes approximately Normal under the CLT?
2. What does n_samples control? What does n_averages control?
3. Why do averages cluster around 3.5 for a fair die?
4. How does standard error change when n grows from 25 to 100?
5. Give one AI connection.

Solutions:
1. The repeated sampling distribution of sums/means, not necessarily raw data.
2. Values per mean; number of repeated means stored.
3. 3.5 is the population expected value, and extremes cancel through averaging.
4. sigma/sqrt(n) halves because sqrt(100) is twice sqrt(25).
5. Mini-batch averaging reduces gradient noise and stabilizes updates.
""")


def main():
    demonstrate_one_dry_run(); demonstrate_sample_sizes(); demonstrate_shape()
    practice_questions()


if __name__=="__main__":
    main()
