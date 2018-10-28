import analysis

data = analysis.load_csv('example.txt')
print(analysis.basic_stats(data, 1, 0))
print(analysis.basic_stats(data, 2, 0))
print(analysis.z_score(10, analysis.basic_stats(data, 1, 0)[0],analysis.basic_stats(data, 1, 0)[3]))
print(analysis.histo_analysis(data[0]))
