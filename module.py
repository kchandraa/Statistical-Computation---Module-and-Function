def show_outlier(df, col_name):
    """
    This function takes a dataframe and a column name and returns the outliers data.
    
    Outliers is data less than q1 - (1.5)*iqr or the data more than q3 + (1.5)*iqr.
    iqr =  q3 - q1
    """
    
    q1 = df[col_name].quantile(0.25)
    q3 = df[col_name].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - (1.5)*iqr
    upper_bound = q3 + (1.5)*iqr

    return df[(df[col_name] < lower_bound) | (df[col_name] > upper_bound)]

    
def inradius(a,b,c):
    """
    This function takes three sides of a triangle and returns the inradius of the triangle.
    """

    s = (a+b+c)/2
    return ((s*(s-a)*(s-b)*(s-c))**0.5)/s

def outradius(a,b,c):
    """
    This function takes three sides of a triangle and returns the outradius of the triangle.
    """

    s = (a+b+c)/2
    L = (s*(s-a)*(s-b)*(s-c))**0.5
    return a*b*c/(4*L)
    