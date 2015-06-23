'''
Ground truth format : person 372 166 13 30 0 0 0 0 0 0 0
lbl  - a string label describing object type (eg: 'pedestrian')
bb   - [l t w h]: bb indicating predicted object extent
occ  - 0/1 value indicating if bb is occluded
bbv  - [l t w h]: bb indicating visible region (may be [0 0 0 0])
ign  - 0/1 value indicating bb was marked as ignore
ang  - [0-360] orientation of bb in degrees

Test data format    : 351.61092985318106 156.07667210440457 25 50
'''

#Place the HPU    data ('test-xxx.dat')   in a  "hpu"    folder
#Place the Ground data ('ground-xxx.txt') in a  "ground" folder
acceptance = 0.0  #Set to 0.5 or any float value
printing  = 0 #Set to 1 to display [Detailed logs]
printingS = 0 #Set to 1 to display [Area and Yes/No]

TP = 0
FP = 0
TN = 0
FN = 0
total_detected = 0
correct = 0
test_files    = ['test-001.dat','test-002.dat','test-003.dat','test-004.dat','test-005.dat','test-006.dat','test-007.dat','test-008.dat','test-009.dat','test-010.dat','test-011.dat','test-012.dat','test-013.dat','test-014.dat','test-015.dat','test-016.dat','test-017.dat','test-018.dat','test-019.dat','test-020.dat','test-021.dat','test-022.dat','test-023.dat','test-024.dat','test-025.dat','test-026.dat','test-027.dat','test-028.dat','test-029.dat','test-030.dat','test-031.dat','test-032.dat','test-033.dat','test-034.dat','test-035.dat','test-036.dat','test-037.dat','test-038.dat','test-039.dat','test-040.dat','test-041.dat','test-042.dat','test-043.dat','test-044.dat','test-045.dat','test-046.dat','test-047.dat','test-048.dat','test-049.dat','test-050.dat','test-051.dat','test-052.dat','test-053.dat','test-054.dat','test-055.dat','test-056.dat','test-057.dat','test-058.dat','test-059.dat','test-060.dat','test-061.dat','test-062.dat','test-063.dat','test-064.dat','test-065.dat','test-066.dat','test-067.dat','test-068.dat','test-069.dat','test-070.dat','test-071.dat','test-072.dat','test-073.dat','test-074.dat','test-075.dat','test-076.dat','test-077.dat','test-078.dat','test-079.dat','test-080.dat','test-081.dat','test-082.dat','test-083.dat','test-084.dat','test-085.dat','test-086.dat','test-087.dat','test-088.dat','test-089.dat','test-090.dat','test-091.dat','test-092.dat','test-093.dat','test-094.dat','test-095.dat','test-096.dat','test-097.dat','test-098.dat','test-099.dat','test-100.dat','test-101.dat','test-102.dat','test-103.dat','test-104.dat','test-105.dat','test-106.dat','test-107.dat','test-108.dat','test-109.dat','test-110.dat','test-111.dat','test-112.dat','test-113.dat','test-114.dat','test-115.dat','test-116.dat','test-117.dat','test-118.dat','test-119.dat','test-120.dat','test-121.dat','test-122.dat','test-123.dat','test-124.dat','test-125.dat','test-126.dat','test-127.dat','test-128.dat','test-129.dat','test-130.dat','test-131.dat','test-132.dat','test-133.dat','test-134.dat','test-135.dat','test-136.dat','test-137.dat','test-138.dat','test-139.dat','test-140.dat','test-141.dat','test-142.dat','test-143.dat','test-144.dat','test-145.dat','test-146.dat','test-147.dat','test-148.dat','test-149.dat','test-150.dat','test-151.dat','test-152.dat','test-153.dat','test-154.dat','test-155.dat','test-156.dat','test-157.dat','test-158.dat','test-159.dat','test-160.dat','test-161.dat','test-162.dat','test-163.dat','test-164.dat','test-165.dat','test-166.dat','test-167.dat','test-168.dat','test-169.dat','test-170.dat','test-171.dat','test-172.dat','test-173.dat','test-174.dat','test-175.dat','test-176.dat','test-177.dat','test-178.dat','test-179.dat','test-180.dat','test-181.dat','test-182.dat','test-183.dat','test-184.dat','test-185.dat','test-186.dat','test-187.dat','test-188.dat','test-189.dat','test-190.dat','test-191.dat','test-192.dat','test-193.dat','test-194.dat','test-195.dat','test-196.dat','test-197.dat','test-198.dat','test-199.dat','test-200.dat','test-201.dat','test-202.dat','test-203.dat','test-204.dat','test-205.dat','test-206.dat','test-207.dat','test-208.dat','test-209.dat','test-210.dat','test-211.dat','test-212.dat','test-213.dat','test-214.dat','test-215.dat','test-216.dat','test-217.dat','test-218.dat','test-219.dat','test-220.dat','test-221.dat','test-222.dat','test-223.dat','test-224.dat','test-225.dat','test-226.dat','test-227.dat','test-228.dat','test-229.dat','test-230.dat','test-231.dat','test-232.dat','test-233.dat','test-234.dat','test-235.dat','test-236.dat','test-237.dat','test-238.dat','test-239.dat','test-240.dat','test-241.dat','test-242.dat','test-243.dat','test-244.dat','test-245.dat','test-246.dat','test-247.dat','test-248.dat','test-249.dat','test-250.dat','test-251.dat','test-252.dat','test-253.dat','test-254.dat','test-255.dat','test-256.dat','test-257.dat','test-258.dat','test-259.dat','test-260.dat','test-261.dat','test-262.dat','test-263.dat','test-264.dat','test-265.dat','test-266.dat','test-267.dat','test-268.dat','test-269.dat','test-270.dat','test-271.dat','test-272.dat','test-273.dat','test-274.dat','test-275.dat','test-276.dat','test-277.dat','test-278.dat','test-279.dat','test-280.dat','test-281.dat','test-282.dat','test-283.dat','test-284.dat','test-285.dat','test-286.dat','test-287.dat','test-288.dat','test-289.dat','test-290.dat','test-291.dat','test-292.dat','test-293.dat','test-294.dat','test-295.dat','test-296.dat','test-297.dat','test-298.dat','test-299.dat','test-300.dat','test-301.dat','test-302.dat','test-303.dat','test-304.dat','test-305.dat','test-306.dat','test-307.dat','test-308.dat','test-309.dat','test-310.dat','test-311.dat','test-312.dat','test-313.dat','test-314.dat','test-315.dat','test-316.dat','test-317.dat','test-318.dat','test-319.dat','test-320.dat','test-321.dat','test-322.dat','test-323.dat','test-324.dat','test-325.dat','test-326.dat','test-327.dat','test-328.dat','test-329.dat','test-330.dat','test-331.dat','test-332.dat','test-333.dat','test-334.dat','test-335.dat','test-336.dat','test-337.dat','test-338.dat','test-339.dat','test-340.dat','test-341.dat','test-342.dat','test-343.dat','test-344.dat','test-345.dat','test-346.dat','test-347.dat','test-348.dat','test-349.dat','test-350.dat','test-351.dat','test-352.dat','test-353.dat','test-354.dat','test-355.dat','test-356.dat','test-357.dat','test-358.dat','test-359.dat','test-360.dat','test-361.dat','test-362.dat','test-363.dat','test-364.dat','test-365.dat','test-366.dat','test-367.dat','test-368.dat','test-369.dat','test-370.dat','test-371.dat','test-372.dat','test-373.dat','test-374.dat','test-375.dat','test-376.dat','test-377.dat','test-378.dat','test-379.dat','test-380.dat','test-381.dat','test-382.dat','test-383.dat','test-384.dat','test-385.dat','test-386.dat','test-387.dat','test-388.dat','test-389.dat','test-390.dat','test-391.dat','test-392.dat','test-393.dat','test-394.dat','test-395.dat','test-396.dat','test-397.dat','test-398.dat','test-399.dat','test-400.dat','test-401.dat','test-402.dat','test-403.dat','test-404.dat','test-405.dat','test-406.dat','test-407.dat','test-408.dat','test-409.dat','test-410.dat','test-411.dat','test-412.dat','test-413.dat','test-414.dat','test-415.dat','test-416.dat','test-417.dat','test-418.dat','test-419.dat','test-420.dat','test-421.dat','test-422.dat','test-423.dat','test-424.dat','test-425.dat','test-426.dat','test-427.dat','test-428.dat','test-429.dat','test-430.dat','test-431.dat','test-432.dat','test-433.dat','test-434.dat','test-435.dat','test-436.dat','test-437.dat','test-438.dat','test-439.dat','test-440.dat','test-441.dat','test-442.dat','test-443.dat','test-444.dat','test-445.dat','test-446.dat','test-447.dat','test-448.dat','test-449.dat','test-450.dat','test-451.dat','test-452.dat','test-453.dat','test-454.dat','test-455.dat','test-456.dat','test-457.dat','test-458.dat','test-459.dat','test-460.dat','test-461.dat','test-462.dat','test-463.dat','test-464.dat','test-465.dat','test-466.dat','test-467.dat','test-468.dat','test-469.dat','test-470.dat','test-471.dat','test-472.dat','test-473.dat','test-474.dat','test-475.dat','test-476.dat','test-477.dat','test-478.dat','test-479.dat','test-480.dat','test-481.dat','test-482.dat','test-483.dat','test-484.dat','test-485.dat','test-486.dat','test-487.dat','test-488.dat','test-489.dat','test-490.dat','test-491.dat','test-492.dat','test-493.dat','test-494.dat','test-495.dat','test-496.dat','test-497.dat','test-498.dat','test-499.dat','test-500.dat','test-501.dat','test-502.dat','test-503.dat','test-504.dat','test-505.dat','test-506.dat','test-507.dat','test-508.dat','test-509.dat','test-510.dat','test-511.dat','test-512.dat','test-513.dat','test-514.dat','test-515.dat','test-516.dat','test-517.dat','test-518.dat','test-519.dat','test-520.dat','test-521.dat','test-522.dat','test-523.dat','test-524.dat','test-525.dat','test-526.dat','test-527.dat','test-528.dat','test-529.dat','test-530.dat','test-531.dat','test-532.dat','test-533.dat','test-534.dat','test-535.dat','test-536.dat','test-537.dat','test-538.dat','test-539.dat','test-540.dat','test-541.dat','test-542.dat','test-543.dat','test-544.dat','test-545.dat','test-546.dat','test-547.dat','test-548.dat','test-549.dat','test-550.dat','test-551.dat','test-552.dat','test-553.dat','test-554.dat','test-555.dat','test-556.dat','test-557.dat','test-558.dat','test-559.dat','test-560.dat','test-561.dat','test-562.dat','test-563.dat','test-564.dat','test-565.dat','test-566.dat','test-567.dat','test-568.dat','test-569.dat','test-570.dat','test-571.dat','test-572.dat','test-573.dat','test-574.dat','test-575.dat','test-576.dat','test-577.dat','test-578.dat','test-579.dat','test-580.dat','test-581.dat','test-582.dat','test-583.dat','test-584.dat','test-585.dat','test-586.dat','test-587.dat','test-588.dat','test-589.dat','test-590.dat','test-591.dat','test-592.dat','test-593.dat','test-594.dat','test-595.dat','test-596.dat','test-597.dat','test-598.dat','test-599.dat','test-600.dat','test-601.dat','test-602.dat','test-603.dat','test-604.dat','test-605.dat','test-606.dat','test-607.dat','test-608.dat','test-609.dat','test-610.dat','test-611.dat','test-612.dat','test-613.dat','test-614.dat','test-615.dat','test-616.dat','test-617.dat','test-618.dat','test-619.dat','test-620.dat','test-621.dat','test-622.dat','test-623.dat','test-624.dat','test-625.dat','test-626.dat','test-627.dat','test-628.dat','test-629.dat','test-630.dat','test-631.dat','test-632.dat','test-633.dat','test-634.dat','test-635.dat','test-636.dat','test-637.dat','test-638.dat','test-639.dat','test-640.dat','test-641.dat','test-642.dat','test-643.dat','test-644.dat','test-645.dat','test-646.dat','test-647.dat','test-648.dat','test-649.dat','test-650.dat','test-651.dat','test-652.dat','test-653.dat','test-654.dat','test-655.dat','test-656.dat','test-657.dat','test-658.dat','test-659.dat','test-660.dat','test-661.dat','test-662.dat','test-663.dat','test-664.dat','test-665.dat','test-666.dat','test-667.dat','test-668.dat','test-669.dat','test-670.dat','test-671.dat','test-672.dat','test-673.dat','test-674.dat','test-675.dat','test-676.dat','test-677.dat','test-678.dat','test-679.dat','test-680.dat','test-681.dat','test-682.dat','test-683.dat','test-684.dat','test-685.dat','test-686.dat','test-687.dat','test-688.dat','test-689.dat','test-690.dat','test-691.dat','test-692.dat','test-693.dat','test-694.dat','test-695.dat','test-696.dat','test-697.dat','test-698.dat','test-699.dat','test-700.dat','test-701.dat','test-702.dat','test-703.dat','test-704.dat','test-705.dat','test-706.dat','test-707.dat','test-708.dat','test-709.dat','test-710.dat','test-711.dat','test-712.dat','test-713.dat','test-714.dat','test-715.dat','test-716.dat','test-717.dat','test-718.dat','test-719.dat','test-720.dat','test-721.dat','test-722.dat','test-723.dat','test-724.dat','test-725.dat','test-726.dat','test-727.dat','test-728.dat','test-729.dat','test-730.dat','test-731.dat','test-732.dat','test-733.dat','test-734.dat','test-735.dat','test-736.dat','test-737.dat','test-738.dat']
ground_files  = ['ground-001.txt','ground-002.txt','ground-003.txt','ground-004.txt','ground-005.txt','ground-006.txt','ground-007.txt','ground-008.txt','ground-009.txt','ground-010.txt','ground-011.txt','ground-012.txt','ground-013.txt','ground-014.txt','ground-015.txt','ground-016.txt','ground-017.txt','ground-018.txt','ground-019.txt','ground-020.txt','ground-021.txt','ground-022.txt','ground-023.txt','ground-024.txt','ground-025.txt','ground-026.txt','ground-027.txt','ground-028.txt','ground-029.txt','ground-030.txt','ground-031.txt','ground-032.txt','ground-033.txt','ground-034.txt','ground-035.txt','ground-036.txt','ground-037.txt','ground-038.txt','ground-039.txt','ground-040.txt','ground-041.txt','ground-042.txt','ground-043.txt','ground-044.txt','ground-045.txt','ground-046.txt','ground-047.txt','ground-048.txt','ground-049.txt','ground-050.txt','ground-051.txt','ground-052.txt','ground-053.txt','ground-054.txt','ground-055.txt','ground-056.txt','ground-057.txt','ground-058.txt','ground-059.txt','ground-060.txt','ground-061.txt','ground-062.txt','ground-063.txt','ground-064.txt','ground-065.txt','ground-066.txt','ground-067.txt','ground-068.txt','ground-069.txt','ground-070.txt','ground-071.txt','ground-072.txt','ground-073.txt','ground-074.txt','ground-075.txt','ground-076.txt','ground-077.txt','ground-078.txt','ground-079.txt','ground-080.txt','ground-081.txt','ground-082.txt','ground-083.txt','ground-084.txt','ground-085.txt','ground-086.txt','ground-087.txt','ground-088.txt','ground-089.txt','ground-090.txt','ground-091.txt','ground-092.txt','ground-093.txt','ground-094.txt','ground-095.txt','ground-096.txt','ground-097.txt','ground-098.txt','ground-099.txt','ground-100.txt','ground-101.txt','ground-102.txt','ground-103.txt','ground-104.txt','ground-105.txt','ground-106.txt','ground-107.txt','ground-108.txt','ground-109.txt','ground-110.txt','ground-111.txt','ground-112.txt','ground-113.txt','ground-114.txt','ground-115.txt','ground-116.txt','ground-117.txt','ground-118.txt','ground-119.txt','ground-120.txt','ground-121.txt','ground-122.txt','ground-123.txt','ground-124.txt','ground-125.txt','ground-126.txt','ground-127.txt','ground-128.txt','ground-129.txt','ground-130.txt','ground-131.txt','ground-132.txt','ground-133.txt','ground-134.txt','ground-135.txt','ground-136.txt','ground-137.txt','ground-138.txt','ground-139.txt','ground-140.txt','ground-141.txt','ground-142.txt','ground-143.txt','ground-144.txt','ground-145.txt','ground-146.txt','ground-147.txt','ground-148.txt','ground-149.txt','ground-150.txt','ground-151.txt','ground-152.txt','ground-153.txt','ground-154.txt','ground-155.txt','ground-156.txt','ground-157.txt','ground-158.txt','ground-159.txt','ground-160.txt','ground-161.txt','ground-162.txt','ground-163.txt','ground-164.txt','ground-165.txt','ground-166.txt','ground-167.txt','ground-168.txt','ground-169.txt','ground-170.txt','ground-171.txt','ground-172.txt','ground-173.txt','ground-174.txt','ground-175.txt','ground-176.txt','ground-177.txt','ground-178.txt','ground-179.txt','ground-180.txt','ground-181.txt','ground-182.txt','ground-183.txt','ground-184.txt','ground-185.txt','ground-186.txt','ground-187.txt','ground-188.txt','ground-189.txt','ground-190.txt','ground-191.txt','ground-192.txt','ground-193.txt','ground-194.txt','ground-195.txt','ground-196.txt','ground-197.txt','ground-198.txt','ground-199.txt','ground-200.txt','ground-201.txt','ground-202.txt','ground-203.txt','ground-204.txt','ground-205.txt','ground-206.txt','ground-207.txt','ground-208.txt','ground-209.txt','ground-210.txt','ground-211.txt','ground-212.txt','ground-213.txt','ground-214.txt','ground-215.txt','ground-216.txt','ground-217.txt','ground-218.txt','ground-219.txt','ground-220.txt','ground-221.txt','ground-222.txt','ground-223.txt','ground-224.txt','ground-225.txt','ground-226.txt','ground-227.txt','ground-228.txt','ground-229.txt','ground-230.txt','ground-231.txt','ground-232.txt','ground-233.txt','ground-234.txt','ground-235.txt','ground-236.txt','ground-237.txt','ground-238.txt','ground-239.txt','ground-240.txt','ground-241.txt','ground-242.txt','ground-243.txt','ground-244.txt','ground-245.txt','ground-246.txt','ground-247.txt','ground-248.txt','ground-249.txt','ground-250.txt','ground-251.txt','ground-252.txt','ground-253.txt','ground-254.txt','ground-255.txt','ground-256.txt','ground-257.txt','ground-258.txt','ground-259.txt','ground-260.txt','ground-261.txt','ground-262.txt','ground-263.txt','ground-264.txt','ground-265.txt','ground-266.txt','ground-267.txt','ground-268.txt','ground-269.txt','ground-270.txt','ground-271.txt','ground-272.txt','ground-273.txt','ground-274.txt','ground-275.txt','ground-276.txt','ground-277.txt','ground-278.txt','ground-279.txt','ground-280.txt','ground-281.txt','ground-282.txt','ground-283.txt','ground-284.txt','ground-285.txt','ground-286.txt','ground-287.txt','ground-288.txt','ground-289.txt','ground-290.txt','ground-291.txt','ground-292.txt','ground-293.txt','ground-294.txt','ground-295.txt','ground-296.txt','ground-297.txt','ground-298.txt','ground-299.txt','ground-300.txt','ground-301.txt','ground-302.txt','ground-303.txt','ground-304.txt','ground-305.txt','ground-306.txt','ground-307.txt','ground-308.txt','ground-309.txt','ground-310.txt','ground-311.txt','ground-312.txt','ground-313.txt','ground-314.txt','ground-315.txt','ground-316.txt','ground-317.txt','ground-318.txt','ground-319.txt','ground-320.txt','ground-321.txt','ground-322.txt','ground-323.txt','ground-324.txt','ground-325.txt','ground-326.txt','ground-327.txt','ground-328.txt','ground-329.txt','ground-330.txt','ground-331.txt','ground-332.txt','ground-333.txt','ground-334.txt','ground-335.txt','ground-336.txt','ground-337.txt','ground-338.txt','ground-339.txt','ground-340.txt','ground-341.txt','ground-342.txt','ground-343.txt','ground-344.txt','ground-345.txt','ground-346.txt','ground-347.txt','ground-348.txt','ground-349.txt','ground-350.txt','ground-351.txt','ground-352.txt','ground-353.txt','ground-354.txt','ground-355.txt','ground-356.txt','ground-357.txt','ground-358.txt','ground-359.txt','ground-360.txt','ground-361.txt','ground-362.txt','ground-363.txt','ground-364.txt','ground-365.txt','ground-366.txt','ground-367.txt','ground-368.txt','ground-369.txt','ground-370.txt','ground-371.txt','ground-372.txt','ground-373.txt','ground-374.txt','ground-375.txt','ground-376.txt','ground-377.txt','ground-378.txt','ground-379.txt','ground-380.txt','ground-381.txt','ground-382.txt','ground-383.txt','ground-384.txt','ground-385.txt','ground-386.txt','ground-387.txt','ground-388.txt','ground-389.txt','ground-390.txt','ground-391.txt','ground-392.txt','ground-393.txt','ground-394.txt','ground-395.txt','ground-396.txt','ground-397.txt','ground-398.txt','ground-399.txt','ground-400.txt','ground-401.txt','ground-402.txt','ground-403.txt','ground-404.txt','ground-405.txt','ground-406.txt','ground-407.txt','ground-408.txt','ground-409.txt','ground-410.txt','ground-411.txt','ground-412.txt','ground-413.txt','ground-414.txt','ground-415.txt','ground-416.txt','ground-417.txt','ground-418.txt','ground-419.txt','ground-420.txt','ground-421.txt','ground-422.txt','ground-423.txt','ground-424.txt','ground-425.txt','ground-426.txt','ground-427.txt','ground-428.txt','ground-429.txt','ground-430.txt','ground-431.txt','ground-432.txt','ground-433.txt','ground-434.txt','ground-435.txt','ground-436.txt','ground-437.txt','ground-438.txt','ground-439.txt','ground-440.txt','ground-441.txt','ground-442.txt','ground-443.txt','ground-444.txt','ground-445.txt','ground-446.txt','ground-447.txt','ground-448.txt','ground-449.txt','ground-450.txt','ground-451.txt','ground-452.txt','ground-453.txt','ground-454.txt','ground-455.txt','ground-456.txt','ground-457.txt','ground-458.txt','ground-459.txt','ground-460.txt','ground-461.txt','ground-462.txt','ground-463.txt','ground-464.txt','ground-465.txt','ground-466.txt','ground-467.txt','ground-468.txt','ground-469.txt','ground-470.txt','ground-471.txt','ground-472.txt','ground-473.txt','ground-474.txt','ground-475.txt','ground-476.txt','ground-477.txt','ground-478.txt','ground-479.txt','ground-480.txt','ground-481.txt','ground-482.txt','ground-483.txt','ground-484.txt','ground-485.txt','ground-486.txt','ground-487.txt','ground-488.txt','ground-489.txt','ground-490.txt','ground-491.txt','ground-492.txt','ground-493.txt','ground-494.txt','ground-495.txt','ground-496.txt','ground-497.txt','ground-498.txt','ground-499.txt','ground-500.txt','ground-501.txt','ground-502.txt','ground-503.txt','ground-504.txt','ground-505.txt','ground-506.txt','ground-507.txt','ground-508.txt','ground-509.txt','ground-510.txt','ground-511.txt','ground-512.txt','ground-513.txt','ground-514.txt','ground-515.txt','ground-516.txt','ground-517.txt','ground-518.txt','ground-519.txt','ground-520.txt','ground-521.txt','ground-522.txt','ground-523.txt','ground-524.txt','ground-525.txt','ground-526.txt','ground-527.txt','ground-528.txt','ground-529.txt','ground-530.txt','ground-531.txt','ground-532.txt','ground-533.txt','ground-534.txt','ground-535.txt','ground-536.txt','ground-537.txt','ground-538.txt','ground-539.txt','ground-540.txt','ground-541.txt','ground-542.txt','ground-543.txt','ground-544.txt','ground-545.txt','ground-546.txt','ground-547.txt','ground-548.txt','ground-549.txt','ground-550.txt','ground-551.txt','ground-552.txt','ground-553.txt','ground-554.txt','ground-555.txt','ground-556.txt','ground-557.txt','ground-558.txt','ground-559.txt','ground-560.txt','ground-561.txt','ground-562.txt','ground-563.txt','ground-564.txt','ground-565.txt','ground-566.txt','ground-567.txt','ground-568.txt','ground-569.txt','ground-570.txt','ground-571.txt','ground-572.txt','ground-573.txt','ground-574.txt','ground-575.txt','ground-576.txt','ground-577.txt','ground-578.txt','ground-579.txt','ground-580.txt','ground-581.txt','ground-582.txt','ground-583.txt','ground-584.txt','ground-585.txt','ground-586.txt','ground-587.txt','ground-588.txt','ground-589.txt','ground-590.txt','ground-591.txt','ground-592.txt','ground-593.txt','ground-594.txt','ground-595.txt','ground-596.txt','ground-597.txt','ground-598.txt','ground-599.txt','ground-600.txt','ground-601.txt','ground-602.txt','ground-603.txt','ground-604.txt','ground-605.txt','ground-606.txt','ground-607.txt','ground-608.txt','ground-609.txt','ground-610.txt','ground-611.txt','ground-612.txt','ground-613.txt','ground-614.txt','ground-615.txt','ground-616.txt','ground-617.txt','ground-618.txt','ground-619.txt','ground-620.txt','ground-621.txt','ground-622.txt','ground-623.txt','ground-624.txt','ground-625.txt','ground-626.txt','ground-627.txt','ground-628.txt','ground-629.txt','ground-630.txt','ground-631.txt','ground-632.txt','ground-633.txt','ground-634.txt','ground-635.txt','ground-636.txt','ground-637.txt','ground-638.txt','ground-639.txt','ground-640.txt','ground-641.txt','ground-642.txt','ground-643.txt','ground-644.txt','ground-645.txt','ground-646.txt','ground-647.txt','ground-648.txt','ground-649.txt','ground-650.txt','ground-651.txt','ground-652.txt','ground-653.txt','ground-654.txt','ground-655.txt','ground-656.txt','ground-657.txt','ground-658.txt','ground-659.txt','ground-660.txt','ground-661.txt','ground-662.txt','ground-663.txt','ground-664.txt','ground-665.txt','ground-666.txt','ground-667.txt','ground-668.txt','ground-669.txt','ground-670.txt','ground-671.txt','ground-672.txt','ground-673.txt','ground-674.txt','ground-675.txt','ground-676.txt','ground-677.txt','ground-678.txt','ground-679.txt','ground-680.txt','ground-681.txt','ground-682.txt','ground-683.txt','ground-684.txt','ground-685.txt','ground-686.txt','ground-687.txt','ground-688.txt','ground-689.txt','ground-690.txt','ground-691.txt','ground-692.txt','ground-693.txt','ground-694.txt','ground-695.txt','ground-696.txt','ground-697.txt','ground-698.txt','ground-699.txt','ground-700.txt','ground-701.txt','ground-702.txt','ground-703.txt','ground-704.txt','ground-705.txt','ground-706.txt','ground-707.txt','ground-708.txt','ground-709.txt','ground-710.txt','ground-711.txt','ground-712.txt','ground-713.txt','ground-714.txt','ground-715.txt','ground-716.txt','ground-717.txt','ground-718.txt','ground-719.txt','ground-720.txt','ground-721.txt','ground-722.txt','ground-723.txt','ground-724.txt','ground-725.txt','ground-726.txt','ground-727.txt','ground-728.txt','ground-729.txt','ground-730.txt','ground-731.txt','ground-732.txt','ground-733.txt','ground-734.txt','ground-735.txt','ground-736.txt','ground-737.txt','ground-738.txt']


