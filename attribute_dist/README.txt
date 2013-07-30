attributeDist.py: count number of occurences of each attributes for all datasets.
attributeDist_c.py: count number of occurences of each representative attributes. In other word, for each cluster, we only count 1 for any attribute even it appears multiple times. To do that, for each cluster, we union the attributes of all belonging datasets. Then do counting.
