import collections
N = {
	'Alabama':{'Georgia':263.4 , 'Tennessee':255.3, 'Mississippi':157.6, 'Florida':547.0 },
	'Alaska':{},
	'Arizona':{'New_Mexico':404.8, 'Colorado':729.2, 'Utah':585.2 , 'Nevada':694.5, 'California':739.9},
	'Arkansas':{'Missouri':293.3, 'Oklahoma':352.8, 'Texas':548.1, 'Louisiana':292.9 , 'Mississippi':295.9, 'Tennessee':390},
	'California':{'Arizona':739.9, 'Nevada':534.8, 'Oregon':667.9},
	'Colorado':{'Oklahoma':791.9, 'New_Mexico':423.8, 'Arizona':729.2, 'Utah':427.9, 'Wyoming':394.6, 'Nebraska':385.4, 'Kansas':465.4},
	'Connecticut':{'Rhode_Island':107, 'Massachusetts':124.2, 'New_York':96.9},
	'Delaware':{'Maryland':70.6, 'New_Jersey':158, 'Pennsylvania':277.8},
	'Florida':{'Georgia':365.8, 'Alabama':547.0},
	'Georgia':{'South_Carolina':183.9, 'Florida':365.8, 'Alabama':263.4 , 'Tennessee':374.3, 'North_Carolina':377.2},
	'Hawaii':{},
	'Idaho':{'Montana':527.7, 'Wyoming':517.7, 'Utah':519, 'Nevada':482.2, 'Oregon':394.9, 'Washington':580.1},
	'Illinois':{'Iowa':259.9, 'Missouri':273.9, 'Kentucky':408.6, 'Indiana':206.4, 'Wisconsin':256.3},
	'Indiana':{'Illinois':206.4, 'Ohio':241.1, 'Michigan':321.5, 'Kentucky':243.4},
	'Iowa':{'Illinois':259.9, 'Wisconsin':323.7, 'Minnesota':403.7, 'South_Dakota':469.9, 'Nebraska':398.5, 'Missouri':325.1},
	'Kansas':{'Nebraska':229.6, 'Missouri':436.3, 'Oklahoma':356.6, 'Colorado':465.1},
	'Kentucky':{'Missouri':466.4, 'Illinois':408.6, 'Indiana':243.4, 'Ohio':248.9, 'West_Virginia':259.7, 'Virginia':418.7, 'Tennessee':267.8},
	'Louisiana':{'Texas':571.5, 'Arkansas':292.9, 'Mississippi':232.9},
	'Maine':{'New_Hampshire':244.1},
	'Maryland':{'Delaware':70.6, 'Pennsylvania':206.9, 'West_Virginia':329.2, 'Virginia':209.7},
	'Massachusetts':{'New_Hampshire':76.1, 'Vermont':212.3, 'New_York':203.2, 'Connecticut':124.2, 'Rhode_Island':76.4},
	'Michigan':{'Wisconsin':451.8, 'Indiana':321.5, 'Ohio':365.1},
	'Minnesota':{'North_Dakota':353, 'South_Dakota':453.9, 'Iowa':403.7, 'Wisconsin':425.6},
	'Mississippi':{'Alabama':157.6, 'Tennessee':343.1, 'Arkansas':295.9, 'Louisiana':232.9},
	'Missouri':{'Iowa':325.1, 'Illinois':273.9, 'Kentucky':466.4, 'Tennessee':479.2, 'Arkansas':293.3, 'Oklahoma':422.9, 'Kansas':436.3, 'Nebraska':606.7},
	'Montana':{'North_Dakota':524.3, 'South_Dakota':659.3, 'Wyoming':422.2, 'Idaho':527.7},
	'Nebraska':{'South_Dakota':215, 'Iowa':398.5, 'Missouri':606.7, 'Kansas':229.6, 'Colorado':385.4, 'Wyoming':453.6},
	'Nevada':{'California':534.8, 'Oregon':553.7, 'Idaho':482.2, 'Utah':463.4, 'Arizona':694.5},
	'New_Hampshire':{'Maine':244.1, 'Vermont':138.8, 'Massachusetts':76.1},
	'New_Jersey':{'New_York':78.4, 'Pennsylvania':233.2 , 'Delaware':158},
	'New_Mexico':{'Texas':450, 'Oklahoma':565.4, 'Colorado':423.8, 'Utah':612, 'Arizona':404.8},
	'New_York':{'Vermont':340.2, 'Massachusetts':203.2, 'Connecticut':96.9, 'New_Jersey':78.4, 'Pennsylvania':204.8},
	'North_Carolina':{'Virginia':151.5, 'Tennessee':554.4, 'Georgia':377.2, 'South_Carolina':202.8},
	'North_Dakota':{'Montana':524.3, 'Minnesota':353, 'South_Dakota':321.9},
	'Ohio':{'Michigan':365.1, 'Indiana':241.1, 'Kentucky':248.9, 'West_Virginia':286.1, 'Pennsylvania':356},
	'Oklahoma':{'Arkansas':352.8, 'Missouri':422.9,'Kansas':356.6, 'Colorado':791.9, 'New_Mexico':565.4, 'Texas':340.8},
	'Oregon':{'Washington':358.5, 'Idaho':394.9, 'Nevada':553.7, 'California':667.9},
	'Pennsylvania':{'New_York':204.8, 'New_Jersey':233.2, 'Delaware':277.8, 'Maryland':206.9, 'West_Virginia':338.2, 'Ohio':356},
	'Rhode_Island':{'Connecticut':107, 'Massachusetts':76.4},
	'South_Carolina':{'North_Carolina':202.8, 'Georgia':183.9},
	'South_Dakota':{'North_Dakota':321.9, 'Minnesota':453.9, 'Iowa':469.9, 'Nebraska':215, 'Wyoming':495, 'Montana':659.3},
	'Tennessee':{'Alabama':255.3, 'Georgia':374.3, 'North_Carolina':554.4, 'Virginia':552.4, 'Kentucky':267.8, 'Missouri':554.4, 'Arkansas':390, 'Mississippi':343.1},
	'Texas':{'Louisiana':571.5, 'Arkansas':548.1, 'Oklahoma':340.8, 'New_Mexico':450},
	'Utah':{'Wyoming':495.3, 'Colorado':427.9, 'New_Mexico':612, 'Arizona':585.2, 'Nevada':463.4, 'Idaho':519},
	'Vermont':{'New_Hampshire':138.8, 'Massachusetts':212.3, 'New_York':340.2},
	'Virginia':{'Maryland':209.7, 'West_Virginia':235.3, 'Kentucky':418.7, 'Tennessee':552.4, 'North_Carolina':151.5},
	'Washington':{'Idaho':580.1, 'Oregon':358.5},
	'West_Virginia':{'Virginia':235.3, 'Kentucky':259.7, 'Ohio':286.1, 'Pennsylvania':338.2, 'Maryland':329.2},
	'Wisconsin':{'Michigan':451.8, 'Illinois':256.3, 'Iowa':323.7, 'Minnesota':425.6},
	'Wyoming':{'Montana':422.2, 'South_Dakota':495, 'Nebraska':453.6, 'Colorado':394.6, 'Utah':495.3, 'Idaho':517.7}
}
n=input('Введите штат старта')
res={}
if n=='Alaska' or n=='Hawaii':
	print('Из данного штата нет путей в другие')
else:
	Q=collections.deque()
	res[n]=0
	Q.append(n)
	while Q:
		v=Q.pop()
		for u in N[v]:
			if u not in res or res[v]+N[v][u]<res[u]:
				res[u]=res[v]+N[v][u]
				Q.append(u)
print(res)



