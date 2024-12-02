# getting used to the time taken to factorise large semiprimes
a=$(openssl prime -generate -bits 24)
b=$(openssl prime -generate -bits 24)
echo 'using prime factors' $a 'and' $b
c=$(echo "$a*$b" | bc)
echo 'their product is' $c
echo 'factorisation took'
time factor $c
