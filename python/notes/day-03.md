# Day 3 — From Individual Values to a Dataset

## What I Learned

Today I learned:

- how to store multiple values in a Python list;
- how to use a `for` loop to process values one by one;
- how to use `if` and `else` inside a loop;
- how to count values that meet a condition.

## What Is a List?

In my own words:

A list is a structure that allows me to store multiple values together. Instead of creating a separate variable for every expression value, I can store several values in one list.

## What Is a For Loop?

In my own words:

A `for` loop goes through the values in a collection one by one. For each value, Python performs the instructions inside the loop.

## My Task

I wrote a program that:

- stores several educational gene expression values in a list;
- checks each value using a `for` loop;
- compares each value with a threshold of 10;
- prints whether each value is high or low;
- counts how many values are above the threshold.

## My Result

The program processed:

6 educational gene expression values.

The number of values above the threshold was:

3.

## My Debugging Experience

The error I intentionally created was:

I wrote the variable name `treshold` instead of `threshold`.

The problem was:

Python could not find the variable because I used a different name from the one I originally created.

I fixed it by:

Changing `treshold` to `threshold`.

## What Was Difficult?

The most difficult part was understanding how the `for` loop works and how the variable inside the loop changes for each value in the list.

At first, it was difficult to understand that the same variable represents a different value during each iteration.

## What I Can Do Now

I can now:

- create a list of numerical values;
- use a `for` loop to process each value;
- use `if` and `else` to classify values;
- count how many values meet a condition.

## Connection to Computational Genomics

A biological dataset may contain many values.

A list and a loop can help a program process these values one by one.

In the future, this idea can be used when working with:

- gene expression values;
- DNA sequences;
- biological measurements;
- genomic datasets.

## Important Limitation

The data used today were educational values, not real experimental data.

The purpose of this exercise was to learn the basic logic of processing a dataset with Python.

## Next Question

How can I organize repeated data-processing logic into a reusable function?
