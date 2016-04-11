errors=0
success=0
for i in $(ls *.out); do
	./$i
	if [ $? -ne 0 ]; then
		errors=$((errors+1))
	else 
		success=$((success+1))
	fi
done

echo "$success successes, $errors errors"
if [ $errors > 0 ]; then
	exit 1
else
	exit 0
fi