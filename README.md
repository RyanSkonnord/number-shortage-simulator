# Number Shortage Simulator

Simulates a number shortage as depicted in [xkcd #3009](https://xkcd.com/3009/).

## Usage

The shortage shown in the original comic can be simulated as

```
from number_shortage_simulator import NumberReserve

NumberReserve({2: 15, 3: 12}).print_nubmer_shortage()
```

which produces the output:

```
We have only 15 2s and 12 3s left.
No, wait, 13 2s and 10 3s.
No, wait, 12 2s and 9 3s.
No, wait, 10 2s and 8 3s.
No, wait, 9 2s and 7 3s.
No, wait, 8 2s and 6 3s.
No, wait, 7 2s and 5 3s.
No, wait, 6 2s and 4 3s.
No, wait, 5 2s and 3 3s.
No, wait, 4 2s and 1 3.
```

To simulate a more complex scenario, suppose we begin with 100 of each decimal digit in our reserve. We can set this up as

```
NumberReserve({int(d): 100 for d in SINGLE_DIGITS})
```

In this case, `print_nubmer_shortage()` produces the following output:

```
We have only 100 0s, 99 1s, 100 2s, 100 3s, 100 4s, 100 5s, 100 6s, 100 7s, 100 8s, and 98 9s left.
No, wait, 83 0s, 91 1s, 99 2s, 98 3s, 99 4s, 99 5s, 99 6s, 99 7s, 96 8s, and 83 9s.
No, wait, 82 0s, 89 1s, 97 2s, 96 3s, 98 4s, 98 5s, 96 6s, 97 7s, 90 8s, and 74 9s.
No, wait, 80 0s, 88 1s, 96 2s, 95 3s, 96 4s, 96 5s, 91 6s, 94 7s, 86 8s, and 67 9s.
No, wait, 78 0s, 86 1s, 95 2s, 94 3s, 93 4s, 94 5s, 87 6s, 90 7s, 81 8s, and 61 9s.
No, wait, 76 0s, 83 1s, 94 2s, 91 3s, 90 4s, 93 5s, 84 6s, 88 7s, 75 8s, and 56 9s.
No, wait, 74 0s, 81 1s, 93 2s, 88 3s, 87 4s, 90 5s, 82 6s, 84 7s, 68 8s, and 53 9s.
No, wait, 72 0s, 79 1s, 90 2s, 86 3s, 85 4s, 87 5s, 79 6s, 79 7s, 63 8s, and 48 9s.
No, wait, 70 0s, 78 1s, 89 2s, 84 3s, 82 4s, 86 5s, 76 6s, 74 7s, 56 8s, and 46 9s.
No, wait, 68 0s, 77 1s, 87 2s, 83 3s, 79 4s, 84 5s, 71 6s, 67 7s, 51 8s, and 44 9s.
No, wait, 67 0s, 74 1s, 86 2s, 81 3s, 74 4s, 82 5s, 67 6s, 61 7s, 47 8s, and 43 9s.
No, wait, 66 0s, 71 1s, 84 2s, 79 3s, 69 4s, 81 5s, 61 6s, 57 7s, 44 8s, and 40 9s.
No, wait, 64 0s, 67 1s, 83 2s, 77 3s, 64 4s, 79 5s, 56 6s, 51 7s, 42 8s, and 38 9s.
No, wait, 63 0s, 65 1s, 81 2s, 74 3s, 60 4s, 75 5s, 51 6s, 48 7s, 38 8s, and 37 9s.
No, wait, 61 0s, 61 1s, 80 2s, 71 3s, 58 4s, 71 5s, 48 6s, 44 7s, 33 8s, and 36 9s.
No, wait, 59 0s, 57 1s, 79 2s, 67 3s, 54 4s, 67 5s, 44 6s, 39 7s, 32 8s, and 32 9s.
No, wait, 58 0s, 56 1s, 76 2s, 63 3s, 50 4s, 63 5s, 39 6s, 37 7s, 30 8s, and 30 9s.
No, wait, 54 0s, 55 1s, 75 2s, 56 3s, 48 4s, 57 5s, 37 6s, 32 7s, 28 8s, and 29 9s.
No, wait, 53 0s, 54 1s, 71 2s, 52 3s, 45 4s, 51 5s, 36 6s, 30 7s, 26 8s, and 27 9s.
No, wait, 51 0s, 50 1s, 67 2s, 49 3s, 42 4s, 47 5s, 32 6s, 26 7s, 25 8s, and 25 9s.
No, wait, 49 0s, 49 1s, 61 2s, 47 3s, 36 4s, 44 5s, 28 6s, 24 7s, 23 8s, and 22 9s.
No, wait, 48 0s, 47 1s, 55 2s, 44 3s, 28 4s, 41 5s, 27 6s, 21 7s, 20 8s, and 21 9s.
No, wait, 46 0s, 43 1s, 49 2s, 42 3s, 22 4s, 40 5s, 25 6s, 20 7s, 19 8s, and 18 9s.
No, wait, 43 0s, 40 1s, 43 2s, 39 3s, 17 4s, 38 5s, 24 6s, 18 7s, 15 8s, and 16 9s.
No, wait, 41 0s, 34 1s, 41 2s, 35 3s, 12 4s, 35 5s, 22 6s, 17 7s, 14 8s, and 15 9s.
No, wait, 40 0s, 28 1s, 36 2s, 31 3s, 9 4s, 32 5s, 20 6s, 15 7s, 12 8s, and 13 9s.
No, wait, 37 0s, 23 1s, 31 2s, 24 3s, 7 4s, 30 5s, 19 6s, 12 7s, 11 8s, and 11 9s.
No, wait, 35 0s, 15 1s, 28 2s, 21 3s, 6 4s, 27 5s, 17 6s, 9 7s, 9 8s, and 8 9s.
No, wait, 34 0s, 11 1s, 24 2s, 19 3s, 3 4s, 26 5s, 15 6s, 8 7s, 6 8s, and 6 9s.
No, wait, 33 0s, 6 1s, 21 2s, 15 3s, 2 4s, 23 5s, 11 6s, 7 7s, 5 8s, and 5 9s.
```
