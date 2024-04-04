# KeystrokeDynamics
Behavioral biometry using the dynamics of keystrokes.

This program calculates the average time a key is down.

- I typed the same randomly generated paragraph two times into the program. We can clearly see the times are a bit similar.
```sql
Key,AverageHoldTime
a,0.12036086453331836
b,0.08013860384623205
c,0.09903676169259203
d,0.10900113799355243
e,0.1101579223711466
f,0.11149962743123366
```

```sql
Key,AverageHoldTime
a,0.12003011173672146
b,0.09202059110005689
c,0.11838650703430172
d,0.11552436351776116
e,0.11189294583869702
f,0.10400636990865066
```

- of course, the more samples you obtain (that is the more text you write), the more accurate it will become
- the letter E was written 99 times, and the two values (0.11015, 0.11189) are very close to each other
- I haven't had the opportunity nor the will to test this on another person, I will do that later on

## TODO:
- I am planning to rewrite this when I have time, but using a different approach, to make it more reliable, so probably measuring how long it takes to press a certain key