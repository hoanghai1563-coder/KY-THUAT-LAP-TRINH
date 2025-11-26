# gán mức lương cố định cho 1 giờ là 2.75
rate = float(input( "enterrate:"))
# cho người dùng nhập thời gian làm
hours= float(input("enterhours:"))
# tính tiền lương 
pay= (rate)*(hours)
luong=round(pay,2)
print("enterhours:", hours)
print ( " enterrate:", rate)
print (" Pay:", luong)