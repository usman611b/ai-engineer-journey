"""
LESSON 6 - JOINT, MARGINAL, AND CONDITIONAL DISTRIBUTIONS
=========================================================

So far we studied one variable at a time. Now we ask how TWO variables behave
together. Run with:

    python 10_joint_and_marginal_distributions.py


===============================================================================
1. TWO RANDOM VARIABLES
===============================================================================

Let:

    W = weather, with values {rain, dry}
    U = umbrella, with values {yes, no}

A joint outcome describes both variables:

    (rain, yes)
    (rain, no)
    (dry, yes)
    (dry, no)

A joint distribution assigns probability to every combination.


===============================================================================
2. JOINT DISTRIBUTION
===============================================================================

Example table:

                    Umbrella yes    Umbrella no    row total
    Rain                 0.36            0.04          0.40
    Dry                  0.12            0.48          0.60
    column total         0.48            0.52          1.00

Each cell is a joint probability:

    P(W=rain AND U=yes)=0.36

Joint means "together." The table must contain nonnegative values and all cells
must add to 1.


===============================================================================
3. MARGINAL DISTRIBUTION: SUM OUT WHAT YOU DO NOT NEED
===============================================================================

Suppose we only care about weather. Umbrella status becomes irrelevant, so add
across it:

    P(rain)=P(rain,yes)+P(rain,no)
           =0.36+0.04
           =0.40

    P(dry)=0.12+0.48=0.60

This is the marginal distribution of W. The word "marginal" comes from totals
written in the margins of a table.

To find the umbrella marginal, add down weather possibilities:

    P(yes)=0.36+0.12=0.48
    P(no)=0.04+0.48=0.52

General discrete rule:

    P(X=x) = sum over all y of P(X=x,Y=y)

"Marginalize Y" means sum over every possible Y because we do not need to know
which Y happened.


===============================================================================
4. CONDITIONAL DISTRIBUTION: FOCUS AFTER EVIDENCE
===============================================================================

Question: what is P(rain | umbrella=yes)?

Once we know umbrella=yes, only that column remains possible. Its total is 0.48.
The rain-and-yes portion is 0.36:

    P(rain | yes)=P(rain and yes)/P(yes)
                 =0.36/0.48
                 =0.75

Before evidence, P(rain)=0.40. After seeing an umbrella, it becomes 0.75. The
evidence changes our belief.

The conditional probabilities inside one given condition must sum to 1:

    P(rain|yes)+P(dry|yes)=0.75+0.25=1


===============================================================================
5. INDEPENDENCE USING THE JOINT TABLE
===============================================================================

W and U would be independent if every cell factorized:

    P(W=w,U=u)=P(W=w)*P(U=u)

Check rain and yes:

    actual joint = 0.36
    product of marginals = 0.40*0.48 = 0.192

They are not equal, so the variables are dependent. This fits intuition: seeing
an umbrella provides information about rain.


===============================================================================
6. AI CONNECTIONS
===============================================================================

Supervised learning starts with a joint data distribution:

    P(features, label)

A classifier tries to learn the conditional:

    P(label | features)

Generative models may model a joint distribution over many variables. Missing
or hidden variables are marginalized by summing/integrating over possibilities.

In language models:

    P(next token | previous tokens)

is a conditional distribution. The previous context is the evidence.


===============================================================================
7. COMMON CONFUSIONS
===============================================================================

1. Joint means probability of variables together, not addition of marginals.
2. Marginalization sums out a variable; conditioning restricts and renormalizes.
3. P(X|Y) generally differs from P(Y|X).
4. A joint table totals 1; each marginal also totals 1.
5. Independence requires factorization for all combinations, not just one lucky
   matching cell.

Mental flow:

    joint table -> sum rows/columns -> marginals
    joint cell / evidence marginal -> conditional
"""


JOINT = {
    ("rain", "yes"): 0.36,
    ("rain", "no"): 0.04,
    ("dry", "yes"): 0.12,
    ("dry", "no"): 0.48,
}


def validate_joint(joint):
    if any(p < 0 for p in joint.values()):
        raise ValueError("Joint probabilities cannot be negative.")
    if abs(sum(joint.values())-1) > 1e-9:
        raise ValueError("A joint distribution must sum to 1.")


def marginal_first(joint):
    """Sum out the second variable."""
    validate_joint(joint)
    result={}
    for (first, _second), probability in joint.items():
        result[first]=result.get(first,0)+probability
    return result


def marginal_second(joint):
    """Sum out the first variable."""
    validate_joint(joint)
    result={}
    for (_first, second), probability in joint.items():
        result[second]=result.get(second,0)+probability
    return result


def conditional_first_given_second(first, second, joint):
    second_marginal=marginal_second(joint)
    return joint[(first,second)]/second_marginal[second]


def demonstrate_joint():
    print("\n"+"="*78)
    print("DEMO 1 - JOINT TABLE")
    print("="*78)
    for pair,probability in JOINT.items():
        print(f"P{pair}={probability}")
    print("Total=",sum(JOINT.values()))


def demonstrate_marginals():
    print("\n"+"="*78)
    print("DEMO 2 - SUM OUT VARIABLES")
    print("="*78)
    weather=marginal_first(JOINT); umbrella=marginal_second(JOINT)
    print("P(rain)=0.36+0.04=",weather["rain"])
    print("P(dry)=0.12+0.48=",weather["dry"])
    print("P(yes)=0.36+0.12=",umbrella["yes"])
    print("P(no)=0.04+0.48=",umbrella["no"])


def demonstrate_conditional():
    print("\n"+"="*78)
    print("DEMO 3 - CONDITION ON UMBRELLA=YES")
    print("="*78)
    p=conditional_first_given_second("rain","yes",JOINT)
    print("P(rain|yes)=P(rain,yes)/P(yes)")
    print("           =0.36/(0.36+0.12)")
    print("           =",p)
    print("P(rain) was",marginal_first(JOINT)["rain"],"so evidence changed belief.")


def demonstrate_independence():
    print("\n"+"="*78)
    print("DEMO 4 - INDEPENDENCE CHECK")
    print("="*78)
    weather=marginal_first(JOINT); umbrella=marginal_second(JOINT)
    product=weather["rain"]*umbrella["yes"]
    print("Actual P(rain,yes)=",JOINT[("rain","yes")])
    print("P(rain)*P(yes)=",product)
    print("Not equal -> weather and umbrella are dependent.")


def practice_questions():
    print("\n"+"="*78)
    print("PRACTICE - ANSWER BEFORE READING SOLUTIONS")
    print("="*78)
    print("""
1. What does P(X=x,Y=y) describe?
2. How do you get P(X=x) from a joint table?
3. How does marginalization differ from conditioning?
4. What factorization identifies independence?
5. What conditional distribution does a classifier learn?

Solutions:
1. The probability that both variable values occur together.
2. Sum P(X=x,Y=y) over all possible y.
3. Marginalization sums possibilities out; conditioning focuses and renormalizes.
4. P(X,Y)=P(X)P(Y) for every combination.
5. P(label | features).
""")


def main():
    demonstrate_joint(); demonstrate_marginals(); demonstrate_conditional()
    demonstrate_independence(); practice_questions()


if __name__=="__main__":
    main()
