cat << EOF | grep -P '^(\(\d{3}\)\s|\d{3}-)\d{3}-\d{4}$'
987-123-4567
123 456 7890
(123) 456-7890
EOF