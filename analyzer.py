cat > count.py << 'EOF'
import csv
from collections import Counter
ips = []
with open('logs.csv') as f:
    for row in csv.DictReader(f):
        ips.append(row['ip'])
print(Counter(ips))
print("Most attacked by:", Counter(ips).most_common(1))
EOF
python count.py
