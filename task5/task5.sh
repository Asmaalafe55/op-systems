echo "The files in the directory before the command: "
ls
start_time=$(date +%s)
echo "Starting process..."

# while loop to gread rows from the "airports.csv" file
# in every row we add this row to a file whith the same name of the third column

while IFS= read -r line; do
fileName=$(echo "$line" | cut -d ',' -f 3)
echo "$line" >> "${fileName}.csv"
done < airports.csv

end_time=$(date +%s)
echo "The files in the directory after the command: "
ls
echo "Process completed!"
elapsed_time=$((end_time - start_time))
echo "Elapsed time: $elapsed_time seconds."