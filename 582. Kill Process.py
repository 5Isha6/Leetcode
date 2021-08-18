# 582. Kill Process
from collections import defaultdict
class sol(object):	
	def killProcess(self,pid,ppid, kill):
		d = defaultdict(list)
		for i in range(len(ppid)):
			d[ppid[i]].append(pid[i])
			
		res = []
		def dfs(node):
			res.append(node)
			#print(d,d[node])
			for i in d[node]:
				#print('i', i)
				node = i
				dfs(node)
				
				
		dfs(kill)
		return res
o = sol()
print(o.killProcess([1, 3, 10, 5], [3, 0, 5, 3], 5))