#TP, FP calculation
for file_index in range(738):
  #print file_index
  with open("hpu/"+test_files[file_index], 'r') as file:
    file.seek(0) #ensure you're at the start of the file..
    first_char = file.read(1) #get the first character
    if not first_char:
      #print "file is empty" #first character is the empty string..
      continue
    else:
      file.seek(0) #first character wasn't empty, return to start of file.

    for line in file:
      if (not line) or (line=='\n'):
        continue
      if printingS or printing:
        print file_index
      words = line.split()
      if printing:
        print words
      x = float(words[0])
      y = float(words[1])
      w = float(words[2])
      h = float(words[3])

      xmin = x
      xmax = x + w
      ymin = y
      ymax = y + h
      total_detected = total_detected + 1
      if printing:
        print "["+str(xmin)+","+str(ymin)+","+str(xmax)+","+str(ymax)+"]"

      flag = 0
      with open("ground/"+ground_files[file_index], 'r') as fileG:
        next(fileG)
        for lineG in fileG:
          if (not lineG) or (lineG=='\n'):
            continue
          #print lineG
          wordsG = lineG.split()
          if printing:
            print wordsG
          xG = float(wordsG[1])
          yG = float(wordsG[2])
          wG = float(wordsG[3])
          hG = float(wordsG[4])
          occ = int(wordsG[5])

          if occ==1:    #Exclude occluded ground truth
            continue

          xminG = xG
          xmaxG = xG + wG
          yminG = yG
          ymaxG = yG + hG
          if printing:
            print "["+str(xminG)+","+str(yminG)+","+str(xmaxG)+","+str(ymaxG)+"]"

          #Logic for this : http://stackoverflow.com/a/21220004
          SA = w * h
          SB = wG * hG
          #SI = max(0, max(xmax, xmaxG) - min(xmin, xminG)) * max(0, max(ymax, ymaxG) - min(ymin, yminG))
          SI = max(0, min(xmax, xmaxG) - max(xmin, xminG)) * max(0, min(ymax, ymaxG) - max(ymin, yminG))
          SU = SA + SB - SI
          S = SI / SU
          if printing:
            print "SA ="+str(SA)
            print "SB ="+str(SB)
            print "SI ="+str(SI)
            print "SU ="+str(SU)
          if printingS or printing:
            print "S ="+str(S)

          if S > acceptance:
            if printingS or printing:
              print ("Yes")
            correct = correct + 1
            TP = TP + 1
            flag = 1
            break

        if flag==0:
          if printingS or printing:
            print ("No")
          FP = FP + 1

