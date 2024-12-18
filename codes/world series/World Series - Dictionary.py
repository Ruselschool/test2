
team_wins = {}  # Key: team, Value: number of wins
year_winner = {}  # Key: year, Value: team


data = '''1903 Boston Americans
1905 New York Giants
1906 Chicago White Sox
1907 Chicago Cubs
1908 Chicago Cubs
1909 Pittsburgh Pirates
1910 Philadelphia Athletics
1911 Philadelphia Athletics
1912 Boston Red Sox
1913 Philadelphia Athletics
1914 Boston Braves
1915 Boston Red Sox
1916 Boston Red Sox
1917 Chicago White Sox
1918 Boston Red Sox
1919 Cincinnati Reds
1920 Cleveland Indians
1921 New York Giants
1922 New York Giants
1923 New York Yankees
1924 Washington Senators
1925 Pittsburgh Pirates
1926 St. Louis Cardinals
1927 New York Yankees
1928 New York Yankees
1929 Philadelphia Athletics
1930 Philadelphia Athletics
1931 St. Louis Cardinals
1932 New York Yankees
1933 New York Giants
1934 St. Louis Cardinals
1935 Detroit Tigers
1936 New York Yankees
1937 New York Yankees
1938 New York Yankees
1939 New York Yankees
1940 Cincinnati Reds
1941 New York Yankees
1942 St. Louis Cardinals
1943 New York Yankees
1944 St. Louis Cardinals
1945 Detroit Tigers
1946 St. Louis Cardinals
1947 New York Yankees
1948 Cleveland Indians
1949 New York Yankees
1950 New York Yankees
1951 New York Yankees
1952 New York Yankees
1953 New York Yankees
1954 New York Giants
1955 Brooklyn Dodgers
1956 New York Yankees
1957 Milwaukee Braves
1958 New York Yankees
1959 Los Angeles Dodgers
1960 Pittsburgh Pirates
1961 New York Yankees
1962 New York Yankees
1963 Los Angeles Dodgers
1964 St. Louis Cardinals
1965 Los Angeles Dodgers
1966 Baltimore Orioles
1967 St. Louis Cardinals
1968 Detroit Tigers
1969 New York Mets
1970 Baltimore Orioles
1971 Pittsburgh Pirates
1972 Oakland Athletics
1973 Oakland Athletics
1974 Oakland Athletics
1975 Cincinnati Reds
1976 Cincinnati Reds
1977 New York Yankees
1978 New York Yankees
1979 Pittsburgh Pirates
1980 Philadelphia Phillies
1981 Los Angeles Dodgers
1982 St. Louis Cardinals
1983 Baltimore Orioles
1984 Detroit Tigers
1985 Kansas City Royals
1986 New York Mets
1987 Minnesota Twins
1988 Los Angeles Dodgers
1989 Oakland Athletics
1990 Cincinnati Reds
1991 Minnesota Twins
1992 Toronto Blue Jays
1993 Toronto Blue Jays
1995 Atlanta Braves
1996 New York Yankees
1997 Florida Marlins
1998 New York Yankees
1999 New York Yankees
2000 New York Yankees
2001 Arizona Diamondbacks
2002 Anaheim Angels
2003 Florida Marlins
2004 Boston Red Sox
2005 Chicago White Sox
2006 St. Louis Cardinals
2007 Boston Red Sox
2008 Philadelphia Phillies
2009 New York Yankees
2010 San Francisco Giants
2011 St. Louis Cardinals
2012 San Francisco Giants
2013 Boston Red Sox
2014 San Francisco Giants
2015 Kansas City Royals
2016 Chicago Cubs
2017 Houston Astros
2018 Boston Red Sox
'''

user_input = input("Enter a year 1903 to 2018: ")

for line in data.splitlines():
    line_split = line.split()
    year = line_split[0]
    if len(line_split) > 1:
        team = ' '.join(line_split[1:])
        year_winner[year] = team
        if team in team_wins:
            team_wins[team] += 1
        else:
            team_wins[team] = 1



if user_input in year_winner:
    team = year_winner[user_input]
    wins = team_wins[team]
    print(f"In {user_input} the {team} won the World Series. They have won {wins} time(s).")
else:
    print(f"No winner in {user_input} or the year is out of range.")
