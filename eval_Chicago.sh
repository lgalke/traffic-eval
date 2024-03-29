echo "============ 100  ==========="
python3 visualize_driving_times.py data/Chicago/results/drivingTimes_100_withoutCostFunctions_10-34-08.txt data/Chicago/results/drivingTimes_100_withoutCostFunctions_12-20-40.txt data/Chicago/results/drivingTimes_100_withCostFunctions_11-32-49.txt --legend "Free-flow" "Randomized A*" "Load-based" 
echo "============ 500  ==========="
python3 visualize_driving_times.py data/Chicago/results/drivingTimes_500_withoutCostFunctions_10-38-02.txt data/Chicago/results/drivingTimes_500_withoutCostFunctions_12-24-10.txt data/Chicago/results/drivingTimes_500_withCostFunctions_11-36-37.txt --legend "Free-flow" "Randomized A*" "Load-based"  
echo "============ 1000 ==========="
python3 visualize_driving_times.py data/Chicago/results/drivingTimes_1000_withoutCostFunctions_10-42-54.txt data/Chicago/results/drivingTimes_1000_withoutCostFunctions_12-28-07.txt data/Chicago/results/drivingTimes_1000_withCostFunctions_11-41-14.txt --legend "Free-flow" "Randomized A*" "Load-based"  
echo "============ 2000 ==========="
python3 visualize_driving_times.py data/Chicago/results/drivingTimes_2000_withoutCostFunctions_10-50-03.txt data/Chicago/results/drivingTimes_2000_withoutCostFunctions_12-34-25.txt data/Chicago/results/drivingTimes_2000_withCostFunctions_11-47-28.txt --legend "Free-flow"  "Randomized A*" "Load-based"
echo "============ 3000 ==========="
python3 visualize_driving_times.py data/Chicago/results/drivingTimes_3000_withoutCostFunctions_11-00-22.txt data/Chicago/results/drivingTimes_3000_withoutCostFunctions_12-43-29.txt data/Chicago/results/drivingTimes_3000_withCostFunctions_11-55-19.txt --legend "Free-flow" "Randomized A*" "Load-based" 
echo "============ 4000 ==========="
python3 visualize_driving_times.py data/Chicago/results/drivingTimes_4000_withoutCostFunctions_11-13-27.txt data/Chicago/results/drivingTimes_4000_withoutCostFunctions_12-55-13.txt data/Chicago/results/drivingTimes_4000_withCostFunctions_12-05-39.txt --legend "Free-flow" "Randomized A*" "Load-based"
echo "============ 5000 ==========="
python3 visualize_driving_times.py  data/Chicago/results/drivingTimes_5000_withoutCostFunctions_11-29-38.txt data/Chicago/results/drivingTimes_5000_withoutCostFunctions_13-08-41.txt data/Chicago/results/drivingTimes_5000_withCostFunctions_12-17-28.txt --legend "Free-flow" "Randomized A*" "Load-based" 
