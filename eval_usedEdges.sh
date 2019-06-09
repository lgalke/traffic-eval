echo "============ 100  ==========="
python3 visualize_edge_dist.py data/Melbourne2/results/usedEdges_100_withoutCostFunctions_17-11-15.txt \
	data/Melbourne2/results-astar/results/usedEdges_100_withoutCostFunctions_03-20-14.txt \
	data/Melbourne2/results/usedEdges_100_withCostFunctions_17-14-05.txt \
	--legend "Free-flow" "Randomized A*" "Load-based" 
echo "============ 500  ==========="
python3 visualize_edge_dist.py data/Melbourne2/results/usedEdges_500_withoutCostFunctions_17-16-59.txt \
	data/Melbourne2/results-astar/results/usedEdges_500_withoutCostFunctions_03-21-46.txt \
	data/Melbourne2/results/usedEdges_500_withCostFunctions_17-20-13.txt \
	--legend "Free-flow" "Randomized A*" "Load-based"  
echo "============ 1000 ==========="
python3 visualize_edge_dist.py data/Melbourne2/results/usedEdges_1000_withoutCostFunctions_17-23-38.txt \
	data/Melbourne2/results-astar/results/usedEdges_1000_withoutCostFunctions_03-23-42.txt \
	data/Melbourne2/results/usedEdges_1000_withCostFunctions_17-27-45.txt \
	--legend "Free-flow" "Randomized A*" "Load-based"  
echo "============ 2000 ==========="
python3 visualize_edge_dist.py data/Melbourne2/results/usedEdges_2000_withoutCostFunctions_17-31-51.txt \
	data/Melbourne2/results-astar/results/usedEdges_2000_withoutCostFunctions_03-25-28.txt \
	data/Melbourne2/results/usedEdges_2000_withCostFunctions_17-38-15.txt \
	--legend "Free-flow"  "Randomized A*" "Load-based"
echo "============ 3000 ==========="
python3 visualize_edge_dist.py data/Melbourne2/results/usedEdges_3000_withoutCostFunctions_17-44-12.txt \
	data/Melbourne2/results-astar/results/usedEdges_2000_withoutCostFunctions_03-25-28.txt \
	data/Melbourne2/results/usedEdges_3000_withCostFunctions_17-53-38.txt \
	--legend "Free-flow" "Randomized A*" "Load-based" 
echo "============ 4000 ==========="
python3 visualize_edge_dist.py data/Melbourne2/results/usedEdges_4000_withoutCostFunctions_18-02-19.txt \
	data/Melbourne2/results-astar/results/usedEdges_4000_withoutCostFunctions_03-38-12.txt \
	data/Melbourne2/results/usedEdges_4000_withCostFunctions_18-14-53.txt \
 	--legend "Free-flow" "Randomized A*" "Load-based"
echo "============ 5000 ==========="
python3 visualize_edge_dist.py data/Melbourne2/results/usedEdges_5000_withoutCostFunctions_18-27-27.txt \
	data/Melbourne2/results-astar/results/usedEdges_5000_withoutCostFunctions_03-49-07.txt \
	data/Melbourne2/results/usedEdges_5000_withCostFunctions_18-42-59.txt \
	--legend "Free-flow" "Randomized A*" "Load-based" 
