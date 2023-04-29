# pylint: disable=R0801
"""
This py class represents a test case of bibtext
"""
from s23openalex import Works

REF_BIBTEX = """@article{Kitchin2015,
author = John R. Kitchin,
year = 2015
title = Examples of Effective Data Sharing in Scientific Publishing
journal = ACS Catalysis
volume = 5
number = 6,
pages = 3894-3899,
doi = https://doi.org/10.1021/acscatal.5b00538
}"""


"""
This def test represents a test reference of Works()
"""


def test_bibtex():
    """
    This def test represents a test reference of Works()
    """
    work = Works("https://doi.org/10.1021/acscatal.5b00538")
    assert REF_BIBTEX == work.test_bibtex_work()

