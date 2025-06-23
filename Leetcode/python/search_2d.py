def searchMatrix(matrix: list[list[int]], target: int) -> bool:
        for row in matrix:
            # perform binary search
            l,r = 0, len(row)-1
            while l<=r:
                mid = (l+r)//2
                if row[mid] == target: return True
                elif row[mid]>target: r=mid-1
                else: l=mid+1
        return False