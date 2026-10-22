# Probability: the basics, sets, conditional probability and counting

The language of chance. Everything else in this folder builds on it.

## Probability: the basics

- **Probability** is a number from 0 (impossible) to 1 (certain) saying how likely an event is.
- **Probability vs likelihood.** Probability quantifies what you expect to happen given a model (a fair coin gives heads with probability 0.5). Likelihood quantifies how well a model fits what you saw (52 heads in 100 flips makes "fair coin" fairly believable).
- **Two views.** Count outcomes (equally likely cases: probability = favorable outcomes ÷ all outcomes), or treat it as an informed degree of belief (a 67% chance the home team wins). The mathematics is the same either way.
- **Vocabulary.** *Random experiment* (a process with an uncertain result), *outcome* (one result), *sample space S* (all outcomes), *event* (a set of outcomes), *trial* (one run of the experiment).
- **Key words.** "Or" and "at least" mean union; "and" and "all of" mean intersection.
- **The three axioms.** (1) P(A) ≥ 0. (2) P(S) = 1. (3) For disjoint events, P(A1 ∪ A2 ∪ …) = P(A1) + P(A2) + …
- **Rules that follow from the axioms:**
  - Complement: P(not A) = 1 − P(A).
  - P(empty set) = 0, and P(A) ≤ 1.
  - P(A − B) = P(A) − P(A ∩ B).
  - **Addition rule (inclusion–exclusion):** P(A ∪ B) = P(A) + P(B) − P(A ∩ B). For three events: add the singles, subtract the pairs, add the triple.
  - If A is inside B, then P(A) ≤ P(B).
- **Worked example.** Rain today 60%, rain tomorrow 50%, no rain either day 30%. Rain today or tomorrow = 1 − 0.3 = 0.7. Both days = 0.6 + 0.5 − 0.7 = 0.4. Today only = 0.6 − 0.4 = 0.2.
- **Equally likely outcomes.** For a fair die each face is 1/6 (the six probabilities must add to 1). Probability is defined for sets, so "P(2)" really means P({2}).

## Sets (the language of events)

- **Venn diagram:** a closed region for each set inside the rectangle of the universal set S.
- **Union** (in A or B), **intersection** (in both), **complement** (in S but not A), **difference** A − B = A ∩ (not B).
- **Disjoint (mutually exclusive):** no shared elements. A **partition** is a collection of non-empty disjoint sets whose union is the whole set.
- **De Morgan's laws:** the complement of a union is the intersection of the complements; the complement of an intersection is the union of the complements.
- **Distributive laws:** A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C), and A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C).
- **Cartesian product** A × B: ordered pairs; **multiplication principle:** |A × B| = |A| × |B|.
- **Inclusion–exclusion for counting:** |A ∪ B| = |A| + |B| − |A ∩ B|.
- **Countable vs uncountable.** The whole numbers, integers and rationals are countable (you can list them). Any interval of real numbers is uncountable. This is why continuous variables need densities, not lists.
- **Function:** a rule from a domain to a co-domain; the *range* is the set of values it actually produces.

## Conditional probability, independence, Bayes

- **Definition:** P(A|B) = P(A ∩ B) / P(B), when P(B) > 0. Intuition: once B is known, throw away every outcome outside B and rescale.
- **P(A|B) is not P(B|A).** Example: if a person has dengue, there is a 90% chance the test is positive. If a person tests positive, there may be only a 15% chance they have dengue, because false positives are common. Swapping them is the **base rate fallacy**.
- **Independence:** A and B are independent if P(A|B) = P(A), equivalently P(A ∩ B) = P(A) P(B). Independent examples: two coin tosses. Not independent: rain in two nearby cities; two cards drawn without replacement.
- **Chain (multiplication) rule:** P(A ∩ B) = P(A) P(B|A). For three events: P(A) P(B|A) P(C|A,B). Tree diagrams multiply along branches.
- **Law of total probability:** for a partition B1, B2, …: P(A) = Σ P(A|Bi) P(Bi). Example: three bags of marbles chosen at random give P(red) = 0.60.
- **Bayes' theorem:** P(A|B) = P(B|A) P(A) / P(B), where P(B) comes from the law of total probability. It reverses a conditional probability.
- **The disease-test example:** incidence 0.1%, no false negatives, false-positive rate 5%. Of 1,000 people, 1 has the disease and about 50 test positive without it, so P(disease | positive) ≈ 1/51 ≈ **2%**. Over 98% of positives are healthy. A version of this question was reportedly given to doctors and medical students in a 1978 study, and only about 18% answered correctly. *Lesson:* a test's accuracy and the chance a positive is right are different numbers, and the base rate drives the second.
- **Two-child problem.** Given the first child is a girl, P(two girls) = 1/2. Given only that at least one child is a girl, P(two girls) = 1/3. The information differs, so the answer differs.
- **Tip:** turn probabilities into counts ("imagine 4,000 families") to check your intuition.

## Counting

- **Multiplication rule:** m choices then n choices gives m × n ways (3 appetizers × 5 mains × 2 desserts = 30).
- **Factorial:** n! = n × (n−1) × … × 1 (the number of orderings of n different things; 4 letters give 24 arrangements).
- **Permutations (order matters):** P(n,k) = n! / (n−k)!
- **Combinations (order does not matter):** C(n,k) = n! / (k! (n−k)!)
- **Probability by counting:** favorable ÷ total, with both counted by permutations or combinations. Example: 6 numbers from 48 has C(48,6) = 12,271,512 equally likely draws.
- **Birthday problem.** With 5 people the chance two share a birthday is about 2.7%; with 30 people about 70.6%. (With 23 people it passes 50%.) It is surprising because the number of *pairs* grows much faster than the number of people.
