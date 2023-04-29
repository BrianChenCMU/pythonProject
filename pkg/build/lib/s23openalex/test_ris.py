# pylint: disable=R0801
"""
This py class represents a test case of ris
"""
from s23openalex import Works

REF_RIS = """TY  - JOUR
AU  - John R. Kitchin
PY  - 2015
TI  - Examples of Effective Data Sharing in Scientific Publishing
JO  - ACS Catalysis
VL  - 5
IS  - 6
SP  - 3894
EP  - 3899
DO  - https://doi.org/10.1021/acscatal.5b00538
ER  -"""


"""
This def test represents a test reference of Works()
"""


def test_ris():
    """
    This def test represents a test reference of Works()
    """
    work = Works("https://doi.org/10.1021/acscatal.5b00538")
    assert REF_RIS == work.test_ris_work()
