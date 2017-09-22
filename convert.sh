for file in *\ TI-84\ Plus.8xp; do
    mv -- "$file" "${file%%\ TI-84\ Plus.8xp}.8xp"
done
for file in *.8xp; do
    python ~/git/parse8xp/main.py "$file" "${file%%.8xp}.txt"
done