ground_total = 0
ground_match = 0
#False Negative calculation
for file_index in range(738):
  #print file_index
  with open("ground/"+ground_files[file_index], 'r') as file:
    next(file)

    for line in file:
      if (not line) or (line=='\n'):
        continue
      if printingS or printing:
        print file_index
      words = line.split()
      if printing:
        print words
      x = float(words[1])
      y = float(words[2])
      w = float(words[3])
      h = float(words[4])

      occ = int(words[5])
      if occ==1:    #Exclude occluded ground truth
        continue
      ground_total = ground_total + 1

      xmin = x
      xmax = x + w
      ymin = y
      ymax = y + h
      if printing:
        print "["+str(xmin)+","+str(ymin)+","+str(xmax)+","+str(ymax)+"]"

      flag = 0
      with open("hpu/"+test_files[file_index], 'r') as fileG:
        fileG.seek(0) #ensure you're at the start of the file..
        first_char = fileG.read(1) #get the first character
        if not first_char:
          #print "file is empty" #first character is the empty string..
          FN = FN + 1
          continue
        else:
          fileG.seek(0) #first character wasn't empty, return to start of file.


        for lineG in fileG:
          if (not lineG) or (lineG=='\n'):
            continue
          #print lineG
          wordsG = lineG.split()
          if printing:
            print wordsG
          xG = float(wordsG[0])
          yG = float(wordsG[1])
          wG = float(wordsG[2])
          hG = float(wordsG[3])

          xminG = xG
          xmaxG = xG + wG
          yminG = yG
          ymaxG = yG + hG
          if printing:
            print "["+str(xminG)+","+str(yminG)+","+str(xmaxG)+","+str(ymaxG)+"]"

          #Logic for this : http://stackoverflow.com/a/21220004
          SA = w * h
          SB = wG * hG
          #SI = max(0, max(xmax, xmaxG) - min(xmin, xminG)) * max(0, max(ymax, ymaxG) - min(ymin, yminG))
          SI = max(0, min(xmax, xmaxG) - max(xmin, xminG)) * max(0, min(ymax, ymaxG) - max(ymin, yminG))
          SU = SA + SB - SI
          S = SI / SU
          if printing:
            print "SA ="+str(SA)
            print "SB ="+str(SB)
            print "SI ="+str(SI)
            print "SU ="+str(SU)
          if printingS or printing:
            print "S ="+str(S)

          if S > acceptance:
            if printingS or printing:
              print ("Yes")
            ground_match = ground_match + 1
            flag = 1
            break

        if flag==0:
          if printingS or printing:
            print ("FN"+str(ground_files[file_index]))
          FN = FN + 1

precision = TP * 1.0 / (TP + FP)
recall    = TP * 1.0 / (TP + FN)
true_negative_rate = TN * 1.0 / (TN + FP)
accuracy = ((TP + TN) * 100.0) / (TP + TN + FP + FN)
#accuracy_other_formula = correct * 100.0 / total_detected
f_measure = 2*((precision*recall)/(precision + recall))

print "TP =", TP
print "FP =", FP
print "TN =", TN
print "FN =", FN
#print "Correct =", correct #(correct = TP)
print "Total detected =", total_detected
print "Accuracy =", accuracy
#print "Accuracy (non-standard) =", accuracy_other_formula
print "F-Measure =", f_measure
print "Ground Total =", ground_total
print "TP + FP + FN =", TP + FP + FN
#print "TP + FP =", TP + FP
#print "TP + FN =", TP + FN
#print "Ground Match =", ground_match