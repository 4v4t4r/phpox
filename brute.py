"""brute.py
brute.py opens sample php file and get words inside��  ��, and used
as data of botnet password dictionary info.
"""

import re
# �Nsample���}
def open_sample(sample):
    with open(sample, "r") as sample_fp:
        sample_string = sample_fp.read()
    return sample_string
# ���open_sample(sample)�����r��A�u�n�O " " �����r��A�N�|�Q��X��
def find_strings(sample):
    string_list = re.findall(r'"(.*?)"', open_sample(sample))
    return set(string_list)