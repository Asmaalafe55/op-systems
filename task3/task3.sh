echo "The name of the directory I am currently in: "
pwd
echo "Which bash I am ?"
which bash
echo "The files in the directory I am currently in: "
ls
echo "In how much lines does small_airports appears in file airports: "
grep "small_airport" airports.csv | wc -l
