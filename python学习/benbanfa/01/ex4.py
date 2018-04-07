# -*- coding: utf-8 -*-
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print "这里有",cars, "量车"
print "这里只有",drivers,"个司机"
print "今天将会有",cars_not_driven, "量空车"
print "我们可以运送",carpool_capacity,"名乘客"
print "今天我们有",passengers,"名乘客"
print "我们需要将",average_passengers_per_car,"名乘客放入每辆车"