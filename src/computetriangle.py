class ComputeTriangle:
    # def __init__(self):
    #     pass

    def compute_triangle(self,s1,s2,s3):
        if s1 + s2 > s3:
            if s1 == s2 and s2 == s3:
                return 'Equallateral Triangle'
            if s1 == s2 or s2 == s3 or s1 == s3:
                return 'Isosolese Triangle'     
            return 'Scalene Triagle'    
        return 'Not a Triangle'