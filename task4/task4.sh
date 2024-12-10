echo "The files in the directory before the command: "
ls
start_time=$(date +%s)
echo "Starting process..."
cut -d ',' -f 3 airports.csv > third_column.csv
end_time=$(date +%s)
echo "The files in the directory after the command: "
ls
echo "Process completed!"
elapsed_time=$((end_time - start_time))
echo "Elapsed time: $elapsed_time seconds."