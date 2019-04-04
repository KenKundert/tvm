TVM - Time Value of Money
=========================

:Author: Ken Kundert
:Version: 0.0.0
:Released: 2019-01-16


What?
-----

*tvm* computes one of the future value, present value, payment, or number of 
periods given the interest rate and given the remaining values.


Savings Accounts
----------------

For example, consider case where you have a interest bearing account that pays 
5% per annum compounded monthly. If you start with $10,000, you can compute the 
amount you will have after 10 years with::

    tvm --pv=10000 --rate=5 --freq=12 --years=5 fv

The value in 5 years is referred to as the future value (fv). The current amount 
is the present value (pv). The frequency is the number of periods per year. The 
program responds with::

    fv = $12,833.59
    pv = $10,000.00
    pmt = $0.00
    r = 5%
    N = 60

You can specify values with SI scale factors, units, and commas.  So you can do 
the same thing with either::

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
payment for a mortgage given the principal and interest rate::

    tvm --ignore --pv=-250k --rate=4.375 --years=30 pmt

    pmt = $1,248.21
    pv = -$250,000.00
    fv = $0.00
    r = 4.38%
    N = 360

The --ignore option was added so that we start from scratch; any values that
were previously specified are ignored.

You can now understand how paying a little extra affects how long it takes
to pay off the loan::

    tvm --pmt=1.5k years

    years = 21.42
    pv = -$250,000.00
    pmt = $1,500.00
    fv = $0.00
    r = 4.38%
    N = 257.08


Getting Started
---------------

Install using::

    pip3 install --user tvm

This installs *tvm* to ~/.local/bin; make sure this directory is on your path.
