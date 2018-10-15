from api.review_parser import ReviewParser

rp = ReviewParser(['java'], directory_name="../../student_work/sushigo/sushigo-dovgin2/")

rp.parse_repository()
