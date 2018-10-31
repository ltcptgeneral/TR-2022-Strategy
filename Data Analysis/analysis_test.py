import analysis

data = analysis.load_csv('example.txt')
print(analysis.basic_stats(0, 'debug', 0))
print(analysis.basic_stats(data, 1, 0))
print(analysis.basic_stats(data, 2, 0))
print(analysis.z_score(10, analysis.basic_stats(data, 1, 0)[0],analysis.basic_stats(data, 1, 0)[3]))
print(analysis.histo_analysis(data[0]))
print(analysis.histo_analysis_2(data[0], 0.01, -1, 1))

x = analysis.objectives(["switch", "scale", "climb"], [0,1,2], [[0,0],[1,1],[2,0]], ["0,1", "1,1", "0,5"])
