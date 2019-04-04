TVM - Time Value of Money
=========================

:Author: Ken Kundert
:Version: 0.3.0
:Released: 2019-04-04


What?
-----

Time value of money calculations relate the following quantities:

- future value
- present value
- payments
- number of periods
- discount rate

*tvm* computes one of these values (other than discount rate) given the others.

The number of periods is split between two values, the number of years and the 
number of periods per year (the frequency).


Getting Started
---------------

Install using::

    pip3 install --user tvm

This installs *tvm* to ~/.local/bin; make sure this directory is on your path.

Usage::

    tvm [options] [fv|pv|pmt|years]

Options::

    -f <val>, --fv <val>     future value
    -p <val>, --pv <val>     present value
    -P <val>, --pmt <val>    payment per period
    -y <val>, --years <val>  total number of years
    -n <val>, --freq <val>   number of payments per year
    -r <val>, --rate <val>   annual discount rate
    -i, --ignore             ignore any previously specified values

If a value is not given it is recalled from the previous invocation.
Specify --ignore to use the default values for all unspecified options,
which are: pv=0, fv=0, pmt=0, years=30, freq=12.

When the program runs, it always prints the computed value first, and then 
prints the remaining values to make it easy for you to confirm that you used the 
right values.

Savings Accounts
----------------

Consider case where you have a interest bearing account that pays 5% per annum 
compounded monthly. If you start with $10,000, you can compute the amount you 
will have after 5 years with::

    tvm --pv=10000 --rate=5 --freq=12 --years=5 fv

The amount in 5 years is referred to as the future value (fv). The current 
amount is the present value (pv). The frequency is the number of periods per 
year. The program responds with::

    fv = $12,833.59
    pv = $10,000.00
    pmt = $0.00
    r = 5%
    N = 60

*N* is the total number of periods and equals the product of the years and the 
number of periods per year.

You can specify values with SI scale factors, units, and commas.  The units and 
commas are ignored. So you can do the same thing with either::

    tvm --pv='$10,000' --rate=5% --freq=12 --years=5 fv

or::

    tvm --pv=10k --rate=5% --freq=12 --years=5 fv

The quotes are needed in the first case to prevent $ from being interpreted by 
the shell.

*tvm* remembers the values specified on the previous invocation and uses them if 
they are not specified.  This allows you to rapidly run what-if experiments 
without having to re-specify values that do not change.
So, once you have run the first command, you can now quickly determine how much 
you will have in 10 years using::

    tvm -y 10

    fv = $16,470.09
    pv = $10,000.00
    pmt = $0.00
    r = 5%
    N = 120

Without changing anything else, you can determine what happens if you make an 
additional $100 contribution each month::

    tvm --pmt 100

    fv = $31,998.32
    pv = $10,000.00
    pmt = $100.00
    r = 5%
    N = 120


Loans
-----

You can also use *tvm* to explore loans.  For example, you can compute the 
payment for a mortgage given the principal, interest rate, and length::

    tvm --ignore --pv=-250k --rate=4.375 --years=30 pmt

    pmt = $1,248.21
    pv = -$250,000.00
    fv = $0.00
    r = 4.38%
    N = 360

The --ignore option was added so that we start from scratch; any values that
were previously specified are ignored.

You can now understand how paying a little extra affects how long it takes
to pay off the loan using::

    tvm --pmt=1.5k years

    years = 21.42
    pv = -$250,000.00
    pmt = $1,500.00
    fv = $0.00
    r = 4.38%
    N = 257.08

To compute the payments for a 5-year interest only balloon mortgage, use::

    tvm -y 5 -f -250k pmt

    pmt = $911.46
    pv = -$250,000.00
    fv = -$250,000.00
    r = 4.38%
    N = 60
